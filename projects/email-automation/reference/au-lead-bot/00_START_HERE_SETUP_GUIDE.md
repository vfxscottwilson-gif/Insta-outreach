# START HERE: Setup Guide (v5, about 30-45 minutes, $0)

This bot finds businesses in the US, Canada, UK, Australia, New Zealand and Ireland (optional: UAE, Saudi Arabia,
Qatar) that can pay you $500 to $1,000+ per month, plus YouTube creators who can pay $1k-2k.

**What it does for each business:**
1. Finds the public emails, phone, social links and decision-maker name. Facts only: a name is used only when it is
   printed on their site or in a public LinkedIn result title.
2. Checks the emails and scores the lead.
3. Writes a short **Lead Insight**: who they are and their likely pains.
4. Adds the lead to that country's Google Sheet, one tab per niche, always below the last row.

It runs by itself twice a day on GitHub. **It never writes emails.** Your outreach bot does that (`CONTRACT.md`).

---

## A. What every file is

```
au-lead-bot/
├── 00_START_HERE_SETUP_GUIDE.md   <- THIS FILE
├── SHEETS_SETUP.md                <- the sheets, one per country (create + share)
├── SECRETS_GUIDE.md               <- every GitHub secret: name, format, where to get it, free limit
├── UPGRADE_V5.md                  <- what changed in v5 (+ tests, risks)
├── README.md, requirements.txt, .gitignore
├── .github/workflows/run-lead-bot.yml   <- THE FILE THAT RUNS THE AUTOMATION
├── src/                           <- the code (you never edit it)
│   ├── leadbot.py   main program        ├── keys.py      secret checks + registration report
│   ├── insight.py   Lead Insight        ├── quality.py   segments (PRIME, GROWING, ...)
│   ├── enrich.py    website reader      ├── optional.py  optional paid/free helpers
│   ├── osm.py       free map            ├── yt.py        YouTube (no key needed)
│   ├── ai.py        AI keys failover    ├── places.py    Google Places (optional, billing)
│   ├── importer.py  scraper imports     ├── localsheet.py offline sheet for tests
│   ├── defaults.py  first-run tab contents  ├── score.py, market.py, selftest.py
└── tests/                         <- offline tests (the workflow runs them first)
```

---

## B. Setup, step by step

### Step 1. Create the Google "robot account" (GOOGLE_SA), 10 minutes
1. **Create a project:** go to console.cloud.google.com → project picker → **New Project** → "lead-bot" →
   **Create**.
2. **Enable the APIs:** **APIs & Services → Library** → enable **Google Sheets API** (and **Google Drive API**).
3. **Create the account:** **IAM & Admin → Service Accounts → Create service account** → name it "lead-bot" →
   **Done**.
4. **Copy its email:** it looks like `lead-bot@lead-bot-123.iam.gserviceaccount.com`. You need it in Step 2.
5. **Download a key:** open the account → **Keys → Add key → Create new key → JSON**. A `.json` file downloads.
   **Keep it private and never upload it to GitHub.**
6. **Copy its text:** open the file in Notepad and select all of it (from `{` to `}`). That whole text is your
   `GOOGLE_SA` value.

### Step 2. Create the sheets and share them, 2 minutes per sheet
Follow **[SHEETS_SETUP.md](SHEETS_SETUP.md)**. In short, for each country you want:
1. Create a blank sheet.
2. **Share** it with the robot email from Step 1.4 as **Editor**.
3. Copy the sheet id from its URL.

Start with `SHEET_ID_US` (the US sheet also holds the **Master Dashboard**), then add the others whenever you like.

### Step 3. Put the files on GitHub, 5 minutes
1. **Create the repo:** github.com → **New repository** → `lead-bot` → **Public** (unlimited free Actions
   minutes; no secret is ever in the files) → **Create**.
2. **Upload:** unzip `au-lead-bot-v5.zip`. In the repo click **Add file → Upload files**, drag in the contents
   (including the `src`, `tests` and `.github` folders) → **Commit changes**.
3. **If `.github` did not upload:** **Add file → Create new file**, name it
   `.github/workflows/run-lead-bot.yml`, then paste that file's text from the zip.

### Step 4. Add the secrets, 5-15 minutes
Go to repo → **Settings → Secrets and variables → Actions → New repository secret**. **One key per secret**, with
the exact names in **[SECRETS_GUIDE.md](SECRETS_GUIDE.md)**.

