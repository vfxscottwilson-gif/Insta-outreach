# ig-outreach (v3)
Purpose: sheet leads -> personalised IG DMs + follow-up schedule; a human sends via `send_assist.py` (no auto-sender by design). Source in `app\` (own git; `app\CLAUDE.md` has the code rules). Layout rules: `F:\Github Repos\projects\README.md`.
Run: `install\INSTALL.cmd` once, then `install\run.cmd main.py --sync-only` (safe), `main.py` (full), `send_assist.py`. Cloud: GitHub Actions "Daily outreach prep".
Secrets (names only): GOOGLE_SERVICE_ACCOUNT_JSON, SHEET_ID, AI_API_KEYS, OFFER, IG_ACCESS_TOKEN, IG_USER_ID (+ optional settings in `secrets\SECRETS-CHECKLIST.md`). Values only in `secrets\`.
## Status / next step
- 2026-11-05: packaged from `D:\All Automations Records\Insta outreach Automation\ig-outreach` (copy; original untouched). Installer tested in a temp copy (install, imports, run reaches the settings check). Not tested against the real Sheet/AI/Instagram (needs the owner's logins).
- Next: owner adds Google key + AI keys to `secrets\`, runs a 5-10 lead test with one account.
