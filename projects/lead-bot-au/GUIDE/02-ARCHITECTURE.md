# 02 Architecture: how Lead Bot AU works

Checked against `app\src\*.py`, `app\.github\workflows\run-lead-bot.yml`, `app\AU_EDITION.md` and `app\CONTRACT.md` (v5). Anything I could not run live is marked "not verified".

The AU bot is the worldwide bot with one different file: `app\src\market.py` sets `MARKET` to AU. Everything else is identical code.

## 1. The big picture

No server, no database, no website. Three things only:

| Piece | Where it lives | Job |
|---|---|---|
| The code (Python 3.12) | `app\src\` here and on GitHub | finds, reads, scores and writes leads |
| GitHub Actions | GitHub cloud | starts the code by itself twice a day |
| Google Sheet | Google cloud | ONE sheet (secret `SHEET_ID_AU_ONLY`) that you read |

Your PC is only needed to install, to test with `--local` (CSV files, no Google) and to edit.

## 2. Data flow (one run)

```
GitHub schedule (19:00 and 07:00 UTC = about 6am / 6pm Sydney) or "Run workflow"
   |
   v
[setup job]   selftest.py + unit tests (offline); a failure stops the run
              leadbot.py --setup : creates control tabs + Stats once
   |
   v
[collect jobs]  6 jobs, ONE AT A TIME (max-parallel 1) because they all write the same sheet
   nsw-act   (AU-NSW, AU-ACT; sources input + maps)
   vic-tas   (AU-VIC, AU-TAS; maps)
   qld       (AU-QLD; maps)
   wa-sa-nt  (AU-WA, AU-SA, AU-NT; maps)
   youtube   (YouTube creators)
   imports   (scraper files / Import tab)
   each job:
     1 read the control tabs (Rules, Niches, Locations, Options, Seen, Blacklist ...)
     2 get candidates from its sources (table below)
     3 drop duplicates (Seen tab + Place Id already in the sheet), chains, blocked names
     4 read the website: emails, phones, socials, owner name printed on the site, ABN printed on the site
     5 optional helpers (ABN Lookup, Hunter, Serper ...) only where a key exists
     6 score: R (revenue proxy), S (social gap), A (agency) -> Segment + ICP score /10
     7 keep only ICP >= MIN_ICP_SCORE (default 7)
     8 one optional AI call writes "Lead Insight"; no key or a 429 -> fact-only text
     9 APPEND the row under the last row of that niche's tab
   |
   v
