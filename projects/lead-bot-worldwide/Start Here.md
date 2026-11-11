# Start Here

Lead Bot Worldwide, version 6. Read this page top to bottom. Nothing in it needs coding. Never paste a key or password into chat.

## What It Does
Finds local businesses in the United States, Canada, United Kingdom, Australia, New Zealand and Ireland (optional: United Arab Emirates, Saudi Arabia, Qatar) plus YouTube creators, keeps only those that pass the benchmark below, and writes one row per lead into one Google Sheet per country.

Each row has: company name, niche, decision maker name, first name, role, personal / generic / other emails (with a verified flag), phone, Instagram, Facebook, LinkedIn, TikTok, YouTube, Twitter / X, other socials, website, full address, city, state, postcode, country, a Lead Insight, Segment, ICP score and the new **Benchmark Check**. It never writes outreach emails (your outreach bot does).

## The Benchmark A Lead Must Pass
| Check | Rule | How it is known |
|---|---|---|
| Can pay US$500 a month | Revenue of at least US$10,000 a month (US$120,000 a year) when the revenue is known | Review count and review growth x average ticket from the `Niches` tab. Unknown revenue is never guessed; the row shows `?` |
| Posts on social | At least 1 post or upload in the last 30 days | Instagram stats (Meta token or Apify) and the YouTube API. Unknown shows `?` |
| Active | 4 or more posts in 30 days (preferred) | Same |
| Reachable | An email, or at least a social profile | The business's own pages |
| Decision maker | A named owner, founder or director, if one is printed anywhere public | Page text, LinkedIn search result, YouTube description |
| Overall | ICP score 7 out of 10 or more | The existing score |

Change any number in the sheet's `Rules` tab (`MIN_MONTHLY_REVENUE`, `MIN_POSTS_30D`, `PREFERRED_POSTS_30D`, `MIN_ICP_SCORE`). No code needed. The reasoning and sources are in `What Changed.md`.

Reading the `Benchmark Check` column: a tick means a fact proves it, a cross means a fact says no, and `?` means public data cannot show it. Do not treat `?` as a failure.

