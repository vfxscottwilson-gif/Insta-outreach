# ig-outreach: Setup guide

For a non-expert on Windows 10. Never write secret values in this file.

## 1. What this app is
Reads leads from your Google Sheet, reads public Instagram bios (optional), writes a short DM (under 40 words, 9 rotating angles, free-sample offer), schedules DMs across your accounts with follow-ups on days 4/8/12. You send each DM yourself; `send_assist.py` makes it one click. It never logs into Instagram or sends by itself (on purpose: that gets accounts banned). Main screens: the Google Sheet tabs (Outreach Log, Today Queue, Accounts, Run Log).

## 2. Accounts needed
| Service | Why | Free? | Sign-up link |
|---|---|---|---|
| Google (Sheets + Cloud) | Sheet is the database; service account lets the bot edit it | Yes | console.cloud.google.com |
| AI provider(s), at least 2 | Writes the DMs, fails over if one is limited | Free tiers exist (Gemini, Groq, OpenRouter) | aistudio.google.com/apikey, console.groq.com/keys, openrouter.ai/keys |
| GitHub (private repo) | Runs the daily job in the cloud | Yes (about 150-250 free minutes/month used) | github.com |
| Meta developer (optional) | Reads Instagram profiles | Yes | developers.facebook.com |

Google service-account steps: create a Cloud project, enable the Google Sheets API, create a Service Account, add a JSON key, download it into `secrets\`, then share your Sheet (Editor) with the `client_email` inside that file.

## 3. How it fits together
Cloud: GitHub Actions runs `main.py` daily (12:00 UTC full run, every 4 hours sync only). Database: your Google Sheet (cloud). Local (this PC): the same scripts through `install\run.cmd`, plus `send_assist.py`, which opens Chrome profiles. There is no web front end.

## 4. Folder map
See `README.md`. Code is in `app\` (own git history). Old zips are in `archive\`.

## 5. First-time install
1. Double-click `install\INSTALL.cmd` (click **Yes** if Windows asks). To look first without changing anything, open PowerShell in `install\` and run:
```
.\install.ps1 -Check
```
You should see OK lines and DRY lines (what it would do).
2. Run the real install. It installs Python 3.12 if missing, creates `app\.venv`, installs packages, asks for each value (typing is hidden; Enter skips), runs an offline health check and puts an "IG Send Assist" shortcut on the Desktop.
3. You should end with a CHECKLIST: OK / SKIP lines; a WARN about the Google key means you still need to put the `.json` key in `secrets\`.

## 6. Secrets
See `secrets\SECRETS-CHECKLIST.md`. Values go in `secrets\.env` (NAME=value lines) and the Google `.json` key file in `secrets\`. For the cloud run, the same values go in GitHub: Settings > Secrets and variables > Actions (secrets: GOOGLE_SERVICE_ACCOUNT_JSON, AI_API_KEYS, IG_ACCESS_TOKEN; variables: SHEET_ID, OFFER and the optional settings).

## 7. Run it / use it
1. Safe test (reads the Sheet, no AI, no messages written):
```
install\run.cmd main.py --sync-only
```
2. Full run (writes DMs into Today Queue; use 3 to 10 leads and one account first):
```
install\run.cmd main.py
```
3. Send: double-click "IG Send Assist" on the Desktop (or `install\run.cmd send_assist.py acc1`). Put `profiles.json` (copy of `app\profiles.example.json`) in `secrets\` first.
4. Each day the cloud job fills Today Queue by itself. Mark `Done? = Yes` after you send, and `Replied? = Yes` on replies.

## 8. How to change common things
| I want to... | Do this |
|---|---|
| Change the offer, daily limit, send window | Edit the value in `secrets\.env` and the GitHub variable of the same name |
| Change message styles | Edit `app\styles.py` |
| Add an AI key | Add it to `AI_API_KEYS`, comma separated |
| Pause an account | Accounts tab in the Sheet: Status = Paused |
| Back up | `powershell -ExecutionPolicy Bypass -File backups\backup.ps1` and download the Sheet (`database\README.md`) |

## 9. Troubleshooting
See `GUIDE\04-TROUBLESHOOTING.md`. Quick ones: "MISSING SETTING" = a value in `secrets\.env` is empty or the `.json` key is not in `secrets\`; "Cannot open sheet" = share the Sheet with the service-account email.

## 10. Move to a new PC
1. Copy the whole `ig-outreach` folder.
2. Put the secrets back in `secrets\` (from your password manager) if they were not copied.
3. Double-click `install\INSTALL.cmd`.
4. Check: open PowerShell in `install\` and run:
```
.\install.ps1 -Check
```
Every line should say OK (DRY lines mean "already fine or would be done").

Not verified: the real Google Sheet, AI keys and Instagram flow (they need your logins). The installer, environment setup and script start-up were tested in a temp copy.

## 11. Deeper chapters (read these when you need detail)
| Question | Chapter |
|---|---|
| Run order, sheet tabs and columns, account ramp, how the AI keys fail over | `GUIDE\02-ARCHITECTURE.md` |
| Exact settings and files for each change (wording, angles, limits, schedule, accounts, keys) | `GUIDE\03-HOW-TO-CHANGE-THINGS.md` |
| Error messages and fixes, how to read the Run Log | `GUIDE\04-TROUBLESHOOTING.md` |
| Order of work and known limits | `GUIDE\01-ROADMAP.md` |

Key facts to remember:
- A human sends every DM. The bot only writes and schedules. Never add auto-login or auto-send.
- Account ramp: no outreach before day 14, max 5 a day until day 28, then your limit; hard cap 20.
- Never delete rows in the Outreach Log; it is the bot memory.
- Test with 3-10 leads and one account first:
```
install\run.cmd main.py
```
