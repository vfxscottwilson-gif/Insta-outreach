# Scraper Tools: Setup guide

For a non-expert on Windows 10. Numbered steps. No secret values anywhere (none exist).

## 1. What this app is
A toolbox of four free scrapers that find leads (businesses and YouTube creators) from public pages. They run on your PC from the command line. Their CSV/JSON output feeds the lead bot. They are not a website and have no login.

## 2. Accounts needed
| Service | Why | Free? | Link |
|---|---|---|---|
| None | The tools use public pages only | yes | |
| GitHub (optional) | Only if you later schedule the tools on GitHub Actions | free | https://github.com |

Internet is needed to install and to run them.

## 3. How it fits together
All local: programs in `app\`, Python virtual environments (`.venv`) for scrapetube and crawl4ai, two downloaded programs (`gmaps.exe`, `yt-dlp.exe`). Nothing is cloud-hosted. No database. Output files are CSV/JSON you create.

## 4. Folder map
See `README.md`. Details of each tool: `docs\TOOLS-MANIFEST.md`.

## 5. First-time install
1. Open the `install\` folder and double-click `INSTALL.cmd`. Click Yes if Windows asks.
2. To look first without changing anything:
```
powershell -ExecutionPolicy Bypass -File install\install.ps1 -Check
```
Run it from the `scraper-tools` folder. You should see `[OK]` lines for what is present and `[DRY]` lines for what would be added, then a CHECKLIST ending `Done. No keys needed.` Nothing is changed in this mode.
3. It installs Python 3.12 if missing, downloads `gmaps.exe` and `yt-dlp.exe` if missing (yt-dlp is checked against the official checksum), creates two venvs, and downloads Chromium for crawl4ai (large, can take 10+ minutes).
4. At the end read the CHECKLIST. `FAIL` or `WARN` lines: see `GUIDE\04-TROUBLESHOOTING.md`. Re-running is safe; it only does what is missing.
5. Time: about 5 to 15 minutes, longer on slow internet (the Chromium download is the slow part).

## 6. Secrets
None needed. See `secrets\SECRETS-CHECKLIST.md`.

## 7. Run it / use it
Always test with 1-3 queries first. Open PowerShell in the project folder.
1. YouTube creators (yt-dlp). You should get a CSV and a line "N channels written":
```
powershell -ExecutionPolicy Bypass -File app\yt-dlp\yt_leads.ps1 -Query "personal trainer youtube channel" -Max 30 -MinSubs 5000 -MaxSubs 500000 -Out yt_leads.csv
```
2. YouTube channel search (scrapetube). Prints a count and 3 sample channels:
```
app\scrapetube\.venv\Scripts\python.exe app\scrapetube\test_scrapetube.py
```
3. Website emails and socials (crawl4ai). Prints JSON with emails and socials:
```
app\crawl4ai\.venv\Scripts\python.exe app\crawl4ai\site_leads.py https://example.com
```
4. Google Maps (gosom): create `queries.txt` with one search per line (for example `gym in Austin TX`), then:
```
app\gosom-google-maps-scraper\gmaps.exe -input queries.txt -results out.csv -email -depth 1 -exit-on-inactivity 2m
```
This one has never been run in this setup (not verified); first start downloads Chromium. All commands and CSV columns: `docs\INTEGRATION.md`.

Where results go: into the folder you run from, unless you pass a path. `site_leads.py` and `test_scrapetube.py` always overwrite `sample_site_crawl.json` / `sample_channels.json` there, so rename results you want to keep.

## 8. How to change common things
| I want to... | Do this |
|---|---|
| Update yt-dlp | `app\yt-dlp\yt-dlp.exe -U` |
| Use a newer gosom | Change the version in the URL in `docs\TOOLS-MANIFEST.md` step 1 and in `install\install.ps1` (`$GmapsVer`), delete old `gmaps.exe`, re-run INSTALL |
| Pin a different crawl4ai / scrapetube | Edit `$Crawl4aiVer` / `$ScrapetubeVer` in `install\install.ps1` |
| Rebuild a broken venv | Delete that tool's `.venv` folder, run INSTALL.cmd |
| Redo the Chromium setup for crawl4ai | Delete `app\crawl4ai\.setup-done`, run INSTALL.cmd |
| Back up the folder | `powershell -ExecutionPolicy Bypass -File backups\backup.ps1` (zip in `backups\`, no `.venv`) |
| Change search words, subscriber range, delays, flags | `GUIDE\03-HOW-TO-CHANGE-THINGS.md` |

## 9. Troubleshooting
See `GUIDE\04-TROUBLESHOOTING.md`. It lists every installer message, how to read results (there are no log files; the yt-dlp wrapper hides its errors) and fixes.

Other chapters in `GUIDE\`: 00-START-HERE (install and first run), 01-ROADMAP (done/open/next), 02-ARCHITECTURE (data flow), 03-HOW-TO-CHANGE-THINGS, 05-ACCOUNTS-AND-KEYS (none).

## 10. Move to a new PC
1. Copy the whole `scraper-tools` folder.
2. Double-click `install\INSTALL.cmd` (it restores everything that is missing; nothing else to bring).
3. Check (run from the `scraper-tools` folder):
```
powershell -ExecutionPolicy Bypass -File install\install.ps1 -Check
```
After a successful install every line should say `OK`. On a fresh PC before installing you will see `DRY` lines; that is normal.
4. Not copied by design: the `.venv` folders (about 700 MB, rebuilt by the installer), `gmaps.exe` and `yt-dlp.exe` (re-downloaded). Your own result CSV/JSON files are in the folder you ran from; copy them yourself if you want them.
