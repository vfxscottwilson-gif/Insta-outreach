# UI-PUNCHLIST.md: Database dashboard (Level Up VFX)

Date: 2026-11-05. Decision-maker: Fable (senior product designer). Sources: functional + numbers audit (165 controls, 44 metrics) and design/motion/chart audit. Code proposals: `F:\Github Repos\projects\database\docs\ui-audit\` (chart-smoothing.py, charts-smooth.css, charts-smooth.js, charts-smooth.test.js, chart-preview.html, chart-preview-dark.png, chart-preview-light.png). App: `F:\Github Repos\projects\database\app\dashboard\dash\`.

User's words this round: purposeful, minimal, professional, glanceable, smooth curves, rounded edges, alive motion, everything functional, show the preview.

Effort: S = under 1 h, M = half day, L = a day or more.

## Decisions on conflicts between the two audits
| Topic | Functional audit | Design audit | Decision |
|---|---|---|---|
| Waiting / Clients tiles | Make them links | Remove, fold into needs-you strip and funnel | Remove the tiles; the remaining five tiles are links; "Not yet contacted" lives in the needs-you strip (P2) and as the REACHED tile note until then |
| Chart keyboard focus | Roving tabindex (first mark 0, arrows) | Every mark tabindex 0 (charts-smooth.js assumes it) | Roving tabindex; adjust charts-smooth.js (P2) |
| Count-up | Start at 85 %, 600 ms | Tween from shown value, 700 ms | Server renders the final number; JS tweens from 85 % to final in 700 ms; reduced motion writes final at once |
| Leads row actions | CSS nowrap now | Row drawer | Both: nowrap in P1, drawer in P2 |
| Chart summaries (1,260 / 712) | Add `summary` arg | New smooth_* functions | Pass explicit summary strings when swapping to smooth_* |
| Hero card | Keep, fix count-up | Delete with beam | Delete; total becomes title text |

## Verified by me before deciding (source read 2026-11-05)
list.html loads only leads.js (L91); approvals.html data-confirm on the shared form (L23); stats.py last_week is the whole previous week (L68); approvals_pending only in approvals.py (L78), no template; charts.py _summary() sums every series; leads.py abort(403) at L283; charts.py every non-zero mark tabindex 0 (L22). Everything else is taken from the two reports.

## P1: one build round (real mistakes, then charts, then layout, then motion)
| # | Area | Change | File(s) | Effort |
|---|---|---|---|---|
| 1 | Leads list: dead confirm | Load admin.js after leads.js so Trash / Request removal ask first (admins get no dialog today) | dash/templates/leads/list.html L91 | S |
| 2 | Approvals: Reject asks "Approve?" | data-confirm moves to the Approve button; admin.js reads `e.submitter.dataset.confirm` | dash/templates/admin/approvals.html L23-27, dash/static/admin.js | S |
| 3 | KPI This week: false red | Add `last_wtd` (Mon..same weekday last week) in kpis(); `week_delta=_pct(k['week'], k['last_wtd'])`; note "39 same days last week"; fix tests if needed | dash/stats.py L60-73, dash/dashboard.py L88, dashboard/index.html L31, tests/test_stats.py | S |
| 4 | Bare 400/403/404 pages | errorhandlers render error.html (extends base.html, message + back link); bulk_status / assign flash + redirect on blank input; set_status employee-DNC case flash + `_back()` instead of abort(403); `required` on assign count | dash/__init__.py, dash/leads.py L280-283 + bulk_status/assign, leads/list.html, new templates/error.html | M |
| 5 | Charts: corners, wrong width, wrong summaries, halo dots | Copy smooth_* from docs/ui-audit/chart-smoothing.py into charts.py (keep mini_bar rx 4, delete stacked_bars); w per span 278/448/614/950; explicit `summary` for funnel ("742 leads; 28 became clients") and clients; charts-smooth.css after app.css; charts-smooth.js from base.html; drop per-template charts.js tags | dash/charts.py, dash/dashboard.py L88-101, templates/base.html L10, dashboard/index.html L97, countries/index.html L24, countries/detail.html L33 | M |
| 6 | Minimal dashboard layout | Delete hero card + beam, Last month / Clients / Waiting tiles, By source, Clients over time, More breakdowns, bottom Last synced, niche donut, Team workload (and their queries). Five linked tiles TODAY (sparkline) / THIS WEEK / THIS MONTH (note "last month 297") / REACHED / QUALITY ring; Leads per day (30/60 d, 7-day average) + Month pace row; Automations table; below: By country rank bars linking to /countries/<code>, By niche rank bars top 6 + Other, Status funnel with conversion % and steps linking to /leads?status= | dashboard/index.html, dash/dashboard.py, dash/stats.py overview(), app.css L344-352 | L |
| 7 | Ambiguous numbers | "Not yet contacted" includes Drafted; "N of them unassigned" from new `waiting_unassigned` (assignee IS NULL within the waiting set); funnel stage "Contacted or further"; REACHED note "plus 351 marked contacted in the sheets" | dash/stats.py kpis(), dashboard/index.html L35-37 | S |
| 8 | Approvals count invisible | Nav badge `{{ approvals_pending }}` on the Approvals item (.navcount in charts-smooth.css) | templates/base.html L60-62 | S |
| 9 | Numbers wrong for 1 s | Server renders the final value; tween from 85 % over 700 ms; data-decimals/suffix; reduced motion writes final at once | charts-smooth.js countUp, templates using data-count | S |
| 10 | /api/pulse 500 | `since = int(since) if since.isascii() and since.isdigit() and len(since) < 16 else 0` | dash/dashboard.py pulse() | S |
| 11 | Leads / Team rows 181 px, 1908 px wide | `.actions{display:flex;gap:6px;flex-wrap:nowrap}` + reason input 120 px; Status/Assignee/Actions after Company; hide Niche/Segment/Added under 1440 px; Team drops all-zero status columns | dash/static/app.css L114, leads/list.html L59-87, leads/team.html L7-11, leads/_actions.html | M |

P1 proof: screenshots of / at 1280 and 375 (dark + light) taken 1.5 s after load, pytest green, list of anything not verified.

## P2: next round (glanceable additions, employee home, drill-down, motion polish)
| # | Area | Change | File(s) | Effort |
|---|---|---|---|---|
| 12 | Dashboard health strip | Live dot, "Synced N s ago", "X of Y sheets healthy, late, lost access", Sync now; from sources.last_ok / last_error / bot_late; replaces both Last synced lines | dash/dashboard.py _page(), dashboard/index.html | M |
| 13 | Needs-you strip | approvals, missing_in_source, unassigned > 24 h, not yet contacted, DNC to-do, unknown-country; each a link | dash/dashboard.py, dashboard/index.html | M |
| 14 | REACHED tile from reach_events | reached this week vs same days last week | dash/stats.py, dashboard.py | S |
| 15 | Employee home /my | 3 tiles (Due/overdue, Open now, Reached this week) + progress ring; "Contact now" list (due today first, then business-hours-now via tzmap); My sheets as chips; leads table with row drawer so rows are one line | leads/mine.html, leads/_actions.html, dash/leads.py, app.css | L |
| 16 | Leads page | 4 primary filters + More filters; bulk bar only when rows ticked; drawer for email/website/source/segment/removal | leads/list.html, leads.js, app.css | M |
| 17 | Keep place after actions | `id="lead-{{id}}"`, next = full_path#lead-id, `tr[data-lead]{scroll-margin-top:72px}` | leads/mine.html, list.html, _actions.html, app.css | S |
| 18 | Drill-down | Duplicates companies link to /leads?q=; Team Sheets/status counts link to filtered lists | leads/duplicates.html, leads/team.html | S |
| 19 | Team page | Person, Sheets, Assigned, % worked bar, Reached this week, Overdue, View; "-" for Unassigned % worked; drop duplicate Clients; sheet x person access matrix | leads/team.html, dash/leads.py | M |
| 20 | Sources & sync | Status chips replace 8 tiles; status + next run per sheet; banner for stale/blocked | admin/sync.html, dash/admin.py | M |
| 21 | Orphan source after disconnect | source_labels() reads sources_archive; inventory() drops the connected-source filter (or restore refuses); Trash pager 50 + Restore all from sheet | dash/dashboard.py, dash/registry.py L134, admin/trash.html | M |
| 22 | Phone 375 | Filters disclosure, health/needs chips, 2-col tiles, chart panels scrollLeft to newest, lead cards 6 fields | dashboard/index.html, charts-smooth.js, app.css | M |
| 23 | Keyboard | Marks tabindex -1, roving focus with arrows; update charts-smooth.js | dash/charts.py _mark, charts-smooth.js | S |
| 24 | Motion polish | rise 280 ms capped stagger; 120-180 ms colour transitions on nav/rows/buttons; press scale on .side a / a.kpi; sliding tab pill; crosshair + gliding tooltip; flash enter + auto-dismiss; bell ring + badge pop; poll always scheduled + visibilitychange | charts-smooth.css/js, app.css L76-79, L144, L210, L324-330, L371-375 | M |
| 25 | Labels | With email / With name / With phone; avg score 6.6/10; "distinct within each country"; "Include leads removed from the sheet"; title on clipped cells and site links; worked definition on /my | dashboard/index.html, countries/index.html, leads/list.html, mine.html, _partials/macros.html | S |
| 26 | Second login | Flash "signed out because this account signed in on another device" before redirect | dash/authz.py require_login() | S |

## P3: later
| # | Area | Change | File(s) | Effort |
|---|---|---|---|---|
| 27 | Niches page | Folder per niche: leads, emails, phones, avg score, this month | new blueprint + template | M |
| 28 | Approvals in place | Background POST, animated row exit, toast, badge update, fallback submit | approvals.html, charts-smooth.js | M |
| 29 | Theme crossfade | document.startViewTransition 280 ms, skip for reduced motion | dash/static/theme.js | S |
| 30 | Lists | Delete values with 0 leads; Leads filter uses renamed labels | dash/lists.py, dash/leads.py vals() | S |
| 31 | Add-a-sheet | Keep Name/link after error; plain message; auto-refresh during sync | dash/admin.py, admin/sync.html | S |
| 32 | Countries | Cards: Leads, Emails, Phones, +N this month; detail lists states once | countries/index.html, detail.html | S |
| 33 | Latest activity | 6 audit rows below the fold | dashboard/index.html, dash/dashboard.py | S |
| 34 | Leads per month | smooth_bar_chart(highlight_last) or drop per_month query | dash/charts.py, stats.py L296 | S |
| 35 | Perf | Live dot pauses on idle/hidden; waitress threads 8 only if login stays slow | charts-smooth.js, dash/serve.py | S |

## Not verified
- The smooth charts were never run inside the Flask app; only python/node self-tests and final-state headless renders (chart-preview-*.png). Draw-in, bar rise, donut sweep, crosshair glide were read, not watched.
- Employee row height cause (141 px) is inferred from CSS and screenshots.
- Health strip / needs-you / reached-this-week assume reach_events, sources.bot_late, approvals and tzmap hold the data; columns were read in code, not queried.
- Not tested in Safari/Firefox; phone rendering of the new charts not rendered; light theme not reviewed page by page.
- Demo DB only (742 leads, 4 sheets); real-volume Trash and 100-row pages inferred.
- Users, Trash, DNC to-do, Settings, Lists, Sheet/Tab detail screens only skimmed.

## Owner decisions (override the rows above)
- **2026-11-05: KEEP the Clients tile** (owner decision). Do NOT remove it. Dashboard keeps six tiles in one row at 1280 (three by two below 1100 px, two columns on phone): TODAY (sparkline) / THIS WEEK / THIS MONTH / CLIENTS / REACHED / QUALITY. CLIENTS shows the number of clients, "x% of all leads" as the note, a small 14-day cumulative sparkline (this replaces the removed "Clients over time" chart), and links to /leads?status=Client. Clients also stay as the last step of the Status funnel.
- Still removed: hero card + beam (the total stays as "742 leads in database" in the title row), Last month tile (its number goes into the THIS MONTH note), Waiting tile (becomes the "Not yet contacted" note and the needs-you strip), By source, More breakdowns, nine-colour niche donut, stacked Team workload, duplicate Last synced.
