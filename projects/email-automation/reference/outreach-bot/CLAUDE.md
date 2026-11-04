# outreach-bot (v3) - CLAUDE.md

## Purpose
Drafts personalised cold emails (fact-based, nothing sent) for a solo video editor offering a free 30-60s sample reel
to local businesses. Reads all per-country lead sheets, writes drafts into one **Outreach** Google Sheet; target
400-700 drafts/day. Sending is parked and OFF (a human copies and sends).

## How to run
- Local: `pip install -r requirements.txt` (gspread), `python selftest.py` (offline), `python generate.py`.
- GitHub Actions `generate-emails`: daily `0 10 * * *` UTC + manual (inputs `limit`, `dry_run`); runs selftest first.
- GitHub Actions `diagnose-keys`: manual; tests AI keys (masked output) via `tools/diag_keys.py`.

## Secrets needed (names only; GitHub Actions secrets)
- Required: `GOOGLE_SA`, `OUTREACH_SHEET_ID`.
- Lead sheets (all optional): `SHEET_ID_US/CA/GB(UK)/AU/NZ/IE/AE/SA/QA/YOUTUBE/AU_ONLY`, `EXTRA_LEAD_SHEET_IDS`,
  legacy `SHEET_ID`, `LEADS_SHEET_ID`.
- AI (all optional): `GEMINI_API_KEY_1..5`, `GROQ_API_KEY`, `GROQ_API_KEY_2`, `MISTRAL_API_KEY`,
  `OPENROUTER_API_KEY`, plus legacy `GEMINI_KEY(S)`, `GROQ_KEY`, `OPENROUTER_KEY`, `AI_KEYS`.
- Variables: `RUN_LIMIT`, `DRY_RUN`, `DAILY_TARGET`, `TEMPLATE_FALLBACK`, `*_MODELS`. Full table: `SECRETS_GUIDE.md`.

## Key files
- `generate.py` - the whole bot (~1950 lines): multi-sheet read, dedupe, AI batches of 5, legal footers.
- `selftest.py` - offline tests; also run in CI.
- `rules.md` - base AI writing rules (user rules go in the sheet's "Email Rules" tab).
- `tools/diag_keys.py` - key tester used by `diagnose-keys`.
- `START_HERE.md` (setup), `ROADMAP.md` (order of work, AI quota maths), `SECRETS_GUIDE.md`.
- `INBOX_OPTIONS.md`, `INBOX_SETUP.md` - sending/inbox choices. `DIAGNOSIS.md` - why old keys died.
- `phase2_parked/` - `send.py`, `replies.py`, disabled workflow; needs `SEND_ENABLED=yes`. Do not enable.

## Status / known issues
- **This is the current bot (labelled v3; newest, generate.py modified 2026-11-01).** `outreach-bot-v2` is the older
  generation: one lead sheet ("All Leads") -> "Ready to Send" tab, writes Status back to the lead sheet, ~1340 lines.
  v3: many lead sheets read-only, one Outreach sheet (Leads/Emails/Options/Email Rules/Inboxes/AI Usage), optional
  inbox rotation and day 3/7 follow-ups, GB/IE free-mail skipped, template fallback off by default.
- DIAGNOSIS (2026-10-31): old Groq/OpenRouter keys were dead (401), Groq blocked by default User-Agent, 3 Gemini keys
  shared one project quota. Fixed in code; user must create new keys (each Gemini key in its OWN project).
- Realistic output with free keys: ~400-700 AI drafts/day; unreached leads wait for the next run.
- Sheets limit: <=19 reads/min (service account shared with the lead bot; see Lead generation/CONTRACT.md).

## Rules for Claude
- Never commit, print or write secret values (keys, service-account JSON); do not open key files or `.env`.
- Test on 5-10 rows first (`dry_run=On`, `limit=5..10`) before any full run.
- Keep paid APIs optional: free keys and the template fallback must keep working.
- Keep sending OFF; never write to lead sheets; never log emails, names or keys.
