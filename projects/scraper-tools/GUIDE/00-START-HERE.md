# 00 Start here: set up and first run of Scraper Tools

For a non-expert on Windows 10. Every command is in its own box. Nothing here needs a password, key or account.

## What this is
Four free programs that find sales leads from public web pages and save them as CSV/JSON files:

| Tool | Finds | Your input | Your output |
|---|---|---|---|
| gosom `gmaps.exe` | Local businesses on Google Maps (website, phone, emails) | `queries.txt` | CSV (36 columns) |
| yt-dlp + `yt_leads.ps1` | YouTube channels in a subscriber range, with emails from the About text | a search phrase | CSV (8 columns) |
| scrapetube | YouTube channels (about 20 per call) with subscriber text | one line edited in a script | `sample_channels.json` |
| crawl4ai + `site_leads.py` | Emails and social links on one website | a website address | JSON on screen + `sample_site_crawl.json` |

They run on your PC, one at a time, from PowerShell. There is no website, no login, no database. The lead bot (a different project) reads the CSV files.

## A. Install (5 to 15 minutes; up to 30 on slow internet)
1. Copy the whole `scraper-tools` folder to the PC.
2. Open PowerShell and go to the folder:
```
cd "F:\Github Repos\projects\scraper-tools"
```
3. Look first without changing anything:
```
powershell -ExecutionPolicy Bypass -File install\install.ps1 -Check
```
4. Expected: lines starting `[OK]` (already there) or `[DRY]` (would be added), then `===== CHECKLIST =====` and the last line `Done. No keys needed. Usage examples: docs\INTEGRATION.md`. Nothing is changed in this mode.
5. Install for real: double-click `install\INSTALL.cmd`. Click Yes if Windows asks. A black window shows progress and waits at the end ("Press any key").
6. What it does, in order: checks Python (installs Python 3.12 with winget if missing), downloads `gmaps.exe` (58 MB) and `yt-dlp.exe` (checked against the official checksum), builds two Python environments (`.venv`) for scrapetube and crawl4ai, then runs `crawl4ai-setup`, which downloads a browser (Chromium). The Chromium step is the slow one.
7. Expected at the end: every CHECKLIST line says `OK` or `SKIP`. For any `FAIL` or `WARN` line, open `04-TROUBLESHOOTING.md` and search for the words in that line.
8. If it says Python is "not on PATH yet": close the window and run `INSTALL.cmd` again. Re-running is safe; it only does what is missing.

## B. Keys
None. See `05-ACCOUNTS-AND-KEYS.md`.

## C. First run (1 to 3 queries only, never the full batch)
Run these from the `scraper-tools` folder in PowerShell.

1. Quickest proof it works: read emails from one website.
```
app\crawl4ai\.venv\Scripts\python.exe app\crawl4ai\site_leads.py https://example.com
```
You should see a small JSON with `"url"`, `"emails"` and `"socials"`. For example.com both lists are empty; that is correct (the installer test saw the same).

2. YouTube creators, small test (a few minutes: it waits 2 seconds per channel):
```
powershell -ExecutionPolicy Bypass -File app\yt-dlp\yt_leads.ps1 -Query "personal trainer youtube channel" -Max 10 -MinSubs 5000 -MaxSubs 500000 -Out yt_leads.csv
```
You should see `N channels written to yt_leads.csv`. N can be 0 or 1 with `-Max 10`: most channels fall outside the subscriber range (a 12-result test gave 1). Open the CSV in Excel.

3. YouTube channel search (scrapetube). Prints a count and 3 samples, saves `sample_channels.json`:
```
app\scrapetube\.venv\Scripts\python.exe app\scrapetube\test_scrapetube.py
```

4. Google Maps. Create a file `queries.txt` in the `scraper-tools` folder with one line, `gym in Austin TX`, then:
```
app\gosom-google-maps-scraper\gmaps.exe -input queries.txt -results out.csv -email -depth 1 -exit-on-inactivity 2m
```
The first start downloads its own Chromium, so expect a wait. Afterwards `out.csv` should hold businesses. **Not verified:** this program was never executed in this setup (an earlier safety check blocked it); the flags come from the upstream README.

## D. Where files land
Output goes into the folder you ran the command from, unless you pass a path (`-Out`, `-results`). `site_leads.py` and `test_scrapetube.py` always write `sample_site_crawl.json` / `sample_channels.json` into that folder and overwrite the old one. Rename results you want to keep.

## E. Next
How it works: `02-ARCHITECTURE.md`. Changing settings: `03-HOW-TO-CHANGE-THINGS.md`. Status: `01-ROADMAP.md`. Commands and CSV columns in full: `docs\INTEGRATION.md`.
