# WS3 (scheduler, planner, capacity forecast): interfaces for other sessions, 2026-11-04

Repo `F:\Github Repos\projects\email-automation\app`, `engine/src/outreach/{scheduler,capacity,planner}.py`. Tests: `tests/test_scheduler.py`, `test_capacity.py`, `test_planner_*.py` (helpers: `tests/planner_helpers.py`).

## What runs
Tick phases (registered by `from . import planner` in `__main__.py`, between `send` and `drafts`): `plan` every 15 min (not blocked by the Health Check) and `capacity` every 30 min.
`planner.plan(conn, settings, now)` is the whole run and is idempotent. It never sends, never writes text, never touches `supabase/`.

## Contract with the draft writer (WS2) and the sender (Engine)
- The planner creates `drafts(lead_id, touch_no, account_id, send_at, status='draft', new_thread)` with no subject/body. The writer fills them and flips to `ready`.
- First emails: shells for the next `PLAN_AHEAD_DAYS` (7) days, so a Saturday run already has next Monday-Friday. The lead goes `new -> active` when its shell is created.
- Follow-ups: a shell for touch n+1 appears after touch n is really `sent` (due = lead-local send date + `FOLLOWUP_GAP_BUSINESS_DAYS` business days, lead calendar), on the account that sent touch n. A later send_at is only ever moved by the planner (stale > `MAX_CLAIM_LATENESS_MINUTES`, capacity, account paused). Drafts due within 30 min are left alone.
- Orphans: account `disabled` or `mode='tracking'`: `ORPHAN_FOLLOWUPS=pause` holds the lead (`hold_reason='account_removed'`, alert `plan_orphans`; it resumes by itself when the account is back); `restart_new_thread` moves the shell to another account with `new_thread=true`. Unsent first emails are reassigned.
- Contact registry: before a first email is planned `engine.contact_block(lead)` is called; a blocked lead becomes `held`, `hold_reason='recently_contacted'`, `hold_until` = end of the cool-down (`engine.release_contact_holds()` is called every run).
- TEST_MODE on: only leads whose address is in `TEST_ADDRESSES` are admitted. `DRAIN_MODE`: no first emails.
- Not resurrected: drafts the admin cancelled/skipped. A lead whose reply stopped it is ignored (the DB cancels its drafts).

## Data for the app (WS5 / WS6)
- `capacity_forecast(day, planned_followups, planned_new, capacity, utilization)`: `day` is a **bucket date** = the 24 h from 08:00 UTC that day to 08:00 UTC the next (US day D, Australian day D+1; chosen so US and AU windows never split one rolling 24 h). Rows: the next 20 weekday buckets, plus weekend buckets that have planned work. `planned_followups` includes survival-weighted projections of touches not yet created (`SURVIVAL_RATE`), `planned_new` is real shells + sends so far in the current bucket. `utilization` is in percent, can exceed 100 (that is the honest overload signal).
- Alerts raised (counts only): `plan_no_capacity`, `plan_late` (follow-ups later than `MAX_SLIP_BUSINESS_DAYS`), `plan_dropped` (NEW_FIRST drops, skip_reason `dropped: ...`, lead set `completed`), `plan_orphans`.
- Run counts are in `run_log.counts.plan` (admitted, held_contacted, followups_created/moved/dropped/late/unplaced, first_rescheduled, woken, orphans_paused/resumed).
- Settings added (Planning (WS3) block): `FORECAST_DAYS` 20, `PLAN_AHEAD_DAYS` 7, `SEND_SLOT_ROTATION` off. `country_rules` is seeded (US/CA/AU, 08:30-12:30, weekend 10:00-13:00, second window off) on the first run; edit it in the app.

## Behaviour worth knowing
- BALANCED: new share starts at the 30% target, then settles near 24% (4 follow-ups, survival 0.9); simulation in `test_planner_quota.py` shows peak load 100%, follow-ups under 80%. NEW_FIRST: 30-35% new, the rest slips or is dropped past the slip limit.
- Accounts are chosen by remaining room relative to their own effective cap, with a per-account hourly maximum (`MAX_PER_HOUR_*`) respected when spreading `send_at`.
- Windows are lead-local from `country_rules`; a lead with `tz_uncertain` is planned in its majority zone (not narrowed).
- An account that cannot send for a while (token lost, paused) keeps its follow-ups: they slip day by day on that account (BALANCED) or are dropped past the slip limit (NEW_FIRST). Reconnect quickly in NEW_FIRST mode.
- TEST_MODE pilot: `tools/pilot` drafts due now are left alone; one that sits unsent for more than `MAX_CLAIM_LATENESS_MINUTES` is re-timed like any stale draft (a pilot follow-up goes to +5 business days).
- Timing on a loaded dev PC: a plan run with 1,500 leads in sequence and 4,000 waiting takes about 4 s, 1 s when nothing changes.
- Not supported: per-account `window_override` (format undefined), tz-uncertain window narrowing.
