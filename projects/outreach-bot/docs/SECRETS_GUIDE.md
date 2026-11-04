# SECRETS_GUIDE: every name the bot reads

Where: GitHub repo > **Settings > Secrets and variables > Actions**. **Secret** = hidden value (tab *Secrets*).
**Variable** = visible setting (tab *Variables*). Every value is trimmed: spaces, quotes, `Bearer ` and a pasted
`NAME=` in front are removed automatically.
The example values below are fake and cut short with `...`. Never paste a real key into a file, issue or chat.

## Required

| Name | Secret or Variable | Required? | Fake example (format) | Where to get it | Free limit |
|---|---|---|---|---|---|
| `GOOGLE_SA` | Secret | **Yes** | `{"type": "service_account", "client_email": "bot@proj.iam.gserviceaccount.com", ...}` (the whole JSON file) | console.cloud.google.com > IAM > Service accounts > Keys > Add key > JSON. Enable the Google Sheets API. | Free: 60 reads and 60 writes per minute per user. The lead bot uses the same account, so this bot stays at 19 reads and about 30 writes a minute or fewer (CONTRACT.md 4.6) |
| `OUTREACH_SHEET_ID` | Secret | **Yes** | `1AbCdEf...xYz` (about 44 characters, from the sheet URL `/d/<ID>/edit`; the full URL also works) | Make a NEW blank Google Sheet. Share it with the `client_email` above as **Editor**. | Free |

## Lead sheets: each one optional (a missing one = a `SKIP` line, never a crash)

Names follow `D:\All Automations Records\Lead generation\CONTRACT.md`. If that file names a sheet differently, add
it as `EXTRA_LEAD_SHEET_IDS`. Share every lead sheet with the service account (**Viewer** is enough: this bot
never writes to lead sheets). A bare ID or the full sheet URL both work.
What is read in each sheet (CONTRACT.md v5):
- Every tab whose header row has both `Place Id` and `Company Name`. Columns are matched by header name, so you can
  move columns or rename tabs.
- Never read: `All Leads`, `Master Dashboard`, `Stats`, `Rules`, `Niches`, `Blacklist`, `Run Log`, tabs starting
  with `OLD `, and the other control tabs.
- Emails and domains listed in a sheet's `Blacklist` tab (column A) are skipped.

| Name | Secret or Variable | Required? | Fake example | Where to get it | Free limit |
|---|---|---|---|---|---|
| `SHEET_ID_AU` | Secret | optional | `1Qw...e9` | URL of the AU lead sheet | Free |
| `SHEET_ID_AU_ONLY` | Secret | optional | `1Rt...k2` | URL of the separate AU-only sheet | Free |
| `SHEET_ID_US`, `SHEET_ID_CA`, `SHEET_ID_GB` (or `SHEET_ID_UK`), `SHEET_ID_IE`, `SHEET_ID_NZ` | Secret | optional | `1Zx...p0` | URL of each country sheet | Free |
| `SHEET_ID_AE` (or `_UAE`), `SHEET_ID_SA` (or `_KSA`), `SHEET_ID_QA` | Secret | optional | `1Ui...m4` | URL of each country sheet | Free |
| `SHEET_ID_YOUTUBE` (or `SHEET_ID_YT`) | Secret | optional | `1Op...d7` | URL of the worldwide YouTube sheet | Free |
| `EXTRA_LEAD_SHEET_IDS` | Secret | optional | `1Aa...1,1Bb...2` | any other lead sheets, comma separated | Free |
| `SHEET_ID` / `LEADS_SHEET_ID` | Secret | old layout only | `1Cc...3` | used ONLY when no `SHEET_ID_<country>` is set | Free |

When the same business is in two sheets (same Place Id, or any shared email address), the first one wins, in this
order: AU, AU_ONLY, US, CA, GB, IE, NZ, AE, SA, QA, YOUTUBE.

## AI keys: one secret per key, all optional

