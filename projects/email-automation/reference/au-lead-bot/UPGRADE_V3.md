# Lead Bot v3: worldwide, more niches, free YouTube, scraper imports, parallel runs

v3 is a drop-in upgrade of v2 (same sheet, same columns, one column renamed: see section 2). Tested locally:
`python src/selftest.py` (35 checks) + `python -m unittest discover -s tests` (52 tests, network mocked, including a full
dry run and a full local run), plus live runs against real OpenStreetMap, websites and YouTube (section 5).

## 1. Files changed (copy into your GitHub repo, same paths)

| File | Status | What changed |
|---|---|---|
| `src/leadbot.py` | changed | Per-location country (no more "not in Australia" reject), niche rules (exclude words / must-match / reject regex / chain cut-off), OSM brand + takeaway filters, scraper import step, YouTube chooser, Places `regionCode` per location + monthly safety cap, OSM failure breaker, `--local / --setup / --finish / --no-finish`, `REGIONS` / `SOURCES` filters for parallel jobs, dry run writes nothing, v2 tab header migration, race-safe tab creation |
| `src/defaults.py` | changed | Countries table, **53 new metros** (US, UK, CA, NZ, IE, UAE), new niches (boutique gyms, fine dining / restaurant groups, 4 worldwide YouTube niches), new Rules, international chain blocklist, Playbook rules for US/UK/IE/CA/NZ/UAE |
| `src/yt.py` | rewritten | **Free no-key YouTube reader** (default) + YouTube API as optional fast path, country from YT_COUNTRIES |
| `src/importer.py` | **new** | Reads gosom google-maps-scraper CSV/JSON, the yt-dlp CSV and any CSV/JSON with alias mapping |
| `src/localsheet.py` | **new** | Offline sheet (CSV folder) for `--local` runs and tests |
| `src/osm.py` | changed | **bounding-box queries + wait-and-retry on the main server** (the old `around:` queries timed out on every public server when measured), `!=` / `!~` selectors, country from the Locations row, brand/cuisine/takeaway tags, Nominatim per country |
| `src/enrich.py` | changed | Follows the contact/about/team links the home page really has (fewer 404 guesses), UTF-8 fix, JSON-LD founders inside `@graph`, world city names never taken as people |
| `src/places.py` | small | `regionCode` per location, `priceLevel` field (same SKU, no extra cost) |
| `src/drafts.py` | small | Country-neutral AI prompt (country passed as a fact) |
| `src/selftest.py` | small | Checks the renamed pitch column |
| `tests/test_v3.py`, `tests/test_v31.py`, `tests/au_pipeline_case.py` | **new** | 52 offline tests (incl. a full Australia-edition run) |
| `src/market.py` | **new (v3.1)** | `WORLD` here; `AU` in the Australia-only edition. The only difference between the two repos |
| `imports/README.md` | **new** | How to drop scraper files |
| `.github/workflows/run-lead-bot.yml` | rewritten | setup → 6 parallel jobs (regions/sources) → finish, 2 runs/day, tests before every run |
| `README.md`, `00_START_HERE_SETUP_GUIDE.md` | small | Worldwide wording, new files |

**v3.1 additions (same repo):** `src/optional.py` (Serper, Brave, ZenRows, ABN Lookup, Apify Google Maps helpers),
`src/enrich.py` (ABN checksum, AU phone type/timezone, strict website/LinkedIn matching from search results, ZenRows
fallback), `src/score.py` (business age counts as "established" when there are no reviews), `src/defaults.py`
(5 new Options rows, 13 new Rules), `src/leadbot.py` (website finder, Google rating via Serper, LinkedIn owner, ABN facts,
`SOURCE=serper|apify`, `REGIONS=AU-NSW` style state filter), workflow (4 new optional secrets). An **Australia-only
edition** lives in `D:\All Automations Records\Lead generation\au-only-lead-bot` (see its `AU_EDITION.md`).

