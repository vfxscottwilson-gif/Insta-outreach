# START HERE: Lead Dashboard ("Database") setup

Local Flask + SQLite app that reads your lead Google Sheets, keeps history, shows the dashboard and lets admins assign leads. Everything below runs on this PC; nothing is pushed anywhere.

## 0. What you need
- Windows 10, Python 3.12 (installed), the folder `D:\All Automations Records\Lead Dashboard`.
- A Google **service account** JSON (new one recommended, see step 3). Never paste its contents in chat.
- Optional: a Gmail address + **app password** for "forgot password" codes (step 6). Without it, codes print to the server console (local use only).

## 1. One-time install
Open PowerShell in the project folder, then:

```bash
python -m venv .venv
```
```bash
.venv\Scripts\python.exe -m pip install -r requirements.txt
```
```bash
.venv\Scripts\python.exe manage.py init
```
You should see `Created .env ...` and `Database ready.` The `.env` file now holds `DASH_SECRET_KEY` and `DASH_PASSWORD_KEY` (random; never share or commit them; `.env` is gitignored).

## 2. Create your admin (you become the owner)
```bash
.venv\Scripts\python.exe manage.py create-admin --email you@example.com --name "Your Name" --owner
```
Type the password twice when asked (it is not shown). Minimum 10 characters.

## 3. Google service account (read access to the sheets)
1. Go to https://console.cloud.google.com, create a project, for example `lead-dashboard`.
2. APIs & Services -> Library -> enable **Google Sheets API**.
3. IAM & Admin -> Service Accounts -> Create -> name `lead-dashboard` -> Done.
4. Open it -> Keys -> Add key -> JSON. Save the file as `service_account.json` in the project folder (gitignored).
5. Copy the service account email (ends with `.iam.gserviceaccount.com`).
6. Share each lead sheet with that email as **Viewer** (Editor only if you later switch write-back on).
Why a new account: Google allows 60 reads per minute per account; the lead bots already use one, so the dashboard gets its own quota.

## 4. Connect the sheets
Either paste each sheet link in the app (Sources & sync -> Add a sheet), or list them once in `sources.yaml` (copy `sources.example.yaml`, fill the ids; they are read into the database on the first sync and the file is not needed afterwards).
Niche -> category rules: copy `categories.example.yaml` to `categories.yaml` and edit the regexes (optional).

## 5. First sync and start
```bash
.venv\Scripts\python.exe manage.py sync
```
You should see one line per sheet: `us: 1234 rows, 1234 new`. Then:
```bash
.venv\Scripts\python.exe manage.py serve
```
Open http://127.0.0.1:8080 and sign in. The server also syncs in the background (interval `DASH_SYNC_MINUTES` in `.env`).

## 6. Reset-code emails (optional)
In `.env` add `SMTP_USER=you@gmail.com`, `SMTP_PASSWORD=<16-char app password>`, `MAIL_FROM=you@gmail.com`. Create the app password at https://myaccount.google.com/apppasswords (needs 2-Step Verification). Limit: 500 mails/day; the app sends about one per reset.

## 7. Settings in `.env` (all optional)
| Key | Default | Meaning |
|---|---|---|
| `DASH_TIMEZONE` | `Asia/Karachi` | "Today" for live views and the sync schedule |
| `DASH_SYNC_MINUTES` | `2` | Background scan interval (tail reads; key+Status sweep every `DASH_SWEEP_MINUTES`=10); `0` = off |
| `DASH_READS_PER_MIN` | `45` | Google read budget for the whole app; on HTTP 429 it pauses 60 s |
| `DASH_BOT_LATE_HOURS` | `14` | Sync page shows "Late" when the bot's own Last run is older |
| `DASH_WRITEBACK` | `off` | Write status + `Dash Assignee` back into the sheets. Keep off until the one-sheet pilot passes |
| `DASH_APP_NAME` | `Database` | Name in the top bar |
| `DASH_ACCENT` | `purple` | `mono` for a black-and-white accent |
| `DASH_COOKIE_SECURE` | `off` | `on` when served over https |

## 8. Demo on fake data (safe to try first)
```bash
.venv\Scripts\python.exe manage.py demo
```
```bash
.venv\Scripts\python.exe manage.py serve --demo
```
Logins are in `demo_credentials.txt` (fake accounts, separate `data/demo.db`).

## 9. Backups and keys
- `manage.py backup` copies the database to `data/backups/` **without** the encrypted password copies and sessions. Keep `.env` and the backup apart: together they decrypt employee passwords.
- Admin-viewable employee passwords: the login check always uses the salted hash; a separate Fernet-encrypted copy (key `DASH_PASSWORD_KEY` in `.env`) exists only so an admin can reveal an employee's password after re-entering their own. Every reveal is logged. Lose `.env` and the copies are unreadable (logins still work; set new passwords).
- `manage.py rotate-password-key` re-encrypts the copies with a fresh key.

## 10. Tests
```bash
.venv\Scripts\python.exe -m pytest tests -q -p no:cacheprovider
```

## Troubleshooting
- `DASH_SECRET_KEY missing` -> run `manage.py init`.
- A sheet shows an error on Sources & sync -> share it with the service account email shown there, or check the link.
- Reset codes not arriving -> check `SMTP_*` in `.env`; without them the code is printed in the server window.
- The PC sleeping stops the background sync; the dashboard shows the last sync time on every page.
