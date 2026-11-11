@echo off
rem Full run. Stop any time with Ctrl+C (everything found so far is saved).
cd /d "%~dp0app"
if not exist ".venv\Scripts\python.exe" (
  echo Run install\INSTALL.cmd first.
  pause
  exit /b 1
)
".venv\Scripts\python.exe" run.py %*
if /i not "%~1"=="--scheduled" pause
