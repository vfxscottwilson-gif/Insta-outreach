# AU Lead Bot v2: what changed, why, and how to install it

## 1. Files changed: copy these into your GitHub repo (same paths)

| File | Status | What changed |
|---|---|---|
| `src/leadbot.py` | rewritten | New column order, decision-maker flow, Personal/Generic/Other emails, ICP gate >= 7/10, parallel website reads, YouTube niches, Options tab, Dashboard (first tab), All Leads tab, Australia-timezone dates, old-tab migration |
| `src/enrich.py` | extended | Finds owner/founder/director names written on the site (team/about pages + structured data), phones from `tel:` links, ad/booking signals, splits emails into Personal and Generic |
| `src/optional.py` | extended | Keys can come from the Options tab. Hunter now returns people + positions. New Hunter email finder. Jina returns page text |
| `src/score.py` | rewritten | ICP score out of 10, tiers by ICP, suggested monthly pitch price, YouTube gap |
| `src/drafts.py` | rewritten | ONE AI call per lead returns Case Study + decision maker (checked word-for-word against the site) + email. Fallback to template + fact-only case notes |
| `src/yt.py` | **new** | YouTube Data API source for AU creators (optional) |
| `src/ai.py` | small | `temperature` option (low for fact work) |
| `src/defaults.py` | extended | New columns, settings, 5 new business niches + 3 YouTube niches, Options list, chain blocklist, playbook |
| `src/selftest.py` | **new** | Offline test, runs before every bot run |
| `.github/workflows/run-lead-bot.yml` | small | Runs the self-test first. Adds `YOUTUBE_API_KEYS`. AI is now optional |

In GitHub: open each file > pencil icon > paste the new content > **Commit changes**. For a new file, use **Add file > Create new file** and type the path, e.g. `src/yt.py`.

**Use a NEW Google Sheet (strongly recommended).** Make a new sheet, share it with the robot email and update the `SHEET_ID` secret. The new sheet seeds every new setting and niche cleanly. If you keep the old sheet: old niche tabs are renamed `OLD <name>` (nothing is deleted), and old `W_*` weights / `MIN_SCORE` settings are ignored. v2 uses `W2_*` and `MIN_ICP_SCORE`.

## 2. Is it automatic?

Yes. GitHub runs it every day at 20:00 UTC (6-7am Sydney) with no clicks. **Actions > Run Lead Bot > Run workflow** runs it now. You never run anything manually. Repo minutes: one run of about 45 minutes a day is about 1,350 minutes a month. A private repo gets 2,000 free minutes, a public repo is unlimited. Do not add a second daily run on a private repo.

## 3. How many leads per day

- **Hard cap:** `NEW_LEADS_PER_RUN` = 60.
- **Realistic with only free sources (OpenStreetMap + websites):** about **20-45 leads/day** at the 7/10 quality gate.
- **With a free YouTube key:** about **+5-15/day** of AU creators.
- **With a Google Places key:** more businesses found and real review counts, so more leads pass 7/10. Expect about **40-60/day**.
- The **Dashboard > "Average leads per day (7 days)"** shows the real number after one week. Trust that over this estimate. If it is too low, lower `MIN_ICP_SCORE` to 6.5 or raise `MAX_SEARCH_REQUESTS_PER_RUN`. If it is too high, raise the gate.

These are estimates. Website quality and how many owners publish their names vary by niche.

## 4. Columns (in this order, every niche tab + All Leads)

Niche, Group, **ICP Score /10**, Tier, **Company Name**, **Decision Maker Name**, First Name, Decision Maker Role, Name Source, **Personal Email**, **Generic Email**, **Other Emails**, Email Verified, Phone, Instagram, Facebook, LinkedIn, TikTok, YouTube, Twitter / X, Other Socials, Website, Full Address, Suburb, City, State, Postcode, Country, Map Url, **Case Study**, **Suggested Pitch AUD/mo**, Pitch Angle, Social Gap, Email Subject, Email Draft, Website Summary, Ad / Spend Signals, Google Rating, Review Count, Employee Count, Business Type, YT Subscribers, YT Uploads 30d, IG Followers, IG Engagement %, IG Posts 30d, Email Source, Email Type, Notes, Enrichment, Data Source, Found On, Status (dropdown), My Notes, Last Checked, Lead Added On, Score (0-100), Place Id.

- **Decision Maker Name** is filled only when a name and a decision role (owner, founder, director, principal, practice/marketing manager, licensee, CEO) appear together on their website, in structured data, in the YouTube description or in Hunter. An AI-suggested name is kept only if it appears word-for-word on the site next to a role. Otherwise it stays blank. Nothing is guessed.
- **Personal Email** is filled in this order: (1) the decision maker's own mailbox found on the site or in Hunter, (2) the Hunter email finder (score >= 80), (3) a non-generic mailbox on the business domain. **Generic Email** holds info@/hello@/reception@-style mailboxes. All remaining addresses go in **Other Emails**, comma-separated in one cell.
- **Case Study** holds 2-3 AI sentences on their problem and the angle to pitch. Inferences start with "Likely". With no AI, or when AI credit runs out, it holds fact-only notes starting "Observed:", so the run never fails.
- **Suggested Pitch AUD/mo** is a starting price. It runs 500-1,000 for businesses and 1,000-2,000 for YouTube, scaled by ICP score and niche budget. You can change the ranges in Rules (`PITCH_*`). It is an estimate.

