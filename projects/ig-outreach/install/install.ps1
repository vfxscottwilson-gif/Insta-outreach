<#
  ig-outreach installer (safe to re-run).  Run via install\INSTALL.cmd.
    -Check / -DryRun   show what would happen; change nothing
    -Uninstall         remove only the Desktop shortcut
    -SkipSecrets       do not ask for keys
  Prints no secret values. Network: winget (Python) and pip only.
#>
param([Alias('Check')][switch]$DryRun, [switch]$Uninstall, [switch]$SkipSecrets)
$ErrorActionPreference = 'Continue'
$Root    = Split-Path -Parent $PSScriptRoot
$App     = Join-Path $Root 'app'
$Sec     = Join-Path $Root 'secrets'
$Py      = Join-Path $App '.venv\Scripts\python.exe'
$EnvFile = Join-Path $Sec '.env'
$Lnk     = Join-Path ([Environment]::GetFolderPath('Desktop')) 'IG Send Assist.lnk'
$Results = New-Object System.Collections.ArrayList
function Note($s, $w, $d = '') { [void]$Results.Add([pscustomobject]@{S=$s;W=$w;D=$d}); Write-Host ("[{0}] {1} {2}" -f $s, $w, $d) }
function Have($c) { [bool](Get-Command $c -ErrorAction SilentlyContinue) }
function Refresh-Path { $env:Path = [Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [Environment]::GetEnvironmentVariable('Path','User') }
function Run-Step($label, [scriptblock]$act, $would) {
  if ($DryRun) { Note 'DRY' $label "would: $would"; return }
  try { $global:LASTEXITCODE = 0; & $act; if ($LASTEXITCODE -ne 0) { throw "exit code $LASTEXITCODE" }; Note 'OK' $label }
  catch { Note 'FAIL' $label $_.Exception.Message }
}

Write-Host "ig-outreach installer. Folder: $Root"
if ($DryRun) { Write-Host '*** DRY RUN: nothing will be changed ***' }

if ($Uninstall) {
  if (Test-Path $Lnk) { if ($DryRun) { Note 'DRY' 'Remove shortcut' $Lnk } else { Remove-Item $Lnk -Force; Note 'OK' 'Removed shortcut' } } else { Note 'SKIP' 'Shortcut not present' }
  Write-Host 'Only the shortcut was removed.'; exit 0
}

# 0. layout
if (-not (Test-Path (Join-Path $App 'main.py'))) { Note 'FAIL' 'Folder layout' "app\main.py missing. Copy the WHOLE ig-outreach folder."; exit 1 }
Note 'OK' 'Folder layout' 'app\main.py found'

# 1. Python 3.12
Refresh-Path
if (Have 'python') { Note 'OK' 'Python' ((& python --version 2>&1) -join '') }
elseif (-not (Have 'winget')) { Note 'FAIL' 'Python' 'missing and winget not available: install Python 3.12 from python.org, then re-run' }
else {
  Run-Step 'Install Python 3.12' { winget install --id Python.Python.3.12 -e --silent --accept-package-agreements --accept-source-agreements; Refresh-Path } 'winget install Python.Python.3.12'
  if (-not $DryRun -and -not (Have 'python')) { Note 'WARN' 'Python' 'installed but not on PATH yet: close this window and run INSTALL.cmd again' }
}

# 2. venv + packages
if (Test-Path $Py) { Note 'SKIP' 'Virtual env' 'app\.venv exists' }
elseif (Have 'python') { Run-Step 'Create virtual env' { python -m venv (Join-Path $App '.venv') } 'python -m venv app\.venv' }
if ($DryRun -or (Test-Path $Py)) {
  Run-Step 'pip install requirements' { & $Py -m pip install -q -r (Join-Path $App 'requirements.txt') } 'pip install -r app\requirements.txt'
}

# 3. secrets\.env  (asks one value at a time; Enter = skip; hidden input; values never printed)
$vars = @(
  @{N='SHEET_ID';       Secret=$false; Why='Google Sheet ID (text between /d/ and /edit in its URL)'},
  @{N='AI_API_KEYS';    Secret=$true;  Why='AI keys, comma separated (at least 2 providers)'},
  @{N='OFFER';          Secret=$false; Why='What you sell, one sentence'},
  @{N='IG_ACCESS_TOKEN';Secret=$true;  Why='Optional: Meta token for reading Instagram profiles'},
  @{N='IG_USER_ID';     Secret=$false; Why='Optional: Instagram business user id'}
)
if (-not (Test-Path $EnvFile)) {
  if ($DryRun) { Note 'DRY' 'Create secrets\.env' 'would ask for each value (Enter = skip)' }
  elseif ($SkipSecrets) { Set-Content $EnvFile ($vars | % { "$($_.N)=" }) -Encoding ASCII; Note 'SKIP' 'Secrets prompts' 'empty secrets\.env created; fill it in Notepad' }
  else {
    $lines = foreach ($v in $vars) {
      Write-Host "$($v.N): $($v.Why)  (Enter = skip)"
      if ($v.Secret) { $s = Read-Host -AsSecureString; $val = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($s)) } else { $val = Read-Host }
      "$($v.N)=$val"
    }
    Set-Content $EnvFile $lines -Encoding ASCII; Note 'OK' 'Create secrets\.env' 'written (values not shown)'
  }
} else { Note 'SKIP' 'secrets\.env' 'already exists (not touched)' }

# 4. Google service-account key
$key = Get-ChildItem $Sec -Filter '*.json' -ErrorAction SilentlyContinue | Select-Object -First 1
if ($key) { Note 'OK' 'Google key' "secrets\$($key.Name) found" } else { Note 'WARN' 'Google key' 'no .json key in secrets\: download it from Google Cloud (see SETUP-GUIDE.md section 2) and put it there' }

# 5. Health check (offline): packages import and code compiles
if (-not $DryRun -and (Test-Path $Py)) {
  Run-Step 'Health check (imports + compile)' { & $Py -c "import gspread, google.auth, requests; import py_compile,glob; [py_compile.compile(f,doraise=True) for f in glob.glob(r'$App\*.py')]" } 'import gspread/google.auth/requests and compile app\*.py'
}

# 6. Desktop shortcut
Run-Step 'Desktop shortcut "IG Send Assist"' {
  $l = (New-Object -ComObject WScript.Shell).CreateShortcut($Lnk)
  $l.TargetPath = Join-Path $PSScriptRoot 'run.cmd'; $l.Arguments = 'send_assist.py'; $l.WorkingDirectory = $App; $l.Save()
} "create $Lnk"

Write-Host "`n===== CHECKLIST ====="
$Results | % { Write-Host ("{0,-5} {1}  {2}" -f $_.S, $_.W, $_.D) }
$f = @($Results | ? { $_.S -eq 'FAIL' }).Count
if ($f) { Write-Host "$f step(s) FAILED. See GUIDE\04-TROUBLESHOOTING.md."; exit 1 }
Write-Host 'Done. Next: secrets\SECRETS-CHECKLIST.md, then install\run.cmd main.py --sync-only'
