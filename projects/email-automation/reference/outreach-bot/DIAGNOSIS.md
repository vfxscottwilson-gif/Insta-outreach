# DIAGNOSIS: why the AI keys "die after 1-2 emails"

Date: 2026-10-31. "Old" means `generate.py` v1. It is identical to the copy in `Draft-bot-fixed.zip`. That zip is
**older** than the folder: the only difference is the daily `schedule:` in `generate.yml`.
Line numbers below refer to the old file.

Evidence comes from 3 sources:
1. Real API answers from `tools/diag_keys.py` and curl, run on 2026-10-31. Keys are masked to their last 4 characters.
2. A simulation of the old code with fake providers, no network (`old start-up` and `old daily` below).
3. The code itself.

## Summary in plain words

1. **The two keys in your keys file are dead.** The Groq key (...Bxqh) answers `401 Invalid API Key` and the OpenRouter
   key (...ec1d) answers `401 User not found`. The file has **no Gemini key at all**: the `GEMINI_KEY` label is empty.
   So everything depended on whatever Gemini keys are in GitHub secrets.
2. **Groq was blocked even with a good key.** The old bot used Python's default User-Agent, and Groq's Cloudflare
   answers it with `403 error code: 1010`. The old bot reads every 403 as "key rejected".
3. **Your 3 Gemini keys share one quota.** Gemini limits are per Google Cloud project, not per key. The old bot spent
   6 test calls of that shared quota on every run, then up to 3 calls per email. It also picked the newest models
   (`gemini-flash-latest`, `gemini-3.8-flash`), which have the smallest free quota. In the simulation this leaves
   **1-16 emails** before "all AI providers failed".
4. **The real error text was thrown away**, so the log only said "REJECTED" or "no quota". You could not see that the
   cause was a revoked key, a Cloudflare block or a shared project.

## Root causes, ranked

