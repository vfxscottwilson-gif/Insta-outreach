# sheet-organizer
Purpose: files notes pasted in a Google Sheet `Inbox` into Tasks / Problems / Achievements / Ideas / Resources, flags overdue items, writes a monthly report. Source in `app\` (own git; `app\CLAUDE.md` has the code rules). Layout rules: `F:\Github Repos\projects\README.md`.
Run: `install\INSTALL.cmd` once, then `install\run.cmd organizer.py` (DRY_RUN=yes unless `secrets\.env` sets DRY_RUN=no). Cloud: GitHub Actions "Organize my sheet" (daily).
Secrets (names only): SHEET_ID, GOOGLE_SA, GEMINI_API_KEY, GROQ_API_KEY, OPENROUTER_API_KEY, FIGMA_TOKEN (+ optional settings in `secrets\SECRETS-CHECKLIST.md`). Values only in `secrets\`.
## Status / next step
- 2026-11-05: packaged from `D:\All Automations Records\Figma Organizer\sheet-organizer` (copy; original untouched). Installer tested in a temp copy (install, imports, run reaches the AI-key check). Not tested against a real Sheet/AI (needs the owner's logins).
- Next: owner adds Google key + one AI key to `secrets\`, does a dry run, then a live run on 5-10 rows (RUN_LIMIT=10).
