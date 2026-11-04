# Scraper Tools

**Purpose:** free, open-source lead sources that feed the lead bot's CSV importer. Full shortlist: `README.md`. Exact commands and CSV formats: `INTEGRATION.md`.

| Tool | Folder | Status (2026-10-31) |
|---|---|---|
| gosom google-maps-scraper v1.18.1 | `gosom-google-maps-scraper/gmaps.exe` | Downloaded, **not run yet** |
| yt-dlp + `yt_leads.ps1` | `yt-dlp/` | Installed + tested |
| scrapetube | `scrapetube/.venv` | Installed + tested |
| crawl4ai | `crawl4ai/.venv` | Installed + tested (2026-11-01), `site_leads.py` |

## Rules for Claude
- Not a git repo (binaries + venvs). Don't commit these.
- Public data only, no logins (no instaloader).
- Test with 1-3 queries first, save sample output, then scale.
- Cold-email law differs by country (see INTEGRATION.md §1).
