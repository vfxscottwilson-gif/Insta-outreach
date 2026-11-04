# INTEGRATION.md — exact formats, commands, scheduling

Status legend: **TESTED** = run here with real output saved; **UNTESTED** = formats taken from the upstream README/source, not run here.

## 1. gosom/google-maps-scraper v1.18.1 (MIT) — UNTESTED
Installed: `gosom-google-maps-scraper\gmaps.exe` (official release `google_maps_scraper-1.18.1-windows-amd64.exe`, 61 MB). **Not executed**: the session's safety classifier blocked running it (no published checksum to verify). Run it yourself once to confirm; it downloads its own Chromium (Playwright) on first start.

**Input**: text file, one search per line, e.g. `queries.txt`
```
gym in Austin TX
independent real estate agency in Leeds UK
fine dining restaurant group in Dubai
```
**Command (Windows)**
```
gmaps.exe -input queries.txt -results gym_results.csv -email -depth 10 -lang en -exit-on-inactivity 3m -c 2
```
Useful flags: `-json` (JSON output), `-geo "30.27,-97.74" -radius 5000`, `-fast-mode` (fewer fields, faster, no email), `-c N` concurrency, `-depth N` scroll depth (more results per query).

**CSV columns (36, in order, from upstream README)**:
`input_id,link,title,category,address,open_hours,popular_times,website,phone,plus_code,review_count,review_rating,reviews_per_rating,latitude,longitude,cid,status,descriptions,reviews_link,thumbnail,timezone,price_range,data_id,street_view_url,place_id,images,reservations,order_online,menu,owner,complete_address,credit_cards_accepted,about,user_reviews,user_reviews_extended,emails`

Mapping to lead fields: name=`title`, website=`website`, phone=`phone`, address=`address`/`complete_address`, rating=`review_rating`, reviews=`review_count`, emails=`emails` (needs `-email`; may be `;`/`,` separated — importer should split on both), category=`category`. No owner name, no socials (get those from the website crawl step). `owner` is only a claimed-listing flag, not a person.
Sample row shape (illustrative, not from a real run): `q1,https://www.google.com/maps/place/...,Iron Works Gym,Gym,"12 Main St, Austin, TX",...,https://ironworksgym.com,+1 512-555-0100,...,214,4.8,...,info@ironworksgym.com`

**Schedule**: GitHub Actions `ubuntu-latest` using the Linux binary (`google_maps_scraper-1.18.1-linux-amd64`) or Docker `gosom/google-maps-scraper`; cron e.g. `0 2 * * *`, upload CSV as artifact or commit it. Windows: Task Scheduler running a `.bat` with the command above. Actions runner IPs get blocked more often than home IPs; keep `-c` low.

**Leads/day (estimate, unverified)**: ~100–300 listings/query-hour at `-c 2`; with `-email`, ~25–40% have a usable email. One machine ≈ 150–500 emailed leads/day if you feed ~100+ city×niche queries.
**Risk**: Scraping Google Maps violates Google ToS (not a crime per se, but IP blocks/CAPTCHAs likely). Collecting business emails for cold outreach: CAN-SPAM (US) needs opt-out + address; **UK/AU/NZ/IE/EU/UAE rules are stricter** (UK PECR: fine to B2B corporate addresses, sole traders need consent; AU Spam Act requires inferred/express consent + unsubscribe; Ireland/EU GDPR legitimate-interest + opt-out). Verify before mass sending.

## 2. yt-dlp 2026.10.26 (Unlicense) — TESTED (no API key, no quota)
Installed: `yt-dlp\yt-dlp.exe` (SHA-256 verified against the official `SHA2-256SUMS`). Wrapper: `yt-dlp\yt_leads.ps1`.

