# 02 Architecture: how outreach-bot works inside

Everything is one Python file, `app\generate.py` (about 1950 lines), plus `app\selftest.py` (offline tests) and `app\tools\diag_keys.py` (key tester). There is no server and no database: Google Sheets is the only storage. All names below were checked against `generate.py` (version dated 2026-11-01).

## 1. Data flow (one run, in order)

1. **Start** (`main()`): reads `OUTREACH_SHEET_ID`. Stops with a clear message if it is empty, or if it equals a lead sheet (the bot never writes to lead sheets). Time limit = `MAX_RUN_MIN` (default 50 minutes).
2. **Find lead sheets** (`lead_sheet_ids()`): looks for the secrets `SHEET_ID_AU`, `_AU_ONLY`, `_US`, `_CA`, `_GB` (or `_UK`), `_IE`, `_NZ`, `_AE`, `_SA`, `_QA`, `_YOUTUBE`, plus `EXTRA_LEAD_SHEET_IDS`. A missing one prints `SKIP <label>: no ... secret set.` and the run goes on.
3. **Read leads** (`read_book`, `parse_tab`, `load_leads`): in each lead sheet, every tab whose header row has both `Place Id` and `Company Name` is a lead tab. Columns are matched by header NAME, not position (aliases in `ALIASES`; add more with the option `COLUMN_ALIASES`). Tabs such as `Master Dashboard`, `Stats`, `All Leads`, `Rules`, `Niches` are never read (`LEAD_TAB_SKIP`). A `Blacklist` tab (column A) lists emails/domains to skip.
4. **De-duplicate** (`lead_key`): same Place Id, or any shared email, counts as one lead. The first sheet wins in the order AU, AU_ONLY, US, CA, GB, IE, NZ, AE, SA, QA, YOUTUBE.
5. **Open the Outreach sheet** (`class Outreach`): creates any missing tab, fills `Options` with defaults it does not have yet, and reads `Options` and `Email Rules`. A GitHub Variable with the same name as an option overrides the sheet value.
6. **Select** (`select()`): each new lead gets a one-time `Note` in the `Leads` tab: `queued`, `already drafted`, `no usable email (...)`, `status in lead sheet: ...`, `country not selected in Options`, `segment ...: not cold-pitched`, `ICP below MIN_ICP`, `email marked invalid in the lead sheet`, or `skipped: ...` (legal rules, e.g. free-mail addresses in GB/IE). Queued leads are sorted PRIME, PRIME-REVIEW, GROWING, then the rest, then by ICP score, highest first.
7. **Write** (`run()`): takes leads in batches (`BATCH_SIZE`, default 5; with `VERIFY_MX=On` it first drops domains that cannot receive mail), sends ONE prompt per batch, parses the answer and checks each draft (`check()`: word counts, subject length, no links/emoji, no "I watched your...", no prices, no copied sentences, your hard rules). A failed draft prints `AI draft rejected (...)`, is counted as rejected and the lead stays queued for the next run. With `TEMPLATE_FALLBACK=On` the built-in template (`OPENERS`, `OFFERS`, `ASKS`) is used when the AI is out of budget.
8. **Finish**: adds greeting, signature and the country's legal footer (`compose`, `footer`), appends rows to `Emails`, flushing every 25 drafts (`FLUSH_EVERY`) so a crash loses at most 25. The last log line starts with `DONE.`

The run stops early when: `DAILY_TARGET` is reached (counted by `Drafted On` = today, across runs), `RUN_LIMIT` is reached, the time limit passes, or every AI key is spent. If no AI key is registered and `TEMPLATE_FALLBACK` is Off it drafts nothing and says so.

## 2. Outreach sheet tabs and columns (the only sheet the bot writes)

