# BUILD PROMPT: Fully automated cold-email outreach system (Google Sheets + Gmail API + GitHub Actions)

You are a senior Python/automation engineer and a cold-email outreach specialist with 10+ years of experience. Build the complete system described below. Read the whole brief first. Do not ask me questions: where something is unspecified, choose the safest sensible default, put it in the Settings tab/config, and note it in START_HERE.md.

## 0. How to deliver

Deliver in phases. After each phase, list every file created, the exact commands to test it, and what I should see. Then wait for me to say "next".

- **Phase 1:** repo skeleton, config loader, Google Sheets layer, sheet creation (all tabs + headers + formatting), Settings, Health Check, dry-run mode.
- **Phase 2:** header-agnostic lead importer, suppression, dedupe, country/niche/timezone inference.
- **Phase 3:** accounts, caps, ramp, Gmail OAuth helper, sending engine (with threading), Send Log.
- **Phase 4:** AI layer (API-agnostic), email composer + validator, signature, drafts generation (weekend batch).
- **Phase 5:** scheduler (timezones, windows, business days, holidays, capacity planner, weekend follow-up lane).
- **Phase 6:** reply scanner, fuzzy label mapping, inbox-moving, classification, human takeover.
- **Phase 7:** notifications (Telegram + alternatives), Daily Report, Dashboard, Alerts.
- **Phase 8:** GitHub workflows, tests, START_HERE.md, OPTIONAL_TOOLS.md, hardening pass.

Write Python 3.12. The only hard dependencies are `gspread` (or Google Sheets API client), `google-auth`, `google-auth-oauthlib`, `google-api-python-client`, `requests`, `holidays`, `PyYAML`, and the standard library (`zoneinfo`, `difflib`, `email`). Avoid heavy dependencies. Everything must run free on GitHub Actions and on my local PC (Windows, VS Code, Python installed).

**Rules for the code:**
- Never crash the whole run because of one bad row, account or provider. Catch, log (no personal data), alert, continue.
- Everything must be idempotent and safe to re-run, because GitHub scheduled runs can be late, duplicated or skipped.
- A `DRY_RUN` mode must do everything except send email, apply Gmail labels, and write to source sheets.
- Never write to the lead source sheets (read-only).
- Include unit tests (pytest) for: caps/ceilings, ramp, business-day math, time-zone windows, header detection, label fuzzy matching, validator, template rendering, thread headers, classification rules, planner allocation.

## 1. Business context

- I am a video editor and motion designer. I offer short-form (Reels/TikTok/Shorts), long-form editing and motion graphics to YouTubers, brands and local businesses.
- Targets: USA, Canada, Australia. All leads end up in one master tab, each tagged with country and niche (YouTubers, restaurants, real estate, auto, etc.).
- The main person/brand is **Haroon VFX** (spelling to be kept in a config value; the agency is not formally set up). Outreach is sent from 14 Gmail accounts "on behalf of" Haroon VFX.
- I already have a separate GitHub bot that generates leads into Google Sheets. It is out of scope. This system **reads** those sheets (5–7 source sheets, possibly several tabs each, headers unknown/inconsistent).
- Offer in every email: a **sample edit of 30–60 seconds, at no cost**, before they decide anything. The sample/no-cost line must appear in **every** email, including every follow-up.
- Volume: about 600–900 sends/day now, expandable to ~2,000/day later by adding accounts. Total spending must stay minimal; free tiers or very cheap paid AI APIs only. No credit-card-required tools unless they sit in OPTIONAL_TOOLS.md.
- Public GitHub repo (see section 17).

## 2. Architecture (queue + short scheduled runs, not one long job)

Workflows (GitHub Actions, all with `concurrency` groups, `permissions: contents: read`, timeouts, and no PII in logs):

1. **import** (every 2–3 hours): read source sheets, normalize, dedupe, append new leads to `Leads`.
2. **plan** (daily weekday morning UTC + a long **weekend generation** run): admission control, write drafts, schedule.
3. **send** (every 10 minutes): send whatever is due now, respecting caps, windows, pacing.
4. **replies** (every 30 minutes): scan all accounts, classify, label, move out of inbox, update sheet, alert.
5. **report** (daily, default 15:00 UTC = 8:00 PM Pakistan time): Daily Report row + phone message.
6. **keepalive** (weekly): a tiny commit or API call so GitHub does not disable schedules after 60 days of inactivity in a public repo.

Each run starts by reading each needed tab **once** into memory (Sheets API quotas), and writes in **batches** (`values.batchUpdate`). It must tolerate a run starting 15–60 minutes late (catch-up behavior: send what is due, never skip, never double-send).

**Double-send protection:**
1. Before sending, write the draft row status `sending` with a unique claim token and re-read to confirm.
2. After the Gmail API returns, write the Gmail message ID and thread ID to the `Send Log` immediately.
3. If a run dies between send and write, the next run checks the account's Sent mail for that recipient and subject in the last 48 hours before retrying that row.

**Concurrency:** use the GitHub `concurrency` group so two sender runs never overlap, and also a lock row in Settings with a timestamp and 20-minute expiry.

