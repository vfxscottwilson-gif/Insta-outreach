# Runs the bot from this folder. Loads secrets\.env (and secrets\google-sa.json) into this process only. Prints no values.
# Default = DRY RUN (writes no rows). -Live really writes drafts. -SelfTest runs the offline tests.
param([switch]$Live, [switch]$SelfTest, [string]$Limit = '10')
$Root = Split-Path -Parent $PSScriptRoot; $App = Join-Path $Root 'app'; $Sec = Join-Path $Root 'secrets'
$py = if (Test-Path "$App\.venv\Scripts\python.exe") { "$App\.venv\Scripts\python.exe" } else { 'python' }
Set-Location $App
if ($SelfTest) { & $py selftest.py; exit $LASTEXITCODE }
$f = Join-Path $Sec '.env'
if (Test-Path $f) { foreach ($l in Get-Content $f) { if ($l -match '^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.+?)\s*$') { Set-Item "Env:$($Matches[1])" $Matches[2].Trim('"', "'") } } }
$j = Join-Path $Sec 'google-sa.json'
if (-not $env:GOOGLE_SA -and (Test-Path $j)) { $env:GOOGLE_SA = (Get-Content $j -Raw) }
$env:DRY_RUN = $(if ($Live) { 'off' } else { 'on' }); $env:RUN_LIMIT = $Limit
Write-Host "Mode: $(if ($Live) {'LIVE (writes drafts)'} else {'DRY RUN (writes nothing)'}), limit $Limit"
& $py -u generate.py
if ($Host.Name -eq 'ConsoleHost') { Read-Host 'Done. Press Enter to close' | Out-Null }
