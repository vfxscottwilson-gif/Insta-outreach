<#
  Backup of the full-cycle-emails folder (docs only, no database).
  Run:  powershell -ExecutionPolicy Bypass -File backups\backup.ps1   [-DryRun]
#>
param([switch]$DryRun)
$ErrorActionPreference = 'Stop'
$Root = Split-Path -Parent $PSScriptRoot
$Stamp = Get-Date -Format 'yyyy-MM-dd_HHmm'
$zip = Join-Path $PSScriptRoot "full-cycle-emails-folder-$Stamp.zip"
if ($DryRun) { Write-Host "[DRY] would zip $Root (without backups) to $zip"; exit 0 }
$tmp = Join-Path ([IO.Path]::GetTempPath()) "fce-bk-$Stamp"
robocopy $Root $tmp /E /XD backups /NFL /NDL /NJH /NJS /NP | Out-Null
if ($LASTEXITCODE -ge 8) { throw "robocopy failed ($LASTEXITCODE)" }
Compress-Archive -Path (Join-Path $tmp '*') -DestinationPath $zip -Force
Remove-Item $tmp -Recurse -Force
Write-Host "[OK] Folder zip: $zip"