## Where It Runs
| Part | Where | Cost |
|---|---|---|
| The daily robot | **GitHub Actions** (cloud, 20:00 and 08:00 UTC, every day) | Free on a public repo |
| The lead lists | **Google Sheets**, one per country | Free |
| Test runs, edits | **Your Windows PC** (`install\run-local.ps1`), writes CSV files to `app\local_sheet\` | Free |
| Optional big lists from Google Maps | **Your PC**, run the gosom scraper yourself (see "Optional Extras") | Free |

## What You Need
| Item | Required? | Where |
|---|---|---|
| Google account | Yes | accounts.google.com |
| GitHub account | Yes | github.com |
| Google robot key (JSON) | Yes | Step 2 |
| Optional keys (AI, Serper, YouTube, Hunter, Apify...) | No, each adds quality | `Secrets Guide` in `app\` |

## Step By Step
### Step 1. Install on this PC (2 minutes)
1. Open the `install` folder.
2. Double-click `INSTALL.cmd`. Click **Yes** if Windows asks.
3. When it asks for a key or sheet id, paste it (nothing shows while you type) and press Enter, or press Enter to skip.
4. You should see only `OK` lines. To re-check any time, run in PowerShell inside `install`:
```
.\INSTALL.cmd -Check
```

### Step 2. Make the Google robot (10 minutes, once)
Follow `app\Google And GitHub Setup.md`, Step 1: Google Cloud, new project, enable **Google Sheets API** and **Google Drive API**, Service Accounts, Create, Keys, Add key, JSON. Keep the file in the `secrets` folder.

### Step 3. Make the sheets
1. In Google Sheets create one blank sheet per country: US, CA, GB, AU, NZ, IE (optional AE, SA, QA) and one for YouTube.
2. For each sheet click **Share**, paste the robot's email (the `client_email` inside the JSON file, ends in `.iam.gserviceaccount.com`), choose **Editor**.
3. Copy each sheet id: the long text between `/d/` and `/edit` in its address.

### Step 4. Put the code on GitHub
1. Create an empty **public** repository on github.com (public gives unlimited free minutes; the repo holds only code, keys never go in).
2. In PowerShell run, replacing the two names:
```
cd "F:\Github Repos\projects\lead-bot-worldwide\app"
```
```
git remote add origin https://github.com/YOUR-GITHUB-USER/YOUR-REPO-NAME.git
```
```
git push -u origin main
```
(Use `master` instead of `main` if `git branch` shows `master`.)

### Step 5. Add the secrets
In the GitHub repo: **Settings, Secrets and variables, Actions, New repository secret**. Add:
- `GOOGLE_SA`: the whole text of the JSON key file.
- `SHEET_ID_US` (required, it also holds the Master Dashboard), then `SHEET_ID_CA`, `SHEET_ID_GB`, `SHEET_ID_AU`, `SHEET_ID_NZ`, `SHEET_ID_IE`, `SHEET_ID_YOUTUBE`, and optionally `SHEET_ID_AE`, `SHEET_ID_SA`, `SHEET_ID_QA`.
- Any optional keys you have.

### Step 6. Try it on your PC first (recommended)
Double-click the Desktop shortcut **Lead Bot Worldwide (local test)**. Open `app\local_sheet\US\`. Check 5-10 rows: names, emails, phones (no leading plus), social links, `Benchmark Check`. Press Ctrl+C to stop.

### Step 7. First cloud run
GitHub repo, **Actions**, **Run Lead Bot**, **Run workflow**. Expect green ticks for `setup`, each `collect`, and `finish`. A country with no sheet secret prints `SKIP` and is still green. A **red** job now means a real problem (for example a sheet not shared with the robot): open the log, the last lines name the failed sheet.

### Step 8. Work the leads
Open the Google Sheets. Filter `Segment` (PRIME first) and `Tier` (A first), read `Lead Insight` and `Benchmark Check`, then pass the row to your outreach bot. Never sort, delete or insert rows (the bot only appends); use the filter feature instead.

## How Many Leads A Day
- Hard ceiling: 120 new leads per job per run, 10 jobs, 2 runs a day, which is 2,400. This is a limit, not a forecast.
- The real number depends on the quality gates, how many free map results each area has, and your optional keys. It has not been measured on live Google Sheets. Judge after 2 to 3 days and read the `Stats` tab and `Run Log`.
- Free mode finds fewer decision makers and personal emails (about 20 to 35 percent per the earlier notes). Adding Serper, Hunter, Prospeo or Snov raises that.

## Private Repo Warning
Ten jobs twice a day use about 900 runner-minutes a day. A private repo has a much smaller free allowance, so set the repository variable `LEAD_MATRIX` to `{"include":[{"name":"us","country":"US"}]}` and delete the second `cron` line in `.github\workflows\run-lead-bot.yml`. GitHub also pauses scheduled runs on a public repo after 60 days without a commit; push any small change to wake it.

## Optional Extras
- **Google Maps scraper (gosom/google-maps-scraper):** run it on your PC, save its CSV into `app\imports\` named `Niche name__anything.csv`. The bot imports it through the same quality gates. Google may block the scraper (terms of service), so keep volumes small. Set `DISABLE_TELEMETRY=1` before running it (it reports usage to PostHog by default), and run it with `-input queries.txt -results out.csv -email`.
- **theHarvester:** run it separately for a domain; paste the emails into an import CSV with the columns `website` and `emails`.
- **Facebook emails:** read from the public page when reachable. Facebook usually blocks automated reads, so most emails come from the business website. A ZenRows key does not change that, because robots.txt is still obeyed.

## When Something Looks Wrong
See `Guide\Troubleshooting.md`. Common causes: sheet not shared with the robot email, a secret pasted with extra spaces, a daily free-key limit (the bot then writes fact-only insights, which is normal).

## Files
| File | What |
|---|---|
| `Start Here.md` | This page |
| `What Changed.md` | What version 6 changed and why, with sources |
| `Setup Guide.md` | Longer setup notes |
| `Guide\` | Roadmap, architecture, how to change things, accounts and keys |
| `app\` | The code |
| `docs\CONTRACT.md` | The sheet interface your outreach bot reads |
