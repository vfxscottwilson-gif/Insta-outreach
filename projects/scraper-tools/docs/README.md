# Scraper Tools — shortlist (checked 2026-10-31 via GitHub API)

| # | Tool | Stars | Last push | License | Lead quality | Volume/day | Risk | Windows / Actions | Status |
|---|------|-------|-----------|---------|--------------|------------|------|-------------------|--------|
| 1 | gosom/google-maps-scraper | 7.1k | 2026-10-21 | MIT | High (phone, site, rating, emails) | 150–500 emailed | Google ToS, IP blocks | .exe + Linux bin + Docker | Downloaded, **not run** (blocked) |
| 2 | yt-dlp (+ `yt_leads.ps1`) | 204k | 2026-10-29 | Unlicense | Med (subs + sometimes email) | 20–60 with email | YouTube ToS | .exe / pip, Actions OK | **Installed + tested** |
| 3 | crawl4ai | 87k | 2026-10-30 | Apache-2.0 | High for site→email/socials/owner | 500+ sites | Low (public pages, robots) | pip, needs Python | Not installed (no Python) |
| 4 | omkarcloud/google-maps-scraper | 3.9k | 2026-10-19 | MIT | High | similar to #1 | Google ToS | Python/Node | Not installed; #1 preferred (single binary) |
| 5 | reacher | 10k | 2026-10-30 | MIT | Verifies emails (cuts bounces) | n/a | Port 25 blocked on Actions/ISPs | Linux/Docker only | Not installed; VPS needed |
| 6 | scrapetube | 0.5k | 2025-09 | MIT | = yt-dlp but no subs | – | YouTube ToS | pip | Redundant; skipped |
| 7 | theHarvester | 18k | 2026-10-30 | GPL-2.0 | Low-Med (domain emails, many sources need keys) | low | Low | pip | Not installed (no Python) |
| 8 | instaloader | 13.7k | 2026-10-26 | MIT | Public bios only | low | **High: Instagram ToS, login bans** | pip | Skipped (rule: no logins) |
| ✗ | youtube-search-python | 0.8k | 2022 | MIT | – | – | – | – | **Archived, dead — don't use** |

OSM Overpass is already used by the bot (free, no ToS risk, but few emails).

## Recommended daily stack to reach 400+ qualified leads/day
1. **gosom** nightly in GitHub Actions/Windows: ~150 queries (niche × city across US/UK/CA/AU/NZ/IE/UAE), `-email -depth 10 -c 2` → 1,500–4,000 listings, ~30% with emails.
2. **Website crawl step** (crawl4ai once Python exists, or the bot's existing site reader) on rows with a website but no email: contact page, socials, owner/"about" names.
3. **yt-dlp YouTube script** for the creator vertical: ~30 queries/day.
4. Dedupe on domain, score ≥7/10, import via CSV importer (formats: `INTEGRATION.md`).
5. Optional: reacher on a cheap VPS for SMTP verification.

Honest estimate: 400+ *emailed* leads/day is plausible only with gosom running ≥150 queries/day across several IPs; 20–60/day from the free YouTube path. Numbers are estimates, not measured here.

## To finish (what failed)
- **gosom not run**: the safety classifier blocked executing it. Run `gmaps.exe -input queries.txt -results sample.csv -email -depth 1 -exit-on-inactivity 2m` yourself (or allow it), then save the output in its folder.
- **Python 3.12.10 now installed.** scrapetube: installed + tested (`scrapetube\sample_channels.json`; returns subs text for ~20 channels per call, no key — best YouTube discovery step, then yt-dlp for About emails).
- **crawl4ai: DONE + tested** (see INTEGRATION.md §2c; sample `crawl4ai\sample_site_crawl.json`). Old note, now obsolete: venv at `crawl4ai\.venv`; `pip install crawl4ai` (v0.9.5) is running very slowly (downloads stall; progress log `crawl4ai\pip_out.txt`). When it prints "Successfully installed", run `crawl4ai\.venv\Scripts\crawl4ai-setup.exe` (downloads Chromium) and test with `crawl4ai\.venv\Scripts\crwl.exe https://example.com`. Not yet tested, no sample output. theHarvester/instaloader not installed.
- Legal: cold email rules differ by country (see INTEGRATION.md §1). Public data only, no logins.
