# 00 Start here: Lead Bot Worldwide

## What it is
A robot that, twice a day, searches for local businesses (and YouTube creators) that could pay a video/social-media agency $500-1,000+ a month. It reads their websites, scores them out of 10, and adds only the good ones (7/10 or more) as new rows in Google Sheets. It never writes emails; a separate outreach bot does that.

Countries: US, Canada, UK, Australia, New Zealand, Ireland (optional UAE, Saudi Arabia, Qatar) plus a worldwide YouTube sheet. One Google Sheet per country.

## Where everything is

| Thing | Where |
|---|---|
| This folder | `F:\Github Repos\projects\lead-bot-worldwide\` (copy the whole folder to move it) |
| The code | `app\` (its own git repo, not pushed anywhere yet: no remote is set) |
| The daily schedule | GitHub Actions, file `app\.github\workflows\run-lead-bot.yml` |
| The leads | Google Sheets (one per country) |
| Your keys | `secrets\` (never share, never commit) |
| Installer | `install\INSTALL.cmd` |
| Chapters | `GUIDE\00` to `05`; the step-by-step is `SETUP-GUIDE.md` |

Cloud or local: the daily run and the leads live in the cloud (GitHub + Google). This PC is only for installing, testing and editing.

## Your first 5 minutes

1. Check the PC is ready. Open PowerShell and run:

```
powershell -ExecutionPolicy Bypass -File "F:\Github Repos\projects\lead-bot-worldwide\install\install.ps1" -Check
```

   Expected before the first install: `OK` for Python, git, `app\src\leadbot.py`, the secrets checklist, and `MISSING` for `app\.venv` and `secrets\.env`. Those two are what the installer creates.

2. Double-click `install\INSTALL.cmd`, click **Yes** if Windows asks. It installs Python packages, makes `secrets\.env`, adds a Desktop shortcut and runs the bot's self-test. It asks for each key with hidden typing; press Enter to skip any.

3. Run the same check again. Every line should say `OK`.

4. Try the bot without Google: double-click the Desktop shortcut **Lead Bot Worldwide (local test)**. Lines of progress appear; CSV files appear in `app\local_sheet\`. Press Ctrl+C to stop; a full run takes a long time.

5. Open `secrets\SECRETS-CHECKLIST.md`. Only two things are required for the daily run: `GOOGLE_SA` (robot key) and `SHEET_ID_US` (the US sheet id). Then follow `GUIDE\01-ROADMAP.md`.

## Rules to remember

- Never sort or delete rows in a lead tab; the bot only appends.
- Never paste key values into chat, documents or commits.
- Test changes with `--local` before touching GitHub.
- Anything marked "not verified" in these chapters needs your accounts to confirm (GitHub run, live Sheets).

## Next

| If you want to | Read |
|---|---|
| go from zero to the daily run | `01-ROADMAP.md` |
| understand how it works | `02-ARCHITECTURE.md` |
| change cities, niches, score, schedule | `03-HOW-TO-CHANGE-THINGS.md` |
| fix an error | `04-TROUBLESHOOTING.md` |
| see which keys exist | `05-ACCOUNTS-AND-KEYS.md` |
