' Starts the Database demo server and the online tunnel with NO visible windows. Logs go to the two .log files in the demo folder.
' Stop them with install\STOP-ONLINE-DEMO.cmd.
Dim sh, fso, here, proj, demo
Set sh = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")
here = fso.GetParentFolderName(WScript.ScriptFullName)
proj = fso.GetParentFolderName(here)
demo = "F:\caches\database-online-test"
sh.Run "cmd /c ""cd /d " & demo & " && """ & proj & "\app\dashboard\.venv\Scripts\python.exe"" manage.py serve --demo --port 8099 >> serve.log 2>&1""", 0, False
WScript.Sleep 4000
sh.Run "cmd /c ""cd /d " & here & " && node online-supervisor.mjs 8099 >> " & demo & "\supervisor.log 2>&1""", 0, False
