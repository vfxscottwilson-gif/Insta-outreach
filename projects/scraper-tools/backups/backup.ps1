<#
  Backup of the whole scraper-tools folder (no database; the .venv folders are rebuilt by the installer).
  Run:  powershell -ExecutionPolicy Bypass -File backups\backup.ps1   [-DryRun]
  Output (this backups\ folder, gitignored): scraper-folder-<date>.zip
#>
param([switch]$DryRun)
$ErrorActionPreference = 'Stop'
$Root = Split-Path -Parent $PSScriptRoot
$Stamp = Get-Date -Format 'yyyy-MM-dd_HHmm'
$zip = Join-Path $PSScriptRoot "scraper-folder-$Stamp.zip"
if ($DryRun) { Write-Host "[DRY] would zip $Root (without .venv, backups, caches) to $zip"; exit 0 }
$tmp = Join-Path ([IO.Path]::GetTempPath()) "scraper-bk-$Stamp"
robocopy $Root $tmp /E /XD node_modules .venv backups __pycache__ .pytest_cache /XF *.log /NFL /NDL /NJH /NJS /NP | Out-Null
if ($LASTEXITCODE -ge 8) { throw "robocopy failed ($LASTEXITCODE)" }
Compress-Archive -Path (Join-Path $tmp '*') -DestinationPath $zip -Force
Remove-Item $tmp -Recurse -Force
Write-Host ("[OK] Folder zip: {0} ({1:N1} MB)" -f $zip, ((Get-Item $zip).Length / 1MB))
