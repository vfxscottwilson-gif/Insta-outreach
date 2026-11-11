# secrets/ : SECRETS. Do not share, upload or commit.

This folder is gitignored (only `.gitignore` and the `SECRETS-*.md` files are tracked). Names and where each is used: `SECRETS-CHECKLIST.md`.

| File | What | Used by |
|---|---|---|
| `app.env.backup` | Copy of `app\.env` (Supabase URL + anon key, admin email, Supabase access token) | Installer copies it to `app\.env`; `database\*.mjs` read the token from it |
| `supabase-access-token.txt` | Supabase access token (fallback for scripts) | `database\lib.mjs` |
| `google-sa.json` | Google service-account key (Sheet mirror) | Installer, `scripts\load-google-secret.mjs` |
| `password-vault-key.txt` | `PASSWORD_VAULT_KEY`. Losing it makes stored password copies unreadable | `scripts\set-vault-key.mjs` |
| `.env` (optional, create yourself) | Add `DATABASE_URL=...` to enable the schema export | `database\cloud-export.ps1` |

Rules: keep off cloud drives and chat; if a key leaks, rotate it at its service, then update the file here. Backup zips include this folder.
