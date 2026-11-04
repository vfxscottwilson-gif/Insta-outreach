# FREE TOOLS RESEARCH - B2B lead-gen bot (video/social agency)
Date: 2026-11-01. Method: 4 web searches (vendor-blog heavy) + prior knowledge. Items marked (v) = verified in a search this session; (u) = from memory, CONFIRM on the vendor pricing page before building. Free tiers change without notice.
Risk = ToS/legal. GHA = works from GitHub Actions runners (Azure IPs, outbound port 25 blocked).

## 1. Search / discovery engines (to find contact pages and emails)
| Tool | Adds | Free limit | Key? | GHA | Risk | Verdict |
|---|---|---|---|---|---|---|
| Bing Web Search API | nothing | RETIRED 11 Aug 2025 (v) learn.microsoft.com/lifecycle/announcements/bing-search-api-retirement | - | - | - | SKIP |
| Google Programmable Search JSON API | site-restricted search | Closed to new customers; shutdown 1 Jan 2027 (v, vendor blogs: apiserpent.com, addsearch.com) | key | ok | low | SKIP (do not build on it) |
| SearXNG self-hosted | meta-search, no key, JSON output | unlimited, but upstream engines (Google/Bing) rate-limit/CAPTCHA datacenter IPs | none | Docker service in workflow possible; IP blocks likely | med (scraping engines) | OPTIONAL (use with DDG/Brave/Mojeek/Yandex engines only) |
| DuckDuckGo (ddgs / duckduckgo-search lib) | free web+maps-style text search | no key; throttled ~dozens of queries before 202/ratelimit | none | frequent blocks from GHA IPs | med (unofficial) | OPTIONAL fallback |
| Mojeek / Marginalia | independent index, API-able | Mojeek API paid; Marginalia free key (u) | key | ok | low | SKIP |
| Common Crawl (index.commoncrawl.org CDX + WARC) | find all pages of a domain (contact/about) w/o hitting site | free, public S3/HTTP | none | ok (be polite) | low | OPTIONAL - good for "does domain have /contact" and old email strings |

## 2. Email finding / enrichment (free tiers)
| Tool | Free limit | Key | GHA | Risk | Verdict |
|---|---|---|---|---|---|
| Snov.io | 50 credits/mo shared pool, API on free (v) | client id+secret | ok | low | ADD (small) |
| Skrapp | ~50-150 credits/mo (u) | key | ok | low | OPTIONAL |
| Tomba | 25 searches + 50 verifications/mo (v 25 searches) | key+secret | ok | low | OPTIONAL |
| Prospeo | free plan conflicting (50 / 75 / 100 per mo reported (v)); person+domain, mobile paid | key | ok | low | ADD (test real quota) |
| Findymail | no recurring free; ~10 trial credits (v) | key | ok | low | SKIP |
| Anymail Finder | ~20 trial credits, pay only for valid (u) | key | ok | low | SKIP |
| Voila Norbert | 50 trial credits (u) | key | ok | low | SKIP |
| Hunter (already used) | 50 credits/mo incl. API (v) | - | - | - | already in |
| Own pipeline: website crawl (crawl4ai) + mailto/regex + schema.org + obfuscation decode (`[at]`, JS-cfemail Cloudflare decode) | unlimited | none | ok | low (public data) | ADD if missing: cfemail decoder, /contact /about /team /privacy-policy (privacy pages often contain a real email) |
| Email permutator (first.last@, flast@ ...) + verify | unlimited | none | SMTP part fails (see below) | low | OPTIONAL, only for named decision-makers |
| Whois/RDAP registrant email | mostly GDPR-redacted | none | ok | low | SKIP |
| Gravatar / GitHub commit email | rare hits for creators | none | ok | low | SKIP |
| YouTube channel "About" business email | behind CAPTCHA; yt-dlp does not expose it. Descriptions often contain email/links - parse description + linked Linktree/Beacons/Stan pages | none | ok | low | ADD (link-in-bio crawler: linktr.ee, beacons.ai, stan.store, bio.link, lnk.bio) |

