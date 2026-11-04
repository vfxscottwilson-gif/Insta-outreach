<#
  Backup of the whole local-drafter folder (no database: this app has none).
  Run:  powershell -ExecutionPolicy Bypass -File backups\backup.ps1   [-DryRun]
  Output (this backups\ folder, gitignored): local-drafter-folder-<date>.zip
  WARNING: the zip contains secrets\ (keys). Keep it safe; never share or upload it.
#>
param([switch]$DryRun)
$ErrorActionPreference = 'Stop'
$Root = Split-Path -Parent $PSScriptRoot
$Stamp = Get-Date -Format 'yyyy-MM-dd_HHmm'
$zip = Join-Path $PSScriptRoot "local-drafter-folder-$Stamp.zip"
if ($DryRun) { Write-Host "[DRY] would zip $Root (without .venv, backups, caches, logs) to $zip"; exit 0 }
$tmp = Join-Path ([IO.Path]::GetTempPath()) "local-drafter-bk-$Stamp"
robocopy $Root $tmp /E /XD .venv backups __pycache__ .pytest_cache /XF *.log /NFL /NDL /NJH /NJS /NP | Out-Null
if ($LASTEXITCODE -ge 8) { throw "robocopy failed ($LASTEXITCODE)" }
Compress-Archive -Path (Join-Path $tmp '*') -DestinationPath $zip -Force
Remove-Item $tmp -Recurse -Force
Write-Host ("[OK] Folder zip: {0} ({1:N1} MB)" -f $zip, ((Get-Item $zip).Length / 1MB))
