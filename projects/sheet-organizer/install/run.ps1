# Runs a script from app\ with the keys from secrets\.env loaded into the environment.
# Usage: run.cmd organizer.py   (test run by default: DRY_RUN=yes unless set in secrets\.env)
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
if ($key -and -not $env:GOOGLE_SA) { $env:GOOGLE_SA = [IO.File]::ReadAllText($key.FullName) }   # the app wants the JSON content
if (-not $env:DRY_RUN) { $env:DRY_RUN = 'yes' }
if ($args.Count -eq 0) { $args = @('organizer.py') }
Set-Location $App
& $Py @args
exit $LASTEXITCODE
