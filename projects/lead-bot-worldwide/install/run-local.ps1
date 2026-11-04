# Local test run: loads secrets\.env into this window only, then runs the bot WITHOUT Google (writes CSV files to app\local_sheet\).
# Usage: run-local.ps1 [bot arguments]   default: --local --country US   Press Ctrl+C to stop.
$Root = Split-Path -Parent $PSScriptRoot
$App = Join-Path $Root 'app'
$envFile = Join-Path $Root 'secrets\.env'
if (Test-Path $envFile) { Get-Content $envFile | ForEach-Object { if ($_ -match '^﻿?\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.+?)\s*$') { Set-Item -Path "Env:$($Matches[1])" -Value $Matches[2].Trim('"',"'") } } }
$args2 = if ($args.Count) { $args } else { '--local --country US'.Split(' ') }
Set-Location $App
& (Join-Path $App '.venv\Scripts\python.exe') src\leadbot.py @args2
Write-Host "Done. Output is in $App\local_sheet"
