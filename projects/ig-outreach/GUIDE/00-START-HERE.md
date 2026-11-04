# 00 Start here: set up ig-outreach on a PC

**What it is:** reads leads from your Google Sheet, writes a short personalised Instagram DM for each (under 40 words, 9 rotating angles, free-sample offer), schedules them across your accounts and writes follow-ups. **A human sends every DM**; nothing logs into Instagram for you. The daily run is in the cloud (GitHub Actions); this PC is for testing and for the send helper.

**Reading order:** 00 (this), 01 roadmap, 05 accounts, then 02 / 03 / 04 as needed. Full guide: `SETUP-GUIDE.md`.

## A. Install
1. Copy the whole `ig-outreach` folder (with `secrets\`) to the PC.
2. Optional first look (changes nothing):
```
install\INSTALL.cmd -Check
```
3. Double-click `install\INSTALL.cmd`. Click **Yes** if Windows asks.
4. It installs Python if missing, builds the environment and asks for your keys (hidden typing; Enter skips). Expect a checklist of OK / SKIP / WARN lines. FAIL lines: see `04-TROUBLESHOOTING.md`.

## B. Keys
`05-ACCOUNTS-AND-KEYS.md` and `secrets\SECRETS-CHECKLIST.md` say where each key comes from. Put the Google `.json` key file in `secrets\`. Accounts needed: Google (Sheets + service account), GitHub (daily run), at least one AI provider (two recommended). Meta/Instagram is optional.

## C. First test (safe)
1. Sync only (does not write new messages):
```
install\run.cmd main.py --sync-only
```
2. You should see `Synced: 0` (or a count) and no "MISSING SETTING" line.
3. Full run with a few test leads (needs AI keys and `OFFER`):
```
install\run.cmd main.py
```
4. Open the Sheet: new rows appear in `Outreach Log` and `Today Queue`, and one row in `Run Log`.

## D. Daily use
1. Open `Today Queue`. For each row: open the chat link, follow + like 2 posts (the "Before You Send" column), paste the message, send.
2. Type `Yes` in `Done? (type Yes)`. The sheet stamps the time, and the next sync (every 4 hours) updates `Outreach Log`.
3. When someone replies set `Replied? = Yes` in `Outreach Log` so follow-ups stop.
4. Optional one-click helper on this PC:
```
install\run.cmd send_assist.py
```

## Not verified
A live run against Google Sheets, the AI APIs and Instagram needs your logins; the packager did not run one.
