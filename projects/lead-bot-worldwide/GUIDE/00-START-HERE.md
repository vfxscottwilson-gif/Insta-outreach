# 00 Start here: set up Lead Bot Worldwide on a PC

## A. Install
1. Copy the whole `lead-bot-worldwide` folder (with `secrets\`) to the new PC, e.g. into `F:\Github Repos\projects\`.
2. Open the `install` folder and double-click `INSTALL.cmd`. Click **Yes** if Windows asks.
3. Expected: green `OK` lines, then "self-test passed" and "Install finished". `MISSING` lines before the install are normal; they are what the installer adds.
4. To only look (change nothing), run this in PowerShell inside `install\`:
```
.\install.ps1 -Check
```
Every line should say `OK` after the install.

## B. Keys
1. Open `secrets\SECRETS-CHECKLIST.md`. Only `GOOGLE_SA` and `SHEET_ID_US` are required.
2. Where each key comes from: `05-ACCOUNTS-AND-KEYS.md` and the checklist.

## C. Try it
1. Double-click the Desktop shortcut **Lead Bot Worldwide (local test)**.
2. Expected: a PowerShell window prints progress lines; CSV files appear in `app\local_sheet\`. Press Ctrl+C to stop (a full run takes long).
3. For the real daily run on GitHub, follow `..\SETUP-GUIDE.md` section 6.
