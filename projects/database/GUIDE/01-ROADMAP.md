# 01 Roadmap

| Stage | Status |
|---|---|
| Flask + SQLite app: sync engine, login (one session, reset code), admin users, dashboard, leads/assign, sources in DB, approvals, trash, audit, vault | Built; tests pass except 1 stale test (see PACKAGING-STATUS.md) |
| Live Google test with the user's service account and real sheet links | NOT DONE (needs Q1: sheet URLs + service account) |
| Gmail reset codes | NOT DONE (needs Q6: Gmail app password); console fallback works |
| Wave B2: per-sheet access, standing assign rules, employee dashboard | See `docs\HANDOFF-GAPS.md` section 1 |
| Wave B3: scanner hardening; B4: metrics (week, states, time zones, quality/10) | See `docs\HANDOFF-GAPS.md` |
| Browser QA, security review | Pending |
| Optional design preview `app\web` (mock data) | Reference only |

Full gap list and decisions: `docs\HANDOFF-GAPS.md`. Original brief: `notes\BRIEF.md`.
