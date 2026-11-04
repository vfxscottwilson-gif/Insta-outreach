# outreach-bot v3: hand-over (2026-11-01)
Folder: D:\All Automations Records\Draft Creating automation Code\outreach-bot. Zip: ..\outreach-bot-v3.zip (19 files).
Built against Lead generation\CONTRACT.md v5. Selftest: 58/58 passed on Python 3.12, pyflakes clean.

## Reading the lead sheets
- Reads every SHEET_ID_<AU|AU_ONLY|US|CA|GB/UK|IE|NZ|AE|SA|QA|YOUTUBE>, plus EXTRA_LEAD_SHEET_IDS.
  The old SHEET_ID is used only when none of these is set. Each value may be a bare ID or the full sheet URL.
- A missing or unreadable sheet logs "SKIP <label>: ..." and the run carries on.
- Lead tab = a header row with both Place Id and Company Name. All Leads, OLD tabs and control tabs are ignored.
  Rows matching the sheet's Blacklist tab are skipped.
- Columns are matched by header name. The COLUMN_ALIASES option can add more names.
- Old rows without Lead Insight fall back to Case Study, then Pitch Angle.
- Duplicates are removed across sheets by Place Id or any shared email; the first sheet in the order above wins.

## Writing
- It NEVER writes to a lead sheet; the tests make every lead tab raise on any write. The earlier write-back to the
  niche tabs is removed.
- Output goes to OUTREACH_SHEET_ID, with these tabs:
  - Leads: append-only, with a Note.
  - Emails: Email | First Name | Subject | Email body | Company | Place Id | Country | Niche | Assigned Inbox |
    Drafted On | Status | FU1 Due | FU2 Due, then Sent On, the FU subjects and bodies, Written By and Flags.
  - Options, Email Rules, Inboxes and AI Usage.
- The ledger is the Emails tab (Place Id + email), so a lead is never drafted twice.

## AI keys
- One secret per key: GEMINI_API_KEY_1..5, GROQ_API_KEY(_2), MISTRAL_API_KEY, OPENROUTER_API_KEY. The old combined
  names still work.
- Each key is trimmed and format-checked. A masked report at the start shows REGISTERED / IGNORED / duplicate /
  not set.
- 429 handling: the first per-minute 429 pauses that key and the next key is used. A second 429, or a per-day 429,
  marks the key exhausted for the day.
- When every key is spent, the remaining leads stay queued. TEMPLATE_FALLBACK=On (default Off) uses the template
  instead.
- A Cloudflare 403 with error code 1010 never marks a key bad.

## Options (all off by default)
- INBOX_ROTATION: assigns inboxes round-robin under warm-up caps and makes "Queue <inbox>" QUERY tabs.
- FOLLOW_UPS: adds follow-ups on day 3 and day 7. When the user sets Status to Sent, the bot fills Sent On and
  re-dates the follow-ups.

## Compliance
- A footer is added per country: CAN-SPAM, the Spam Act, CASL, PECR and IE ePrivacy. It needs SENDER_NAME and
  SENDER_ADDRESS in Options.
- GB/IE free-mail addresses are skipped (STRICT_B2B=On). Possible sole traders are flagged.

## Sheets quota
- Reads are spaced 3.2 s apart, at most 19 a minute (contract 4.6). Writes are spaced 1.1 s apart.
- Measured for 11 sheets and 700 drafts: 60 reads and 43 writes, about 3.6 minutes.

## Parked sender
- send.py and replies.py now use the Emails tab Status. They are still OFF.
