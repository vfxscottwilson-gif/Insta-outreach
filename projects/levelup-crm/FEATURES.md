# ClickUp paid features → LevelUp CRM build map

Checked 2026-11-03 (Sonnet research). Sources: clickup.com/pricing (official; only a summary was readable) plus 7 third-party pricing pages. Plan tiers marked NV in the research weren't verified against ClickUp's live compare table. This matters little here, because we build **all** of them.

ClickUp price for reference (official page, 2026-11-03, billed yearly): Core $9, Business $17, MAX $100 per user/month, Enterprise custom. ClickUp is running a pricing split test, so this is not final.

Legend: **Cost**: 🟢 free (open source / built in) · 🟡 free tier, paid at scale · 🔴 needs a paid service or contract. **Decide** = needs your answer (see the bottom of this file).

## Phase 1: Shell, hierarchy, core tasks (U1-U5, in progress)

| Feature | How | Cost |
|---|---|---|
| Unlimited Spaces / Folders / Lists, hierarchy templates | Supabase tables + sidebar tree | 🟢 |
| Custom statuses per List/Space | `statuses` per list | 🟢 |
| Multiple assignees, watchers, subtasks, nested subtasks | already in the schema (assignees/watchers); add `parent_id` | 🟢 |
| Custom task types (bug, milestone…), Milestones | `task_types` table | 🟢 |
| Tags, checklists, task templates, bulk edit | tables + multi-select bar | 🟢 |
| List, Board, Calendar views; task side panel; Ctrl+K | dnd-kit, FullCalendar (MIT), cmdk | 🟢 |
| Unlimited storage for attachments | Supabase Storage (1 GB free, 100 GB on Pro) | 🟡 |

## Phase 2: Views, fields, time, agile

| Feature | How | Cost |
|---|---|---|
| Table view | TanStack Table | 🟢 |
| Gantt + dependencies, Timeline | SVAR/Frappe Gantt (MIT) or custom SVG | 🟢 |
| Workload view, capacity, time off, resource management | per-user capacity + time-off table | 🟢 |
| Mind Map view | React Flow (MIT) | 🟢 |
| Map view | Leaflet + OpenStreetMap tiles | 🟢 (OSM fair-use) |
| Activity view | from `audit_log` | 🟢 |
| Embed view | iframe view | 🟢 |
| Private views, protected (locked) views, saved views | `views` table + RLS | 🟢 |
| Custom Fields: text, number, dropdown, date, people, money, rating, progress, **formula**, **rollup**, location, files | JSONB + typed definitions; formulas evaluated client- and server-side | 🟢 |
| Recurring tasks | scheduled job (pg_cron in Supabase) | 🟢 |
| Time tracking, estimates, **Timesheets**, billable time, labels | `time_entries` (exists) + timesheet grid | 🟢 |
| Time in Status reports | status-change history table | 🟢 |
| Sprints, story points, sprint rollover, burndown, velocity | sprint tables + charts | 🟢 |

## Phase 3: Docs, collaboration, reporting, automation

| Feature | How | Cost |
|---|---|---|
| Docs + Wikis, verified wikis, private docs, doc permissions, embeds | Tiptap (MIT core) + RLS | 🟢 |
| Whiteboards (unlimited) | Excalidraw (MIT). Not tldraw, which needs a paid licence | 🟢 |
| Chat: channels, DMs, full history, threads, @mentions | Supabase Realtime | 🟢 |
| Inbox, Replies, Assigned Comments | notifications table | 🟢 |
| Clips (screen recordings) | browser MediaRecorder + Storage | 🟡 storage |
| Calendar meeting scheduling | own calendar; Google Calendar sync = later | 🟢 |
| SyncUps (video/audio calls) | Jitsi Meet embed (free) or LiveKit (free tier) | 🟡 **Decide** |
| Dashboards: advanced cards, unlimited cards, custom reports, team time reports, sprint cards | Recharts | 🟢 |
| Goals, goal folders, auto progress | goals + key results linked to tasks | 🟢 |
| Portfolios, project health (red/amber/green), rollups | portfolio views over Lists | 🟢 |
| Automations (unlimited actions), templates | rules engine in Postgres triggers + Edge Functions | 🟢 (Edge Functions: 500K/month free) |
| Automation webhooks / integrations | outbound webhooks | 🟢 |
| Forms: unlimited, conditional logic, auto-assign, public submission | form builder + public route | 🟢 |
| Email in tasks (send) | Resend | 🟡 3,000/month free |
| Email in tasks (receive) | inbound email address | 🔴 **Decide** (paid Resend/Postmark inbound) |

