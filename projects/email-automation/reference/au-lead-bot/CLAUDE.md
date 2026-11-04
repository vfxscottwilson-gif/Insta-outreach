# Lead Bot v5 (worldwide edition)

## Purpose
Daily $0 lead generation for a video/social agency: finds local businesses (US, CA, UK, AU, NZ, IE; optional AE/SA/QA) that can pay $500-1k+/mo, plus YouTube creators. Writes facts-only contact data, Segment, ICP score and a Lead Insight to per-country Google Sheets. It never writes emails (the outreach bot does).

## How to run
- Local, no Google: `python src/leadbot.py --local --country US` (writes `local_sheet/US/*.csv`).
- Tests: `python src/selftest.py` then `python -m unittest discover -s tests`.
- GitHub Actions: workflow "Run Lead Bot" (`.github/workflows/run-lead-bot.yml`), cron `0 20 * * *` and `0 8 * * *` UTC, plus manual `workflow_dispatch`. Jobs: setup, collect per country (5 parallel), finish.

## Secrets needed (names only)
- Required: `GOOGLE_SA`, at least `SHEET_ID_US`.
- Sheets (each optional, missing = skipped): `SHEET_ID_CA`, `SHEET_ID_GB`, `SHEET_ID_AU`, `SHEET_ID_NZ`, `SHEET_ID_IE`, `SHEET_ID_AE`, `SHEET_ID_SA`, `SHEET_ID_QA`, `SHEET_ID_YOUTUBE`.
- Optional AI: `GEMINI_API_KEY_1/2/3`, `GROQ_API_KEY`, `CEREBRAS_API_KEY`, `OPENROUTER_API_KEY`, `MISTRAL_API_KEY`.
- Optional data: `SERPER_API_KEY`, `HUNTER_API_KEY`, `GOOGLE_PLACES_API_KEY`, `YOUTUBE_API_KEY_1/2`, `APIFY_API_TOKEN`, `APOLLO_API_KEY`, `BRAVE_API_KEY`, `ABN_GUID`, `ZENROWS_API_KEY`, `JINA_API_KEY`.
- Variables: `KEY_CHECK`, `LEAD_MATRIX`, `TIMEZONE`. Full list: `SECRETS_GUIDE.md`.

## Key files
- `src/leadbot.py`: main program (search, enrich, score, append to sheets).
- `src/insight.py`: Lead Insight (AI or fact-only fallback).
- `src/enrich.py`: website reader (emails, phones, socials, decision maker).
- `src/quality.py`, `src/score.py`: segments and ICP score. `src/market.py`: edition switch.
- `src/keys.py`: secret registry and shape checks. `src/ai.py`: AI key failover.
- `src/osm.py`, `src/places.py`, `src/yt.py`, `src/optional.py`: sources and optional helpers.
- `src/defaults.py`: first-run tab contents, niches, locations, Rules.
- `CONTRACT.md`: sheet interface the outreach bot relies on (keep stable, version it).
- `00_START_HERE_SETUP_GUIDE.md`, `SECRETS_GUIDE.md`, `SHEETS_SETUP.md`, `UPGRADE_V5.md`: setup and change notes.

## Status / known issues
- v5 (2026-11-01): append-only sheets, Lead Insight, Stats/Master Dashboard, one secret per key. 60 selftest checks, 92 unit tests.
- Pending: free-tier AI limits change (429 = fact-only insights); decision-maker/personal-email coverage only ~20-35% on free sources; Gulf sheets thin without Serper/Apify; Tomba not wired (Prospeo/Snov/NZBN/Disify/Reacher wired, untested live); Seen tab nears 10M cells in about a year.
- AU-only twin: `Lead generation/au-only-lead-bot` (same code, only `src/market.py` differs).

## Rules for Claude
- Never commit secrets; do not open .env, Keys or "all info" files.
- Test on 5-10 rows first (`--local`) before any full run.
- Lead sheet rows are append-only: never sort, delete or rewrite existing rows (incl. Status, My Notes).
- Paid APIs stay optional; a missing or bad key must never crash the bot.
- Decision-maker names are facts only (printed on site or public result), never guessed.
- Keep `CONTRACT.md` stable; change it only with a new version line. Copy code fixes to the AU-only repo, keep its `market.py`.
