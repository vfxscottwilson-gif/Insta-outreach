# Lead Bot Worldwide
Purpose: Finds local businesses in the US, Canada, UK, Australia, New Zealand and Ireland (optional UAE, Saudi Arabia, Qatar) that can pay $500-1,000+ per month, plus YouTube creators. It writes facts-only contact data, a Segment, an ICP score and a short Lead Insight into one Google Sheet per country. It never writes emails (the outreach bot does).
Code: `app\` (Python 3.12, own git). Folder standard: `F:\Github Repos\projects\README.md`. Original app notes: `app\CLAUDE.md`.

## How to run
- Install / check: `install\INSTALL.cmd` (or `install\INSTALL.cmd -Check`).
- Local test, no Google: `install\run-local.ps1` (Desktop shortcut "Lead Bot Worldwide (local test)") = `python src\leadbot.py --local --country US` with `secrets\.env` loaded; CSVs go to `app\local_sheet\`.
- Tests (from `app\`): `.venv\Scripts\python.exe src\selftest.py` then `.venv\Scripts\python.exe -m unittest discover -s tests`.
- Daily run: GitHub Actions workflow "Run Lead Bot" (20:00 and 08:00 UTC (`0 20 * * *`, `0 8 * * *`)) in the app's GitHub repo.

## Secrets (names only; values in `secrets\.env` and GitHub repo secrets)
GOOGLE_SA, SHEET_ID_US (required, holds the Master Dashboard), SHEET_ID_CA, SHEET_ID_GB, SHEET_ID_AU, SHEET_ID_NZ, SHEET_ID_IE, SHEET_ID_AE, SHEET_ID_SA, SHEET_ID_QA, SHEET_ID_YOUTUBE, plus optional AI/data keys: see `secrets\SECRETS-CHECKLIST.md`.

## Status / next step
- Latest release: `Lead Bot Worldwide v6.zip` (project root). Release rule: global CLAUDE.md section 14 (next delivery = `Lead Bot Worldwide v7.zip`; move older zips to `Archive\`).
- 2026-11-11: v6. Audit fixes (failed sheets now fail the job, UK/YT aliases passed), benchmark gates + `Benchmark Check` column (10,000/mo revenue floor, 1 post/30d; sources in `What Changed.md`), clean phones (no '+'), JSON-LD/Facebook/link-in-bio facts, dedupe, tenacity + Scrapling, pinned requirements, docs renamed to Title Case (`Start Here.md` is the entry point). 114 unit tests + selftest pass. Live Google Sheets and the GitHub run are NOT tested (need the user's logins).
- 2026-11-05: packaged into the standard folder. Current version = `au-lead-bot\au-lead-bot` (its CLAUDE.md is the newest, 2026-11-01 05:12, and says Prospeo/Snov/NZBN/Disify/Reacher are wired). The sibling `au-lead-bot-v5` and the outer `au-lead-bot` wrapper have identical code and an older CLAUDE.md, so they were archived (`archive\au-lead-bot-v5-folder`, `archive\au-lead-bot-outer-wrapper`). Old zips v2-v5 and `au-lead-bot.zip` are in `archive\`.
- Installer tested in a temp copy (see PROGRESS.md). The GitHub run and live Google Sheets were NOT tested (need the user's logins).
- Next: user links the GitHub repo + secrets (SETUP-GUIDE section 6) and confirms the sheet(s) are shared with the robot email.

## Rules for Claude
- Never open or print `secrets\`. Sheet rows are append-only. Test on 5-10 rows (`--local`) before a full run. Never push without the user's OK.
- Sync code fixes with the twin app (`lead-bot-au`) and keep each one's `src\market.py`.
