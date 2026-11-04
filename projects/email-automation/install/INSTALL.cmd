@echo off
rem One-time installer for the Outreach app. Safe to run again.
rem   Install.cmd            install / repair
rem   Install.cmd -DryRun    show what would happen, change nothing
rem   Install.cmd -Uninstall remove the Desktop + Start-menu shortcuts only
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0install.ps1" %*
echo.
pause
