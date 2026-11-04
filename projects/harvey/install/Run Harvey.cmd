@echo off
rem Starts the Harvey heartbeat loop (finds prospects, writes and SENDS emails). Make sure sending limits and keys are set first (GUIDE\00-START-HERE.md).
cd /d "%~dp0..\app"
if not exist ".venv\Scripts\harvey.exe" ( echo Harvey is not installed yet. Run install\INSTALL.cmd first. & pause & exit /b 1 )
".venv\Scripts\harvey.exe" run
pause