**Alternative backend (design for it, don't build now):** a `SendBackend` interface with `GmailApiBackend` (default) so a non-Google domain mailbox could later use SMTP/IMAP.

## 3. Google Sheets design

All tabs are created automatically if missing, with frozen header rows, filters, column widths, number formats and data validation. **Match columns by header name, never by position**, and tolerate me reordering or adding columns. Most important columns come first. Date-time display format everywhere: `dd mmm yyyy hh:mm AM/PM` (e.g. "10 Sep 2026 02:30 PM"), stored as real date-time values so they sort. Add a settings option for uppercase text display if I want "10 SEP 2026".

**Tabs (in this order):**

1. **Dashboard**: totals today / 7 days / 30 days; sends by country, by niche, by account, by touch number; reply rate by country, niche, local send hour, weekday and account; bounce rate by account; cost estimate; capacity forecast chart (next 20 business days of planned sends vs capacity). Built from the Daily Report plus small summary tables the bot writes, using formulas so it updates live.
2. **Daily Report**: one row per date: date, new emails sent, follow-ups sent (touch 2, 3, 4, 5), total sent, replies (total), responses, not interested, auto replies, bounces/invalid, unsubscribes, reply %, bounce %, accounts active / paused / reduced, errors, AI provider used, tokens in/out, estimated AI cost (USD and PKR), emails drafted that day, leads imported that day, notes.
3. **Outreach** (the main send sheet; one row per lead). Columns in this order: Status, Email, First Name, Subject, Email Body (touch 1), Country, Niche, Next Send (their local time, 12-hour), Their Time Zone, Sender Account, Touch # Done, Reply Status (No / Yes – Response / Auto Reply / Not Interested / Invalid / Manual), Reply Snippet, Last Sent (their local), Follow-up 1 Sent, Follow-up 2 Sent, Follow-up 3 Sent, Follow-up 4 Sent, Channel/Company, City/State, Website, Source URL (consent evidence), Source Sheet, Source Row, Angle, Email Check Result, Lead ID, Notes.
4. **Drafts**: one row per planned email (touch 1–5): Lead ID, Touch #, Status (draft / ready / sending / sent / skipped / cancelled), Subject, Body (final composed text without signature), Scheduled (their local), Scheduled (UTC), Account, Generated By (ai / template / ai-light), Provider, Tokens In, Tokens Out, Rules Version, Generated At, Skip Reason.
5. **Send Log** (append-only ledger): Sent At (UTC and their local), Touch #, From Account, To, Subject, Gmail Message ID, Thread ID, Result, Error Code (HTTP status/short text, no body), Country, Niche, Lead ID, Local Send Hour, Weekday.
6. **Replies**: Received At, Account, Lead Email, Lead ID, Type (Response / Not Interested / Unsubscribe / Auto Reply / Bounce-Invalid / Wrong Person / Manual Conversation), Snippet (first 300 characters), AI Summary (1 line), Handled? (checkbox for me), Gmail Thread ID.
7. **Leads** (master): all imported leads with every normalized field plus an `Extra Data` JSON column with unmapped source columns.
8. **Accounts**: see section 5.
9. **Settings**: key / value / description / default / last changed. All tunables from this brief live here.
10. **Country Rules**: per country: IANA default timezone, send window start/end (local), weekend window, holiday calendar code (and subdivision), state/province→timezone table.
11. **Season Calendar**: date range, country, label, angle hint (e.g. Thanksgiving, Black Friday, Christmas, end of financial year, Melbourne Cup). The AI may only use these hints for seasonal lines.
12. **Templates**: follow-up templates 1–4, footer line, greeting, sample phrases, variant pools. Editable live in the sheet (repo has seed defaults).
13. **Signature**: signature lines, font, colour, per-account overrides (section 9).
14. **Suppression**: email, domain (optional), reason (unsub / bounce / replied / not interested / manual / auto reply / do-not-contact), date added, source.
15. **Sources**: each source sheet URL/ID, tab name, detected column mapping, confidence, manual override columns, last imported row, last import time, enabled flag.
16. **Label Map**: per account, per role: resolved Gmail label name, label ID, match type (exact / synonym / fuzzy / created), confidence.
17. **Capacity Forecast**: next 20 business days: planned follow-ups, planned new, capacity, utilization.
18. **Alerts**: time, severity, account (if any), message, acknowledged?
19. **Run Log**: workflow, start/end, counts, errors (no personal data).

## 4. Lead import: header-agnostic (I do not know the headers yet)

Do not rely on exact headers. For every tab of every source sheet:

1. Find the header row (scan the first 10 rows; score rows by how many cells look like header words).
2. Map columns using **both** header-name aliases (case/space/dash/underscore-insensitive, with fuzzy matching) **and content sniffing** (e.g., a column where most values match an email regex is the email column; URL patterns for website/YouTube/Instagram/LinkedIn; names such as "United States", "Canada", "Australia", "USA", "AU", "CA"; US/Canada/AU state and province abbreviations; phone codes +1/+61).
3. Required: email. Optional: name, company/channel, website, YouTube URL, socials, niche, city, state/province, country, phone, notes, latest video, subscribers (never sent to the AI), score/price (never sent to the AI), active/status.
4. Handle multiple emails in one cell (take the first valid; store the rest in Extra Data), merged cells, blank rows, duplicated headers, trailing spaces, mixed case.
5. If there's no country column, infer country from: the sheet/tab name (e.g. "Canada Restaurants Data" → Canada, restaurants), the address/state, phone code, or website TLD (.com.au, .ca). If still unknown → mark `Unknown` and **hold** the lead (never guess a time zone).
6. Infer niche similarly (tab name, a niche column, keywords in description). Store the confidence.
7. Write the detected mapping and confidence into the `Sources` tab so I can see it and override it per column. If mapping confidence for the email column is low, skip that tab and write an Alert instead of guessing.
8. Keep the original row number and sheet name in `Source Sheet` / `Source Row`, and the page where the email was found in `Source URL` if it exists (this is the consent evidence for Canada and Australia).
9. Normalize: lowercase emails, trim, validate syntax, reject blocked handles (noreply, postmaster, abuse, etc.) and fake domains (example.com, test.com), optional role-account handling via setting `ALLOW_ROLE_EMAILS` (default yes), disposable-domain list, DNS MX check (via DNS-over-HTTPS), optional external verifier (supply a pluggable function; QuickEmailVerification free tier 100/day etc. for risky leads only).
10. **Dedupe** by email (global), plus a domain cool-down setting `DOMAIN_COOLDOWN_DAYS` (default 30): do not email two people at the same business domain within that window unless I turn it off. Skip leads already on `Suppression`, already in `Send Log`, or whose Active/Status columns contain negative or stop words (no, false, 0, inactive, dead, closed, stop, unsubscribed, replied, bounced, invalid, dnc, blocked, sent). A lead that failed 3 times is skipped permanently.
11. Reuse the first-name rules from my old generate.py: take the name from a name column; reject brand words, multiple-word titles and handles; strip titles (Dr, Mr, Muhammad, etc.); fall back to a clean `first.last` in the email local part; AI-proposed names are accepted only if they appear in the lead's own data. If no name can be verified, greet with **"Hi there,"** (not "Hi Team").

## 5. Accounts, caps, ramp and fail-safes

**Accounts tab columns:** Email, Display Name, Account Type (auto: gmail / domain), Status (active / paused / reduced / disabled), Daily Cap (my setting), Effective Cap Today, Ramp Start Cap, Ramp Step, Ramp Day, Sent Last 24h, Sent Today, Sent 7 Days, Bounces 7 Days, Bounce % (last 100 sends), Replies 7 Days, Last Send, Last Error, Pause Until, Health Notes, Signature Override, Window Override, Gmail Auth OK?, Added Date.

**Seed accounts (load into the Accounts tab via a setup script. Do NOT commit these addresses to the repo; the repo is public. Read them from the sheet or a setup input file in `.gitignore`):**

| Display name | Email |
|---|---|
| Chris Ewart | vfx.chrisewart@gmail.com |
| Scott Wilson | vfx.scottwilson@gmail.com |
| Jack Roth | vfx.jackroth@gmail.com |
| Kris Taylor | vfx.kristaylor@gmail.com |
| William Gurbick | vfx.williamgurbick@gmail.com |
| Eric Steven | vfx.ericsteven@gmail.com |
| Josh Heller | joshvfx3@gmail.com |
| James Scott | jamesvfx3@gmail.com |
| Noah Walton | noahvfx3@gmail.com |
| Henry Wilson | henryvfx3@gmail.com |
| Micheal Gallick | vfx.michealgallick@gmail.com |
| Jason Harris | vfx.jasonharris@gmail.com |
| Richard Heller | vfx.richardheller@gmail.com |
| Brad Mills | vfx.bradmills@gmail.com |

(All fourteen are gmail.com, warmed accounts. Display name = signature name = From name, always the same.)

**Account type detection:** `gmail.com` or `googlemail.com` → type `gmail`; anything else → type `domain`. Never let a setting override the type.

**Hard ceilings in code (constants at the top of one file, easy to edit, each commented):** `GMAIL_MAX_PER_DAY = 70`, `DOMAIN_MAX_PER_DAY = 700`.

**Effective cap for an account on a given day = the minimum of:**
1. The Daily Cap in the Accounts tab.
2. The hard ceiling for its type.
3. The ramp cap. New accounts start at `Ramp Start Cap` (Gmail default 40, step +5/day; domain default 30, step +20/day) counting from the date the bot first sent from them. This protects me if I forget to set a cap on a new account.
4. The health cap (below).
5. The remaining headroom in the **rolling last 24 hours** (not the calendar day, because Australian and US windows straddle UTC midnight). Count from the Send Log and also from the account's Gmail Sent folder, so messages I send manually from that account also count against its limit.
6. The global total (`GLOBAL_DAILY_MAX`, which is only a maximum; total capacity = the sum of effective caps, so removing or lowering an account lowers the total automatically).

**If a cap cell is blank, text, zero by mistake or higher than the ceiling:** clamp to a safe value, write an Alert, and keep running. Never crash. Never exceed the ceiling.

**Pacing:** minimum random gap between sends from one account 60–240 seconds; maximum per account per hour 15 for gmail and 60 for domain (both in Settings); randomize the order of accounts; never send from all accounts at the same second. Add small random jitter to each send time.

**Health auto-rules (editable in Settings):**
- Bounce rate over the last 100 sends above 3% → halve the account's cap for 3 days and alert.
- Bounce rate above 6%, or any suspension, security-check, captcha, "account disabled" or repeated 403/`rateLimitExceeded`/`userRateLimitExceeded` errors → status `paused` for 72 hours and alert.
- Gmail's "daily sending quota exceeded" error → stop that account for the next 24 hours.
- The bot lowers caps automatically but **never raises** them. Only I raise caps.
- `Pause Until` is respected until it passes.

**Removing an account:** set Status to `disabled`. Its unsent touch-1 drafts are reassigned to other accounts. Its pending follow-ups follow the setting `ORPHAN_FOLLOWUPS` = `pause` (default) or `restart_new_thread` (restart from a different account as a new thread, flagged in the sheet).

**Authorization:** one Google Cloud project, one OAuth client, scope `gmail.modify` only. Publish the OAuth consent screen "In production" (not "Testing", which makes tokens expire in 7 days; an unverified app is fine for fewer than 100 users, and the warning screen is expected). Write `tools/authorize_account.py` to run locally (VS Code/Python): it opens the browser, I log into one account, it saves the refresh token, tests it, creates/resolves labels, and prints a JSON snippet to add to the GitHub secret `GMAIL_TOKENS` (one JSON object keyed by email address). Adding an account later = run this once, paste, add a row. If a token is revoked or expired, mark the account `Gmail Auth OK? = no`, pause it, and alert me.

## 6. Scheduling

**Business-day math.** Use my per-country holidays (via the `holidays` library with the country and state/province) plus Mon–Fri. Follow-up due date = previous actual send date + 5 business days (so the same weekday next week; a holiday shifts it by one day).

**Touches:** touch 1 = first email, touches 2–5 = follow-up 1–4. All follow-ups go in the **same Gmail thread**, from the **same account** as touch 1.

**Time zones.** Every lead has an IANA time zone (from the state/province/city table; country default if only the country is known; US states with two zones such as TX, FL, KY, TN, IN, MI, ID, OR, ND, SD, NE, KS need a city-level or county-level hint, otherwise use the majority zone and mark the lead "tz uncertain"). AU: AEST/AEDT, ACST/ACDT, AWST, Queensland (no DST), Tasmania, and so on. Use `zoneinfo`. Never guess: an unknown country is held.

**Send windows** (Country Rules tab, editable):
- Defaults: 08:30–12:30 local for US, CA and AU. Optional second window (off by default) 13:30–15:30.
- First emails: **Mon–Fri only**, skipping local public holidays.
- Follow-ups: normally Mon–Fri. Plus the **weekend lane** (below).
- Because AU, US East and US West mornings fall at different UTC hours, the sender each tick picks leads whose local window is open **now**. Mixed sheets work: leads whose window is closed wait. If only one region has leads, the other accounts' capacity simply goes unused.
- Each lead gets a scheduled local time inside its window, spread with jitter so there are no spikes. Log local send hour so the Dashboard can show reply rate by hour, and optionally rotate three slots (08:30, 10:00, 11:30) to learn the best one. I want the best time to be learned from my own data.
- Display format is the one in section 3, in 12-hour time, with a separate column for the time zone name (e.g. "EST – New York") and one for the country.

**Weekend lane (my decision).**
- First emails: never on weekends.
- Follow-ups **may** be sent on Saturday and Sunday (lead-local weekend) to drain a backlog. Setting `WEEKEND_FOLLOWUPS` (default on), `WEEKEND_CAP_PERCENT` (default 50% of the normal cap), window default 10:00–13:00 local.
- Weekend sends count toward each account's rolling 24-hour cap.

**Allocation between new leads and follow-ups (I asked for options B and C together, and a 30–35% share for new leads).**

Per sending day, with total effective capacity `C`:
1. **Priority with a floor (option B).** Follow-ups due (including slipped ones) go first, but new leads always keep at least `NEW_SHARE_MIN` of `C` (default 20%) so the pipeline never stalls. Target share for new leads: `NEW_SHARE_TARGET` = 30%. Ceiling: `NEW_SHARE_MAX` = 35%.
2. **Planned intake (option C).** Before admitting new leads, forecast the next 20 business days: scheduled follow-ups already planned, plus the projected follow-ups of the new batch, using a survival rate `SURVIVAL_RATE` (default 0.90) at each step. Admit the new leads only up to what keeps every future day under `C × (1 − NEW_SHARE_MIN)` for follow-ups.
3. **Honest consequence, which must be documented in START_HERE.md and shown in the Capacity Forecast tab.** With 4 follow-ups per lead, steady state supports roughly 22% new / 78% follow-ups. A permanent 30–35% new share would make follow-up demand exceed capacity (about 25–35% of follow-ups would be late or dropped). So:
   - `ALLOCATION_MODE = BALANCED` (default): the planner picks the new-lead number each day inside the band 20–35%, so new share floats near 30% during the first weeks while follow-up demand is low, and settles toward about 22% as follow-ups build up. Nothing is silently dropped.
   - `ALLOCATION_MODE = NEW_FIRST`: new share held at 30–35%; follow-ups that slip beyond `MAX_SLIP_BUSINESS_DAYS` (default 3) are dropped, oldest touch 5 first, and a Daily Report note/Alert says how many.
4. **Follow-up priority** (setting): touch 2 > touch 3 > touch 4 > touch 5; within a touch, the oldest due first.
5. **Slip:** a follow-up that cannot be sent today moves to the next available day (including the weekend lane) and stays in the same thread.
6. If a lead replies, bounces, unsubscribes, becomes `Manual` or `Auto Reply` before the follow-up is sent, **cancel** its remaining touches.

## 7. Drafts and weekend generation (to save AI cost)

- The planner writes drafts ahead of time. On **Saturday/Sunday UTC** it runs a long generation job that writes everything due next Monday–Friday (new first emails, and any follow-up personalization that uses AI), stored in `Drafts`. Weekday runs normally only send. The window is configurable (`GENERATION_MODE` = weekend_only / always / offpeak_hours) because AI providers' discount schedules change; prices and the off-peak definition live in `providers.yml`, never hardcoded.
- **At send time, always re-check:** the lead's status (replied, suppressed, bounced, manual), the account's health and caps, the holiday and the weekday. A draft older than `DRAFT_MAX_AGE_DAYS` (default 14) is regenerated. Seasonal lines must still be valid on the send date, otherwise they are dropped.
- Cache by lead hash: never regenerate an email whose inputs have not changed.

## 8. Email composition and validation

**Assembled by code, never by the AI** (in this order): greeting, AI/template body, opt-out line, sign-off, signature.

1. Greeting: `Hi {FirstName},` or `Hi there,`.
2. Body (written by the AI for touch 1; template-based for follow-ups).
3. Opt-out line (editable in Templates): `Not Interested, Reply "Unsub".`
4. `Best regards,` then the signature (section 9).

The AI must **not** write any greeting, sign-off, name, signature or unsubscribe line.

**Merged email rules** (save as `rules/email_rules.md`; this file is sent in compact form with every AI call, so keep it short. The full validator is in code):

- Sender: one person, video editor and motion designer, who works with YouTubers, brands and local businesses (short-form, long-form editing, motion graphics). Write as "I" and "me". Never "we", "our team" or "our editors". Never write a company or brand name or any person's name in the body (the signature carries identity).
- Offer: a 30–60 second sample edit made from their own clip (YouTubers) or a short sample made for their business (local businesses), **at no cost**, before they decide anything. The email must state clearly that the sample costs nothing.
- Allowed sample phrases (pick one per email, rotate): "at no cost", "no cost to you", "on me", "complimentary", "nothing to pay". The standalone word "free" is not used (setting `ALLOW_WORD_FREE` default false). Use it only about the sample.
- Structure (no greeting): 1) one short sentence about THEM (YouTubers: name the channel exactly as in the data; local businesses: company name plus one fact such as city, what they do, a social gap or reviews); 2) one short sentence on what they may be missing, said as a possibility, tied to the row's Angle; 3) what they get (my role and the sample; either one sentence or at most 3 bullet lines, each under 12 words, starting with "- ", only if it helps scanning); 4) **one** easy question as the very last line. YouTubers: ask them to reply with a clip or a video link. Local businesses: an easy one-line question.
- 60–100 words. Plain text. 2–3 short paragraphs, at most 2 sentences each, every sentence under 20 words, plain everyday words, readable on a phone. No links, emoji, exclamation marks, markdown, numbered lists.
- Use ONLY facts in LEAD DATA. Never invent numbers, clients, results, awards, people. Copy names and numbers exactly. If quoting a video title, copy it exactly inside double quotes. Use at most ONE other specific fact besides the channel/company.
- Never say you watched, visited, read or noticed anything; "came across" is the most allowed.
- Never mention prices, budgets, ad spend, views, subscribers, income or scores. Never criticise their videos or say they "need an editor". Say what they could gain.
- Banned words: guarantee, discount, risk-free, limited time, act now, no obligation, click here, urgent, free (unless `ALLOW_WORD_FREE`).
- Angles by row: `pain` (a likely problem as an observation or question, never as a claim about them), `missed` (one possibly under-used opportunity such as Shorts/Reels or consistent editing style), `default` (their channel/business, one thing they may be missing, then the sample). Niche hints from a niche→angle table in config (YouTuber, restaurant, real estate, auto, fitness, etc.). Seasonal lines come only from the Season Calendar.
- If `LOW_DATA` is yes: shorter, honest, talk only about their niche, mention no video or detail, still include the no-cost sample.
- Vary the first sentence and the question across emails (a `STYLE` index per lead).
- Subject: 2–6 plain words, at most 40 characters, no clickbait, no all caps, no "Re:", no "free". Follow-ups reuse the thread (Gmail shows "Re: <original subject>").

