# Who can write what (audit 2026-11-04)

Enforced in Postgres (RLS policies + guard triggers), migrations `20261104000010` and `20261104000011`.
Proof: `npm run check:db` 156 PASS / 0 FAIL (offline); pgTAP on the hosted project 59 ran / 0 failed (rolled back).

## Tables

| Table | Employee could write before | Employee can write now |
|---|---|---|
| profiles | own name, avatar | nothing (only the server clears forced_password_change after a password change) |
| profiles.role / is_active / job_title | no | no. Admin only; the last active admin can't be demoted or deactivated (also blocks server code) |
| active_sessions | own row | own row (needed for one-session-per-account) |
| tasks: insert | yes (own tasks) | **no** |
| tasks: update | creator: everything; assignee: status, progress, notes, time taken, image | **assignee: status only** |
| tasks: delete | creator | **no** |
| task_assignees: add/remove | task creator | **no** |
| task_watchers: add/remove | self, task creator | **no** |
| projects, statuses, priorities | no | no |
| workday_settings, duty_overrides, workspace_settings | no | no |
| time_entries: clock in/out | insert/stop own, any time, many per day | **clock in/out only (RPC or direct), once a day, inside the duty window** |
| time_entries: task timers | start/stop own | **no** |
| time_entries: corrections, delete | no | no (admin; corrections are flagged and audited) |
| hourly_reports / daily_reports: create, edit draft, submit | yes | yes (own only; locked once submitted) |
| hourly_reports / daily_reports: delete | own drafts | **no** |
| report_comments: add | on own daily reports | on own daily reports |
| report_comments: edit, delete | own comments | **no** |
| notifications: create | no | no |
| notifications: update | own rows, any column | **own rows, read_at only** |
| notifications: delete | own rows | **no** |
| documents (vault) | no | no |
| audit_log | no | no |

## RPCs (functions an employee can call)

| Function | Runs as | Employee result |
|---|---|---|
| claim_session() | definer | claims own session (single-session rule) |
| clock_in(), clock_out() | invoker | same rules as the table: once a day, inside the window |
| clock_status() | invoker | reads own status only |
| list_team() | definer | read-only team directory (id, name, email, role, job title) |
| get_document_secret(id) | definer | refused unless the admin turned on vault_visible_to_all |
| set_document_secret(id, value) | definer | refused (admin check) |
| cleanup_old_data(months, types) | definer | refused (admin check) |
| private.* helpers and triggers | definer | not callable directly to change data |

Admin Edge Function `admin-users` (create, deactivate, set_role, send_reset): verifies the caller's JWT and `profiles.role = 'admin'` before using the service role.

## Decision taken by default (say if you want it changed)
- Employees can no longer start task timers; only the clock counts their time. Reversible in one policy.
- Employees can no longer edit their own name; the admin does it.
