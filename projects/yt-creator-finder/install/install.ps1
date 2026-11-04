<#
  YT Creator Finder: local installer (safe to re-run). Run via install\INSTALL.cmd. Flags:
    -Check / -DryRun   show what would happen; change nothing
    -Uninstall         remove only the Desktop shortcut
    -SkipKeys          do not ask for keys
  The bot itself runs in the cloud on GitHub Actions; this sets up a LOCAL copy for test runs (dry run).
  Prints no secret values. Keys are typed hidden and saved only to secrets\.env (then copied to app\.env).
#>
param([Alias('Check')][switch]$DryRun, [switch]$Uninstall, [switch]$SkipKeys)
$ErrorActionPreference = 'Continue'
$Root = Split-Path -Parent $PSScriptRoot
$App = Join-Path $Root 'app'; $Sec = Join-Path $Root 'secrets'
$Py = Join-Path $App '.venv\Scripts\python.exe'
$Lnk = Join-Path ([Environment]::GetFolderPath('Desktop')) 'YT Creator Finder (dry run).lnk'
$Results = New-Object System.Collections.ArrayList
function Note($s, $w, $d = '') { [void]$Results.Add([pscustomobject]@{ Status = $s; Step = $w; Detail = $d }); Write-Host ("[{0}] {1} {2}" -f $s, $w, $d) }
function Refresh-Path { $env:Path = [Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [Environment]::GetEnvironmentVariable('Path','User') }
function Have($c) { [bool](Get-Command $c -ErrorAction SilentlyContinue) }
function Run-Step($label, [scriptblock]$act, $would) {
  if ($DryRun) { Note 'DRY' $label "would: $would"; return }
  try { $global:LASTEXITCODE = 0; & $act; if ($LASTEXITCODE -and $LASTEXITCODE -ne 0) { throw "exit code $LASTEXITCODE" }; Note 'OK' $label }
  catch { Note 'FAIL' $label $_.Exception.Message }
}
Write-Host "YT Creator Finder installer. Folder: $Root"
if ($DryRun) { Write-Host '*** CHECK / DRY RUN: nothing will be changed ***' }

if ($Uninstall) {
  if (Test-Path $Lnk) { if ($DryRun) { Note 'DRY' 'Remove shortcut' $Lnk } else { Remove-Item $Lnk -Force; Note 'OK' 'Removed shortcut' $Lnk } } else { Note 'SKIP' 'Shortcut not present' $Lnk }
  Write-Host 'Only the shortcut was removed. Folder, GitHub repo and Google Sheet are untouched.'; exit 0
}
if (-not (Test-Path (Join-Path $App 'src\leadbot.py'))) { Note 'FAIL' 'Folder layout' "app\src\leadbot.py missing under $Root. Copy the WHOLE yt-creator-finder folder."; exit 1 }
Note 'OK' 'Folder layout' 'app\src found'

# 1. Python 3.12
Refresh-Path
if (Have 'python') { Note 'OK' 'Python' ((& python --version 2>&1) -join '') }
elseif (Have 'winget') { Run-Step 'Install Python 3.12' { winget install --id Python.Python.3.12 -e --silent --accept-package-agreements --accept-source-agreements; Refresh-Path } 'winget install Python.Python.3.12' }
else { Note 'FAIL' 'Python' 'missing and winget not available; install Python 3.12 from python.org' }
if (-not $DryRun -and -not (Have 'python')) { Note 'WARN' 'Python' 'installed but not on PATH yet: close this window and run INSTALL.cmd again' }

# 2. venv + requirements
if (Test-Path $Py) { Note 'SKIP' 'venv' 'app\.venv already exists' }
else { Run-Step 'Create venv' { & python -m venv (Join-Path $App '.venv') } 'python -m venv app\.venv' }
if ($DryRun) { Note 'DRY' 'pip install' 'would: pip install -r app\requirements.txt' }
elseif (Test-Path $Py) {
  & $Py -c "import gspread, pydantic, feedparser, yaml" 2>$null
  if ($LASTEXITCODE -eq 0) { Note 'SKIP' 'pip install' 'packages already installed' }
  else { Run-Step 'pip install requirements' { & $Py -m pip install --quiet -r (Join-Path $App 'requirements.txt') } 'pip install' }
}

# 3. Keys -> secrets\.env -> app\.env
$secEnv = Join-Path $Sec '.env'; $appEnv = Join-Path $App '.env'; $ex = Join-Path $App '.env.example'
if (-not (Test-Path $secEnv) -and (Test-Path $ex)) { Run-Step 'Create secrets\.env from template' { New-Item -ItemType Directory -Force $Sec | Out-Null; Copy-Item $ex $secEnv } 'copy app\.env.example to secrets\.env' }
if (-not $DryRun -and -not $SkipKeys -and (Test-Path $secEnv)) {
  $lines = [IO.File]::ReadAllLines($secEnv); $changed = $false
  foreach ($name in 'GOOGLE_SA','SHEET_ID','YOUTUBE_API_KEYS','GEMINI_API_KEYS','GROQ_API_KEYS','JINA_API_KEY','UPWORK_CLIENT_ID','UPWORK_CLIENT_SECRET','UPWORK_REFRESH_TOKEN') {
    $i = -1; for ($k = 0; $k -lt $lines.Count; $k++) { if ($lines[$k] -match "^\s*$name\s*=") { $i = $k; break } }
    $cur = if ($i -ge 0) { ($lines[$i] -replace "^\s*$name\s*=\s*", '').Trim() } else { '' }
    if ($cur) { continue }
    $hint = if ($name -eq 'GOOGLE_SA') { ' (type the PATH of the service-account .json file, or paste the JSON on one line)' } else { '' }
    $req = if ($name -in 'GOOGLE_SA','SHEET_ID','YOUTUBE_API_KEYS') { 'REQUIRED' } else { 'optional' }
    $ss = Read-Host "$name [$req]$hint. Enter to skip" -AsSecureString
    $val = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($ss))
    if (-not $val) { continue }
    if ($name -eq 'GOOGLE_SA' -and (Test-Path -LiteralPath $val -ErrorAction SilentlyContinue)) { $val = [Convert]::ToBase64String([IO.File]::ReadAllBytes($val)) }
    if ($i -ge 0) { $lines[$i] = "$name=$val" } else { $lines += "$name=$val" }
    $changed = $true
  }
  if ($changed) { [IO.File]::WriteAllLines($secEnv, $lines, (New-Object Text.UTF8Encoding($false))); Note 'OK' 'Saved keys' 'secrets\.env updated (values not shown)' }
  else { Note 'SKIP' 'Keys' 'nothing entered / already filled' }
}
if (Test-Path $secEnv) { Run-Step 'Copy secrets\.env to app\.env' { Copy-Item $secEnv $appEnv -Force } 'copy secrets\.env to app\.env (gitignored)' }
else { Note 'WARN' 'Keys' 'no secrets\.env yet' }

