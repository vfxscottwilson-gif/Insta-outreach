# START HERE: outreach-bot v3 (drafts only; you send by hand; automatic sending is parked and OFF)

What it does: reads every lead sheet (one per country, plus YouTube and AU-only), removes duplicates, and writes
one email per lead into YOUR **Outreach** sheet. Lead sheets are only read, never written.
It is built against `D:\All Automations Records\Lead generation\CONTRACT.md` (v5):
- Lead tabs are found by their `Place Id` + `Company Name` headers.
- `All Leads` and the `OLD ` tabs are ignored.
- The `Blacklist` tab is respected.
- Reads stay at 19 a minute or fewer, because the lead bot shares the service account.

## Setup, step by step (about 30 minutes)

1. **Make the Outreach sheet.** sheets.new > name it "Outreach". Copy the ID from the URL (`/d/<ID>/edit`).
2. **Share the sheets** with the service account email (the `client_email` inside your `GOOGLE_SA` JSON):
   the Outreach sheet as **Editor**, every lead sheet as **Viewer**.
3. **GitHub secrets** (repo > Settings > Secrets and variables > Actions > New repository secret). Full table:
   `SECRETS_GUIDE.md`.
   - `GOOGLE_SA` = the whole service-account JSON. `OUTREACH_SHEET_ID` = the ID from step 1.
   - One `SHEET_ID_<COUNTRY>` per lead sheet you have (`SHEET_ID_AU`, `SHEET_ID_US`, ..., `SHEET_ID_YOUTUBE`,
     `SHEET_ID_AU_ONLY`). Leave out the ones you don't have.
   - AI keys, one secret per key: `GEMINI_API_KEY_1..3` (each from its OWN Google Cloud project), `GROQ_API_KEY`,
     `MISTRAL_API_KEY`, `OPENROUTER_API_KEY`. Without any key, set `TEMPLATE_FALLBACK` to `On` (step 7).
4. **Upload the code.** Copy the contents of `outreach-bot-v3.zip` over the repo and delete files that are not in
   the zip. Then:
   ```
   git add -A
   git commit -m "outreach bot v3: multi-sheet, Outreach sheet, Email Rules, options"
   git push
   ```
5. **Test the keys.** Actions > **diagnose-keys** > Run workflow. Every key should show `REGISTERED` and then
   `HTTP 200`. `IGNORED` = re-copy that key. `401` = the key is wrong or revoked. `limit: 0` = that model has no free
   quota in that project.
6. **Dry run.** Actions > **generate-emails** > Run workflow with `dry_run` = `On`. In the log, check:
   the `SKIP` / `READ` line for every sheet, the key registration, and `DONE. ... written N`. This first run also
   creates the tabs **Leads, Emails, Options, Email Rules, Inboxes, AI Usage** in the Outreach sheet.
7. **Options tab** (Outreach sheet): fill `SENDER_NAME` and `SENDER_ADDRESS` (needed for the legal footer), and
   optionally `AGENCY_NAME`, `SENDER_WEBSITE`. Leave the rest as is for now.
8. **Email Rules tab**: paste your own writing rules, one per row. Word limits ("between 60 and 110 words"), banned
   words ("Never use these words: a, b, c") and "No links" are also checked in code; everything else goes to the AI.
9. **Real run.** Run **generate-emails** again with `limit` = `20` (dry_run empty). Open the **Emails** tab:
   `Email | First Name | Subject | Email body | ...`, Status `Drafted`. The **Leads** tab shows every lead pulled in,
   with a Note saying why it was or was not queued.
10. **Daily.** The schedule runs at 10:00 UTC and drafts up to `DAILY_TARGET` (400). Copy each email into your mail
    account, send it, then set Status to `Sent`. Set `Replied` / `Bounced` / `Do not contact` when that happens.
    The bot never drafts the same lead twice (it checks Place Id and email in the Emails tab).

**Multi-inbox and follow-ups** (both Off): activation steps and my recommendation are in `INBOX_OPTIONS.md`.

## Files

| File | What it is |
|---|---|
| `generate.py` | The bot (one file). |
| `rules.md` | Base AI rules. Your own rules go in the **Email Rules** tab. |
| `selftest.py` | 58 offline tests; they also run before every GitHub run. `pip install gspread` then `python selftest.py`. |
| `tools/diag_keys.py` | Real but tiny key test (masked). The **diagnose-keys** workflow runs it with your secrets. |
| `.github/workflows/` | `generate.yml` (daily + manual) and `diagnose-keys.yml` (manual). |
| `phase2_parked/` | Automatic sending (OFF). |
| `SECRETS_GUIDE.md` | Every secret and variable, formats, free limits, and why the old keys "burned". |
| `INBOX_OPTIONS.md` | Manual vs parked sender vs add-ons vs platforms, costs, recommendation. |
| `INBOX_SETUP.md` | Domains, DNS (SPF/DKIM/DMARC) and warm-up. |
| `DIAGNOSIS.md` | The original key diagnosis with evidence. |
| `ROADMAP.md` | Realistic drafts per day and what to do next. |

## How an email is written
- Facts only: Lead Insight, niche, city, country, website summary, social gap, reviews. Draft or subject text found in
  a lead sheet is never copied (the code rejects any AI text that shares 8 words in a row with it).
- Greeting: `Hi <first name>,` only when the Decision Maker Name is a verified fact (titles removed; `Dr Smith`
  stays), else `Hi <Company> team,`.
- Subject: 2-7 words (the AI is asked for 3-7), max 45 characters, no `!`, no spam words, not all capitals.
- Body: greeting, 45-130 words (the AI is asked for 55-110), the question last, `Best regards,`, your name, then
  the legal footer for the lead's country.
- AI: 5 leads per call, paced, no test calls. When every key is spent, the rest waits for the next run
  (`TEMPLATE_FALLBACK=On` = use the built-in template instead).
- The GitHub log never shows emails, names or key values (keys only as the last 4 characters).
