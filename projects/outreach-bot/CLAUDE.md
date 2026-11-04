# outreach-bot (v3)
Drafts personalised cold emails from lead Google Sheets into one Outreach sheet; sends nothing. Python, only dependency gspread. Layout/rules: `F:\Github Repos\projects\README.md`. Bot details: `app\CLAUDE.md`.
## Run
- Install: `install\INSTALL.cmd` (`-Check` = dry). Test: `install\run-bot.ps1` (dry run), `-Live -Limit 10`, `-SelfTest`.
- Daily cloud run: GitHub Actions `generate-emails` (workflow in `app\.github\workflows`).
## Secrets (names only; in `secrets\.env`, `secrets\google-sa.json`)
GOOGLE_SA, OUTREACH_SHEET_ID, SHEET_ID_<COUNTRY>, GEMINI_API_KEY_1..5, GROQ_API_KEY(_2), MISTRAL_API_KEY, OPENROUTER_API_KEY. See `secrets\SECRETS-CHECKLIST.md`.
## Status / next step
- 2026-11-05: packaged from `D:\All Automations Records\Draft Creating automation Code\outreach-bot`. Installer and selftest (58/58) tested in a temp copy. Not tested: live Sheets/AI run (needs logins).
- Next: user makes fresh AI keys, Outreach sheet, GitHub secrets; dry run 5-10 rows.
