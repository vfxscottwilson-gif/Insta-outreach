# secrets/ : SECRETS. Do not share, upload or commit.

Gitignored by the hub. Holds what the installer needs on a new PC.

| File | What | Used by |
|---|---|---|
| `.env` | Harvey keys (names in SECRETS-CHECKLIST.md) | Installer copies it to `app\.env` |

No keys existed on the original PC when this folder was packaged, so `.env` is created by the installer on first run. The Claude login lives outside this folder (Claude CLI, Windows user profile): log in again on a new PC. `app\data\dashboard-token` (created by Harvey) is also private.
| harvey-db-snapshot-2026-11-05.db | copy of the original SQLite database (prospect data) | restore: see database\README.md |
