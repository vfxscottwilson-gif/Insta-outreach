@echo off
rem Stops the real Database app, the tunnel and the tunnel supervisor started by START-ONLINE.cmd.
powershell -NoProfile -Command "Get-CimInstance Win32_Process | Where-Object { $_.Name -in 'python.exe','node.exe','cloudflared.exe' -and $_.CommandLine -match '8080' } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force }"
echo Stopped. The public address now shows the offline page.
timeout /t 4 >nul
