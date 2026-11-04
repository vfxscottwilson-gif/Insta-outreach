<#
  Backup of the whole email-automation folder + the live Supabase database.
  Run:  powershell -ExecutionPolicy Bypass -File backups\backup.ps1   [-NoDb] [-DryRun]
  Output (in this backups\ folder, gitignored): outreach-folder-<date>.zip, db-<date>-schema.sql, db-<date>-data.sql
  WARNING: the zip contains private\ (keys). Keep it somewhere safe; never share or upload it publicly.
#>
param([switch]$NoDb, [switch]$DryRun)
$ErrorActionPreference = 'Stop'
$Root = Split-Path -Parent $PSScriptRoot
$Out  = $PSScriptRoot
$Stamp = Get-Date -Format 'yyyy-MM-dd_HHmm'

# ---- 1. Folder zip (skips node_modules, .venv, dist, backups, caches) ----
$zip = Join-Path $Out "outreach-folder-$Stamp.zip"
if ($DryRun) { Write-Host "[DRY] would zip $Root (without node_modules, .venv, dist, backups) to $zip" }
else {
  $tmp = Join-Path ([IO.Path]::GetTempPath()) "outreach-bk-$Stamp"
  robocopy $Root $tmp /E /XD node_modules .venv dist backups __pycache__ .pytest_cache /XF *.log /NFL /NDL /NJH /NJS /NP | Out-Null
  if ($LASTEXITCODE -ge 8) { throw "robocopy failed ($LASTEXITCODE)" }
  Compress-Archive -Path (Join-Path $tmp '*') -DestinationPath $zip -Force
  Remove-Item $tmp -Recurse -Force
  Write-Host ("[OK] Folder zip: {0} ({1:N1} MB)" -f $zip, ((Get-Item $zip).Length / 1MB))
}

# ---- 2. Database export (needs pg_dump = PostgreSQL client tools) ----
if ($NoDb) { Write-Host '[SKIP] database export (-NoDb)'; exit 0 }
$pg = Get-Command pg_dump -ErrorAction SilentlyContinue
if (-not $pg) {
  Write-Host '[TO DO] pg_dump not found. Install it once:  winget install PostgreSQL.PostgreSQL.17   (only the "Command Line Tools" are needed), then re-run this script.'
  Write-Host '        Supabase also keeps its own daily backups: Dashboard > Database > Backups.'
  exit 0
}
$envFile = Join-Path $Root 'app\.env'
$line = (Get-Content $envFile -ErrorAction SilentlyContinue | Where-Object { $_ -match '^\s*DATABASE_URL\s*=' } | Select-Object -First 1)
if (-not $line) { Write-Host '[FAIL] DATABASE_URL missing in app\.env'; exit 1 }
$url = ($line -replace '^\s*DATABASE_URL\s*=\s*', '').Trim('"', "'", ' ')
if ($url -notmatch '^postgres(?:ql)?://([^:]+):(.*)@([^@/]+):(\d+)/([^?]+)') { Write-Host '[FAIL] DATABASE_URL has an unexpected shape (a "@" inside the password must be written %40)'; exit 1 }
$user, $pass, $dbhost, $port, $db = $Matches[1], [Uri]::UnescapeDataString($Matches[2]), $Matches[3], $Matches[4], $Matches[5]
if ($DryRun) { Write-Host "[DRY] would run pg_dump (schema, then data) against $dbhost, database $db, as $user"; exit 0 }
$env:PGPASSWORD = $pass
try {
  & pg_dump -h $dbhost -p $port -U $user -d $db --schema-only --no-owner --no-privileges -f (Join-Path $Out "db-$Stamp-schema.sql")
  & pg_dump -h $dbhost -p $port -U $user -d $db --data-only --no-owner -f (Join-Path $Out "db-$Stamp-data.sql")
  Write-Host "[OK] Database exported to $Out (db-$Stamp-schema.sql, db-$Stamp-data.sql). The data file holds real data: keep it private."
} finally { Remove-Item Env:PGPASSWORD -ErrorAction SilentlyContinue }
