@echo off
rem Starts the Database demo (fake data) and the free online tunnel, with no windows. Double-click to start.
rem Public address: https://levelup-database.outreach-web.workers.dev (stays the same after restarts, ready in about a minute).
rem To stop: double-click STOP-ONLINE-DEMO.cmd.
wscript.exe "%~dp0start-hidden.vbs"
echo Started in the background. Open https://levelup-database.outreach-web.workers.dev in about one minute.
timeout /t 6 >nul
