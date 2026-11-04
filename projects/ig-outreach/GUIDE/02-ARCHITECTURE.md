# 02 Architecture

- Front end: none. The Google Sheet is the interface (Outreach Log, Today Queue, Accounts, Run Log, your leads tab).
- Back end: Python scripts in `app\`, run on GitHub Actions (daily) or locally via `install\run.cmd`.
- Hosting: GitHub Actions (private repo). Database: the Google Sheet.
- Data flow: leads tab -> `main.py` (sync, expire stale, follow-ups, re-queue, AI writes DM, `rules.py` checks it) -> Today Queue -> you send with `send_assist.py` -> log updated.

| Want to change | File |
|---|---|
| Message angles | `app\styles.py` |
| Safety checks (length, spam words, links) | `app\rules.py` |
| AI providers / failover | `app\ai.py` |
| Scheduling, caps, follow-ups | `app\main.py` (settings are env vars) |
| Cloud schedule | `app\.github\workflows\outreach.yml` |
| Exact send-time stamp in the Sheet | `app\apps_script.gs` |
