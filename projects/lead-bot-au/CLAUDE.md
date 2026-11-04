# Lead Bot AU
Purpose: The Australia-only twin of the worldwide bot: finds AU businesses that can pay $500-1,000+ per month (AUD) and AU YouTube creators, with 8 extra AU columns (ABN, entity, GST ...). One Google Sheet. It never writes emails.
Code: `app\` (Python 3.12, own git). Folder standard: `F:\Github Repos\projects\README.md`. Original app notes: `app\CLAUDE.md`.

## How to run
- Install / check: `install\INSTALL.cmd` (or `install\INSTALL.cmd -Check`).
- Local test, no Google: `install\run-local.ps1` (Desktop shortcut "Lead Bot AU (local test)") = `python src\leadbot.py --local` with `secrets\.env` loaded; CSVs go to `app\local_sheet\`.
- Tests (from `app\`): `.venv\Scripts\python.exe src\selftest.py` then `.venv\Scripts\python.exe -m unittest discover -s tests`.
- Daily run: GitHub Actions workflow "Run AU Lead Bot" (19:00 and 07:00 UTC (`0 19 * * *`, `0 7 * * *`, about 6am/6pm Sydney)) in the app's GitHub repo.

## Secrets (names only; values in `secrets\.env` and GitHub repo secrets)
GOOGLE_SA, SHEET_ID_AU_ONLY (old name SHEET_ID still works), plus optional AI/data keys: see `secrets\SECRETS-CHECKLIST.md`.

## Status / next step
- 2026-11-05: packaged into the standard folder. Same code as worldwide; only `app\src\market.py` differs (MARKET = "AU"). Needs its OWN GitHub repo and its OWN sheet. Old zips (`au-only-lead-bot.zip` and the copy from `New File`) are in `archive\`.
- Installer tested in a temp copy (see PROGRESS.md). The GitHub run and live Google Sheets were NOT tested (need the user's logins).
- Next: user links the GitHub repo + secrets (SETUP-GUIDE section 6) and confirms the sheet(s) are shared with the robot email.

## Rules for Claude
- Never open or print `secrets\`. Sheet rows are append-only. Test on 5-10 rows (`--local`) before a full run. Never push without the user's OK.
- Sync code fixes with the twin app (`lead-bot-worldwide`) and keep each one's `src\market.py`.