## 3. Email verification (list hygiene)
| Tool | Free limit | GHA | Risk | Verdict |
|---|---|---|---|---|
| dnspython MX (already) | unlimited | ok | low | keep |
| Disify (disify.com API) | free, no key, throwaway/format/DNS check; rate-limited (u) | ok | low | ADD (cheap pre-filter, disposable detection) |
| check-if-email-exists / Reacher (open-source, AGPL; hosted API paid) | self-host unlimited; needs outbound port 25 | NO on GHA (25 blocked); needs a VPS/home box with clean IP + rDNS | med (probing mail servers; IP gets blocklisted) | OPTIONAL - run on a $5 VPS or free Oracle/Hetzner-class box, not GHA |
| Raw SMTP RCPT verify (smtplib) | free | NO on GHA (port 25) | med | SKIP on GHA; catch-all and Gmail/M365 give false positives anyway |
| MillionVerifier | 100 free credits one-off (u); cheap paid ~$37/10k | ok | low | OPTIONAL later |
| Bouncer | 100 free credits one-off (u) | ok | low | OPTIONAL |
| Emailable | 250 free one-off (u) | ok | low | OPTIONAL |
| ZeroBounce (already) | 100/mo free | - | - | keep, reserve for final-stage only |
Rule: verify only leads that score >=7 (saves credits). Never send to catch-all/"risky" without a separate low-volume stream.

## 4. Social handles and follower counts
| Tool | Adds | Free limit | GHA | Risk | Verdict |
|---|---|---|---|---|---|
| Parse own website HTML for social links (header/footer/JSON-LD sameAs) | highest-precision handle discovery | free | ok | low | ADD first (most reliable) |
| Instagram public page / web_profile_info endpoint | followers, bio, public email/phone in business bio | unofficial, aggressive login-walls and 429 after ~tens of requests per IP; datacenter IPs blocked fast | poor | HIGH (Meta ToS) | SKIP direct scraping; use Meta IG Graph business_discovery (already) for handle->followers. Only needs IG business token + handle |
| Instagram Graph: business_discovery | followers, media count for ANY public business/creator account | 200 calls/hr/user | ok | low (official) | keep (already) - best free follower source |
| TikTok: oEmbed (no key) + public page `__UNIVERSAL_DATA_FOR_REHYDRATION__` JSON | followers, bio, bio-link | oEmbed free; page scrape rate-limited | medium (blocks) | med-high | OPTIONAL (page JSON, low volume, 1 req/3s) |
| TikTok Research/Display API | needs approval; not for lead-gen | - | - | - | SKIP |
| Facebook page public "About" (mbasic/m.facebook) | phone, email, address, followers | blocks/login wall fast | poor | HIGH | SKIP; use Graph API Page Public Content Access only if approved (hard) |
| YouTube Data API (already) | subs, channel links, description email | 10k units/day free | ok | low | keep |
| social-analyzer (qeeqbox, open-source) | username -> profile across ~1000 sites | free | ok | med (probes sites) | SKIP (low value for businesses; handle already on website) |
| Sherlock / maigret | username enumeration | free | ok | med; also creepy for personal persons (GDPR) | SKIP for decision-makers; OPTIONAL for creators' other handles |
| X/Twitter API | free tier effectively write-only (u) | - | - | - | SKIP |
| LinkedIn | no free API; scraping = HIGH risk | - | - | HIGH | SKIP; use Google/Serper query `site:linkedin.com/in "Owner" "<business>"` for name only (facts from snippet; already via Serper/Brave) |

