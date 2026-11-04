# 03 How to change things (outreach-bot)

Order of precedence for every option: **GitHub Variable (same name) > `Options` tab value > built-in default** (`class Cfg`). If a setting "does not change", check there is no GitHub Variable overriding it (GitHub > repo > Settings > Secrets and variables > Actions > Variables).

Always test a change with a dry run of 5-10 leads first (section 9).

## 1. Change what the emails say (rules)
1. Open the Outreach Google Sheet, tab `Email Rules`.
2. Add one rule per row in plain English, e.g. `Keep the email between 60 and 100 words`. Rows starting with `#` are ignored.
3. These rules are added after the base rules and win when they disagree. The next run uses them.
4. Three kinds are also enforced in code (`hard_rules()`): word ranges (`60 to 100 words`, `under 90 words`, `at least 50 words`; put the word `subject` in the row to apply it to the subject line), banned words (`Never use these words: amazing, cheap`), and no links. Anything else is only a request to the AI, not checked.

Base rules (sender, structure, hard rules) are in `app\rules.md`. Editing that file changes `app\` source, so it needs a new upload to the GitHub repo to reach the daily run. Prefer the `Email Rules` tab. The template used when the AI is off lives in `generate.py` (`OPENERS`, `OFFERS`, `ASKS`, `SUBJECTS`).

## 2. Limits: how many drafts
| Want | Where | Option |
|---|---|---|
| Drafts per day (all runs together) | `Options` tab | `DAILY_TARGET` (default 400) |
| Most drafts in one run | `Options` tab, or Actions input `limit` | `RUN_LIMIT` (default 700) |
| Leads per AI call | `Options` tab | `BATCH_SIZE` (1-10, default 5) |
| Minutes before a run stops | GitHub Variable | `MAX_RUN_MIN` (default 50) |
| Only some countries | `Options` tab | `COUNTRIES`, e.g. `AU, NZ` |
| Only better leads | `Options` tab | `MIN_ICP`, e.g. `7` |
| Segments never pitched | `Options` tab | `SKIP_SEGMENTS` |

The real ceiling is the free AI quota (about 400-700 drafts a day). Leads not reached wait for the next run.

## 3. Schedule
1. Edit `app\.github\workflows\generate.yml`, the line `- cron: "0 10 * * *"` (UTC; 10:00 UTC = 15:00 Pakistan). Keep it after Gemini's daily reset (07:00/08:00 UTC).
2. Upload the changed file to the GitHub repo.
3. Manual run: GitHub > Actions > `generate-emails` > Run workflow (inputs `limit`, `dry_run`).
4. GitHub may pause scheduled runs after 60 days without repo activity (GitHub rule, not verified for this repo). If so, re-enable the workflow in the Actions tab.

## 4. Sender identity and legal footer
`Options` tab: `SENDER_NAME`, `AGENCY_NAME`, `SENDER_ADDRESS` (required for the footer), `SENDER_WEBSITE`, `FOOTER` (On/Off). Without name and address, rows get the flag `no footer yet...` in `Emails > Flags`. Country wording is in `FOOTER_EXTRA` in `generate.py`.

## 5. Add a country / lead sheet
1. Share the lead sheet with the service-account email (Viewer is enough).
2. Add a GitHub secret `SHEET_ID_<COUNTRY>` (ID or full URL). Known names: AU, AU_ONLY, US, CA, GB/UK, IE, NZ, AE, SA, QA, YOUTUBE.
3. A country not in that list: put its ID in the secret `EXTRA_LEAD_SHEET_IDS` (comma separated).
4. Different column names in that sheet: `Options` tab, `COLUMN_ALIASES` = `Insight=Pain Points|Lead Notes; Company=Business`.
5. A brand-new secret name must also be listed under `env:` in `generate.yml` to reach the daily run (all names above are already there).

## 6. Add or change AI keys / models / provider order
- **New key**: add the secret (`GEMINI_API_KEY_1..5`, `GROQ_API_KEY`, `GROQ_API_KEY_2`, `MISTRAL_API_KEY`, `OPENROUTER_API_KEY`), then run `diagnose-keys`. Each Gemini key must be created in its OWN Google Cloud project, or they share one quota.
- **Order**: `Options` tab, `AI_ORDER`, e.g. `groq,gemini,mistral,openrouter`.
- **Models / budgets**: GitHub Variable `GEMINI_MODELS`, `GROQ_MODELS`, `MISTRAL_MODELS` or `OPENROUTER_MODELS`, format `model:requests-per-minute:requests-per-day,model2:rpm:rpd`. Take the numbers from your own provider usage page.
- **A whole new provider** needs code: add it to `PROVIDERS`, `DEFAULT_MODELS`, `KEY_NAMES`, `KEY_FORMAT`, `CALLS` and `DAY_OF` in `generate.py`, and write a call function like `openai_call` (fits any OpenAI-compatible API). Run `python selftest.py` after.
- **No AI at all**: `AI_MODE` = `template`.

## 7. Sheet columns
Lead sheets: columns are found by header name, so you may reorder them; add alternative names with `COLUMN_ALIASES`. Outreach sheet: the bot appends by its own header names (`EMAILS_H`, `LEADS_H` in `generate.py`). Do not rename or delete those headers in `Emails` or `Leads`. Extra columns to the right are probably safe (not verified: test with a dry run). A new bot-written column needs a code change to those lists.

## 8. Inboxes and follow-ups
`Options`: `INBOX_ROTATION` On, `FOLLOW_UPS` On, `FU1_DAYS` (3), `FU2_DAYS` (7), `WARM_START` (5), `WARM_STEP` (2), `INBOX_MAX` (50). Add addresses in the `Inboxes` tab (Daily Cap, Warm-up Start date, Active Yes/No). Sending itself stays manual; do not enable `app\phase2_parked\`.

## 9. Safe test after any change
1. Offline tests:
```
powershell -ExecutionPolicy Bypass -File install\run-bot.ps1 -SelfTest
```
2. Dry run (writes nothing, 10 leads):
```
powershell -ExecutionPolicy Bypass -File install\run-bot.ps1
```
3. To really write 10 drafts, add `-Live -Limit 10` to the command in step 2.
