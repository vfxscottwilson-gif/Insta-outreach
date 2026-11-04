# 00 Start here: set up outreach-bot on a PC

## A. Install
1. Copy the whole folder (with `secrets\`) to the PC.
2. Double-click `install\INSTALL.cmd`. Click **Yes** if Windows asks.
3. Expected: lines marked OK / SKIP, ending with `[OK] Self-test passed`. FAIL lines point to `04-TROUBLESHOOTING.md`.

## B. Keys
1. Names and where each comes from: `05-ACCOUNTS-AND-KEYS.md` and `secrets\SECRETS-CHECKLIST.md`.
2. Put values in `secrets\.env`; save the Google service-account JSON as `secrets\google-sa.json`.

## C. Run it
1. Safe test (writes nothing):
```
powershell -ExecutionPolicy Bypass -File install\run-bot.ps1
```
2. You should see the "AI KEY REGISTRATION" report and a "DRY RUN" line.