## 5. Registries (owner/director name = facts-only, plus size proxy)
| Registry | Adds | Free | Key | GHA | Risk | Verdict |
|---|---|---|---|---|---|---|
| Companies House UK (already) | directors, officers, SIC, accounts size | 600 req/5min | key | ok | low | keep; add `officers` + `PSC` endpoints if not used. Note GDPR: sole-trader names = personal data (legit-interest ok for B2B, document it) |
| ABN Lookup AU (already) | entity name/type/status/GST | free | GUID | ok | low | keep; add ASIC company data via data.gov.au bulk CSV (weekly, free) for directors-by-company? ASIC dataset has company names only, no directors |
| NZBN API (api.business.govt.nz) | NZ company name, addresses, phone, email, website, directors, trading names | free API w/ subscription key (u) | key (free signup) | ok | low | ADD (NZ coverage; returns emails/phones often) -> NZBN_API_KEY |
| CRO Ireland (core.cro.ie open data API) | IE company names, addresses, status | free with registered key (u); directors only in paid/limited | key | ok | low | OPTIONAL -> CRO_API_KEY |
| Corporations Canada (ised-isde.canada.ca open data CSV/API) | federal corps only; most local businesses are provincial | free | none | ok | low | SKIP (low yield); BC/ON/AB registries mostly paywalled |
| US state Secretary of State (CA bizfile, FL Sunbiz, TX, NY open data on data.ny.gov) | officer/agent names | bulk free for FL (Sunbiz), NY (Socrata), several; others scraping/CAPTCHA | none | ok for open data only | low (open data) / high (scraping) | OPTIONAL: Socrata open data portals (NY, CT, CO, OR, WA) = free JSON, no key (rate-limited, app token free) |
| OpenCorporates | 140+ jurisdictions | free tier restricted to open-data/public-benefit; sources disagree 200/mo vs 1,000/mo (v) | key | ok | med (licence: commercial use needs paid) | SKIP for commercial lead-gen |
| UAE (DED/DMCC/free-zone registers), Saudi MoC/"Wathq", Qatar MOCI | no free API; Wathq is paid (u) | - | - | - | - | SKIP; use Google Maps/OSM + website + trade-licence number on site footers |
| Wappalyzer | open-source repo archived; use `wappalyzer-core` fork or webappanalyzer (community fork, free) | free | none | ok | low | OPTIONAL - detect Shopify/Wix/WordPress, Meta Pixel, GA, booking tools = budget proxy |
| BuiltWith free | domain lookup page; API is paid, free API limited (u) | - | - | - | SKIP |
| Similarweb free | traffic rank only via UI; API paid | - | - | - | SKIP |
| Own tech sniff (HTML: Meta Pixel, GTM, TikTok pixel, booking widgets) | ad-spend/size proxy | free | none | ok | low | ADD (cheap with crawl4ai already running) |

## 6. Agency detection and size/revenue proxy (free signals)
- Meta Ad Library (already): advertiser page + "Active ads" count = ad spender; page_name vs landing-page domain.
- Website footer / `<meta generator>` / "Website by X" / "Powered by" credit links = agency already exists (regex: "designed by|website by|marketing by|powered by").
- Instagram bio tags (@agency) and tagged-post accounts; YouTube video descriptions with "edited by".
- Size proxies: Google Places review count + rating (already), number of Maps locations for same brand, Companies House accounts category (micro/small), team page headcount, ABN GST-registered, Meta Pixel presence, posting frequency, last-post date.

## 7. AI free tiers (short summaries/classification, not core extraction)
| Provider | Free limit (all vendor-blog (v) - confirm in console) | Key | GHA | Risk | Verdict |
|---|---|---|---|---|---|
| Google Gemini (AI Studio) | Flash-class free, ~1,500 req/day claimed; Pro models moved to paid Apr 2026; limits no longer published prominently (v) | GEMINI_API_KEY | ok | low | ADD (primary) |
| Groq | ~30 RPM; 1k-14.4k req/day by model (v conflicting) | GROQ_API_KEY | ok | low | ADD (fallback, fastest) |
| Cerebras | ~1M tokens/day claimed vs $5 trial credit (v conflicting) | CEREBRAS_API_KEY | ok | low | OPTIONAL |
| OpenRouter `:free` models | rate-limited; daily cap tied to purchase history (v) | OPENROUTER_API_KEY | ok | low | OPTIONAL (flaky) |
| Mistral La Plateforme free "Experiment" tier | low RPM, ~1B tokens/mo (u) | MISTRAL_API_KEY | ok | low | OPTIONAL |
| Cloudflare Workers AI | 10k neurons/day free (u) | CF token+account id | ok | low | OPTIONAL |
| GitHub Models | free for prototyping w/ GITHUB_TOKEN, tight RPD (u) | uses GITHUB_TOKEN (no new secret) | ok | low | OPTIONAL (zero signup) |
| HuggingFace Inference | small monthly free credit (u) | HF_TOKEN | ok | low | SKIP |
Pattern: provider chain Gemini -> Groq -> GitHub Models; cache by domain hash; send <=1.5k tokens (title, meta, services, reviews snippets).

