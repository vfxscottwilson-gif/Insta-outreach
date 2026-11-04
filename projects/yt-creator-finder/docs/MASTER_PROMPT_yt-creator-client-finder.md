# yt-creator-client-finder: Diagnosis + Master Build Prompt

Date: 2026-11-01. Part A lists what is wrong in the two Gemini-written prompts. Part B is the single fixed prompt to paste into Claude Pro/Max (or to have Claude build here).

---

## PART A: Diagnosis (bugs, dead tools, logic holes)

### A1. Dead or unusable tools (removed from the build)

| Item in old prompts | Status (Nov 2026) | Replacement |
|---|---|---|
| Upwork RSS feeds (`upwork_buyers.py`) | Retired Aug 2024. Upwork's GraphQL API needs an approved app and forbids lead harvesting. | Delete the module. Use public hiring posts instead (B4). |
| Fiverr "Buyer Requests" (`fiverr_buyers.py`) | Removed; replaced by "Briefs", which are login-only and not scrapable. | Delete the module. |
| Google Programmable Search JSON API ("search the entire web") | Closed to new customers. Shuts down **1 Jan 2027**. | Do not build on it. Use YouTube Data API search plus DuckDuckGo HTML as a best-effort fallback. |
| `site:twitter.com` / X searches | X is login-walled. Jina and search engines return almost nothing useful. | Store an X link only when the creator lists it on their channel or website. |
| `site:linkedin.com/in "hiring video editor"` | `/in/` pages are **personal profiles, mostly editors looking for work**. That is the opposite of the ICP. | Drop it. If you keep LinkedIn, only use `linkedin.com/posts` with the "we're hiring" wording, and treat it as low-yield. |
| Scraping the YouTube "View email address" button | Behind a CAPTCHA. Bypassing it breaks YouTube's ToS. | Pull emails only from the channel description, video descriptions, linked websites and link-in-bio pages. |
| OpenStreetMap (old prompt 2) | Leftover from a Google-Maps bot. It adds nothing for YouTubers. | Delete. |
| SMTP email "verification" | GitHub runners block outbound port 25. | "Verified" = valid syntax + domain has MX records + not a disposable domain. Name the column accordingly. |

### A2. Logic bugs (the bot would return zero leads or wrong ones)

1. **The AND filter returns almost nothing.** Prompt 2 requires a hiring post within 14 days, a budget of at least $1,000, 15k+ subscribers, a Tier-1 country and an upload in the last 21 days, all at once. Creators almost never publish a budget. Fix: make subscribers, recency and channel ownership **hard gates**. Make hiring signal, budget and country **score points** that set PRIME / GROWING / REVIEW.
2. **Country is usually blank.** YouTube's `snippet.country` is optional, and most channels leave it empty. Hard-rejecting blanks throws away good leads. Fix: infer the country from email TLD, phone prefix, website TLD and description text. If it still can't be inferred, keep the lead as REVIEW.
3. **Deduplication with "a local set" fails on GitHub Actions.** Runners are wiped after every run, so the set is always empty. Fix: at the start of each run, read every Channel_ID and email from all lead tabs plus Blacklist.
4. **RSS cannot give subscriber counts.** The channel RSS feed gives the 15 latest videos with views and dates, but no subscribers. Fix: use YouTube Data API `channels.list` (1 unit per call, up to 50 IDs per call). The RSS feed covers recency and average views for free.
5. **`search.list` costs 100 units.** The daily quota of 10,000 allows only about 100 searches. Old prompts didn't budget for this, so the quota runs out mid-run and every later call returns 403. Fix: track a per-run quota budget (B6).
6. **Hard-coded AI model names crash the run.** This is exactly the "agent name not available" bug you described. Names like `gemini-pro`, `gemini-1.5-flash` and `llama3-70b-8192` have already been retired and now return 404. Fix: read model lists from env vars, try each one in order, treat 404/400 "model not found" as "skip to the next model" (never crash), and fall back to the template generator last.
7. **The 429 path isn't the only failure.** The AI can also return 500/503, time out, hit a safety block (empty text) or return broken JSON. All of these must route to the next provider.
8. **Schema conflicts.** Prompt 1 has 20 columns and prompt 2 has 23. `Place_ID` is a Google-Maps leftover. There is no Channel_ID column to dedup on, and no signal URL or signal date to prove intent. Fixed in B5.
9. **The "Blacklist & Run Log" tab mixes two tables.** Appending to one corrupts the other. Split it into two tabs.
10. **Routing between editing and thumbnails is undefined.** Fix: route by keyword. If the signal covers both, put the lead in Video Editing and add "+thumbnails" to Sourcing_Signal. Never write the same lead to both tabs.
11. **Sheets write limits.** Appending row by row hits the 60 writes/min quota. Fix: use one batched `append_rows` per tab per run, with retry/backoff on 429.
12. **Days_Since_Last_Upload goes stale.** Store `Last_Upload_Date`, and let a sheet formula compute the days.

