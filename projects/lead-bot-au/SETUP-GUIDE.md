# Lead Bot AU: Setup guide
Written for a non-expert on Windows 10. Never type secret values into chat or documents.

## 1. What this app is
The Australia-only twin of the worldwide bot: finds AU businesses that can pay $500-1,000+ per month (AUD) and AU YouTube creators, with 8 extra AU columns (ABN, entity, GST ...). One Google Sheet. It never writes emails.
It runs by itself twice a day on GitHub (19:00 and 07:00 UTC (`0 19 * * *`, `0 7 * * *`, about 6am/6pm Sydney)) and can be tried on your PC.

## 2. Accounts needed
| Service | Why | Free? | Sign-up link |
|---|---|---|---|
| Google (Gmail account) | Sheets (the lead lists) and the Google Cloud "robot" | Yes | accounts.google.com |
| Google Cloud Console | create the robot key (service account) | Yes | console.cloud.google.com |
| GitHub | runs the daily automation | Yes (public repo = free minutes) | github.com |
| AI / data APIs (optional) | nicer insights, more leads | free tiers | see `secrets\SECRETS-CHECKLIST.md` |

## 3. How it fits together (cloud vs local)
- **Cloud:** GitHub Actions runs the code on a schedule; Google Sheets stores the leads.
- **Local (this PC):** for installing, testing and editing; writes CSV files to `app\local_sheet\`.
- No separate frontend, backend server or database. Details: `GUIDE\02-ARCHITECTURE.md`.

## 4. Folder map
See the table in `README.md`. The code is in `app\` (own git), your keys in `secrets\`.

## 5. First-time install (this PC)
1. Open the `install` folder and double-click `INSTALL.cmd`. Click **Yes** if asked.
2. When it asks "Paste SHEET_ID_AU_ONLY" or "Paste GEMINI_API_KEY_1", paste the value (nothing shows while you type) and press Enter, or just press Enter to skip.
3. Check that nothing is missing:
```
INSTALL.cmd -Check
```
You should see only `OK` lines.
4. To see what the installer would do without changing anything:
```
INSTALL.cmd -DryRun
```

## 6. Secrets and accounts: connect GitHub and Google (needed for the daily run)
1. Create the Google robot key: follow `app\00_START_HERE_SETUP_GUIDE.md` Step 1 (Google Cloud > new project > enable **Google Sheets API** and **Google Drive API** > Service Accounts > Create > Keys > Add key > JSON). A key file may already be in `secrets\` (see `secrets\SECRETS-CHECKLIST.md` section D).
2. Create the sheet(s): SHEET_ID_AU_ONLY. Help: `app\00_START_HERE_SETUP_GUIDE.md` and `app\AU_EDITION.md`. For each sheet: create a blank Google Sheet, click **Share**, paste the robot's email (the `client_email` inside the .json; it ends in `.iam.gserviceaccount.com`), choose **Editor**, and copy the sheet id from the URL (the long text between `/d/` and `/edit`).
3. Create a GitHub repository for `app\` (its own repo, not shared with the worldwide bot) and push the code. Run in PowerShell, replacing the two names:
```
cd "F:\Github Repos\projects\lead-bot-au\app"
```
```
git remote add origin https://github.com/YOUR-GITHUB-USER/YOUR-REPO-NAME.git
```
```
git push -u origin master
```
Use `main` instead of `master` if `git branch` shows `main`. This publishes the code only; `.gitignore` blocks keys and key files.
4. In the GitHub repo: **Settings > Secrets and variables > Actions > New repository secret**. Add `GOOGLE_SA` (paste the whole text of the .json file) and the sheet ids: SHEET_ID_AU_ONLY (old name SHEET_ID still works). Add optional keys from `secrets\SECRETS-CHECKLIST.md`.
5. GitHub repo > **Actions** > "Run AU Lead Bot" > **Run workflow**. Expect green ticks and new rows in the sheet. A job that says `SKIP ... no SHEET_ID` just has no sheet secret set.

## 7. Run it / use it
- Local test: double-click the Desktop shortcut **Lead Bot AU (local test)**; CSVs appear in `app\local_sheet\`; Ctrl+C stops it.
- Daily: nothing to do. Open the Google Sheet(s) and work the leads. Never sort or delete rows.
- The outreach bot reads the sheet(s) following `docs\CONTRACT.md`.

## 8. How to change common things
See `GUIDE\03-HOW-TO-CHANGE-THINGS.md`.

## 9. Troubleshooting
See `GUIDE\04-TROUBLESHOOTING.md`.

## 10. Move to a new PC
1. Copy the whole `lead-bot-au` folder (including `secrets\`) to the new PC.
2. Double-click `install\INSTALL.cmd`.
3. Check: open PowerShell in `install\` and run:
```
.\install.ps1 -Check
```
Every line should say OK. GitHub and the Google Sheets live in the cloud and need nothing moved.

Not verified by the packager: the GitHub run and the live Google Sheets (they need your logins).
