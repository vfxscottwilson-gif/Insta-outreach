# 04 Troubleshooting (outreach-bot)

## How to read the log
- Cloud: GitHub > repo > Actions > `generate-emails` > click the run > step `python -u generate.py`. First lines: `SKIP ...` for lead sheets, then `AI KEY REGISTRATION` (keys shown as the last 4 characters), then `N lead(s) queued...`, then progress, and last a line starting `DONE.` with counts (read, written, AI/template, rejected, queued, skipped, AI calls).
- Local: the PowerShell window of `install\run-bot.ps1`.
- In the sheet: `Leads > Note` says why each lead was skipped; `AI Usage` shows each key's calls, State and Last error; `Emails > Flags` shows warnings.

## Failure table (messages come from `generate.py`)
| You see | Meaning | Fix |
|---|---|---|
| `OUTREACH_SHEET_ID secret is missing` | No Outreach sheet ID | Create a NEW blank Google Sheet, share it with the service-account email as Editor, set `OUTREACH_SHEET_ID` |
| `OUTREACH_SHEET_ID is the same as a lead sheet` | Wrong sheet used | Use a separate sheet; the bot never writes to lead sheets |
| `GOOGLE_SA secret is missing or is not the full service-account JSON` | Empty or cut JSON | Paste the whole JSON file. Locally save it as `secrets\google-sa.json` |
| `Cannot open the Outreach sheet (APIError 403 / 404)` | Not shared, or wrong ID | Share with the `client_email` inside the JSON as Editor; recheck the ID in the sheet URL |
| `SKIP AU: cannot open the sheet` | Lead sheet not shared | Share with the service account (Viewer) |
| `SKIP XX: no ... secret set` | Normal for countries you do not use | Nothing |
| `SKIP XX: no lead tab found` | No tab has `Place Id` and `Company Name` headers | Fix the headers or set `COLUMN_ALIASES` |
| `<name>: IGNORED ... wrong format` | Key pasted wrongly (spaces, cut) | Copy it again; the message states the expected format |
| `BAD KEY for today` / HTTP 401 | Key revoked, deleted or wrong. The old Groq and OpenRouter keys were 401 on 2026-10-31 | Make a new key; run `diagnose-keys`; read `app\DIAGNOSIS.md` |
| `blocked by Cloudflare (error 1010)` on Groq | Not a key problem | Handled in code (custom User-Agent); if it returns, report it |
| `EXHAUSTED for today ... limit: 0` | Your Google project has no free quota for that model | Use a key from another project, or change `GEMINI_MODELS` |
| `429, paused 20s` | Per-minute limit | Normal; the next key is used meanwhile |
| `every AI key is spent for today` | Daily quota used up | Wait for the next day (Gemini resets 07:00/08:00 UTC), add keys, or set `TEMPLATE_FALLBACK` On |
| `No AI key is registered and TEMPLATE_FALLBACK is Off: nothing is drafted` | No usable key | Add a key or set `TEMPLATE_FALLBACK` On |
| Few drafts although many leads | Quota (about 400-700/day), `DAILY_TARGET` reached, or many leads skipped | Check `AI Usage` and `Leads > Note` |
| `AI draft rejected (...)` many times | Your `Email Rules` conflict with the checks (e.g. a word range) | Loosen the rule; the lead stays queued |
| Many `no usable email` | Leads have no valid address | Fix in the lead bot, not here |
| `Flags: no footer yet` | `SENDER_NAME` or `SENDER_ADDRESS` empty | Fill in the `Options` tab |
| Slow run / Sheets `429` | Sheets quota (about 19 reads a minute, shared with the lead bot) | Do not run both bots in the same minute; `retry()` already waits |
| Run stops at about 50 minutes | `MAX_RUN_MIN` | Normal; remaining leads wait. Raise `MAX_RUN_MIN` (the job limit is 60 minutes) |
| Option change has no effect | A GitHub Variable of that name overrides the tab | Delete or edit the Variable |
| Daily run did not start | Workflow disabled or repo inactive (GitHub rule, not verified here) | Actions tab > enable the workflow, run it once by hand |

## Local install problems
| Problem | Fix |
|---|---|
| `python` not found after install | Close the window and run `install\INSTALL.cmd` again |
| "running scripts is disabled" | Use the `-ExecutionPolicy Bypass` commands in `GUIDE\00` |
| Self-test fails | Run the self-test (below), read the first failing line; do not run live until it passes |

Self-test:
```
powershell -ExecutionPolicy Bypass -File install\run-bot.ps1 -SelfTest
```
Check what is installed (changes nothing):
```
powershell -ExecutionPolicy Bypass -File install\install.ps1 -Check
```

## Safety while fixing
Never paste a key or the service-account JSON into chat, an issue, or any file outside `secrets\`. Keep sending off.
