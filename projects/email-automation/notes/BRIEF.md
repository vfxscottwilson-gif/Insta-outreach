# Email Automation App: Goal-first brief and critical analysis

Status: **DRAFT, waiting for approval** (2026-11-03). Nothing built yet.
Inputs: the user's build prompt (sections 0-21, pasted in chat), extra requirements in the same message, one Behance reference shot ("Marketing Automation App", dark UI, purple accent).

## 1. Goal

| | |
|---|---|
| **Goal** | Book more video-editing clients by running cold outreach from 14+ Gmail accounts on autopilot, with zero duplicate emails, inside a premium app you control from Windows and your phone. |
| **Done when** | 1. Dry run imports 2 differently-structured lead sheets with no header setup. 2. Pilot: 2 accounts x 10/day to your own test addresses, touch 1 + follow-up in one Gmail thread, 0 duplicates (proved by DB constraint + test). 3. A cap of 500 typed on a Gmail account never sends more than 70 (domain: 650). 4. Replies, bounces and auto-replies are classified, labelled, archived and stop the sequence; your manual reply stops it too. 5. Dashboard shows daily / weekly / monthly per account, health score, bounces, replies, capacity forecast, in dark and light mode with the blue/black theme. 6. Windows app installs (.exe); phone app installs on iPhone and Android home screen; a push alert and the daily report arrive at the time and time zone you set. 7. Switching AI provider = new key only. 8. All tests pass. |

## 2. Options researched (architecture)

| # | Option | Good | Bad | Verdict |
|---|---|---|---|---|
| A | **Prompt as written**: Python + Google Sheets as database + GitHub Actions cron + Telegram | Free, already specified | Sheets has no transactions, so "never send twice" is best-effort only; GitHub cron runs late or gets skipped; GitHub terms risk (see red flag 5); no real app | Keep the engine logic, replace the database and host |
| B | **Hybrid (recommended)**: Python engine from the prompt + Postgres (Supabase) as the single source of truth + always-on small worker + one React web app that installs as a PWA (iPhone/Android/Mac/Windows) and is wrapped by Tauri as a Windows .exe | Real transactions and unique keys make duplicates impossible at DB level; runs 24/7 without your PC; one UI codebase for every platform; ~$7/month total (9e) | Needs a ~€6/month server (or a free tier with limits, 9a) | **Pick** |
| C | **Buy SaaS** (Instantly, Smartlead, Saleshandy...) | Ready in a day: mailbox rotation, warm-up, unified inbox, analytics | Monthly fee; your custom rules (validator, AI layer, weekend lane, 1-2-3 replies, PKT report) only partly possible; data lives with them | Use as UI/feature reference only |
| D | **Fork open source** (e.g. ethanplusai/harvey, already scanned: CAUTION) | Some code reuse | Built for one mailbox and its own workflow; would be rewritten anyway | Borrow ideas, not the app |
| E | **n8n workflows** (skills installed) | Visual | 14 accounts x caps x threading x claim tokens becomes unmaintainable; no custom dashboard | No |

**Why B:** it is the only option that turns "not one email ever duplicated" into a database guarantee instead of a hope, keeps everything you asked for, and stays near-free.

## 3. Target architecture (option B)

```
Lead bot (yours, out of scope) ──> Google Sheets (read-only sources)
                                          │ import every 2-3 h
                                          ▼
 ┌────────────── Worker (Python 3.12, always on, small VPS) ──────────────┐
 │ importer · dedupe · planner · AI composer+validator · sender (every   │
 │ 1-2 min tick) · reply scanner · labels · health rules · reports ·     │
 │ web-push + Telegram notifier · nightly backup                         │
 └──────────────┬───────────────────────────────────┬─────────────────────┘
                │ Gmail API (OAuth, gmail.modify)    │ SQL (transactions)
                ▼                                    ▼
        14+ Gmail accounts               Supabase Postgres (truth) + Auth + Realtime
                                                     ▲
                                                     │ live data (row-level security)
                     React app (Vite + TS + Tailwind + shadcn + Motion; base: satnaing/shadcn-admin)
                     ├─ PWA: iPhone / Android / Mac / Windows browser, web push
                     └─ Tauri wrapper: Windows .exe (Mac .dmg later)
```