| Tab | Columns / purpose |
|---|---|
| `Leads` | Added On, Place Id, Country, Niche, Company, Email, Email Type, First Name, Decision Maker Name, City, Website, Lead Insight, Segment, ICP Score /10, Source, Note. A log of every lead seen and why it was or was not queued. |
| `Emails` | Email, First Name, Subject, Email body, Company, Place Id, Country, Niche, Assigned Inbox, Drafted On, Status, Follow-up 1 Due, Follow-up 2 Due, Sent On, Follow-up 1 Subject, Follow-up 1 Body, Follow-up 2 Subject, Follow-up 2 Body, Written By, Flags. The drafts you copy and send. Also the ledger: a lead already here is never drafted twice. |
| `Options` | Option, Value, What it does. All switches (list in `03-HOW-TO-CHANGE-THINGS.md`). |
| `Email Rules` | One rule per row; rows starting with `#` are ignored. |
| `Inboxes` | Inbox Address, Daily Cap, Warm-up Start (YYYY-MM-DD), Active (Yes/No), Notes. Used only if `INBOX_ROTATION=On`. |
| `AI Usage` | Day, Provider, Key (last 4 characters only), Model, Calls, Tokens, Emails, State, Last error. The bot's memory of what each key has spent today. |
| `Queue <inbox>` | Created per inbox when rotation is On (formulas listing that inbox's emails). |

`Written By` shows `ai <Provider> <model>` or `template`. `Flags` carries warnings, e.g. `no footer yet: set SENDER_NAME and SENDER_ADDRESS in Options before sending`.

## 3. AI provider rotation (`class AI`, `class Slot`)

- Providers: Gemini, Groq, Mistral, OpenRouter. One KEY x one MODEL = one "slot". Defaults (`DEFAULT_MODELS`, format `model:requests-per-minute:requests-per-day`): `gemini-2.5-flash-lite:8:500`, `gemini-2.5-flash:4:200`, `llama-3.3-70b-versatile:20:900`, `llama-3.1-8b-instant:20:1400`, `mistral-small-latest:20:1000`, `meta-llama/llama-3.3-70b-instruct:free:15:45`. These budgets are deliberately below the free limits.
- Slot order = option `AI_ORDER` (default `gemini,groq,mistral,openrouter`). The first slot that is ready and has budget left is used; each slot is paced to its own requests-per-minute (Groq also by tokens per minute).
- Daily counters are saved in the `AI Usage` tab, so a second run the same day continues where the first stopped. Gemini's day ends at midnight Pacific time, the others at midnight UTC.
- Error handling (`classify()`): `429` per minute -> pause 20 s or more, second strike in a run -> slot off for the run. `429` per day (or "limit: 0") -> `exhausted` for today. `401/403` or "api key not valid" -> `bad key` (all models of that key are off for today). `404` / model errors -> `bad model`. `402` or "insufficient credit" -> bad key. `5xx` or empty answer -> back off and retry, key kept. Groq `403 error code 1010` is a Cloudflare block, NOT a dead key.
- Keys are routed by prefix (`AIza` Gemini, `gsk_` Groq, `sk-or-` OpenRouter), so a key under the wrong secret name still reaches the right provider. Key values are masked everywhere (`mask`, `scrub`).
- No test calls at start-up: the "AI KEY REGISTRATION" report only lists what was found.

## 4. Other parts
- **Legal footer**: per-country text in `FOOTER_EXTRA` (AU, NZ, CA, GB, IE) plus an unsubscribe line. Needs `SENDER_NAME` and `SENDER_ADDRESS` in Options.
- **Email checks**: `pick_email` / `email_problem` reject `noreply`, example domains and bad syntax.
- **Inbox rotation and follow-ups** (`Rotation`, `FOLLOW_UPS`): round-robin over `Inboxes` with warm-up caps (`WARM_START`, `WARM_STEP`, `INBOX_MAX`); follow-ups due after `FU1_DAYS` / `FU2_DAYS`.
- **Cloud**: `app\.github\workflows\generate.yml` (daily 10:00 UTC, runs `selftest.py` first, then `generate.py`; a concurrency lock stops two runs overlapping) and `diagnose-keys.yml` (manual).
- **Parked**: `app\phase2_parked\` (`send.py`, `replies.py`) is OFF on purpose.
- Sheets read limit: keep to about 19 reads a minute (the service account is shared with the lead bot); `retry()` waits and retries on quota errors.
