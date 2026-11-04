<#
  Backup of the whole outreach-bot folder (no database: data lives in Google Sheets, see database\README.md).
  Run:  powershell -ExecutionPolicy Bypass -File backups\backup.ps1 [-DryRun]
  Output (gitignored): backups\outreach-bot-folder-<date>.zip. WARNING: the zip contains secrets\. Keep it private.
#>
param([switch]$DryRun)
$ErrorActionPreference = 'Stop'
$Root = Split-Path -Parent $PSScriptRoot; $Stamp = Get-Date -Format 'yyyy-MM-dd_HHmm'
$zip = Join-Path $PSScriptRoot "outreach-bot-folder-$Stamp.zip"
if ($DryRun) { Write-Host "[DRY] would zip $Root (without .venv, backups, __pycache__) to $zip"; exit 0 }
$tmp = Join-Path ([IO.Path]::GetTempPath()) "outreach-bk-$Stamp"
robocopy $Root $tmp /E /XD .venv backups __pycache__ .pytest_cache /NFL /NDL /NJH /NJS /NP | Out-Null
if ($LASTEXITCODE -ge 8) { throw "robocopy failed ($LASTEXITCODE)" }
Compress-Archive -Path (Join-Path $tmp '*') -DestinationPath $zip -Force
Remove-Item $tmp -Recurse -Force
Write-Host ("[OK] {0} ({1:N1} MB)" -f $zip, ((Get-Item $zip).Length / 1MB))
