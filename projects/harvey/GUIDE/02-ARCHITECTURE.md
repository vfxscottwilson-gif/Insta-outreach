# 02 Architecture

| Part | What | Where |
|---|---|---|
| Backend | Python package `harvey` (CLI `harvey`, heartbeat loop every 15 min, sub-agents for prospecting, writing, replies) | `app\harvey\` |
| Frontend | Local dashboard (FastAPI + static HTML/JS) at http://127.0.0.1:5555, private token link | `app\harvey\web\` |
| Database | SQLite file, local only | `app\data\harvey.db` |
| AI | Claude CLI subprocess using your Claude subscription (no API key) | outside this folder |
| Email | Gmail API / SMTP+IMAP / Microsoft 365 / Instantly, chosen in config | cloud (your provider) |
| Config | `app\harvey.yaml` (defaults) + `app\harvey.local.yaml` (yours) + `app\.env` (keys) | `app\` |
| Prompts / skills | Text files that steer the AI | `app\prompts\`, `app\skills\` |
| Tests | about 89 test files, pytest | `app\tests\` |

Upstream developer docs: `app\README.md`, `app\CLAUDE.md`, `app\docs\`.
