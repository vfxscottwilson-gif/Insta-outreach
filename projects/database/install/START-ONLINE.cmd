@echo off
rem Puts the REAL Database app online (real logins and data). Double-click to start; no windows stay open.
rem Public address: https://levelup-database.outreach-web.workers.dev (ready in about a minute).
rem Works only while this PC is on and awake. To stop: double-click STOP-ONLINE.cmd.
wscript.exe "%~dp0start-online-hidden.vbs"
echo Started in the background. Open https://levelup-database.outreach-web.workers.dev/admin/login in about one minute.
timeout /t 6 >nul