**Validator (code, runs on every email, AI or template):** word count (60–100 for touch 1; follow-ups 40–70, i.e. about 70% of touch 1), forbidden words/characters, links, emoji, exclamation marks, markdown, bullet count/length, last line is one question, the required sample phrase present exactly once and used only for the sample, channel/company name present when required, every number and quoted title appears in LEAD DATA, no greeting or sign-off inside the body. On failure: one cheap repair attempt (send only the failing text plus the specific error), then fall back to the deterministic template. Count the repair tokens.

**MIME (all in one place, no tracking at all):**
- `multipart/alternative`: a plain-text part (the whole email) and a minimal HTML part (only `<div>`/`<br>` with the signature in inline `font-family`/`color`).
- Absolutely no images, tracking pixels, open tracking, link tracking, hidden HTML, hidden text, external CSS or web fonts. Setting `SIGNATURE_HTML` (default true) can be switched to false for plain-text only.
- Set From as `Display Name <account@gmail.com>`. Do not set Reply-To.
- Add `List-Unsubscribe: <mailto:{account}?subject=unsubscribe>` (setting `LIST_UNSUBSCRIBE_MAILTO`, default on). Treat any message to an account with the subject "unsubscribe" the same as a reply of "Unsub".
- Threading for follow-ups: use the Gmail API `threadId` of touch 1, set `In-Reply-To` and `References` to touch 1's Message-ID, and subject `Re: <touch 1 subject>`.
- Identify messages sent by the bot by their Gmail message IDs recorded in the Send Log (no hidden markers in the email).