# 4. Health check: offline tests
if ($DryRun) { Note 'DRY' 'Tests' 'would run pytest (offline)' }
elseif (Test-Path $Py) {
  Push-Location $App; $out = (& $Py -m pytest -q 2>&1 | Out-String); $code = $LASTEXITCODE; Pop-Location
  Note $(if ($code -eq 0) { 'OK' } else { 'WARN' }) 'Offline tests' (($out -split "`r?`n" | Where-Object { $_.Trim() } | Select-Object -Last 1))
}

# 5. Shortcut (dry run: writes nothing to the Sheet)
$cmdArgs = '/k cd /d "' + $App + '" && ".venv\Scripts\python.exe" -m src.leadbot --dry-run --max-leads 10 --export "' + (Join-Path $Root 'proof\dryrun-leads.csv') + '"'
Run-Step 'Desktop shortcut (dry run)' {
  $l = (New-Object -ComObject WScript.Shell).CreateShortcut($Lnk); $l.TargetPath = "$env:WINDIR\System32\cmd.exe"; $l.Arguments = $cmdArgs
  $l.WorkingDirectory = $App; $l.Description = 'Test run of the YT creator lead bot (writes nothing to the Sheet)'; $l.Save()
} "create $Lnk"

Write-Host "`n===== CHECKLIST ====="
foreach ($r in $Results) { Write-Host ("{0,-5} {1}  {2}" -f $r.Status, $r.Step, $r.Detail) }
$fails = @($Results | Where-Object { $_.Status -eq 'FAIL' }).Count
if ($fails -gt 0) { Write-Host "$fails step(s) FAILED. See GUIDE\04-TROUBLESHOOTING.md."; exit 1 }
Write-Host 'Done. The real schedule runs on GitHub Actions: see SETUP-GUIDE.md section 7.'
