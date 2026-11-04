# secrets/ : SECRETS. Do not share, upload or commit.

This folder is gitignored. It holds the copies the installer needs on a new PC.

| File | What | Used by |
|---|---|---|
| `.env` | All keys (database URL + password, Supabase secret key, Google OAuth, AI keys, Cloudflare, admin login) | Installer copies it to `app\.env` |
| `sheet-reader.json` | Google service-account key (reads/writes the Sheets) | Installer copies it to `%USERPROFILE%\.secrets\` and sets `GOOGLE_SA_JSON` |
| `accounts.local.csv` | The list of sender accounts | Engine seeding |
| `DEMO-LOGINS.md` | Sample-data demo logins (not real) | Web demo build |

Rules: keep this folder off cloud drives and chat; if a key leaks, rotate it at its service. Originals still exist in `app\` and `C:\Users\<you>\.secrets\`; these are copies. Re-copy after any key change (`app\.env` > `secrets\.env`).