| Name | Secret or Variable | Required? | Format (fake) | Where to get it | Free limit (check your own page) |
|---|---|---|---|---|---|
| `GEMINI_API_KEY_1`, `_2`, `_3` (up to `_5`) | Secret | optional | `AIza` + 35 characters, 39 in total, e.g. `AIzaSy...k3Xq` | aistudio.google.com > API keys > Create API key > **"Create key in a new project"**, a NEW project for EACH key | Per Google Cloud **project**, per model, reset at midnight Pacific. See aistudio.google.com/usage > Rate limits. Small (tens to a few hundred requests a day per model) |
| `GROQ_API_KEY` (`GROQ_API_KEY_2` for a 2nd account) | Secret | optional | `gsk_` + about 52 letters/digits, e.g. `gsk_8Hn...Zq9w` | console.groq.com/keys | Per organisation. Last published: llama-3.1-8b-instant 14,400 requests and 500K tokens a day; llama-3.3-70b-versatile 1,000 requests and 100K tokens a day. See console.groq.com/settings/limits |
| `MISTRAL_API_KEY` | Secret | optional | 32 letters/digits, no prefix, e.g. `aB3...9Zk` | console.mistral.ai > API keys (free "Experiment" plan, phone check) | Free plan: per-second rate limit plus a monthly token cap; see console.mistral.ai > Limits. Free-plan prompts may be used for training |
| `OPENROUTER_API_KEY` | Secret | optional | `sk-or-v1-` + 64 characters, e.g. `sk-or-v1-3f...a1c0` | openrouter.ai/keys | 50 free-model requests a day per account; 1,000 a day after a one-time $10 credit |

Old names still work as a fallback (comma separated): `GEMINI_API_KEY`, `GEMINI_KEY(S)`, `GOOGLE_API_KEY`,
`GROQ_KEY(S)`, `OPENROUTER_KEY(S)`, `MISTRAL_KEY`, `AI_KEYS`. Keys are routed by their prefix, so a Groq key under a
Gemini name still goes to Groq (the report says so).

## Variables (optional; the Options tab in the Outreach sheet is the normal place)

A Variable with the same name as an option overrides the Options tab: `DAILY_TARGET`, `RUN_LIMIT`, `DRY_RUN`,
`TEMPLATE_FALLBACK`. Model lists: `GEMINI_MODELS`, `GROQ_MODELS`, `MISTRAL_MODELS`, `OPENROUTER_MODELS` in the form
`model:RPM:RPD,model2:RPM:RPD` (defaults are pinned, stable models; put your own numbers from the provider pages).
`MAX_RUN_MIN` (50) = stop drafting after this many minutes.

## What you see at the start of every run (registration report)

```
SKIP NZ: no SHEET_ID_NZ secret set.
READ AU: 812 rows from 9 tab(s), 790 new after removing duplicates.
AI KEY REGISTRATION (values masked to the last 4 characters):
  GEMINI_API_KEY_1: REGISTERED Gemini key ...k3Xq
  GEMINI_API_KEY_2: IGNORED Gemini key ...7a2B - wrong format: expected 'AIza' + 35 characters (39 in total), got 31 characters. Copy it again from the provider.
  GEMINI_API_KEY_3: ...k3Xq is the same key as GEMINI_API_KEY_1 - counted once
  GROQ_API_KEY: REGISTERED Groq key ...Zq9w
  MISTRAL_API_KEY: not set
  OPENROUTER_API_KEY: not set
AI keys registered: Gemini 1, Groq 1, Mistral 0, OpenRouter 0. Slots (key x model): 4. No test calls are made.
```
To test the keys for real (one tiny call each), run Actions > **diagnose-keys**.

## Why the old files "burned" keys after 1-2 emails (plain words)

1. **Dead keys.** The keys in the old keys file were already dead: Groq answered `401 Invalid API Key`, OpenRouter
   `401 User not found`. No code can make a dead key work.
2. **A 403 misread as "bad key".** Groq sits behind Cloudflare, which blocks Python's default user-agent with
   `403 error code: 1010`. The old code read that 403 as a broken key and dropped a good key.
3. **One shared Gemini project.** Gemini limits belong to the Google Cloud *project*, not the key. Several keys made
   in the same project share one small daily quota, so "3 keys" was really 1.
4. **Probe calls.** The old start-up made 13 HTTP calls (8 of them real generations) to test models before the first
   email, spending most of a small daily quota on tests.
5. **Newest preview models.** The old code chased the newest models; preview models often have `limit: 0` free quota
   (instant 429) or disappear, which looked like the keys dying.

**How v3 prevents it:** keys are trimmed and format-checked, and the registration report shows each one as
REGISTERED or IGNORED (masked), so a bad paste is visible before any call. There are zero test calls. Models are
pinned and stable. A custom user-agent is sent, and a Cloudflare 1010 never marks a key dead. A per-minute 429
pauses only that key and the next key is used; a second 429, or a per-day 429, stops that key until tomorrow. When
every key is spent, the leads stay queued for the next run instead of being spammed with a template. Per-key daily
counters live in the **AI Usage** tab, so a spent key is not retried in later runs the same day.
