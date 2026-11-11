@echo off
rem Starts the Database dashboard on this PC and opens the ADMIN login page.
rem Keep this window open while you use the app. Close it to stop the app.
cd /d "%~dp0app\dashboard"
start "" "http://127.0.0.1:8080/admin/login"
.venv\Scripts\python.exe manage.py serve
pause