**Step A – discover** (search → one JSON per video):
```
yt-dlp.exe "ytsearch50:gym owner vlog" --flat-playlist --dump-json --no-warnings > search.jsonl
```
Fields used: `channel_id, channel, channel_url, uploader_id (@handle), uploader_url, title, view_count, duration` (sample: `sample_search.jsonl`, 15 rows).
**Step B – channel facts**:
```
yt-dlp.exe "https://www.youtube.com/@handle/videos" --playlist-items 1 --dump-single-json --no-warnings
```
Fields: `channel_follower_count` (subs, rounded e.g. 10100), `description` (channel About text — often contains a business email/links), `uploader_url`, `channel_id`, plus `entries[0].upload_date` for activity (sample: `sample_channel.json`; real hit: description exposed `alex@wallacetrainingsystems.com`).
**Wrapper** (does A+B, filters subs, regex-extracts emails):
```
powershell -File yt_leads.ps1 -Query "personal trainer youtube channel" -Max 50 -MinSubs 5000 -MaxSubs 500000 -Out yt_leads.csv
```
**CSV columns (exact)**: `title,website,email,subscribers,channel_id,latest_video,source_query,description`
Sample row (real, `sample_yt_leads.csv`): `Total Body Training,https://www.youtube.com/@TotalBodyTraining,,5580,...`
`title`/`website`/`email` match the importer's generic aliases (website = channel URL; the creator's own site must be taken from description links).
**Schedule**: Actions `ubuntu-latest` (`pip install yt-dlp` or the Linux binary) with a matrix of queries; Windows Task Scheduler for `yt_leads.ps1`. Keep ~2 s between channel fetches.
**Leads/day**: ~1 search returns up to ~50–100 videos, ~30–60% unique channels; subs filter passes ~30–50%; description email present ~10–20%. Roughly 150–400 channels/day of which ~20–60 have a public email. **Observed here: 12 results → 1 channel passed the filter**, so use many niche queries ("gym tour", "realtor vlog", "restaurant owner"...).
**Risk**: Violates YouTube ToS (automated access), IP throttling possible; data is public. Hidden "business email" on the About tab (behind CAPTCHA) is **not** collected.

## 2b. scrapetube 2.6.0 (MIT) — TESTED (no API key)
Installed: `scrapetube\.venv` (Python 3.12.10; use `scrapetube\.venv\Scripts\python.exe`). Script: `scrapetube\test_scrapetube.py`.
Best use: **channel search with subscriber text in one call, ~20 channels per call, no per-channel fetch**:
```python
import scrapetube
for c in scrapetube.get_search("gym owner vlog", limit=20, results_type="channel"):
    # c["channelId"], c["title"]["simpleText"], c["subscriberCountText"/"videoCountText"]["simpleText"] (e.g. "2.37K subscribers"),
    # c["navigationEndpoint"]["commandMetadata"]["webCommandMetadata"]["url"] (e.g. "/@handle")
```
Output JSON (real, `sample_channels.json`): `[{"channel_id":"UCKaTqGqGizyEk9iz2yXIQTw","title":"Punjabi Gym Vlogger","subs_text":"2.37K subscribers","handle":"/@punjabigymvlogger6272"}, ...]` (20 rows).
Gives NO email/description: parse `subs_text` (K/M), filter 5k–500k, then fetch the About text with yt-dlp (step B above) only for survivors → far fewer yt-dlp calls. Also `scrapetube.get_channel(channel_url=...)` lists a channel's videos (activity check).
Schedule: Actions `pip install scrapetube`; Windows Task Scheduler. Same YouTube ToS/throttling risk as yt-dlp.

## 3. Tools researched but NOT installed (blocked or no Windows build)
- theHarvester and instaloader were not installed (low value / ToS risk).

## 2c. crawl4ai 0.9.5 (Apache-2.0) — TESTED (website → emails + socials)
Installed: `crawl4ai\.venv` (+ Chromium via `crawl4ai-setup`). Script: `crawl4ai\site_leads.py`.
```
set CRAWL4AI_NO_CLOUD_NOTICE=1
crawl4ai\.venv\Scripts\python.exe crawl4ai\site_leads.py https://example-gym.com
```
Output JSON (real, `sample_site_crawl.json`): `{"url":"https://wallacetrainingsystems.com","emails":["train@wallacefitnesscenter.com"],"socials":["https://www.instagram.com/wallacefitnesscenter", "https://www.facebook.com/wallacefitnesscenter", ...]}`
Fetches home + `/contact` (the /contact fetch was blocked by anti-bot on that site; handle failures per URL). ~8 s for a cold page, <1 s afterwards; run 3–5 sites in parallel. Socials list includes tracking-pixel junk URLs (filter `facebook.com/tr?`). Owner names are NOT extracted by this script (add an /about parse or LLM step).
Use: feed it the `website` column from gosom/OSM rows that have no email. Schedule: Actions (`pip install crawl4ai && crawl4ai-setup`) or Task Scheduler. Risk: low (public pages; respect robots.txt and rate limits).
- **reacher / check-if-email-exists v0.11.11 (MIT)**: only Linux/macOS binaries or Docker `reacherhq/backend`; no Windows binary. Needs outbound **port 25**, which is blocked on GitHub Actions runners and most home ISPs → only usable from a VPS. Output is JSON: `{input, is_reachable: safe|risky|invalid|unknown, misc, mx, smtp, syntax}`.

## Generic importer notes
Accept aliases: `title|name|business_name`, `website|url|site`, `phone`, `address|complete_address`, `review_rating|rating`, `review_count|reviews`, `emails|email` (split on `,` `;` whitespace), `category`, `subscribers`. Dedupe on domain (website host) then on phone; skip rows without website and email.