- The worker has **no public port**: it only calls out (Gmail, Supabase, AI, push). Smaller attack surface.
- The app never sees Gmail tokens. Tokens are encrypted in Supabase Vault; only the worker can read them.
- Google Sheets stays as the lead input, plus an optional "export to sheet" mirror for you.
- Every setting you change in the app (cap, pause, add/remove account, templates) is read by the worker on its next tick, so changes apply within 1-2 minutes.

## 4. Red flags found (and the fix for each)

| # | Red flag | Why it matters | Fix |
|---|---|---|---|
| 1 | **"Log in each account with Gmail + password"** | Google: "Gmail no longer supports third-party apps or devices which require you to share your Google username and password" (support.google.com/mail/answer/7126229). App passwords need 2-Step Verification and work for IMAP/SMTP only, not the Gmail API. Storing 14 passwords is also a big security risk. | Each account is connected once with **"Sign in with Google" (OAuth)** in the browser. The app stores a refresh token (encrypted), never a password. OAuth consent screen "In production" (Testing mode tokens expire in 7 days; unverified apps are capped at 100 users, fine for 14). Google keeps only 100 refresh tokens per account per app, so don't reconnect in a loop. Your app login (email + password) is separate. |
| 2 | **Sender names may not be real people** (Chris Ewart, Scott Wilson... "on behalf of Haroon VFX") | CAN-SPAM bans misleading "From" / header info; CASL and the Australian Spam Act require accurate sender identification. Fake personas are also the fastest way to lose accounts under Google's policies. Your own prompt (section 9) says the name must be the real operator. | **Resolved 2026-11-03:** the user confirmed all 14 names are real people who operate those accounts. Keep display name = From = signature name. |
| 3 | **14 consumer Gmail accounts for cold email** | Gmail policy: "Don't use Gmail to distribute spam or unsolicited commercial mail"; circumvention rules ban using multiple accounts to repeat prohibited behaviour (support.google.com/mail/answer/16734397, updated 20 Oct 2026). All 14 accounts share one OAuth app and one server IP, so a flag on one can spread. Consumer Gmail gives no Postmaster/spam-rate data. Near 5,000/day to Gmail recipients, Google's bulk-sender rules (one-click unsubscribe, spam rate under 0.3%) may apply. | Keep the ramp + caps + jitter + health auto-pause; spread send times; monitor reply/bounce health daily. Long term (OPTIONAL_TOOLS.md): your own domains with SPF/DKIM/DMARC and Postmaster Tools. |
| 4 | **Google Sheets as the database** | No transactions or locks; two runs (late + duplicate GitHub runs are normal) can both "claim" the same row; Sheets API quota (per-minute limits) breaks at 900-2,000 sends/day with 10-minute runs. This is the main duplicate-email risk. | Postgres: `UNIQUE(lead_id, touch_no)` on sends, `UNIQUE(canonical_email)` on leads, claim rows with `SELECT ... FOR UPDATE SKIP LOCKED`. A second send of the same touch is rejected by the database itself. |
| 5 | **GitHub Actions as the always-on sender** | GitHub docs: schedules "can be delayed during periods of high loads" and queued jobs "may be dropped". Actions terms: hosted runners not for activity "unrelated to the production, testing, deployment, or publication of the software project"; the Acceptable Use Policy bars "sending unsolicited emails". Public-repo schedules auto-disable after 60 days without activity; a private repo at a 10-minute cron (4,320 runs/month) exceeds the free ~2,000 minutes. | Run the worker on a small always-on server. Use GitHub only for code, tests (CI) and deploys. Repo can then be **private**. |
| 6 | **Crash between "Gmail sent" and "DB saved"** | Gmail API has no idempotency key; a blind retry = duplicate. | Row is committed as `sending` (with our own pre-generated Message-ID) **before** the API call. On restart, any `sending` row is reconciled against the account's Sent folder (by Message-ID, fallback: recipient + subject in last 48 h) and is never blindly retried. Unknown result = hold + alert, not resend. |
| 7 | **Same person, different spelling** | `J.Smith@gmail.com`, `jsmith+yt@gmail.com` and `jsmith@googlemail.com` are one inbox; plain lowercase dedupe misses it. | Store a `canonical_email` (lowercase, Gmail dots and +tags removed, googlemail -> gmail) and dedupe on it, across all sources and all accounts. |
| 8 | **Caps in the prompt differ from your message** | Prompt: domain ceiling 700. You: domain never above 650. | Code constants: `GMAIL_MAX_PER_DAY = 70`, `DOMAIN_MAX_PER_DAY = 650`. Daily target varies inside a band: Gmail 50-60 normal, rare days up to 70; domain 500-600 normal, up to 650. Never above the ceiling, whatever is typed in the app. |
| 9 | **Domain mailbox at 500-650 cold emails/day** | Far above common cold-email practice for one inbox (industry guides suggest tens per inbox, not hundreds). Burns domain reputation fast. | Ceiling stays 650 as you asked, but a new domain account starts at 30/day with ramp, and the app warns when you set a cap above a "safe" level. |
| 10 | **"free of cost"** | Contains the word "free", which the prompt bans (spam-filter trigger). | Allowed phrases: "at no cost", "no cost to you", "on me", "complimentary", "nothing to pay", "costs you nothing". Validator rejects any "free". **Question 9** if you want "free of cost" allowed. |
| 11 | **Claude Code as the running AI engine** | A Claude Code subscription is for interactive coding, not the 24/7 engine of a production app. | Engine uses an API key (Claude Haiku first, then Gemini / DeepSeek / Groq / Grok by config). Templates-only mode costs $0 if all providers fail. Claude Code stays the build tool. |
| 12 | **Daily report at 8 PM PKT (15:00 UTC) is mid-US-window** | US East sends 13:30-17:30 UTC, so "today" is cut in half. | Report covers the last full 24 h and shows per-region totals by the lead's local date. |
| 13 | **Australian replies arrive 2-6 AM PKT** | Phone buzzes all night. | Quiet hours in notification settings; hot responses can bypass quiet hours (your choice). Morning digest. |
| 14 | **iPhone notifications** | PWAs can't schedule local reminders on iOS. Web push works on iOS/iPadOS 16.4+ only after "Add to Home Screen", and permission must be asked from a tap (webkit.org, caniuse). A native iOS app needs the Apple Developer Program ($99/year); the free route expires every 7 days. | Reminders and daily reports are pushed **from the server** at your chosen time/time zone. Telegram as a second channel that always works. Native iOS app only if you want to pay Apple yearly. **Question 6.** |
| 15 | **"Reply 2 = ask me again next month"** has no rule for what happens next | Lead would sit forever. | After 30 days: send the remaining touches in the same thread (default), configurable. |
| 16 | **Lead supply** | At ~770 sends/day and 5 touches, only ~1 in 4 sends can be a new lead: about **185 new leads per business day, ~4,000/month**. | Dashboard shows "days of leads left"; alert when under 5 days. |
| 17 | **Vercel free plan is non-commercial** | Hosting a business app there breaks its terms (already verified for LevelUp CRM). | Host the web app on Cloudflare Pages (free) or on the same server. |
| 18 | **Supabase free pauses after 1 week idle; single-session is a paid feature** (verified for LevelUp CRM) | | Worker activity keeps it awake; single session per account done with our own `active_sessions` table (same design as LevelUp CRM). |
| 19 | **gmail.modify can read all mail** | Tokens are the keys to 14 inboxes. | Encrypted in Vault, worker-only access, never logged, revoke button per account. |
| 20 | **Unsigned desktop apps** | Windows shows a SmartScreen warning; Mac needs Apple notarization. | Fine for personal use ("More info -> Run anyway"). Signing later if needed. |