| # | Cause | Verdict | Evidence | Fix (v2) |
|---|---|---|---|---|
| 1 | **Keys invalid / missing** (outside cause) | CONFIRMED | Groq `GET /openai/v1/models` -> `HTTP 401 {"message":"Invalid API Key","code":"invalid_api_key"}`. OpenRouter `GET /api/v1/key` and a `:free` chat call -> `HTTP 401 {"message":"User not found.","code":401}`. The keys file: `GEMINI_KEY` label with no value under it, `OUTUBE_KEY` (typo, empty), `ZEROBOUNCE_KEY` empty. Both key values are complete (56 and 73 characters, no hidden characters). | Make new keys (ROADMAP step 1). Run the **diagnose-keys** workflow, which tests the keys in your GitHub secrets the same way. Never paste keys into a repo or a public log: Google, Groq and OpenRouter take part in GitHub secret scanning and revoke leaked keys automatically. `.gitignore` now blocks `*.txt` and `*Keys*`. |
| 2 | **(g) + (d) Groq blocked by Cloudflare, read as "dead key"** | CONFIRMED | Same Groq key, Python `urllib` default User-Agent -> `HTTP 403 "error code: 1010"`. With a custom User-Agent -> `HTTP 401 Invalid API Key` (the real answer). Old `classify()` turns every 403 into `BadKey` (old 740-741), so `probe()` returns "key is bad" (old 896-897) and prints "Groq key 1: REJECTED". `old start-up` reproduces: "Groq key 1: REJECTED by the provider ... Skipped." **A valid Groq key would also have been killed this way.** | Every request sends `User-Agent: outreach-bot/2.0` (`generate.py` `_http`, `UA`). Errors are classified from the provider's own words. |
| 3 | **(c) 3 Gemini keys share ONE project quota** | CONFIRMED (docs) + simulated | Official rate-limits page (updated 2026-10-28): limits are "applied per project, not per API key", and RPD resets at midnight Pacific. The old bot treats each key as fresh capacity: 3 keys x 2 models = 6 "combos", all draining the same counter. `old daily`, RPD 20, 3 keys in one project: **7-16 emails**, then "all AI providers failed". RPD 5: **1 email**. | One key per **separate** Google Cloud project (ROADMAP step 1). The bot stops at the first per-day 429 for a slot and saves that in the **AI Usage** tab, so it does not try again until the reset. |
| 4 | **(a) Probing: test calls on every run, before the first email** | CONFIRMED | `probe(..., want=2, max_tries=7)` (old 882-900) is called for every key on every run (old 988-993). It runs **before** the sheet is even opened (old 1393-1394), so a sheet error still burns quota. `old start-up`: **13 HTTP calls, 8 of them generations, before email 1.** 6 of them hit the shared Gemini counter. Every manual re-run repeats this. A per-minute 429 during the test still counts as "good" (old 894-895). | **Zero test calls.** Models are pinned (`DEFAULT_MODELS`, or the `GEMINI_MODELS` / `GROQ_MODELS` / `OPENROUTER_MODELS` variables). A test proves the start-up makes no network call (`no_http_at_startup`). |
| 5 | **(b) Picks the newest `-latest` / `flash` models** | CONFIRMED (code) | `rank_gemini_models()` (old 811-829) sorts `-latest` aliases first, then the highest version number. With today's model list it picks `gemini-flash-latest, gemini-3.8-flash` (`old start-up`). Newest models have the lowest free quota, sometimes `limit: 0`. They also think by default (cause 7). Google no longer publishes per-model free numbers. The page says to look in AI Studio. | Pinned stable `gemini-2.5-flash-lite` then `gemini-2.5-flash`, with thinking off. You can change them per variable, e.g. `GEMINI_MODELS=gemini-2.5-flash-lite:10:20`, after checking your project's numbers at aistudio.google.com/usage. |
| 6 | **Up to 3 AI calls per email, for YouTube-only rules** | CONFIRMED (code) | `write_one(max_attempts=3)` (old 1192-1220) asks again whenever `check()` fails. Several checks only make sense for YouTubers: "channel name missing" (old 1147-1149), "no ask" unless the body says "clip" or "link" (old 1150-1151), and the "facts_used" rules. With your v2 business leads most drafts fail them, so every email costs 2-3 calls. Also, the v2 sheet has no plain `Email` column. The old `ALIASES` (old 137-153) does not know `Personal Email`, `Generic Email` or `Company Name`, so on `All Leads` the old bot stops with "no Email column" (old 167-169). | Batches: **one call writes 5 emails** (`BATCH_SIZE`). A draft that fails a rule goes to the template, and the AI is never asked again. Rules are rewritten for AU local businesses (`rules.md`). |
| 7 | **(e) Thinking tokens + big `maxOutputTokens`** | CONFIRMED (code) | Old Gemini call: `maxOutputTokens: 4096` and no `thinkingConfig` (old 753-754). `gemini-flash-latest` / 3.x Flash think by default, and thinking tokens count against the token limits. When thinking uses up the budget, the reply has no text, which raised `Transient` (old 759-761). That meant one more call. Groq/OpenRouter used `max_tokens: 1500` per single email (old 769). | `thinkingBudget: 0` on 2.5 models, `thinkingLevel: low` on 3.x, `maxOutputTokens = 180 x leads + 200` (1,100 for 5 emails). Measured prompt: about 1,300 input tokens for 5 leads, about 450 tokens per email in total. |
| 8 | **(h) Real error text thrown away** | CONFIRMED (code) | `_http()` reads the error body only to classify it, then raises an empty exception (old 720-727). The log prints fixed sentences: "a key was rejected (invalid, disabled or out of credit)" (old 959-960), "REJECTED by the provider" (old 995), "none answered a test message" (old 997-999). The 1010 block, "User not found" and "limit: 0" were never visible. | Every failure prints `provider + model + key ...last4 + STATE + the provider's own message`, with key values scrubbed. The last error is also written to the AI Usage tab. Tests: `real_error_text_is_kept_and_scrubbed`, `http_layer_reads_real_error_body`. |
| 9 | **(d) Per-minute limit handling** | PARTLY | `ask()` gives a combo a 60 s rest after a 429 and switches it off after 3 (old 952-957). `WRITE_PAUSE=4` s (old 1399) aims at 15 requests a minute, while the free tier allows about 5-10. `old daily` with RPM only (no daily cap): it **survives** 50 emails, but makes 18-33 extra 429 calls. So this wastes calls but is **not** the 1-2-email killer. Causes 1-6 are. | Calls are paced at `60/RPM` per slot. Groq is also paced by tokens per minute. A 429 waits for the provider's `Retry-After` / `retryDelay`, or uses exponential backoff, and **never drops the key**. Only a per-day 429 marks a slot exhausted, until the reset. |
| 10 | **(f) OpenRouter free daily cap** | CONFIRMED (docs) | Official limits page: free models allow 20 requests a minute, **50 a day with under $10 of credit**, and 1,000 a day after $10 has been bought. The cap is per account, so extra keys do not add more. The old bot spent up to 7 of those 50 on probes per run (old 882). It also chose the **biggest** free model (old 876), which is the most congested and often returns "rate-limited upstream". In your case the key itself is gone (`User not found`). | Pinned `meta-llama/llama-3.3-70b-instruct:free`, budget 45 a day, one shared counter per account (`*free*` in AI Usage). `free-models-per-day` -> exhausted until the reset. |
| 11 | (g) Key sent to the wrong provider by secret name | Possible, not seen | `env_keys()` (old 50-58) trusts the secret name. A Groq key pasted into `GEMINI_KEY` goes to Google, which answers 400 "API key not valid". The old code then switches that key off. Your file labels match the prefixes. | Keys are routed by **prefix** (`AIza` Gemini, `gsk_` Groq, `sk-or-` OpenRouter). A mismatch prints a warning with the last 4 characters only. Test: `keys_routed_by_prefix`. |
| 12 | 400 errors switch the model off for **all** keys | Code risk | `classify()`: any 400 -> `BadModel` (old 744-745), which kills the model for every key (old 964-966). One bad request or a region error ends the whole provider. | 400 is a model error only when the text says so. Key errors are told apart from model errors, and every state is per slot. |

