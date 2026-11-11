' Starts the REAL Database app (real logins, data\dash.db) on port 8080 and the online tunnel, with NO visible windows.
' Public address: https://levelup-database.outreach-web.workers.dev  Stop with install\STOP-ONLINE.cmd.
Dim sh, fso, here, proj, app, logs
Set sh = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")
here = fso.GetParentFolderName(WScript.ScriptFullName)
proj = fso.GetParentFolderName(here)
app = proj & "\app\dashboard"
logs = "F:\caches\database-online-test"
' https only: session cookies are sent over the secure public address (wins over .env, which is not edited)
sh.Environment("PROCESS")("DASH_COOKIE_SECURE") = "on"
sh.Run "cmd /c ""cd /d """ & app & """ && .venv\Scripts\python.exe manage.py serve --port 8080 >> """ & logs & "\serve-real.log"" 2>&1""", 0, False
WScript.Sleep 5000
sh.Run "cmd /c ""cd /d """ & here & """ && node online-supervisor.mjs 8080 >> """ & logs & "\supervisor-real.log"" 2>&1""", 0, False
