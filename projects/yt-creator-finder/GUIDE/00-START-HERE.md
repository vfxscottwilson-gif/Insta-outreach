# 00 Start here: set up YT Creator Finder on a PC

## A. Install (local test copy)
1. Copy the whole `yt-creator-finder` folder (with `secrets\`) to the PC.
2. Double-click `install\INSTALL.cmd`. Click Yes if Windows asks.
3. Expected: a CHECKLIST of OK / SKIP lines; FAIL lines point to `04-TROUBLESHOOTING.md`.

## B. Keys
1. Where each key comes from: `05-ACCOUNTS-AND-KEYS.md`. Type them when INSTALL.cmd asks (hidden), or fill `secrets\.env` later and re-run INSTALL.cmd.

## C. Use it
1. Test: double-click the Desktop shortcut "YT Creator Finder (dry run)". You should see leads printed and `proof\dryrun-leads.csv` created. Nothing is written to the Sheet.
2. Live: put the code and secrets on GitHub (`SETUP-GUIDE.md` section 7). Results appear in your Google Sheet.