## 2. Column contract (for the outreach bot)

Unchanged names and positions, except **one rename**: `Suggested Pitch AUD/mo` → **`Suggested Pitch /mo`**
(same column position; existing tabs are renamed in place on the next run). The currency is in the new column
**`Pitch Currency`** (from Rules `PITCH_CURRENCY`, default `AUD`; set `USD` if you price in dollars US).
Three columns are appended **after `Place Id`**: `Pitch Currency`, `Country Code`, `YT Last Upload (days)`.
`All Leads` keeps merging by position. Outreach bot: read `Suggested Pitch /mo` (fallback to the old name for old exports).

For the outreach/draft bot:
- **`Drafted`** is now in the Status dropdown (after `New`); the dropdown is refreshed on every lead tab each run.
- The lead bot **never rewrites** Status, My Notes or any other cell of an existing lead. It only appends new rows.
  Sorting moves whole rows, so Status and My Notes stay with their lead.
- `All Leads` is a read-only QUERY view, so write Status back to the niche tab. Find the row by **`Place Id`**
  right before writing, because the finish job may re-sort the tab between your read and your write.
- `Place Id` is unique and never changes: `osm:node/123`, a Google place id (`ChIJ...`) from Places or gosom imports,
  `yt:UC...`, `gmapscid:...`, `imp:<hash>`, `input:<hash>`. A business is added once (Seen tab + same website/email check).
  One rare exception: the imports job and a maps job running at the same moment can both add the same business
  under two different ids (OSM id vs Google id). The next run sees it, but the duplicate row stays: dedupe on email before sending.

## 3. Your step-by-step roadmap

1. **Copy the files** (section 1) into the repo and commit. Nothing to change in the sheet: new Rules, niches and
   metros are added automatically on the next run (existing values are never overwritten).
2. **Make the repo public** (Settings → General → Danger zone → Change visibility). Reason: the default workflow uses about
   550 runner-minutes a day; public repos have unlimited free minutes, private ones only 2,000/month. The repo contains
   no keys (they are GitHub Secrets). Do NOT put scraper CSVs in `imports/` of a public repo: paste them into the
   sheet's **Import** tab instead. If you keep it private: set repository variable `LEAD_MATRIX` to
   `{"include":[{"name":"all","regions":"","sources":""}]}` and delete the second `cron` line.
3. In the sheet, Rules tab, set: `TIMEZONE` = your timezone (e.g. `Asia/Karachi`), `PITCH_CURRENCY` (AUD or USD),
   and if you came from v2: `NEW_LEADS_PER_RUN` = 120, `MAX_SEARCH_REQUESTS_PER_RUN` = 40, `PARALLEL_SITE_READS` = 10,
   `MAX_SITE_PAGES` = 5 (v2 sheets keep their old, smaller values).
4. **Actions → Run Lead Bot → Run workflow.** Check Run Log: one row per job (`job[maps US] added=...`).
5. Locations tab: switch whole countries on/off with `Enabled`. Niches tab: the two new niches are on; the old
   "Boutique Gyms & Pilates Studios" row (v2, off) can stay off.
6. **Volume lever (the only real way to 400+/day for free):** run gosom google-maps-scraper on your PC every day
   (see `D:\All Automations Records\Scraper Tools\INTEGRATION.md`), then paste the CSV into the **Import** tab (or
   `imports/` in a private repo). The bot dedupes, reads the websites, scores and keeps only ≥ 7/10.
7. Optional: Google Places key with a hard quota (section 6). Optional: YouTube API key (only speeds up YouTube).
8. After 7 days read Dashboard → "Average leads per day (7 days)". Tune `MIN_ICP_SCORE` only if you must.

## 4. What is new, in plain words

