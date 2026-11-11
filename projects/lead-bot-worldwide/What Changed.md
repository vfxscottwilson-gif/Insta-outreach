# What Changed In Version 6

Date: 2026-11-11. Same bot, same sheets, same columns plus one new column (`Benchmark Check`). Nothing already in your sheets is touched.

## The Benchmark (Why These Numbers)
Goal: a lead who can pay an agency at least US$500 a month.

| Step | Number | Source |
|---|---|---|
| Typical marketing budget, small business | 7-8% of gross revenue | SBA guidance as quoted by Synovus and Constant Contact (the SBA page itself was not opened) |
| Large-company reference | 7.7% of revenue (7.8% in 2026) | Gartner CMO Spend Survey 2025 |
| Survey average | 9.0% of revenue | The CMO Survey (Duke, Deloitte, AMA), January 2026 |
| Share spent on social | 14% of the marketing budget (26.7% in consumer services) | The CMO Survey 2026 |
| Conservative rule | US$500 a month = US$6,000 a year = 5% of US$120,000 | arithmetic |

**Minimum:** known revenue of **US$10,000 a month (US$120,000 a year)**. Below that the lead is rejected.
**Preferred:** US$15,000 a month or more (room for ad spend on top of the fee). This is the existing Mid band.
**Social floor:** at least **1 post (or upload) in the last 30 days**. **Active:** 4 or more (about one a week). Industry studies put healthy brands at 12-18 posts a month (Buffer, Hootsuite).

Facts only. Revenue is never guessed. It is known only when the review-velocity formula has the data (reviews per month x ticket size from the `Niches` tab). When it is unknown the lead stays and the sheet shows `?`, not a tick. Social activity is known only when Instagram stats (Meta token or Apify) or the YouTube API supply it; otherwise it also shows `?`.

## What Was Not Good In Version 5, And What Version 6 Does
| Problem in the old code | Old behaviour | New behaviour |
|---|---|---|
| A broken or unshared sheet in the setup and finish jobs | Printed an error, job stayed green, Master Dashboard silently skipped it | Other sheets still run, then the job ends **red** and names the failed sheets |
| One sheet stopping hard (bad key, old-sheet check) | Aborted every sheet after it | Only that sheet stops |
| Aliases `SHEET_ID_UK` and `SHEET_ID_YT` | Documented, but the workflow never passed them, so the country was silently skipped | Passed through |
| Phones | Stored as the source gave them, possibly `+61...` or `+1...` | Cleaned with python-phonenumbers: national format for the lead's own country, country code **without a plus** for foreign numbers; junk dropped |
| Cells starting with `=`, `+` or `@` | Safe only in the raw-write path | Leading characters stripped in every path |
| Emails like `name+tag@site.com` | Kept | Rejected (not a real mailbox); syntax checked with email-validator |
| Link-in-bio pages (Linktree and similar) | Could end up as the Website | Never. The creator's own site is taken from the page: a link printed on their own page is theirs, unless it is a social, shop or link-in-bio host |
| Structured data on the site | Ignored | JSON-LD and microdata (`sameAs`, `email`, `telephone`) are read with extruct, so social links and contacts the site itself declares are captured |
| Facebook page | Only the link was kept | The public page is read for email, phone and website (see the limits below) |
| 429 / 503 from a website | The page was skipped | Retried 3 times with backoff (tenacity) |
| 403 from a website | The page was skipped | One more try with Scrapling (browser-grade TLS and headers). robots.txt is still obeyed |
| Same business from two sources | Only exact Place Id matched | Same phone number, or same registered domain plus a near-identical name (RapidFuzz and tldextract), is dropped. Chain branches with different phones stay |
| Qualification checklist | Score only | New `Benchmark Check` column: tick = proven by a fact, cross = a fact says no, `?` = cannot be checked from public data |
| Unpinned libraries | A future release could break a run | Versions pinned to the ones that passed the tests |
| Test counts in the docs | 92 unit tests | 114 |

## What Was Good And Is Kept
- Append-only sheets (rows are never sorted, edited or deleted; your `Status` and `My Notes` are safe).
- Facts-only rule: decision makers and emails are only what a page, a LinkedIn result or an API printed.
- Free first: OpenStreetMap, website reading, free map data. Every paid key stays optional and a bad key never crashes the bot.
- One Google Sheet per country plus the YouTube sheet, Master Dashboard, Stats, Lead Insight, Segment and ICP score.
- The sheet contract for the outreach bot (`docs\CONTRACT.md`): all existing columns unchanged.

## Libraries And Tools Added
| Name | Used for | Licence |
|---|---|---|
| python-phonenumbers | Clean phone numbers | Apache-2.0 |
| tenacity | Retry with backoff | Apache-2.0 |
| extruct | Read JSON-LD and microdata | BSD-3-Clause |
| email-validator | Email syntax | Unlicense |
| RapidFuzz | Fuzzy business-name match | MIT |
| tldextract | Registered domain | BSD-3-Clause |
| Scrapling | Second try when a site answers 403 | BSD-3-Clause |
| gosom/google-maps-scraper (external, optional) | Big lists of Google Maps businesses, saved as CSV into `app\imports\` | MIT |
| theHarvester (external, optional) | Extra public emails for a domain, pasted into an import CSV | GPL-2.0, run as a separate program, never copied into the code |

Safety scan verdicts (2026-11-11, reports in `F:\Github Repos\scans\`, log in `F:\Github Repos\SKILLS-REGISTRY.md`): python-phonenumbers, tenacity, extruct, email-validator, RapidFuzz and tldextract are **SAFE** (their flagged lines were test samples, docs and CI files). Scrapling, theHarvester and gosom/google-maps-scraper are **CAUTION**: Scrapling has anti-bot features, so it is used only for one retry after a 403 on pages robots.txt allows; theHarvester (GPL) and gosom (Google terms, default telemetry) are not installed in the bot and run only if you choose to. You asked for all of them, so Scrapling is installed. Two scans (phonenumbers and gosom) ran on trimmed code-only copies because the full repos timed out.

## Honest Limits
- **Facebook:** Facebook's robots.txt asks automated tools to stay away, and the bot obeys it, so a direct read usually returns nothing. Email and website from Facebook therefore come mostly from the business's own website footer and structured data. The Facebook reader is switched on (`READ_FACEBOOK_PAGES` in the `Rules` tab) and works on any page that is reachable. Bypassing a login wall or robots.txt would break Facebook's terms and risk a ban, so it is not done.
- **Google Maps scraping** (gosom) breaks Google's terms and Google may block the IP. It runs on your PC, not on GitHub, and is optional.
- **Instagram and Facebook activity** cannot be read without an Instagram token or Apify key. Without one the sheet shows `?` for activity.
- **LinkedIn:** only profile links that appear on the business's own pages or in search results. Nothing is logged into or scraped.
- **Email rules by country:** UK and Ireland (GDPR and PECR) treat `firstname@` mailboxes of sole traders as personal data; Canada (CASL) is the strictest. Prefer company addresses and keep an opt-out in every message. Not legal advice.
