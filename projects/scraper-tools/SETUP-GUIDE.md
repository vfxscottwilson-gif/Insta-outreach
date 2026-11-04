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
INSTALL.cmd -Check
```
You should see `[OK]` lines for what is present and `[DRY]` lines for what would be added.
3. It installs Python 3.12 if missing, downloads `gmaps.exe` and `yt-dlp.exe` if missing (yt-dlp is checked against the official checksum), creates two venvs, and downloads Chromium for crawl4ai (large, can take 10+ minutes).
4. At the end read the CHECKLIST. `FAIL` lines: see `GUIDE\04-TROUBLESHOOTING.md`.

## 6. Secrets
None needed. See `secrets\SECRETS-CHECKLIST.md`.

## 7. Run it / use it
Always test with 1-3 queries first. Open PowerShell in the project folder.
1. YouTube creators (yt-dlp). You should get a CSV and a line "N channels written":
```
powershell -File app\yt-dlp\yt_leads.ps1 -Query "personal trainer youtube channel" -Max 30 -MinSubs 5000 -MaxSubs 500000 -Out yt_leads.csv
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
This one has never been run in this setup; first start downloads Chromium. All commands and CSV columns: `docs\INTEGRATION.md`.

## 8. How to change common things
| I want to... | Do this |
|---|---|
| Update yt-dlp | `app\yt-dlp\yt-dlp.exe -U` |
| Use a newer gosom | Change the version in the URL in `docs\TOOLS-MANIFEST.md` step 1 and in `install\install.ps1` (`$GmapsVer`), delete old `gmaps.exe`, re-run INSTALL |
| Pin a different crawl4ai / scrapetube | Edit `$Crawl4aiVer` / `$ScrapetubeVer` in `install\install.ps1` |
| Rebuild a broken venv | Delete that tool's `.venv` folder, run INSTALL.cmd |

## 9. Troubleshooting
See `GUIDE\04-TROUBLESHOOTING.md`.

## 10. Move to a new PC
1. Copy the whole `scraper-tools` folder.
2. Double-click `install\INSTALL.cmd` (it restores everything that is missing; nothing else to bring).
3. Check:
```
INSTALL.cmd -Check
```
Every line should say OK.
