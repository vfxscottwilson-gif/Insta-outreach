# Lead Bot v5: append-only sheets, Lead Insight, per-country dashboards, one secret per key

Applies to **both editions**: worldwide (this repo) and Australia-only (`au-only-lead-bot`; same code, only
`src/market.py` = AU). The outreach-bot interface is in `CONTRACT.md` (also at
`D:\All Automations Records\Lead generation\CONTRACT.md`).

**Tests:**
- `python src/selftest.py`: 60 checks, passing in both `LEAD_MARKET=WORLD` and `LEAD_MARKET=AU`.
- `python -m unittest discover -s tests`: 100 tests, network mocked; 21 are new in `tests/test_v5.py` and 8 in `tests/test_free_tools.py`.
- A live free-sources run (section 6).

## 1. What changed for you

| Before (v4) | v5 |
|---|---|
| AI wrote `Case Study` + `Email Subject` + `Email Draft` | **One column, `Lead Insight`**: 3-4 short lines on who they are and their likely pains. **No email drafts.** One small AI call per **qualified** lead; no key, a 429 or an error gives a fact-only summary |
| On a 429 the AI client waited 20 s, then 40 s, and retried | **A 429 switches that key off for the run.** The next key is tried at once. When all keys are off, AI stops for the rest of the run and the rows say `insight: fact-only (AI quota hit)` |
| 7 sheets | **Up to 10:** US, CA, GB, AU, NZ, IE + optional **AE, SA, QA**, + YouTube. AU-only edition: its own `SHEET_ID_AU_ONLY` |
| `finish` sorted every tab and rebuilt `All Leads` + `Dashboard` | **Append-only:** new rows go below the last used row. Nothing is sorted, inserted, rebuilt or rewritten, including `Status`, `My Notes` and your own columns |
| Duplicates were checked against the Seen tab only | Also deduped by **Place Id across every lead tab of that sheet**, re-checked right before each write |
| Dashboard: formulas re-reading every tab | **US sheet:** tab 1 **Master Dashboard** (all sheets) and tab 2 **US Stats**. **Every other sheet:** tab 1 **Stats**. Values overwrite in place, from a hidden **Meta** tab plus the rows written this run (no full re-reads) |
| `AI_API_KEYS` with several keys in one secret | **One secret per key** (`GEMINI_API_KEY_1/2/3`, `GROQ_API_KEY`, `GOOGLE_PLACES_API_KEY`, `YOUTUBE_API_KEY_1/2`, `ABN_GUID`, …). Values are trimmed and shape-checked, and the startup **registration report** is masked to the last 4 characters. Old combined names still work. See `SECRETS_GUIDE.md` |

## 2. Files changed

