# 00 Start here: set up sheet-organizer on a PC

**What it is:** a "senior manager" robot. You paste messy notes into the `Inbox` tab of a Google Sheet; once a day it files each note into Tasks, Problems & Solutions, Achievements, Ideas or Resources, flags overdue / blocked / forgotten items, and writes a monthly report. Optionally it also reads FigJam sticky notes. It never edits or deletes your Inbox. The daily run is in the cloud (GitHub Actions); this PC is for testing.

**Reading order:** 00 (this), 01 roadmap, 05 accounts, then 02 / 03 / 04 as needed. Full guide: `SETUP-GUIDE.md`.

## A. Install
1. Copy the whole `sheet-organizer` folder (with `secrets\`) to the PC.
2. Optional first look (changes nothing):
```
install\INSTALL.cmd -Check
```
3. Double-click `install\INSTALL.cmd`. Click **Yes** if Windows asks.
4. Expect a checklist of OK / SKIP / WARN lines. FAIL lines: see `04-TROUBLESHOOTING.md`.

## B. Keys
`05-ACCOUNTS-AND-KEYS.md` and `secrets\SECRETS-CHECKLIST.md` say where each key comes from. Put the Google `.json` key file in `secrets\`. Accounts needed: Google (Sheet + service account, with the Sheets API enabled), GitHub (daily run), at least one AI key (Gemini, Groq or OpenRouter, all free tiers). Figma is optional.

## C. First test (writes nothing)
1. Put 5-10 notes in the `Inbox` tab of the Sheet, one per row.
2. Run:
```
install\run.cmd organizer.py
```
3. You should see lines like `Gemini: 1 key(s), N model(s) found live`, `New notes found: N`, `DRY RUN: nothing is written to the sheet.` and a final `DONE.` line, with no error about missing settings.

## D. First real run
1. In `secrets\.env` set `DRY_RUN=no` and `RUN_LIMIT=10`, run the same command again.
2. Open the Sheet: new tabs appear (Tasks & Progress, Problems & Solutions, Achievements, Ideas & Notes, Resources & Links, Attention Needed, Monthly Summary, Review Needed, `_Ledger`, `_Log`) and your notes are filed.

## E. Daily use
Paste notes in `Inbox`. At 02:00 UTC (07:00 Pakistan) the cloud run files them. Read `Attention Needed` each morning and `Monthly Summary` at month end.

## Not verified
A live run against Google Sheets, the AI APIs and Figma needs your logins; the packager did not run one.
