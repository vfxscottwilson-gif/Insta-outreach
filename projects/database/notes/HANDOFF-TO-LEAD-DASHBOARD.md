# Handoff to the Lead Dashboard chat (main app, chosen by the user on 2026-11-04)

The user ran two builds of the same dashboard and picked **Lead Dashboard** (`D:\All Automations Records\Lead Dashboard`, Flask + SQLite) as the main app. The "Database" build (React + Supabase, folder `F:\Github Repos\projects\database`) is frozen; nothing there is deleted. This file carries over everything the user asked for in the Database chat and what its red-team found, so nothing is lost. Treat it as input, not orders: keep what your code already does well, and ask the user in one batch before changing a rule they approved in your chat.

## Read these (all under `F:\Github Repos\projects\database\`)
| File | Why |
|---|---|
| `USER-REQUEST.md` | The user's own words (voice dictation, rambling). The source of truth for what they want |
| `UI-SPEC.md` | Every screen they would see (section 4) and the red-team amendments (section 7). Reuse the screen list and content, not the React code |
| `BRIEF.md` sections 5 to 7 | Metric definitions, roles, the removal flow, 39 red flags with fixes |
| `REDTEAM.md` | 105 findings, 40 verified; the exact fixes |
| `recon/recon-findings.json` | Facts about the lead bot's sheets and columns, ICP rules, Harvey, Google quotas |
| `brand/database-logo.svg` | The 3D purple logo the user supplied and approved (render checked) |
| `reference/` | The 3 dashboards the user liked (layout inspiration) and the logo reference |
| `lead-dashboard-preview/` | Screenshots of your app as it runs today (fake demo data) |

