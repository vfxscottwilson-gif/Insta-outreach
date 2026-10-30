# Instagram Outreach v3: Setup Guide & Roadmap

## What it does (the full flow)
1. **Sheet in**: reads your leads tab (needs an Instagram/Handle column; optional Name, Niche, Bio, Email, Phone, LinkedIn/Website, Location).
2. **Profile analysis**: reads public bio, follower count and recent captions through Meta's official API (business/creator accounts). Personal/private accounts fall back to your sheet's Niche/Bio.
3. **Writes the message**: under 40 words, one of 9 rotating angles (pain mirror, micro-advice, money left on the table, fear of falling behind, curiosity gap, compliment + gap, direct free sample, case study, success story). First message always says the sample is **free**.
4. **Schedules**: max 10 per account per day (hard cap 20), accounts interleaved, 15-20 min between one account's messages, inside a send window (default 09:00-21:00 New York).
5. **Today Queue**: each row = account, time, chat link, message.
6. **You send** (one click with `send_assist.py`), the sheet records message, date, stage, follow-up dates.
7. **Follow-ups** (days 4/8/12 by default) are written automatically; replies or a final Lead Status stop them.

## What changed vs v2 (bugs fixed)
- Re-running the workflow could exceed the daily limit. Fixed: every queued item today + everything sent in the last 24h counts.
- Skipped queue rows stayed forever and blocked capacity; the lead was lost. Fixed: stale rows expire and the message is re-queued.
- A crash between "write log" and "write queue" lost leads. Fixed: log first, orphans re-queued.
- Header rows were overwritten if you added a column. Fixed: columns are matched by name, missing ones appended.
- Google Sheets 429/5xx errors crashed the run. Fixed: retries.
- Personal accounts were all dropped as "Private". Fixed: uses your Niche/Bio instead.
- Instagram API rate limit stopped the whole run. Fixed: continues without profile reading.
- Spam filter blocked the word "free". Fixed: "free" is now required in message 1.
- AI: added OpenAI and Anthropic keys; bad key / no credit / rate limit now switches provider automatically.
- Invented statistics are blocked: numbers and "we had a client like you" stories are only allowed from your real `CASE_STUDIES`.
- Timezone default is now America/New_York; rows with no valid handle are counted in Run Log.

## What I did NOT build, and why
I did not build an unattended sender that logs into your accounts through Chrome and clicks "send" while hiding from Instagram's detection. It is against Instagram's terms, it is the fastest way to lose every account you've warmed up, and rotating a fleet of accounts to dodge detection is exactly what their systems link and ban together. `send_assist.py` removes almost all the effort instead: it opens the right chat in the right Chrome profile at the right time, copies the message, and records everything. You press paste + Enter + Enter.

## Setup
### 1. Google Sheet + service account
Create a project at console.cloud.google.com, enable Google Sheets API, create a Service Account, download its JSON key, and share your sheet (Editor) with the `client_email` in it.

### 2. Apps Script (exact send time when you tick Done by hand)
Extensions > Apps Script > paste `apps_script.gs` > Save.

### 3. AI keys: ONE secret `AI_API_KEYS`, one key per line
Gemini (aistudio.google.com/apikey), Groq (console.groq.com/keys), OpenRouter (openrouter.ai/keys), Mistral, OpenAI, Anthropic. No model names needed. Use at least 2 providers (one free + one paid) so a limit never stops a day.

### 4. Instagram profile reading (optional)
Instagram Professional account + Facebook Page + Meta developer app (`instagram_basic`, `pages_show_list`, `pages_read_engagement`). Secrets/vars: `IG_ACCESS_TOKEN`, `IG_USER_ID`. Use a spare account.

### 5. GitHub (private repo)
Upload everything. Settings > Secrets and variables > Actions.
**Secrets:** `GOOGLE_SERVICE_ACCOUNT_JSON`, `AI_API_KEYS`, `IG_ACCESS_TOKEN` (optional)
**Variables:**
| Name | Example |
|---|---|
| `SHEET_ID` | ID between /d/ and /edit in the sheet URL |
| `AGENT_ACCOUNTS` | `acc1,acc2,acc3` (first run only; later use the Accounts tab) |
| `AGENCY_NAME`, `SENDER_NAME` | your agency / first name |
| `OFFER` | what you sell, one sentence |
| `FREE_SAMPLE` | `a free 30-60 second sample video made for them` |
| `CASE_STUDIES` | real results only, one per line, e.g. `Helped a dental clinic double reel views in 60 days` |
| `DAILY_LIMIT_PER_ACCOUNT` | `10` |
| `SEND_WINDOW` | `09:00-21:00` |
| `MSG_GAP_MINUTES` | `15-20` |
| `FOLLOWUP_GAPS` | `4,4,4` |
| `TIMEZONE` | `America/New_York` |
| `DATE_FORMAT` | `%d-%b-%Y` |
| `LEADS_TAB`, `IG_USER_ID` | optional |

### 6. Local helper (your computer)
`pip install gspread google-auth requests tzdata`. Copy `profiles.example.json` to `profiles.json` and map each account to its Chrome profile folder (open `chrome://version` in that profile: "Profile Path" ends with `Default`, `Profile 1`, ...). Set env vars `GOOGLE_SERVICE_ACCOUNT_JSON` (path to the key file), `SHEET_ID`, `TIMEZONE`. Then `python send_assist.py`.

### 7. Test
3 leads, 1 account with a Start Date older than 28 days, run Actions > Run workflow, check all tabs and Run Log, then try `send_assist.py`.

## Safety controls
- Account ramp: days 0-13 = no outreach, 14-27 = max 5/day, 28+ = your limit (hard cap 20). Blank start date = 5/day.
- Pause an account: Status = Paused or a Pause Until date. Do it on any warning or "Action blocked" (3-7 days).
- Every message is checked: under 40 words, no links/@, no spam words, no invented stats, no repeated openers.
- Replied / Not interested / Do not contact / Interested / Call booked / Client stop all follow-ups.
- Each lead stays with the same account for follow-ups.

## What you were missing (advice)
1. **Reply tracking is manual.** Nothing here can read your DMs. Mark `Replied? = Yes` quickly, or a follow-up goes to someone who answered.
2. **Same IP/device = linked accounts.** 12 accounts from one network get banned together. Use mobile data or separate networks per batch, stagger logins.
3. **Follow + engage first.** The queue's "Before You Send" column tells you to like 2 posts; skipping it raises report rates.
4. **Message requests.** DMs to non-followers land in Requests; many are never seen. Expect low reply rates (2-5% is normal). Email is far better: use the Email column for a parallel email sequence.
5. **LinkedIn handle -> Instagram.** The sheet needs the Instagram handle itself. Finding it from LinkedIn automatically means scraping LinkedIn, which I did not add (terms, and it gets accounts banned). Fill it by hand/VA or a lead-data tool.
6. **Real case studies.** Add real results to `CASE_STUDIES`; the bot refuses to invent them. The case-study angles are skipped if it's empty.
7. **Free sample = capacity.** Track who accepts; set Lead Status to Interested so follow-ups stop and you deliver the sample.
8. **Measure.** The Outreach Log has a Style column. After 100 sends, compare reply rate by style and delete the losers from `styles.py`.
9. **Keep a small test.** Do not send the same offer to 100% of leads before a 20-lead test.
10. **Rotate your sample, not just your words.** Identical sample videos across many leads look templated.

## Costs
GitHub private repo: ~150-250 free minutes/month used. AI: free tiers cover ~120 messages/day on 2 providers.
