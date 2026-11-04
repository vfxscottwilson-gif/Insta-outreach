# WS4 (mailbox sync, classification, replies, labels, snapshots, exports): interfaces for other sessions, 2026-11-04

Repo `F:\Github Repos\projects\email-automation\app`, package `engine/src/outreach/mailbox/`. Run: `cd engine`, `uv run pytest tests/test_mailbox_*.py -q` (DB tests are slow on a busy machine: ~5 s each).
Registered by ONE line in `__main__.py`: `from .mailbox import phase as _mailbox`.

## Tick phases (mailbox/phase.py)
| Phase | Cadence | What |
|---|---|---|
| `mailbox` | every tick | syncs accounts whose `sync_state.last_sync_at` is older than `MAILBOX_SYNC_MINUTES` (40 s budget per tick), then labels human replies with the AI (batches of 20), then manual over-sending alerts |
| `mailbox_exports` | every tick | pending `export_requests` -> new tab in `EXPORT_SHEET_ID`, scoped by requester role, `audit_log` row (action `export`) |
| `mailbox_snapshots` | 6 h | `engine.snapshot_month` for the last 3 finished months (REPORT_TZ): freeze, then `late_adjustments` |
| `mailbox_mirror` | ~23 h | `SHEETS_MIRROR` on: rewrites tabs "Mirror: deliverability this month" and "Mirror: accounts" |

## What it writes
- `mail_events`: one row per outreach message (owner at event time, `source` automation|manual, `snippet` <= 300 chars only for human replies and unsubscribes, never a manual mail's body). A DSN found in its own Gmail thread is stored with the ORIGINAL message's `thread_id` (so `v_account_stats` bounce attribution works).
- Consequences of an inbound message: lead stopped (`stop_reason` response / not_interested / unsubscribed / auto_reply / bounced / wrong_person / manual; reply "2" = snoozed 30 days), `suppression` (unsub, not_interested, wrong_person, hard bounce, 4.2.2), a `replies` row (every inbound outcome, both modes; a human reply starts as type `response` and the AI may refine it; `classified_by` rules|ai). `RESUME_AFTER_OOO` keeps the sequence going after an out-of-office.
- `contacts` + the `double_contact` alert come from the 0004 trigger on `mail_events` (not Python).
- `label_map` + Gmail labels, automation accounts only (tracking accounts get a `ReadOnly` client: no send/label/archive/revoke).
- `sync_state` (history_id, last_sync_at, backfilled_until = backfill cursor, last_full_sync_at, last_error).

## Alerts raised (no addresses or text in messages)
`mailbox_resync` (warning: history expired, window re-read), `token:<id>` (critical: Gmail auth lost; same key as accounts.py), `mailbox:<id>` (warning: 403), `manual_oversend` (warning > safe band 60/600, critical >= ceiling), `manual_bounce` (warning > 3% over >= 20 sends), `label_created` / `label_choice` (info).

## Settings added (Mailbox (WS4) block)
`TRACKING_BACKFILL_DAYS` 30, `MAILBOX_SYNC_MINUTES` 10, `EXPORT_SHEET_ID`, `SHEETS_MIRROR`. Existing: `RESPONSE_KEEP_IN_INBOX`, `RESUME_AFTER_OOO`, `REPORT_TZ`.

## Export kinds (`export_requests.kind`, `filters` jsonb)
`deliverability` {from, to, by: account|employee|all}, `monthly` {period}, `accounts`, `events` {from, to}. Employees get only rows whose `owner_user_id` is theirs (the worker bypasses RLS, so the scoping is in SQL).

## Needs from others / not verified
- Needs `GOOGLE_SA_JSON` with Sheets write access (the Engine's reader uses the read-only scope; `GoogleSheetsWriter` asks for the full scope) and the sheet shared with that service account as editor.
- Never run against a real mailbox: Gmail shapes are from fixtures (DSN `message/delivery-status` sub-part headers as the Gmail API returns them) - verify with the first connected account.
- Labels: fuzzy threshold 0.8 (prompt says 0.75) because "Internal Emails" scores 0.74 against "Invalid Emails".
