# 02 Architecture: how Lead Bot Worldwide works

Checked against `app\src\*.py`, `app\.github\workflows\run-lead-bot.yml` and `app\CONTRACT.md` (v5). Anything I could not run live is marked "not verified".

## 1. The big picture

No server, no database, no website. Three things only:

| Piece | Where it lives | Job |
|---|---|---|
| The code (Python 3.12) | `app\src\` here and on GitHub | finds, reads, scores and writes leads |
| GitHub Actions | GitHub cloud | starts the code by itself twice a day |
| Google Sheets | Google cloud | the "database" you read: one sheet per country plus one YouTube sheet |

Your PC is only needed to install, to test with `--local` (writes CSV files, no Google) and to edit.

## 2. Data flow (one run)

```
GitHub schedule (20:00 and 08:00 UTC) or the "Run workflow" button
   |
   v
[setup job]   selftest.py + unit tests (offline); any failure stops the whole run
              leadbot.py --setup --all : creates control tabs + Stats in every sheet that has an id
   |
   v
[collect jobs]  one per country, 5 at a time, each is the ONLY writer of its own sheet
   us  ca  uk  au  nz  ie  youtube  uae  saudi  qatar
   each job:
     1 read the control tabs (Rules, Niches, Locations, Options, Seen, Blacklist ...)
     2 get candidate businesses from the sources (table below)
     3 drop duplicates (Seen tab + Place Id already in the sheet), chains, blocked names
     4 read the business website: emails, phones, social links, owner name printed on the site
     5 optional helpers (Hunter, Serper, Apollo ...) only where a key exists
     6 score: R (revenue proxy), S (social gap), A (agency) -> Segment + ICP score /10
     7 keep only ICP >= MIN_ICP_SCORE (default 7)
     8 one optional AI call writes "Lead Insight"; no key or a 429 -> fact-only text
     9 APPEND the row under the last row of that niche's tab
   |
   v
