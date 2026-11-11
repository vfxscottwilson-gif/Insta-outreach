# Handoff: Lead Bot Worldwide (2026-11-11)

## 1. Created Or Changed (paths under `F:\Github Repos\projects\lead-bot-worldwide\`)
- `app\src\clean.py` (new): phones without a plus, link cleanup, JSON-LD and Facebook facts, duplicate check, Benchmark Check text.
- `app\src\enrich.py`: retry on 429/503 (tenacity), Scrapling retry on 403, structured data, Facebook page read, relaxed link-in-bio site pick, `+tag` emails rejected.
- `app\src\leadbot.py`: phone cleanup, activity gate, revenue floor gate, `Benchmark Check` column, duplicate drop, Website shown as site root, `--all` jobs exit non-zero when a sheet fails, `cell()` formula guard.
- `app\src\quality.py`, `app\src\defaults.py`: `Below Floor` revenue band; Rules `MIN_MONTHLY_REVENUE` 10000, `MIN_POSTS_30D` 1, `PREFERRED_POSTS_30D` 4, `READ_FACEBOOK_PAGES`; new column `Benchmark Check`.
- `app\.github\workflows\run-lead-bot.yml`: passes `SHEET_ID_UK` and `SHEET_ID_YT`.
- `app\requirements.txt`: pinned, plus phonenumbers, tenacity, extruct, email-validator, RapidFuzz, tldextract, scrapling[fetchers].
- `app\tests\test_v6.py` (new), edits in `app\tests\test_v4.py` and `app\tests\test_free_tools.py`.
- Docs renamed to Title Case: `Start Here.md` (new), `What Changed.md` (new), `Setup Guide.md`, `Read Me.md`, `Guide\*.md`, `docs\Free Tools Research.md`, `docs\High Quality Leads Spec.md`, `app\Google And GitHub Setup.md`, `app\Secrets Guide.md`, `app\Sheets Setup.md`, `app\Upgrade V2-V5.md`. `PROGRESS.md` and both `CLAUDE.md` files updated.
- Outside the project: `F:\Github Repos\SKILLS-REGISTRY.md` (10 rows), `F:\Github Repos\scans\`, `F:\Github Repos\repos\` (cloned vetting copies).

## 2. Finished And Verified
- 114 unit tests and the selftest pass (run in `app\.venv`).
- Local pilot, US, 3-minute cap: 5 leads, phones with no plus, benchmark column present.
- Committed in `app` as `7ff56d6` (local only, not pushed). Safety scans: six libraries SAFE; Scrapling, theHarvester, gosom CAUTION (see `What Changed.md`).

## 2b. Added After The First Handoff
- `Lead Bot Worldwide v6.zip` (project root, 67 files, extracted and 114 tests pass, no secrets). Next delivery must be `Lead Bot Worldwide v7.zip`; older zips go to `Archive\`.
- Release naming rule saved as section 14 of the global `CLAUDE.md` and memory file `release-zip-naming-rule.md`; sent to 9 automation chats.

## 3. Not Done Or Not Verified
- Live Google Sheets and the GitHub Actions run (need the user's logins).
- Top folder is still named `lead-bot-worldwide`; rename to `Lead Bot Worldwide` when no session is inside it, then fix the paths in the project and global CLAUDE.md files.
- `Start Here.md`, `What Changed.md`, `PROGRESS.md`, `CLAUDE.md` edits at the project root are not under the `app` git (only `app` is committed).
- Benchmark thresholds are not back-tested on real leads; the SBA source was secondhand.
- Revenue and social activity show `?` without review counts and an Instagram token or Apify key.
- theHarvester wrapper (domain and emails CSV) not written.

## 4. Exact Next Step
User follows `Start Here.md` steps 2 to 5 (Google robot key, sheets shared with the robot email, GitHub repo, secrets), then runs the workflow once and checks the `Stats` tab and `Benchmark Check` column after 2 to 3 runs.