| File | Change |
|---|---|
| `src/keys.py` | **new.** Secrets registry: trim spaces/quotes, cut a sheet id out of a URL, shape check per key, masked report (`registered: X (...abcd)` / `ignored: X (reason)`). Builds the legacy combined names from the single keys. `KEY_CHECK=warn` keeps a key whose format changed |
| `src/insight.py` | **new** (replaces `drafts.py`). Lead Insight: AI (one call, 220 tokens, plus a verbatim-checked decision maker) or a fact-only summary; `QuotaHit` sets the quota flag |
| `src/drafts.py` | **deleted** (outreach bot's job) |
| `src/ai.py` | One pass over the keys, no sleeping. 401/402/403/429 switch a key off for the run; `QuotaHit` when all are off. Cerebras (`csk-`) added |
| `src/leadbot.py` | **Reads:** 1 metadata read + 1 batched read of all control tabs; tab cache tied to one sheet. **Writes:** `write_leads` appends at an explicit range below the last used row (a retried write can't double-append), re-reads the header and watched columns first (handles moved, added or deleted columns and rows typed by hand), dedupes by Place Id, recreates a deleted tab, stops near 10M cells. **Bookkeeping:** Seen/Searches/Snapshots read and written by header name. **Stats:** Stats, Meta, Master Dashboard. **Lock:** a Meta lock keeps a second run off the same sheet. `finish` no longer sorts or rebuilds. AI is called only after the ICP gate (qualified leads only). Retry: 7 tries with 10-90 s backoff plus jitter on 429/5xx. Clear error when a sheet isn't shared |
| `src/defaults.py` | New `LEAD_H` (no Case Study / Email columns, adds `Lead Insight`); `OLD_LEAD_COLS`; Saudi Arabia + Qatar (countries, currencies, 5 seed areas); `SHEET_TARGETS` 10 (AU edition: `["AU"]`); new Rules `USE_AI_INSIGHT`, `MAX_AI_INSIGHTS_PER_RUN` (60), `CELL_LIMIT_STOP`; `SORT_TABS` ignored; Options rows for single-key secrets and the research tools |
| `src/enrich.py` | WhatsApp click-to-chat numbers (`wa.me/…`, `api.whatsapp.com/send?phone=…`) now count as phones (high yield in the Gulf) |
| `src/quality.py` | Review factors for SA / QA |
| `src/localsheet.py` | `values_batch_get`, `add_rows`, hidden tabs (test stand-in for the new Sheets calls) |
| `src/selftest.py` | Lead Insight, the AI 429 stop, the secrets registry, no draft columns, Gulf targets, AU-only sheet id |
| `tests/test_v5.py` | **new**, 21 tests (section 4) |
| `tests/test_v3.py`, `tests/test_v4.py` | Updated for append-only, Stats, Lead Insight; fake test ids use `KEY_CHECK=warn` |
| `.github/workflows/run-lead-bot.yml` | **Jobs:** 10 collect jobs (5 at a time, 20 s stagger). **Secrets:** every single-key secret, plus the old ones as fallback. **Finish:** builds Stats plus the Master Dashboard |
| `SECRETS_GUIDE.md` | **new.** Each secret: Secret or Variable, required or not, a fake format example, where to get it, the free limit, what it unlocks |
| `SHEETS_SETUP.md`, `00_START_HERE_SETUP_GUIDE.md`, `README.md` | Rewritten for v5 |
| AU-only edition | The same `src/` and `tests/`. **Workflow:** v5 secrets, `SHEET_ID_AU_ONLY`, collect jobs **one at a time** (one shared sheet). Updated `AU_EDITION.md` and START_HERE |

## 3. Free tools (from `FREE_TOOLS_RESEARCH.md`)

- **Wired in:**
  - WhatsApp phone links.
  - Cerebras as an AI fallback.
  - Single-key Gemini ×3 / Groq / OpenRouter / Mistral.
- **Already present:** Cloudflare email decode, contact/about/team/privacy pages, link-in-bio pages, JSON-LD
  founders, pixel and booking detection, "website by" agency credits.
- **v5.1, wired in as optional modules** (`src/optional.py`; tested in `tests/test_free_tools.py`). All of them:
  no key = no request; an odd reply = nothing used; 429/401/403 = off for the run; per-run caps in Rules. Free
  limits are shown as "check vendor page", because the research could not verify them.
  - **Link-in-bio, own site:** a creator's linktr.ee / beacons.ai / stan.store page is read, and their OWN website is
    followed (with its contact pages). The site is used only when its domain contains a word of the channel name.
  - **Disify** (no key): disposable / no-DNS email check. Off by default (Rules `USE_DISIFY`).
  - **Reacher** (`REACHER_URL`, optional `REACHER_SECRET`): self-hosted SMTP check on your own VPS. GitHub runners
    block port 25, so the free MX check stays the default there.
  - **NZBN register** (`NZBN_API_KEY`), New Zealand leads only, exact registered-name match only:
    - a director becomes the decision maker when the site names nobody;
    - a registry email is used only when it is on the business's own domain;
    - the phone is used only when none was found;
    - removed or closed companies are skipped.
  - **Prospeo** (`PROSPEO_API_KEY`), then **Snov.io** (`SNOV_CLIENT_ID` + `SNOV_CLIENT_SECRET`): the personal email of
    a known decision maker.
    - Called **only for leads that already passed the 7/10 gate** and have no personal email.
    - The address must be on their own domain, and it is dropped if verification says invalid.
  - The API field names for NZBN / Snov.io / Prospeo come from memory, not tested against the live services. The
    code reads replies defensively: it takes any email on the right domain at any depth, and a director from any
    `rolePerson`. If a vendor's format differs, the module simply finds nothing; it never crashes.
- **Listed in the Options tab, not wired:** Tomba.
- **Skipped as the research advises:** Bing (retired), Google CSE (closing), Instagram/Facebook/LinkedIn scraping (ToS),
  SMTP verification (port 25 is blocked on GitHub runners).

## 4. Diagnose and harden: what was checked (and the tests)

| Risk | What the bot does now | Test |
|---|---|---|
| API format changes | AI reply not JSON / a list / a number → fact-only insight. Maps item missing fields → skipped or defaulted. Sheets batchGet with fewer ranges → empty lists. A key whose shape changed → `KEY_CHECK=warn` | `test_ai_reply_shape_changes_fall_back`, `test_maps_item_shape_change`, `test_batch_values_tolerates_missing_ranges`, `TestKeys` |
| Tab renamed or deleted by the user | The tab is recreated with the right headers (once, mid-run too). Lead tabs are found by header, not name | `test_deleted_tab_is_recreated`, `test_old_v2_tab_is_found_by_header_and_counted` |
| Columns re-ordered or added; key column deleted | Every read and write maps by header name. User-added columns count when finding the last row. A deleted `Place Id` / `Company Name` / `Lead Insight` header is re-added at the end | `test_appends_below_last_row_and_never_touches_existing`, `test_key_column_deleted_by_user_is_restored` |
| Empty sheet / wiped header | Headers are written, then the rows | `test_empty_sheet_scan` |
| 10M-cell limit | WARNING in Run health at 80%. At `CELL_LIMIT_STOP` (9.5M) no rows are added (ERROR in health), and those businesses stay eligible for later | `test_cell_limit_stops_writes` |
| GitHub Actions minutes and timeouts | Bot deadline 42 min < job timeout 60. Missing sheets skip in about 1 min. 10 jobs × about 45 min × 2 runs ≈ 900 min/day → **public repo** | – |
| Partial-run recovery | Per search: leads first, then Seen, then Searches. Writes are explicit-range, so retries are idempotent. The next run dedupes against the lead tabs and re-searches an unfinished search. The lock is released in `finally`; if a job is killed, it goes stale after 57 min | `test_retry_never_double_appends`, `test_lock` |
| Duplicate concurrent jobs on one sheet | Workflow `concurrency` group; worldwide = one job per sheet; AU-only = `max-parallel: 1`. A Meta lock makes a second run or a local run skip with a log line | `test_concurrent_jobs_are_locked_out` |
| Timezones | Dates in Rules › `TIMEZONE` (an invalid zone falls back to UTC). "Today" on the Master Dashboard is shown only for sheets whose Stats were written today | `test_timezone` |
| Unicode | Emoji and accents in names and tabs; control characters stripped; values capped below 50,000 characters per cell; console logs ASCII-only (masks use `...`) | `test_unicode_and_cell_limits` |
| Rate limits | **Sheets:** 7 tries with backoff + jitter, about 5 Sheets reads at job start (was about 40), 5 parallel jobs with a 20 s stagger. **AI:** no retry-spin. **Paid helpers:** keep their per-run caps and circuit breakers | `test_rate_limit_backoff`, `test_429_stops_without_spinning` |

## 5. Quota budget per job (Google Sheets, one service account)

| Phase | Reads | Writes |
|---|---|---|
| Start (metadata, all control tabs, Meta, lead-tab scan) | about 5-8 | 1-2 (Options status, lock) |
| Per search | 2 (header + watched columns of that tab, only when leads were found) | 3-4 (leads, Seen, Searches, Snapshots) |
| End | 1-2 | 3 (Run Log, Stats, Meta) |

**Total:** about 40-60 reads and 70-90 writes per 42-minute job. **Ten jobs at five at a time:** about 15 reads/min
and 20 writes/min at peak, against limits of 60 reads/min/user and 300 writes/min/project.

## 6. Live check (2026-11-01, free sources only, local sheet)

Same two Chicago searches as the v4 measurement (dentists, independent real estate):

| | v4 (2026-10-31) | v5 run 1 | v5 run 2 (same searches again) |
|---|---|---|---|
| Leads written | 15 | **14** (8 dentists, 6 real estate) | **0 new**: all 83 businesses already seen; the 14 rows unchanged, 14 unique Place Ids |
| Minutes | – | 3.6 | 1.6 |

Priority-field fill on the 14 run-1 leads:
- Company, Phone, Address, Website: 14/14.
- Any social: 12/14.
- Generic email: 8/14.
- Other emails: 7/14.
- Personal email: 5/14.
- Decision maker: 3/14.

Lead Insight was fact-only (no AI key in the test).

## 7. Remaining risks

1. **Free-tier limits change.** Gemini, Groq and similar tiers have changed often. If all keys hit 429, insights are
   fact-only for the rest of that run (by design).
2. **Decision-maker and personal-email coverage is low on free sources** (about 20-35%). The biggest upgrades are
   `SERPER_API_KEY` (LinkedIn owner titles), `HUNTER_API_KEY`, and an AI key (verbatim-checked name from the site).
3. **If a user types a row below the data with nothing in any watched column** (every bot column blank, and only a
   column the bot also writes), the next lead can land on it. In practice users fill Status/My Notes, which are
   watched.
4. **Shape checks can reject a valid key after a provider changes its format.** The report says "ignored: bad format".
   Set the Variable `KEY_CHECK=warn`.
5. **The Seen tab grows** by about 20-30k cells/day on a busy sheet: roughly a year to the 10M limit. Run health warns
   at 80%. Trim old `Rejected:` rows then.
6. **Gulf sheets** yield few leads on free OSM data. They need Serper/Apify, or a Google Places key.
7. **The Master Dashboard** depends on each sheet's Meta. A sheet whose job crashed before writing Meta shows its
   previous numbers (marked by its "Last run").
8. **The AU-only edition** now runs its 6 collect jobs one after another: up to about 4.5 h per run, and still well
   apart from the second daily run.
