# Lead Bot v4: high-quality segments + one Google Sheet per country

Implements `D:\All Automations Records\Lead generation\HIGH_QUALITY_LEADS_SPEC.md` in the worldwide edition.
Setup steps for the 7 sheets: **[SHEETS_SETUP.md](SHEETS_SETUP.md)**. The Australia-only edition (`au-only-lead-bot`)
is NOT changed yet (it keeps v3.1 scoring and its single sheet).

Tests: `python src/selftest.py` (52 checks) and `python -m unittest discover -s tests` (71 tests, network mocked,
including a full US-sheet run that produces a PRIME and a HAS-AGENCY lead), plus a live run (section 4).

## 1. Files changed

| File | Change |
|---|---|
| `src/quality.py` | **new**: R revenue proxy, S social strength, A agency/in-house score, segment rules, revenue band + basis, v4 ICP weights, YouTube editor-credit check, niche threshold profiles (spec section 5), country review factors (section 7) |
| `src/leadbot.py` | one sheet per target (`COUNTRY` / `--country`, `--all`), missing `SHEET_ID_<X>` = skip, old `SHEET_ID` fallback; per-sheet seeds; imports routed to their country's sheet (YouTube rows to the YouTube sheet); v4 scoring in `qualify` (`SEGMENT_SCORING=No` = old v3 score); in-house LinkedIn check for PRIME candidates; review-count `Snapshots` (velocity); sort by Segment then ICP; niche tabs in logical order after the Dashboard; Dashboard segment bars; `All Leads` merges tabs with older column orders |
| `src/defaults.py` | new column layout (Segment, Revenue Band near the front; 13 evidence columns after `Place Id`); 34 new Rules (incl. `FREE_MODE_NICHE_WEIGHT`) (all thresholds + `W3_*` weights + review factors + YouTube gates); 10 new Niches columns with country-specific tickets; `SHEET_TARGETS`, `seeds_for()`, `GROUP_ORDER`, `SNAP_H` |
| `src/yt.py` | median views of the last 5 videos (free RSS feed / 1-unit API call), gate `YT_MIN_VIEWS` |
| `src/enrich.py` | agency evidence + booking tool collected from the pages already fetched |
| `src/optional.py` | Instagram stats now include posts/90 days, Reels share, posting regularity, captions + bio (Meta and Apify) |
| `src/localsheet.py` | multi-key sort, any tab move |
| `src/selftest.py` | + segment boundaries, agency cap, YouTube gates, missing-sheet-id skip |
| `tests/test_v4.py` | **new**, 18 tests |
| `tests/test_v3.py`, `tests/au_pipeline_case.py` | v3-path tests pinned with `SEGMENT_SCORING=No`; new column layout |
| `.github/workflows/run-lead-bot.yml` | 7 jobs (US, GB, CA, AU, NZ, IE, YOUTUBE), `--setup --all`, `--finish --all`, 7 sheet secrets |
| `SHEETS_SETUP.md` | **new**: create/share the 7 sheets, secrets |

## 2. How a lead is judged now

1. **Hard rejects** (unchanged + spec): closed, chain/franchise, low rating, no contact. Also **too few reviews for
   the niche** (niche min × country factor, unless the ABN says the business is 3+ years old).
2. **R revenue proxy 0-10**: reviews 30%, review velocity 25%, locations sharing the website 15%, price level 10%,
   ad pixels + premium booking tool 10%, size (Apollo staff / AU GST) 10%. Unknown parts count as neutral (0.5) and
   lower `R Confidence`.
3. **S social strength 0-10** from Instagram (followers, posts/30 days, posts/90 days, engagement, Reels share). Without
   an IG token: no profile found = 1.0; profile found but not measurable = `S_UNMEASURED` (4.0).
4. **A agency 0-100**: footer credit "marketing/social by X" +30, "website by X" +10, GoHighLevel/CallRail/WhatConverts/
   2+ GTM containers +15, IG caption credits (managed/content/shot by @x, or one handle tagged on 3+ posts) +30, pro
   cadence +15, LinkedIn in-house social/marketing person +20, scheduler link +5. **Capped at 49 without a named credit
   or in-house role**, so cadence or tools alone never make HAS-AGENCY.
5. **Segment** (Rules thresholds): REJECT R < 3 → HAS-AGENCY A ≥ 50 → PRIME (R ≥ 7, S ≤ 4, A < 30) → PRIME-REVIEW
   (A 30-49) → GROWING (R 4-6.9 & S ≤ 6.5, or R ≥ 7 & 4 < S ≤ 6.5) → POLISHED-NO-SIGNAL (S > 6.5) → else REJECT.
   REJECT rows are only in the Seen tab.
