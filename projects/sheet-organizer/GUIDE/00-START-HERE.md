# 00 Start here: set up sheet-organizer on a PC

## A. Install
1. Copy the whole `sheet-organizer` folder (with `secrets\`) to the new PC.
2. Double-click `install\INSTALL.cmd`. Click **Yes** if Windows asks.
3. Expect a CHECKLIST of OK / SKIP / WARN lines. FAIL lines: see `04-TROUBLESHOOTING.md`.

## B. Keys
`05-ACCOUNTS-AND-KEYS.md` and `secrets\SECRETS-CHECKLIST.md` say where each key comes from. Put the Google `.json` key file in `secrets\`.

## C. First test (writes nothing)
1. Open PowerShell in `install\` and run:
```
.\run.cmd organizer.py
```
2. You should see counts of notes found and no error about missing settings.
