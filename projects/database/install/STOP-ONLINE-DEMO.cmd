@echo off
rem Stops the Database demo server, the tunnel and the tunnel supervisor started by START-ONLINE-DEMO.cmd.
powershell -NoProfile -Command "Get-CimInstance Win32_Process | Where-Object { $_.Name -in 'python.exe','node.exe','cloudflared.exe' -and $_.CommandLine -match '8099' } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue }"
echo Stopped. The public link now shows "Database is offline" until you start it again.
timeout /t 5 >nul
