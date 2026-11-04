# 03 How to change things (recipes)

Two places hold settings, and mixing them up is the number one mistake:

| Where | What lives there | Takes effect |
|---|---|---|
| **The Google Sheet** (tabs `Rules`, `Niches`, `Locations`, `Options`) | scoring, limits, niches, search words, suburbs | next run, no push needed |
| **The code** (`app\src\defaults.py`, `app\.github\workflows\run-lead-bot.yml`) | first-run defaults, schedule, which jobs exist | after you commit and push `app\` to GitHub |

`defaults.py` only seeds a sheet the first time: `load_config()` in `leadbot.py` appends Rules or Niches that are MISSING and never overwrites a row that exists. Changing a value in `defaults.py` does not change an existing sheet. Edit the sheet.

Try any change first without Google (writes CSV files to `app\local_sheet\`):

```
powershell -ExecutionPolicy Bypass -File "F:\Github Repos\projects\lead-bot-au\install\run-local.ps1" --local
```

## Recipe 1: change the score threshold

1. Sheet tab **Rules**, row `MIN_ICP_SCORE` (default `7`): leads below this ICP score out of 10 are not added.
2. Change the **Value** cell, for example `7.5`. Next run uses it. Fewer, better leads.
3. Related rows: `TIER_A_ICP` (8.5), `TIER_B_ICP` (7.5), `PRIME_R_MIN` (7), `PRIME_S_MAX` (4), `MIN_REVIEWS` (8), `MAX_REVIEWS` (600), `MIN_RATING` (3.5), `MIN_BUDGET_AUD` (500).
4. Column C of each Rules row explains it in plain English.

## Recipe 2: change which states / areas are searched

1. Sheet tab **Locations**: columns Country, State, City, Search Area, Enabled (Yes/No), Priority (1-3), Latitude, Longitude, Radius km. 73 Australian areas are seeded.
2. Disable an area: `Enabled` = `No`. Add one: a new row with latitude, longitude, radius.
3. Which job searches which state is set in the workflow matrix (`regions`, for example `AU-NSW,AU-ACT`). To move a state to another job, or to search fewer states, set GitHub Variable `LEAD_MATRIX` (Settings > Secrets and variables > Actions > Variables). Example that searches only NSW and Victoria:

```
{"include":[{"name":"nsw","regions":"AU-NSW","sources":"input,maps"},{"name":"vic","regions":"AU-VIC","sources":"maps"}]}
```

`sources` can contain `input, imports, maps, youtube`. Keep `max-parallel: 1` in the workflow: all jobs write one sheet.

Other countries are not supported by this edition (rows from other countries are skipped on import). Use the worldwide bot for that.

## Recipe 3: change search queries and niches

1. Sheet tab **Niches**, one row per niche (31 are seeded). Edit `Search Terms (separate with ;)` and `Free Map Selectors (OSM, separate with ;)`.
2. Switch off: `Enabled (Yes/No)` = `No`. Do not delete default rows; missing defaults are added back on the next run.
3. A niche is skipped when `Budget Low AUD` is under Rules `MIN_BUDGET_AUD`.
4. New niche = new row; its lead tab appears with the first lead. Avoid `[ ] * ? : / \` in the name; max 90 characters.
5. Per-niche filters: `Exclude Name Words`, `Must Match On Website (regex)`, `Reject If Website Matches (regex)`. A bad regex is reported in the run problems and ignored.

## Recipe 4: change the schedule

1. Edit the two lines under `schedule:` in `app\.github\workflows\run-lead-bot.yml` (UTC):

```
    - cron: "0 19 * * *"
    - cron: "0 7 * * *"
```

2. Commit and push:

```
cd "F:\Github Repos\projects\lead-bot-au\app"
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

3. Private repo: delete the second cron line (see the comment at the top of the workflow file).
4. Sydney clock changes with daylight saving but cron is fixed UTC, so the Sydney hour shifts by one.

## Recipe 5: change sheet columns

- No code: reorder columns or add your own in the sheet. The bot and the outreach bot find columns by header name (`CONTRACT.md` section 3). Keep `Place Id`, `Company Name`, `Status` as they are. Sort or filter only with Data > Filter views, never Sort range.
- A new column the bot should fill: add the header name to `LEAD_H` (or `AU_COLS` for Australian-only fields) in `app\src\defaults.py`, then set the value where the row is built in `app\src\leadbot.py` (search `"Pitch Angle": pitch_line`, around line 1108). Existing tabs get the new header appended at the END of row 1 on the next run (`ensure_headers`). Run the tests (Recipe 7).
- Changes the outreach bot reads must be recorded as a new version line in `app\CONTRACT.md`.

## Recipe 6: add a data source

No code: save a scraper export (for example the gosom Google Maps scraper) as CSV or JSON in `app\imports\`, or paste the rows with their header into the sheet tab **Import**. Name the file `Niche Name__anything.csv` to pick the niche. Details: `app\imports\README.md`. The `imports` job processes them. Warning: files in `imports\` are public in a public repo; use the Import tab.

With code (developer job): write a function returning the same "place dictionaries" as `osm.py`/`yt.py`, call it where `leadbot.py` chooses sources (search `use_osm`), and add the source name to `SOURCES`. Add an offline test in `app\tests\`.

## Recipe 7: other everyday changes

| I want to | Do this |
|---|---|
| Add or change a key | `secrets\.env` (this PC) AND GitHub > Settings > Secrets and variables > Actions. Names: `GUIDE\05-ACCOUNTS-AND-KEYS.md` |
| Fill the 8 Australian ABN columns better | register the free GUID at abr.business.gov.au (Web Services), add secret `ABN_GUID` |
| Run now on GitHub | Actions > "Run AU Lead Bot" > Run workflow |
| Run the tests | `cd app` then `.venv\Scripts\python.exe src\selftest.py` and `.venv\Scripts\python.exe -m unittest discover -s tests` |
| Back up | `powershell -ExecutionPolicy Bypass -File backups\backup.ps1` |
| Remove the Desktop shortcut | `install\INSTALL.cmd -Uninstall` (only the shortcut) |
| Stop the daily run | GitHub > Actions > "Run AU Lead Bot" > ... menu > Disable workflow |

Never sort or delete rows in a lead tab.
