# 01 Roadmap: done, left, order

Source of truth: `app\PROGRESS.md` and `app\docs\ROADMAP.md` (phases A-G, details and effort). Snapshot 2026-11-05.

## Done
| Area | State |
|---|---|
| Database (Supabase `haroonvfx-outreach`) | Migrations 0001-0017 live, 33 tables + 16 views, RLS on all, owner login works |
| Engine | Import, dedupe, caps 70/650, ramp, planner, sender, mailbox sync, AI layer, task reports, sheet backup. 1349 tests pass, 1 skipped. Not run against a real mailbox |
| Web app | All screens, roles, Team, reports, exports, sign-in lock, phone layout. Live on Cloudflare (sample data) |
| Edge functions | `gmail-connect`, `admin-users`, `sign-in` written + tested, **not deployed** |
| Packaging | This folder, installer, backup script, guides |

## Left, in order
| # | Step | Who | Blocker |
|---|---|---|---|
| 1 | `SUPABASE_ACCESS_TOKEN` in `.env`; deploy 3 edge functions; enable the access-token hook | You + Engine | Token |
| 2 | Wire web to Supabase (`web/.env.local` publishable key), remove demo login | Design session | 1 |
| 3 | Google Cloud OAuth clients (Desktop + Web), consent screen In production | You | - |
| 4 | One AI key (Gemini or Groq) in `.env`; `python -m outreach.ai smoke` | You | - |
| 5 | Postal address + opt-out line + TEST_ADDRESSES | You | - |
| 6 | Connect 2 Gmail accounts; worker on this PC with DRY_RUN | You + Engine | 3, 5 |
| 7 | TEST_MODE pilot to your own address, then real leads (ramp from 40/day) | You approve | 6 |
| 8 | Employee accounts connect (tracking mode) | Employees | 2 |
| 9 | Notifications (Telegram + web push), daily report | WS6 | 7 |
| 10 | 24/7 worker host (Google Cloud e2-micro or Hetzner), nightly backup to Drive | You (account) | 7 |
| 11 | Hardening: RedTeam + security review | WS7 | 8 |

## Open owner-side items
- Real-phone check of the iPhone tab bar (`app\web\KNOWN-ISSUES.md`).
- `GOOGLE_SA_JSON` in `app\.env` pointed to a file that does not exist (`sheets-reader.json` vs real `sheet-reader.json`); `install.ps1` repairs it.
