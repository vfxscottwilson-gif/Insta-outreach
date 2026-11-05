@echo off
rem Double-click AFTER you copied the Supabase secret key in the dashboard (API Keys > Secret keys > click the eye to reveal > click copy).
rem It saves the key into secrets\supabase-backup.env and clears the clipboard. It never shows the key.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0save-clipboard-key.ps1"
echo.
pause
