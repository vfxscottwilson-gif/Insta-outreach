<#
  Outreach app: one-time installer (safe to re-run).
  Run via install\INSTALL.cmd. Flags:
    -DryRun / -Check   show what would happen; change nothing, install nothing
    -Uninstall         remove only the Desktop + Start-menu shortcuts
    -SkipHealthcheck   do not contact the database at the end
  Prints no secret values. Network is used only by winget / npm / uv (package installs) and the final healthcheck.
#>
param([Alias('Check')][switch]$DryRun, [switch]$Uninstall, [switch]$SkipHealthcheck)
$ErrorActionPreference = 'Continue'

$Root    = Split-Path -Parent $PSScriptRoot            # projects\email-automation
$App     = Join-Path $Root 'app'                       # the git repo (kept name 'app')
$Web     = Join-Path $App 'web'
$Engine  = Join-Path $App 'engine'
$Private = Join-Path $Root 'secrets'
$Launch  = Join-Path $App 'Start Outreach App.vbs'
$LnkName = 'Outreach.lnk'
$Desktop = [Environment]::GetFolderPath('Desktop')
$StartMenu = Join-Path ([Environment]::GetFolderPath('Programs')) $LnkName
$DeskLnk = Join-Path $Desktop $LnkName
$Results = New-Object System.Collections.ArrayList

