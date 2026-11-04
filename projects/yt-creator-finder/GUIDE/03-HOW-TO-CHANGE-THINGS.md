# 03 How to change things

Two places hold settings: `app\config.yaml` (needs a push to GitHub to affect the cloud run) and GitHub Variables (take effect on the next run, no push). A GitHub Variable or environment variable with the UPPER_CASE name of a config key overrides the file (`src\config.py`, `load`). Empty values are ignored. Never put secrets in `config.yaml`.

Rule before editing anything in `app\`: make sure no other session is working there. After editing, test, commit inside `app\`, then push (push only when you decide to).

## Quick table
| I want to... | Setting | Where |
|---|---|---|
| Minimum subscribers (default 15000) | `min_subs` / `MIN_SUBS` | config.yaml or Variable |
| Max subscribers (0 = none) | `max_subs` | config.yaml |
| Channel must have uploaded within N days (21) | `max_days_since_upload` / `MAX_DAYS_SINCE_UPLOAD` | either |
| Cap leads per day (0 = no cap) | `daily_lead_target` / `DAILY_LEAD_TARGET` | either |
| Fewer YouTube quota units | `yt_search_budget` / `YT_SEARCH_BUDGET` (searches per run, 100 units each) | either |
| Keep more quota in reserve | `yt_units_reserve` (1500) | config.yaml |
| Make PRIME harder or easier | `prime_score` (7), `growing_score` (5) | config.yaml |
| Write only better leads | `min_score_to_write` (3) | config.yaml |
| Which countries earn +2 points | `tier1_countries` | config.yaml |
| Turn a source off | `use_ytjobs`, `use_upwork`, `use_linkedin`, `use_freelancer`, `use_remotive`, `use_web_search`, `use_youtube_hiring_search`, `use_youtube_niche_search` set to `false` | config.yaml |
| AI models | `gemini_models`, `groq_models` (wrong names are skipped, a current model is auto-picked) | config.yaml or `GEMINI_MODELS` / `GROQ_MODELS` |
| Run times | `cron` line | workflow file |

## Recipes

**1. Get more leads (lower the bar)**
1. Open `app\config.yaml`.
2. Lower `min_subs` (for example 15000 to 5000) and raise `max_days_since_upload` (21 to 45).
3. Or, without a push: GitHub repo > Settings > Secrets and variables > Actions > Variables > New repository variable, name `MIN_SUBS`, value `5000`.

**2. Cap leads while testing**
Manual run: Actions tab > "YT creator lead bot" > Run workflow > `max_leads` 10. Local:
```
app\.venv\Scripts\python.exe -m src.leadbot --dry-run --max-leads 10
```
Run it from inside `app`. `--export file.csv` also saves the dry-run leads as a CSV.

**3. Change search phrases or niches**
In `config.yaml` edit the lists `upwork_queries`, `linkedin_queries`, `freelancer_queries`, `web_search_queries`, `youtube_hiring_queries`, `niche_queries`. Put best niches first. `linkedin_pages_per_country` (2) and `linkedin_detail_max` (60) limit how much LinkedIn is read; keep them small.

**4. Change what counts as "hiring"**
Edit the regex lines `hiring_regex`, `thumbnail_regex`, `editing_regex` (case-insensitive). `freelancer_regex` rejects channels of freelancers looking for work. Test with the offline tests after editing.

**5. Change run times**
1. Open `app\.github\workflows\run-lead-bot.yml`.
2. Edit `cron: "17 1,4,7,10,13,16 * * *"`. Hours are UTC; Pakistan time = UTC + 5. Example: 08:00 PKT = `0 3 * * *`.
3. Commit and push. GitHub cron may start a few minutes late.

**6. Pause or resume the bot**
GitHub > Actions > "YT creator lead bot" > the `...` menu > Disable workflow (or Enable workflow).

**7. Add a lead source**
1. Create `app\src\sources\mysource.py` with a `collect(...)` function returning a list of candidates (copy `remotive.py`, the smallest, and see `sources\common.py` for the Candidate fields).
2. In `src\leadbot.py` add `from .sources import mysource`, add a `use_mysource` line with `add("mysource", mysource.collect, ...)` next to the others in `run`, and add the name to `SOURCE_RANK`.
3. Add `use_mysource: true` in `config.yaml`. Also add it to `DEFAULTS` in `src\config.py` so it is on when config.yaml cannot be read (optional).
4. Add a test in `app\tests\` and run the tests (recipe 9).

**8. Add or rotate a key**
Update the line in `secrets\.env` AND the GitHub secret with the same NAME. Then copy to `app\.env`: re-running `install\INSTALL.cmd` does this. Several keys for one name are separated by commas (YouTube, Gemini, Groq) to multiply quota.

**9. Run the tests**
```
cd app
```
```
.venv\Scripts\python.exe -m pytest -q
```
Expected: a line like `22 passed` (count per `app\CLAUDE.md`; not re-run in this step).

**10. Block a person or company**
In the Sheet tab `Blacklist` add a row: `Channel_ID`, `Email` or `Domain`. The bot reads it on every run. Setting a lead's `Status` to `Do-Not-Contact` is only for your own tracking; the bot never overwrites `Status`.

**11. Change the AI model**
Edit `gemini_models` / `groq_models` in `config.yaml`. Do not hard-code names in `ai_insight.py`.

**12. Reset the YTJobs position (re-read old jobs)**
Edit the hidden `_State` tab in the Sheet (right-click a tab > Show, or View > Hidden sheets), delete the row `ytjobs_cursor`. The next run back-fills `ytjobs_backfill` (120) IDs. Hide the tab again afterwards. Not tested live (no real Sheet has been used yet).
