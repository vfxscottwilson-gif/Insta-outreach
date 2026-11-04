@echo off
rem Double-click to install. Passes any arguments (e.g. -Check) to install.ps1.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0install.ps1" %*
pause
