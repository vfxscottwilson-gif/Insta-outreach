<#
  Backup of the whole levelup-crm folder + the cloud data (Supabase).
  Run:  powershell -ExecutionPolicy Bypass -File backups\backup.ps1   [-NoDb] [-DryRun]
  Output (this backups\ folder, zip/sql are gitignored): levelup-crm-folder-<date>.zip
  and, via database\cloud-export.ps1, the files in database\backups\ (schema SQL, table JSON, storage/function inventory).
  WARNING: the zip contains secrets\ (keys) and staff data. Keep it somewhere safe; never share or upload it publicly.
#>
param([switch]$NoDb, [switch]$DryRun)
$ErrorActionPreference = 'Stop'
$Root = Split-Path -Parent $PSScriptRoot
$Out  = $PSScriptRoot
$Stamp = Get-Date -Format 'yyyy-MM-dd_HHmm'

# ---- 1. Folder zip (skips node_modules, dist, caches and this backups folder) ----
$zip = Join-Path $Out "levelup-crm-folder-$Stamp.zip"
if ($DryRun) { Write-Host "[DRY] would zip $Root (without node_modules, dist, backups) to $zip" }
else {
  $tmp = Join-Path ([IO.Path]::GetTempPath()) "levelup-bk-$Stamp"
  robocopy $Root $tmp /E /XD node_modules dist backups __pycache__ .pytest_cache .vercel-tmp /XF *.log /NFL /NDL /NJH /NJS /NP | Out-Null
  if ($LASTEXITCODE -ge 8) { throw "robocopy failed ($LASTEXITCODE)" }
  Compress-Archive -Path (Join-Path $tmp '*') -DestinationPath $zip -Force
  Remove-Item $tmp -Recurse -Force
  Write-Host ("[OK] Folder zip: {0} ({1:N1} MB)" -f $zip, ((Get-Item $zip).Length / 1MB))
}

# ---- 2. Cloud export (schema + data + inventory) ----
if ($NoDb) { Write-Host '[SKIP] cloud export (-NoDb)'; exit 0 }
$args2 = @(); if ($DryRun) { $args2 += '-DryRun' }
& powershell -NoProfile -ExecutionPolicy Bypass -File (Join-Path $Root 'database\cloud-export.ps1') @args2