6. **ICP /10** = 35 R + 25 gap + 15 fit + 15 contact + 5 decision maker + 3 rating + 2 location − agency penalty.
   PRIME / PRIME-REVIEW / GROWING must still reach **7/10**. HAS-AGENCY / POLISHED are kept when R ≥ `SIDE_SEGMENT_R_MIN` (6).
7. **Revenue Band** Low / Mid / High (< 15k, 15-60k, > 60k local currency per month) with **Revenue Est. Basis**:
   - the formula (review velocity ÷ review rate × visits × ticket) when a review velocity is known (`Snapshots` after
     30+ days, or reviews ÷ ABN age in AU);
   - otherwise a proxy band from R, said in plain words.
   It is never an exact revenue claim.

## 3. YouTube sheet (worldwide)

Subscribers 20,000–500,000 · last upload ≤ 14 days · median views of the last ~5 videos ≥ 20,000 (`YT_MIN_VIEWS`)
· unknown country allowed (blank `Country`) · one tab per YouTube niche · Segment PRIME, or HAS-AGENCY when the
description credits an editor/manager.

## 4. Realistic leads/day per country

### Measured (live, 2026-10-31): same 4 searches, Chicago, free sources only (no Places / Serper key)

| Search | Businesses | v3 score | v4 strict (spec as written) | **v4 with free-mode fallback (shipped)** |
|---|---|---|---|---|
| Dentists | 60 | 14 | 0 | **9** |
| Boutique gyms / studios | 127 | 11 | 0 | **6** |
| Real estate (independent) | 23 | 8 | 1 | **6** |
| Cosmetic & skin clinics | 12 | 4 | 0 | **2** |
| **Total** | **222** | **37** | **1** | **23** (6 PRIME-REVIEW, 17 GROWING; bands 18 Mid / 5 High) |

Why strict v4 gave ~0: without a review count, R tops out around 4.5-5.5, so almost nothing reaches 7/10. A first
fallback that only renormalised over the free signals made it worse (**0 leads**): a typical business has just 1
location (scores 0.3) and 0-1 ad pixels. **Shipped fix:** in free mode the niche's Budget Fit is one of the present R
signals (weight `FREE_MODE_NICHE_WEIGHT` 0.30), rows say "free signals (unverified)", and such rows are **capped at
PRIME-REVIEW** (never PRIME without a review count; the evidence says "check Google rating/reviews by hand").

### With a review count (Google Places key, or `SERPER_API_KEY`, or gosom/Apify imports): estimate, not measured

There was no key to test it. Mechanically:
- reviews become 30% of R (velocity follows after 30 days of Snapshots);
- businesses under the niche minimum are rejected outright;
- strong ones (150+ reviews for a dentist, 2+ sites or ad pixels) reach R ≥ 7, which **unlocks PRIME**.

Expect a similar or somewhat lower count than free mode (±30%), but about 20-30% of them PRIME and fewer weak
GROWING rows. The difference is **precision, not volume.**

### Leads/day per country sheet (free mode, default workflow = 2 runs/day, 1 job per country)

One job does ~15-18 map searches in 42 minutes. Free-mode v4 yield ≈ 60% of v3. That is ~2-3 written leads per
search across all niches (Chicago's dense centre measured ~6 per search). Each country has a finite free-map pool:
**28 niches × its areas**, and each area + niche pair is searched once, then rechecked after 120 days.

| Sheet | Areas seeded | Leads/day while fresh | Fresh for about | Total pool (free) | After that |
|---|---|---|---|---|---|
| US | 23 | 70-100 | 3 weeks | ~1,600 | 5-15/day |
| UK | 12 | 40-70 | 10 days | ~700 | 3-8/day |
| Canada | 7 | 40-70 | 6 days | ~400 | 2-5/day |
| Australia | 39 | 70-100 | 1 month | ~2,500 | 5-15/day |
| New Zealand | 4 | 25-40 | 3 days | ~200 | 1-3/day |
| Ireland | 3 | 15-30 | 3 days | ~150 | 1-3/day |
| YouTube (worldwide) | – | 5-15 | ongoing | – | 5-15/day (gates: 20k-500k subs, ≤ 14 days, ≥ 20k median views) |

**Total while fresh ≈ 250-400/day, falling to ≈ 25-60/day after ~3-4 weeks.** To keep 400+/day:
- **gosom imports** (each country job imports its own rows; ~150-300 extra/day per 1,500-2,000 rows), and/or
- **more suburbs** in each country's Locations tab (each area ≈ +60-80 leads in total), and/or
- **`SERPER_API_KEY`**: review counts for PRIME, plus websites found for the 35% of businesses listed without one.

GitHub minutes: ~7 jobs × ~45 min × 2 runs ≈ 650 min/day, so the repo should be public. Countries without a sheet id cost ~1 minute.
