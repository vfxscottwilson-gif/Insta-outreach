# High-Quality Leads Spec (v1, 2026-10-31)

Maps to `au-lead-bot/src` (score.py, enrich.py, defaults.py). Goal: rank leads by **ability to pay** (revenue proxy) x **need** (social gap), and keep businesses that **already have an agency or in-house team** in a separate list.

> Honesty rule: nobody can read "customers per day" or revenue from a Google profile. Everything below is a *proxy band* (Low / Mid / High), never a number to quote to the prospect. Starting thresholds are heuristics; recalibrate after ~50 replies or closed deals.

---

## 1. Three sub-scores, one segment

| Sub-score | Range | Meaning |
|---|---|---|
| **R** Revenue proxy | 0-10 | Can they afford $500-1k/mo? |
| **S** Social strength | 0-10 | How good their social is now (low S = big gap) |
| **A** Agency / in-house confidence | 0-100 | How sure we are someone already runs their social |

### Segments (evaluated in this order)

| Segment | Rule | Action |
|---|---|---|
| **REJECT** | Any hard filter (section 6) OR R < 3 | Drop |
| **HAS-AGENCY** | A >= 50 | Separate tab, "replacement pitch" later (show `agency_evidence`) |
| **PRIME** | R >= 7 AND S <= 4 AND A < 30 | Outreach first |
| **PRIME-REVIEW** | R >= 7 AND S <= 4 AND 30 <= A < 50 | Manual 1-min check, then PRIME or HAS-AGENCY |
| **GROWING** | (R 4-6.9 AND S <= 6.5 AND A < 50) OR (R >= 7 AND 4 < S <= 6.5 AND A < 50) | Second wave / nurture |
| **POLISHED-NO-SIGNAL** | S > 6.5 AND A < 50 | Treat like HAS-AGENCY (likely in-house); low priority |
| **REJECT (low)** | Everything else (R 3-4 with weak contact) | Drop or archive |

### Final ICP /10 (only for PRIME, PRIME-REVIEW, GROWING)

| Component | Weight | Existing Rules key -> new value | Formula (0-1) |
|---|---|---|---|
| Revenue proxy R | 35 | new `W3_REVENUE` (replaces `W2_ESTABLISHED` 15) | R/10 |
| Social gap | 25 | `W2_SOCIAL_GAP` 10 -> 25 | (10 - S)/10 |
| Niche budget fit | 15 | `W2_NICHE_BUDGET` 30 -> 15 | fit/5 (Budget Fit column) |
| Contactability | 15 | `W2_CONTACT` 20 -> 15 | existing `c` logic |
| Decision maker known | 5 | `W2_DECISION_MAKER` 10 -> 5 | existing |
| Reputation | 3 | `W2_REPUTATION` 3 | existing |
| Location priority | 2 | `W2_LOCATION` 2 | existing |
| Agency penalty | -(A/100) x 15 | new `W3_AGENCY_PENALTY` | applied only when A < 50 |

`W2_SPEND_SIGNAL` and `W2_WEBSITE` fold into R (no double counting). Keep `MIN_ICP_SCORE` = 7 and tiers A >= 8.5, B >= 7.5.

---

## 2. Revenue proxy R (0-10)

`R = 10 x (0.30 n_reviews + 0.25 n_velocity + 0.15 n_locations + 0.10 n_price + 0.10 n_spend + 0.10 n_size)`
Each `n` is 0-1 against the niche row in section 5 (linear between "min" and "strong", capped). Missing value -> 0.5 of its weight (unknown, not bad), and lower `r_confidence`.

| n | Field (new unless noted) | How |
|---|---|---|
| n_reviews | `reviews` (exists) | `userRatingCount` x country factor (section 7) vs niche min/strong |
| n_velocity | `review_velocity_m` | Method A (best): snapshot delta. Store `userRatingCount` + date per `place_id`; on re-check after >= 30 days, velocity = delta / months. Method B (day 1): newest-5 window: if 5 newest reviews span D days, velocity ~ 5 x 30 / D. Legacy Place Details supports `reviews_sort=newest`; Places API (New) returns 5 "most relevant" (verify sort option before relying on B). |
| n_locations | `locations` | Text Search for business name; count results whose `websiteUri` domain == lead domain. 1 = 0.3, 2 = 0.7, 3+ = 1.0 (but 10+ = chain -> REJECT via existing BLOCK_NAME_WORDS) |
| n_price | `price_level` | Places `priceLevel` (INEXPENSIVE..VERY_EXPENSIVE) -> 0.25/0.5/0.75/1.0. Mostly restaurants/cafes; null elsewhere |
| n_spend | `spend` (exists, 0-3) + `booking_tool` | Existing pixel signals; add premium booking tools (section 4) = +1 |
| n_size | `staff_band`, `gst`, `accounts_type`, `hiring` | Apollo `estimated_num_employees` (exists in enrich.apollo), Companies House accounts type, ABN GST status, open job ads |

