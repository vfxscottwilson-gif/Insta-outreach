# Database CRM (Lead Dashboard): Setup guide

For a non-expert on Windows 10. Never put secret values in this file.

## 1. What this app is
A dashboard that reads your lead Google Sheets (made by the lead bots and the YouTube finder), keeps its own history in a small local database file, and shows leads per day/month, per country, niche and source. Admins can assign leads to employees. Login is email + password; one active session per account; "forgot password" sends a code to the account email; the admin portal manages employees and everything else.

## 2. Accounts needed
| Service | Why | Free? | Link |
|---|---|---|---|
| Google Cloud (a service account) | Lets the app READ your lead sheets | Free | https://console.cloud.google.com |
| Google Sheets (your existing lead sheets) | The data source; each sheet is shared with the service account email as Viewer | Free | - |
| Gmail with an app password (optional) | Sends "forgot password" codes. Without it the code prints in the server window | Free (500 mails/day) | https://myaccount.google.com/apppasswords |

No Supabase, GitHub or hosting account is needed. Everything else runs on this PC.

## 3. How it fits together
- Frontend and backend are ONE Python (Flask) program in `app\dashboard`; pages are rendered by the server. Served by `waitress` on port 8080 of this PC.
- Database = a SQLite file `app\dashboard\data\dash.db` (local). Cloud parts: only the Google Sheets being read.
- A background loop inside the server syncs the sheets every 2 minutes (PC asleep = no sync).
- `app\web` is a separate design preview with fake data; optional, not needed.

## 4. Folder map
See `README.md`.

## 5. First-time install
1. Open the `install` folder and double-click `INSTALL.cmd`. Click **Yes** if Windows asks.
2. Optional dry run first (changes nothing): open PowerShell in `install\` and run:
```
.\install.ps1 -Check
```
You should see `OK`/`SKIP`/`DRY` lines.
3. The installer: installs Python 3.12 if missing, creates `app\dashboard\.venv`, installs packages, creates the random keys (`manage.py init`), asks (hidden input; press Enter to skip) for the Gmail details, runs a local health check, makes a Desktop shortcut.
4. Create your owner login: double-click `install\create-admin.cmd`, type your email and name, then the password twice (not shown, min 10 characters).
5. Expected at the end: a CHECKLIST with no `FAIL` lines and "Done".

## 6. Secrets
See `secrets\SECRETS-CHECKLIST.md` (names only). Master copy of the settings: `secrets\.env` (the installer copies it to `app\dashboard\.env`, which is where the app reads it). Put `service_account.json` and (optional) `sources.yaml` in `secrets\` too; the installer restores them.

## 7. Run it / use it
1. Double-click **Database Dashboard** on the Desktop (or `install\start-dashboard.cmd`). A black window stays open (that is the server); the browser opens http://127.0.0.1:8080.
2. Sign in with the owner login. Add sheets: **Sources & sync -> Add a sheet** (paste the link), or list them in `secrets\sources.yaml`.
3. Demo on fake data (safe, separate database): run `install\start-dashboard.cmd --demo` from PowerShell:
```
.\start-dashboard.cmd --demo
```
First make demo data once: in `app\dashboard` run `.venv\Scripts\python.exe manage.py demo`. Demo logins are in `secrets\demo_credentials.txt`.
4. Close the black window to stop the app.

## 8. How to change common things
| I want to... | Do this |
|---|---|
| Add a new employee | Sign in as admin -> Users -> add |
| Add a lead sheet | Share it with the service account email (Viewer), then Sources & sync -> Add a sheet |
| Change the time zone / sync interval / app name | Edit `secrets\.env` keys `DASH_TIMEZONE`, `DASH_SYNC_MINUTES`, `DASH_APP_NAME`, then re-run INSTALL.cmd and restart |
| Turn on writing status back into the sheets | `DASH_WRITEBACK=on` in `secrets\.env` AND share sheets as Editor. Keep OFF until the one-sheet pilot passes |
| Group niches into categories | Copy `categories.example.yaml` to `secrets\categories.yaml`, edit, re-run INSTALL.cmd |
| Make a backup | `powershell -ExecutionPolicy Bypass -File backups\backup.ps1` |

## 9. Troubleshooting
| Problem | Fix |
|---|---|
| `DASH_SECRET_KEY missing` | Run INSTALL.cmd again (it runs `manage.py init`) |
| Window closes immediately / "Not installed yet" | Run `install\INSTALL.cmd` first |
| A sheet shows an error | Share it with the service account email (Viewer) or check the link |
| Reset codes do not arrive | Fill `SMTP_USER`, `SMTP_PASSWORD`, `MAIL_FROM` in `secrets\.env` and re-run INSTALL.cmd; until then codes print in the server window |
| Dashboard looks out of date | PC was asleep; the last sync time is shown on every page |
More: `GUIDE\04-TROUBLESHOOTING.md`.

## 10. Move to a new PC
1. Copy the whole `database` folder (with `secrets\`) to the new PC.
2. Double-click `install\INSTALL.cmd`.
3. To keep your data: copy the SQLite file back, see `database\RESTORE.md`.
4. Check: in `install\` run `.\install.ps1 -Check`. Every line should say OK/SKIP.