- **Worldwide.** Each Locations row has its own country. Map searches, Google Places (`regionCode`) and geocoding
  use it; the Country / Country Code columns come from the data or the row, never guessed. Drafts and the AI prompt
  no longer say "Australian". `TIMEZONE` is now *your* timezone (default UTC). Health niches get the right rule note per
  country (AHPRA/TGA, ASA/CAP, FTC, DHA...).
- **Niches.** Boutique Fitness Studios & Gyms (owner-operated: franchise brands blocked by name, OSM brand tag and
  "franchise opportunities" text on the site; up to 5 sites allowed before it counts as a chain). Fine Dining &
  Restaurant Groups (cafes, takeaways, fast food, pizza/kebab/burger blocked; the site must show tasting menu /
  degustation / sommelier / awards / private dining, or several venues, or Google price level $$$+). Real estate now
  searches "estate agent / realtor" too and blocks corporate brands (Foxtons, Savills, Purplebricks, Compass...).
  All of this lives in 4 new Niches columns, so you can edit it in the sheet.
- **YouTube without quota.** Default `YT_SOURCE=auto` reads YouTube's public pages (search → About page → RSS feed):
  subscribers, videos, country, description, links, last upload, uploads in 30 days. Polite pauses, max 150 channels
  per run, stops cleanly on 429/consent/captcha. With a `YOUTUBE_API_KEYS` secret the API takes over if the free
  reader is blocked. Countries: `YT_COUNTRIES` (default AU,US,GB,CA,NZ,IE,AE).
- **Scraper import.** Section 3 step 6. Google place ids are kept, so a business found by gosom and later by Places is
  never added twice.
- **Throughput.** 6 parallel jobs (AU+NZ, US, UK+IE, CA+UAE, YouTube, imports) twice a day; 10 parallel site reads;
  home-page link discovery instead of guessing 7 URLs.

## 5. Measured speed and realistic leads/day

**Measured on 2026-10-31** (local PC, real OpenStreetMap + real websites + real YouTube, mocked sheet, no AI key):

| Search (free map) | Businesses | With website | Qualified ≥ 7/10 | Map query | Site pipeline |
|---|---|---|---|---|---|
| Jewellers, Central London | 148 | 72 | **12** | 31 s | 528 s (old batch reader) |
| Kitchen/bath showrooms, Manchester | 34 | 15 | 2 | 32 s | 57 s |
| Pools/landscaping, Kensington · Mortgage brokers, London | 1 · 0 | – | 0 | 41 s · 33 s | – |
| Fine dining, Manhattan | 149 | 121 | **7** (76 rejected as not upscale) | 37 s | 252 s |
| Real estate, Manhattan | 18 | 8 | 4 | 25 s | 44 s |
| Gyms, Miami | 38 | 23 | 6 | 43 s | 29 s |
| Fine dining, Chicago | 149 | 100 | 3 | 38 s | 286 s |
| Real estate, Los Angeles | 13 | 8 | 2 | 36 s | 26 s |
| Gyms, Chicago | 127 | 96 | **13** | 53 s | 128 s |
| **Total, 11 searches** | **677** | | **49 (7%)** | ~37 s avg | ~1-2 s per business |

- Average **~4.5 qualified leads per search** in the good niches, ~3.5 across all niches (some niches/areas have almost
  nothing in OSM). One search costs ~2-3 minutes, so one 42-minute job does ~15-18 searches ≈ **50-80 leads**.
- Typical rejections: no website (OSM has none for ~35% of businesses), not upscale, chain/franchise, ICP < 7.
- Lead quality seen: 50-80% with a Personal Email, ~40-70% with a Decision Maker name (facts from the site).
- **YouTube free reader:** ~7 s per channel. 20 channels → 7 matched size/activity/country → **1** with a public
  email (email is the bottleneck, an API key does not change that). 150 channels per run ≈ 7-10 leads.
- Before the fix in bug 12, 4 of 5 map searches failed and one run produced 4 leads in 15 minutes.

**Realistic leads/day (≥ 7/10):**

