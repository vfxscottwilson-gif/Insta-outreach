# Engine: 0004 interfaces (employees + tracking), 2026-11-04

Migration `supabase/migrations/0004_employees_tracking.sql` (commit aa343d5), Edge Function `supabase/functions/gmail-connect/` (b74a88c). Spec: `app/docs/SPEC-EMPLOYEES-TRACKING.md`.

## Ownership
| Path | Owner |
|---|---|
| `engine/src/outreach/mailbox/` | email-mailbox |
| `engine/src/outreach/scheduler.py`, `planner.py`, `capacity.py` | email-planner |
| `gmail.py`, `mail.py`, `sender.py`, `accounts.py`, `importer.py`, `supabase/` | Engine (ask for schema or Gmail client changes) |

## Gmail read interface (`outreach.mail.MailboxReader`, implemented by `outreach.gmail.Gmail`, `gmail.connect(conn, account_id)`)
| Method | Returns |
|---|---|
| `profile()` | `{"email", "history_id", "messages_total"}` |
| `history_list(start_history_id, *, history_types=("messageAdded",), label_id=None)` | `(records, latest_history_id)`, all pages. Stored id too old: `MailError("history_expired", 404)` -> full re-sync + alert |
| `get_message(gmail_id, fmt="metadata", headers=READ_HEADERS)` | Gmail message resource; fmt minimal / metadata / full; 404 -> `MailError("not_found")` |
| `list_messages(q, *, max_results=500, include_spam_trash=False)` | `[{"id", "threadId"}]`, all pages (max_results = page size) |
| `get_thread(thread_id, fmt="metadata")` | Gmail thread resource |
Reads retry rate_limit / unknown 3 times (1, 2, 4 s). `MailError.kind` meanings are in `mail.py`. No write methods: tracking accounts stay read-only.

## Database facts for writers
- `mail_events`: UNIQUE(account_id, gmail_message_id). `direction` must fit `kind` (CHECK). `snippet` only on reply / unsubscribe. `owner_user_id` = account owner AT EVENT TIME: copy it from `accounts` when inserting.
- Bot sends write their own `mail_events` row by trigger when a send becomes `sent` (source automation). If the sync saw the message first, the trigger upgrades that row. Sync should `on conflict do nothing`.
- Do NOT write `contacts`: a trigger fills it from outbound `mail_events` and raises the `double_contact` alert.
- `engine.contact_block(lead_id)` -> null | 'recently_contacted' | 'domain_contacted'. Claim skips and the guard refuses touch 1 on either; follow-ups are never blocked. Planner should use it to avoid planning such leads.
- Tracking accounts: `claim_for_account` returns nothing, a direct insert into `sends` raises. Filter `mode = 'automation'` in anything that plans sends. Effective caps are only written for automation accounts.
- `v_account_*`, `v_overview` now read `mail_events`: `replies` = human replies (reply + unsubscribe, not auto-replies), `responses` = classified interested.
- `engine.snapshot_month(date)`: freezes a month; a second call records late changes in `late_adjustments`. Not scheduled yet (run on the 1st in REPORT_TZ: reports workstream).
- `export_requests` (status pending -> done/failed): worker for "Send to Google Sheet" not built yet; it must filter by `requested_by`'s own accounts unless they are admin.

## Web app (email-design)
- Connect button: `POST {SUPABASE_URL}/functions/v1/gmail-connect/start` with the user's JWT, body `{email, display_name?}` -> `{url}`; open it in the system browser. 400 = readable sentence to show.
- Supabase rewrites `text/html` from functions to `text/plain` on `*.supabase.co`, so set `CONNECT_RESULT_URL` to an app page (e.g. `/connected`): the callback redirects there with `?status=ok` or `?status=error&reason=<sentence>`. That page is needed.
- New mailboxes start in `tracking` mode, owner = the employee (admin connects: admin pool). Admin switches mode / owner by updating `accounts.mode` / `owner_user_id`.
- Employees may update only status (active <-> paused), pause_until, pause_reason, display_name, token_revoke_requested_at on their own accounts; anything else raises.
- Views: `v_employee_stats` (cards), `v_employee_daily`, `v_deliverability`, RPC `deliverability_report(p_from, p_to, p_by)` (account | employee | all), `v_oauth_users` (used / cap / warn_at, admin only makes sense), `monthly_snapshots`. `v_account_stats` adds mode, owner_user_id, owner_name, provider, safe_max, over_safe_band, interested_7d, auto_replies_7d, last_sync_at.
- Exports: after each CSV / Excel call `rpc('log_export', {p_kind, p_format, p_filters, p_rows})`. Google Sheet: insert `export_requests (kind, filters)`.
- RLS now scopes everything: an employee querying `v_overview` gets their own numbers; ops tables (sources, suppression, contacts, run_log, daily_report, ai_usage, capacity_forecast, audit_log) return nothing for them.

## 0005 task reports (web app)
Tables `task_reports`, `report_tasks`, view `v_task_report_status`: see docs/SCHEMA.md "0005". Task status values: todo, in_progress, done, blocked. Approve/reject: plain update of `status` + `decision_note` (bulk with `id in (...)`); never send `decided_by` / `decided_at`. An employee update on a frozen report affects 0 rows (no error), so check the row count. Assigned tasks start with `report_id` null: list `assignee_user_id = me and (report_id = today's report or report_id is null)` and set `report_id` when they go into a report. A new tracking account and a new migration file must grant explicitly: default privileges are closed since 0005.
