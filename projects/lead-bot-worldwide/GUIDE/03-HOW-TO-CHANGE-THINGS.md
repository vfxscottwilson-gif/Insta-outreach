# 03 How to change things (recipes)

Two places hold settings, and mixing them up is the number one mistake:

| Where | What lives there | Takes effect |
|---|---|---|
| **The Google Sheet** (tabs `Rules`, `Niches`, `Locations`, `Options`) | scoring, limits, niches, search words, cities | next run, no code change, no push |
| **The code** (`app\src\defaults.py`, `app\.github\workflows\run-lead-bot.yml`) | first-run defaults, schedule, which jobs exist | after you commit and push `app\` to GitHub |

`defaults.py` only seeds a sheet the first time: `load_config()` in `leadbot.py` appends Rules or Niches that are MISSING and never overwrites a row that exists. So changing a value in `defaults.py` does not change an existing sheet. Edit the sheet.

Always try a change first without Google (writes CSV files to `app\local_sheet\`):

```
powershell -ExecutionPolicy Bypass -File "F:\Github Repos\projects\lead-bot-worldwide\install\run-local.ps1" --local --country US
```

## Recipe 1: change the score threshold (how picky the bot is)

1. Open the sheet, tab **Rules**, find `MIN_ICP_SCORE` (default `7`). Leads below this ICP score out of 10 are not added.
2. Change the **Value** cell, for example `7.5`. Done. Fewer, better leads.
3. Related cells in the same tab: `TIER_A_ICP` (8.5), `TIER_B_ICP` (7.5), `PRIME_R_MIN` (7), `PRIME_S_MAX` (4), `MIN_REVIEWS` (8), `MAX_REVIEWS` (600), `MIN_RATING` (3.5), `MIN_BUDGET_AUD` (500).
4. Each Rules row has a plain-English "What it does" in column C.

Use this for one sheet only; each country sheet has its own Rules tab.

## Recipe 2: change countries

Which countries run is decided by two things.

1. Sheet secrets. A country runs only if its secret exists in GitHub (Settings > Secrets and variables > Actions): `SHEET_ID_US, CA, GB, AU, NZ, IE, AE, SA, QA, YOUTUBE`. Remove the secret or leave it unset and that job prints `SKIP` and ends green. This is the easiest on/off switch.
2. Job list. Variable `LEAD_MATRIX` (same page, tab Variables) overrides the default list in `run-lead-bot.yml`. To run only the US and UK, set it to:

```
{"include":[{"name":"us","country":"US"},{"name":"uk","country":"GB"}]}
```

Adding a country that is not in the nine above (`COUNTRIES` in `defaults.py`) means editing `COUNTRIES`, `SHEET_TARGETS`, the `SHEET_ID_XX` line in the workflow `env:` block and the matrix. Not verified end to end: ask for a developer test first.

## Recipe 3: change cities (where it searches)

1. Sheet tab **Locations**. Columns: Country, State, City, Search Area, Enabled (Yes/No), Priority (1-3), Latitude, Longitude, Radius km.
2. Disable an area: set `Enabled` to `No`. Add an area: new row with its latitude, longitude and radius.
3. A country's job only reads rows whose Country matches that sheet.

## Recipe 4: change search queries and niches

1. Sheet tab **Niches**. One row per niche. Edit `Search Terms (separate with ;)` for Google-style searches and `Free Map Selectors (OSM, separate with ;)` for the free map search.
2. Switch a niche off with `Enabled (Yes/No)` = `No`. Do not delete default rows: missing default niches are added back on the next run.
3. A niche is skipped when its `Budget Low AUD` is below Rules `MIN_BUDGET_AUD`.
4. New niche = new row. Its lead tab is created on the first lead. Keep the name free of `[ ] * ? : / \` and under 90 characters.
5. Filters per niche: `Exclude Name Words`, `Must Match On Website (regex)`, `Reject If Website Matches (regex)`. A bad regex is reported in the run problems and ignored.

## Recipe 5: change the schedule

1. Open `app\.github\workflows\run-lead-bot.yml`. Edit the two lines under `schedule:` (times are UTC):

```
    - cron: "0 20 * * *"
    - cron: "0 8 * * *"
```

2. Commit and push `app\`:

```
cd "F:\Github Repos\projects\lead-bot-worldwide\app"
```
```
git add .github/workflows/run-lead-bot.yml
```
```
git commit -m "Change schedule"
```
```
git push
```

3. Private repo: delete the second `cron` line (about 900 runner-minutes a day are needed for two runs, see the comment in the file).
4. GitHub may start scheduled runs a few minutes late. Not verified for your repo.

## Recipe 6: change sheet columns

- Safe, no code: reorder columns or add your own in the sheet. The bot and the outreach bot find columns by header name (`CONTRACT.md` section 3). Do not rename or delete `Place Id`, `Company Name`, `Status`.
- To sort or filter for yourself use Data > Filter views, never Sort range: the bot assumes rows stay where they were written.
- A new column the bot should FILL: add the header name to `LEAD_H` in `app\src\defaults.py`, then set the value where the row is built in `app\src\leadbot.py` (search for `"Pitch Angle": pitch_line`, around line 1108, to find the row dictionary). Existing tabs get the new header appended at the END of row 1 on the next run (`ensure_headers`), so old column positions never move. Then run the tests (Recipe 8).
- Any output change the outreach bot reads must be recorded in `app\CONTRACT.md` as a new version line.

## Recipe 7: add a data source

Easiest, no code: a scraper export.
1. Save the CSV or JSON from your scraper (for example gosom Google Maps scraper) in `app\imports\`, or paste the rows with the header into the sheet tab **Import**.
2. Name the file `Niche Name__anything.csv` to choose the niche, or include a `niche` column. Details: `app\imports\README.md`.
3. Rows then go through the same filters and scoring. Warning: files in `imports\` are public in a public repo; use the Import tab then.

With code (developer job): write a function that returns the same "place dictionaries" as `yt.py`/`osm.py`, call it where `leadbot.py` chooses sources (search for `use_osm`), and add the source name to the `SOURCES` set. Add an offline test in `app\tests\`.

## Recipe 8: other everyday changes

| I want to | Do this |
|---|---|
| Add or change a key | `secrets\.env` (this PC) AND GitHub > Settings > Secrets and variables > Actions (daily run). Name list: `GUIDE\05-ACCOUNTS-AND-KEYS.md` |
| Run now on GitHub | Actions > "Run Lead Bot" > Run workflow |
| Run the tests | `cd app` then `.venv\Scripts\python.exe src\selftest.py` and `.venv\Scripts\python.exe -m unittest discover -s tests` |
| Back up | `powershell -ExecutionPolicy Bypass -File backups\backup.ps1` |
| Remove the Desktop shortcut | `install\INSTALL.cmd -Uninstall` (removes only the shortcut) |
| Stop the daily run | GitHub > Actions > "Run Lead Bot" > ... menu > Disable workflow |

Never sort or delete rows in a lead tab.
