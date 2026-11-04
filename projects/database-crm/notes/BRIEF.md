# Database app: Goal-first brief, analysis and red flags

Status: **FROZEN 2026-11-04. The user chose the Lead Dashboard (`D:\All Automations Records\Lead Dashboard`, Flask) as the main app; this brief is now reference material for it (see `HANDOFF-TO-LEAD-DASHBOARD.md`).** Was: DRAFT v3 (2026-11-04). v1 = recon. v2 = your answers. v3 = red-team review folded in (6 independent reviewers, 105 findings, 40 adversarially checked, all 40 survived; details in `REDTEAM.md`).
**Answered by you:** 2 admins including you; both approve and remove; a folder named Approvals in the admin section; every employee has their own dashboard; the extra features are accepted; you want at least 1 GB free storage if one exists, otherwise Supabase.
**Decided (section 13):** stay on Supabase with a lean mirror and automatic log trimming (500 MB lasts about 7 years at your bot's volume; no free 1 GB option keeps login, access rules and live updates). **Checked in your Supabase dashboard (2026-11-04):** organisation "Level Up VFX", Free plan, 2 projects, so there is no free slot. **Your decision (2026-11-04):** no paid plan; Database goes on a Supabase account made with a different Gmail address (**confirmed by you 2026-11-04**; you sign up yourself, I do the rest). **Still open:** 4 short questions A-D (section 11) and the brief approval.
Inputs: your message (`USER-REQUEST.md`), 4 reference images, 7-agent recon (`recon/recon-findings.json`), red-team (`REDTEAM.md`).

## 1. Goal

| | |
|---|---|
| **Goal** | See at one glance how many good leads every automation produced (today, week, month, last month), where they are (country, state, time zone), what niche, who is working on them, and how many were reached, without ever losing data. |
| **Done when** | 1. Add a sheet by pasting its link: access tested, tabs and columns auto-detected, no header setup. 2. Pilot on 2 real sheets: per sheet, the app's rows and the counts by `Lead Added On` (today, 7 days, this month, last month) equal a SQL count AND the sheet's own Stats tab (`Total leads`, `Leads today`); new-lead lag is measured and shown. 3. A new lead appears in the app within 2 minutes (measured, not promised; if the pilot shows Google's change signal is slower, the gate stays off and the 60 s tail read is used). 4. Overview, per-automation, per-country/state/niche, quality and daily report numbers equal a SQL count on the same data, and Overview, the Automations table and Leads filters agree for the same range. 5. An employee can add a lead and cannot delete anything; a removal request lands in Approvals; nothing is removed until an admin approves; approved removals sit in Trash and can be restored; a purged lead does not come back after a full resync or a re-added sheet. 6. Per-sheet access proved by tests: an employee with no access to sheet X gets 0 rows from it through the app and the API, never sees its name, notes or status through lists, search, filters, "also in" or add-lead; an employee JWT running `select *` on the contact table gets nothing. 7. Max admins enforced in the database (default 2, includes you); only the owner can change the cap or promote/demote an admin; the owner cannot be removed or demoted. 8. Same login standard as the other two apps (email + password, one active session, reset by code). 9. Every screen tested in a real browser on desktop and phone (Playwright); RedTeam pass on auth, RLS and the delete flow. 10. A restore drill done once before launch, with the steps written in `CLAUDE.md`. 11. "Reached" shows its source and "Not tracked yet" where no source exists, never a false 0. |

## 2. What I found (the facts that shaped the design)

| # | Finding | Source |
|---|---|---|
| 1 | Your only real lead producer is the lead bot: worldwide = up to 10 Google Sheets (US, CA, GB, AU, NZ, IE, optional AE, SA, QA, one YOUTUBE), AU-only edition = 1 sheet. Each sheet = one tab per niche + a visible Stats tab + hidden Meta tab + control tabs. Lead tabs are found by header (row 1 has `Place Id` and `Company Name`) after dropping the bot's reserved tab names and tabs starting with `OLD `. 74 columns (82 in AU). | `au-lead-bot` CONTRACT.md, `leadbot.py:43-44` |
| 2 | The bot is **append-only**: it adds rows under the last row, never sorts, inserts or deletes lead rows. `Status` and `My Notes` are edited later by people. **No tool writes Status back today** (the draft bot never writes to a lead sheet, Outreach reads sheets read-only, IG logs by handle). | same, red-team |
| 3 | `Lead Added On` is a **date only** (YYYY-MM-DD, in the sheet's own zone: UTC worldwide, Sydney in the AU edition). The Stats tab says "Dates in <TZ>". There is no time of day on any lead row. | same |
| 4 | Rows arrive in **bursts**: two ~42 minute jobs a day (worldwide 08:00 and 20:00 UTC, AU-only 07:00 and 19:00 UTC). "Live" means "live during those windows". | same |
| 5 | **Quality already exists**: the bot writes `ICP Score /10` and refuses to add a lead below 7, **except** the HAS-AGENCY and POLISHED-NO-SIGNAL side segments, which it writes at 6 or above (often below 7) and the draft bot never pitches. Tiers: A >= 8.5, B >= 7.5, else C. | `leadbot.py:1001-1039`, quality.py |
| 6 | "Hard ceiling" is **not defined for lead intake or quality** anywhere. It only appears for email sending (Gmail 70/day, domain 650/day). | SCHEMA.md, DESIGN.md |
| 7 | The CRM's Google Sheets code only writes the CRM **to** one sheet and asks for the full write scope. Reusable: service-account login, retry wrapper, cron-secret pattern, login/reset/single-session, owner protection, admin-users function. | CRM `supabase/functions/sheets-sync` |
| 8 | The Outreach web app is a clean cloneable shell (new screen = 1 route file + 1 feature folder + 1 line in `nav.ts`) on mock data and a demo login. Its delete-approval trigger (migration 0005) and its owner + 2-admin cap (migration 0015, not yet committed) are the templates for your rules. | Outreach `web/`, `supabase/migrations` |
| 9 | Supabase Free: **2 active projects total** (CRM uses one, Outreach plans one), **500 MB** per project, **no backups**, pauses after 7 idle days. Pro: $25/month per organisation (includes a $10 compute credit), 8 GB, daily backups for 7 days, no pausing. | supabase.com/pricing + docs, 2026-11-04 |
| 10 | Google Sheets API: **60 reads/min per user per project** (a service account = 1 user), 300/min per project; one `batchGet` = 1 read. Your lead bot and outreach bot already use the shared service account. | developers.google.com limits + 2 sources, 2026-11-04 |
| 11 | Best 1-minute runner: Supabase `pg_cron` -> `pg_net` -> one Edge Function per tick (43,200 calls/month = 8.6% of the Free 500k). Rejected: GitHub Actions (5 min minimum, hours of delay), Vercel Hobby cron (once a day), Cloudflare Workers Free (10 ms CPU). Fallback: the VPS planned for Outreach. | docs, 2026-11-04 |
| 12 | Harvey is an **autonomous cold-email sender** (CAUTION in your registry), single-user SQLite, no Sheets reader; its brain uses your Claude subscription login, which Anthropic's terms do not cover for a multi-user app. Worth borrowing: `fit.py` and `send_window.py` (`zone_for`). | `D:\All Automations Records\Harvey` |
| 13 | A lone `YouTube` sheet exists in two shapes: the lead bot's YOUTUBE sheet (has `Place Id` like `yt:UC...`) and the separate `yt-creator-client-finder` (Lead_ID, Company_Name, Quality_Segment, Score, Found_At_PKT; **no Place Id**). | red-team, sample CSV |

## 3. Options researched

| # | Option | Verdict |
|---|---|---|
| A | Sheets stay the database; app reads only each sheet's Stats/Meta tab. No per-lead features, fail-safe unenforceable. | Reject |
| B | **Mirror lead rows into Postgres, Sheets read-only, all app state in the database.** Real access control, enforceable fail-safe, cannot corrupt the bots' sheets, same stack as your other apps. | **Pick** |
| C | Change the bots to write straight into Postgres. Cleanest but touches working bots. | Later option |
| D | Off the shelf (Looker Studio, Metabase, NocoDB, Airtable). No per-sheet employee access, no approvals, no shared theme. | Reference only |
| E | Run Harvey as the engine. It sends emails by itself, one user, subscription-login risk. | Reject; borrow 2 ideas |

## 4. Pick and architecture

```
Lead bots (unchanged, append-only) --> Google Sheets  (shared as VIEWER only, with a NEW service account in its own Google Cloud project)
                                           |  every 60 s: tail read of each lead tab (+ Stats heartbeat every 5 min) ; every ~10 min: narrow sweep (Place Id + Status columns)
                                           v
     Supabase pg_cron --> pg_net --> Edge Function "scan-sheets"  (lease lock, per-tab state keyed by Google gid, read budget 45/min, dead-man ping)
                                           |  ONE ingest function writes lead_sources (unique sheet_id + place_id)
                                           v
        Postgres: sheets, tabs, lead_sources, leads (derived grouping), lead_contacts (no employee SELECT), reach_events, do_not_contact,
        niches, geography, quality, assignments + assignment_rules, sheet_access, deletion_requests, audit_log (append-only), daily_stats
                                           |  Realtime carries only a scan tick, counters, requests and alerts (never lead rows)
                                           v
        Web app: Outreach shell (Vite + React + TS + Tailwind 4 + shadcn + TanStack Router), PWA, Cloudflare Pages Free
        Export: app-owned Google Sheet "Database - added leads" (employee-added leads after approval; Outreach reads it like any source)
```

- **Sheets are read-only by scope, not by a dropdown**: the scanner asks only for `spreadsheets.readonly` and `drive.metadata.readonly`; a build test fails if scanner code references `batchUpdate`, `batchClear` or `values:update`; the wizard warns when a sheet is shared as Editor. A separate write token (same service account) exists only for the app-owned export sheet.
- **Auth** is copied from the CRM (live and tested there): email + password, sign-up off, admin creates accounts, forced password change, reset by 6-digit code, one active session via `claim_session`.
- **Quality** shows the bot's `ICP Score /10`, Tier and Segment as they are, plus completeness metrics that do move; side segments are shown but excluded from the headline averages by default.
- **Hosting**: Cloudflare Pages Free (commercial use allowed; Vercel Hobby is non-commercial).

### Scanner rules (from the red-team; the builders follow these exactly)
1. State per tab (cursor, anchor hash, last ok, last error, header hash) is keyed by Google's `sheetId` (gid), never by tab title; niche comes from the Niche column.
2. A lead tab = row 1 has `Place Id` and `Company Name`, after dropping the bot's reserved names and `OLD ` tabs; the wizard shows dropped tabs with the reason.
3. Every tail range starts AT the anchor row (so it is always inside the grid; a tab that fills exactly to its last row cannot make Google return a 400). Tab titles are quoted; batchGet chunked at 40 ranges.
4. A 400 on a batch re-runs that sheet's tabs one by one; a failing tab gets its own error and a resync entry while the others keep syncing. A sheet is "synced" only when every tab read succeeded.
5. The ~10 minute sweep reads the full Place Id + Status columns per tab, diffs against what is stored and fetches rows whose key is new or changed. Rows with no usable key are parked as "incomplete".
6. "Missing in source" is judged per spreadsheet, only after a key is absent from 2 consecutive complete sweeps, never after an errored or rate-limited sweep. If more than min(50, 5% of active rows) vanish at once: one sheet-level Approvals item and the sheet is marked "needs attention".
7. Only `lead_sources` is written by the scanner. One ingest function handles every path (tail, sweep, resync, backfill, re-added sheet, manual add, paste) and its identity lookup includes trashed and purged rows, so a removed lead never returns as new.
8. Read budget: every Google call is logged; 45 reads/min per tick budget spent in the order live tails, safety net, sweep; on a 429 the invocation ends and a `blocked_until` is stored (no sleeping).
9. Drive `modifiedTime` gate is a feature flag, OFF by default; turned on only if the pilot shows it trips within 30 s.
10. The scanner never ingests the app-owned export sheet.
11. Run health: per sheet the Stats heartbeat (Last run, Run health, Total leads, Dates in TZ) is read; Stopped = lost access or two crashed runs; Late = no new Last run after the expected window; never "late" from the absence of rows. A dead-man ping (Healthchecks.io, free) goes to you by email and Telegram, plus a SQL-only watchdog that raises a bell notice when the last good scan is too old. A nightly reconcile compares non-blank Place Ids in each tab with the app.

## 5. How the numbers are defined (so every figure is checkable)

| Term | Definition |
|---|---|
| Row (source row) | One line in a sheet tab. Visibility, access, assignment, trash and removal work on source rows |
| Lead (grouping) | Derived, reversible link for Owner/Admin totals: exact Place Id, else canonical email (Personal/Generic email only, never free-mail), else website domain (never social, aggregator or site-builder hosts such as linktr.ee); no chaining across key types; admins can Unmerge. "Also in" and "unique leads" are computed only from rows the viewer may read |
| Period (today, this week Mon-Sun, this month, last month, daily report) | Counted by `Lead Added On` (sheet date) in each sheet's own zone (the same number as that sheet's Stats tab). The cross-sheet "Leads today" sums each sheet's own today; it shows no delta and says "each sheet's own date". Monthly totals are frozen into `daily_stats` at month end. **Default pending your answer (question C)** |
| First seen | Exact time the scanner first saw the row, in Pakistan time. Used only for the live strip, arrival hour and burst charts, and only for rows found live (previous successful read of that tab <= 15 min earlier). Everything from the first import, a resync or a longer gap is "history" and excluded from those charts |
| Usable lead | Valid contact route AND Segment not in the skip list (default HAS-AGENCY, POLISHED-NO-SIGNAL, like the draft bot) AND Status not in (Do not contact, Not interested, Unsubscribed, Bounced) AND not on Database's do-not-contact list |
| Waiting to be contacted | Usable AND Status blank or New AND no reach event |
| Reached | The lead has at least one **reach event**: (a) "Mark contacted" pressed in the app (audited), (b) the scanner sees the sheet Status move to Contacted, Follow-up 1/2, Replied, Call booked or Client after the first import, (c) later: the Outreach app's mail events through the app-owned export sheet. Rows already past New at first import are "reached before tracking" (own bucket, never in "this month"). Reached is sticky. Every tile shows its sources and "last reach event N days ago"; with no source it says "Not tracked yet", never 0. Reach % = reached / usable |
| Headline "Leads" | All rows (equals each sheet's Stats `Total leads`), with a subline "of which N side-segment" |
| Quality | Bot score unchanged + completeness (personal email, decision maker, phone, website, socials, verified email). Average and Tier mix use core segments by default (toggle includes side segments). For sheets without a score, a fallback 0-10 using the bot's weights (niche budget fit 3.0, contactability 2.5, target country 1.5, decision maker 1.0, size/reputation 1.5, website/social 0.5) |
| Missing in source | A row that disappeared from its sheet. Never deleted in the app; goes to Approvals |
| Sheet capacity | Cells used / the bot's own stop at 9.5M (Google now documents 20M cells; the meter follows the bot's limit) |

## 6. Roles, access and the delete fail-safe

| | Owner (you) | Admin (2 including you) | Employee |
|---|---|---|---|
| Add / remove / re-map sheets, niches, ICP, general settings | Yes | Yes | No |
| Create / remove people, set access per sheet | Yes | Yes (cannot touch the owner) | No |
| **Owner only**: set the admin cap, promote or demote an admin, Trash retention, auto-purge switch, anything that widens admin rights | Yes | Read-only, with the reason shown | No |
| Approve or reject a removal request, remove leads, purge Trash | Yes | **Yes** (your decision: both admins) | No |
| Delete a lead | Goes to Trash first | Goes to Trash first | **Cannot.** Can request removal |
| Add a lead (form or paste, max 200 rows, daily cap) | Yes | Yes | Yes where access = Contribute; audited "added by" |
| Edit imported fields | No (the sheet is the truth) | No | No |
| Notes, tags, Mark contacted, Do not contact | Yes | Yes | Yes on accessible leads |
| Export | Yes | Yes | Off by default; allowed per person, row-capped, logged, through a checked server function |
| See a sheet | Yes | Yes | Per sheet: Hidden / View / Contribute; scope whole sheet or only assigned leads; assignment never grants visibility |

**Approvals folder:** a sidebar item named **Approvals** (count badge) in the admin section. Every request and query from employees lands there: removal requests first, then employee-added lead batches for Outreach, access requests and rows missing in a sheet. Both admins see it, get a bell + push, and either can approve or reject.

**Removal flow:** employee clicks "Request removal" + reason -> pending in Approvals -> either admin Approves or Rejects (with a note) -> Approve moves the leads to Trash (30 days, restorable) -> Purge needs an admin's typed confirmation (lead count and sheet name). The dialogs say: "Removes it from Database only. The row stays in the Google Sheet. Only you can delete it there."

**How it is enforced (not in the UI):**
- No role has DELETE or TRUNCATE on any table. Purge is one locked function that **anonymises in place** (personal fields, notes, tags, assignment emptied; Place Id, email hash, domain and sheet kept as a tombstone) so a resync can never re-import the lead. The scanner's database role gets select/insert/update only; `audit_log` is append-only for every caller; all foreign keys are RESTRICT (people and sheets are deactivated, never deleted).
- Contact fields live in a separate table with no employee SELECT. Employees get "has email / has phone" flags and read contacts only through a Reveal function that checks session, sheet access, scope and permission and writes the audit row in the same transaction. Say it plainly: this is audit and friction (company, city, website and Place Id stay visible), not secrecy from someone with access to the sheet itself.
- Lead actions are audited through explicit rows (assign, mark contacted, do-not-contact, request, approve, reject, trash, purge, reveal, export, access change), never a whole-row trigger that would copy names and emails into an unremovable log; purge scrubs that lead from the log.
- Realtime never carries lead rows. Employees get no direct Google Sheets access; the app is the only door.
- **Do not contact**: set in the app by any role, enforced at once in Usable, Waiting, assignment and every export; it is NOT written into the bots' sheets. Outward delivery: an owner to-do "Add X to the Blacklist tab of sheet Y" with a Copy button now; when Outreach goes live, the same keys go to the app-owned export sheet's Blacklist tab, which Outreach registers as a source, with an alert after 1 h if undelivered.
- **Standing assignments**: assigning a whole sheet or tab creates a rule so new leads from the next bot run are assigned automatically ("also assign new leads that arrive", default on); unassigned for over 24 h shows in Needs you.
- **Employee-added leads** appear in Database at once but reach the export sheet (and so the email sender) only after an admin approves the batch ("Send to Outreach" tab in Approvals); exported columns are limited to email, company, country, niche, city, state, website. These are the only rows that cannot be re-scanned, so the export is also their backup.
- **Backup:** Supabase Pro daily backups (7 days): data loss up to 24 h, same-day recovery. Restore goes to a NEW project, and its pg_cron jobs are unscheduled before anything else (they start at once and would call production). Lead rows can always be rebuilt by re-scanning the sheets; only app-owned state (assignments, notes, tags, requests, audit) cannot. If you stay on Free (section 13) this is replaced by a nightly export of that app-owned state.

## 7. Red flags found and the fix for each

| # | Sev | Red flag | Fix |
|---|---|---|---|
| 1 | High | Supabase Free: no backups, pauses after 7 idle days, only 2 projects (CRM + Outreach already use them) | Section 13 (data plan) |
| 2 | High | Shared Google quota: 60 reads/min per user; bots and CRM already use the same service account | New Google Cloud project + new service account for Database only; hard limit 45 reads/min shown in the UI |
| 3 | High | Writing into the bots' sheets would corrupt them (stray cell moves the bot's "last row"; a header named Status/Country gets the bot's value in both columns; renaming `Place Id`/`Company Name` breaks dedupe; a title row breaks tab detection; reserved tab names collide; two writers overwrite each other) | Viewer-only share, read-only scopes, all app state in the database, export to an app-owned sheet only |
| 4 | High | "Live" is bursty and Google's change signal may lag (Drive `modifiedTime` for Sheets reported ~3 min; API appends not documented) | 60 s tail read, gate OFF until the pilot proves it; every number shows "last synced" |
| 5 | High | Existing rows change (Status, My Notes); a tail read only sees new rows | Narrow sweep every ~10 min (scanner rules 5) |
| 6 | High | Employees with edit access to the Google Sheets could delete rows there | Employees get no sheet access; vanished rows become "Missing in source", never an automatic delete |
| 7 | Med | Quality chart looks flat; two score formulas share one column (YouTube older v3) | Show as-is with Tier/Segment, 0-10 axis, core segments by default, completeness KPIs, per-row formula tag |
| 8 | Med | Date-only dates in different zones (UTC, Sydney) vs Pakistan time | Period numbers use each sheet's own date; Pakistan time only for live arrival views (question C) |
| 9 | Med | No stable row id; users may reorder tabs/columns | Identity = Place Id per sheet, never a row number; per-tab state by gid; anchor check |
| 10 | Med | Sheet cell cap | Capacity meter + alert at 80% |
| 11 | Med | Duplicates across sheets | Visibility on source rows; grouping only for admin aggregates; weak keys excluded |
| 12 | Med | Realtime ignores RLS on DELETE; deleted rows do not shrink the DB | No DELETE grants; flags and tombstones; Realtime carries no lead rows |
| 13 | Med | CRM has only a floor of 1 admin; races | Port Outreach 0015 (`is_owner()`, locked cap); owner-only switches; refuse a cap below the current count |
| 14 | Med | Employees can copy the lead list | Export off by default; contact table with no employee SELECT; Reveal and export are logged server functions with caps; watermark |
| 15 | Med | Reset by code is not live in the CRM yet (no SMTP; Free blocks template edits) | One shared SMTP for all three apps (you provide an app password; I never type or print it) |
| 16 | Med | First import is big (Edge limits 2 s CPU, 150 s wall) | Chunked backfill across ticks with progress; rows tagged "history" |
| 17 | Med | Personal data from AU/US/GB/IE/CA/NZ/AE/SA/QA (GDPR, UK PECR, AU Spam/Privacy Acts, CASL). Not legal advice | Do-not-contact list, removal-on-request executed by an admin, retention setting, access log. Legal review deferred (lawyer, not this project) |
| 18 | Med | Anthropic terms: subscription login is not for a multi-user app | Any AI step uses an API key stored as a secret (Harvey option B is deferred) |
| 19 | Low | Vercel Hobby is non-commercial | Cloudflare Pages Free |
| 20 | Low | Cloning Outreach: hard-coded `outreach-*` keys, cookies, manifest, PWA colours | Renamed in the first commit; checked by QA |
| 21 | Low | Outreach web has a demo login | Database copies the CRM's tested auth |
| 22 | Info | No real sheets on disk: volumes are estimates, fill rates unknown | The pilot decides |
| **23** | **High** | **"Reached" has no writer**: nothing writes Status into the lead sheets, so the headline KPI and every employee progress bar would show about 0 | Reach events (section 5); "Not tracked yet" instead of 0; source label on every tile. Question A |
| **24** | **High** | **Removals are not durable**: a full resync, re-added sheet or sibling row re-imports a purged lead as new; the row also stays in the sheet and in Outreach | Tombstone on purge; one ingest function that skips trashed/purged keys; dialogs say the sheet row stays; test: trash, purge, resync, re-add, lead must not return |
| **25** | **High** | **Do not contact never reaches the senders** (sheets are Viewer-only; Outreach reads only its own suppression list and Blacklist tabs) | Database-side list enforced at once; owner to-do with Copy button; Blacklist tab on the export sheet when Outreach is live |
| **26** | **High** | **"Owner only" is not enforced as owner**: templates test "any admin", so the second admin could raise the cap, mint admins, set retention 0 | Owner-only group, `is_owner()`, one small table writable only by the owner; test: second admin gets 42501 |
| **27** | **High** | **Contact masking is UI-only**: RLS filters rows, not columns, so an employee JWT can pull every email and phone through the API, unlogged | Separate contact table, Reveal and export functions, leads out of Realtime; test in Done-when 6 |
| 28 | Med | Day basis contradicted itself; first import would stamp history as "today", "last month" = 0, burst chart one spike | Sheet date for periods; first-seen only for live rows; pilot check right after import |
| 29 | Med | One out-of-grid range fails the whole batchGet (a tab full to its last row, ~28-30% of 200-row cycles) | Tail starts at the anchor row; bisect failing batches; per-tab errors; fixture test |
| 30 | Med | "Missing in source" storms from tab renames, row moves, half-saved headers | Per-tab state by gid; 2 consecutive complete sweeps; breaker min(50, 5%); "key column changed" guard |
| 31 | Med | Weak-key merges (linktr.ee, site builders) collapse unrelated leads and leak a hidden sheet's data | Source-row visibility; grouping only for admin aggregates; no chaining |
| 32 | Med | Side segments break the quality numbers (below 7, never pitched) | Corrected finding 5; Usable and Waiting exclude them; averages on core segments |
| 33 | Med | The scanner's own database role could delete or overwrite everything; a whole-row audit trigger would freeze names and emails into an unremovable log | Select/insert/update only; append-only audit; explicit audit rows; purge scrubs the log; privilege-matrix test |
| 34 | Med | Nobody is alerted when the scanner stops (every alert runs on the chain that died; pg_cron reports success once the request is queued) | Dead-man ping + SQL watchdog + red Live strip + "data as of" on reports; pilot: disable cron, phone alerted within 15 min |
| 35 | Med | Employee-added leads flow unreviewed into the sheet the email sender reads | Export only after approval, limited columns, paste cap 200, daily add cap |
| 36 | Med | Backup and restore undefined; a "snapshots" table in the same database is not a backup; a restored clone starts cron against production | Backup statement (section 6), restore drill, unschedule cron first |
| 37 | Med | Assignments are one-time lists: an "assigned only" employee never sees the next bot run's leads | Standing assignment rules; refuse assigning to someone with Hidden access |
| 38 | Low | The CRM Google helper requests the write scope and ships `batchClear` | Pin read-only scopes; import only the token helpers; build test |
| 39 | Low | Header-only detection would ingest the legacy v4 "All Leads" view and double rows | Reserved-name and `OLD ` filter before the header check |

## 8. Time zones and geography
- Country and ISO-2 code from the sheet; state abbreviations for US/CA/AU; one time-zone table: US, CA, AU by state (plus the AU edition's `AU Timezone` column), GB/IE/NZ/AE/SA/QA by country. Method borrowed from Harvey's `zone_for`.
- Every lead and country shows local time now, "inside business hours (9-17 local)" and the matching Pakistan time.
- Niche: the bot's `Niche` + `Niche Group` become a two-level tree. Unknown values land in an "Unclassified" queue you map in one click (the rule is saved).

## 9. Harvey: what "also use Harvey" becomes
| Option | What | Verdict |
|---|---|---|
| A | Native scoring and time-zone code in Database, using Harvey's `fit.py` / `send_window.py` as the design reference | **Default (accepted)** |
| B | "Ask Harvey" button through an Anthropic API key (never the subscription): suggests a score and a note, saved apart, never written to a sheet | Deferred |
| C | Run the real Harvey as a separate worker | Only if needed |
| No | Harvey's autonomous prospecting or sending on these leads | Not recommended |

## 10. Workstreams (each its own titled chat, all in the sidebar group "Database app (lead tracking)")

| # | Chat | Owner / model | Output | Done when | Starts |
|---|---|---|---|---|---|
| 0 | Database app: Control room | Opus-level (me) | brief, tracker, verification | each chat's proof checked | now |
| 1 | Database UI: clickable preview | Sonnet builders, Opus review | `app/web` preview + proof | you can click every screen, desktop and phone | **running** |
| 2 | Build: schema, RLS, auth | Opus designs, Sonnet writes | migrations + pgTAP tests | access, owner-only, 2-admin cap, request flow, tombstone, privilege matrix proved | after your approval |
| 3 | Build: sheet scanner | Opus designs, Sonnet writes | Edge Function + cron + pilot numbers table | pilot P1 below | after approval and the sheet shares |
| 4 | Build: web app on real data | Sonnet | screens live on Supabase | Playwright passes desktop + phone | after P1; ships Overview + Sheets + Leads first, then Team, Approvals, Reports |
| 5 | Build: quality, geography, niches | Sonnet, Opus review | score engine, time-zone table, niche tree | numbers equal SQL checks | after approval |
| 6 | Build: notifications and reports | Sonnet | bell, push, daily report, dead-man alerts | report arrives at the set time | after 4 |
| 7 | QA and red team | Sonnet; Opus RedTeam | attack tests on RLS, auth, delete flow, mobile, a11y | zero open high findings | after each build |
| G | Gates | **Fable** | go / no-go | written verdict | after P1 and before launch |

**Pilot defined once.** P1 = scanner spike on 2 real sheets, verified by SQL only: per sheet, rows and rows per `Lead Added On` (today, 7 days, this month, last month) next to that sheet's Stats `Total leads` and `Leads today`, plus measured lag (an append to a scratch tab of an app-owned sheet at a noted time); output is a one-page table you read at the gate. P2 = removal flow proved by database tests, re-run in the browser. First task of the scanner chat: read-only recon the moment a sheet is shared (tabs + hidden flag, headers, 20 sample rows per tab, Stats time zone, fill rates, grid rows vs last row). Test data policy: redacted fixtures only; no real company or contact data in the repo, screenshots or proof.

## 11. Questions

**Accepted by default (you did not object; say so if wrong):** read-only sheets with a new Google service account; quality = the bot's score unchanged plus completeness KPIs; Harvey option A only; brand "Level Up VFX"; the shipped purple theme (#846aff on near-black); the three apps keep separate logins for now; "hard ceiling" is undefined for leads, so people and admin caps are built in and lead/storage caps are warnings only (tell me if you meant something else).

**Open (answer "approve all defaults" if you agree):**

| # | Question | Default |
|---|---|---|
| A | Where is "contacted" recorded today: by hand in the lead sheet's Status, in the draft bot's own sheet, in the Instagram log, or nowhere? May employees press **Mark contacted** in Database? | Database tracks reach itself: a Mark contacted button for everyone on their leads, plus any sheet Status change it sees. The Outreach feed comes when that app is live. |
| B | Is "daily task report" the daily lead report only, or employee task reports like the CRM (title, description, time, deadline, status)? | Daily lead report only; tasks stay in the CRM. Assignments get a deadline, status and note. |
| C | Period numbers (today, week, month, last month, daily report) use each sheet's own date (the same number as the sheet's Stats tab); Pakistan time is used only for the live "arrived in the last hour" view. OK? | Yes |
| D | HAS-AGENCY and POLISHED-NO-SIGNAL leads count in the headline "Leads" (so the app matches the sheets) but not in Usable, Waiting or Average quality. OK? | Yes |
| E | For the pilot I need, in one go: (1) the second Supabase account made by you with the other Gmail (you sign up yourself; steps given in chat), then I create the project and org settings with you watching, and the access token goes into `.env` through the clipboard script, never into chat; (2) a sign-in link for a new Google Cloud project + service account (I do the rest); (3) two sheets shared as Viewer; (4) confirmation both already hold rows; (5) confirmation that the YouTube sheet is the lead bot's YOUTUBE sheet. | AU Leads + AU Only (Sydney) for the pilot; YOUTUBE added after P1 |

## 12. Not verified
- Real sheet contents, row counts, fill rates, who owns the sheets, whether the lead bot is still scheduled.
- Whether a bot's API write bumps Drive `modifiedTime` and how fast (pilot measures it; the gate stays off until then).
- Whether `pg_cron` runs every 60 s on a Free project and whether cron-triggered calls count toward the Free invocation quota (assumed yes).
- Whether a Viewer-only service account can read hidden tabs (not needed for this design).
- Google may start billing for over-quota use later in 2026 (re-check before launch).
- Legal exposure by country (not legal advice; lawyer review deferred).
- The preview is mock data only; no backend exists yet.

## 13. Data plan: where the data lives (researched and measured 2026-11-04)

**Decision: stay on Supabase, no vendor switch.** A free 1 GB database that also gives login, per-sheet access rules, live counters and a 1-minute scheduler does not exist (24 providers checked, each against 3 sources where a number was involved; see `recon/storage-research.json`).

**How long does 500 MB last with 4-5 employees and everything assigned?** Measured in a real Postgres (PGlite = PostgreSQL 18.6), not guessed: one lead costs 867 bytes at 20,000 rows, falling to about 658 bytes at scale (lean design). Assigning every lead to an employee costs one small column (about 9 bytes per lead). What actually fills the database is the activity log and the scan log, not the leads.

| Scenario (5 employees, everything assigned, lean design, 300 logged actions per employee per day) | Old logs trimmed automatically | Months until Free 450 MB is full | Months until 1 GB | Database size after 12 months |
|---|---|---|---|---|
| Your bot's own volume (about 10,000 leads in month 1, then about 2,500 a month) | no | 6.9 | 16.3 | 761 MB |
| same | **yes (audit 90 days, scan log 30 days)** | **90 (7.5 years)** | 271 | **202 MB** |
| 5,000 new leads a month | yes | 53 (4.4 years) | 165 | 238 MB |
| 20,000 new leads a month (stress case, e.g. the scraper tools running) | yes | 10.3 | 45 | 477 MB |
| Copy all 74 sheet columns instead (full design), bot volume | yes | 31 | 96 | n/a |

Reading it: with trimming, 500 MB lasts years; without trimming it fills in about 7 months, so trimming is part of the build, not optional. A full copy of all 74 columns is about 3 times bigger, so the app mirrors only the ~30 fields the dashboards use. Everything else (address, Lead Insight, Pitch Angle, socials) stays only in the Google Sheets, which remain the permanent archive and are re-read on demand.

**The plan**
- **Lean mirror** (30 fields per lead, no copy of the whole sheet row). The sheets are the raw archive; lead rows can always be rebuilt by re-scanning. Only app-owned state (assignments, notes, tags, requests, reach events, audit) is irreplaceable, and it is small.
- **Trim from day one** by scheduled jobs: audit log 90 days, scan log 30 days (written only on change or error), cron history 7 days, status history in a slim 129-byte table; the search index on company name waits until about 50,000 rows. The dead-man alert also covers the trim jobs.
- **Backup on Free:** nightly dump of the app-owned tables only into the free 1 GB file store (7 kept), plus one weekly copy outside Supabase, and a restore drill before launch. On Pro this is replaced by the daily backups.
- **Own organisation:** Database goes in its own Supabase organisation so that a quota problem there can never block the CRM or Outreach.
- **Move to Pro ($25/month, 8 GB, daily backups, no pausing)** when the 7-day average database size passes 350 MB (alert at 300), when backups or no-pausing become a business need, or on day one if there is no free project slot. The upgrade is in place, no migration.

**The one catch: Free allows only 2 projects per person, and your dashboard shows both used** (organisation "Level Up VFX": CRM and Outreach). Three ways out:
1. **A second Supabase account made with a different Gmail, Database on its Free plan there (your choice, no cost).** Supabase's own rule is 2 free projects across all organisations where one person is Owner or Admin, so a separate account has its own 2. Caveat found in the research: Supabase's Acceptable Use Policy (version 1, 1 June 2026, section 4.2) bars "an excessive number of accounts as a single user" without their permission; no number is given and the Terms of Service have no such clause. One extra account for one separate business app is a small step but not explicitly allowed. Mitigations: (a) ask Supabase support for a written OK (free email, optional); (b) the nightly dump of the app-owned data plus the weekly copy outside Supabase and the sheets as the raw archive mean a suspended account costs a rebuild, not the data; (c) do not add your main account as Owner or Admin of that organisation (it would count against the main account's 2 projects); (d) keep that Gmail's recovery details safe, because losing it loses the project.
2. Pro for Database in its own organisation, $25/month (8 GB, daily backups, no pausing).
3. Put Database inside an existing project: rejected, because the three apps would share 500 MB and one over-quota month would block all of them.

| Option checked | Free storage | Verdict |
|---|---|---|
| **Supabase Free, own org, lean mirror + trimming + nightly app-state dump** | 500 MB quota (about 450 MB usable), 1 GB file store | **Pick, if a free slot exists** |
| **Supabase Pro, own org** | 8 GB, daily backups, no pausing | **Pick if no free slot**, and the upgrade path; $25/month |
| Neon Free | 1 GB | Reject: a scanner that never sleeps uses up the free compute around day 17 each month; no realtime; login rebuilt |
| Prisma Postgres Free | 2 GB | Reject: 200,000 operations a month vs about 475,000 needed; "evaluation only" |
| Nile Free, Aiven Free | 1 GB | Reject: bare databases, no backups or realtime, powered off when idle or not for production; login and access rules rebuilt |
| Turso Free | 5 GB | Reject: not Postgres, no login/RLS/realtime; the daily read budget is exceeded by one count per minute |
| Oracle Always Free (self-hosted Supabase) | about 150 GB | Reject as the only copy: allowance halved in June 2026, idle reclaim, terminations reported; maybe a 1-day pilot later if $25/month ever blocks |
| Self-hosted Supabase on a small VPS | 40-80 GB | Later option; you become the database administrator |
| Firestore, D1, Cosmos, Aurora DSQL, DynamoDB, Render, Koyeb, Railway, Fly, Heroku, CockroachDB, Xata, Tiger, MongoDB, Convex, Appwrite, Back4App, PocketBase | various | Fail: under 1 GB, expire or delete when idle, no free tier left, or a rewrite with no login/RLS/realtime |

**Risks and not verified**
- Real bytes per lead rest on synthetic leads (assumed 45.8 of 74 columns filled, lengths from the bot's code); the pilot import re-measures. The measuring database was PostgreSQL 18, Supabase runs 15 or 17 (expected within a few percent).
- Not verified: whether a free project slot exists in your account; whether a 1-minute scanner counts as activity against the 7-day idle pause; whether `pg_cron` runs every 60 s on Free; how long Supabase's grace period is before a quota breach turns into HTTP 402 for the whole organisation (reports say 2-3 weeks, unpublished); Supabase Free's commercial-use wording (no ban found, not stated officially).
- Pruning is the whole plan: if the trim jobs never run, Free fills in about 7 months instead of 7 years.
- Some sheet columns are not searchable in the app because the mirror is lean (they are read live from the sheet); the UI says so.
- Nightly dumps in the same Supabase account are not true off-site backups; the weekly external copy is mandatory.
