@echo off
rem Creates (or resets) the owner/admin login. You are asked for the password twice; it is not shown.
setlocal
set /p EMAIL=Admin email:
set /p NAME=Your name:
cd /d "%~dp0..\app\dashboard"
".venv\Scripts\python.exe" manage.py create-admin --email "%EMAIL%" --name "%NAME%" --owner
pause
