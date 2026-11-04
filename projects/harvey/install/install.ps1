<#
  Harvey: one-time installer (safe to re-run). Run via install\INSTALL.cmd. Flags:
    -Check / -DryRun   show what would happen; change nothing, install nothing
    -Uninstall         remove only the Desktop + Start-menu shortcuts
    -NoPrompt          never ask for keys (use secrets\.env as it is)
    -WithBrowser       also download the Playwright Chromium browser (~150 MB; only needed for LinkedIn / deep crawling)
    -RunTests          run Harvey's test suite after installing
  Prints no secret values. Network is used only by winget and pip (and Playwright with -WithBrowser).
#>
param([Alias('Check')][switch]$DryRun, [switch]$Uninstall, [switch]$NoPrompt, [switch]$WithBrowser, [switch]$RunTests)
$ErrorActionPreference = 'Continue'

$Root    = Split-Path -Parent $PSScriptRoot            # projects\harvey
$App     = Join-Path $Root 'app'                       # upstream clone (own .git), never edited by this script
$Private = Join-Path $Root 'secrets'
$VenvPy  = Join-Path $App '.venv\Scripts\python.exe'
$Launch  = Join-Path $PSScriptRoot 'Start Harvey Dashboard.cmd'
$LnkName = 'Harvey Dashboard.lnk'
$DeskLnk = Join-Path ([Environment]::GetFolderPath('Desktop')) $LnkName
$MenuLnk = Join-Path ([Environment]::GetFolderPath('Programs')) $LnkName
$Results = New-Object System.Collections.ArrayList