## 9. Signature (fully configurable, no images ever)

Edited in the `Signature` tab; per-account overrides allowed. Placeholders: `{account_name}`, `{title}`, `{behalf_line}`, `{brand}`, `{role_line}`, `{address}`, `{website}`, `{phone}`. Defaults:

```
Best regards,

{account_name}
Outreach Specialist
on behalf of Haroon VFX
Video Editor and Motion Designer
{address}
```

Font Georgia (fallback Georgia, "Times New Roman", serif), colour `#6E6E6E`, size 14px; the font/colour/size are in the Signature tab and apply to the signature block (setting `STYLE_BODY_TOO`, default false). Lines can be removed, reordered or added (physical address, number, website, any link) by editing cells. The "on behalf of" line is optional; an alternative layout is `{account_name}` / `Outreach Specialist` / `Haroon VFX`.

**Identity and legal note (put in START_HERE.md):**
- The name in the signature and the From name must be the real person or role who actually operates that account, or a clearly truthful role such as "Outreach Specialist, on behalf of Haroon VFX".
- US (CAN-SPAM), Canada (CASL) and Australia (Spam Act) all need accurate sender identification and contact details. CAN-SPAM and CASL require a valid postal address, so `{address}` must be filled before any real send. The `Health Check` fails and blocks sending until the address and the opt-out line are present (override requires explicitly setting `ALLOW_SEND_WITHOUT_ADDRESS=true`).
- One working opt-out. Suppress unsubscribes the same day.
- Canada (CASL) is the strictest. Only send to business addresses that are publicly published with no "no unsolicited email" notice and where my offer is relevant to the recipient's role; keep the `Source URL`. `CANADA_REQUIRE_SOURCE_URL` setting (default true): Canadian leads without a Source URL are held, not sent. This is not legal advice.