| Add now | Value |
|---|---|
| `GOOGLE_SA` | the whole JSON text from Step 1.6 |
| `SHEET_ID_US` (+ `SHEET_ID_CA`, `SHEET_ID_GB`, `SHEET_ID_AU`, `SHEET_ID_NZ`, `SHEET_ID_IE`, `SHEET_ID_YOUTUBE`, optional `SHEET_ID_AE` / `SHEET_ID_SA` / `SHEET_ID_QA`) | each sheet's id (or its full URL) |
| `GEMINI_API_KEY_1` (recommended) | aistudio.google.com/apikey → Create API key (`AIza…`) |
| `GEMINI_API_KEY_2`, `GROQ_API_KEY` (optional) | more free AI quota for Lead Insight |
| `SERPER_API_KEY` (best optional upgrade) | serper.dev: Google rating + review counts → PRIME leads |

Everything else is optional. A missing key never causes an error.

### Step 5. First run
1. **Enable workflows:** repo → **Actions**. If asked, click **"I understand my workflows, enable them"**.
2. **Start it:** **Run Lead Bot → Run workflow**.
3. **Watch the jobs:** `setup` runs (tests + tabs), then the `collect (us)`, `collect (ca)`, … jobs, then `finish`.
4. **Check the keys:** open `collect (us)` → "Run the bot". The first lines are the **registration report**.
   Every key you added should say `registered`.
5. **Open the US sheet:** tab 1 is the **Master Dashboard**, tab 2 is **US Stats**, then one tab per niche.
   Each other sheet starts with a **Stats** tab.

From now on it runs by itself at 08:00 and 20:00 UTC.

---

## C. Working the leads (no code ever)

| Tab | What to do |
|---|---|
| **Master Dashboard / Stats** | Totals, leads today, PRIME counts, last run and run health. Updated in place every run. |
| **Niche tabs** | Your leads. New ones always appear **at the bottom**, and rows never move. Use **Status** and **My Notes** freely, add your own columns, or reorder columns. To sort for yourself, use Data → **Filter views** (it doesn't change the real order). |
| **Niches / Locations / Rules** | Switch niches or areas on and off and change thresholds. Every Rules row explains itself. |
| **Leads Input** | Paste businesses you found yourself. The bot enriches and scores them. |
| **Blacklist** | A name, email or website you never want. |
| **Options** | The list of optional services and their status after the last run. |

**How to read a lead:**
- **Segment:** PRIME means contact first. PRIME-REVIEW needs a 1-minute check. GROWING is the second wave.
  HAS-AGENCY means they already have an agency (replacement pitch later).
- **Lead Insight** says who they are and their likely pains. **Pitch Angle** is an opening line idea.
- **Personal Email** reaches a named person. **Generic Email** is info@ and similar.

---

## D. Honest limits of the free version
- **The free map (OpenStreetMap):** it has no Google review counts. Without `SERPER_API_KEY` or Google Places, leads
  are capped at PRIME-REVIEW: check the reviews by hand.
- **Gulf countries:** OSM coverage is thin, so expect few leads there without Serper or Apify.
- **Free AI keys:** they have daily limits. On a 429 the bot stops AI for that run and writes a fact-only Lead
  Insight. Nothing breaks.

## E. Troubleshooting
| You see | Fix |
|---|---|
| `ignored: GEMINI_API_KEY_1 (bad format …)` | Re-paste the key with no quotes or spaces. A provider changed its format? Set the Variable `KEY_CHECK` = `warn`. |
| `SKIP NZ: no SHEET_ID_NZ secret set` | Normal if you don't want that country. Otherwise add the secret. |
| `no access. Share it with the service-account email as Editor` | Share that sheet with the robot email (Step 2). |
| `GOOGLE_SA is not valid service-account JSON` | Paste the whole file content, from `{` to `}`. |
| `SKIP …: another job is writing this sheet right now` | Two runs overlapped. Nothing was written, and the next run continues. |
| `AI quota hit (429)` in Run health | The free AI daily limit was reached. Add `GEMINI_API_KEY_2` / `GROQ_API_KEY`, or ignore it. |
| `ERROR sheet is near Google's 10M-cell limit` | Delete old `Rejected:` rows in the Seen tab (SHEETS_SETUP.md). |
| Green run but 0 leads | Read **Run Log**: it lists every reject reason with counts. |
