<#
  local-drafter: one-time installer (safe to re-run).
  Run via install\INSTALL.cmd. Flags:
    -Check / -DryRun   show what would happen; change nothing, install nothing
    -Uninstall         remove only the Desktop shortcut
    -SkipModel         do not install Ollama or pull the model (used in tests)
    -SkipTests         do not run pytest at the end
    -NonInteractive    never prompt (no secret questions, model pull is skipped with a note)
  Prints no secret values. Network is used only by winget / pip / ollama pull.
#>
param([Alias('Check')][switch]$DryRun, [switch]$Uninstall, [switch]$SkipModel, [switch]$SkipTests, [switch]$NonInteractive)
$ErrorActionPreference = 'Continue'

$Root    = Split-Path -Parent $PSScriptRoot            # projects\local-drafter
$App     = Join-Path $Root 'app'
$Secrets = Join-Path $Root 'secrets'
$Venv    = Join-Path $App '.venv'
$VPy     = Join-Path $Venv 'Scripts\python.exe'
$Model   = 'qwen3:8b'
$LnkName = 'Local Drafter.lnk'
$DeskLnk = Join-Path ([Environment]::GetFolderPath('Desktop')) $LnkName
$Results = New-Object System.Collections.ArrayList

function Note($status, $what, $detail = '') { [void]$Results.Add([pscustomobject]@{ Status = $status; Step = $what; Detail = $detail }); Write-Host ("[{0}] {1} {2}" -f $status, $what, $detail) }
function Refresh-Path { $env:Path = [Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [Environment]::GetEnvironmentVariable('Path','User') }
function Have($cmd) { [bool](Get-Command $cmd -ErrorAction SilentlyContinue) }
function Run-Step($label, [scriptblock]$act, $wouldDo) {
  if ($DryRun) { Note 'DRY' $label "would: $wouldDo"; return $true }
  try { $global:LASTEXITCODE = 0; & $act; if ($LASTEXITCODE -and $LASTEXITCODE -ne 0) { throw "exit code $LASTEXITCODE" }; Note 'OK' $label; return $true }
  catch { Note 'FAIL' $label $_.Exception.Message; return $false }
}
function Read-Secret($prompt) {
  $s = Read-Host -AsSecureString $prompt
  $b = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($s)
  try { return [Runtime.InteropServices.Marshal]::PtrToStringBSTR($b) } finally { [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($b) }
}
function Set-EnvLine($file, $name, $value) {
  $lines = @(); if (Test-Path $file) { $lines = [IO.File]::ReadAllLines($file) }
  $idx = -1; for ($i = 0; $i -lt $lines.Count; $i++) { if ($lines[$i] -match "^\s*$name\s*=") { $idx = $i; break } }
  if ($idx -ge 0) { $lines[$idx] = "$name=$value" } else { $lines += "$name=$value" }
  [IO.File]::WriteAllLines($file, $lines, (New-Object Text.UTF8Encoding($false)))
}

Write-Host "local-drafter installer. Folder: $Root"
if ($DryRun) { Write-Host '*** DRY RUN: nothing will be changed ***' }

# ---- Uninstall: shortcut only ----
if ($Uninstall) {
  if (Test-Path $DeskLnk) { if ($DryRun) { Note 'DRY' 'Remove shortcut' $DeskLnk } else { Remove-Item $DeskLnk -Force; Note 'OK' 'Removed shortcut' $DeskLnk } }
  else { Note 'SKIP' 'Shortcut not present' $DeskLnk }
  Write-Host 'Only the shortcut was removed. Python, Ollama, the model and this folder are untouched.'; exit 0
}

# ---- 0. Sanity ----
if (-not (Test-Path (Join-Path $App 'draft_emails.py'))) { Note 'FAIL' 'Folder layout' "app\draft_emails.py missing under $Root. Copy the WHOLE local-drafter folder."; exit 1 }
Note 'OK' 'Folder layout' 'app\draft_emails.py found'

# ---- 1. Prerequisites ----
Refresh-Path
$hasWinget = Have 'winget'
$pre = @(
  @{ Name='Python 3.12'; Cmd='python'; Id='Python.Python.3.12' },
  @{ Name='Ollama';      Cmd='ollama'; Id='Ollama.Ollama' }
)
foreach ($t in $pre) {
  if ($SkipModel -and $t.Cmd -eq 'ollama') { Note 'SKIP' $t.Name 'skipped by -SkipModel (NOT installed by this run)'; continue }
  if (Have $t.Cmd) { Note 'OK' $t.Name 'already installed'; continue }
  if ($t.Cmd -eq 'ollama' -and (Test-Path "$env:LOCALAPPDATA\Programs\Ollama\ollama.exe")) { $env:Path += ";$env:LOCALAPPDATA\Programs\Ollama"; Note 'OK' $t.Name 'installed (added to PATH for this run)'; continue }
  if (-not $hasWinget) { Note 'FAIL' $t.Name 'missing and winget not available. Install "App Installer" from the Microsoft Store, then re-run.'; continue }
  Run-Step "Install $($t.Name)" { winget install --id $t.Id -e --silent --accept-package-agreements --accept-source-agreements; Refresh-Path } "winget install $($t.Id)" | Out-Null
  if (-not $DryRun -and -not (Have $t.Cmd)) { Note 'WARN' $t.Name 'installed but not on PATH yet: close this window and run INSTALL.cmd again' }
}
if (Have 'python') { $pv = (& python --version 2>&1) -join ''; if ($pv -notmatch '3\.(1[0-9])') { Note 'WARN' 'Python version' "$pv (needs 3.10 or newer)" } }
if (Have 'nvidia-smi') { Note 'OK' 'NVIDIA GPU' 'nvidia-smi found' } else { Note 'WARN' 'NVIDIA GPU' 'nvidia-smi not found: the model will run on the CPU (slow)' }

# ---- 2. Model (large download: ask first) ----
if ($SkipModel) { Note 'SKIP' "Model $Model" 'skipped by -SkipModel (the model is NOT installed by this run)' }
elseif (-not (Have 'ollama')) { Note 'SKIP' "Model $Model" 'ollama not available yet' }
else {
  $have = (& ollama list 2>$null) -join "`n"
  if ($have -match [regex]::Escape($Model)) { Note 'SKIP' "Model $Model" 'already pulled' }
  elseif ($DryRun) { Note 'DRY' "Model $Model" 'would ask, then run: ollama pull qwen3:8b (about 5.2 GB download)' }
  elseif ($NonInteractive) { Note 'WARN' "Model $Model" 'not installed; run later:  ollama pull qwen3:8b  (about 5.2 GB)' }
  else {
    $a = Read-Host "Download the AI model qwen3:8b now? It is about 5.2 GB. (y/N)"
    if ($a -match '^[yY]') { Run-Step "ollama pull $Model" { & ollama pull $Model } "ollama pull $Model" | Out-Null }
    else { Note 'WARN' "Model $Model" 'skipped by you; run later:  ollama pull qwen3:8b' }
  }
}

# ---- 3. Python venv + packages ----
if (Test-Path $VPy) { Note 'SKIP' 'Virtual environment' 'app\.venv already exists' }
elseif (Have 'python') { Run-Step 'Create virtual environment' { & python -m venv $Venv } 'python -m venv app\.venv' | Out-Null }
else { Note 'FAIL' 'Virtual environment' 'python not available' }
if ($DryRun) { Note 'DRY' 'pip install' 'would: app\.venv\Scripts\python -m pip install -r requirements.txt' }
elseif (Test-Path $VPy) {
  Run-Step 'pip install -r requirements.txt' { & $VPy -m pip install --disable-pip-version-check -q -r (Join-Path $App 'requirements.txt') } '' | Out-Null
}

# ---- 4. Secrets (.env) in secrets\, copied to app\.env ----
$secEnv = Join-Path $Secrets '.env'; $appEnv = Join-Path $App '.env'; $envEx = Join-Path $App '.env.example'
if (-not (Test-Path $secEnv)) {
  if ($DryRun) { Note 'DRY' 'secrets\.env' 'would create from app\.env.example' }
  elseif (Test-Path $envEx) {
    New-Item -ItemType Directory -Force $Secrets | Out-Null
    Copy-Item $envEx $secEnv
    $sa = Get-ChildItem $Secrets -Filter '*.json' -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($sa) { Set-EnvLine $secEnv 'GOOGLE_SERVICE_ACCOUNT_FILE' $sa.FullName; Note 'OK' 'GOOGLE_SERVICE_ACCOUNT_FILE' "set to the JSON key found in secrets\ ($($sa.Name))" }
    elseif (-not $NonInteractive) {
      $p = (Read-Host 'Full path of your Google service-account JSON key (Enter = skip; file mode works without it)').Trim('"')
      if ($p -and (Test-Path $p)) { Copy-Item $p $Secrets; Set-EnvLine $secEnv 'GOOGLE_SERVICE_ACCOUNT_FILE' (Join-Path $Secrets (Split-Path $p -Leaf)); Note 'OK' 'Service-account key' 'copied into secrets\' }
      else { Set-EnvLine $secEnv 'GOOGLE_SERVICE_ACCOUNT_FILE' ''; Note 'SKIP' 'Service-account key' 'not provided (only needed for Google Sheet mode)' }
    } else { Set-EnvLine $secEnv 'GOOGLE_SERVICE_ACCOUNT_FILE' ''; Note 'SKIP' 'Service-account key' 'non-interactive; add later' }
    if (-not $NonInteractive) {
      foreach ($n in @('YOUTUBE_API_KEY','AI_API_KEY')) {
        $v = Read-Secret "$n (optional, hidden input, Enter = skip)"
        if ($v) { Set-EnvLine $secEnv $n $v; Note 'OK' $n 'saved to secrets\.env' } else { Note 'SKIP' $n 'left empty' }
      }
    }
    Note 'OK' 'secrets\.env' 'created (values are never printed)'
  } else { Note 'FAIL' 'secrets\.env' 'no app\.env.example found' }
} else { Note 'SKIP' 'secrets\.env' 'already exists (not touched)' }
if (Test-Path $secEnv) {
  if ($DryRun) { Note 'DRY' 'app\.env' 'would copy secrets\.env to app\.env' }
  else { Copy-Item $secEnv $appEnv -Force; Note 'OK' 'app\.env' 'copied from secrets\.env (edit secrets\.env, then re-run the installer to refresh)' }
}

# ---- 5. Desktop shortcut ----
function Make-Shortcut($path) {
  $sh = New-Object -ComObject WScript.Shell
  $l = $sh.CreateShortcut($path)
  $l.TargetPath = Join-Path $App 'run.bat'
  $l.WorkingDirectory = $App
  $l.Description = 'Local AI email drafter'
  $l.Save()
}
if (Test-Path $DeskLnk) { Note 'SKIP' 'Desktop shortcut' 'already exists' }
else { Run-Step 'Desktop shortcut' { Make-Shortcut $DeskLnk } "create $DeskLnk -> app\run.bat" | Out-Null }

# ---- 6. Health check: tests ----
if ($SkipTests -or $DryRun) { Note 'SKIP' 'pytest' $(if ($DryRun) { 'dry run' } else { 'skipped by flag' }) }
elseif (Test-Path $VPy) {
  Push-Location $App
  try { $out = & $VPy -m pytest -q 2>&1 | Select-Object -Last 3; $out | ForEach-Object { Write-Host $_ }
        if ($LASTEXITCODE -eq 0) { Note 'OK' 'pytest' 'all tests passed' } else { Note 'FAIL' 'pytest' 'see output above' } }
  finally { Pop-Location }
} else { Note 'FAIL' 'pytest' 'venv missing' }

# ---- Checklist ----
Write-Host ''; Write-Host '=== CHECKLIST ==='
$Results | ForEach-Object { Write-Host ("{0,-5} {1}  {2}" -f $_.Status, $_.Step, $_.Detail) }
$fails = @($Results | Where-Object Status -eq 'FAIL').Count
Write-Host ''; Write-Host "FAIL lines: $fails. Next: GUIDE\00-START-HERE.md, then double-click 'Local Drafter' on the Desktop (or app\run.bat --check)."
exit $fails