## 10. Follow-up templates and personalization

Templates live in the `Templates` tab (seed copies in `templates/`). I will supply my own text for follow-ups 1–4; until then, ship these placeholders. Each template section has 3–5 **variants**; the variant is chosen deterministically from the Lead ID so two leads get different wording, and the same lead never gets the same variant twice.

- **Follow-up 1 (touch 2, +5 business days):** short reminder tied to the first email. Mention they were probably busy. Remind of the sample at no cost. Frictionless CTA: "Reply 'yes' and I'll start on it." 
- **Follow-up 2 (touch 3, +10):** same thread. Offer options: "If you're busy, just reply with 1, 2 or 3: 1 = send the sample, 2 = ask me again next month, 3 = not for you." The scanner reads these replies by simple rules (no AI): `1` → hot Response, `2` → snooze 30 days, `3` → Not Interested.
- **Follow-up 3 (touch 4, +15):** a different angle (a fact-based idea for their niche or a seasonal line from the calendar), still short, still the sample line, one easy question.
- **Follow-up 4 (touch 5, +20):** last follow-up. "This is my last follow-up. To save both of our time, if it ever becomes a priority, you can reach out; otherwise I won't follow up again." Keep the sample line. No guilt, no fake urgency.

Personalization slots filled in code from LEAD DATA: `{first_name}`, `{channel_or_company}`, `{niche_phrase}` (from a niche table), `{city}`, `{angle_line}`, `{season_line}`, `{sample_phrase}`. Follow-ups are about 70% of touch 1's length (40–70 words) and all use the same validator.

