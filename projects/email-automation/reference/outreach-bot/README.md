# outreach-bot v3

Drafts cold emails from all your lead sheets (one per country, plus a YouTube and an AU-only sheet) into one
**Outreach** Google Sheet. It sends nothing. You copy and send by hand; automatic sending is parked and OFF.

- **Read-only on lead sheets.** Columns are found by header name, every sheet is optional, and duplicates across
  sheets are removed by Place Id and email.
- **Outreach sheet tabs.**
  - **Leads**: append-only.
  - **Emails**: `Email | First Name | Subject | Email body | ...`.
  - **Options**: every switch is off by default.
  - **Email Rules**: your own writing rules.
  - **Inboxes** and **AI Usage**.
- **Every email is written from facts.** The bot never copies template text found in a lead sheet. It adds a legal
  footer for the lead's country (US, AU, CA, GB, IE, NZ and others). GB and IE free-mail addresses are skipped.
- **Free AI keys** (Gemini, Groq, Mistral, OpenRouter):
  - A masked registration report runs at the start, and no test calls are made.
  - Calls are paced, and a rate-limited key stops for the day.
  - Unwritten leads wait for the next run.
- **Optional:**
  - Inbox rotation with warm-up caps, plus one queue view per inbox.
  - Follow-ups on day 3 and day 7, in the same thread from the same inbox.

**Start with `START_HERE.md`.** Then read `SECRETS_GUIDE.md` and `INBOX_OPTIONS.md`.

```
pip install gspread
python selftest.py     # offline tests, no network
python generate.py     # needs GOOGLE_SA + OUTREACH_SHEET_ID (+ SHEET_ID_<COUNTRY>, AI keys)
```