## 5. Things you didn't ask for but need

- **Audit log**: who changed which cap/setting and when, with one-click revert. This is the real "if something looks wrong, I can fix it" fail-safe.
- **Kill switch** in the app header (pause everything), per-account pause, and "drain" mode (finish follow-ups, no new leads).
- **Health score per account** (0-100): bounce %, reply %, error rate, auth status, cap usage; shown as a ring with trend.
- **Daily / weekly / monthly tracking per account**: sends, replies, positive replies, bounces, unsubscribes, health trend.
- **Unhandled-response reminder**: push again if a positive reply is not marked handled within X hours.
- **Lead timeline**: every touch, reply and status change for one lead on one screen.
- **Template editor with live validator**: word count, banned words, sample phrase check while you type.
- **Nightly database backup** (Supabase free has limited backups; not verified).
- **Test mode**: real sends only to your own addresses, for the pilot.
- **Data deletion on request**: delete a lead's data but keep a hashed suppression entry so they are never emailed again.

## 6. The app (screens)

| Screen | What's on it |
|---|---|
| **Overview** | KPI tiles (sent today vs capacity, new vs follow-ups, replies, positive replies, reply %, bounce %, unsubscribes, AI cost), live "next sends" ticker, capacity forecast (20 business days), funnel (imported -> touch 1 -> ... -> touch 5 -> replied -> positive), reply rate by country / niche / weekday / local hour (heatmap), lead supply days left |
| **Accounts** | Table: health ring, today vs cap bar, rolling 24 h, 7 d / 30 d sends, bounce %, reply %, status pill, auth OK; inline cap edit (clamped to ceiling), pause/resume, connect/reconnect, remove. Detail page: weekly and monthly charts |
| **Leads** | Search + filters, status, timeline, manual hold/suppress |
| **Queue** | Calendar of planned sends by region window; slipped follow-ups |
| **Replies** | All classified replies, AI one-line summary, "handled" checkbox, open in Gmail |
| **Templates & signature** | Touch 1 rules, follow-ups 1-4 with variants, signature editor with preview |
| **Reports** | Daily / weekly / monthly, CSV/PDF export |
| **Alerts** | All alerts, acknowledge |
| **Settings** | Every tunable with validation and default, dry run, test mode, notification channels, quiet hours, report time + time zone, reminders |
| **Admin** | Users/employees and roles, sessions, audit log (app standard: email + password, single session, reset by email code) |