Setting `FOLLOWUP_AI` = `off` (default; code-only variation, zero tokens), `light` (one tiny AI call that rewrites a single "personal line" slot, max 40 output tokens) or `full`. Include the token/cost effect in the Daily Report.

## 11. AI layer: API-agnostic, token-efficient

- **Providers are defined by config (`config/providers.yml`), not by model.** Per provider: `name`, `protocol` (`openai` compatible by default; also `gemini` native and `anthropic`), `base_url`, `api_key_env` (the GitHub secret name), optional `model` (blank = auto-discover), `priority`, `weight`, `daily_request_budget`, `daily_token_budget`, `rpm_limit`, `price_in_per_million`, `price_out_per_million`, `offpeak_price_in`/`offpeak_price_out` and the off-peak rule, and `enabled`. I will give you only an API key and (if needed) a base URL: the bot must work from that.
- **Model auto-discovery at start-up:** call the provider's models endpoint (cheap). Filter out embeddings, audio, tts, vision-only, moderation and "thinking/reasoner" models unless the model is pinned. Rank by a configurable preference list (small/fast chat models first). If discovery fails, try the pinned model, else skip that provider. Never hardcode a model name anywhere else in the code.
- **Distribute, don't just fail over:** spread requests across providers by weight and remaining budget so one free tier is not exhausted. Reading a 429 correctly is critical:
  - Per-minute or token-per-minute limit: wait using `Retry-After` / `retryDelay`, then retry the **same** provider. Do not disable it.
  - Daily quota ("per day", "limit: 0" for the day): disable that provider/model until the next UTC day.
  - 401/403: key problem. 402: no credit. 404: model problem. 5xx/network: back off and retry up to 4 times.
  - **Log the real HTTP status and a short message for every rejected key (no secrets, no prompts).**
- **Token efficiency:**
  - Stable prefix first (compact rules), variable lead data last, to hit provider prompt caching.
  - Send a compact lead JSON with only the fields that matter (no sensitive columns). Rules sent to the AI target about 400–500 tokens.
  - `max_tokens` just above the expected output (about 220 for touch 1), low temperature, thinking mode OFF.
  - Local validation first; one cheap repair prompt only for the failing text; template fallback.
  - Reply classification: rules first (bounce/auto-reply/unsub/1-2-3 handled without AI); AI only for the ambiguous human replies, batching several in one call.
  - Skip the AI for `LOW_DATA` leads when `LOW_DATA_USE_TEMPLATE` is on.
  - Daily token budget in Settings (`AI_DAILY_TOKEN_BUDGET`); at 80% alert me and switch to templates.
  - Record tokens in/out, provider, and estimated cost per day (USD, plus PKR via a Settings value `USD_TO_PKR`, default 276) in the Daily Report.
- If every provider is down or out of quota: use the deterministic templates for new emails, keep sending follow-ups, alert me, and finish the run with a warning (not a failure exit code). Use a failure exit code only for real breakage.

## 12. Reply scanning, labels, human takeover

**Run for every active account every 30 minutes.** Only touch threads/messages that belong to the bot's Send Log, plus bounce/auto-reply notices that refer to them. Never modify unrelated mail (for example my existing "Internal Emails" label or newsletters).

**Classification, in order:**
1. **Bounce / invalid:** from `mailer-daemon` / `postmaster` / `Mail Delivery Subsystem`, DSN status 5.x.x or 4.2.2 (mailbox full), "address not found", "no such user", "mailbox unavailable", "receptionist/mailbox full", "message blocked". → role `INVALID`. Suppress the address, stop the sequence, count a bounce for the account (5.7.x blocks are also logged as deliverability warnings).
2. **Auto reply:** headers `Auto-Submitted` (not `no`), `X-Autoreply`, `Precedence: auto_reply|bulk|junk`, or subjects/bodies such as "out of office", "automatic reply", "on leave", "vacation", "no longer with the company", "left the company". → role `AUTO_REPLY`. **Stop the sequence for that address** and never reply to it (my instruction). Setting `RESUME_AFTER_OOO` default false.
3. **Unsubscribe:** "Unsub", "unsubscribe", "stop", "remove me", "do not contact" (and the `unsubscribe` mailto message). → role `NOT_INTERESTED`, add to Suppression the same day.
4. **1 / 2 / 3 replies** to follow-up 2 (rules).
5. **Human reply:** classify with AI into Response / Not Interested / Wrong Person / Question. → roles `RESPONSE` or `NOT_INTERESTED`. Stop the sequence. Send me the reply details in the phone alert.

**The bot never replies to anyone.** It only sends touch 1 and the scheduled follow-ups.

**Human takeover (my manual conversations):**
- If a thread contains any message **from that account** whose Gmail message ID is **not** in the Send Log (i.e. I replied myself, from the web or phone), mark the lead `Manual`, cancel all remaining touches, and do not touch the thread again.
- If the thread carries my `Conversation` label (role `CONVERSATION`), treat it the same.
- Emails I send to people who are not in the Outreach sheet are ignored completely.
- To have a conversation: just reply in Gmail in the same thread from the same account. Optionally add the Conversation label. Nothing else is needed.

