<#
  Installer for Lead Bot AU (Python app). Safe to run again. Never prints secret values.
  Flags:  -Check (look only)   -DryRun (say what it would do)   -Uninstall (remove Desktop shortcut only)   -NoPrompt (never ask for secrets)
#>
param([switch]$Check, [switch]$DryRun, [switch]$Uninstall, [switch]$NoPrompt)
$ErrorActionPreference = 'Continue'
$Root    = Split-Path -Parent $PSScriptRoot
$App     = Join-Path $Root 'app'
$Secrets = Join-Path $Root 'secrets'
$EnvFile = Join-Path $Secrets '.env'
$Venv    = Join-Path $App '.venv'
$VPy     = Join-Path $Venv 'Scripts\python.exe'
$Lnk     = Join-Path ([Environment]::GetFolderPath('Desktop')) 'Lead Bot AU (local test).lnk'
$bad = 0
function Ok($m){ Write-Host "OK      $m" -ForegroundColor Green }
function Miss($m){ Write-Host "MISSING $m" -ForegroundColor Yellow; $script:bad++ }
function Step($m,[scriptblock]$a){ if($DryRun){ Write-Host "[DRY]   $m" } else { Write-Host "...     $m"; & $a } }

if ($Uninstall) {
  if (Test-Path $Lnk) { Step "remove Desktop shortcut" { Remove-Item $Lnk -Force }; Write-Host "Shortcut removed. App, secrets and data are untouched." } else { Write-Host "No shortcut found." }
  exit 0
}

# 1. Python 3.10+
function Find-Py { foreach($c in 'python','py'){ $x = Get-Command $c -ErrorAction SilentlyContinue; if($x -and $x.Source -notmatch 'WindowsApps'){ return $x.Source } } return $null }
$py = Find-Py
if ($py) { Ok "Python found ($(& $py --version 2>&1))" } else { Miss "Python 3.12 (the installer adds it with winget)" }
$g = Get-Command git -ErrorAction SilentlyContinue
if ($g) { Ok "git found" } else { Write-Host "SKIP    git not found (only needed to push to GitHub; winget install Git.Git)" }
if (Test-Path (Join-Path $App 'src\leadbot.py')) { Ok "app\src\leadbot.py present" } else { Miss "app\src\leadbot.py (app folder incomplete)" }
if (Test-Path (Join-Path $Secrets 'SECRETS-CHECKLIST.md')) { Ok "secrets checklist present" } else { Miss "secrets\SECRETS-CHECKLIST.md" }
if (Test-Path $VPy) { Ok "virtual environment app\.venv" } else { Miss "virtual environment app\.venv (installer creates it)" }
if (Test-Path $EnvFile) { Ok "secrets\.env present" } else { Miss "secrets\.env (installer creates it from the checklist)" }
if ($Check) { Write-Host "Check done. Problems: $bad"; exit $bad }

