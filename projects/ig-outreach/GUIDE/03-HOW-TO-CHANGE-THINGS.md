# 03 How to change things (ig-outreach)

Settings come from environment variables: GitHub repo Variables/Secrets for the daily run, `secrets\.env` for runs on this PC (`install\run.cmd` loads it). After any change, test with 3-10 leads and ONE account.

## 1. Change the message wording
| Want | Where |
|---|---|
| Sender, agency, services | Variables `SENDER_NAME`, `AGENCY_NAME`, `OFFER` |
| What the free sample is | Variable `FREE_SAMPLE` (default `a free 30-60 second sample video made for them`) |
| Real results the AI may quote | Variable `CASE_STUDIES`, one per line (or separated by `||`). Empty = the two case-study angles are skipped |
| Core instructions (length, tone, format) | `app\main.py`, text block `COMMON` (needs a new upload to GitHub) |
| Follow-up goals | `app\main.py`, dict `FU_GOALS` |
| Message angles | `app\styles.py`, dict `STYLES` (name: (instruction, needs_case_studies)). Delete a losing angle or add a new one in the same shape |
| Max words, spam words | `app\rules.py`: `MAX_WORDS` (40), `SPAM_WORDS` |

Compare angles: after about 100 sends, filter `Outreach Log` by the `Style` column and compare replies.

## 2. Limits and pace
| Want | Setting | Default |
|---|---|---|
| Messages per account per day | Variable `DAILY_LIMIT_PER_ACCOUNT` | 10 (code hard cap 20) |
| One account faster/slower for a day | `Accounts` tab, `Max Per Day Override` | blank |
| Send hours | `SEND_WINDOW` | `09:00-21:00` |
| Minutes between one account's messages | `MSG_GAP_MINUTES` | `15-20` |
| Follow-up days after each send | `FOLLOWUP_GAPS` | `4,4,4` |
| Time zone | `TIMEZONE` | `America/New_York` |
| Date text in the log | `DATE_FORMAT` | `%d-%b-%Y` |

The ramp (nothing for 14 days, 5 a day until day 28) is `account_cap()` in `app\main.py`. The cap of 20 is `HARD_CAP`. Do not raise either; they protect your accounts.

## 3. Schedule
Edit `app\.github\workflows\outreach.yml`: `cron: "0 12 * * *"` is the full run (UTC), `"0 */4 * * *"` the sync-only run. Upload the file to GitHub. Manual run: Actions > "Daily outreach prep" > Run workflow (tick `sync_only` to only sync).

## 4. Accounts
1. Add a row in the `Accounts` tab: Account name, Start Date (YYYY-MM-DD), Status Active.
2. Pause one: set Status to `Paused`, or fill `Pause Until`. Do this on any warning or "Action blocked" for 3-7 days.
3. For the one-click sender add the account to `profiles.json` (copy of `profiles.example.json`) with its Chrome profile folder (open `chrome://version` in that profile, "Profile Path").

## 5. Leads sheet columns
The bot finds the Instagram column by header words (instagram, insta, handle, social; `ig` also works). Optional columns are found by words: name, niche/category/industry, bio/about/description, email, phone, linkedin/website, address/location/city/country. To use another tab set `LEADS_TAB`. Different words need an edit to `read_leads()` in `app\main.py`.

## 6. Add or change AI keys
1. Edit the secret `AI_API_KEYS` (GitHub) or `AI_API_KEYS` in `secrets\.env`: one key per line.
2. Use at least 2 providers so one limit never stops a day. Supported: Gemini, Groq, OpenRouter, Mistral, OpenAI, Anthropic.
3. No model names are needed. A NEW provider needs code: add it to `BASES`, `detect()`, `candidates()` and `_call()` in `app\ai.py`.

## 7. Instagram profile reading (optional)
Set secret `IG_ACCESS_TOKEN` and variable `IG_USER_ID` (Meta developer app, Instagram Professional account linked to a Facebook Page, permissions `instagram_basic`, `pages_show_list`, `pages_read_engagement`). Without them the bot uses your sheet's Niche/Bio. API version: env `GRAPH_VERSION` (default `v24.0`).

## 8. Sheet columns of the Log/Queue
Matched by header name; if you add a column of your own, it is kept. Renaming a header the bot uses (see `02`) makes it append a new column with the original name. Add a bot-written column by adding the name to `LOG_H` or `Q_H` in `main.py` and writing it in the code.

## 9. Test after a change
1. Put 3 leads in the Leads tab and one account with a Start Date older than 28 days.
2. Sync-only check (writes nothing new):
```
install\run.cmd main.py --sync-only
```
3. Full run:
```
install\run.cmd main.py
```
4. Check `Outreach Log`, `Today Queue` and the last row of `Run Log`.
