# 02 Architecture: how Scraper Tools works

Four independent command-line tools. All run locally; they share no state and no database. Nothing runs on a schedule by itself.

## Data flow (text diagram)
```
queries.txt ---------------------> gmaps.exe (Chromium) -----------> out.csv (36 columns)
search phrase -------------------> yt_leads.ps1 + yt-dlp.exe -------> yt_leads.csv (8 columns)
(phrase edited in script) -------> test_scrapetube.py (scrapetube) -> sample_channels.json
website URL ---------------------> site_leads.py (crawl4ai+Chromium)-> sample_site_crawl.json + screen
                                                                          |
                          CSV/JSON files --> lead bot importer (separate project, reads them)
```
Suggested chain (from `docs\INTEGRATION.md`, not automated): scrapetube or yt-dlp finds creators; crawl4ai reads a lead's website for emails; gosom finds local businesses.

## The tools step by step

### 1. Google Maps: `app\gosom-google-maps-scraper\gmaps.exe`
1. Reads `queries.txt`, one search per line.
2. Opens Chromium (own download on first start), scrolls results to `-depth`, visits listings, optionally visits each website for emails (`-email`).
3. Writes one CSV row per business. Columns (upstream README): `input_id,link,title,category,address,...,website,phone,...,review_count,review_rating,...,emails`.
External: Google Maps. Version 1.18.1. Not verified by a run.

### 2. YouTube via yt-dlp: `app\yt-dlp\yt_leads.ps1` + `yt-dlp.exe`
1. Search: `yt-dlp ytsearch<Max>:<Query> --flat-playlist --dump-json` gives one JSON line per video.
2. Keeps the first video of each unique `channel_id`; waits `-DelayMs` (default 2000 ms) per new channel.
3. For each channel: `yt-dlp <channel_url>/videos --playlist-items 1 --dump-single-json` gives `channel_follower_count` and the About `description`.
4. Drops channels outside `-MinSubs`..`-MaxSubs` (defaults 5000..500000). A channel with no subscriber count counts as 0 and is dropped.
5. Finds emails in the description with a regex; several are joined with `;`.
6. Writes the CSV (UTF-8) with columns `title,website,email,subscribers,channel_id,latest_video,source_query,description`. `website` is the channel URL, not the creator's own site.
External: YouTube (no key). Script finds `yt-dlp.exe` in its own folder.

### 3. YouTube via scrapetube: `app\scrapetube\test_scrapetube.py`
Runs `scrapetube.get_search("gym owner vlog", limit=20, results_type="channel")` (query is fixed in the file), keeps `channel_id`, `title`, `subs_text`, `handle` and writes `sample_channels.json`. No email or description (use yt-dlp for those).

### 4. Websites: `app\crawl4ai\site_leads.py`
1. Takes one URL from the command line.
2. Opens the page, then `<url>/contact`, in headless Chromium via crawl4ai.
3. Regex-finds emails (drops names ending `.png .jpg .webp`) and links to instagram, facebook, linkedin, tiktok, twitter, x, youtube.
4. Prints JSON (first 1500 characters) and writes `sample_site_crawl.json`.

## Files and folders
| Path | Role |
|---|---|
| `install\INSTALL.cmd`, `install\install.ps1` | Installer and `-Check` dry run |
| `app\` | Tools; its own git repo. Ignored by git: `.venv/`, `*.exe`, `__pycache__/`, `.setup-done`, `pip_*.txt`, `yt-dlp/sample_channel.json` |
| `app\crawl4ai\.setup-done` | Marker so Chromium setup is not repeated |
| `docs\INTEGRATION.md`, `docs\TOOLS-MANIFEST.md` | Commands, CSV formats; versions, sources, manual reinstall |
| `backups\backup.ps1` | Zips the folder (without `.venv`) into `backups\` |
| `secrets\` | Empty on purpose |
| `proof\` | Installer test output |

## Storage
Only files. No database (`database\README.md`). crawl4ai-setup also initialises crawl4ai's own small local database and browser download outside this folder; exact location not verified.

## External services
GitHub releases (gmaps.exe, yt-dlp.exe, checksums), PyPI (scrapetube, crawl4ai), winget (Python), Google Maps, YouTube, the websites you crawl. No API keys for any.

## Versions (pinned in `install\install.ps1`)
gosom 1.18.1, scrapetube 2.6.0, crawl4ai 0.9.5, yt-dlp = latest at download time (this PC: 2026.10.26), Python 3.12.

## Schedule
None. Ideas only (GitHub Actions cron, Windows Task Scheduler) in `docs\INTEGRATION.md`.
