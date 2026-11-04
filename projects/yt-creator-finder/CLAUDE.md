# YT Creator Finder
Finds YouTube channel owners hiring editors/thumbnail designers (Upwork, Freelancer, LinkedIn Jobs, Remotive, YTJobs, YouTube search) and writes scored leads (PRIME/GROWING/REVIEW + AI pitch) to a Google Sheet. Runs on GitHub Actions 6x/day. Layout/rules: `F:\Github Repos\projects\README.md`.
- Local run (dry run, writes nothing to the Sheet): `app\.venv\Scripts\python.exe -m src.leadbot --dry-run --max-leads 10`. Tests: `-m pytest -q` in `app\` (offline). Install: `install\INSTALL.cmd`.
- Secrets NAMES: GOOGLE_SA, SHEET_ID, YOUTUBE_API_KEYS (required); GEMINI_API_KEYS, GROQ_API_KEYS, JINA_API_KEY, UPWORK_CLIENT_ID, UPWORK_CLIENT_SECRET, UPWORK_REFRESH_TOKEN (optional). Values in `secrets\.env` and GitHub Actions secrets. Details: `secrets\SECRETS-CHECKLIST.md`.
- `app\` = original repo with its git history (code rules in `app\CLAUDE.md`). Original on D:\All Automations Records\YT Leads Autmation is untouched. No database (Google Sheet).
- Docs: `docs\MASTER_PROMPT_yt-creator-client-finder.md`, sample leads CSV; old zips in `archive\`.
## Status / next step
- 2026-11-05: packaged. App never run against a real Sheet; Upwork path untested live. Next: create GitHub repo + 3 required secrets, run the workflow with dry_run, then a 10-lead pilot.
