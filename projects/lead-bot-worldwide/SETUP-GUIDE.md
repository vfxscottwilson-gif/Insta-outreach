# Lead Bot Worldwide: Setup guide
Written for a non-expert on Windows 10. Never type secret values into chat or documents.

## 1. What this app is
Finds local businesses in the US, Canada, UK, Australia, New Zealand and Ireland (optional UAE, Saudi Arabia, Qatar) that can pay $500-1,000+ per month, plus YouTube creators. It writes facts-only contact data, a Segment, an ICP score and a short Lead Insight into one Google Sheet per country. It never writes emails (the outreach bot does).
It runs by itself twice a day on GitHub (20:00 and 08:00 UTC (`0 20 * * *`, `0 8 * * *`)) and can be tried on your PC.

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
2. When it asks "Paste SHEET_ID_US" or "Paste GEMINI_API_KEY_1", paste the value (nothing shows while you type) and press Enter, or just press Enter to skip.
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
2. Create the sheet(s): SHEET_ID_US; SHEET_ID_CA; SHEET_ID_GB; SHEET_ID_AU; SHEET_ID_NZ; SHEET_ID_IE; SHEET_ID_AE; SHEET_ID_SA; SHEET_ID_QA; SHEET_ID_YOUTUBE. Help: `app\SHEETS_SETUP.md`. For each sheet: create a blank Google Sheet, click **Share**, paste the robot's email (the `client_email` inside the .json; it ends in `.iam.gserviceaccount.com`), choose **Editor**, and copy the sheet id from the URL (the long text between `/d/` and `/edit`).
3. Create a GitHub repository for `app\` (one repo for this worldwide bot) and push the code. Run in PowerShell, replacing the two names:
```
cd "F:\Github Repos\projects\lead-bot-worldwide\app"
```
```
git remote add origin https://github.com/YOUR-GITHUB-USER/YOUR-REPO-NAME.git
```
```
git push -u origin master
```
Use `main` instead of `master` if `git branch` shows `main`. This publishes the code only; `.gitignore` blocks keys and key files.
4. In the GitHub repo: **Settings > Secrets and variables > Actions > New repository secret**. Add `GOOGLE_SA` (paste the whole text of the .json file) and the sheet ids: SHEET_ID_US (required, holds the Master Dashboard), SHEET_ID_CA, SHEET_ID_GB, SHEET_ID_AU, SHEET_ID_NZ, SHEET_ID_IE, SHEET_ID_AE, SHEET_ID_SA, SHEET_ID_QA, SHEET_ID_YOUTUBE. Add optional keys from `secrets\SECRETS-CHECKLIST.md`.
5. GitHub repo > **Actions** > "Run Lead Bot" > **Run workflow**. Expect green ticks and new rows in the sheet. A job that says `SKIP ... no SHEET_ID` just has no sheet secret set.

## 7. Run it / use it
- Local test: double-click the Desktop shortcut **Lead Bot Worldwide (local test)**; CSVs appear in `app\local_sheet\`; Ctrl+C stops it.
- Daily: nothing to do. Open the Google Sheet(s) and work the leads. Never sort or delete rows.
- The outreach bot reads the sheet(s) following `docs\CONTRACT.md`.

### What a good first run looks like
- On GitHub: `setup` green, then `collect (us)` etc. green, then `finish` green. Jobs for countries with no sheet secret print `SKIP ...` and are green too.
- In the log of "Run the bot (us)": first the key report (`registered: ...` / `ignored: ...`), last a line starting `Done:`.
- In the Google Sheet: tab 1 is `Stats` (the US sheet has `Master Dashboard` and `US Stats`), new tabs per niche with rows, a new row in `Run Log`.
- A first run can find few leads (the bot keeps only ICP 7/10 or higher). Judge after 2-3 days.

### Costs and limits (from the workflow file and the code)
- Everything works at $0: free OpenStreetMap, free website reading, free Google Sheets. Optional keys add AI text and more data.
- Two daily runs of ten jobs need about 900 runner-minutes a day (workflow comment), so use a PUBLIC repo. A private repo has 2,000 free minutes a month (workflow comment; GitHub's current number is not verified): set variable `LEAD_MATRIX` to `{"include":[{"name":"us","country":"US"}]}` and delete the second `cron` line.
- Google Sheets: 60 reads per minute per robot account, shared by all jobs; the bot slows down and retries by itself.
- The public repo holds only code. Keys stay in GitHub secrets and in `secrets\`.

## 8. How to change common things
See `GUIDE\03-HOW-TO-CHANGE-THINGS.md`.

## 9. Troubleshooting
See `GUIDE\04-TROUBLESHOOTING.md`.

## 10. Move to a new PC
1. Copy the whole `lead-bot-worldwide` folder (including `secrets\`) to the new PC.
2. Double-click `install\INSTALL.cmd`.
3. Check: open PowerShell in `install\` and run:
```
.\install.ps1 -Check
```
Every line should say OK. GitHub and the Google Sheets live in the cloud and need nothing moved.

Not verified by the packager: the GitHub run and the live Google Sheets (they need your logins).
