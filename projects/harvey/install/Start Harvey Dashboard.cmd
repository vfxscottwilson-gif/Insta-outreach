@echo off
rem Opens the Harvey dashboard. It prints a private link (http://127.0.0.1:5555/#token=...): open that link in your browser.
cd /d "%~dp0..\app"
if not exist ".venv\Scripts\harvey.exe" ( echo Harvey is not installed yet. Run install\INSTALL.cmd first. & pause & exit /b 1 )
".venv\Scripts\harvey.exe" dashboard
pause