## What the user asked for in the Database chat, compared with what your app has today
| Requirement (from `USER-REQUEST.md`) | Lead Dashboard today | To do |
|---|---|---|
| Scan sheets every 1-2 minutes, live numbers | `sync_minutes` default 60 | 1-2 min with a cheap tail read per lead tab (see scanner rules below), "last synced" on every number |
| Add / remove sheets and tabs from the app, paste a link | Done (registry, add/disconnect) | Keep. Add the access test with the "share with this email as Viewer" hint (you have `service_email`) |
| Categorise by country, **state**, niche; **time zones** of the countries | Country, niche, category rules (`categories.yaml`) | Add state, a time-zone table (US, CA, AU by state; GB, IE, NZ, AE, SA, QA by country), local time now and "inside business hours" next to Pakistan time. Harvey's `zone_for` in `D:\All Automations Records\Harvey\harvey\send_window.py` is a reference |
| Leads this day / week / month / **last month**, per automation, emails / names / phones found | Day, month, last month, month-to-date delta | Add week; a per-sheet (automation) table with leads, emails, names, phones found for the period |
| Leads **used / reached** | Status funnel | See "Reached" below |
| Which sheet or leads are assigned to which employee | Admin-only assign/unassign by lead | Add whole-sheet / tab assignment (standing rule so new leads auto-assign) and a people x sheets view |
| **Two admins**, count includes the user, admin can change the cap; admin changes everything (sheet names, employees, caps, access) | One admin | Admin cap setting (default 2, includes the owner), owner-only switches (cap, promote/demote, retention), both admins approve |
| **Employee folder / dashboard**: each employee sees their own dashboard; admin sees how many sheets each employee has access to | "My leads" with counts | Per-employee dashboard (assigned, progress, my sheets and access level, my adds, my requests); admin employee folder |
| Give each employee access to **specific sheets or data**, remove it later | Employees see only their assigned leads | Per-sheet access (Hidden / View / Contribute) in addition to assignment; assignment never grants visibility |
| **Fail-safe**: employees can add data but cannot remove it; removal needs admin approval | Tab vanishing is marked "Removed from sheet"; admin Yes/No | Employee "Request removal" -> **Approvals** folder (admin sidebar, count badge, all employee requests and queries land there) -> either admin approves or rejects -> Trash (30 days) -> purge with typed confirmation. Employees can add leads (form / paste) |
| **Approvals folder** where all queries land | None | Removal requests, rows missing in source, employee-added lead batches, later access requests |
| Notifications and live updates | None | Bell with real events (request waiting, scanner stopped, sheet lost access, burst of new leads); push/Telegram later |
| Lead **quality vs their ICP** (their draft-prompt ICP; "7/10") | `score` column shown | Show the bot's `ICP Score /10`, Tier, Segment unchanged; note the bot writes HAS-AGENCY and POLISHED-NO-SIGNAL below 7 (side segments); add completeness KPIs (personal email, decision maker, phone, website) |
| "Use Harvey" | Not used | Reference only: `fit.py` (score with reasons) and `send_window.py`. Do not run Harvey; any AI step needs an API key, never the Claude subscription login |
| Same look and feel as the CRM and Outreach apps, **3D alive logo**, animation vibe | Plain light default theme, no logo | Purple family tokens from `levelup-crm\app\src\index.css` and Outreach `theme.css` (#846aff dark, #6E4CF5 light), the logo, Apple-like motion, reduced-motion respected. Your own DESIGN-SPEC.md already has the tokens |
| Works on phone and for employees | Local PC; nav wraps untidily on phone | Mobile nav (drawer), and a way for employees to reach it (see open questions) |
| Same login standard (email + password, one active session, reset by code, admin portal) | Done (61 tests) | Keep. Reset codes need the Gmail app password (not provided yet) |
| Everything tested for real, not on paper | 275 tests | Add browser tests (Playwright) of every screen as admin and employee |

## Red-team findings that apply to your app (full text in `REDTEAM.md`; numbers = red flags in `BRIEF.md` section 7)
1. **Reached has no writer (23).** Nothing writes Status into the lead sheets, so a "reached" KPI would read about 0. Define reach as events: "Mark contacted" in the app (audited, any role on their leads) + sheet Status moving to Contacted / Follow-up 1-2 / Replied / Call booked / Client **after** the first import (observed time). Rows already past New at first import = "reached before tracking" (own bucket). Sticky. Show "Not tracked yet" instead of 0. Waiting to contact = usable AND New AND no reach event.
2. **Removals must be durable (24).** A resync, re-added sheet or backfill must never re-import a removed lead: keep a tombstone (place id + email hash + sheet) and make every ingest path (tail, sweep, resync, backfill, manual add, paste) check it. Purge = anonymise in place, never hard-delete. Dialogs say: "Removes it from the dashboard only. The row stays in the Google Sheet."
3. **Do not contact (25).** Set in the app by any role, enforced at once in lists, assignment and exports. It cannot reach the senders through Viewer-only sheets; give the owner a to-do with a Copy button for the sheet's Blacklist tab.
4. **Owner-only switches (26).** Admin cap, promote/demote, retention, auto-purge: owner only, enforced server-side, not just hidden in the UI.
5. **Contact fields (27).** Server-side rule, not a hidden column: employees get "has email / has phone", and a logged Reveal action returns the contact; exports checked and capped, off by default for employees.
6. **Period numbers (28, 8).** Count today / week / month / last month by `Lead Added On` (sheet date, in each sheet's own zone: the Stats tab says "Dates in <TZ>"; UTC worldwide, Sydney in the AU edition). Pakistan time only for live arrival views. First import = "history", never "today". Side segments count in the headline total, not in Usable / Waiting / Average quality.
7. **Scanner rules (29, 30, 31, 39).** State per tab keyed by Google `sheetId` (not title); lead tab = header has `Place Id` + `Company Name` after dropping the bot's reserved names (`leadbot.py:43-44`) and `OLD ` tabs; tail range starts AT the anchor row (a tab filled to its last grid row otherwise returns HTTP 400 and kills the whole batch); on a 400 retry tab by tab; a sheet is "synced" only if all tabs read; "missing in source" only after 2 consecutive complete sweeps and with a breaker (more than min(50, 5% of rows) vanishing = one sheet-level item); narrow sweep (Place Id + Status columns) every ~10 min for edits to existing rows; identity = Place Id per sheet, never a row number; weak merge keys (linktr.ee, site builders) never group leads.
8. **Run health (34).** Read the Stats tab heartbeat (Last run, Run health, Dates in TZ); Late/Stopped come from that, never from "no new rows". Alert the owner when the scanner itself stops (dead-man check; a local PC that sleeps will stop it, so say so).
9. **Audit (33).** Append-only; explicit audit rows for lead actions; never copy names and emails into an unremovable log; the purge scrubs them.
10. **Employee-added leads (35).** They reach any export or Outreach feed only after admin approval; paste cap 200 rows; daily add cap.
11. **Backup (36).** Say what the backup is and rehearse a restore once (SQLite file copy + sheets re-scan rebuilds leads; only app-owned state cannot be rebuilt).
12. **Quota (2).** The 60 Google reads/min per service account is shared with the lead bots, outreach bot and CRM. Use a dedicated service account (or at least a budget of 45 reads/min with a counter shown in the UI).

## Write-back: needs one decision
The user wrote in the Database chat that they will give read **and write** access, and approved write-back in yours. The red-team found writing into the bots' sheets risky: the lead bot finds its "last used row" from watched columns plus **any column not in its own header list**, writes with an explicit range, and a header named like a bot column gets the bot's value in both. Your safeguards (only status + assignee, found by Place Id right before writing, switch off with `DASH_WRITEBACK=off`) are a good start. Before turning it on against real sheets: prove with the lead bot's own last-row logic that the write-back columns do not move its append position, pilot on one sheet, and keep it off by default until the user confirms. Never write `My Notes` (your rule, keep it).

## Open questions for the user (ask once, in one batch, with defaults)
1. **Theme and name.** Purple family like the CRM and Outreach (default) or black-and-white (an earlier request in your chat)? Keep the name "Lead Dashboard" or call it "Database" with the new logo?
2. **How do employees reach it?** "Local PC first" means only the user's PC. Options: same Wi-Fi only; a free tunnel (Cloudflare Tunnel) to the user's PC (PC must stay on); or host it later. Default: local first, then host.
3. **Reached:** may employees press "Mark contacted"? Default yes.
4. **Write-back:** on or off for the first real run? Default off until the pilot proves it is safe.
5. **Inputs you already asked for:** sheet URLs / IDs, Gmail app password for reset codes, a Google service account. The user signed up for a Supabase account with a second Gmail; that is not needed for this app (it only matters if the app is later hosted on Supabase).

## Rules
No push without the user's OK. No secrets in chat or code. Test data only fake (`.test` domains). Commit each working step. Report to the user: done / not done / not verified, with proof (test output, screenshots).