[finish job]  leadbot.py --finish : Stats tab (values overwritten in place)
```

Each job also takes a lock in the hidden `Meta` tab, so a second run or a local run cannot write at the same time.

| Source (`SOURCES`) | Key needed? | Code |
|---|---|---|
| `input`: the `Leads Input` tab | no | `leadbot.py` |
| `imports`: files in `app\imports\` or the `Import` tab; rows from other countries are skipped in this edition | no | `importer.py` |
| `maps`: free OpenStreetMap Overpass + Nominatim | no | `osm.py` |
| `maps` with Google Places / Serper / Apify | `GOOGLE_PLACES_API_KEY`; `SOURCE=serper`; `USE_APIFY_MAPS=Yes` | `places.py`, `optional.py` |
| `youtube`: free page reader, optional YouTube Data API | no / `YOUTUBE_API_KEY_1`,`_2` | `yt.py` |

## 3. Modules (`app\src\`)

| File | What it does |
|---|---|
| `leadbot.py` | main program and command line (`--local`, `--dry`, `--setup`, `--finish`, `--no-finish`); sheet reading and writing, retry on Google 429, write lock |
| `defaults.py` | first-run content; for AU: 82 lead columns, 31 niches, 73 locations |
| `enrich.py` | reads the website (honours robots.txt): emails, phones, socials, owner name, ABN |
| `quality.py`, `score.py` | R / S / A sub-scores, Segment, ICP score, pitch price |
| `insight.py`, `ai.py` | Lead Insight (AI or fact-only) and AI key failover (Gemini, Groq, OpenRouter, Mistral, Cerebras) |
| `keys.py` | reads secrets, trims and shape-checks them, prints the masked "registered / ignored" report |
| `optional.py` | optional helpers (ABN Lookup, Jina, Hunter, ZeroBounce, Apify, Apollo, Meta Instagram ...). Each fails quietly; a 429/401/402/403 switches that service off for the rest of the run |
| `osm.py`, `places.py`, `yt.py`, `importer.py` | the sources above |
| `localsheet.py` | fake offline "sheet" = CSV files in `app\local_sheet\` |
| `market.py` | `MARKET` = AU in this repo |
| `selftest.py` | offline checks run before every real run |

## 4. The Google Sheet

Tab 1 is `Stats` (totals, leads today, PRIME count, run health, keys registered). There is no Master Dashboard in this edition.

| Control tab | Purpose |
|---|---|
| Rules | `Setting / Value / What it does`; AU defaults: `YT_COUNTRIES=AU`, `TIMEZONE=Australia/Sydney`, `PITCH_CURRENCY=AUD` |
| Niches | one row per niche: search terms, budget fit, OSM selectors, regex filters |
| Locations | `Country, State, City, Search Area, Enabled (Yes/No), Priority (1-3), Latitude, Longitude, Radius km`; 73 Australian areas |
| Options | keys you may paste instead of GitHub secrets (a secret wins) |
| Leads Input | your own businesses |
| Import | pasted scraper CSV rows with header |
| Seen, Searches, Snapshots | memory: processed leads, search history, review counts |
| Blacklist, Run Log, Playbook | do-not-contact list, one row per job, Australian rules of thumb (Spam Act, AHPRA/TGA, Do Not Call Register) |
| Meta (hidden) | counters, run health, write lock; do not edit |

Lead tabs: one per niche (a tab with `Place Id` and `Company Name` in row 1). The first 74 columns are the worldwide ones (`LEAD_H`); this edition appends 8 at the end, so positions never move: `ABN`, `ABR Entity Name`, `Entity Type`, `GST Registered`, `ABN Active Since`, `Business Age (yrs)`, `Phone Type`, `AU Timezone`. Columns the outreach bot reads are listed in `app\CONTRACT.md` section 3.

Segments: PRIME, PRIME-REVIEW, GROWING, HAS-AGENCY, POLISHED-NO-SIGNAL. Rows are append-only; `Status` and `My Notes` are never touched.

## 5. APIs and services

| Service | Required? | Notes |
|---|---|---|
| Google Sheets API + Google Drive API (service account `GOOGLE_SA`) | yes | 60 reads per minute per service account; retries on 429 |
| GitHub Actions | for the daily run | |
| OpenStreetMap Overpass, Nominatim | built in, no key | free servers, can be busy |
| ABN Lookup (abr.business.gov.au), key name `ABN_GUID` | optional, free GUID | without it only ABNs printed on the site are filled |
| Gemini, Groq, OpenRouter, Mistral, Cerebras | optional | Lead Insight only |
| Google Places, YouTube Data, Serper, Brave, Hunter, ZeroBounce, Apollo, Apify, ZenRows, Jina, Snov, Prospeo, Reacher, Meta Instagram | optional | each switches itself off without a key |

Key names: `GUIDE\05-ACCOUNTS-AND-KEYS.md`. Free-tier sizes change: not verified, check each vendor.

## 6. GitHub Actions schedule

File `app\.github\workflows\run-lead-bot.yml`, workflow "Run AU Lead Bot".

| Item | Value |
|---|---|
| Cron (UTC) | `0 19 * * *` (6am Sydney in summer, 5am in winter) and `0 7 * * *`, plus the "Run workflow" button |
| Jobs | `setup` (15 min) then `collect (name)` x 6, one at a time, 60 min limit each, the bot stops itself after Rules `MAX_RUNTIME_MIN` = 42, then `finish` (15 min) |
| Queueing | group `au-lead-bot`: a new run waits for the old one |
| Cost | workflow comment: needs a PUBLIC repo for unlimited minutes. Private repo: variable `LEAD_MATRIX` = `{"include":[{"name":"all","regions":"","sources":""}]}` and delete the second cron line. GitHub's current free-minute numbers: not verified |