function Note($status, $what, $detail = '') { [void]$Results.Add([pscustomobject]@{ Status = $status; Step = $what; Detail = $detail }) ; Write-Host ("[{0}] {1} {2}" -f $status, $what, $detail) }
function Refresh-Path { $env:Path = [Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [Environment]::GetEnvironmentVariable('Path','User') }
function Have($cmd) { [bool](Get-Command $cmd -ErrorAction SilentlyContinue) }
function Run-Step($label, [scriptblock]$act, $wouldDo) {
  if ($DryRun) { Note 'DRY' $label "would: $wouldDo"; return $true }
  try { $global:LASTEXITCODE = 0; & $act; if ($LASTEXITCODE -and $LASTEXITCODE -ne 0) { throw "exit code $LASTEXITCODE" }; Note 'OK' $label; return $true }
  catch { Note 'FAIL' $label $_.Exception.Message; return $false }
}

function Make-Shortcut($path) {
  $sh = New-Object -ComObject WScript.Shell
  $l = $sh.CreateShortcut($path)
  $l.TargetPath = "$env:WINDIR\System32\wscript.exe"
  $l.Arguments = '"' + $Launch + '"'
  $l.WorkingDirectory = $App
  $ico = Join-Path $Web 'public\favicon.ico'; if (Test-Path $ico) { $l.IconLocation = "$ico,0" }
  $l.Description = 'Outreach app'
  $l.Save()
}

Write-Host "Outreach installer. Folder: $Root"
if ($DryRun) { Write-Host '*** DRY RUN: nothing will be changed ***' }

# ---- Uninstall: shortcuts only ----
if ($Uninstall) {
  foreach ($p in @($DeskLnk, $StartMenu)) {
    if (Test-Path $p) { if ($DryRun) { Note 'DRY' 'Remove shortcut' $p } else { Remove-Item $p -Force; Note 'OK' 'Removed shortcut' $p } }
    else { Note 'SKIP' 'Shortcut not present' $p }
  }
  Write-Host 'Only shortcuts were removed. The folder, database and cloud are untouched.'; exit 0
}

# ---- 0. Sanity ----
if (-not (Test-Path $App) -or -not (Test-Path $Web) -or -not (Test-Path $Engine)) { Note 'FAIL' 'Folder layout' "app\web or app\engine missing under $Root. Copy the WHOLE email-automation folder."; exit 1 }
Note 'OK' 'Folder layout' 'app\web and app\engine found'

# ---- 1. Prerequisites ----
Refresh-Path
$hasWinget = Have 'winget'
$pre = @(
  @{ Name='Node.js LTS'; Cmd='node'; Id='OpenJS.NodeJS.LTS' },
  @{ Name='Python 3.12'; Cmd='python'; Id='Python.Python.3.12' },
  @{ Name='uv';          Cmd='uv';     Id='astral-sh.uv' },
  @{ Name='Git';         Cmd='git';    Id='Git.Git' }
)
foreach ($t in $pre) {
  if (Have $t.Cmd) { Note 'OK' $t.Name 'already installed'; continue }
  if (-not $hasWinget) { Note 'FAIL' $t.Name 'missing and winget not available. Install App Installer from the Microsoft Store, then re-run.'; continue }
  Run-Step "Install $($t.Name)" { winget install --id $t.Id -e --silent --accept-package-agreements --accept-source-agreements; Refresh-Path } "winget install $($t.Id)" | Out-Null
  if (-not $DryRun -and -not (Have $t.Cmd)) { Note 'WARN' $t.Name 'installed but not on PATH yet: close this window and run INSTALL.cmd again' }
}
$edge = @("${env:ProgramFiles(x86)}\Microsoft\Edge\Application\msedge.exe", "$env:ProgramFiles\Microsoft\Edge\Application\msedge.exe") | Where-Object { Test-Path $_ }
if ($edge) { Note 'OK' 'Microsoft Edge' 'present (app window)' } else { Note 'WARN' 'Microsoft Edge' 'not found; Chrome or the default browser will be used' }
if (Have 'python') { $pv = (& python --version 2>&1) -join ''; if ($pv -notmatch '3\.1[2-9]') { Note 'WARN' 'Python version' "$pv (engine needs 3.12+); uv will fetch its own if needed" } }

# ---- 2. Web: npm install + build ----
if (Have 'npm') {
  if (Test-Path (Join-Path $Web 'node_modules')) { Note 'SKIP' 'npm install' 'node_modules already present' }
  else { Run-Step 'npm install (web)' { Push-Location $Web; try { npm install --ignore-scripts } finally { Pop-Location } } 'npm install --ignore-scripts in app\web' | Out-Null }
  if (Test-Path (Join-Path $Web 'dist\index.html')) { Note 'SKIP' 'Build web app' 'dist\index.html already exists (the launcher rebuilds when code changes)' }
  else { Run-Step 'Build web app' { Push-Location $Web; try { npm run build } finally { Pop-Location } } 'npm run build in app\web' | Out-Null }
} else { Note 'FAIL' 'Web steps' 'npm not available' }

# ---- 3. Engine: uv sync ----
if (Have 'uv') {
  if (Test-Path (Join-Path $Engine '.venv')) { Note 'SKIP' 'uv sync' '.venv already present' }
  else { Run-Step 'uv sync (engine)' { Push-Location $Engine; try { uv sync } finally { Pop-Location } } 'uv sync in app\engine' | Out-Null }
} else { Note 'FAIL' 'Engine steps' 'uv not available' }

# ---- 4. Keys (.env) ----
$envFile = Join-Path $App '.env'; $envEx = Join-Path $App '.env.example'; $privEnv = Join-Path $Private '.env'
$needNotepad = $false
if (Test-Path $envFile) { Note 'SKIP' '.env' 'app\.env already exists (not touched)' }
elseif (Test-Path $privEnv) { Run-Step 'Restore .env' { Copy-Item $privEnv $envFile } 'copy secrets\.env to app\.env' | Out-Null }
elseif (Test-Path $envEx) { Run-Step 'Create .env from template' { Copy-Item $envEx $envFile; $script:needNotepad = $true } 'copy .env.example to app\.env, open Notepad' | Out-Null }
else { Note 'FAIL' '.env' 'no secrets\.env and no .env.example' }

# ---- 5. Google service-account key -> %USERPROFILE%\.secrets, then fix GOOGLE_SA_JSON ----
$key = Get-ChildItem $Private -Filter '*.json' -ErrorAction SilentlyContinue | Select-Object -First 1
if ($key -and (Test-Path $envFile)) {
  $dstDir = Join-Path $env:USERPROFILE '.secrets'; $dst = Join-Path $dstDir $key.Name
  $lines = [IO.File]::ReadAllLines($envFile)
  $idx = -1; for ($i = 0; $i -lt $lines.Count; $i++) { if ($lines[$i] -match '^\s*GOOGLE_SA_JSON\s*=') { $idx = $i; break } }
  $cur = if ($idx -ge 0) { ($lines[$idx] -replace '^\s*GOOGLE_SA_JSON\s*=\s*', '').Trim('"', "'", ' ') } else { '' }
  if ($cur -and (Test-Path $cur)) { Note 'SKIP' 'Google key' 'GOOGLE_SA_JSON already points to an existing file' }
  else {
    Run-Step 'Restore Google key' {
      New-Item -ItemType Directory -Force $dstDir | Out-Null
      if (-not (Test-Path $dst)) { Copy-Item $key.FullName $dst }
      if ($idx -ge 0) { $lines[$idx] = "GOOGLE_SA_JSON=$dst" } else { $lines += "GOOGLE_SA_JSON=$dst" }
      [IO.File]::WriteAllLines($envFile, $lines, (New-Object Text.UTF8Encoding($false)))
    } "copy secrets\$($key.Name) to $dstDir and set GOOGLE_SA_JSON in app\.env" | Out-Null
  }
} else { Note 'SKIP' 'Google key' 'no key file in secrets\ (only needed to read the lead Google Sheets)' }

# ---- 6. Healthcheck ----
if ($SkipHealthcheck -or $DryRun) { Note 'SKIP' 'Engine healthcheck' $(if ($DryRun) { 'dry run' } else { 'skipped by flag' }) }
elseif (-not (Test-Path $envFile) -or $needNotepad) { Note 'SKIP' 'Engine healthcheck' 'fill in app\.env first, then re-run INSTALL.cmd' }
elseif (Have 'uv') {
  Push-Location $Engine
  $out = (& uv run python -m outreach healthcheck 2>&1 | Out-String); $code = $LASTEXITCODE
  Pop-Location
  $tail = ($out -split "`r?`n" | Where-Object { $_.Trim() } | Select-Object -Last 12) -join "`n"
  Note $(if ($code -eq 0) { 'OK' } else { 'WARN' }) 'Engine healthcheck' "exit code $code (lines below; some items, e.g. postal address, are the owner's to-do)"
  Write-Host $tail
}

# ---- 7. Shortcuts ----
foreach ($p in @($DeskLnk, $StartMenu)) {
  if (Test-Path $p) { Run-Step "Refresh shortcut $([IO.Path]::GetFileName((Split-Path $p -Parent)))" { Make-Shortcut $p } "re-point $p at this folder" | Out-Null }
  else { Run-Step "Create shortcut ($p)" { Make-Shortcut $p } "create $p" | Out-Null }
}

# ---- 8. Notepad for a fresh .env ----
if ($needNotepad -and -not $DryRun) { Start-Process notepad.exe $envFile }

# ---- Checklist ----
Write-Host "`n===== CHECKLIST ====="
foreach ($r in $Results) { Write-Host ("{0,-5} {1}  {2}" -f $r.Status, $r.Step, $r.Detail) }
$fails = @($Results | Where-Object { $_.Status -eq 'FAIL' }).Count
if ($needNotepad) { Write-Host "TO DO: Notepad opened app\.env. Paste each key after '=', save, then run INSTALL.cmd again." }
if ($fails -gt 0) { Write-Host "$fails step(s) FAILED. See guide GUIDE\04-TROUBLESHOOTING.md." ; exit 1 }
Write-Host 'Done. Double-click "Outreach" on the Desktop to open the app.'
