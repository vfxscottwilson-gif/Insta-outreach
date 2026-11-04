# 01 Roadmap (outreach-bot)

## Where it stands
v3 code is finished and passes its offline self-test. It waits on things only you can do (logins, fresh keys). Source of truth for the order of work: `app\ROADMAP.md`.

## Steps
| # | Step | Who | Blocker | Done |
|---|---|---|---|---|
| 1 | Create a NEW blank Google Sheet "Outreach"; make a Google service account; share the sheet (Editor) and every lead sheet (Viewer) with its email | You | Google login | [ ] |
| 2 | Create the GitHub repo, upload the `app\` contents (workflows included), add secrets (`GOOGLE_SA`, `OUTREACH_SHEET_ID`, `SHEET_ID_*`) | You | GitHub login | [ ] |
| 3 | Make fresh AI keys: the old Groq and OpenRouter keys were dead (401); each Gemini key in its OWN Google project | You | Provider logins | [ ] |
| 4 | Run Actions > `diagnose-keys`; every key must show OK | You | step 3 | [ ] |
| 5 | Dry run (`dry_run` = On, `limit` = 10), then 10 real drafts; read them | You | step 4 | [ ] |
| 6 | Fill `SENDER_NAME` and `SENDER_ADDRESS` in the `Options` tab (legal footer) | You | none | [ ] |
| 7 | First week: `DAILY_TARGET` 100-200, tune the `Email Rules` tab | You | none | [ ] |
| 8 | Raise to 400-700 a day once rejected drafts are few | You | step 7 | [ ] |
| 9 | Pick an inbox option (`app\INBOX_OPTIONS.md`, `INBOX_SETUP.md`); optionally `INBOX_ROTATION` and `FOLLOW_UPS` On | You | none | [ ] |
| 10 | Much later: sending / reply tracking (`app\phase2_parked\`). Parked on purpose; do not enable | Later | decision | [ ] |

## Known limits
- Free AI quota allows about 400-700 drafts a day; leads not reached wait for the next run.
- Sheets read limit about 19 a minute, shared with the lead bot.
- Sending is manual by design.

## How to know it works
The `Emails` tab gains rows each day, `AI Usage` shows calls per key, and the log ends with a `DONE.` line.
