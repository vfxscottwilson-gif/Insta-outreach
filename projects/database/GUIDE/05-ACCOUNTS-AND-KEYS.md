# 05 Accounts and keys (names and IDs only; values live in `secrets/`)

| Service | Name | ID / account email | Where used | Secret lives in |
|---|---|---|---|---|
| Flask | DASH_SECRET_KEY | auto-generated | Session signing | `secrets\.env` |
| Fernet | DASH_PASSWORD_KEY | auto-generated | Admin-viewable password copies | `secrets\.env` |
| Google Cloud service account | service_account.json | (the `...iam.gserviceaccount.com` email, shown in the app on Sources & sync) | Read the lead sheets | `secrets\service_account.json` |
| Google Sheets | sheet IDs (US, CA, GB, AU, NZ, IE, AE, SA, QA, YouTube, AU-only, YT finder) | not yet supplied by the user | Sources | `secrets\sources.yaml` or entered in the app (stored in the database) |
| Gmail (optional) | SMTP_USER, SMTP_PASSWORD, MAIL_FROM | the sending Gmail address | Reset-code emails | `secrets\.env` |

How to get each: `secrets\SECRETS-CHECKLIST.md`. Demo accounts (fake): `secrets\DEMO-LOGINS.md`, `secrets\demo_credentials.txt`.
Not needed: Supabase, GitHub, hosting.
