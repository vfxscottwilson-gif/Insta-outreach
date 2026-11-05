<#
  Database (Lead Dashboard) installer. Safe to re-run. Run via install\INSTALL.cmd. Flags:
    -DryRun / -Check   show what would happen; change nothing
    -Uninstall         remove only the Desktop + Start-menu shortcuts
    -WithPreview       also build the optional Vite design preview (app\web; needs Node)
    -RunTests          run the test suite at the end (327 tests expected; uses fake data only)
    -NoPrompt          never ask for secrets (unattended)
  Prints no secret values. Never reads Google Sheets: the health check uses local files only.
#>
param([Alias('Check')][switch]$DryRun, [switch]$Uninstall, [switch]$WithPreview, [switch]$RunTests, [switch]$NoPrompt)
$ErrorActionPreference = 'Continue'
$Root = Split-Path -Parent $PSScriptRoot
$App = Join-Path $Root 'app\dashboard'; $Web = Join-Path $Root 'app\web'; $Sec = Join-Path $Root 'secrets'
$Py = Join-Path $App '.venv\Scripts\python.exe'
$Launch = Join-Path $PSScriptRoot 'start-dashboard.cmd'
$LnkName = 'Database Dashboard.lnk'
$DeskLnk = Join-Path ([Environment]::GetFolderPath('Desktop')) $LnkName
$MenuLnk = Join-Path ([Environment]::GetFolderPath('Programs')) $LnkName
$Results = New-Object System.Collections.ArrayList
function Note($s, $w, $d = '') { [void]$Results.Add([pscustomobject]@{S=$s;W=$w;D=$d}); Write-Host ("[{0}] {1} {2}" -f $s, $w, $d) }
function Refresh-Path { $env:Path = [Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [Environment]::GetEnvironmentVariable('Path','User') }
function Have($c) { [bool](Get-Command $c -ErrorAction SilentlyContinue) }
function Run-Step($label, [scriptblock]$act, $would) {
  if ($DryRun) { Note 'DRY' $label "would: $would"; return $true }
  try { $global:LASTEXITCODE = 0; & $act; if ($LASTEXITCODE -ne 0) { throw "exit code $LASTEXITCODE" }; Note 'OK' $label; return $true }
  catch { Note 'FAIL' $label $_.Exception.Message; return $false }
}
function Make-Shortcut($p) {
  $l = (New-Object -ComObject WScript.Shell).CreateShortcut($p)
  $l.TargetPath = $Launch; $l.WorkingDirectory = $App; $l.Description = 'Start the Lead Dashboard'; $l.Save()
}
function Has-Key($file, $name) { (Test-Path $file) -and (Select-String -Path $file -Pattern "^\s*$name\s*=\s*\S" -Quiet) }
function Sync-File($from, $to) { if ((Test-Path $from) -and -not (Test-Path $to)) { Copy-Item $from $to } }

Write-Host "Lead Dashboard installer. Folder: $Root"
if ($DryRun) { Write-Host '*** DRY RUN: nothing will be changed ***' }

if ($Uninstall) {
  foreach ($p in @($DeskLnk, $MenuLnk)) {
    if (Test-Path $p) { if ($DryRun) { Note 'DRY' 'Remove shortcut' $p } else { Remove-Item $p -Force; Note 'OK' 'Removed shortcut' $p } }
    else { Note 'SKIP' 'Shortcut not present' $p }
  }
  Write-Host 'Only shortcuts were removed. Folder, database and secrets are untouched.'; exit 0
}

# 0. layout
if (-not (Test-Path (Join-Path $App 'manage.py'))) { Note 'FAIL' 'Folder layout' "app\dashboard\manage.py missing under $Root. Copy the WHOLE database folder."; exit 1 }
Note 'OK' 'Folder layout' 'app\dashboard found'

# 1. prerequisites
Refresh-Path
$need = @(@{N='Python 3.12'; C='python'; I='Python.Python.3.12'})
if ($WithPreview) { $need += @{N='Node.js LTS'; C='npm'; I='OpenJS.NodeJS.LTS'} }
foreach ($t in $need) {
  if (Have $t.C) { Note 'OK' $t.N 'already installed'; continue }
  if (-not (Have 'winget')) { Note 'FAIL' $t.N 'missing and winget not available (install "App Installer" from the Microsoft Store)'; continue }
  Run-Step "Install $($t.N)" { winget install --id $t.I -e --silent --accept-package-agreements --accept-source-agreements; Refresh-Path } "winget install $($t.I)" | Out-Null
  if (-not $DryRun -and -not (Have $t.C)) { Note 'WARN' $t.N 'installed but not on PATH: close this window and run INSTALL.cmd again' }
}

# 2. venv + packages
if (Test-Path $Py) { Note 'SKIP' 'Create venv' 'app\dashboard\.venv exists' }
else { Run-Step 'Create venv' { Push-Location $App; try { python -m venv .venv } finally { Pop-Location } } 'python -m venv app\dashboard\.venv' | Out-Null }
Run-Step 'pip install requirements' { Push-Location $App; try { & $Py -m pip install -q -r requirements.txt } finally { Pop-Location } } 'pip install -r requirements.txt' | Out-Null

# 3. secrets: secrets\.env is the master copy; app\dashboard\.env is the copy the app reads
$sEnv = Join-Path $Sec '.env'; $aEnv = Join-Path $App '.env'
New-Item -ItemType Directory -Force $Sec -ErrorAction SilentlyContinue | Out-Null
if (-not $DryRun) { Sync-File $sEnv $aEnv }
Run-Step 'Create keys + empty database (manage.py init)' { Push-Location $App; try { & $Py manage.py init | Out-Null } finally { Pop-Location } } 'manage.py init (adds DASH_SECRET_KEY / DASH_PASSWORD_KEY if missing; values not shown)' | Out-Null
if (-not $DryRun -and (Test-Path $aEnv)) {
  if (-not $NoPrompt) {
    foreach ($k in 'SMTP_USER','SMTP_PASSWORD','MAIL_FROM') {
      if (Has-Key $aEnv $k) { continue }
      $sec = Read-Host "$k for reset-code emails (Enter = skip; hidden)" -AsSecureString
      $v = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($sec))
      if ($v) { Add-Content -Path $aEnv -Value "$k=$v" -Encoding UTF8; Note 'OK' "Saved $k" '(value not shown)' } else { Note 'SKIP' $k 'left empty: reset codes print in the server window' }
    }
  }
  Copy-Item $aEnv $sEnv -Force; Note 'OK' 'secrets\.env' 'master copy refreshed from app\dashboard\.env'
}
foreach ($f in 'service_account.json','sources.yaml','categories.yaml') {
  $src = Join-Path $Sec $f
  if (Test-Path $src) { if (-not $DryRun) { Sync-File $src (Join-Path $App $f) }; Note 'OK' $f 'restored from secrets\' }
  elseif ($f -eq 'service_account.json') { Note 'SKIP' $f 'not in secrets\: needed only to read the real Google Sheets (see GUIDE\05)' }
  else { Note 'SKIP' $f 'optional' }
}

# 4. optional preview
if ($WithPreview -and (Have 'npm')) {
  if (Test-Path (Join-Path $Web 'node_modules')) { Note 'SKIP' 'npm ci (preview)' 'node_modules exists' }
  else { Run-Step 'npm ci (preview)' { Push-Location $Web; try { npm ci } finally { Pop-Location } } 'npm ci in app\web' | Out-Null }
  Run-Step 'Build preview' { Push-Location $Web; try { npm run build } finally { Pop-Location } } 'npm run build in app\web' | Out-Null
} else { Note 'SKIP' 'Design preview (app\web)' 'optional; use -WithPreview' }

# 5. health check (local only, no Google)
if ($DryRun) { Note 'DRY' 'Health check' 'would import the app and request /login locally' }
elseif (Test-Path $Py) {
  $code = "from dash import create_app; from dash.config import Config; a=create_app(Config.from_env()); r=a.test_client().get('/login'); print('login page HTTP', r.status_code); raise SystemExit(0 if r.status_code==200 else 1)"
  Push-Location $App; $o = (& $Py -c $code 2>&1 | Out-String).Trim(); $c = $LASTEXITCODE; Pop-Location
  Note $(if ($c -eq 0) {'OK'} else {'FAIL'}) 'Health check' ($o -split "`n" | Select-Object -Last 1)
}
if ($RunTests -and -not $DryRun -and (Test-Path $Py)) {
  Push-Location $App; $o = (& $Py -m pytest tests -q -p no:cacheprovider 2>&1 | Out-String); $c = $LASTEXITCODE; Pop-Location
  Note $(if ($c -eq 0) {'OK'} else {'FAIL'}) 'Test suite' (($o -split "`n" | Where-Object { $_.Trim() } | Select-Object -Last 1))
}

# 6. shortcuts
foreach ($p in @($DeskLnk, $MenuLnk)) { Run-Step "Shortcut $p" { Make-Shortcut $p } "create $p" | Out-Null }

Write-Host "`n===== CHECKLIST ====="
foreach ($r in $Results) { Write-Host ("{0,-5} {1}  {2}" -f $r.S, $r.W, $r.D) }
Write-Host 'TO DO (first time only): double-click install\create-admin.cmd to make your owner login.'
$fails = @($Results | Where-Object { $_.S -eq 'FAIL' }).Count
if ($fails -gt 0) { Write-Host "$fails step(s) FAILED. See GUIDE\04-TROUBLESHOOTING.md."; exit 1 }
Write-Host 'Done. Double-click "Database Dashboard" on the Desktop.'
