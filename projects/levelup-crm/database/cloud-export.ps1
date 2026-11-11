<#
  Best-effort export of the cloud side of LevelUp CRM (Supabase).
  Run:  powershell -ExecutionPolicy Bypass -File database\cloud-export.ps1 [-DryRun] [-NoSchema]
  Writes into database\backups\ (gitignored, holds personal data):
    schema-<date>.sql     full SQL schema (needs the database connection string, see below)
    <date>\ *.json        table data via Management API token (node database\backup-data.mjs, read-only)
    cloud-<date>\ *.json  storage buckets, functions, secret NAMES, cron jobs (storage-and-config-inventory.mjs)
  Connection string: variable DATABASE_URL (or SUPABASE_DB_URL), read at run time from secrets\.env, then
  secrets\app.env.backup, then app\.env. Supabase: Project Settings > Database > Connection string (URI).
  If it is not there the schema step is skipped with a TO DO line (the data + inventory steps still run).
  Secret values are never printed or logged.
#>
param([switch]$DryRun, [switch]$NoSchema)
$ErrorActionPreference = 'Continue'
$Root = Split-Path -Parent $PSScriptRoot
$Db   = $PSScriptRoot
$Out  = Join-Path $Db 'backups'
$Stamp = Get-Date -Format 'yyyy-MM-dd_HHmm'
function Dry([string]$t) { Write-Host "[DRY] $t" }

# ---- read a variable from the first env file that has it (value stays in memory) ----
function Get-Var([string[]]$names) {
  foreach ($f in @('secrets\.env', 'secrets\app.env.backup', 'app\.env')) {
    $p = Join-Path $Root $f
    if (-not (Test-Path $p)) { continue }
    foreach ($n in $names) {
      $l = Get-Content $p | Where-Object { $_ -match "^\s*$n\s*=" } | Select-Object -First 1
      if ($l) { $v = ($l -replace "^\s*$n\s*=\s*", '').Trim('"', "'", ' '); if ($v) { return $v } }
    }
  }
  return $null
}

# ---- 1. schema ----
if ($NoSchema) { Write-Host '[SKIP] schema (-NoSchema)' }
else {
  $url = Get-Var @('DATABASE_URL', 'SUPABASE_DB_URL')
  $pg  = Get-Command pg_dump -ErrorAction SilentlyContinue
  if (-not $url) {
    Write-Host '[TO DO] schema: no DATABASE_URL in secrets\.env. Add a line DATABASE_URL=postgresql://... (Supabase > Project Settings > Database > Connection string, use the Session pooler) and re-run.'
    Write-Host '        Until then the schema is still recoverable from app\supabase\migrations\ (27 files).'
  }
  elseif ($url -notmatch '^postgres(?:ql)?://([^:]+):(.*)@([^@/]+):(\d+)/([^?]+)') {
    Write-Host '[FAIL] schema: DATABASE_URL has an unexpected shape (a "@" inside the password must be written %40)'
  }
  else {
    $u, $pw, $h, $port, $dbn = $Matches[1], [Uri]::UnescapeDataString($Matches[2]), $Matches[3], $Matches[4], $Matches[5]
    $file = Join-Path $Out "schema-$Stamp.sql"
    if ($DryRun) { Dry "would run pg_dump --schema-only (schemas public, auth, storage) against $h, database $dbn, as $u -> $file$(if (-not $pg) { '  [pg_dump missing: winget install PostgreSQL.PostgreSQL.17, Command Line Tools only]' })" }
    elseif (-not $pg) { Write-Host '[TO DO] schema: pg_dump not found. Install once: winget install PostgreSQL.PostgreSQL.17 (only "Command Line Tools"), then re-run.' }
    else {
      New-Item -ItemType Directory -Force -Path $Out | Out-Null
      $env:PGPASSWORD = $pw
      try {
        & pg_dump -h $h -p $port -U $u -d $dbn --schema-only --no-owner --no-privileges -n public -n storage -f $file
        if ($LASTEXITCODE -eq 0) { Write-Host "[OK] schema -> $file" } else { Write-Host "[FAIL] pg_dump exit $LASTEXITCODE" }
      } finally { Remove-Item Env:PGPASSWORD -ErrorAction SilentlyContinue }
    }
  }
}

# ---- 2. data + 3. storage/functions inventory (Management API token, read-only) ----
$node = Get-Command node -ErrorAction SilentlyContinue
if (-not $node) { Write-Host '[TO DO] Node.js missing: run install\INSTALL.cmd first.'; exit 0 }
if ($DryRun) {
  Dry 'would run: node database\backup-data.mjs   (every public table to JSON)'
  & node (Join-Path $Db 'storage-and-config-inventory.mjs') --dry-run
} else {
  & node (Join-Path $Db 'backup-data.mjs')
  & node (Join-Path $Db 'storage-and-config-inventory.mjs')
}
Write-Host 'Reminder: Vercel and Cloudflare settings are not exported by script. See database\CLOUD-CONFIG.md.'
