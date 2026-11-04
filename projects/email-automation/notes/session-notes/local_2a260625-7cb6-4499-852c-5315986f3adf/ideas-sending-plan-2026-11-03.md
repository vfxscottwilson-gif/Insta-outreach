# Sending plan (from the Ideas chat, 2026-11-03)

## Decision (user, 2026-11-03)
- Send under ONE real identity (the user's real name + Haroon VFX brand) on secondary domains.
- The 14 free @gmail.com persona accounts (listed in `Full Cycle Emails Outreach File/CLAUDE_MAX_BUILD_PROMPT.md`) are retired from cold email.
- Still open: does "400-700/day" mean total sends or new leads; monthly budget ceiling.

## Brief for the Control Room
Act as a senior email-deliverability engineer. Goal: move cold sending off the 14 free Gmail persona accounts onto a
compliant, warmed setup and pilot it.
(1) Prepare a buy list: 4-5 secondary .com domains and 10 mailboxes (2-3 per domain), all under the user's real name
with the Haroon VFX brand. Compare Google Workspace with Zoho Mail Lite, prices checked 3 times and dated. The user makes
every purchase; ask for the budget ceiling first.
(2) Give the exact SPF/DKIM/DMARC/MX records per domain; check each domain with mail-tester (aim for 9/10 or better).
(3) Choose Smartlead Pro or Saleshandy Pro: verified prices, trial availability, CSV custom fields for Subject, Body and
Follow-up 1-2. Write the export mapping from outreach-bot v3's Emails tab. No changes to the bot's sending code;
leave `phase2_parked` off.
(4) Fix `INBOX_OPTIONS.md` (the $37-39 entry plans cap at 5-6k emails/month, so that recommendation is outdated) and
mark the 14-Gmail account list in `CLAUDE_MAX_BUILD_PROMPT.md` as retired. Update `PROGRESS.md`.
(5) After 2-4 weeks of warm-up, pilot 10 inboxes at 30/day for 2 weeks. Done when a pilot report shows bounce under 2%,
spam complaints under 0.1%, and replies and booked calls per 1,000 sends.
Report: buy list, DNS table, tool decision with sources, pilot sheet link.

## Verified facts (checked 2026-11-03; NV = not verified)
- Gmail Program Policies: "Don't use Gmail to distribute spam or unsolicited commercial mail."
  https://support.google.com/mail/answer/16734397
- Daily limits: free Gmail 500/day (https://support.google.com/mail/answer/22839); Workspace 2,000/user/day
  (https://knowledge.workspace.google.com/admin/gmail/gmail-sending-limits-in-google-workspace).
- Bulk-sender rules (5,000+/day) for Google/Outlook; 400-700/day is under the threshold, but SPF/DKIM/DMARC still
  apply. Google spam rate: keep under 0.10%, never 0.30% (https://support.google.com/a/answer/81126).
- Capacity: with 2 follow-ups, sends = new leads x 2.6 (`outreach-bot/INBOX_SETUP.md`). 13 inboxes x 30-40/day =
  390-520 sends = about 150-200 new leads/day. 400 NEW leads/day needs about 27 inboxes.
- Vendor guidance (not official limits): Instantly 30/day per inbox, 2+ weeks warm-up, 2-3 inboxes per domain;
  Smartlead 50 or fewer per day, 14 days warm-up (21-30 for new domains).
- Tool prices (official page + independent sources; conflicts noted):
  | Plan | Monthly | Annual/mo | Emails/mo |
  |---|---|---|---|
  | Smartlead Pro | $94 | $78 | 90k (2 blogs say 150k) |
  | Saleshandy Pro | $99 | $76 | 100k |
  | Instantly Hypergrowth | $107 | $85.58 | 125k (2 blogs say $97 / $77.60) |
  | lemlist Email | $69 | $55 | 50k (per-user vs per-team unclear) |
  Entry plans (about $37-39) cap at 5-6k emails/month: too small for 9k-21k/month.
- Harvey: docs point to one mailbox (about 50/day max, `max_daily_sends`); multi-inbox rotation only via Instantly (NV
  in code). Good later for reply handling.
- Law (not legal advice): US CAN-SPAM is opt-out, with honest From/headers and a postal address; CA CASL, AU Spam Act
  and NZ need consent (inferred/implied from a conspicuously published, role-relevant address); UK sole traders need
  consent; all require sender identification and an unsubscribe.
- NV: domain, Workspace and Zoho prices; Smartlead/Saleshandy free trials.
