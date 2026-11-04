# YT Creator Finder: Setup guide

For a non-expert on Windows 10. Numbered steps. No secret values (names only). The bot's own very detailed guide is `app\SETUP_GUIDE.md` (Google Cloud and Upwork click-by-click).

## 1. What this app is
A lead bot that finds YouTube channel owners who are hiring video editors or thumbnail designers. Each lead is scored (PRIME / GROWING / REVIEW), gets an AI-written pitch angle, and is added to a Google Sheet without duplicates. It runs by itself on GitHub Actions at 06:17, 09:17, 12:17, 15:17, 18:17 and 21:17 Pakistan time. Upwork and Freelancer leads are pitched on those platforms only (their rules).

## 2. Accounts needed
| Service | Why | Free? | Link |
|---|---|---|---|
| Google (Cloud + Sheets) | YouTube Data API key, service account, the Sheet | free | https://console.cloud.google.com |
| GitHub | Runs the bot on a schedule and stores the secrets | free | https://github.com |
| Google AI Studio (Gemini) | AI pitch (optional) | free | https://aistudio.google.com |
| Groq | AI fallback (optional) | free | https://console.groq.com |
| Jina | Faster reading of YTJobs (optional) | free | https://jina.ai |
| Upwork developer | Upwork jobs (optional, needs approval) | free | https://www.upwork.com/developer/keys/apply |
Freelancer.com, LinkedIn Jobs, Remotive and YTJobs need no account.

## 3. How it fits together
Cloud: GitHub Actions runs `python -m src.leadbot` (Python 3.12, workflow `app\.github\workflows\run-lead-bot.yml`), reads job sources, calls YouTube/Gemini/Groq APIs, writes to your Google Sheet. Local (this folder): a test copy for dry runs. No database other than the Sheet.

## 4. Folder map
See `README.md`. Detailed chapters:
| Chapter | Read it for |
|---|---|
| `GUIDE\00-START-HERE.md` | Install, first dry run, what you should see |
| `GUIDE\01-ROADMAP.md` | Done / open / next, known limits |
| `GUIDE\02-ARCHITECTURE.md` | How a run works, files, storage, APIs, schedule |
| `GUIDE\03-HOW-TO-CHANGE-THINGS.md` | Recipes with exact files and settings |
| `GUIDE\04-TROUBLESHOOTING.md` | Real error messages, exit codes, how to read logs |
| `GUIDE\05-ACCOUNTS-AND-KEYS.md` | Every secret NAME, where to get it |

## 5. First-time install (local test copy)
1. Open `install\` and double-click `INSTALL.cmd`. To look first without changing anything:
```
INSTALL.cmd -Check
```
You should see `[OK]`, `[SKIP]` and `[DRY]` lines.
2. The installer installs Python 3.12 if missing, creates `app\.venv`, installs packages, creates `secrets\.env`, then asks for each key with hidden typing. Press Enter to skip any key. For GOOGLE_SA type the path of the service-account JSON file.
3. It runs the offline tests and makes a Desktop shortcut "YT Creator Finder (dry run)".
4. To get the keys, follow `GUIDE\05-ACCOUNTS-AND-KEYS.md` (summary) or `app\SETUP_GUIDE.md` (full).

## 6. Secrets
Names and where to get each: `secrets\SECRETS-CHECKLIST.md`. Required: GOOGLE_SA, SHEET_ID, YOUTUBE_API_KEYS. Optional: GEMINI_API_KEYS, GROQ_API_KEYS, JINA_API_KEY, UPWORK_CLIENT_ID, UPWORK_CLIENT_SECRET, UPWORK_REFRESH_TOKEN.

## 7. Run it / use it
**Go live on GitHub (cloud schedule)**
1. On github.com create a new PRIVATE repository (no files).
2. Push the contents of `app\` to it (the folder already has git history; this step sends your code to GitHub, so do it only when you are ready):
```
cd app
```
```
git remote add origin https://github.com/YOUR-NAME/YOUR-REPO.git
```
```
git push -u origin main
```
(The branch in `app` is called `main`.)
3. On the repo page: Settings > Secrets and variables > Actions > New repository secret. Add every secret NAME from section 6 (at least the three required ones), value pasted from your own notes.
4. Optional tuning: same page, Variables tab: DAILY_LEAD_TARGET, MIN_SUBS, MAX_DAYS_SINCE_UPLOAD, YT_SEARCH_BUDGET.
5. Actions tab > "YT creator lead bot" > Run workflow with `dry_run` ticked and `max_leads` 10. Open the run log: you should see leads printed and nothing written.
6. Run again with `dry_run` unticked and `max_leads` 10 (pilot). Check the Sheet. Then leave the schedule on.
7. What you should see in the Sheet after the pilot: tabs `Master Dashboard`, `YouTube_Video_Editing_Leads`, `YouTube_Thumbnail_Design_Leads`, `Blacklist`, `Run Log` (the bot creates them; `_State` is hidden), and at most 10 new lead rows. In the run log, the last line `SUMMARY written N` tells you how many rows were added. A green run with `written 0` is possible: see `GUIDE\04-TROUBLESHOOTING.md`.
8. Before step 3 you also need an empty Google Sheet shared with the service account `client_email` as Editor; its id is `SHEET_ID` (`app\SETUP_GUIDE.md` Part 3).

**Local dry run (no Sheet writes)**: double-click the Desktop shortcut "YT Creator Finder (dry run)". It saves `proof\dryrun-leads.csv`. Or:
```
app\.venv\Scripts\python.exe -m src.leadbot --dry-run --max-leads 10
```
Upwork: after Upwork approves your key, run once on your PC to get the refresh token, then add the three UPWORK_* secrets:
```
app\.venv\Scripts\python.exe app\tools\upwork_auth.py
```

## 8. How to change common things
| I want to... | Do this |
|---|---|
| Change filters (subscribers, days since upload, niches, scoring) | Edit `app\config.yaml`, or set the GitHub Variables of section 7 step 4 |
| Change run times | Edit the `cron` line in `app\.github\workflows\run-lead-bot.yml` (UTC; PKT = UTC+5) and push |
| Add or rotate a key | Update `secrets\.env` and the GitHub secret with the same NAME |
| Pause the bot | GitHub > Actions > the workflow > ... > Disable workflow |

## 9. Troubleshooting
See `GUIDE\04-TROUBLESHOOTING.md`.

## 10. Move to a new PC
1. Copy the whole `yt-creator-finder` folder (with `secrets\`).
2. Double-click `install\INSTALL.cmd`. The cloud part (GitHub repo, secrets, Sheet) does not move, it keeps running.
3. Check:
```
INSTALL.cmd -Check
```
Every line should say OK or SKIP (on a PC where it was already installed).
4. Back up first if you wish: `backups\backup.ps1` makes a zip of the folder (it contains `secrets\`, keep it private). The Sheet is backed up from Google (`database\README.md`).

## Not verified
The bot has not been run against a real Sheet, and the Upwork path has not been tested live (needs an approved key). Offline tests passed earlier (22).
