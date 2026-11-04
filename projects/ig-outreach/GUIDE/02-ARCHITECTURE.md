# 02 Architecture: how ig-outreach works inside

A small Python app in `app\`. No server, no database: your Google Sheet is the storage, GitHub Actions is the daily runner, and a human sends every DM. All names below were checked against the code.

| File | Job |
|---|---|
| `main.py` | The whole pipeline (sync, follow-ups, re-queue, new leads, scheduling) |
| `ai.py` | AI client with automatic provider and model fallback |
| `ig.py` | Optional Instagram profile reader (Meta Business Discovery API) |
| `rules.py` | Safety checks on every message |
| `styles.py` | The 9 message angles |
| `send_assist.py` | Local helper: opens the DM chat, copies the message; you paste and send |
| `apps_script.gs` | Sheet script that stamps the real send / reply time |
| `.github\workflows\outreach.yml` | Schedule and settings wiring |

## 1. Data flow (`python main.py`, in order)
1. **Check settings**: needs `GOOGLE_SERVICE_ACCOUNT_JSON` and `SHEET_ID`; a full run also needs `AI_API_KEYS` and `OFFER`. Otherwise exits with `MISSING SETTING: <name>`.
2. **Connect** (`connect()`): opens the sheet, creates any missing tab, and maps columns by the REAL header names (missing headers are appended, nothing is overwritten). `GOOGLE_SERVICE_ACCOUNT_JSON` may be the JSON text or a path to the file.
3. **Sync** (`sync()`): for every `Today Queue` row where you typed `Yes` in `Done? (type Yes)`, copies the send date into `Outreach Log` (`Message Sent On` or `Follow-up N`), sets `Stage`, `Lead Status` = Contacted and `Next Due (auto)` = send date + gap. Unfinished rows from earlier days become `Synced = Expired`. With `--sync-only` the run stops here (cron every 4 hours).
4. **Accounts** (`load_accounts`, `account_cap`): reads the `Accounts` tab (seeded from `AGENT_ACCOUNTS`) and works out each account's cap for today: Paused or `Pause Until` in the future = 0; start date younger than 14 days = 0; 14-27 days = max 5; 28+ days = `DAILY_LIMIT_PER_ACCOUNT` (default 10); blank start date = max 5; `Max Per Day Override` wins; hard cap 20 always. Messages already queued today are subtracted. The result is written to the `Phase (auto)` column.
5. **Due follow-ups**: log rows in Stage "Message sent" / "Follow-up 1 sent" / "Follow-up 2 sent" whose `Next Due (auto)` is today or earlier, not replied, and `Lead Status` not in the stop list (interested, call booked, client, not interested, do not contact, unsubscribed) get a follow-up text and a queue row, from the same account.
6. **Re-queue**: log rows still in Stage `Queued` with no live queue row (skipped yesterday, or crash) get a fresh queue row.
7. **New leads** (`read_leads`): reads the Leads tab (`LEADS_TAB`, else the first tab). The Instagram column is found by header (contains instagram/insta/handle/social); name, niche, bio, email, phone, website, location are optional and found the same way. Duplicate and already-known handles are skipped. For each lead: pick the account with most capacity left, read the profile through `ig.py` if a token exists, choose a style (`styles.pick`, least used of the last 60), write the message (`write_message`: up to 3 tries, each rejection reason is fed back to the AI), then log + queue it.
   - Private/unreadable account with no niche/bio -> Stage `Private - follow manually`.
   - No niche and no bio -> Stage `Needs review`.
   - Still failing the rules after 3 tries -> Stage `Needs review`, reason in `Notes`.
8. **Write**: log changes first, then new log rows, then queue rows with suggested times (`assign_times`: round-robin across accounts, staggered, `MSG_GAP_MINUTES` between one account's messages, inside `SEND_WINDOW`; rows past the window say "late, tomorrow is better").
9. **Run Log**: always appends one row (`Run time`, `Summary` counts, `Problems`). Console prints `Done: ...` and `Problems: ...`.

## 2. Sheet tabs and columns
| Tab | Columns |
|---|---|
| Leads (your input; name set by `LEADS_TAB`) | needs an Instagram/Handle column; optional Name, Niche, Bio, Email, Phone, LinkedIn/Website, Location |
| `Outreach Log` | Date Added, Agent Account, Niche, Name, Instagram Handle, Profile Link, Open DM Chat, Account About, Followers, Email, Phone, LinkedIn / Website, Location, Message Sent, Message Sent On, Replied? (Yes/No), Replied At (auto), Reply Message, Follow-up 1/2/3 and Follow-up 1/2/3 Text, Lead Status, Stage, Next Due (auto), Notes, Style |
| `Today Queue` | Queue Date, Suggested Time, Agent Account, Type, Name, Instagram Handle, Open DM Chat, Profile Link, Before You Send, Message to Send, Done? (type Yes), Sent At (auto), Synced, Style |
| `Accounts` | Account, Start Date (YYYY-MM-DD), Status (Active/Paused), Pause Until (YYYY-MM-DD), Max Per Day Override, Phase (auto), Notes |
| `Run Log` | Run time, Summary, Problems |

Log rows are only appended or updated in place, never deleted.

## 3. AI provider rotation (`ai.py`)
- Secret `AI_API_KEYS`: one key per line (also split on commas/semicolons/spaces).
- Provider is detected from the key prefix: `sk-ant-` Anthropic, `gsk_` Groq, `sk-or-` OpenRouter, `AIza` Gemini, `sk-` OpenAI; other keys are tried against Groq, Mistral, Gemini, OpenRouter.
- At start it asks each provider for its CURRENT model list and ranks newest first (Gemini: flash models only; OpenRouter: free models only; OpenAI: gpt/o-series, mini first). No model name is hard-coded.
- `generate()`: tries the first 5 models of each live key. 401/403 -> key off for the run; 402 -> out of credit, key off; 429 -> next provider; other errors -> 1 s then next model. Up to 3 rounds with 20 s, 40 s pauses. The model that worked moves to the front. All failed -> `All AI providers failed: ...`.
- No usable key at all -> `No working AI key.` and the run stops.

## 4. Message safety (`rules.py`)
Max 40 words; spam-word list (not "free": the first message MUST say free); no links, no `@`, max 1 exclamation mark; numbers/percentages only if they appear in your `CASE_STUDIES`; no repeated opening four words; a rejected text is retried with the reason.

## 5. Cloud schedule (`outreach.yml`)
- `0 12 * * *` UTC: full run. `0 */4 * * *`: `--sync-only`. Manual run has the input `sync_only`. Lock `outreach` stops overlapping runs; job limit 45 minutes.
- Instagram sending is never automated. `send_assist.py` runs on your PC and only opens chats and copies text.