## 8. Things you may be missing
**Deliverability / hygiene**
- Send from a separate domain (not main brand), SPF+DKIM+DMARC (p=none -> quarantine), warm-up 3-4 weeks, <=30-50/day/mailbox. Free checks: MXToolbox, Google Postmaster Tools, mail-tester.com (limited free tests).
- Suppress: role accounts for personal outreach (info@/admin@ ok for first touch, but not noreply/abuse/postmaster), disposable domains (Disify), catch-all handled separately, bounces >2% = stop.
- Dedupe by domain + normalised phone (E.164 via `phonenumbers` lib, free); validate phone type (mobile vs landline) with libphonenumber; store `source_url` + `fetched_at` per field (provenance = defence in GDPR requests).
- Unsubscribe list stored and checked BEFORE each run (global suppression sheet/DB).
**Compliance (not legal advice; get a lawyer for scale)**
| Region | Rule | Practical impact |
|---|---|---|
| US | CAN-SPAM | B2B cold email allowed; no deceptive headers, physical address, working opt-out honoured within 10 business days |
| Canada | CASL | Strictest. Implied consent only for "conspicuously published" business address WITHOUT a "no unsolicited" notice AND message relevant to their role. Must include sender id + unsubscribe. Fines up to C$10M |
| UK | PECR + UK GDPR | Corporate subscribers (Ltd/LLP/PLC) can be emailed B2B; sole traders/partnerships = individuals, need consent. Legitimate-interest assessment, privacy notice, opt-out |
| Ireland | ePrivacy Regs 2011 + GDPR | Similar to UK; unsolicited to legal persons ok if opt-out offered; individuals need consent |
| Australia | Spam Act 2003 | Needs consent (express or inferred from conspicuously published work address + relevant to role); sender id + functional unsubscribe (5 business days). Do-Not-Call Register applies to cold calls |
| NZ | Unsolicited Electronic Messages Act 2007 | Needs consent; conspicuously published business address can imply it; unsubscribe required |
| UAE / Saudi / Qatar | PDPL (UAE Federal Decree-Law 45/2021; Saudi PDPL in force Sept 2023, enforcement from Sept 2024; Qatar Law 13/2016) + telecom rules (TDRA/CST/CRA) | Treat as consent-leaning: prefer WhatsApp/LinkedIn manual first touch on public business numbers, state opt-out; Saudi bans transferring personal data abroad without conditions - avoid storing named individuals from KSA in US cloud without basis |
- Facts-only names rule: keep `name_source_url`; drop names from private/personal sources; honour deletion requests within 30 days; keep a record of processing.
- Cold calling: US TCPA/DNC (mobile numbers), UK TPS/CTPS check (free for lookup via paid TPS; skip auto-dialing), AU DNCR. Do not auto-text.
**Infrastructure**
- Google Sheets cap: 10M cells/workbook (also 18,278 columns, 5M cells recommended for speed; API 300 read/min/project, 60 write/min/user). 40 columns x 250k rows = 10M -> hit the cap. Mitigate: one tab per country/niche, archive scored <7 and sent leads to CSV/Parquet in repo releases or SQLite/DuckDB; store only top fields in Sheets; free alternatives: Supabase free (500MB), Cloudflare D1 free, Turso free, Airtable free (1k rows - too small), NocoDB self-host.
- Batch writes (`values.batchUpdate`, append 500 rows) to avoid 429.
- GHA limits: public repo unlimited minutes; private 2,000 min/mo; 6h/job; IPs are datacenter (Google/Instagram/LinkedIn block) -> route risky fetches via Jina/ZenRows (already) or Cloudflare Workers (free 100k req/day, different IP pool).
- robots.txt respect + polite delay + custom UA with contact URL (reduces legal exposure and IP bans).
- Free CRM for tracking replies: HubSpot free CRM, Twenty (OSS), Attio free tier (u).
- Free outbound sending: Brevo (300/day), Mailgun/Resend free are transactional-oriented and may ban cold email; use real mailboxes (Google Workspace/Zoho) + open-source sequencers: Mautic, Listmonk (consent-based only).
- Google Maps data gaps: OSM `contact:email`, `contact:phone`, `contact:instagram` tags are ignored by many - Overpass can pull them directly (already partially).
- Wikidata/Wikipedia SPARQL for creators >100k subs (official site, socials) - free, no key, LOW risk -> OPTIONAL.
- Yelp Fusion free (500/day, u), Foursquare Places free tier (u; ~$ credit), TomTom/HERE free tiers (u) as extra POI sources outside Google: OPTIONAL for UAE/KSA/QA where OSM is thin.
- Gulf specifics: Google Maps coverage good; add Arabic query terms; use `.ae/.sa/.qa` + Instagram-first (WhatsApp numbers on bios, "wa.me/" links = phone proxy; parse wa.me and api.whatsapp.com/send links in websites - free, high-yield).