## 5. New tabs

- **Dashboard** is always the first tab:
  - Leads added today (this cell updates every day; no new rows are added), last 7 days, average per day, total, Tier A count, % with a personal email, % with a decision-maker name, and the last run's summary.
  - A table per niche with Total / Today / 7 days / Tier A / Personal email / Decision maker / Avg ICP / Share %, plus a **horizontal green bar** per niche.
- **All Leads** merges every niche tab into one live list, best first. Point the draft bot's master tab at `All Leads`.
- **Options** lists every free or optional service: key name, free tier, what it adds, whether it is wired in, a sign-up link, and a **Status (last run)** that the bot writes (Active / Not set / Off: out of credit).
  - You can paste a key into "Your key" and it is used next run. A GitHub secret always wins over the sheet.
  - **Keep the sheet private** if you do this: anyone with access can read the keys. GitHub secrets are safer.

## 6. Free options that improve quality (all optional)

| Service | Free tier | Adds | Wired |
|---|---|---|---|
| Gemini / Groq / OpenRouter (`AI_API_KEYS`) | free, no card | Case Study, name check, personalised drafts | yes |
| YouTube Data API (`YOUTUBE_API_KEYS`) | 10,000 units/day | AU creator niches | yes |
| Hunter.io (`HUNTER_API_KEY`) | 25 searches + 50 verifications/mo | names + personal emails + verification | yes |
| ZeroBounce (`ZEROBOUNCE_API_KEY`) | 100 verifications/mo | bounce-proof emails | yes |
| Jina Reader (`JINA_API_KEY`) | keyless; key = more | reads JavaScript sites | yes |
| Google Places (`PLACES_API_KEYS`) | billing account + monthly free allowance | better discovery + reviews | yes |
| Apollo (`APOLLO_API_KEY`) | free plan, limited API | employee count | yes |
| Apify (`APIFY_API_TOKEN`) | $5 credit/mo | Instagram stats | yes |
| Meta IG Graph (`IG_ACCESS_TOKEN` + `IG_USER_ID`) | free | Instagram stats | yes |
| Snov.io, ContactOut, Apollo extension | small free quotas | by hand on Tier A leads | manual |

Best value for quality: **Gemini key + YouTube key + Hunter**. Hunter's 25 searches/month are spent only where the site showed no email or no decision maker. Free tiers change, so check each site.

## 7. Errors fixed now (would have hurt later)

1. **"Today" was wrong.** Dates were in UTC, but the run is at 6am Sydney, so leads were stamped with yesterday. Dates now use `TIMEZONE` (Australia/Sydney).
2. **Weak leads got in.** `MIN_SCORE` 50/100 let roughly 5/10 leads through. The gate is now `MIN_ICP_SCORE` 7/10. Leads that cannot reach it skip the AI call, which saves credit.
3. **One email column.** Personal and generic emails were mixed and owner names were never filled. They are now split, and names are filled only from facts.
4. **Slow runs meant few leads.** Websites were read one at a time. 6 now read in parallel (`PARALLEL_SITE_READS`).
5. **Link-in-bio hosts were treated as chains.** linktr.ee and similar no longer count as a "chain" website.
6. **`SOURCE=places` with no key crashed the bot.** It now falls back to free OpenStreetMap.
7. **When Places keys ran out, the run stopped searching.** It now continues on OpenStreetMap.
8. **New niches never reached existing sheets.** Missing default niches are now appended once. To remove one, set Enabled = No; don't delete the row.
9. **A bad AI JSON reply would have switched AI off for the whole run.** Only real outages trip the breaker now.
10. **AI key was mandatory in the docs.** Only `GOOGLE_SA` + `SHEET_ID` are required now.
11. **No pre-run check.** `selftest.py` now runs first and fails loudly before touching your sheet.
12. **No merged view for the draft bot.** It looked for a `Main` tab that did not exist. **All Leads** now provides one.

## 8. Known limits / what can still go wrong

- **Small owner-operated clinics** often publish no names. Decision Maker Name will be blank there, by design.
- **OpenStreetMap has no review counts**, so "established" is neutral for free leads. Google Places fixes this.
- **YouTube hides many creator emails** behind a captcha. Only emails in the description or on their site are used, so some channels are rejected.
- **Spam Act 2003 (AU):** set `SENDER_NAME`, `AGENCY_NAME` and `SENDER_ADDRESS` (repo Variables), keep the opt-out line, and honour "no thanks" replies. **AHPRA rules** apply to health niches.
- **Google Sheets has a 10M-cell limit.** Seen grows by about 300 rows/day, so at roughly 2 years, archive old Seen rows.
- **Security:** plain-text keys exist on your D: drive (`Draft Emails API Keys.txt`, `Insta Automation API's.txt`, the service-account `.json`). Move them into GitHub secrets / a password manager, then delete or rotate them.
