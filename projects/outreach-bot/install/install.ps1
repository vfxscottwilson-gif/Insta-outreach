<#
  outreach-bot installer (safe to re-run). Run via install\INSTALL.cmd. Flags:
    -Check / -DryRun   show what would happen; change nothing
    -Uninstall         remove only the Desktop shortcut
    -NoPrompt          do not ask for secrets (fill secrets\.env later)
  Prints no secret values. Network is used only by winget and pip.
#>
param([Alias('Check')][switch]$DryRun, [switch]$Uninstall, [switch]$NoPrompt)
$ErrorActionPreference = 'Continue'
$Root = Split-Path -Parent $PSScriptRoot; $App = Join-Path $Root 'app'; $Sec = Join-Path $Root 'secrets'
$EnvF = Join-Path $Sec '.env'; $Lnk = Join-Path ([Environment]::GetFolderPath('Desktop')) 'Outreach Bot (dry run).lnk'
function Note($s, $w, $d = '') { Write-Host ("[{0}] {1} {2}" -f $s, $w, $d) }
function Refresh-Path { $env:Path = [Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [Environment]::GetEnvironmentVariable('Path','User') }
function Have($c) { [bool](Get-Command $c -ErrorAction SilentlyContinue) }
function Real-Python { $p = Get-Command python -ErrorAction SilentlyContinue; [bool]($p -and $p.Source -notmatch 'WindowsApps') }
Write-Host "outreach-bot installer. Folder: $Root"; if ($DryRun) { Write-Host '*** DRY RUN: nothing will be changed ***' }
if ($Uninstall) { if (Test-Path $Lnk) { if (-not $DryRun) { Remove-Item $Lnk -Force }; Note 'OK' 'Shortcut removed' } else { Note 'SKIP' 'No shortcut' }; exit 0 }
if (-not (Test-Path "$App\generate.py")) { Note 'FAIL' 'Folder layout' 'app\generate.py missing: copy the WHOLE outreach-bot folder'; exit 1 }
Note 'OK' 'Folder layout' 'app\generate.py found'
Refresh-Path
# 1. Python
if (Real-Python) { Note 'OK' 'Python' ((& python --version 2>&1) -join '') }
elseif ($DryRun) { Note 'DRY' 'Python' 'MISSING: would run winget install Python.Python.3.12' }
elseif (Have 'winget') {
  winget install --id Python.Python.3.12 -e --silent --accept-package-agreements --accept-source-agreements; Refresh-Path
  if (Real-Python) { Note 'OK' 'Python installed' } else { Note 'WARN' 'Python' 'installed but not on PATH yet: close this window and run INSTALL.cmd again' }
}
else { Note 'FAIL' 'Python' 'missing and winget not available (install App Installer from the Microsoft Store)' }
# 2. venv + gspread
$vpy = "$App\.venv\Scripts\python.exe"
if (Test-Path $vpy) { Note 'SKIP' 'venv' 'app\.venv exists' }
elseif ($DryRun) { Note 'DRY' 'venv' 'would create app\.venv' }
elseif (Real-Python) { python -m venv "$App\.venv"; Note 'OK' 'venv created' }
if (-not $DryRun -and (Test-Path $vpy)) {
  & $vpy -m pip install -q -r "$App\requirements.txt"
  if ($LASTEXITCODE -eq 0) { Note 'OK' 'pip install' 'gspread ready' } else { Note 'FAIL' 'pip install' "exit $LASTEXITCODE" }
}
elseif ($DryRun) { Note 'DRY' 'pip install' 'would install app\requirements.txt (gspread)' }
# 3. secrets\.env
if (Test-Path $EnvF) { Note 'SKIP' 'secrets\.env' 'exists, not touched' }
elseif ($DryRun) { Note 'DRY' 'secrets\.env' 'would create from install\env.example' }
else {
  Copy-Item "$PSScriptRoot\env.example" $EnvF; Note 'OK' 'secrets\.env created' '(names only, empty values)'
  if (-not $NoPrompt) {
    Write-Host 'Enter each secret (typing is hidden). Press Enter to skip.'
    $lines = Get-Content $EnvF | ForEach-Object {
      if ($_ -match '^([A-Z_0-9]+)=$' -and $Matches[1] -ne 'GOOGLE_SA') {
        $n = $Matches[1]; $s = Read-Host -AsSecureString $n
        $v = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($s))
        "$n=$v"
      } else { $_ }
    }
    [IO.File]::WriteAllLines($EnvF, $lines, (New-Object Text.UTF8Encoding($false)))
    Write-Host 'GOOGLE_SA: save the service-account JSON file as secrets\google-sa.json (it is not typed here).'
  }
}
# 4. Desktop shortcut (starts a safe DRY RUN)
if ($DryRun) { Note 'DRY' 'Shortcut' $Lnk }
elseif (Test-Path $Lnk) { Note 'SKIP' 'Shortcut' 'exists' }
else {
  $l = (New-Object -ComObject WScript.Shell).CreateShortcut($Lnk); $l.TargetPath = 'powershell.exe'
  $l.Arguments = "-NoProfile -ExecutionPolicy Bypass -File `"$PSScriptRoot\run-bot.ps1`""; $l.WorkingDirectory = $App; $l.Save(); Note 'OK' 'Shortcut' $Lnk
}
# 5. Health check: offline self-test
if ($DryRun) { Note 'DRY' 'Self-test' 'would run app\selftest.py' }
elseif (Test-Path $vpy) {
  Push-Location $App; & $vpy selftest.py *> "$env:TEMP\outreach-selftest.log"; $rc = $LASTEXITCODE; Pop-Location
  if ($rc -eq 0) { Note 'OK' 'Self-test' 'passed' } else { Note 'FAIL' 'Self-test' "exit $rc, see $env:TEMP\outreach-selftest.log" }
}
# 6. Secrets checklist (presence only, never values)
if (Test-Path $EnvF) {
  if (Select-String -Path $EnvF -Pattern '^OUTREACH_SHEET_ID=.+' -Quiet) { Note 'OK' 'OUTREACH_SHEET_ID' 'set' } else { Note 'TODO' 'OUTREACH_SHEET_ID' 'empty: fill in secrets\.env' }
  if ((Select-String -Path $EnvF -Pattern '^GOOGLE_SA=.+' -Quiet) -or (Test-Path "$Sec\google-sa.json")) { Note 'OK' 'GOOGLE_SA' 'set' } else { Note 'TODO' 'GOOGLE_SA' 'save the JSON as secrets\google-sa.json' }
}
Write-Host 'Done. Test run: Desktop shortcut, or:  powershell -File install\run-bot.ps1'