### Customers/day and revenue estimate (display as a band only)

```
new_customers_month = review_velocity_m / review_rate          # review_rate default 0.03 (range 0.01-0.10)
est_rev_month       = new_customers_month x visits_per_customer x avg_ticket
band: Low < 15k, Mid 15-60k, High > 60k (local currency / month)
```
**Review rate is the weakest link.** No credible public "reviews per customer" study exists; surveys only say ~10% of happy customers *would* review ([Review42](https://review42.com/online-reputation-management-statistics)), ~20% of diners *regularly* review ([McCain via restaurantonline](https://www.restaurantonline.co.uk/Article/2017/08/16/Younger-diners-far-more-likely-to-leave-negative-reviews-online)), 30% of diners use Google for reviews ([Toast](https://pos.toasttab.com/vi-us/blog/data/restaurant-feedback-insights)). Actual "left a Google review per visit" is far lower; 1-5% is an assumption. Keep `REVIEW_RATE_<niche>` editable in Rules and show `est_rev_band` with `r_confidence`.

### Average ticket defaults (Rules tab, editable)

| Niche | Value | Source / status |
|---|---|---|
| Dentist AU | A$321 per visit; A$710 per person per year | [CommBank Health Insights 2025](https://www.commbank.com.au/content/dam/commbank-assets/business/health/commbank-health-insights-report.pdf) (bank card data, solid) |
| Dentist US | US$150-290 per visit (use 250) | [dojobusiness](https://dojobusiness.com/blogs/news/dental-clinic-complete-guide), [clerri](https://clerri.com/blog/dental-practice-revenue-statistics/) (vendor blogs, weak) |
| Dentist UK/CA/NZ/IE | no primary source found; use 0.8x US (UK, NHS mix) / 1.0x AU (NZ) | ASSUMPTION |
| Med spa US | US$164 avg ticket (Zenoti) to US$527 spend per visit (AMSPA) - use 300 | [Zenoti 2025](https://www.zenoti.com/resources/medspa-benchmark-report-2025), [Sagapixel/AMSPA](https://sagapixel.com/marketing/medspa-statistics/) |
| Boutique gym US | US$125/mo per member (range 110-360); class US$21 | [Wodify](https://www.wodify.com/blog/boutique-studio-statistics-trends-owners-should-know), [FitDegree](https://www.fitdegree.com/post/how-to-price-fitness-studio-memberships-without-leaving-money-on-the-table) |
| Gym AU | A$95/mo (all gyms; boutique higher) | [Canstar Blue](https://www.canstarblue.com.au/health-beauty/average-gym-cost/) |
| Real estate | Commission: US 5.44% total; AU ~2.08% metro / 2.45% regional; UK 1-2%; CA no reliable avg | [anyone.com 2026](https://anyone.com/blog/post/real-estate-commission-rates-by-country-2026), [PropertyNow AU](https://www.propertynow.com.au/blog/real-estate-agent-commission-by-state/). Use listings count (realestate.com.au / Rightmove / Zillow public pages, manual) not reviews |
| Upscale restaurant | No sourced figure found | ASSUMPTION: A$/US$/C$ 60-90, GBP 45-70 per head; map from `priceLevel` |
| YouTuber | Not ticket-based; keep existing subs band (20k-250k sweet spot) + uploads30 | existing `score.py` |

For gyms, `visits_per_customer` = months retained (default 8) and velocity -> new members; for real estate skip revenue formula and use `n_size` + listings.

---

## 3. Social strength S (0-10)

`S = 10 x (0.35 n_followers + 0.35 n_cadence + 0.15 n_engagement + 0.15 n_format)`

| n | Field | Rule |
|---|---|---|
| n_followers | `ig_followers`, `fb_followers`, `tt_followers`, `yt_subs` -> `followers_best` | max platform, vs niche weak/strong (section 5) |
| n_cadence | `posts30`, `posts90` (IG main; FB/TT if known) | posts30 vs niche weak/strong; if posts90 < 3 -> 0 ("dormant") |
| n_engagement | `engagement` (exists, %) | <0.5% = 0, 1% = 0.5, >=3% = 1 |
| n_format | `reels_share` (IG `media_product_type`=REELS) | reels share of last 12 posts: 0% = 0, >=40% = 1 |

Existing `social_gap()` becomes `gap = (10 - S)/10` and keeps its plain-English fact strings (add "no post in 60 days", "no Reels in last 12 posts").

---

## 4. Agency / in-house confidence A (0-100, capped)

| Signal | Points | Collection | Field |
|---|---|---|---|
| Footer credit naming a **marketing/social** agency ("marketing by", "managed by", "social by") | +30 | regex on already-fetched site HTML | `agency_credit` |
| Footer credit **web only** ("website by", "designed by", "powered by <studio>") | +10 | same | `web_credit` |
| IG bio / captions contain "managed by @", "content by @", "shot by @", agency handle tagged on >= 3 of last 25 posts | +30 | IG Business Discovery `caption` field (public) | `ig_credit_handles` |
| Agency-type stack on site: GoHighLevel/LeadConnector (`msgsndr.com`, `leadconnectorhq.com`), CallRail, WhatConverts, multiple GTM containers, agency UTM `utm_source=<agency>` | +15 | regex on HTML (extend `SPEND_SIGNS`) | `agency_stack` |
| Pro cadence: posts30 >= niche "strong" AND interval CV < 0.5 AND reels_share >= 40% | +15 | from IG timestamps | `cadence_cv` |
| LinkedIn person at company titled social media / content / marketing manager or coordinator | +20 (in-house) | web-search snippets (`site:linkedin.com/in "<company>" "social media"`), as `people_from_linkedin` already does | `inhouse_role` |
| Open job ad for social media / content creator | +10 (in-house forming; also +n_size) | Adzuna API / search snippets | `hiring_social` |
| Active Meta ads (EU/UK: API; elsewhere manual Ad Library UI check) | +5 | section 8 | `meta_ads_active` |
| Scheduling tool in links (Later, Planoly, Linkin.bio by Later, Sprout) | +5 | IG bio link domain | `sched_tool` |
| Owner-run cues: posts selfie-style, captions first-person "I", irregular gaps > 21 days | -15 | timestamps + caption heuristics | |

Bands: **>= 50 HAS-AGENCY**, 30-49 PRIME-REVIEW, < 30 none. Store `agency_evidence` as a facts-only string ("footer: 'Marketing by XYZ Digital'; @xyzdigital tagged on 5/25 posts"), and `agency_name` when a credit names one (for the replacement pitch).
Reliability: footer/caption credits = high precision, low recall (many agencies stay invisible). Cadence alone = medium (good owners post consistently too). Never put a lead in HAS-AGENCY on cadence alone (cap that signal so A < 50 without a named credit or role).

Premium booking tools (+1 to n_spend, not agency): Boulevard, Zenoti, SevenRooms, Mindbody, Dentally, Cliniko, Jane App (CA), HotDoc / HealthEngine (AU), Zocdoc (US), Fresha / Vagaro (lower tier, +0.5), OpenTable / Resy, Glofox.

---

## 5. Niche thresholds (starting values, country factor 1.0 = US)

| Niche | Reviews min / strong | Velocity strong /mo | Followers weak / strong | posts30 weak / strong | Fit |
|---|---|---|---|---|---|
| Dentist | 20 / 150 | 6 | <1,000 / >5,000 | <4 / >=12 | 4 |
| Med spa / aesthetics | 25 / 200 | 8 | <2,000 / >10,000 | <6 / >=15 | 5 |
| Clinic (physio, chiro, derm) | 20 / 150 | 5 | <800 / >4,000 | <4 / >=12 | 4 |
| Real estate office | 15 / 100 (+ listings) | 4 | <1,500 / >8,000 | <6 / >=16 | 4 |
| Boutique gym / studio | 30 / 200 | 8 | <1,500 / >8,000 | <8 / >=20 | 3 |
| Upscale / multi-site restaurant | 150 / 1,000 | 30 | <3,000 / >15,000 | <6 / >=15 | 3 |
| YouTuber (subs) | 10k / 250k (cap 500k) | uploads30 2 / 5 | n/a | uploads30 <2 / >=5 | 4-5 |

New Rules columns in `NICHES_H` (defaults.py): `Reviews Min`, `Reviews Strong`, `Velocity Strong`, `Followers Weak`, `Followers Strong`, `Posts30 Weak`, `Posts30 Strong`, `Avg Ticket`, `Visits/Customer`, `Review Rate`.

---

## 6. Hard REJECT filters

`businessStatus` != OPERATIONAL; rating < 3.5 with >= 20 reviews; reviews < niche min x country factor (and no registry age >= 3 yrs); chain / franchise (existing `BLOCK_NAME_WORDS*`, or locations >= 10); no website AND no social AND no phone; YouTuber subs < 10k or > 500k (existing).

---

## 7. Country differences

| Country | Review factor* | Registry (free) | Ads data | Notes |
|---|---|---|---|---|
| US | 1.0 | None national; state SOS sites (ToS vary, many ban bulk scraping) | Meta API political only; UI manual | No public staff/revenue data; rely on Apollo + jobs |
| UK | 0.7 | [Companies House API](https://developer.company-information.service.gov.uk/) free, 600 req / 5 min; `accounts.last_accounts.type` (micro-entity / small / full) = size band; officers = decision maker | Meta API **includes commercial ads** delivered in UK (from ~Jul 2025) | NHS dentists vs private: check site for "private" |
| Ireland | 0.5 | CRO open data (data.gov.ie bulk) / CORE web search | EU -> Meta API commercial ads | Small market: lower thresholds |
| Canada | 0.8 | [Corporations Canada API](https://ised-isde.canada.ca/site/corporations-canada/en/node/269) (free key, ~60/min) + daily CSV; BC OrgBook API | political only | Most small firms are provincial, not federal |
| Australia | 0.8 | [ABN Lookup web services](https://abr.business.gov.au/Tools/WebServices) free GUID: ABN age (exists), **GST registered = turnover >= A$75k** (new `gst`) | political only | ASIC officer data not free |
| NZ | 0.5 | NZBN / Companies Office API (free registration) | political only | Treat like AU with lower thresholds |

*Heuristic multiplier on review thresholds for smaller/lower-review markets; not from a study. Recalibrate with real lead data (median reviews per niche per country).

---

## 8. Source matrix per signal

| Signal | Free source | Paid (cost) | ToS-safe collection | Reliability |
|---|---|---|---|---|
| Review count, rating, priceLevel, website, hours, businessStatus | OSM (no reviews); Places free cap 1,000 Enterprise calls/mo | Places Details **Enterprise $20/1k**, Text Search Enterprise $35/1k ([pricing](https://developers.google.com/maps/billing-and-pricing/pricing)); fields are Enterprise SKU ([data fields](https://developers.google.com/maps/documentation/places/web-service/data-fields)) | Official API with field mask. Google terms limit storing Places content (place_id exempt): refresh rather than archive | High |
| 5 reviews + timestamps | Places "Atmosphere" 1,000 free/mo | $25/1k details; full history only via scrapers (Apify ~$0.5-2/1k reviews) | API only; scrapers break Google ToS | API: max **5** reviews ([ref](https://developers.google.com/maps/documentation/places/web-service/reference/rest/v1/places)) |
| Review velocity | Snapshot delta of `userRatingCount` | - | Re-query monthly | Medium-high after 1 month; low on day 1 |
| Locations | Places Text Search | $35/1k | API | Medium (name collisions) |
| Popular times / foot traffic | **Not in any Google API** | Placer.ai / SafeGraph (enterprise $$$, US-centric) | n/a | Impossible free |
| Ad pixels, booking tools, agency stack, footer credits | Own fetch of public site (exists, robots-aware `allowed()`) | BuiltWith ($295+/mo), Wappalyzer API | Respect robots.txt; low rate | High (pixel present != active spend) |
| Meta ads active | Ad Library **web UI** (all countries, manual) | Apify Ad Library actors (~$1/1k, ToS grey) | API: outside EU/UK returns **political/issue ads only**; UK/EU return commercial ads ([summary](https://admanage.ai/blog/facebook-ads-library-api), [ppc.land](https://ppc.land/ads-library/)). Commercial ads show Page name, **not the agency** | UK/IE: High. US/CA/AU/NZ: manual only |
| Google ads active | Ads Transparency Center UI (manual) | - | No official API for commercial ads | Manual |
| IG followers, posts, captions, engagement | **IG Graph API Business Discovery** ([docs](https://developers.facebook.com/docs/instagram-platform/instagram-api-with-facebook-login/business-discovery)): needs your own IG professional account linked to a FB Page, a Meta app and token (`IG_ACCESS_TOKEN`, `IG_USER_ID`, exists) | - | Official; only **business/creator** accounts; personal/private/age-gated return nothing; Meta rate limits apply (~200 calls/hr per user token, verify) | High when returned |
| FB page followers | Graph API needs app review (Page Public Metadata/Content Access) | Apify FB page scrapers (ToS grey) | Without app review: manual check for shortlist only | Low automated |
| TikTok followers / posts | Public profile page viewed manually | Third-party TikTok scrapers ($) | Research API is academic/non-commercial only ([FAQ](https://developers.tiktok.com/doc/research-api-faq)); Display API = own account | Manual only |
| YouTube subs, uploads | YouTube Data API v3, 10,000 units/day free (`channels.list` = 1 unit) ([quota](https://developers.google.com/youtube/v3/getting-started)) | - | Official | High |
| Staff count | LinkedIn company size via search snippet; registries (UK accounts) | Apollo (exists), ZoomInfo ($$$) | No logged-in LinkedIn scraping | Low-medium |
| Hiring | [Adzuna API](https://developer.adzuna.com/) free key (US, UK, CA, AU, NZ); search snippets for Seek/Indeed | - | Official API | Medium |
| Company age / size | Companies House, ABN Lookup, NZBN, Corporations Canada, CRO | OpenCorporates commercial (from ~GBP 2,250/yr; free only for public-benefit users, [terms](https://opencorporates.com/terms-of-use-2/)) | Official APIs | High for age; size only UK (accounts type) and AU (GST floor) |

---

## 9. Bot mapping

**Existing fields reused:** `fit`, `reviews`, `rating`, `subs`, `age` (ABN), `has_website`, `instagram`, `other_social`, `phone`, `decision_maker`, `spend` + `signals`, `gap_sev`, `priority`, `igs{followers, engagement, posts30}`, Apollo `estimated_num_employees`, site `text`/html, `people`.

**New fields:** `place_id`, `price_level`, `business_status`, `review_velocity_m`, `velocity_method`, `locations`, `booking_tool`, `staff_band`, `gst`, `accounts_type`, `hiring`, `hiring_social`, `est_rev_band`, `r_score`, `r_confidence`, `ig_followers`, `fb_followers`, `tt_followers`, `yt_subs`, `posts90`, `cadence_cv`, `reels_share`, `s_score`, `agency_credit`, `web_credit`, `ig_credit_handles`, `agency_stack`, `inhouse_role`, `meta_ads_active`, `agency_score`, `agency_name`, `agency_evidence`, `segment`.

**Changes / new modules:**

| File | Change |
|---|---|
| `places.py` | Field mask add `priceLevel`, `businessStatus`, `reviews.publishTime`; snapshot table (`place_id`, date, `userRatingCount`) for velocity; locations count by domain |
| `enrich.py` | `instagram_stats`: `media.limit(50){timestamp,like_count,comments_count,caption,media_product_type}` + `biography` -> posts90, cadence_cv, reels_share, credit handles. Extend `SPEND_SIGNS` with booking tools + agency stack. Add footer-credit regex |
| new `registries.py` | Companies House, ABN (add GST), NZBN, Corporations Canada, CRO bulk lookup |
| new `revenue.py` | R score, est_rev_band, r_confidence |
| new `social.py` | Merge IG/FB/TT/YT into S; manual-entry columns for FB/TT |
| new `agency.py` | A score + evidence string |
| new `segment.py` | Section 1 rules; writes HAS-AGENCY to its own sheet tab |
| `score.py` | New weights (section 1); `social_gap` uses S |
| `defaults.py` | New Rules keys (`W3_*`, `REVIEW_RATE_*`, `AGENCY_HAS_MIN`=50, `AGENCY_REVIEW_MIN`=30, `PRIME_R_MIN`=7, `PRIME_S_MAX`=4) and niche columns (section 5) |
| `yt.py` | Already YouTube-based; add uploads90 |

---

## 10. Impossible or unreliable (say so in outreach notes)

1. **Actual customers/day or revenue**: not exposed anywhere public; only bands from proxies.
2. **Google Popular Times**: not in the Places API.
3. **More than 5 Google reviews** via the official API; full review history only by ToS-breaking scrapers.
4. **Commercial Meta ads outside EU/UK via API**, and **agency name** behind any commercial ad (anywhere).
5. **TikTok and Facebook follower counts** at scale without app review / third-party scraping; do these manually for PRIME shortlist only.
6. **Private or personal IG accounts**: Business Discovery returns nothing.
7. **US staff counts / revenue** from public registries (none exist).
8. **Invisible agencies** (no credits, no tags): A will miss them; cadence-only cases go to PRIME-REVIEW.
