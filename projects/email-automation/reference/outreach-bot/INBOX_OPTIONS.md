# INBOX_OPTIONS: sending from 12-13 accounts

The bot only drafts. Everything below is about how YOU send. Prices are list prices as last published and change
often: check the vendor page before you pay. Domains, DNS and warm-up basics are in `INBOX_SETUP.md`.

## Switches in the Outreach sheet (Options tab, all OFF by default)

### INBOX_ROTATION (Off)
Turn on:
1. Fill the **Inboxes** tab, one row per account: `Inbox Address` | `Daily Cap` (e.g. 30) |
   `Warm-up Start (YYYY-MM-DD)` (the day you start sending from it) | `Active (Yes/No)`. Rows starting with `#` are
   ignored.
2. In **Options**, set `INBOX_ROTATION` to `On`. Optional: `WARM_START` (5), `WARM_STEP` (2), `INBOX_MAX` (50).
3. On the next run, every new email gets an **Assigned Inbox** (round-robin). An inbox's cap for the day is
   `WARM_START + WARM_STEP x days since its warm-up start`, never above its Daily Cap or `INBOX_MAX`. The first
   emails AND the follow-ups due that day both count. The bot drafts only as many as your inboxes can send today; the
   rest stay queued.
4. One **Queue <inbox>** tab per inbox appears (QUERY views, rewritten every run so they survive moved columns):
   A = first emails to send (Status `Drafted`), F = Follow-up 1 due, J = Follow-up 2 due. Log into that inbox, copy
   that inbox's batch, send, then set Status in the **Emails** tab.

### FOLLOW_UPS (Off)
Turn on: set `FOLLOW_UPS` to `On` (optional `FU1_DAYS` 3, `FU2_DAYS` 7). Each new email then also gets
Follow-up 1 / Follow-up 2 subject + body (written in the same AI call, no extra cost) and due dates.
- Send a follow-up as a **reply in the same thread, from the same inbox** as the first email (the subject is
  `Re: <subject>`). The Queue tab shows it only for its own inbox.
- Status flow in the Emails tab (you type it): `Drafted` -> `Sent` -> `Follow-up 1 sent` -> `Follow-up 2 sent`.
  When you set `Sent`, the next run writes **Sent On** and moves both due dates to count from that day.
- `Replied`, `Bounced`, `Do not contact` stop everything: no follow-up shows up for those rows.

## The real-world options, honest costs

| | What it is | Rotation / warm-up / follow-ups / stop on reply | Cost | Effort per day (300 emails) |
|---|---|---|---|---|
| **A. Manual** (now) | Copy from the Queue tabs into each Gmail / Outlook account | rotation and follow-ups from the bot's tabs; warm-up = you keep to the caps; you watch for replies | **Free** | High: about 1 minute per email = about 5 hours |
| **B. Parked sender** (`phase2_parked/`) | GitHub Actions sends through each account's SMTP (app password) and reads replies over IMAP | yes / ramp only (no warm-up network) / yes / yes | **Free** | Low after setup. Risk: providers dislike scripted SMTP; one bad day can get an account limited |
| **C. Mail-merge add-on per account** (YAMM, Mailmeteor, GMass) | Gmail add-on sends a sheet of rows from that one account | per account only / no / GMass yes, others limited / partly | roughly $0-25 per account per month; free tiers send about 20-50 a day | Medium: run it in 12-13 accounts every day |
| **D. Cold-email platform** (Instantly, Smartlead; also Saleshandy, Lemlist) | Connect all inboxes once, upload a CSV, the platform sends | **all built in**: rotation, warm-up network, follow-ups in thread, stop on reply, bounce handling | Instantly or Smartlead entry plans about $37-39 a month with unlimited inboxes and warm-up; Lemlist costs more per user | Lowest |

Costs you have with every option: domains (about $10-15 a year each) and mailboxes (Google Workspace about $7-8 per
user per month, Microsoft 365 about $6) if the accounts are not on your own domains yet.

## My recommendation for 12-13 accounts

1. **Do not cold-email from free @gmail.com / @outlook.com accounts.** Their terms forbid bulk unsolicited mail and
   they get limited fast. Use 3-4 secondary domains (e.g. `get<brand>.com`) with 3-4 inboxes each, SPF + DKIM +
   DMARC set (`INBOX_SETUP.md`).
2. **Best value: option D, Instantly or Smartlead (about $37-39 a month in total, not per inbox).** With 12-13 inboxes
   the warm-up network, reply detection and in-thread follow-ups replace hours of manual work. Export the **Emails**
   tab to CSV and map `Email`, `First Name`, `Subject`, `Email body` (and `Follow-up 1/2 Body`) as custom fields; keep
   the platform's own unsubscribe link on. Leave `INBOX_ROTATION` Off (the platform rotates), keep `FOLLOW_UPS` On.
3. **Until you pay for that: option A** with `INBOX_ROTATION=On` and `FOLLOW_UPS=On`, 20-30 per inbox per day after
   2-3 weeks of warm-up (cap 50). 12 inboxes x 25 = about 300 a day.
4. Option B is free and works, but needs app passwords for 12-13 accounts and gives no warm-up network. Use it
   only if C/D are not possible.

## Compliance (every option)
The bot adds a footer for the lead's country when Options `SENDER_NAME` and `SENDER_ADDRESS` are set:
US CAN-SPAM (postal address + opt-out), AU Spam Act 2003 (who you are + unsubscribe; inferred consent from a
published business address), CA CASL (mailing address + contact details + unsubscribe processed within 10 business
days), UK PECR and IE ePrivacy/GDPR (who you are + opt-out; corporate subscribers only). In GB/IE, free-mail addresses
are skipped (`STRICT_B2B=On`), and names without Ltd / LLP / PLC get a "may be a sole trader" flag: check those
before sending. The `Flags` column tells you why. Honour every unsubscribe within 10 days and never re-add the
address. This is practical guidance, not legal advice.
