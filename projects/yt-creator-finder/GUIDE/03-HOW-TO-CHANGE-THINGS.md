# 03 How to change things
| I want to... | Do this |
|---|---|
| Change minimum subscribers / recency | GitHub Variables MIN_SUBS, MAX_DAYS_SINCE_UPLOAD (or `app\config.yaml`) |
| Cap leads per day | Variable DAILY_LEAD_TARGET (0 = no cap) |
| Spend fewer YouTube quota units | Variable YT_SEARCH_BUDGET |
| Change the AI models | `app\config.yaml` (never hard-code model names in code) |
| Change run times | `cron` in `app\.github\workflows\run-lead-bot.yml` (UTC) |
| Add a lead source | New file in `app\src\sources\`, call it from `leadbot.py`, add a test in `app\tests\` |
| Run tests | `app\.venv\Scripts\python.exe -m pytest -q` (from `app\`) |
After any code change: commit inside `app\`, push to GitHub; the next scheduled run uses it.