function Note($status, $what, $detail = '') { [void]$Results.Add([pscustomobject]@{ Status = $status; Step = $what; Detail = $detail }); Write-Host ("[{0}] {1} {2}" -f $status, $what, $detail) }
function Refresh-Path { $env:Path = [Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [Environment]::GetEnvironmentVariable('Path','User') }
function Have($cmd) { [bool](Get-Command $cmd -ErrorAction SilentlyContinue) }
function Run-Step($label, [scriptblock]$act, $wouldDo) {
  if ($DryRun) { Note 'DRY' $label "would: $wouldDo"; return $true }
  try { $global:LASTEXITCODE = 0; & $act; if ($LASTEXITCODE -and $LASTEXITCODE -ne 0) { throw "exit code $LASTEXITCODE" }; Note 'OK' $label; return $true }
  catch { Note 'FAIL' $label $_.Exception.Message; return $false }
}
# Returns a python.exe path that is 3.11+ (empty string if none)
function Find-Python {
  $cands = @()
  if (Have 'py') { foreach ($v in '3.13','3.12','3.11') { $p = (& py "-$v" -c "import sys;print(sys.executable)" 2>$null); if ($LASTEXITCODE -eq 0 -and $p) { $cands += $p.Trim() } } }
  if (Have 'python') { $cands += (Get-Command python).Source }
  foreach ($c in $cands) {
    if ($c -like '*WindowsApps*') { continue }   # Store stub, not a real Python
    $ok = (& $c -c "import sys;print(int(sys.version_info>=(3,11)))" 2>$null)
    if ($ok -eq '1') { return $c }
  }
  return ''
}
function Make-Shortcut($path) {
  $l = (New-Object -ComObject WScript.Shell).CreateShortcut($path)
  $l.TargetPath = $Launch; $l.WorkingDirectory = $App; $l.Description = 'Harvey dashboard'; $l.Save()
}

Write-Host "Harvey installer. Folder: $Root"
if ($DryRun) { Write-Host '*** CHECK / DRY RUN: nothing will be changed ***' }

# ---- Uninstall: shortcuts only ----
if ($Uninstall) {
  foreach ($p in @($DeskLnk, $MenuLnk)) {
    if (Test-Path $p) { if ($DryRun) { Note 'DRY' 'Remove shortcut' $p } else { Remove-Item $p -Force; Note 'OK' 'Removed shortcut' $p } }
    else { Note 'SKIP' 'Shortcut not present' $p }
  }
  Write-Host 'Only shortcuts were removed. The folder, .venv, data and keys are untouched.'; exit 0
}

# ---- 0. Sanity ----
if (-not (Test-Path (Join-Path $App 'pyproject.toml')) -or -not (Test-Path (Join-Path $App 'harvey'))) { Note 'FAIL' 'Folder layout' "app\pyproject.toml or app\harvey missing under $Root. Copy the WHOLE harvey folder."; exit 1 }
Note 'OK' 'Folder layout' 'app\pyproject.toml and app\harvey found'

# ---- 1. Prerequisites ----
Refresh-Path
$py = Find-Python
if ($py) { Note 'OK' 'Python 3.11+' $py }
elseif (Have 'winget') {
  Run-Step 'Install Python 3.12' { winget install --id Python.Python.3.12 -e --silent --accept-package-agreements --accept-source-agreements; Refresh-Path } 'winget install Python.Python.3.12' | Out-Null
  if (-not $DryRun) { $py = Find-Python; if (-not $py) { Note 'WARN' 'Python' 'installed but not on PATH yet: close this window and run INSTALL.cmd again' } }
} else { Note 'FAIL' 'Python 3.11+' 'missing and winget not available. Install App Installer from the Microsoft Store (or Python from python.org), then re-run.' }

if (Have 'claude') { Note 'OK' 'Claude CLI' 'found (Harvey needs it: it is the AI brain)' }
else { Note 'WARN' 'Claude CLI' 'not found. Needed to RUN Harvey (not to install). Install: npm install -g @anthropic-ai/claude-code (needs Node.js), then run: claude login' }
if (Have 'git') { Note 'OK' 'Git' 'present (optional)' } else { Note 'SKIP' 'Git' 'not installed (optional; only for updating Harvey from upstream)' }

# ---- 2. venv + pip install -e ----
if (Test-Path $VenvPy) { Note 'SKIP' 'Create venv' 'app\.venv already exists' }
elseif ($py -or $DryRun) { Run-Step 'Create venv (app\.venv)' { & $py -m venv (Join-Path $App '.venv') } 'python -m venv app\.venv' | Out-Null }
else { Note 'FAIL' 'Create venv' 'no Python' }

$harveyExe = Join-Path $App '.venv\Scripts\harvey.exe'
if (Test-Path $harveyExe) { Note 'SKIP' 'pip install -e' 'harvey already installed in the venv (to refresh: delete app\.venv and re-run)' }
elseif ($DryRun -or (Test-Path $VenvPy)) {
  Run-Step 'pip install -e ".[dev]"' { Push-Location $App; try { & $VenvPy -m pip install --upgrade pip --quiet; & $VenvPy -m pip install -e ".[dev]" --quiet } finally { Pop-Location } } 'pip install -e ".[dev]" in app\.venv' | Out-Null
} else { Note 'FAIL' 'pip install' 'venv missing' }

if ($WithBrowser) {
  Run-Step 'Playwright Chromium' { & $VenvPy -m playwright install chromium } 'python -m playwright install chromium' | Out-Null
} else { Note 'SKIP' 'Playwright Chromium' 'not needed unless you use LinkedIn / deep crawling (re-run with -WithBrowser)' }

# ---- 3. Keys: secrets\.env is the master copy; app\.env is what Harvey reads ----
$privEnv = Join-Path $Private '.env'; $appEnv = Join-Path $App '.env'; $envEx = Join-Path $App '.env.example'
function Set-EnvValue($file, $name, $value) {
  $lines = [IO.File]::ReadAllLines($file); $hit = $false
  for ($i = 0; $i -lt $lines.Count; $i++) { if ($lines[$i] -match "^\s*$name\s*=") { $lines[$i] = "$name=$value"; $hit = $true; break } }
  if (-not $hit) { $lines += "$name=$value" }
  [IO.File]::WriteAllLines($file, $lines, (New-Object Text.UTF8Encoding($false)))
}
if (-not (Test-Path $privEnv)) {
  if ($DryRun) { Note 'DRY' 'Create secrets\.env' 'would: copy app\.env.example to secrets\.env, then ask for keys (hidden input)' }
  elseif (Test-Path $envEx) {
    Run-Step 'Create secrets\.env from template' { New-Item -ItemType Directory -Force $Private | Out-Null; Copy-Item $envEx $privEnv } '' | Out-Null
    # Ask for keys (hidden input; Enter = skip). Only on a fresh .env, only when interactive.
    if (-not $NoPrompt -and [Environment]::UserInteractive) {
      Write-Host "`nKeys: press Enter to skip any. Nothing is shown or logged. Which ones you need: secrets\SECRETS-CHECKLIST.md"
      foreach ($n in 'SMTP_HOST','SMTP_USERNAME','SMTP_PASSWORD','GMAIL_CLIENT_ID','GMAIL_CLIENT_SECRET','INSTANTLY_API_KEY','REOON_API_KEY','ZEROBOUNCE_API_KEY','HUNTER_API_KEY','TRULYINBOX_API_KEY') {
        $s = Read-Host -Prompt $n -AsSecureString
        $v = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($s))
        if ($v) { Set-EnvValue $privEnv $n $v }
      }
      Note 'OK' 'Keys entered' 'saved to secrets\.env (values not shown)'
    } else { Note 'SKIP' 'Key prompts' '-NoPrompt: edit secrets\.env later (names in SECRETS-CHECKLIST.md)' }
  } else { Note 'FAIL' 'secrets\.env' 'no .env and no app\.env.example' }
} else { Note 'SKIP' 'secrets\.env' 'already exists (not touched)' }
if (Test-Path $privEnv) {
  if (-not (Test-Path $appEnv)) { Run-Step 'Copy secrets\.env to app\.env' { Copy-Item $privEnv $appEnv } 'copy secrets\.env to app\.env' | Out-Null }
  elseif ((Get-FileHash $privEnv).Hash -ne (Get-FileHash $appEnv).Hash) { Note 'WARN' 'app\.env differs from secrets\.env' 'not overwritten. If secrets\.env is the right one, delete app\.env and re-run.' }
  else { Note 'SKIP' 'app\.env' 'same as secrets\.env' }
}