**Look and feel:** dark navy/black base with light-blue accent (proposed: background `#07090D`, surface `#0E131B`, accent `#4DB8FF`), light theme toggle, glass-free flat panels, Inter/Geist type, count-up numbers, animated chart draws, spring hover/press feedback, smooth page and panel transitions, reduced-motion respected. The Behance shot is a reference for structure and feel, not copied.

## 7. Repos and skills

Repos: see section 9b.

**Skills already installed and used:**

| Area | Skills |
|---|---|
| Process | goal-first, superpowers (brainstorming, writing-plans, subagent-driven-development, test-driven-development, verification-before-completion, systematic-debugging), ponytail, Council (stack decision), RedTeam (attack the no-duplicate logic) |
| UI + motion | frontend-design, ui-ux-pro-max, emil-design-eng, animate, apple-design, animation-performance, dataviz, shadcn, react-best-practices, web-design-guidelines, mobile-native |
| Backend | supabase, postgres-best-practices, claude-api |
| Testing | webapp-testing, playwright-cli, chrome-devtools-mcp, code-review, security-review |

**Skills to scan and install (SkillSpector gate first):**

| Skill | Installs | Why |
|---|---|---|
| nodnarbnitram/claude-code-extensions@tauri-v2 | 8.2K | Windows .exe / Mac wrapper |
| alinaqi/maggy@pwa-development | 4.2K | Installable PWA, service worker, web push |
| coreyhaines31/marketingskills@cold-email | 132.8K | Cold-email copy rules for templates |
| mbfinotti/sales-skills@cold-email-deliverability | 32K | Deliverability checks |

