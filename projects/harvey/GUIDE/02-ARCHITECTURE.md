# 02 Architecture

Harvey is big (about 30 Python modules in `app\harvey\`). This page is the map. The full technical reference is `app\CLAUDE.md` section "How Harvey Works"; features are in `app\README.md`. Everything below was checked against those files and the source.

## The big picture
Everything runs on your PC. Only two things are in the cloud: Claude (through the Claude CLI) and your email provider.

| Part | What it is | Where |
|---|---|---|
| Backend | Python package `harvey`; command `harvey` | `app\harvey\` |
| Heartbeat loop | `harvey run`: wakes every 15 min (`usage.heartbeat_interval_minutes`), does one job, sleeps | `app\harvey\main.py` |
| Dashboard | FastAPI JSON API plus plain HTML/CSS/JS, no build step, at http://127.0.0.1:5555, locked by a private token link | `app\harvey\dashboard.py`, `app\harvey\web\` |
| Database | One SQLite file | `app\data\harvey.db` |
| AI ("brain") | Runs `claude -p` (headless Claude CLI) as a subprocess with your subscription login. No API key. | `app\harvey\brain.py` |
| Email | Gmail API, Microsoft 365, SMTP+IMAP, or legacy Instantly | `app\harvey\integrations\` |
| Config | `app\harvey.yaml` (defaults), `app\harvey.local.yaml` (yours, wins when present), `app\.env` (keys) | `app\` |
| Prompts / skills | Markdown files injected into the AI prompts | `app\prompts\`, `app\skills\` |

## Data flow in text
1. **Train** (once, `harvey train <url>`): `trainer.py` crawls your site, asks Claude to extract product, targets, objections, writes `harvey.local.yaml` and `skills\product_knowledge.md`.
2. **Signals**: you confirm which facts Harvey may collect (`harvey signals --confirm free`). Only confirmed signals are collected (`signals.py`).
3. **Discover**: `harvey discover` finds businesses from a source (free OpenStreetMap by default; paid ones optional). It estimates cost first and stops at `--max-spend` (default 1.0) (`collectors\discover.py`).
4. **Enrich** (Scout agent, `agents\scout.py`): Python searches the web (DuckDuckGo, then Bing, Google, Serper), visits each company site, finds the owner, learns the company's email pattern, verifies ONE candidate with Reoon/ZeroBounce/Hunter. Each address is tagged verified, catch-all ("risky") or guess. Claude only scores found data.
5. **Write** (Writer, `agents\writer.py`): Claude drafts a 3-email sequence per prospect (email 1 under 75 words, email 2 under 75, email 3 under 40).
6. **Send** (Sender, `agents\sender.py`): emails are staged into the `outbox` table. With default `require_approval: true` they wait for your approval (dashboard Outbox, or `harvey outbox`). Approved items go out on later heartbeats with human-like pacing, subject to the daily cap, quiet hours, warmup ramp, the sending kill switch, and a no-AI pre-send gate (`gate.py`: banned phrases, length, links, do-not-contact list).
7. **Reply handling** (Handler, `agents\handler.py`): every cycle it reads the mailbox, drops duplicates, classifies intent, advances the conversation stage (initial_outreach, engaged, qualifying, presenting, negotiating, closing, closed_won/closed_lost) and queues answers through the same Outbox. A reply from anyone at a company stops the sequence to everyone there. Bounces mark the address invalid and trip a global stop past `channels.email.max_bounce_rate` (default 0.05).
8. **Idle**: the Analyst writes `data\analytics.json`.

## The heartbeat in one list
Each cycle (`main.py`, function `heartbeat`): check quiet hours, check the brain is usable (`claude` logged in), check Claude quota stays under `usage.max_daily_claude_percent` (default 80; else sleep 1 hour), then pick ONE job by fixed rules: send_campaign, else write_campaign, else prospect, else idle. Replies are read every cycle alongside. After consecutive failed cycles it backs off 60 s doubling up to 15 min. Only one loop may run at a time (a lock file in `data\`).

## Folders in `app\harvey\`
| Path | What it does |
|---|---|
| `cli.py` | All `harvey ...` commands |
| `main.py`, `pidfile.py` | Heartbeat loop, single-instance lock |
| `brain.py`, `claude_runtime.py`, `usage.py`, `integrations\quota.py` | Claude calls, usage and quota gauge |
| `codex.py` | Optional ChatGPT brain (refused on Windows) |
| `config.py` | Loads and validates the yaml files |
| `state.py` | SQLite layer; tables include companies, prospects, campaigns, conversations, outbox, observations, signal_codes, settings, usage_events |
| `agents\` | scout, writer, sender, handler, analyst |
| `collectors\` | discover, profile (site facts), people (owners), ats (job boards) |
| `integrations\` | gmail, microsoft, smtp_mail, instantly, email_finder, trulyinbox, precleared, linkedin, signature |
| `gate.py`, `send_window.py`, `deliverability.py` | pre-send checks, per-recipient send hours, SPF/DKIM/DMARC and warmup checks |
| `dashboard.py`, `dashboard_auth.py`, `web\` | Dashboard server, token auth, front end |
| `trainer.py`, `setup.py` | `harvey train`, `harvey setup` wizard |

## Dashboard tabs
Today, Signals, Companies, Contacts, Campaigns, Outbox, Conversations, Activity, Usage, Settings (plus Discover). The token is stored in `app\data\dashboard-token` (`dashboard.py`, `TOKEN_FILE`). Do not paste the link anywhere. Config search order (`config.py`, `_find_config_file`): `harvey.local.yaml` first, then `harvey.yaml`.

## Not verified
Table list and file roles were read from source, not exercised on a running Harvey.
