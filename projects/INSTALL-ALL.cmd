@echo off
rem Runs every app's installer in turn (or just checks them with -Check). Safe to re-run.
rem Usage: INSTALL-ALL.cmd [-Check]
for /d %%A in ("%~dp0*") do (
  if exist "%%A\install\INSTALL.cmd" (
    echo ===== %%~nxA =====
    powershell -NoProfile -ExecutionPolicy Bypass -File "%%A\install\install.ps1" %*
  )
)
echo.
echo Done. Apps are listed in README.md. Cloud logins are listed in each app's SETUP-GUIDE.md.
pause
