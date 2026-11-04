@echo off
rem Runs an app script with keys loaded. Example: run.cmd organizer.py
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0run.ps1" %*
pause
