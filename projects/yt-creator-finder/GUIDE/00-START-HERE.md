# 00 Start here: set up YT Creator Finder on a PC

What this is: a bot that looks for people who are hiring a YouTube video editor or thumbnail designer, scores them, writes a short AI pitch idea, and adds each one as a row in your Google Sheet. The real, automatic version runs for free on GitHub (6 times a day). The copy on your PC is only for test runs that write nothing to the Sheet.

You do NOT need to know Python. Every command below goes in its own box: copy it, paste it, press Enter.

## A. Before you start (5 minutes)
You need:
- Windows 10 and an internet connection.
- The whole `yt-creator-finder` folder on your PC (keep `secrets\` inside it).
- At least ONE key to test locally: `YOUTUBE_API_KEYS` (a YouTube Data API v3 key). Without it the bot stops at once with `[FATAL] Missing required env var(s): YOUTUBE_API_KEYS`, even for a dry run (checked in `app\src\config.py`, function `require`). How to get it: `05-ACCOUNTS-AND-KEYS.md`.
- For the live (cloud) version you also need `GOOGLE_SA` and `SHEET_ID`.

## B. Install
1. Look first, change nothing. Open PowerShell in the `yt-creator-finder` folder and run:
```
powershell -ExecutionPolicy Bypass -File install\install.ps1 -Check
```
2. You should see lines starting `[OK]`, `[SKIP]`, `[DRY]`, `[WARN]`, then a `===== CHECKLIST =====`. `[DRY]` means "would do this". `[WARN] Keys no secrets\.env yet` is normal on a first look.
3. Real install: double-click `install\INSTALL.cmd`. Click Yes if Windows asks.
4. The installer does these things, in this order (read from `install\install.ps1`):
   - checks that `app\src\leadbot.py` exists (else `[FAIL] Folder layout`: you copied only part of the folder);
   - checks Python; if missing it installs Python 3.12 with winget;
   - creates `app\.venv` and installs the packages from `app\requirements.txt`;
   - creates `secrets\.env` from `app\.env.example` and asks for each key with hidden typing (nothing shows while you type). Press Enter to skip a key. For `GOOGLE_SA` you can type the path of the downloaded `.json` key file;
   - copies `secrets\.env` to `app\.env` (the bot reads that copy);
   - runs the offline tests (no internet, no keys needed);
   - makes a Desktop shortcut "YT Creator Finder (dry run)".
5. At the end you see a CHECKLIST. A `FAIL` line: see `04-TROUBLESHOOTING.md`. A `WARN` on tests is not fatal.
6. If it says Python was installed but is not on PATH yet: close the window and double-click `INSTALL.cmd` again.

## C. First run (dry run, safe)
1. Double-click the Desktop shortcut "YT Creator Finder (dry run)". A black window stays open.
2. What you should see: lines like `[INFO] linkedin: ... jobs`, then a table with the columns SEG, SC, PLATFORM, TYPE, SUBS, CTRY, EMAIL, WHO / LINK, then a `[INFO] leadbot: SUMMARY` line, and `Saved N leads to ...proof\dryrun-leads.csv`.
3. Open `proof\dryrun-leads.csv` in Excel. Nothing was written to Google Sheets.
4. Same thing from a command line (10 leads at most). Run it from inside the `app` folder:
```
cd app
```
```
.venv\Scripts\python.exe -m src.leadbot --dry-run --max-leads 10
```
5. "(no leads qualified in this dry run)" is not an error: the filters were strict or the sources returned nothing. See `04-TROUBLESHOOTING.md`.
6. A dry run also creates `app\.state_local.json` (counters such as YouTube units used today). It is gitignored and safe to delete.

## D. Go live (cloud, automatic)
Follow `SETUP-GUIDE.md` section 7: private GitHub repo, push `app\`, add secrets, run once with `dry_run` ticked, then a 10-lead pilot, then leave the schedule on. Pushing sends your code outside this PC: do it only when you are ready.

## E. Daily use
Open the Google Sheet. Sort the tab `YouTube_Video_Editing_Leads` by `Quality_Segment` (PRIME first). Read the `Signal_URL` before you write to anyone. Column guide: `app\SETUP_GUIDE.md` Part 8.

## F. Not verified
- I ran the installer in check mode only. I did not run the full install or the dry run on this PC, and the bot has never written to a real Sheet (`CLAUDE.md` status).
- `01-ROADMAP.md` records a keyless dry run on 2026-11-01. The current code requires a YouTube key even for a dry run, so that earlier run used older behaviour or a placeholder key (not verified which).
