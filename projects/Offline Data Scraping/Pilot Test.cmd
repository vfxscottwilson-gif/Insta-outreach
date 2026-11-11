@echo off
rem Small test run: about 8 leads, a few minutes. Always do this after changing Settings.
cd /d "%~dp0app"
if not exist ".venv\Scripts\python.exe" (
  echo Run install\INSTALL.cmd first.
  pause
  exit /b 1
)
".venv\Scripts\python.exe" run.py --pilot
pause
