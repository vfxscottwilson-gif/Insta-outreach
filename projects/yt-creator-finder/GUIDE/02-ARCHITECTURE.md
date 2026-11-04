# 02 Architecture
| Part | Where | Notes |
|---|---|---|
| Orchestration | `app\src\leadbot.py` | `python -m src.leadbot [--dry-run] [--max-leads N] [--export file.csv]` |
| Sources | `app\src\sources\` | ytjobs (via Jina), upwork (official API), freelancer (public API), linkedin_jobs (guest listings), remotive, youtube_search, web_search (DuckDuckGo, best effort) |
| Enrichment | `app\src\enrichment\` | YouTube API + RSS, contacts (emails, socials, MX), country inference |
| Scoring | `app\src\scoring.py` | gates, score, routing to PRIME / GROWING / REVIEW |
| AI | `app\src\ai_insight.py` | Gemini, then Groq, then a template (never fails) |
| Output | `app\src\sheets_manager.py`, `app\src\state.py` | Google Sheet tabs, de-duplication, hidden `_State` tab for quotas and token |
| Settings | `app\config.yaml` | any key overridable by an UPPER_CASE environment variable |
| Schedule | `app\.github\workflows\run-lead-bot.yml` | cron `17 1,4,7,10,13,16 * * *` UTC; keepalive step stops GitHub disabling it after 60 days |

Cloud: GitHub Actions + Google Sheet + free APIs. Local: optional test copy. Rules (no Upwork/Fiverr scraping, no CAPTCHA bypass, exit code 0 on data errors): `app\CLAUDE.md`.
