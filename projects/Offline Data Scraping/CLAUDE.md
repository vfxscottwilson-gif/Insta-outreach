# Offline Data Scraping
Purpose: local (this PC only) lead scraper for a social media agency. ICP = local business able to pay US$500+/month, active on Instagram (2+ posts in 30 days). Output = one Excel file per country, one Title Case tab per niche. Facts only, never writes emails.
Engine = copy of `lead-bot-worldwide\app\src` v6 (2026-11-11) plus 4 small patches. Runner = `app\run.py`. User guide = `Start Here.md`.

## How to run
- Install / check: `install\INSTALL.cmd` (or `install\INSTALL.cmd -Check`).
- Pilot (about 8 leads): `Pilot Test.cmd` = `app\.venv\Scripts\python.exe run.py --pilot` (from `app\`).
- Full run: `Run Scraper.cmd`. Export only: `run.py --export`. Settings only: `run.py --setup`.
- Tests (from `app\`): `.venv\Scripts\python.exe run.py --check`, `.venv\Scripts\python.exe src\selftest.py`, `.venv\Scripts\python.exe -m unittest discover -s tests`.

## Secrets (names only, all optional, in `secrets\.env`)
IG_ACCESS_TOKEN, IG_USER_ID, APIFY_API_TOKEN, SERPER_API_KEY, GOOGLE_PLACES_API_KEY, HUNTER_API_KEY. See `secrets\SECRETS-CHECKLIST.md`.

## Engine patches (keep when syncing from lead-bot-worldwide)
- `src\ai.py`: provider `local` (key `local:<model>`, env `LOCAL_LLM_URL`, `AI_TIMEOUT`).
- `src\keys.py`: `LOCAL_LLM_KEY` spec.
- `src\localsheet.py`: atomic save.
- `src\leadbot.py`: `sh.save()` at the end of `commit()` in local mode.

## Status / next step
- 2026-11-11: v1 delivered (`Offline Data Scraping v1.zip`). 117 tests pass; pilot wrote 1 real lead. See `PROGRESS.md` and `HANDOFF.md`.
- Next: user provides the local LLM model name; test the local AI path; optional Instagram token so the 2-posts rule is measured.

## Rules for Claude
- Never open or print `secrets\`. `app\data\` is append-only memory: never edit or delete lead rows.
- User edits only `Settings\*.csv`; never overwrite an existing Settings file.
- Pilot (`--pilot`) before any full run. Never push without the user's OK.
- Code fixes to the engine go to `lead-bot-worldwide` and `lead-bot-au` too (three copies now).