## Real API answers (2026-10-31, keys masked)

```
Keys file: 2 key value(s) found.   Per label: {'GROQ_KEY': 1, 'OPENROUTER_KEY': 1}   (GEMINI_KEY: none)
[1] GROQ_KEY ...Bxqh (Groq)
  list models (Python default User-Agent): HTTP 403   provider says: error code: 1010
  list models (custom User-Agent):          HTTP 401   {"error":{"message":"Invalid API Key","type":"invalid_request_error","code":"invalid_api_key"}}
  generate llama-3.1-8b-instant:            HTTP 401   same
[2] OPENROUTER_KEY ...ec1d (OpenRouter)
  key info /api/v1/key:                     HTTP 401   {"error":{"message":"User not found.","code":401}}
  generate meta-llama/llama-3.3-70b-instruct:free and openrouter/free: HTTP 401 same
Gemini: no key in the file. A fake AIza key returns HTTP 400 API_KEY_INVALID, so the endpoint and the script work.
```
There are no quota headers here: a 401 is returned before any rate limiter. Run **diagnose-keys** with your real
GitHub secrets to see `x-ratelimit-*` (Groq/OpenRouter) and Gemini's quota IDs.

## Simulation of the old code (fake providers, fake clock, no network)

```
old start-up (3 Gemini keys, 1 Groq, 1 OpenRouter):
  13 HTTP calls before email 1, 8 of them generations. 6 hit the shared Gemini counter.
  "Gemini key 1..3: using gemini-flash-latest, gemini-3.8-flash | Groq key 1: REJECTED | OpenRouter key 1: REJECTED"
old daily (3 keys in ONE project, 6 start-up tests already used, 4 s pause):
  RPM 5,  RPD 20, 2 calls/email -> 11 emails     RPM 5, RPD 20, 3 calls/email -> 7 emails
  RPM 5,  RPD 10, 2 calls/email -> 4 emails      RPM 5, RPD 5,  3 calls/email -> 1 email
  RPM 10, RPD 20, 2 calls/email -> 16 emails     RPM limit only, no daily cap -> survives 50 emails
```
Takeaway: the 1-2 email deaths match a **small shared daily quota**, drained by start-up tests and repeat calls, with
Groq/OpenRouter already marked "REJECTED" at start-up. Per-minute 429s alone do not explain it.

## What I could not verify

- Your **Gemini keys** (they are only in GitHub secrets) and which project each one belongs to. Run **diagnose-keys**,
  and in AI Studio open *API keys*: the "Project" column shows whether all 3 sit in one project.
- Exact current free numbers per Gemini model. Google's page no longer lists them and says to check AI Studio. The
  same goes for the Groq free plan (console.groq.com/settings/limits). The bot learns the real cap from the first
  per-day 429 anyway.
- Whether the keys were auto-revoked after a leak or deleted by hand. Both give the same 401.
