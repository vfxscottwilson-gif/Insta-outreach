# Runs a script from app\ with the keys from secrets\.env loaded into the environment.
# Usage: run.cmd main.py [--sync-only]   |   run.cmd send_assist.py [acc1 acc2]
# Never prints secret values.
$Root = Split-Path -Parent $PSScriptRoot
$App  = Join-Path $Root 'app'
$Sec  = Join-Path $Root 'secrets'
$Py   = Join-Path $App '.venv\Scripts\python.exe'
if (-not (Test-Path $Py)) { Write-Host 'Not installed yet: run install\INSTALL.cmd first.'; exit 1 }
$envFile = Join-Path $Sec '.env'
if (Test-Path $envFile) {
  foreach ($l in Get-Content $envFile) {
    if ($l -match '^\s*([A-Z0-9_]+)\s*=\s*(.*)$' -and $Matches[2].Trim()) { Set-Item "Env:$($Matches[1])" $Matches[2].Trim().Trim('"') }
  }
}
$key = Get-ChildItem $Sec -Filter '*.json' -ErrorAction SilentlyContinue | Select-Object -First 1
if ($key -and -not $env:GOOGLE_SERVICE_ACCOUNT_JSON) { $env:GOOGLE_SERVICE_ACCOUNT_JSON = $key.FullName }   # the app accepts a file path
if (-not $env:PROFILES_FILE -and (Test-Path (Join-Path $Sec 'profiles.json'))) { $env:PROFILES_FILE = Join-Path $Sec 'profiles.json' }
if ($args.Count -eq 0) { $args = @('main.py', '--sync-only') }
Set-Location $App
& $Py @args
exit $LASTEXITCODE
