# 02 Architecture

One Python process: `app\dashboard\manage.py serve` runs the Flask app under waitress (port 8080) plus a background sync thread.

| Part | Where | Notes |
|---|---|---|
| Web app (pages, login, admin) | `app\dashboard\dash\` (`__init__.py` create_app, `auth.py`, `admin.py`, `leads.py`, `dashboard.py`...), `templates\`, `static\` | Server-rendered, strict CSP |
| Sheet reading | `sync.py`, `sources.py`, `adapters.py` | Read-only; 45 reads/min budget (Google limit 60); `fixture.py` = offline CSV source for tests/demo |
| Write-back | `writeback.py` | OFF by default (`DASH_WRITEBACK`) |
| Database | `data\dash.db` (SQLite) | `db.py` migrations |
| Password vault | `vault.py` | Fernet copies, key `DASH_PASSWORD_KEY` |
| Reset-code mail | `mailer.py` | SMTP; prints to console if not configured |
| Tests | `tests\` | Use temp databases and fixtures only |
| Design preview | `app\web` (Vite + React, mock data) | Optional; not connected to the app |

Cloud: only Google Sheets (read). Everything else is local. Settings are read from `app\dashboard\.env` (copy of `secrets\.env`) and real environment variables.