## 9. TOP 10 TO ADD (ranked by value/effort)
| # | Add | Why | GitHub secret |
|---|---|---|---|
| 1 | Website-first harvester upgrade (own code, free): cfemail decode, /contact /about /team /privacy, mailto, wa.me, JSON-LD sameAs, social links, "website by" agency regex, pixel detection | biggest yield for zero cost | none |
| 2 | Link-in-bio crawler (linktr.ee, beacons.ai, stan.store, bio.link) for creators' business email | creators' emails live here | none |
| 3 | Gemini free tier as primary summariser/classifier | free, strong, simple | GEMINI_API_KEY |
| 4 | Groq as fallback LLM | speed + 2nd quota | GROQ_API_KEY |
| 5 | NZBN API (NZ names, emails, phones, directors) | NZ is otherwise thin | NZBN_API_KEY |
| 6 | Disify + phonenumbers lib pre-filter (disposable/format/E.164) | cheap hygiene, saves paid credits | none (Disify keyless) |
| 7 | Snov.io free credits (email find + verify) | extra 50/mo, API free | SNOV_CLIENT_ID, SNOV_CLIENT_SECRET |
| 8 | Prospeo free plan (person+domain lookups) | extra 50-100/mo; test quota first | PROSPEO_API_KEY |
| 9 | Suppression list + provenance columns (source_url, fetched_at, consent_basis) + per-country compliance flag | CASL/PECR/Spam Act defence | none |
| 10 | Sheets-overflow plan: tab per niche/country + DuckDB/CSV archive; optional Reacher on a VPS for SMTP verify | avoids 10M-cell cliff and port-25 block | REACHER_URL (only if self-hosted) |

Honourable mentions: Common Crawl CDX (OPTIONAL), SearXNG/DDG fallback (OPTIONAL), CRO_API_KEY, Cloudflare Workers as alternate egress IP (CF_API_TOKEN), Socrata US open data (SOCRATA_APP_TOKEN), MillionVerifier 100 free (MILLIONVERIFIER_API_KEY).

## Sources (searched 2026-11-01)
- https://learn.microsoft.com/en-za/lifecycle/announcements/bing-search-api-retirement
- https://apiserpent.com/blog/google-custom-search-api-shutdown-migration
- https://www.addsearch.com/blog/google-programmable-search-engine-alternatives/
- https://prospeo.io/s/free-email-finder (vendor; figures conflict)
- https://reply.io/blog/best-email-finder-apis/
- https://dev.to/0012303/11-free-ai-apis-you-can-use-without-paying-openai-2026-update-422h
- https://benchlm.ai/md/free-tier.md
- https://dev.to/openregistry/hit-opencorporates-200month-limit-heres-a-free-passthrough-to-ukeu-registries-3h7a
- https://zephira.ai/opencorporates-pricing-explained-2026-plans-api-limits-licensing-and-what-it-means-in-production/
Caveat: most sources are vendor blogs; items marked (u) were not re-verified.
