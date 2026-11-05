# Two builds of the same dashboard (found 2026-11-04)

The user asked for a lead dashboard in two chats. Each chat planned and built on its own and neither could see the other (this chat's recon listed `D:\All Automations Records` before the second folder existed).

| | A: **Lead Dashboard** | B: **Database** (this control room) |
|---|---|---|
| Chats | "Build: Lead-gen dashboard & database" (started by "Local AI cold-email draft generator", folder group "All Automations Records"), idle | "Database app: Control room" + "Database UI: clickable preview", idle/running here |
| Folder | `D:\All Automations Records\Lead Dashboard` | `F:\Github Repos\projects\database` |
| Stack | Python Flask + SQLite + gspread, runs on your PC | React/TypeScript + Supabase (Postgres, Auth, Realtime), hosted, installable on phone |
| State | Working locally: about 2,640 lines of code + 2,800 lines of tests, 275 tests pass, 8 commits plus uncommitted work (sheet/tab lifecycle, inventory). About 70%. | Brief v3 + red-team + storage measured. Preview scaffold committed (4 commits), screens not finished, no backend. About 25%. |
| Purpose | Dashboard + database over the lead sheets: counts per day/month, by country/niche/source/status, clients vs leads, duplicates, assigning leads. "Not an email tool." | Same, plus per-sheet access, Approvals folder, time zones, quality score, reached, daily reports, notifications, employee dashboards |
| Who sees what | Admin = you; employees see only their own assigned leads | Owner + 1 admin; employees get per-sheet access (Hidden / View / Contribute) and their own dashboard |
| Sheets | Read **and write-back ON** (assign and status into agreed columns; switch `DASH_WRITEBACK=off`) | Read-only (red-team: writing into the bots' sheets can shift their append position and corrupt dedupe) |
| Removing data | A tab that vanishes is marked "Removed from sheet"; admin confirms Yes/No | Employee request -> Approvals -> either admin -> Trash -> purge |
| Login | Its own: one session, reset code, admin users (61 tests) | Supabase Auth copied from the CRM |
| Theme | Black/white request; its own design spec says both apps are purple on grey and offers a mono option | Purple family like CRM and Outreach |
| Where it lives | Your PC first | Cloudflare Pages + Supabase (new Gmail account) |
| Waiting on you | Sheet URLs, Gmail for reset codes | Sheet URLs, Gmail for reset codes, Google service account |

## Risks of running both
1. Both would read the same sheets with the same Google quota (60 reads/min per service account): live scans of two apps starve each other and the lead bots.
2. Two rule sets (write-back vs read-only, theme, who sees what) give two answers.
3. Twice the cost and time, and both ask you for the same inputs.

## Recommendation
Database (B) is the main product: it matches your latest requirements (hosted, same infrastructure as the CRM and Outreach, employee dashboards, Approvals folder, per-sheet access, time zones). Freeze A at a safe commit (keep it, do not delete it) as a local fallback and a tested reference. Reuse from A: adapters, sheet/tab lifecycle, contact extraction and its 275 tests as acceptance tests for the scanner; the inventory panel (sheets, tabs, niches, leads, emails, phones, social handles) for the Sheets screen; `categories.yaml` idea for niche mapping; add/disconnect whole sheets from the app.
Write-back: Database starts read-only; an optional write-back limited to agreed columns can be added after the pilot proves the bots' append logic is not disturbed.
