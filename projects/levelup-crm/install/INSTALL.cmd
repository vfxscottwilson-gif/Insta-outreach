@echo off
rem Double-click = Setup. Or from a terminal: INSTALL.cmd -Check | -Cloud | -Local
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0install.ps1" %*
echo.
pause