## Phase 4: Polish, tests, deploy (as in the roadmap)

## Phase 5: Admin, permissions, security

| Feature | How | Cost |
|---|---|---|
| Teams (user groups), unlimited | `teams` + membership | 🟢 |
| Custom roles, granular permissions (incl. time tracking) | roles/permissions tables in RLS | 🟢 |
| Guests + guest permissions, private Spaces/Folders/Lists, sharing controls | `guest` role + per-item shares | 🟢 |
| Audit logs | done (trigger-written `audit_log`) + admin page | 🟢 |
| Session management | done (one session per account) + admin "sign out user" | 🟢 |
| 2FA (authenticator app) | Supabase MFA (TOTP) | 🟢 |
| SMS 2FA | Supabase phone MFA + Twilio | 🔴 per SMS |
| Google SSO / Microsoft | Supabase OAuth providers (free). **Conflicts with your "email + password only" rule** | 🟢 **Decide** |
| SAML SSO (Okta, Azure AD) | Supabase SAML is a paid add-on on Pro+ | 🔴 **Decide** |
| SCIM provisioning | not offered by Supabase; custom endpoint | 🟡 build later if needed |
| IP allowlist | Vercel Firewall (paid) or check in Edge Function | 🟡 |
| Data residency | pick the region when creating the Supabase project | 🟢 |
| Workspace backups | Supabase Pro daily backups, plus a CSV/JSON export job | 🟡 |
| White labelling | already your own brand; add brand settings page | 🟢 |
| HIPAA + BAA, MSA | legal contracts (Supabase HIPAA add-on, Team plan), not code | 🔴 skip unless needed |

## Phase 6: AI, integrations, apps

| Feature | How | Cost |
|---|---|---|
| AI assistant (ask, summarise, write) in tasks/docs/chat | Claude API via Edge Function | 🔴 **Decide** (pay per use) |
| AI fields, AI dashboard cards, AI automations, autopilot agents | same API | 🔴 |
| AI Notetaker (meeting transcripts/summaries) | transcription (Whisper locally = free but slow; or a paid API) + Claude summary | 🔴 |
| Talk-to-text | browser Web Speech API | 🟢 |
| Image generation | needs an image API | 🔴 skip unless asked |
| Connected search, MCP connections | own MCP server over the Supabase API | 🟢 later |
| Public REST API (rate limits), API keys | Supabase auto API + per-user API keys | 🟢 |
| Google Drive / Dropbox / Box attachments | their free picker APIs | 🟢 |
| Zapier, Make, Slack, GitHub | via webhooks + Slack/GitHub apps | 🟢 |
| Mobile + desktop apps, offline | installable PWA (one codebase) + offline cache. Native store apps = later | 🟢 |
| Import (CSV, ClickUp/Trello/Asana CSV), Export (CSV, JSON) | import wizard + exports | 🟢 |

## Not copied
ClickUp's name, logo, illustrations and "Brain" branding. ClickUp Assist (human expert hours) and Certified Agents (a service, not software).

## Decisions needed
1. **AI**: OK to use a Claude API key (pay per use, roughly cents per request) for the AI features? Yes / later.
2. **Sign-in**: keep **email + password only** (your standard), or also allow Google/Microsoft sign-in? SAML SSO costs extra on Supabase.
3. **Video calls**: Jitsi embed (free, Jitsi-branded) / LiveKit (free tier, own UI) / skip.
4. **Receive email into tasks**: needs a paid inbound email service. Yes / skip.
5. **SMS 2FA** (per-SMS cost) and **HIPAA** (contracts): skip unless needed?
