@echo off
rem One-time installer for the Outreach app. Safe to run again.
rem   INSTALL.cmd            install / repair
rem   INSTALL.cmd -DryRun    show what would happen, change nothing
rem   INSTALL.cmd -Uninstall remove the Desktop + Start-menu shortcuts only
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0install.ps1" %*
echo.
pause
