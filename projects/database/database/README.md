# Database: SQLite (local)

- Engine: SQLite via Python, created and migrated by the app (`dash\db.py`) the first time `manage.py init` / the server runs.
- Live file: `app\dashboard\data\dash.db` (override with `DASH_DB` in `.env`). It does not exist until the installer has run once.
- Demo file (fake data): `app\dashboard\data\demo.db` (made by `manage.py demo`; safe to delete).
- Gitignored everywhere (`*.db`, `data\`). Not in any cloud.
- What it holds: users, sessions, leads synced from the sheets, assignments, approvals, audit log, Fernet-encrypted copies of employee passwords (key `DASH_PASSWORD_KEY` in `secrets\.env`).

## Back up
| Method | Command | Includes password copies + sessions? |
|---|---|---|
| Full (folder zip + online SQLite copy) | `powershell -ExecutionPolicy Bypass -File backups\backup.ps1` | Yes, keep private |
| App's own safe copy | `app\dashboard\.venv\Scripts\python.exe app\dashboard\manage.py backup` -> `data\backups\dash-<time>.db` | No (stripped) |

Keep `secrets\.env` and any `.db` backup apart: together they can decrypt employee passwords. Lose `.env` and the stored password copies become unreadable (logins still work; set new passwords).

## Restore
See `RESTORE.md`.
