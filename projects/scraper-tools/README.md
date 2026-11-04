# Scraper Tools

Four free tools that find business leads from public data: Google Maps listings (gosom), YouTube channels (yt-dlp, scrapetube) and website emails/socials (crawl4ai). Output is CSV/JSON that the lead bot importer reads. No accounts, no keys.

## Start here
1. New PC? Read `SETUP-GUIDE.md` section 10, then double-click `install\INSTALL.cmd`.
2. Just using the tools? See `SETUP-GUIDE.md` section 7 and `docs\INTEGRATION.md`.
3. Versions and re-download steps: `docs\TOOLS-MANIFEST.md`.

## Folder map
| Folder / file | What is inside |
|---|---|
| `SETUP-GUIDE.md` | The 10-section roadmap for a non-expert; links to `GUIDE/` |
| `GUIDE/` | 00 start, 01 roadmap, 02 architecture, 03 how to change, 04 troubleshooting, 05 accounts and keys (none needed) |
| `install\` | `INSTALL.cmd` (double-click) runs `install.ps1` (`-Check` = dry run). Re-downloads missing programs |
| `app\` | The tools: `gosom-google-maps-scraper\`, `yt-dlp\`, `scrapetube\`, `crawl4ai\` (own git; `.exe` files and `.venv` folders are not in git, the installer restores them) |
| `docs\` | `TOOLS-MANIFEST.md` (versions, sources, reinstall), `INTEGRATION.md` (commands, CSV formats), original `README.md` |
| `database\` | "No database" note |
| `secrets\` | Empty on purpose (no keys needed) + checklist |
| `backups\` | `backup.ps1` (folder zip) |
| `reference\` | Old CLAUDE.md from D:\ |
| `notes\`, `proof\`, `archive\` | Hand-over notes, installer test output, old files |
