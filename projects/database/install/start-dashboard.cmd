@echo off
rem Starts the Lead Dashboard (Database) and opens it in the browser. Add --demo to use fake data. Close this window to stop it.
setlocal
set "APP=%~dp0..\app\dashboard"
if not exist "%APP%\.venv\Scripts\python.exe" ( echo Not installed yet: run install\INSTALL.cmd first. & pause & exit /b 1 )
cd /d "%APP%"
start "" /min powershell -NoProfile -Command "Start-Sleep 4; Start-Process 'http://127.0.0.1:8080'"
".venv\Scripts\python.exe" manage.py serve %*
pause