| Setup | Leads/day | Notes |
|---|---|---|
| Private repo, 1 job, 1 run/day | **40-80** | fits 2,000 free minutes |
| **Public repo, default** (6 jobs × 2 runs) | **250-450 for the first ~3 weeks**, then **50-100** | 4 map jobs × 2 runs × 50-80, minus slow days. The pool is finite: ~28 niches × 92 areas ≈ 2,600 area+niche pairs ≈ 9,000-12,000 OSM leads in total, then only new map entries and rechecks (every 120 days). Add more suburbs to the Locations tab to extend it. |
| + **gosom imports** 1,500-2,000 rows/day | **+150-300, sustained** | the import job reads ~1,500-2,500 rows in 42 min. Google data has more websites + review counts, so more rows pass |
| + Google Places capped at 1,000/month | +40-70 | estimate (no key to test): 32 requests/day × 20 businesses |
| YouTube (inside the default) | 10-20 | `YT_ALLOW_UNKNOWN_COUNTRY=Yes` adds more but weaker ones |

**Bottom line:** free sources alone give ~250-450/day only while the map pool is fresh; **400+/day sustained needs
the scraper imports** (gosom on your PC). GitHub cost: ~275 runner-minutes per run, ~550/day, so a public repo.
The 7/10 gate, never-invented names/emails and the Seen dedupe stay the same at every volume.
Also: free AI keys (Gemini/Groq) cap drafts at `MAX_AI_EMAILS_PER_RUN` (40) per job; the rest get template drafts.
The outreach bot rewrites drafts anyway.

## 6. Google Places: is it worth adding a credit card?

**Verdict: yes, worth it, as long as you set the quota cap below. It costs $0 inside the cap. It is not required for
400/day, though. Imports are the volume lever (step 6).**