### A3. Scheduling bugs (your "credits reset at 8 a.m." problem)

- **GitHub cron uses UTC, not PKT.** PKT = UTC+5, so 6:00 AM PKT = `0 1 * * *`. Scheduled runs also start 5 to 30+ minutes late, and runs at minute :00 get dropped most often. Use an odd minute such as `17 1 * * *`.
- **One job can't "run all day".** The hard limit is 6 hours per job, and a long job burns free minutes on private repos.
- **Quotas don't reset at 6 AM PKT.** YouTube Data API and Gemini both reset at **midnight Pacific**, which is **12:00 PKT (PDT) / 13:00 PKT (PST)**. A 6 AM run that uses up the quota leaves nothing until noon PKT. Your intuition was right.
- **The fix is a quota-aware loop of short runs.** Run every 3 hours from 06:17 to 21:17 PKT (6 runs). Each run:
  1. reads today's counters from a hidden `_State` tab (leads written today, YT units used since the last Pacific midnight, AI calls per provider),
  2. **exits in seconds** if today's lead target is met,
  3. skips any provider whose quota is spent, and resumes it automatically after its own reset,
  4. stops itself at 40 minutes (`timeout-minutes: 45`).
  The 06:17 run uses what's left, the 12:17/15:17 runs get the fresh Pacific-midnight quota, and the day finishes when the target is hit.
- **GitHub disables cron after 60 days without commits** (public repos). Add a monthly keep-alive commit step, or use the `gautamkrishnar/keepalive-workflow` action.
- **Add `concurrency:`** so two runs never write at the same time.

### A4. Compliance (protects your Gmail domain and reputation)
Collect only business contact details the creator published publicly. Record the source URL for each email. Honour a `Blacklist` tab. Outreach must include an opt-out line (CAN-SPAM; GDPR/PECR for UK and IE). Scraping must respect robots.txt and rate limits.

### A5. Reuse before building
You already have `YT-Leads Automation File.zip` (leadgen/: yt.py, enrich.py, ai.py, score.py, leadbot.py). The worldwide lead bot also fills a YouTube sheet, and `Scraper Tools/` has scrapetube and yt-dlp. Part B tells the builder to extract that zip and reuse its working parts, so it doesn't start from zero.

---

## PART B: MASTER PROMPT (copy everything below this line)

