# 02 Architecture: how the bot works

All paths are inside `app\`. One run = one start of `python -m src.leadbot` (file `src\leadbot.py`, function `run`).

## Data flow (input -> steps -> output)
1. **Input**: settings from `config.yaml` (any key can be overridden by an UPPER_CASE environment variable of the same name) and secrets from environment variables (or `app\.env` on your PC). `src\config.py` loads them. Missing required secret -> prints `[FATAL] ...` and exits with code 1.
2. **Open the Sheet** (skipped in a dry run). `src\sheets_manager.py` opens the Sheet with `GOOGLE_SA` + `SHEET_ID`, creates missing tabs, adds missing columns at the end, and reads the dedup sets (existing Lead_IDs, emails, and the `Blacklist` tab). If the Sheet cannot be opened the run continues and buffers leads in `pending_leads.json`.
3. **Flush old buffer**: leads saved by an earlier failed write are written first.
4. **Discover candidates**, strongest intent first. Each source is wrapped so one failure never stops the others:
   - `ytjobs` (YTJobs job pages read through Jina Reader; cursor kept in the `_State` tab)
   - `upwork` (official API, needs 3 keys), `linkedin` (public guest listings), `freelancer` (public API), `remotive` (public API, at most every 6 hours)
   - `web_search` (DuckDuckGo, best effort)
   - `youtube_search` "hiring" and "niche" modes (YouTube API, 100 units per search, budget `yt_search_budget`)
5. **Resolve**: find the YouTube channel for each candidate (from sample video IDs, @handle, or a limited company-name search, `company_channel_lookups`).
6. **Dedupe**: one candidate per channel (strongest signal wins). Candidates with no channel stay as "platform jobs".
7. **Qualify channel owners** (`src\scoring.py`): hard gates (blacklisted, freelancer-looking channel, `min_subs`, `max_subs`, `max_days_since_upload`), then 0-10 score. Recent videos come from the free RSS feed, with the API as fallback.
8. **Enrich** (`src\enrichment\`): `contacts.py` finds emails, socials, phone, website and checks the email domain (MX); `country.py` infers the country; `youtube.py` wraps the API and handles several keys and quota.
9. **AI** (`src\ai_insight.py`): Gemini, then Groq, then a built-in template. Output: `AI_Lead_Insight`, `Recommended_Pitch_Angle`, `AI_Source`.
10. **Route**: score >= `prime_score` (7) PRIME, >= `growing_score` (5) GROWING, else REVIEW; hidden subscriber count is always REVIEW. Leads below `min_score_to_write` (3) are only counted in the Run Log. Role "thumbnail" goes to the thumbnail tab, everything else to the editing tab.
11. **Output**: leads are written in batches of 10 by column NAME. In a dry run they are printed as a table (and saved to a CSV when `--export` is given).
12. **Finish** (`finish`): saves `_State`, appends the Run Log rows (one `SUMMARY` row per run), refreshes the `Master Dashboard`. Returns exit code 0.

## Modules
| File | What it does |
|---|---|
| `src\leadbot.py` | Orchestrator and command line (`--dry-run`, `--max-leads N`, `--export file.csv`) |
| `src\config.py` | Loads config.yaml + env; `require()` checks required secrets |
| `src\net.py` | HTTP session with retries, `safe_call` (never raises), circuit breaker (5 failures in a row mark a source DOWN for the run), Jina Reader, run log with secret masking, PKT/Pacific clocks |
| `src\sources\*.py` | One file per lead source (`common.py` = shared Candidate type and platform names) |
| `src\enrichment\*.py` | YouTube API/RSS, contacts, country |
| `src\scoring.py` | Gates, score, segment, tab routing |
| `src\ai_insight.py` | AI providers, auto-picks a current "flash"/"instant" model if the configured one is gone |
| `src\sheets_manager.py` | Tabs, columns, dedup, batched writes with retry on 429/5xx, dashboard, `pending_leads.json` buffer; blocks formula injection (cells starting `=`, `+`, `-`, `@` get a leading `'`) |
| `src\state.py` | Counters kept in the hidden `_State` tab (a GitHub runner forgets everything between runs) |
| `tools\upwork_auth.py` | One-time helper to get the Upwork refresh token |
| `tests\` | Offline tests (`pytest`) |

## Storage
- **Google Sheet** (the only database). Tabs: `YouTube_Video_Editing_Leads`, `YouTube_Thumbnail_Design_Leads`, `Master Dashboard`, `Blacklist`, `Run Log`, and hidden `_State` (keys: leads per day, YouTube units per Pacific day, YTJobs cursor, query rotation positions, health text, Upwork token).
- Local files in `app\` (all gitignored): `.env`, `pending_leads.json`, `.state_local.json` (used when dry run or the Sheet is unreachable), `leadbot.log` (GitHub run only).
- GitHub Actions cache keeps `pending_leads.json` between runs; the log is uploaded as an artifact for 14 days.

## External APIs
YouTube Data API v3 and YouTube RSS; Google Sheets and Drive API; Gemini; Groq; Jina Reader (`r.jina.ai`); Upwork API; Freelancer.com public API; Remotive API; LinkedIn guest job pages; DuckDuckGo HTML. Only YouTube, Sheets (and Upwork if used) need setup; the AI and Jina keys are optional.

## Schedule
`.github\workflows\run-lead-bot.yml`: cron `17 1,4,7,10,13,16 * * *` (UTC) = 06:17, 09:17, 12:17, 15:17, 18:17, 21:17 Pakistan time. Also manual start ("Run workflow") with inputs `dry_run` and `max_leads`. Python 3.12, timeout 45 minutes, only one run at a time (`concurrency: lead-bot`). A keepalive step stops GitHub from disabling the schedule after 60 idle days.

## Rules baked into the code
Exit code 0 on data errors (red only when a required secret is missing or GOOGLE_SA is unreadable); no Upwork/Fiverr scraping, no CAPTCHA bypass, no SMTP probing; no daily lead cap by default (`daily_lead_target: 0`); model names live in `config.yaml`, never in code. Full list: `app\CLAUDE.md`.