[finish job]  leadbot.py --finish --all : Stats tab in every sheet + Master Dashboard (US sheet)
```

Candidate sources (`SOURCES` = `input,imports,maps,youtube`; code in `leadbot.py`):

| Source | Key needed? | Code |
|---|---|---|
| `Leads Input` tab (businesses you type in) | no | `leadbot.py` |
| Scraper imports: files in `app\imports\` or rows pasted in the `Import` tab | no | `importer.py` |
| Free map search, OpenStreetMap Overpass (+ Nominatim geocoding) | no | `osm.py` |
| Google Places API (New) text search | `GOOGLE_PLACES_API_KEY` | `places.py` |
| Serper Google Maps or Apify Google Maps | optional keys; `SOURCE=serper` or `USE_APIFY_MAPS=Yes` | `leadbot.py`, `optional.py` |
| YouTube creators: free page reader, optional YouTube Data API | no / `YOUTUBE_API_KEY_1`,`_2` | `yt.py` |

`SOURCE=auto` (Rules tab) means: Google Places if a Places key exists, otherwise free OpenStreetMap.

## 3. Modules (`app\src\`)

| File | What it does |
|---|---|
| `leadbot.py` | main program and command line (`--local`, `--dry`, `--setup`, `--finish`, `--no-finish`, `--all`, `--country XX`); reads and writes the sheet, retries Google 429, write lock |
| `defaults.py` | first-run content: 74 lead columns, 127 Rules, 35 Niches, 97 Locations, Options, Playbook |
| `enrich.py` | reads the website (honours robots.txt): emails, phones, socials, owner name |
| `quality.py` | R / S / A sub-scores and the Segment |
| `score.py` | ICP score and pitch price |
| `insight.py` | "Lead Insight": AI text or a fact-only fallback; a person's name is accepted only if it appears word for word on the site |
| `ai.py` | AI key failover (Gemini, Groq, OpenRouter, Mistral, Cerebras) |
| `keys.py` | reads secrets, trims and shape-checks them, prints the masked "registered / ignored" report |
| `optional.py` | optional helpers (Jina, Hunter, ZeroBounce, Apify, Apollo, Meta Instagram, ...); each fails quietly, and a 429/401/402/403 switches that service off for the rest of the run |
| `osm.py`, `places.py`, `yt.py`, `importer.py` | the sources above |
| `localsheet.py` | fake offline "sheet" = CSV files in `app\local_sheet\` |
| `market.py` | one line, `MARKET`: WORLD here, AU in the AU-only twin (the only code difference between the two bots) |
| `selftest.py` | offline checks run before every real run |

## 4. Google Sheets layout

Sheets: `SHEET_ID_US, CA, GB, AU, NZ, IE, AE, SA, QA` plus `SHEET_ID_YOUTUBE`. A missing secret makes that job print `SKIP` and end green.

Control tabs (created automatically in each sheet):

| Tab | Purpose |
|---|---|
| Stats (US sheet: `Master Dashboard` + `US Stats`) | totals, leads today, PRIME count, run health, keys registered; values overwritten in place |
| Rules | columns `Setting / Value / What it does` |
| Niches | one row per niche: search terms, budget fit, OSM selectors, regex filters, thresholds |
| Locations | `Country, State, City, Search Area, Enabled (Yes/No), Priority (1-3), Latitude, Longitude, Radius km` |
| Options | keys you may paste instead of GitHub secrets (a GitHub secret wins) |
| Leads Input | your own businesses: `Business Name, Website, Instagram, Email, Phone, Niche, City, State, Notes, Country` |
| Import | pasted scraper CSV rows, header row included |
| Seen, Searches, Snapshots | memory: processed leads, search history, first review counts |
| Blacklist, Run Log, Playbook | do-not-contact list, one row per run, rules of thumb |
| Meta (hidden) | counters, run health, write lock; do not edit |

Lead tabs: one per niche. A tab is a lead tab when row 1 contains both `Place Id` and `Company Name`. Columns are found by header name, so you can reorder or add your own. The full column list is `LEAD_H` in `app\src\defaults.py`; the ones the outreach bot reads are in `app\CONTRACT.md` section 3 (Place Id, Company Name, Decision Maker Name, First Name, Personal Email, Generic Email, Other Emails, Niche, Country, Country Code, City, Website, socials, Lead Insight, Segment, ICP Score /10, Lead Added On, Status).

Segments: PRIME, PRIME-REVIEW, GROWING, HAS-AGENCY, POLISHED-NO-SIGNAL. Rows are append-only: never sorted, moved or rewritten, so your `Status` and `My Notes` stay put.

## 5. APIs and services

| Service | Required? | Notes |
|---|---|---|
| Google Sheets API + Google Drive API (service account, secret `GOOGLE_SA`) | yes | 60 reads per minute per service account, shared by all jobs; the code backs off and retries on 429 |
| GitHub Actions | for the daily run | |
| OpenStreetMap Overpass, Nominatim | built in, no key | free servers, can be busy |
| Gemini, Groq, OpenRouter, Mistral, Cerebras | optional | only for Lead Insight |
| Google Places, YouTube Data, Serper, Brave, Hunter, ZeroBounce, Apollo, Apify, ZenRows, Jina, Snov, Prospeo, Reacher, ABN Lookup, NZBN, Meta Instagram | optional | each module switches itself off without a key |

Key names: `Guide\Accounts And Keys.md`. Free-tier sizes change often: not verified, check each vendor.

## 6. GitHub Actions schedule

File `app\.github\workflows\run-lead-bot.yml`, workflow "Run Lead Bot".

| Item | Value |
|---|---|
| Cron (UTC) | `0 20 * * *` and `0 8 * * *`, plus the manual "Run workflow" button |
| Jobs | `setup` (15 min limit) then `collect (name)` x 10 (60 min limit each, 5 at once, the bot stops itself after Rules `MAX_RUNTIME_MIN` = 42) then `finish` (15 min) |
| Queueing | group `lead-bot`: a new run waits for the old one, never two writers |
| Python | 3.12, `pip install -r requirements.txt` |
| Cost | the workflow comment says about 900 runner-minutes a day, so it needs a PUBLIC repo (no secrets are stored in the repo). For a PRIVATE repo set variable `LEAD_MATRIX` to `{"include":[{"name":"us","country":"US"}]}` and delete the second cron line. Today's GitHub free-minute numbers: not verified |
