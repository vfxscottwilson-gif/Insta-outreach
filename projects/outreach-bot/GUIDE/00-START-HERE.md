# 00 Start here: set up outreach-bot on a PC

**What it is:** a daily robot that reads your lead sheets and writes one personalised cold-email DRAFT per lead into one Outreach Google Sheet. It never sends anything; you copy and send. The daily run happens in the cloud (GitHub Actions); this PC is for tests and fixes.

**Reading order:** 00 (this), 01 roadmap, 05 keys, then 02 / 03 / 04 as needed. Full guide: `SETUP-GUIDE.md`.

## A. Install
1. Copy the whole folder (with `secrets\`) to the PC.
2. Optional first look (changes nothing):
```
install\INSTALL.cmd -Check
```
3. Double-click `install\INSTALL.cmd`. Click **Yes** if Windows asks. It installs Python 3.12 if missing, makes `app\.venv`, creates `secrets\.env` and asks for each secret with hidden typing (Enter skips one).
4. Expected: lines marked OK / SKIP, ending with `[OK] Self-test passed`. FAIL lines: see `04-TROUBLESHOOTING.md`.

## B. Accounts you need (all free)
Google (Cloud service account + Sheets), GitHub (daily run + cloud secrets), and at least one AI key: Google AI Studio (Gemini), Groq, Mistral or OpenRouter. Names and sources: `05-ACCOUNTS-AND-KEYS.md`.

## C. Keys
1. Put values in `secrets\.env`; save the Google service-account JSON as `secrets\google-sa.json`.
2. For the daily cloud run, the same names must also be GitHub secrets (GitHub > repo > Settings > Secrets and variables > Actions).

## D. Run it
1. Safe test (writes nothing, 10 leads):
```
powershell -ExecutionPolicy Bypass -File install\run-bot.ps1
```
2. You should see the "AI KEY REGISTRATION" report, a "DRY RUN" line, and a final `DONE.` line.
3. Write 10 real drafts:
```
powershell -ExecutionPolicy Bypass -File install\run-bot.ps1 -Live -Limit 10
```
4. Open the Outreach sheet, tab `Emails`: your drafts are there.

## E. Daily use
GitHub > Actions > `generate-emails` runs by itself every day at 10:00 UTC. Check the `Emails` tab, copy drafts into your mail app, send by hand. Tune wording in the `Email Rules` tab.

## Not verified
A live run against Google Sheets and the AI APIs needs your logins; only the offline self-test was run by the packager.
