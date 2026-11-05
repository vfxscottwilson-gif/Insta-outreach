# 04 Troubleshooting

| Problem | Fix |
|---|---|
| INSTALL says Python missing / not on PATH | Close the window, run INSTALL.cmd again (winget just installed it). No winget: install "App Installer" from the Microsoft Store |
| `FAIL Health check` | Run in `app\dashboard`: `.venv\Scripts\python.exe manage.py init` and read the error. Usually a broken `.env`: delete `app\dashboard\.env` (keep `secrets\.env`) and re-run INSTALL.cmd |
| Browser shows "refused to connect" | Server window not open or port 8080 in use. Start via the Desktop shortcut; close other copies |
| `DASH_SECRET_KEY missing` | Re-run INSTALL.cmd |
| Sheet error on Sources & sync | Share the sheet with the service account email (Viewer); check the link |
| HTTP 429 from Google | The app pauses 60 s on its own; lower `DASH_READS_PER_MIN` if it repeats |
| No reset code email | Fill `SMTP_*` and `MAIL_FROM` in `secrets\.env`; until then the code prints in the server window |
| Forgot owner password | Run `install\create-admin.cmd` with the same email (resets it) |
| Test suite: 1 failure `test_employee_sees_no_admin_nav_items` | Known: the test expects only "My leads" but the nav now also shows "Add leads". Test is stale, not the installer. Fix in the app repo when the dashboard chat resumes |
| Dry run prints "Done" | Normal; nothing was changed in `-Check` mode |