**Labels: moved out of the Inbox, not just tagged.**
For `AUTO_REPLY`, `INVALID`, `NOT_INTERESTED` and `RESPONSE`: add the label and **remove `INBOX`** (archive). Mark `RESPONSE` as unread and starred (setting `RESPONSE_KEEP_IN_INBOX`, default false per my request, but the phone alert is what makes sure I never miss a response). Settings let me change the behaviour per role.

**Fuzzy label resolution, per account, cached in `Label Map`:**
- Roles: `RESPONSE`, `NOT_INTERESTED`, `AUTO_REPLY`, `INVALID`, `CONVERSATION`.
- List the account's labels. Normalize names (lowercase, strip punctuation/emoji/plural endings, collapse spaces) and match in this order: exact → synonym list → fuzzy (`difflib` ratio ≥ 0.75, plus token overlap). Examples: RESPONSE ← response, responses, reply, replies, responded, interested, positive, hot leads. NOT_INTERESTED ← not interested, no thanks, declined, rejected, unsubscribe(d), unsub. AUTO_REPLY ← auto reply, autoreply, auto-reply, automatic, out of office, ooo, vacation, away. INVALID ← invalid, invalid emails, bounce(d), bounces, undeliverable, not found, no such user, mailbox, delivery failed, mailbox full. CONVERSATION ← conversation(s), talking, chat, in progress, active.
- Ignore labels that match nothing (e.g. "Internal Emails", "MyCRM", "Purchases").
- If two roles want the same label or confidence is low, pick the best score, write an Alert describing the choice, and continue.
- If a role has no match at all, **create** the label with a clear name ("Response", "Not Interested", "Auto Reply", "Invalid Emails", "Conversation"), record it, and continue. Never crash because a label is missing or renamed. Re-resolve every run, so renaming a label later works automatically. Never delete or rename my labels.

## 13. Phone notifications (free)

Notifier plugin interface with multiple channels, each optional: **Telegram** (default), **ntfy**, **Discord webhook**, **Slack incoming webhook**, **email digest** (via Gmail API to my personal address, from a dedicated non-outreach account). The runner is in the cloud, so Telegram delivery doesn't depend on Pakistan's network; only my phone must be able to open Telegram (use a VPN or switch channel if it is blocked). Support enabling several at once; if one fails, try the next and log the failure.

Messages are plain, scannable, short lines with blank lines between sections, never one block of text; split anything longer than ~3,500 characters into several messages.

**Instant alerts** (every reply scan):
```
New response
Account: Chris Ewart (vfx.chrisewart@gmail.com)
Lead: Maria Lopez, Lopez Fitness (Australia, Gym)
Touch: 2

They wrote:
"Sounds good, can you send an example?"

Summary: wants a sample.
```
Also instant alerts for: account paused or reduced, token expired/revoked, high bounce rate, AI out of quota, run failure, label created or ambiguous, cap clamped.

**Daily report** (default 8:00 PM Pakistan time):
```
Daily Report - 03 Nov 2026

Sent today: 612
  New: 180 | Follow-ups: 432
Replies: 11 (3 Response, 5 Not Interested, 3 Auto)
Bounces: 6 (0.98%)
Unsubscribes: 2

By country: USA 340 | Canada 120 | Australia 152
Top niche: Restaurants

Accounts: 13 active, 1 reduced
  Brad Mills: bounces 4% -> cap halved

Responses today:
- Chris Ewart: Maria Lopez - "Can you send an example?"

Queue: 3,400 planned over next 20 days
AI: 220k tokens, about $0.07 (PKR 20)
```

Setup instructions (in START_HERE.md):
- **Telegram:** open Telegram, search for `@BotFather`, send `/newbot`, choose a name and a username ending in `bot`, copy the token. Open your new bot and send it "hi". Visit `https://api.telegram.org/bot<TOKEN>/getUpdates` and copy `chat.id` (or use `@userinfobot`). Add GitHub secrets `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` (repo → Settings → Secrets and variables → Actions). Provide a test command.
- **ntfy:** install the ntfy app, subscribe to a long random topic, add `NTFY_TOPIC` as a secret.
- **Discord/Slack:** create a webhook, add `DISCORD_WEBHOOK_URL` / `SLACK_WEBHOOK_URL`.

## 14. Settings (all in the `Settings` tab with description and default, loaded with validation)

`DRY_RUN`, `PAUSE_ALL` (kill switch), `GLOBAL_DAILY_MAX`, `GMAIL_MAX_PER_DAY` (read-only display of the ceiling), `DOMAIN_MAX_PER_DAY` (700), ramp values, `ALLOCATION_MODE`, `NEW_SHARE_MIN/TARGET/MAX`, `SURVIVAL_RATE`, `MAX_SLIP_BUSINESS_DAYS`, `WEEKEND_FOLLOWUPS`, `WEEKEND_CAP_PERCENT`, `FOLLOWUP_GAP_BUSINESS_DAYS` (5), `TOUCHES_TOTAL` (5), `DOMAIN_COOLDOWN_DAYS`, `ALLOW_ROLE_EMAILS`, `ALLOW_WORD_FREE`, `SIGNATURE_HTML`, `LIST_UNSUBSCRIBE_MAILTO`, `FOLLOWUP_AI`, `GENERATION_MODE`, `DRAFT_MAX_AGE_DAYS`, `AI_DAILY_TOKEN_BUDGET`, `USD_TO_PKR`, `RESPONSE_KEEP_IN_INBOX`, `RESUME_AFTER_OOO`, `ORPHAN_FOLLOWUPS`, `CANADA_REQUIRE_SOURCE_URL`, `ALLOW_SEND_WITHOUT_ADDRESS`, `REPORT_TIME_UTC`, `NOTIFY_CHANNELS`, `MAX_PER_HOUR_GMAIL`, `MAX_PER_HOUR_DOMAIN`, `MIN_GAP_SECONDS`, `MAX_GAP_SECONDS`, `TEST_MODE` (send only to a list of my own addresses).

