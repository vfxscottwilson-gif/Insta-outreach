@echo off
rem Runs an app script with keys loaded. Example: run.cmd main.py --sync-only
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0run.ps1" %*
pause