**MCP servers to authorize (you, via `/mcp` in a terminal):** context7 (library docs), supabase (DB setup).

## 8. Workstreams (one session each, after approval)

| # | Workstream | Model | Depends on | Done when |
|---|---|---|---|---|
| 0 | Decisions + DB schema contract + design system mock | Opus | your answers | Schema + 1 static dashboard mock approved |
| 1 | Engine core: import, dedupe, accounts, caps, ramp, OAuth, sender, send log | Opus design / Sonnet code | 0 | Pilot 2 x 10/day to test addresses, 0 duplicates |
| 2 | AI layer + composer + validator + templates + signature | Sonnet | 0 | Validator tests pass; provider switch by key only |
| 3 | Scheduler + planner + weekend lane + capacity forecast | Sonnet | 1 | Mixed US/CA/AU leads land in correct windows (tests) |
| 4 | Replies + labels + human takeover | Sonnet | 1 | Classification tests + live label/archive on test account |
| 5 | App UI (all screens, motion, PWA, Tauri .exe) | Sonnet + design skills | 0 | Installs on Windows + iPhone; Lighthouse PWA pass |
| 6 | Notifications + reports (web push, Telegram, daily report, reminders) | Sonnet | 1, 5 | Alerts arrive on phone at set time |
| 7 | Hardening: RedTeam on duplicates/caps, security review, START_HERE.md, OPTIONAL_TOOLS.md | Opus | all | All tests green, red-team findings closed |

## 9. Research results (checked 2026-11-03 by 3 Sonnet research agents; official page first)

### 9a. Where the worker runs

| Host | Cost | Verdict |
|---|---|---|
| Hetzner CX23 (2 vCPU / 4 GB) | €5.99/mo official page; stock shown as "currently unavailable" (⚠ volatile) | **Pick** (or any ~$5 VPS): reliable, runs the prompt's Python as-is, also does nightly DB backups |
| Supabase pg_cron + Edge Functions | $0 (500k invocations; 2 s CPU, 150 s wall; pg_cron on Free not explicitly documented ⚠) | Free fallback, but the engine would be rewritten in TypeScript |
| Oracle Always Free (2 Arm cores / 12 GB) | $0 | Idle VMs can be reclaimed (7-day CPU under 20%); our worker is mostly idle → risky |
| Cloudflare Workers Free | $0 | 10 ms CPU and 50 subrequests per run: too tight for 14 accounts |
| GitHub Actions | $0 public | Red flag 5 |

Design rule either way: the engine is a stateless `tick()` that sends only rows whose pre-computed `send_at` (with jitter) has passed. No long sleeps, so it can move between hosts.

### 9b. Repos to reuse (all MIT/Apache/CC0 unless noted; stars and dates from GitHub API)

