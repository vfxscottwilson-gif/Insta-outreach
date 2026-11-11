@echo off
rem One-click install: creates the Python environment, installs the libraries, tests, creates the Settings files.
rem Check only (changes nothing): INSTALL.cmd -Check
cd /d "%~dp0..\app"
if /i "%~1"=="-Check" goto :check
set PY=python
where py >nul 2>nul && set PY=py -3.12
if not exist ".venv\Scripts\python.exe" (
  %PY% -m venv .venv
  if errorlevel 1 goto :err
)
".venv\Scripts\python.exe" -m pip install --disable-pip-version-check -r requirements.txt
if errorlevel 1 goto :err
:check
if not exist ".venv\Scripts\python.exe" goto :err
".venv\Scripts\python.exe" run.py --check
if errorlevel 1 goto :err
".venv\Scripts\python.exe" src\selftest.py >nul
if errorlevel 1 goto :err
if /i not "%~1"=="-Check" ".venv\Scripts\python.exe" run.py --setup
echo.
echo INSTALL OK. Next: double-click "Pilot Test.cmd" in the main folder.
pause
exit /b 0
:err
echo.
echo INSTALL FAILED. Read the message above. Python 3.12 must be installed (python.org) with "Add to PATH" ticked.
pause
exit /b 1
