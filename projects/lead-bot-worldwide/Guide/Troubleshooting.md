# 04 Troubleshooting

Every message below was taken from the code (`app\src\`). Quoted texts are the real wording, so you can search the log for them.

## 1. How to read a GitHub Actions run

1. Open your GitHub repo, tab **Actions**, click "Run Lead Bot", click the newest run.
2. The page shows jobs: `setup`, `collect (us)`, `collect (ca)` ... `finish`. Green tick = ended without a crash, red cross = failed, grey = skipped or waiting.
3. A green job can still have found nothing. Click the job, then the step "Run the bot (us)" and read from the top:
   - First lines = the **registration report**: `registered: GEMINI_API_KEY_1 (...abcd)` or `ignored: GROQ_API_KEY ...`. This tells you which keys the bot accepted (values are masked).
   - `SKIP US: no SHEET_ID_US secret set ...` = that sheet is not configured.
   - Last lines: `Done: <summary>` and `Problems: ...` (everything that went wrong but did not stop the run).
4. In the Google Sheet, tab **Run Log** has one row per job (time, summary, search requests, problems). Tab **Stats** shows `health`: `OK` or `N issue(s): ...`.
5. If the red job is `setup`, nothing else ran: see section 2, row "setup failed".

## 2. Failures seen in the code

| What you see | Cause | Fix |
|---|---|---|
| `setup` job red, step "Self-test + unit tests" | the code is broken (a bad edit) | open the step log, read the failing check; undo your last change in `app\` (`git revert`) |
| `MISSING CORE SETTING: GOOGLE_SA and SHEET_ID (or SHEET_ID_<COUNTRY>) are required` | secret missing or misspelled | GitHub > Settings > Secrets and variables > Actions: add `GOOGLE_SA` and `SHEET_ID_US`; names are exact and case sensitive. Local: use `--local` |
| `GOOGLE_SA is not valid service-account JSON (paste the whole .json file content)` | the secret holds only part of the key file | open the .json in Notepad, select all, copy, replace the secret |
| `sheet US (...abcd) not found or not shared with the service account` or `no access. Share it with the service-account email as Editor` | wrong id, or sheet not shared | open the sheet > Share > add the `client_email` from the .json as **Editor**; check the id (between `/d/` and `/edit`) |
| `SKIP <country>: no SHEET_ID_... secret set` | secret not created | harmless; add the secret if you want that country |
| `SKIP ...: another job is writing this sheet right now (Meta lock ...)` | a second run or a local run holds the sheet's write lock | nothing written, the next run continues; if it repeats for many runs, a run was killed: wait: a lock older than `MAX_RUNTIME_MIN` + 15 = 57 minutes is ignored |
| `ignored: <KEY> bad format` or `contains spaces or line breaks` | pasted wrong, with quotes, or two keys in one secret | re-paste ONE key per secret. If the key is right and the provider changed its format, create Variable `KEY_CHECK` = `warn` |
| `AI quota hit (429): AI stopped for this run; remaining leads got a fact-only Lead Insight.` | free AI daily limit used up | expected on free keys; add `GEMINI_API_KEY_2`/`_3` from another Google project, or wait a day. Not an error |
| Many `429` / slow steps on Google Sheets | Google allows 60 reads per minute per service account, shared by all jobs | the bot waits and retries (10, 20, 40, 80, 90 s). Do not run extra jobs at the same time; keep the outreach bot under about 20 reads per minute (`CONTRACT.md` section 4) |
| `sheet is near Google's 10M-cell limit` / `WARNING sheet uses ... of Google's 10,000,000 cells` | the sheet is nearly full (the `Seen` tab grows fastest) | the bot stops adding rows at Rules `CELL_LIMIT_STOP` (9,500,000). Trim old rows with Result `Rejected` in `Seen`, or start a new sheet |
| `All Google Places keys are exhausted, invalid, or billing is not enabled.` | Places key out of quota or billing off | the run falls back to free OpenStreetMap; fix the key or leave it empty |
| `All YouTube keys exhausted or invalid for today.` or YouTube blocks the free reader | YouTube quota or consent/captcha page | the run continues without YouTube; try tomorrow. The free reader is capped by `YT_FREE_MAX_CHANNELS_PER_RUN` |
| `[Enrichment Skipped] <Service> API unavailable` | optional service down, bad key, no credit | harmless; that service is skipped for the rest of the run |
| `SOURCE=places but no PLACES_API_KEYS: free OpenStreetMap used instead.` | Rules `SOURCE` is `places` but no key is set | set `SOURCE` to `auto` or add the key |
| Job ends after about 42 minutes with fewer leads than expected | Rules `MAX_RUNTIME_MIN` (42) stops it cleanly on purpose | normal; the next run continues |
| Job red after 60 minutes | GitHub job limit hit | lower `MAX_SEARCH_REQUESTS_PER_RUN` or `NEW_LEADS_PER_RUN` in Rules |
| Free map search fails 3 times in a row | OpenStreetMap servers busy (Rules `OSM_FAIL_STOP` = 3) | map searches stop for that run; retry later |

## 3. "It ran green but added 0 rows"

Check in this order:
1. Stats tab `health` and the Run Log "Problems" cell.
2. Rules `MIN_ICP_SCORE` (7): most businesses score lower by design. Rejected ones are written to `Seen` with a Result.
3. Rules `REQUIRE_CONTACT` = `email_or_social`: a business with no email and no social link is dropped.
4. Rules `REQUIRE_WEBSITE_OSM` = `Yes`: free-map businesses without a website are skipped.
5. The niche may be disabled, or below `MIN_BUDGET_AUD` (listed as "Skipped (budget below MIN_BUDGET_AUD)" in Problems).
6. All candidates were already in `Seen` (duplicates are skipped instantly).
7. Quick local check of one country, no Google needed:

```
powershell -ExecutionPolicy Bypass -File "F:\Github Repos\projects\lead-bot-worldwide\install\run-local.ps1" --local --country US
```

## 4. Installer and PC problems

| Problem | Fix |
|---|---|
| Installer says Python is missing even after installing it | close the window, open a new one, run `INSTALL.cmd` again (PATH refresh) |
| "running scripts is disabled" | start with `INSTALL.cmd`; it bypasses the policy for that run only |
| `MISSING virtual environment` or `MISSING secrets\.env` in `-Check` | normal before the first install; the installer creates them |
| Self-test says `No module named 'requests'` | you used system Python; use the project one: `app\.venv\Scripts\python.exe` (the installer creates it) |
| Self-test fails after install | run `INSTALL.cmd` again (reinstalls packages), then `install\install.ps1 -Check` |

## 5. Other things to know

- GitHub normally pauses scheduled workflows in a repo with no activity for 60 days. This is general GitHub behaviour, not verified for your repo; if the daily run stops, open Actions and click Enable.
- A private repo has limited free minutes; the file comment says two runs of ten jobs exceed them. See `Guide\How To Change Things.md` Recipe 5.
- The code contains no live test of the GitHub run or of your sheets. Not verified: all behaviour that needs your accounts.

More: `app\Google And GitHub Setup.md`, `app\Secrets Guide.md`, `app\Sheets Setup.md`.
