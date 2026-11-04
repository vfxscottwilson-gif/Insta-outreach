<#
  Backup of the whole sheet-organizer folder (no database: data lives in your Google Sheet).
  Run:  powershell -ExecutionPolicy Bypass -File backups\backup.ps1   [-DryRun]
  Output (in this backups\ folder, gitignored): sheet-organizer-folder-<date>.zip
  WARNING: the zip contains secrets\ (keys). Keep it somewhere safe; never share or upload it publicly.
  To back up the Sheet data: in Google Sheets use File > Download > Microsoft Excel and save it in database\.
#>
param([switch]$DryRun)
$ErrorActionPreference = 'Stop'
$Root  = Split-Path -Parent $PSScriptRoot
$Stamp = Get-Date -Format 'yyyy-MM-dd_HHmm'
$zip   = Join-Path $PSScriptRoot "sheet-organizer-folder-$Stamp.zip"
if ($DryRun) { Write-Host "[DRY] would zip $Root (without .venv, backups, caches) to $zip"; exit 0 }
$tmp = Join-Path ([IO.Path]::GetTempPath()) "sheet-organizer-bk-$Stamp"
robocopy $Root $tmp /E /XD node_modules .venv backups __pycache__ .pytest_cache /XF *.log /NFL /NDL /NJH /NJS /NP | Out-Null
if ($LASTEXITCODE -ge 8) { throw "robocopy failed ($LASTEXITCODE)" }
Compress-Archive -Path (Join-Path $tmp '*') -DestinationPath $zip -Force
Remove-Item $tmp -Recurse -Force
Write-Host ("[OK] Folder zip: {0} ({1:N1} MB)" -f $zip, ((Get-Item $zip).Length / 1MB))