```
ROLE
You are a principal Python automation architect and a 10-year B2B outreach specialist who has closed
$1k-$5k/month retainers with YouTube creators for a video-editing and thumbnail-design agency. You think
like a closer: a lead is only worth writing to the sheet if a busy agency owner could email it today
with a specific, relevant pitch. You also write code that never crashes on bad data.

GOAL
Build `yt-creator-client-finder`: a zero-cost Python bot on GitHub Actions that finds YouTube CHANNEL
OWNERS (creators and brands, never freelancers or job seekers) who need a video editor or
thumbnail designer, enriches them with public contacts, scores them, writes AI insight and a pitch
angle, and appends them to Google Sheets without duplicates.

BEFORE YOU WRITE CODE
1. If `YT-Leads Automation File.zip` is provided, extract it into a new folder and reuse its working
   parts (yt.py, enrich.py, ai.py, score.py). List what you reuse and what you replace.
2. Show me the file plan and the list of secrets. Wait for my OK. Then build.
3. Ask every question at once, up front. After that, don't interrupt unless truly blocked.

HARD BANS (do not use, do not mention as a fallback)
- Upwork RSS (retired), Fiverr Buyer Requests/Briefs (removed or login-only), the Google Custom Search
  JSON API (closed to new users, shuts down 2027-01-01), Playwright/Selenium/headless browsers, paid
  proxies, paid scraping APIs, CAPTCHA bypass, the YouTube "View email address" button, SMTP probing,
  OpenStreetMap.
- Never hard-code any key, sheet ID, model name, threshold or keyword list. Everything comes from
  env vars or config.yaml, with safe defaults in code.

ALLOWED FREE SOURCES
- YouTube Data API v3 (free 10,000 units/day): channels.list (1 unit, batch 50 IDs),
  videos.list (1 unit, batch 50), playlistItems.list (1 unit), search.list (100 units, use sparingly).
- YouTube channel RSS: https://www.youtube.com/feeds/videos.xml?channel_id=UC... (no quota; latest 15
  videos, dates, views). Retry 3x, because it intermittently returns 404/5xx.
- Jina Reader: https://r.jina.ai/<url> (works without a key; with the free JINA_API_KEY send
  "Authorization: Bearer"). Use it for creator websites and link-in-bio pages (linktr.ee, beacons.ai,
  stan.store, carrd).
- DuckDuckGo HTML (https://html.duckduckgo.com/html/) is BEST-EFFORT ONLY. It often blocks GitHub
  IPs. On a 202/403/empty response, mark the source DOWN for this run and move on.
- Public hiring boards readable via Jina, if their robots.txt allows: ytjobs.co listings (creators
  hiring editors and thumbnail designers). Check robots.txt at runtime and skip if disallowed.
- Gemini API (free key from aistudio.google.com), Groq API (free key from console.groq.com).
- dnspython for MX checks. gspread + google-auth (service account) for Sheets.

DISCOVERY STRATEGY (rank sources by intent strength)
S1 Hiring posts (strongest): ytjobs.co listings and DuckDuckGo queries such as
   "hiring video editor" "youtube channel", "looking for a thumbnail designer" youtube,
   "[HIRING]" "video editor" youtube. Resolve each post to a YouTube channel ID (from links in the
   post, or by searching the creator name).
S2 In-channel hiring signals: YouTube search.list (type=video, order=date, publishedAfter=now-21d,
   relevanceLanguage=en, regionCode cycling US/GB/CA/AU/NZ/IE) for queries in config.yaml such as
   "hiring editor", "looking for editor", "join my team editor", "thumbnail designer wanted". Then
   fetch descriptions and confirm the hiring phrase with regex.
S3 Growth-gap channels (no explicit hiring post, so the lead is scored lower): niche keyword searches
   (finance, fitness, business, tech, podcasts, real estate, coaching) from config.yaml. These are
   channels with 15k+ subscribers, regular uploads, and weak thumbnails or edits (judged by the AI
   step, from titles and view consistency).
Spend at most YT_SEARCH_BUDGET search calls per run (default 15 = 1,500 units). Rotate queries
across runs (store the cursor in _State) so each run covers new ground.

QUALIFICATION
Hard gates (fail any one -> skip, but log the reason):
  - The channel is an owner/brand, not a freelancer. Reject if the title or description matches the
    freelancer regex: "i edit", "editor for hire", "my portfolio", "hire me", "freelance editor",
    "available for work", "dm me for edits".
  - subscriberCount >= MIN_SUBS (default 15000). If hiddenSubscriberCount=true, send the lead to REVIEW.
  - The last upload was within MAX_DAYS_SINCE_UPLOAD (default 21) days.
  - Not in Blacklist, and not already in the sheet (Channel_ID or any email).
Score (0-10) -> segment:
  +3 explicit hiring signal dated within 14 days (+1 more if the signal is older but still within 30 days)
  +2 country in TIER1 (US, GB, CA, AU, NZ, IE), declared or inferred
  +1 budget stated >= $1,000/month, OR 100k+ subscribers (a proxy for ability to pay)
  +1 avg views of the last 5 videos >= 20% of subscribers
  +1 has a public business email
  +1 uploads >= 4 per month
  +1 has a website or brand (sells a product, course or service)
  PRIME >= 7, GROWING 5-6, REVIEW 3-4, below 3 -> not written (counted in Run Log).
Country inference order: snippet.country -> email/website ccTLD -> phone prefix -> description
mentions (city/state names) -> "Unknown". Unknown never hard-rejects.

ENRICHMENT
- Emails: regex over the channel description, the last 5 video descriptions, the website (home
  plus /contact /about via Jina) and link-in-bio pages. De-obfuscate "name [at] domain [dot] com".
  Classify: Generic (info@, hello@, contact@, support@, team@, business@, collabs@, partnerships@), or
  Personal (firstname@, or matches the creator name). Primary = Personal if present, else Generic.
  Agency/management emails (domain matches a known talent-agency list, or contains "mgmt"/"talent")
  go to the notes as "Managed by agency". These are still valid leads.
- Email_Check: "MX_OK" / "NO_MX" / "DISPOSABLE" / "SYNTAX_BAD". Never claim SMTP verification.
- Socials: Instagram, LinkedIn, X/Twitter, Facebook, TikTok, taken from channel links and the
  website. Normalise the URLs.
- Phone/WhatsApp: only if published (wa.me links, tel:, "+1 ..."). Store in E.164 format.

AI INSIGHT (ai_insight.py)
Input: channel name, niche, last 10 titles, avg views, view variance, upload cadence, hiring text.
Output JSON: {"insight": "<=280 chars: content style, a visible editing/thumbnail gap, a pain point",
              "pitch_angle": "<=200 chars, a specific offer tied to that gap"}
Rules: use only the facts given. Never invent names, numbers or claims. Validate the JSON shape with
pydantic. On any invalid output, move to the next model.
Provider chain, built from env vars:
  GEMINI_API_KEYS  (comma-separated, rotate)   GEMINI_MODELS (comma list, default from config)
  GROQ_API_KEYS    (comma-separated, rotate)   GROQ_MODELS   (comma list, default from config)
At startup, call each provider's list-models endpoint, then keep only the configured models that
actually exist. If none exist, use the first available "flash"/"instant"-class model the endpoint
returns. If that also fails, disable the provider for this run and log it.
Per call: timeout 30s. On 429: mark the key COOLDOWN until the provider's reset and try the next
key/model. On 404/400 model errors: drop the model for this run. On 5xx/timeout: one retry, then
move on. On a safety block or empty/bad JSON: move to the next model.
Final fallback: a deterministic template generator built from the measured facts. Example: "Posts
{cadence}/mo in {niche}; views swing {variance}% between uploads, so packaging (thumbnails/titles) is
inconsistent." Fill the pitch from a niche->offer map. The run NEVER stops on an AI error.
Pace calls (default 4s apart) to stay under free RPM limits.

SHEETS (sheets_manager.py)
Tabs, created if missing and never wiped:
  1 Master Dashboard: KPI cards built from FORMULAS (COUNTA/COUNTIF over the lead tabs), so they never
    drift: Total Leads, PRIME, GROWING, REVIEW, % with MX_OK email, leads today, last 14 runs
    (from Run Log), provider health (last status per provider from _State).
  2 YouTube_Video_Editing_Leads
  3 YouTube_Thumbnail_Design_Leads
  4 Blacklist: Channel_ID | Email | Domain | Reason | Added_At (rows I add by hand are respected)
  5 Run Log: Run_ID | Started_PKT | Ended_PKT | Source | Level | Channel_ID | Message
  6 _State (hidden): key | value. Holds the daily counters, quota usage, query cursor and provider cooldowns.
Lead tab columns (exact order):
  1 Lead_ID (= YouTube Channel_ID, UC...)   2 Quality_Segment   3 Score   4 Creator_Name
  5 Channel_URL   6 Handle   7 Subscriber_Count   8 Last_Upload_Date
  9 Days_Since_Last_Upload (sheet formula: =TODAY()-H{row})   10 Uploads_Last_30d
  11 Avg_Views_Last_5   12 Primary_Email   13 Personal_Email   14 Generic_Email   15 Email_Check
  16 Email_Source_URL   17 Phone_WhatsApp   18 Country   19 Country_Source (declared/inferred/unknown)
  20 State_City   21 Sourcing_Signal (Hiring post / In-video hiring / Growth gap [+thumbnails])
  22 Signal_URL   23 Signal_Date   24 Budget_Mentioned   25 Website   26 Instagram_URL
  27 LinkedIn_URL   28 Twitter_X_URL   29 Facebook_URL   30 AI_Lead_Insight
  31 Recommended_Pitch_Angle   32 AI_Source (gemini:model / groq:model / template)
  33 Status (default "New", data-validation dropdown: New/Contacted/Replied/Call/Won/Lost/Do-Not-Contact)
  34 My_Notes   35 Found_At_PKT
Header formatting: frozen header row, bold, filter enabled, conditional colour on Quality_Segment.
Writes: one batched append_rows per tab per run, with exponential backoff on 429/5xx (5 tries).
Sheet cells must not start with "=", "+", "-" or "@" unless they are intended formulas (prevents
formula injection from scraped text).
Dedup: at run start, load every Lead_ID plus all emails from both lead tabs and Blacklist into sets.
Check each lead before enrichment (saves quota) and again before writing.

SCHEDULE AND QUOTA CONTROL (all times in PKT = UTC+5; GitHub cron is UTC)
.github/workflows/run-lead-bot.yml:
  on: schedule: cron "17 1,4,7,10,13,16 * * *"  (06:17, 09:17, 12:17, 15:17, 18:17, 21:17 PKT)
      workflow_dispatch: inputs dry_run (bool), max_leads (int)
  concurrency: group lead-bot, cancel-in-progress: false
  timeout-minutes: 45; Python 3.12; pip cache; `python -m src.leadbot`
  A step that always uploads leadbot.log as an artifact.
  A keep-alive step that prevents the 60-day cron auto-disable.
Each run:
  - Compute "quota day" per provider: YouTube and Gemini reset at 00:00 America/Los_Angeles (use
    zoneinfo, which handles DST automatically). Groq limits roll, so track its cooldown timestamps.
  - Read _State. If leads_written_today(PKT date) >= DAILY_LEAD_TARGET (default 25), log
    "target met" and exit 0 within seconds.
  - Hold back YT_UNITS_RESERVE (default 1500) so a later run always has quota for channels.list on
    hiring-post leads.
  - Self-stop at RUN_MAX_MINUTES (default 40). Flush pending rows before exiting.
  - Exit code is ALWAYS 0 unless config/secrets are missing (then exit 1 with a clear message naming
    the missing env var, never its value).

ERROR ISOLATION
- One `safe_call(fn, *args, source=..., channel_id=...)` wrapper is used for every network call and
  parser. It catches Exception, logs a row to Run Log, and returns None. Each lead is processed
  inside its own try/except.
- requests.Session with retries (urllib3 Retry: 3 tries, backoff 1.5, on 429/500/502/503/504), a
  timeout of 20s on every request, and a realistic User-Agent. Per-domain polite delay of 1-2s.
- Circuit breaker: if a source fails 5 times in a row, mark it DOWN for this run and skip it.
- If Sheets is unreachable, write leads to `pending_leads.json`, upload it as an artifact, and have
  the next run append it first.
- Never print secrets. Mask them in logs.

FILES TO GENERATE
.github/workflows/run-lead-bot.yml
config.yaml                    (thresholds, keywords, niches, query lists, model defaults, regexes)
.env.example                   (every variable, with comments, no real values)
requirements.txt               (pinned: gspread, google-auth, requests, beautifulsoup4, lxml,
                                feedparser, pydantic, pyyaml, dnspython, tenacity)
src/__init__.py
src/leadbot.py                 (orchestration, run budget, exit logic)
src/config.py                  (load env + yaml, validate, defaults)
src/state.py                   (_State tab, quota days, cooldowns, daily counters)
src/http.py                    (session, retries, safe_call, circuit breaker)
src/sources/hiring_posts.py    (ytjobs via Jina, DuckDuckGo best-effort)
src/sources/youtube_search.py  (search.list with budget, query rotation)
src/enrichment/youtube.py      (channels.list, videos.list, RSS, freelancer filter)
src/enrichment/contacts.py     (Jina crawl, email/social/phone extraction, MX check)
src/enrichment/country.py      (inference chain)
src/scoring.py                 (gates, score, segment, tab routing)
src/ai_insight.py              (model discovery, failover, template fallback)
src/sheets_manager.py          (tabs, headers, formatting, dashboard formulas, dedup, batch writes)
tests/test_scoring.py, tests/test_contacts.py, tests/test_ai_fallback.py (no network; mocks)
README.md and CLAUDE.md        (setup in numbered steps, secrets table, how to run locally,
                                how to dry-run, current status)

SECRETS (GitHub -> Settings -> Secrets and variables -> Actions)
  GOOGLE_SA            full service-account JSON (raw JSON or base64; detect which automatically)
  SHEET_ID             the ID from the sheet URL; share the sheet with the SA email as Editor
  YOUTUBE_API_KEYS     comma-separated (one per Google Cloud project; rotate when one gets 403 quotaExceeded)
  GEMINI_API_KEYS      comma-separated
  GROQ_API_KEYS        comma-separated
  JINA_API_KEY         optional
Variables (non-secret): DAILY_LEAD_TARGET, MIN_SUBS, MAX_DAYS_SINCE_UPLOAD, YT_SEARCH_BUDGET,
  YT_UNITS_RESERVE, RUN_MAX_MINUTES, GEMINI_MODELS, GROQ_MODELS, TIER1_COUNTRIES, DRY_RUN.
Any optional key that is missing disables only that feature, with a Run Log warning. It never crashes.

ACCEPTANCE (prove each one; never just say "done")
1. `pytest` passes offline.
2. `DRY_RUN=1 MAX_LEADS=10 python -m src.leadbot` prints 10 scored leads as a table and writes nothing.
3. PILOT: one real run limited to 10 leads. Show me the sheet rows. I approve before the full schedule.
4. Kill-switch tests: with an invalid Gemini model name, an invalid Groq key, and no Jina key, the run
   still finishes with exit 0 and AI_Source shows the fallback that was used.
5. Re-running immediately adds 0 duplicate rows.
6. Run Log shows one summary row per run: found / gated-out (by reason) / written / quota used.
```

---

## PART C: Tools you need (all free, no card)

| Tool | Get it at | Why |
|---|---|---|
| GitHub account (private repo) | github.com | Runs the schedule. Free tier includes 2,000 Actions min/mo for private repos; this bot uses about 600. |
| Google Cloud project + YouTube Data API v3 + Sheets API + Drive API | console.cloud.google.com | Subscriber counts and channel data; sheet writing |
| Service account JSON key | Cloud console → IAM → Service accounts | `GOOGLE_SA` |
| Gemini API key | aistudio.google.com | AI insight (primary) |
| Groq API key | console.groq.com | AI insight (secondary) |
| Jina Reader key (optional) | jina.ai | Higher reading limits |