# 2. Install Python if missing
if (-not $py) {
  Step "winget install Python 3.12" { winget install --id Python.Python.3.12 -e --accept-package-agreements --accept-source-agreements }
  $env:Path = [Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [Environment]::GetEnvironmentVariable('Path','User')
  $py = Find-Py
  if (-not $py -and -not $DryRun) { Write-Host "FAIL    Python still not found. Close this window, open a new one and run INSTALL.cmd again."; exit 1 }
}

# 3. Virtual environment + packages
if (-not (Test-Path $VPy)) { Step "create virtual environment app\.venv" { & $py -m venv $Venv } }
if (Test-Path $VPy) { Step "pip install -r requirements.txt" { & $VPy -m pip install --quiet --upgrade pip; & $VPy -m pip install --quiet -r (Join-Path $App 'requirements.txt') } }

# 4. secrets\.env (names only in the template; values asked with hidden input, Enter = skip)
$names = @('SHEET_ID_AU_ONLY','GOOGLE_SA','GEMINI_API_KEY_1','GEMINI_API_KEY_2','GEMINI_API_KEY_3','GROQ_API_KEY','CEREBRAS_API_KEY','OPENROUTER_API_KEY','MISTRAL_API_KEY','SERPER_API_KEY','HUNTER_API_KEY','GOOGLE_PLACES_API_KEY','YOUTUBE_API_KEY_1','YOUTUBE_API_KEY_2','APIFY_API_TOKEN','BRAVE_API_KEY','ABN_GUID','ZENROWS_API_KEY','JINA_API_KEY','APOLLO_API_KEY','PROSPEO_API_KEY','SNOV_CLIENT_ID','SNOV_CLIENT_SECRET','NZBN_API_KEY','ZEROBOUNCE_API_KEY','REACHER_URL','REACHER_SECRET')
function Get-EnvVal($n){ if(Test-Path $EnvFile){ $l = Get-Content $EnvFile | Where-Object { $_ -match "^\s*$n\s*=" } | Select-Object -First 1; if($l){ return ($l -replace "^\s*$n\s*=\s*",'').Trim() } } return '' }
function Set-EnvVal($n,$v){ $lines = @(); if(Test-Path $EnvFile){ $lines = @(Get-Content $EnvFile) }
  $hit = $false; $new = foreach($l in $lines){ if($l -match "^\s*$n\s*="){ $hit = $true; "$n=$v" } else { $l } }
  if(-not $hit){ $new = @($new) + "$n=$v" }; [IO.File]::WriteAllLines($EnvFile, [string[]]@($new)) }
if (-not (Test-Path $EnvFile)) { Step "create secrets\.env with empty values" { New-Item -ItemType Directory -Force $Secrets | Out-Null; [IO.File]::WriteAllLines($EnvFile, [string[]]($names | ForEach-Object { "$_=" })) } }
if ((Test-Path $EnvFile) -and -not $DryRun) {
  # Google robot account: point GOOGLE_SA at the .json key file in secrets\ (the bot accepts a file path)
  if (-not (Get-EnvVal 'GOOGLE_SA')) { $j = Get-ChildItem $Secrets -Filter *.json -ErrorAction SilentlyContinue | Select-Object -First 1; if($j){ Set-EnvVal 'GOOGLE_SA' $j.FullName; Ok "GOOGLE_SA set to the key file in secrets\" } else { Write-Host "TO DO   GOOGLE_SA: put the Google service-account .json file in secrets\ and run INSTALL.cmd again" } }
  $interactive = (-not $NoPrompt) -and [Environment]::UserInteractive -and (-not [Console]::IsInputRedirected)
  if ($interactive) {
    foreach($n in @('SHEET_ID_AU_ONLY','GEMINI_API_KEY_1')) { if (-not (Get-EnvVal $n)) {
      $s = Read-Host -AsSecureString "Paste $n (Enter to skip)"
      $v = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($s))
      if ($v) { Set-EnvVal $n $v; Ok "$n saved" } else { Write-Host "SKIP    $n" } } }
  }
}

# 5. Desktop shortcut = local test run (writes CSV files, no Google needed)
if (-not $DryRun) {
  $ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut($Lnk)
  $s.TargetPath = 'powershell.exe'; $s.Arguments = "-NoProfile -ExecutionPolicy Bypass -NoExit -File `"$PSScriptRoot\run-local.ps1`""
  $s.WorkingDirectory = $App; $s.Save(); Ok "Desktop shortcut 'Lead Bot AU (local test)'"
} else { Write-Host "[DRY]   create Desktop shortcut" }

# 6. Health check = the bot's own offline self-test
if ((Test-Path $VPy) -and -not $DryRun) {
  Push-Location $App
  & $VPy src\selftest.py 2>&1 | Select-Object -Last 3
  if ($LASTEXITCODE -eq 0) { Ok "self-test passed" } else { Write-Host "FAIL    self-test failed (see GUIDE\04-TROUBLESHOOTING.md)"; $bad++ }
  Pop-Location
}
Write-Host "Install finished. Next: fill the rest of secrets\.env (names in secrets\SECRETS-CHECKLIST.md) and add the same values as GitHub repo secrets. Then run: .\install.ps1 -Check"