A bad or missing setting value must fall back to its default and write an Alert, never crash.

## 15. Health Check (run at the start of every workflow, and on demand)

Verify: Sheets access (outreach sheet read/write, source sheets read), tabs and headers present, every active account's token valid and Gmail reachable, labels resolved, AI provider keys valid (cheap models-list call, no prompts), signature address and opt-out present, settings valid, holiday library loaded, no lock held. Write results to Run Log and Alerts. Block sending (not importing) if a critical check fails.

## 16. Fail-safes (must be implemented and tested)

Double-send protection (section 2); Sheets quota/429 backoff; Gmail 429/403/`rateLimitExceeded` backoff; per-account circuit breaker; expired/revoked token handling; daily-quota detection; thread-mismatch protection (if the thread no longer exists, don't send the follow-up as a new thread unless `ORPHAN_FOLLOWUPS=restart_new_thread`); lead changes in the source sheet after import ignored (the Leads tab is the truth); header/column changes in my own sheets tolerated; dedupe across all sources and across runs; replies from a different address than the one emailed (match by thread); forwarded replies; catch-all domains; same domain contacted twice; DST changes; leap/holiday edge cases; run late/duplicate; partial writes; Unknown country holds; leads with `tz uncertain`; clock skew; an account added or removed mid-day; caps changed mid-day (apply immediately to remaining sends); cap blank/invalid (clamp, never crash); a domain account added with the wrong cap (ceiling and ramp protect it); label renamed or missing; AI providers all down; Telegram down (fallback channels).

## 17. Public-repo hygiene and secrets

- **GitHub Actions logs are public.** Never print email addresses, names, email bodies, reply text, sheet IDs or tokens. Log counts, lead IDs and HTTP status codes only. Use `::add-mask::` for any secret-derived value. Wrap logging in a helper that redacts addresses by pattern.
- **Do not commit** the accounts list, tokens, API keys, sheet IDs or my address/phone/website. They live in GitHub Secrets (`GOOGLE_SA`, `SHEET_ID`, `GMAIL_TOKENS`, AI keys, notifier tokens) or in the private sheet (Accounts, Signature tabs). Add `.gitignore` for local files.
- Don't run workflows with secrets on `pull_request` from forks. Use `workflow_dispatch` and `schedule` only.
- Secrets inventory in START_HERE.md with where to get each one.

## 18. Documentation to deliver

**`START_HERE.md`** (first file I open): what the system does; the daily flow; step-by-step setup (Google Cloud project, OAuth consent screen set to "In production", service account for Sheets and how to share the sheets with it, authorizing each Gmail account with the helper, creating labels, GitHub secrets list, running Health Check, dry run, first real send with two accounts and 10/day, then scaling); how to add/remove an account; how to raise/lower a cap; how to edit templates, signature, font, colour, rules; how to read each tab; how to pause everything; how to switch AI provider/key; weekend generation explained; the allocation modes and their honest consequences; compliance notes (CAN-SPAM, CASL, Australian Spam Act: not legal advice); troubleshooting by error message.

**`OPTIONAL_TOOLS.md`**: free-but-harder-to-get options: extra AI providers (Groq, Cerebras, NVIDIA NIM, Google AI Studio, Mistral free tier, Cloudflare Workers AI, GitHub Models, Z.ai GLM free models, DeepSeek and others with how to get a key and what to put in `providers.yml`), free email verifiers (QuickEmailVerification 100/day, Verifalia 25/day, ZeroBounce 100/month), notification channels, a future domain/mailbox setup with SPF/DKIM/DMARC and Google Postmaster Tools, and how to use a non-Google mailbox via the SMTP/IMAP backend.

## 19. Repo layout

```
.github/workflows/  import.yml plan.yml send.yml replies.yml report.yml keepalive.yml healthcheck.yml
src/outreach/       config.py sheets.py importer.py accounts.py capacity.py scheduler.py planner.py
                    compose.py validator.py signature.py templates.py ai/ (providers, discovery, router)
                    gmail.py sender.py replies.py labels.py suppression.py notify/ report.py healthcheck.py util/
config/             providers.yml country_rules.yml niche_angles.yml synonyms.yml
rules/              email_rules.md
templates/          followup_1..4 seed files, signature seed
tools/              authorize_account.py setup_sheet.py seed_accounts.py (reads a git-ignored input file)
tests/
START_HERE.md  OPTIONAL_TOOLS.md  requirements.txt  .gitignore
```

## 20. Definition of done

- A dry run imports sample leads from two differently-structured source sheets without my configuring headers, and shows the detected mapping in `Sources`.
- The planner schedules mixed US/CA/AU leads into the right local windows, skipping weekends (first emails) and holidays.
- With 2 accounts at 10/day, real sends thread correctly (touch 1 and follow-up in one Gmail thread), the Send Log and Outreach tab update, and no email is ever sent twice.
- Setting a Gmail account's cap to 500, or leaving a new domain account's cap too high, never sends beyond 70 (gmail) / 700 (domain) / the ramp limit, and writes an Alert.
- Replies, bounces and auto-replies are classified, labelled (fuzzy match or created), moved out of the inbox, suppressed, and shown in `Replies`; my own manual reply stops the sequence.
- The phone alert and the daily report arrive in the formats above on at least one channel.
- Switching the AI provider requires only a new API key and `providers.yml` entry, never a model name.
- All unit tests pass.

## 21. Open items (use placeholders and flag them in START_HERE.md)

- My postal address / website / phone for the signature (required for compliance before any real send).
- My own follow-up templates 1–4 (placeholders provided above).
- Final lead-sheet headers (auto-detection handles it; override in `Sources` if needed).
- Final decision on `ALLOCATION_MODE` (default BALANCED).
- Whether "Aura Media" is part of the signature (not used in this brief; default is the signature in section 9).
