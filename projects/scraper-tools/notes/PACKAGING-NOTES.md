# Packaging notes 2026-11-05
- scraper-tools: app = copy of D:\All Automations Records\Scraper Tools (no .venv). Binaries and venvs ignored in app git, restored by install.ps1. Versions: docs\TOOLS-MANIFEST.md.
- yt-creator-finder: app = copy of yt-creator-client-finder with original git (main). Zips in archive\. No .env or key files existed in the source, so secrets\ holds only checklist.
- Hub git status shows other sessions' pending changes; not touched.
- Installer tested 2026-11-05 in temp copies (removed): yt-creator-finder real install OK, 22 tests pass; scraper-tools full install OK incl. downloads (gmaps, yt-dlp checksum-verified), venvs, Chromium. proof\installer-test-2026-11-05.txt