| Repo | Use |
|---|---|
| andersmyrmel/cold-cli (MIT, Go) | Port the logic: idempotent tick engine, pre-computed `send_at`, reply matching by In-Reply-To, 3 bounce strategies, auto-reply exclusion |
| suneet07/trickle (MIT, TS) | Port the logic: warm-up ramp, 0-100 inbox health score, circuit breaker. New (1 star): read before trusting |
| jmougeot/sequence-mail (MIT) | Reference: Gmail OAuth multi-account, same-thread follow-ups |
| AbdelftahZowail/Quickly (MIT) | Reference: AI reply classifier over many LLM providers (telemetry on by default: don't run it) |
| googleapis/google-api-python-client (Apache) + Python stdlib `email` | Gmail send with `threadId`, In-Reply-To/References, DSN bounce parsing |
| mailgun/talon (Apache) | Strip quoted text/signatures before AI reply classification |
| disposable-email-domains (CC0), mixmaxhq/role-based-email-addresses (MIT), JoshData/python-email-validator (Unlicense) | Lead hygiene |
| satnaing/shadcn-admin (MIT, Vite, 16.4k) | App base: Vite SPA fits Tauri + PWA + Cloudflare Pages better than the Next.js kits |
| magicuidesign/magicui, motiondivision/motion, barvian/number-flow (all MIT) | Motion: number tickers, animated lists, transitions |

Rejected: EmailEngine (paid license), Aceternity UI (custom license), Mautic/listmonk/Dittofeed/Plunk (newsletter/opt-in tools, not cold 1:1 from Gmail), inbox-zero (AGPL, read only), Warmbly (Gmail auth method unclear, ~10 GB).
No library exists for auto-reply detection or first-name extraction: ~20 lines each, from the prompt's rules.

### 9c. Buy instead? (cheapest plans)

| Tool | Price/mo (monthly / annual) | Personal @gmail.com by OAuth? |
|---|---|---|
| Instantly Growth | $47 / $37.60 | **No** (app password only) |
| Smartlead Base | $39 / $32 | **No** (app password only) |
| Saleshandy Starter | $41 / $34 | ⚠ unconfirmed |
| lemlist Email | $69 / $55 ⚠ | Plausible ⚠; lemlist advises against @gmail for cold email |
| GMass / Mailmeteor | $29.95 / $5.99 per user | Yes, but 1 sender per user, no rotation |

None fits 14 personal Gmail accounts by OAuth with your rules. Building wins.

### 9d. AI engine cost (250 first emails/day x 22 days; follow-ups use templates = 0 tokens)

| Model | $ per 1M tokens in / out | Per month |
|---|---|---|
| Claude Haiku 5.5 (default) | $0.10 / $0.50 | ~$1.00 (~$1.30 with its newer tokenizer) |
| Gemini 2.5 Flash-Lite | $0.10 / $0.40, free tier exists | ~$0.87 or $0 |
| OpenAI gpt-5-nano | $0.05 / $0.40 | ~$0.68 |
| Groq gpt-oss-20b | $0.075 / $0.30, free tier | ~$0.65 |
| DeepSeek deepseek-flash | $0.15 / $0.60 off-peak | ~$1.30 |
| xAI grok-build-0.1 | $1.00 / $2.00 | ~$6.27 (avoid) |

### 9e. Running cost estimate

| Item | Monthly |
|---|---|
| Worker VPS | ~€6 |
| Supabase Free (500 MB) | $0 (Pro $25 later if needed) |
| Cloudflare Pages (app hosting) | $0 |
| AI | ~$1 |
| Telegram + web push | $0 |
| Apple developer (only for a native iOS app) | $0 (PWA) or $99/year |
| **Total** | **~$7/month** |

## 10. Questions (answer once, then the build runs)

1. **Sender names:** are Chris Ewart, Scott Wilson etc. real people who operate those accounts? If not: switch to a truthful name pattern (recommended) or keep (your legal risk).
2. **Worker host:** ~€6/month VPS (recommended) / Supabase free (engine rewritten in TypeScript) / GitHub Actions (red flag 5).
3. **Database:** new Supabase project (recommended) or share the LevelUp CRM project? Should positive replies later flow into LevelUp CRM as leads?
4. **"Search engine":** only the AI that writes emails, or also web search to research/enrich leads?
5. **iPhone:** PWA from the Home Screen (free, recommended) or a native App Store app ($99/year)?
6. **Users:** just you, or employees with roles (app standard admin portal)?
7. **Domain accounts:** any planned soon? (Ceiling 650, start 30/day with ramp.)
8. **"free of cost":** ban like "free" (recommended) or allow?
9. **Repo:** private (recommended, logs and code not public)?

**Still needed from you (can come later, build starts without them):** reference UI links/screens, your lead-bot repo or sheet links (read-only), postal address for the signature (law requires it before any real send), your follow-up templates 1-4 (placeholders until then), Telegram bot token (setup steps in START_HERE.md).
