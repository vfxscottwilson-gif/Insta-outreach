@echo off
rem Installs the Python libraries and checks the tool. Double-click to run.
cd /d "%~dp0\.."
python --version || (echo Python is not installed or not on PATH. See START-HERE.md step 1. & pause & exit /b 1)
python -m pip install -r app\requirements.txt || (echo Library install failed. & pause & exit /b 1)
python app\run.py --check
echo.
echo Done. Next: read START-HERE.md
pause
