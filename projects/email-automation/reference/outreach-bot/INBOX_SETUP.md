# INBOX SETUP for 400-700 emails a day (sending is OFF until you finish this)

## 1. How many inboxes and domains

Safe limit for cold email: **30-50 a day per inbox**, and at most **3 inboxes per domain**. Never send cold email from
your main website domain. Buy look-alike domains (for example `getdoemedia.com` or `doemedia.co`) and point their
website to your real one.

Follow-ups count as sends. With 2 follow-ups, every new lead turns into up to 3 emails. In steady state:
total sends a day ≈ new leads a day x about 2.6.

| Goal | Sends a day | Inboxes at 40/day | Domains (3 inboxes each) |
|---|---|---|---|
| 400 sends a day, follow-ups included (≈150 new leads) | 400 | **10** | **4** |
| 700 sends a day, follow-ups included (≈270 new leads) | 700 | **18** | **6** |
| 400 NEW leads a day + 2 follow-ups | ≈1,050 | **27** | **9** |
| 700 NEW leads a day + 2 follow-ups | ≈1,800 | **45** | **15** |

Start with the first row: 10 inboxes on 4 domains. Add domains in groups once the reply and bounce numbers look healthy.
Drafting 700 a day is cheap. Sending 700 *new* leads a day needs around 45 inboxes.

## 2. Warm-up timeline (built into send.py)
- Week 0: buy the domains, create the inboxes, add SPF/DKIM/DMARC, and wait 3-7 days. Send a few real emails by hand
  to friends and clients and reply to them. Optionally turn on a warm-up tool.
- Day 1 of sending (`start_date` in SENDING_INBOXES): **5 a day per inbox**, +2 a day (WARM_START / WARM_STEP).
  That gives 25 a day by day 11 and 40 a day by day 19 (`max_per_day`, hard ceiling 50).
- Keep the bounce rate under 2% and the spam-complaint rate under 0.1% (Gmail's hard line is 0.3%).
  If either goes over, pause that domain for a week.
- Keep warming in the background for as long as an inbox is in use.

## 3. DNS for every sending domain (at your domain registrar)
| Record | Value (example for Google Workspace) |
|---|---|
| SPF (TXT on `@`) | `v=spf1 include:_spf.google.com ~all` (Zoho: `include:zoho.com`). Only ONE SPF record per domain |
| DKIM (TXT) | Generate it in the admin console (Google: Apps > Gmail > Authenticate email; Zoho: Mail Admin > Domains > DKIM), add the TXT, then click "Start authentication" |
| DMARC (TXT on `_dmarc`) | `v=DMARC1; p=none; rua=mailto:dmarc@yourdomain.com` at first. After 2-4 clean weeks, change to `p=quarantine` |
| MX | Your mail provider's MX records, so replies arrive |
| Redirect | Website forward from the look-alike domain to your main site |

Check each domain with mail-tester.com (aim for 9/10 or better) and with Google Postmaster Tools.
Google and Yahoo require SPF + DKIM + DMARC and easy unsubscribing from bulk senders. Microsoft has required the same
since 2025.

## 4. Provider options (approximate prices; check before you buy)
| Option | Cost per inbox / month | Notes |
|---|---|---|
| **Google Workspace** Business Starter | about US$7-8 | Best inbox placement to Gmail. SMTP `smtp.gmail.com:465` + IMAP, using an app password (needs 2-step verification) |
| **Zoho Mail** Mail Lite | about US$1-2 | Cheapest real mailbox. SMTP `smtp.zoho.com.au:465` (AU data centre) or `smtp.zoho.com`, IMAP `imap.zoho.com.au` |
| **Microsoft 365** Business Basic | about US$6 | Good for Outlook-heavy recipients. SMTP `smtp.office365.com:587` (STARTTLS) |
| Domains | about US$10-15 a year each | `.com` is safest. Avoid very cheap new TLDs for cold email |
| Warm-up tool (optional) | about US$15-40 a month | Not required. The built-in ramp plus manual sends is enough to start |

**Do not use** transactional senders (Amazon SES, SendGrid, Mailgun, Brevo...) for cold email. Their terms forbid
unsolicited email, and they close accounts that send it.
Budget example, 10 inboxes on 4 domains: Zoho about US$15/mo + domains about US$50/yr, or Google about US$80/mo
+ domains.

## 5. Legal: Spam Act 2003 (AU) and CAN-SPAM (US)
send.py adds these to every email automatically and refuses to send if any is missing:
- your name (`SENDER_NAME`) and business (`AGENCY_NAME`)
- a **physical postal address** (`SENDER_ADDRESS`; a PO box is fine)
- an opt-out line ("Reply unsubscribe") and a `List-Unsubscribe` header. Set `UNSUB_URL` (an https page) to add one-click unsubscribe.
- Under the Spam Act, opt-outs must be honoured within 5 working days. replies.py puts them in the **Suppression** tab
  and sets the lead to **Do not contact** on the next run.
- Under the Spam Act you need consent. "Inferred consent" covers a business address that is conspicuously published
  (for example on their website), when the email is relevant to their business and the page does not say "no
  unsolicited email". The lead bot collects published business addresses. Keep it that way.

## 6. Fill in the secret (GitHub > Settings > Secrets > Actions > `SENDING_INBOXES`)
```json
[{"email":"alex@getdoemedia.com","name":"Alex Doe","password":"APP-PASSWORD","smtp_host":"smtp.gmail.com",
  "smtp_port":465,"imap_host":"imap.gmail.com","start_date":"2026-11-10","max_per_day":40},
 {"email":"alex@doemedia.co","name":"Alex Doe","password":"APP-PASSWORD","smtp_host":"smtp.zoho.com.au",
  "smtp_port":465,"imap_host":"imap.zoho.com.au","start_date":"2026-11-10","max_per_day":40}]
```
Then follow ROADMAP.md step 6 to switch sending on, with a dry run first.
