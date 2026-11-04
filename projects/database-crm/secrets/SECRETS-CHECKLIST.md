# Secrets checklist

Names only. NEVER write values here. Real values go in `secrets\.env` (gitignored) or your password manager.

| Secret name | Used by | Where to get it | Done |
|---|---|---|---|
| DASH_SECRET_KEY | Flask sessions | Created automatically by INSTALL.cmd (`manage.py init`) | [ ] |
| DASH_PASSWORD_KEY | Encrypted employee-password copies (admin view) | Created automatically by INSTALL.cmd. Back it up: losing it makes the copies unreadable | [ ] |
| service_account.json (file; path var `DASH_SERVICE_ACCOUNT`, default `app\dashboard\service_account.json`) | Reads the Google Sheets | 1. console.cloud.google.com -> new project. 2. Enable Google Sheets API. 3. IAM -> Service Accounts -> Create. 4. Keys -> Add key -> JSON. 5. Save into `secrets\` as `service_account.json`. 6. Share each sheet with its email as Viewer | [ ] |
| Sheet IDs / links (in `sources.yaml` or added in the app) | Sources | Copy from each sheet URL (between /d/ and the next /). Template: `app\dashboard\sources.example.yaml` | [ ] |
| SMTP_USER | Reset-code email | Your Gmail address (optional) | [ ] |
| SMTP_PASSWORD | Reset-code email | myaccount.google.com/apppasswords (needs 2-Step Verification), 16 characters (optional) | [ ] |
| MAIL_FROM | Reset-code email | Same Gmail address (optional) | [ ] |

Non-secret settings (also in `.env`): SMTP_HOST, SMTP_PORT, DASH_DB, DASH_SOURCES, DASH_CATEGORIES, DASH_TIMEZONE, DASH_SYNC_MINUTES, DASH_SWEEP_MINUTES, DASH_READS_PER_MIN, DASH_BOT_LATE_HOURS, DASH_WRITEBACK, DASH_COOKIE_SECURE, DASH_APP_NAME, DASH_ACCENT.

Other files kept here: `DEMO-LOGINS.md`, `demo_credentials.txt` (fake demo accounts; copied from the app, not reviewed).
