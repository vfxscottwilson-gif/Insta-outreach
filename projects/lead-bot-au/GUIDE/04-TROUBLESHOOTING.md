# 04 Troubleshooting

Every message below was taken from the code (`app\src\`), so you can search the log for the exact wording.

## 1. How to read a GitHub Actions run

1. Open your GitHub repo, tab **Actions**, click "Run AU Lead Bot", click the newest run.
2. Jobs: `setup`, then `collect (nsw-act)`, `collect (vic-tas)`, `collect (qld)`, `collect (wa-sa-nt)`, `collect (youtube)`, `collect (imports)` one after another, then `finish`. Green tick = no crash, red cross = failed, grey = waiting or skipped.
3. A green job can still have found nothing. Click the job, then the step "Run the bot (...)" and read from the top:
   - First lines = the **registration report**: `registered: GEMINI_API_KEY_1 (...abcd)` or `ignored: GROQ_API_KEY ...` (values are masked).
   - `SKIP AU: no SHEET_ID_AU_ONLY secret set ...` = the sheet is not configured.
   - Last lines: `Done: <summary>` and `Problems: ...` (everything that went wrong without stopping the run).
4. In the Google Sheet, tab **Run Log** has one row per job (time, summary, search requests, problems). Tab **Stats** shows `health`: `OK` or `N issue(s): ...`.
5. A red `setup` job means nothing else ran: see the first row of section 2.

Because the six collect jobs run one at a time, a full run can take several hours (each job up to about 45 minutes). A new scheduled run waits in the queue for the old one (group `au-lead-bot`).

## 2. Failures seen in the code

| What you see | Cause | Fix |
|---|---|---|
| `setup` red, step "Self-test + unit tests" | the code is broken (a bad edit) | read the failing check; undo your last change in `app\` (`git revert`) |
| `MISSING CORE SETTING: GOOGLE_SA and SHEET_ID (or SHEET_ID_<COUNTRY>) are required` | secret missing or misspelled | GitHub > Settings > Secrets and variables > Actions: add `GOOGLE_SA` and `SHEET_ID_AU_ONLY` (old name `SHEET_ID` also works). Names are exact. Local: use `--local` |
| `GOOGLE_SA is not valid service-account JSON (paste the whole .json file content)` | secret holds only part of the key file | open the .json in Notepad, select all, copy, replace the secret |
| `sheet AU (...abcd) not found or not shared with the service account` or `no access. Share it with the service-account email as Editor` | wrong id, or sheet not shared | sheet > Share > add the `client_email` from the .json as **Editor**; check the id (between `/d/` and `/edit`) |
| `SKIP ...: another job is writing this sheet right now (Meta lock ...)` | a second run or a local run holds the write lock | nothing is written, the next run continues. Locks older than `MAX_RUNTIME_MIN` + 15 = 57 minutes are ignored. Do not run `run-local.ps1` against the real sheet while a GitHub run is going |
| `ignored: <KEY> bad format` or `contains spaces or line breaks` | pasted wrong, with quotes, or two keys in one secret | re-paste ONE key per secret. If the key is right and the provider changed its format, create Variable `KEY_CHECK` = `warn` |
| `AI quota hit (429): AI stopped for this run; remaining leads got a fact-only Lead Insight.` | free AI daily limit used | expected on free keys; add `GEMINI_API_KEY_2`/`_3` from another Google project, or wait a day. Not an error |
| Many `429` / slow Sheets steps | Google allows 60 reads per minute per service account | the bot waits and retries (10, 20, 40, 80, 90 s). Keep the outreach bot under about 20 reads per minute (`CONTRACT.md` section 4) |
| `sheet is near Google's 10M-cell limit` / `WARNING sheet uses ... of Google's 10,000,000 cells` | one sheet holds everything in this edition, so it fills sooner than a per-country sheet; `Seen` grows fastest | the bot stops adding rows at Rules `CELL_LIMIT_STOP` (9,500,000). Trim old rows whose Result starts with `Rejected` in `Seen`, or start a new sheet |
| ABN columns empty | no `ABN_GUID`: only ABNs printed on the website are filled | register the free GUID at abr.business.gov.au (Web Services), add secret `ABN_GUID` (old `ABN_LOOKUP_GUID` works) |
| `All Google Places keys are exhausted, invalid, or billing is not enabled.` | Places key out of quota or billing off | the run falls back to free OpenStreetMap; fix or remove the key |
| `All YouTube keys exhausted or invalid for today.` or YouTube blocks the free reader | quota, or a consent/captcha page | the run continues without YouTube; try tomorrow. Free reader cap: `YT_FREE_MAX_CHANNELS_PER_RUN` |
| `[Enrichment Skipped] <Service> API unavailable` | optional service down, bad key, no credit | harmless; skipped for the rest of the run |
| `SOURCE=places but no PLACES_API_KEYS: free OpenStreetMap used instead.` | Rules `SOURCE` is `places` with no key | set `SOURCE` to `auto` or add the key |
| Job stops after about 42 minutes | Rules `MAX_RUNTIME_MIN` (42) stops it cleanly on purpose | normal; the next run continues |
| Job red after 60 minutes | GitHub job limit hit | lower `MAX_SEARCH_REQUESTS_PER_RUN` or `NEW_LEADS_PER_RUN` in Rules |
| Free map search fails 3 times in a row | OpenStreetMap servers busy (`OSM_FAIL_STOP` = 3) | map searches stop for that run; retry later |

## 3. "It ran green but added 0 rows"

Check in this order:
1. Stats tab `health` and the Run Log "Problems" cell.
2. Rules `MIN_ICP_SCORE` (7): most businesses score lower by design. Rejected ones are written to `Seen` with a Result starting `Rejected`.
3. Rules `REQUIRE_CONTACT` = `email_or_social`: no email and no social link means dropped.
4. Rules `REQUIRE_WEBSITE_OSM` = `Yes`: free-map businesses without a website are skipped. (The AU edition's own live test on 2026-10-31 found 26 of 37 Chatswood dentists had no website in OpenStreetMap; see `app\AU_EDITION.md`.)
5. The niche may be disabled, or below `MIN_BUDGET_AUD`.
6. Everything found was already in `Seen`.
7. The `imports` job finds nothing if `app\imports\` and the `Import` tab are empty; that is normal.
8. Quick local check, no Google needed:

```
powershell -ExecutionPolicy Bypass -File "F:\Github Repos\projects\lead-bot-au\install\run-local.ps1" --local
```

## 4. Installer and PC problems

| Problem | Fix |
|---|---|
| Installer says Python is missing even after installing it | close the window, open a new one, run `INSTALL.cmd` again (PATH refresh) |
| "running scripts is disabled" | start with `INSTALL.cmd`; it bypasses the policy for that run only |
| `MISSING virtual environment` or `MISSING secrets\.env` in `-Check` | normal before the first install; the installer creates them |
| Self-test says `No module named 'requests'` | you used system Python; use `app\.venv\Scripts\python.exe` (the installer creates it) |
| Self-test fails after install | run `INSTALL.cmd` again, then `install\install.ps1 -Check` |

## 5. Other things to know

- GitHub normally pauses scheduled workflows in a repo with no activity for 60 days. General GitHub behaviour, not verified for your repo; if the daily run stops, open Actions and click Enable.
- Not verified: everything that needs your accounts (the GitHub run, the live sheet).

More: `app\00_START_HERE_SETUP_GUIDE.md`, `app\SECRETS_GUIDE.md`, `app\AU_EDITION.md`.
