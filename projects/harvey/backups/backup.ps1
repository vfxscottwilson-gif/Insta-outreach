<#
  Backup of the whole harvey folder (includes app\data\harvey.db, the SQLite database).
  Run:  powershell -ExecutionPolicy Bypass -File backups\backup.ps1   [-DryRun]
  Output (in this backups\ folder, gitignored): harvey-folder-<date>.zip
  WARNING: the zip contains secrets\ (keys) and prospect data. Keep it somewhere safe; never share or upload it.
#>
param([switch]$DryRun)
$ErrorActionPreference = 'Stop'
$Root  = Split-Path -Parent $PSScriptRoot
$Stamp = Get-Date -Format 'yyyy-MM-dd_HHmm'
$zip   = Join-Path $PSScriptRoot "harvey-folder-$Stamp.zip"
if ($DryRun) { Write-Host "[DRY] would zip $Root (without .venv, backups, caches) to $zip"; exit 0 }
$tmp = Join-Path ([IO.Path]::GetTempPath()) "harvey-bk-$Stamp"
robocopy $Root $tmp /E /XD .venv backups __pycache__ .pytest_cache node_modules /XF *.log /NFL /NDL /NJH /NJS /NP | Out-Null
if ($LASTEXITCODE -ge 8) { throw "robocopy failed ($LASTEXITCODE)" }
Compress-Archive -Path (Join-Path $tmp '*') -DestinationPath $zip -Force
Remove-Item $tmp -Recurse -Force
Write-Host ("[OK] Folder zip: {0} ({1:N1} MB)" -f $zip, ((Get-Item $zip).Length / 1MB))
