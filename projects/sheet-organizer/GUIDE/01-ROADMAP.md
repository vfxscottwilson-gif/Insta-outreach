# 01 Roadmap (sheet-organizer)

## Where it stands
The code is finished and working by design (see `app\SETUP_GUIDE.md`). It needs your Google Sheet, a service account, an AI key and a GitHub repo. No separate ROADMAP or DIAGNOSIS document exists for this bot.

## Steps
| # | Step | Who | Blocker | Done |
|---|---|---|---|---|
| 1 | Create the Google Sheet with an `Inbox` tab (or name yours and set `INBOX_TAB`) | Owner | none | [ ] |
| 2 | Google Cloud: enable the Sheets API, create a service account, download the JSON key, share the Sheet (Editor) with its `client_email` | Owner | Google login | [ ] |
| 3 | Get at least one AI key (Gemini / Groq / OpenRouter) | Owner | Provider account | [ ] |
| 4 | Upload `organizer.py`, `requirements.txt`, `.github/workflows/organize.yml` to a private GitHub repo; add secrets `SHEET_ID`, `GOOGLE_SA`, AI key(s) | Owner | GitHub login | [ ] |
| 5 | Actions > "Organize my sheet" > Run workflow with `dry_run` = `yes`; read the log | Owner | steps 1-4 | [ ] |
| 6 | Real run with Variable `RUN_LIMIT` = 10; check the tabs; then remove the limit | Owner | step 5 | [ ] |
| 7 | Optional: Figma token + board link (`FIGMA_TOKEN`, `FIGMA_FILE`) | Owner | Figma account | [ ] |
| 8 | Every 2 months: press Run workflow once so GitHub does not pause the schedule | Owner | none | [ ] |
| 9 | Phase 2 (not built): Gmail sorting (needs an OAuth login flow) | Later | not built | [ ] |
| 10 | Phase 2 (not possible with Figma's web API): arranging the canvas; needs a Figma plugin | Later | Figma limit | [ ] |

## Known limits
- Free AI tiers cap about 150 notes a run; extras wait a day.
- Two differently worded notes about one item can become two rows.
- Runs once a day, not live; GitHub may start it a few minutes late.

## How to know it works
`_Log` gets a line each day, the Inbox notes appear in the filing tabs, and `Attention Needed` shows "All clear" or real items.