# ---- 4. Health check (no network, no keys needed) ----
if ($DryRun) { Note 'SKIP' 'Health check' 'dry run' }
elseif (Test-Path $VenvPy) {
  $out = (& $VenvPy -c "import harvey, harvey.cli; print('import ok')" 2>&1 | Out-String).Trim()
  Note $(if ($out -match 'import ok') { 'OK' } else { 'FAIL' }) 'Health check: import harvey' (($out -split "`n") | Select-Object -Last 1)
  $h = (& $harveyExe --help 2>&1 | Out-String); Note $(if ($LASTEXITCODE -eq 0) { 'OK' } else { 'FAIL' }) 'Health check: harvey --help' "exit code $LASTEXITCODE"
} else { Note 'FAIL' 'Health check' 'venv missing' }

# ---- 5. Tests (optional) ----
if ($RunTests -and -not $DryRun -and (Test-Path $VenvPy)) {
  Push-Location $App; & $VenvPy -m pytest -q tests 2>&1 | Select-Object -Last 8 | ForEach-Object { Write-Host $_ }; $tc = $LASTEXITCODE; Pop-Location
  Note $(if ($tc -eq 0) { 'OK' } else { 'FAIL' }) 'Test suite' "exit code $tc"
}

# ---- 6. Shortcuts ----
foreach ($p in @($DeskLnk, $MenuLnk)) { Run-Step "Shortcut $p" { Make-Shortcut $p } "create $p (opens the Harvey dashboard)" | Out-Null }

# ---- Checklist ----
Write-Host "`n===== CHECKLIST ====="
foreach ($r in $Results) { Write-Host ("{0,-5} {1}  {2}" -f $r.Status, $r.Step, $r.Detail) }
$fails = @($Results | Where-Object { $_.Status -eq 'FAIL' }).Count
if ($fails -gt 0) { Write-Host "$fails step(s) FAILED. See GUIDE\04-TROUBLESHOOTING.md."; exit 1 }
Write-Host 'Done. Next: GUIDE\00-START-HERE.md (log in to Claude, add keys, train Harvey).'