What this code buys (Google's pricing page, updated 2026-10-30):
- The field mask (`websiteUri`, phone, `rating`, `userRatingCount`, `priceLevel` + basic fields) is billed as
  **Places API Text Search Enterprise**. Google bills the highest SKU any requested field belongs to.
- **Free cap: 1,000 requests per month**, then **US$35 per 1,000** (first tier, up to 100,000). The old $200 monthly
  credit ended on 28 Feb 2025. Since 1 Mar 2025 each SKU has its own free monthly cap.
- One request returns up to 20 businesses. Every next-page request is a new billable request. The bot uses at most
  `MAX_PAGES_PER_SEARCH` (2) pages per search.
- 1,000 requests a month ≈ 32 a day ≈ **640 businesses a day** with website, phone, rating, review count, open/closed
  status and price level.

Quality vs free OpenStreetMap:

| | Google Places | OpenStreetMap (default) |
|---|---|---|
| Coverage | Almost every operating business that has a Maps listing | Volunteer-mapped. Good in city centres, patchy in suburbs and for specialists (surgeons, studios) |
| Website on the record | Most listings | Measured: 65% (443 of 677 businesses) |
| Rating + review count | Yes: the "established" and "too big" filters work, and the ICP score gets up to 1.5 extra points | None: neutral score, so some leads miss 7/10 |
| Open/closed | `businessStatus` | Often stale |
| Upscale restaurants | `priceLevel` $$$/$$$$ counts as proof | Website text only |
| Terms | Google ToS (no long-term caching outside the sheet) | ODbL: keep the Data Source column |

Expected effect: about **+40-70 qualified leads/day** on top of OSM (640 listings/day × the 7/10 pass rate measured
below, which is higher with review data).

**How to make it impossible to bill (do all 3):**
1. Google Cloud console → **Google Maps Platform → Quotas** → API **Places API (New)** → the **Text Search requests per
   day** row → **Edit** → **32** → Submit. Also set **requests per minute** to about 10. Google's own advice: "To put a
   hard cap on usage of an API, lower its per-day quota". The cap resets at midnight Pacific time.
2. Keep Rules `PLACES_MAX_REQUESTS_PER_MONTH` = **950**. The bot counts its own requests in the Searches tab
   (Source = Google Places) and switches to OSM when it reaches the cap.
3. Restrict the key (APIs & Services → Credentials) to **Places API (New)** only. Add a **budget alert** of $1. A
   budget alert only emails you; it does not stop billing, so steps 1 and 2 are the real caps.

A card is still required: Google needs a billing account even for the free cap. Where to add it:
`PLACES_API_KEYS` secret, and Rules `SOURCE` = `auto` (Places when a key exists, OSM otherwise).

## 6b. Optional APIs (v3.1): paste a key and it is used; leave it blank and the bot runs exactly as before

Each key can be a GitHub Secret (same name) or pasted in the sheet's **Options** tab (`Your key` column). Every
helper has a per-run cap in **Rules** and switches itself off on errors/out-of-credit (no crash, no retry storm).

| Key | Free tier (checked 2026-10/11) | What the bot does with it | Rules caps (per job) |
|---|---|---|---|
| `SERPER_API_KEY` | 2,500 free queries on sign-up, no card (paid credits are cheap) | **Best value.** (1) Google rating + review count for free-map leads, so the size filters and score work like Google Places. (2) Finds the website of businesses the map lists without one (35% of them). (3) Owner names from LinkedIn result titles ("Jane Smith - Owner - Company"). (4) Optional discovery: `SOURCE=serper` | `MAX_SERPER_PLACES_PER_RUN` 25, `MAX_WEB_SEARCH_PER_RUN` 25, `MAX_LINKEDIN_SEARCH_PER_RUN` 15, `SERPER_MAPS_SEARCHES_PER_RUN` 30 |
| `BRAVE_API_KEY` | monthly free credit (Brave states $5-$20 of calls; ~1,000+ searches), card asked to prevent abuse | backup web search for (2) and (3) when Serper is missing or used up | same caps |
| `ZENROWS_API_KEY` | 5,000 credits/month, no card (JavaScript page = 5 credits) | reads home pages that block normal readers or need JavaScript; robots.txt still respected | `MAX_ZENROWS_PER_RUN` 30 |
| `APIFY_API_TOKEN` | $5 credit/month, no card | Instagram stats (as before) and, with `USE_APIFY_MAPS=Yes`, a few Google Maps searches per run (~$1.50 per 1,000 places) | `APIFY_MAPS_SEARCHES_PER_RUN` 2 × 40 places |
| `APOLLO_API_KEY` | free plan, limited API | company size / employee count (as before) | `MAX_APOLLO_PER_RUN` |
| `HUNTER_API_KEY` | 25 searches + 50 verifications / month | names + personal emails by domain, email finder, verification (as before) | `MAX_HUNTER_*` |
| `ZEROBOUNCE_API_KEY` | 100 verifications / month | bounce-proof email check (as before) | `MAX_VERIFY_PER_RUN` |
| `ABN_LOOKUP_GUID` (AU) | free, register at abr.business.gov.au/Tools/WebServices | official ABN facts (see AU columns); ABN by exact name + state when the site shows none | `MAX_ABN_PER_RUN` 300 |

**Watch the Serper budget:** caps are per job, and the default workflow runs ~8 map jobs a day. 65 queries × 8 ≈
500/day, so the 2,500 free queries last about 5 days, then paid credits (about US$1 per 1,000 at the entry pack, check
serper.dev). Lower the caps in Rules if you want it to last longer.

Facts-only rules still hold: a website from search is kept only if its domain contains a distinctive word of the
business name (never a directory); a Google rating only if the Google listing has the same name or website; a LinkedIn
owner only if name + decision role + company word are in the same result title; an ABN only if printed next to "ABN"
and checksum-valid, or an exact registered-name match in the same state.

## 6c. "If Google Places = 10/10, what are we without it?"

Measured + estimated, for the free setup (OpenStreetMap + website reading), Places = 10:

| Part of lead quality | Free (no Google) | Why |
|---|---|---|
| Contact facts (emails, owner name, socials, phone) | **10/10** | identical: both read the business's own website |
| Picking the right-size business (not tiny, not a big brand) | **6/10** | no review count, so the bot cannot drop 3-review newcomers or 2,000-review chains; it scores them neutral |
| Business still open | **7/10** | OSM can be stale; a working website catches most closures |
| Coverage (how many businesses are found at all) | **~5/10** (estimate) | OSM is volunteer-mapped; Google lists far more, and 35% of OSM businesses have no website on record |
| **Quality of each lead that passes 7/10** | **~8/10** | contact data is the same; size/fit filtering is weaker |
| **Overall (quality × how many you get)** | **~7/10** | same niches/areas give ~50-60% of the leads Places would |

With **SERPER_API_KEY** (Google rating + reviews + website finder) the size filter and coverage gap mostly close:
**~9/10 per lead**, and ~+20-30% more leads from the recovered "no website" businesses. In Australia, **ABN_LOOKUP_GUID**
adds the business age as a second "established" signal (~8.5/10 without Serper). `SOURCE=serper` (Google Maps results
as the discovery source) is ~9.5/10, limited only by the query budget. Coverage numbers are estimates: they could not be
measured against Google without a key.

## 7. Bugs fixed in this pass (code had never run before)

First real execution (Python 3.12.10, gspread 6.2.1): the v2 selftest passed. Bugs found by runtime + static review:

1. **Wrong text encoding.** Pages without a charset header were decoded as ISO-8859-1 (requests default), so
   "Seán Ó Brien" became mojibake and the name was lost. Now uses the page's meta charset, else UTF-8. *(test)*
2. **JSON-LD founders dropped.** Founders inside `@graph` or in a `founder` list were ignored (`_rel` was never
   set). Fixed. *(test)*
3. **Dry run wrote to the sheet** (a Run Log row and geocoded coordinates). It now writes nothing. *(test)*
4. **New default Locations never reached an existing sheet** (seeded only when the tab was empty), so worldwide
   metros would never appear. They are now added once, matched by Search Area. *(test via local run)*
5. **Seed rows were appended by column position**, so a user who moved or added a column got shifted rows. Rows are
   now written by header name. *(test)*
6. **Chain-name blocklist matched inside words**: "my dentist" blocked "Tammy Dentistry". Now whole words plus
   plural/possessive ("mcdonald" still hits "McDonald's"). *(test)*
7. **OSM outage burned the run**: every later niche retried 3 servers × 75 s. Map searches now stop after
   `OSM_FAIL_STOP` failures in a row.
8. **Parallel/duplicate work**: several places sharing one website were downloaded twice in the same batch; two
   jobs creating the same niche tab crashed with "already exists". Both fixed.
9. **Hard-coded Australia** in 9 places (country reject, address fallback, Leads Input, OSM addresses, Nominatim
   `countrycodes=au`, Places `regionCode`, YouTube `regionCode` + AU-word filter, AI prompt, timezone, pitch label).
   All now come from the Locations row / Rules. *(tests)*
10. **v2 tabs not touched in a run would fall out of All Leads** after the column change. All lead tabs are now
    migrated before All Leads is rebuilt. *(test)*
11. **YouTube "website" was sometimes a Typeform/Google Form link.** Form and payment hosts are skipped.
12. **Free map searches barely worked.** Live test: 4 of 5 `around:` queries timed out on all 3 public Overpass
    servers (~4 minutes lost per search). Now bounding-box queries (~30-40 s), retry the main server after a fast
    502, mirrors as backup. *(test)*
13. **AI calls could get Cloudflare 403 "1010"** (Groq blocks default library User-Agents). The bot now sends its own User-Agent.
14. **Sorting covered only the bot's columns.** A column you added to the right of `Place Id` would not move with its
    row. The sort now covers every column.
