# 00 Start here: set up ig-outreach on a PC

## A. Install
1. Copy the whole `ig-outreach` folder (with `secrets\`) to the new PC.
2. Double-click `install\INSTALL.cmd`. Click **Yes** if Windows asks.
3. It installs Python if missing, builds the environment and asks for your keys (hidden typing; Enter skips). Expect a CHECKLIST of OK / SKIP / WARN lines. FAIL lines: see `04-TROUBLESHOOTING.md`.

## B. Keys
`05-ACCOUNTS-AND-KEYS.md` and `secrets\SECRETS-CHECKLIST.md` say where each key comes from. Put the Google `.json` key file in `secrets\`.

## C. First test (safe)
1. Open PowerShell in `install\` and run:
```
.\run.cmd main.py --sync-only
```
2. You should see a short run summary and no "MISSING SETTING" line.
