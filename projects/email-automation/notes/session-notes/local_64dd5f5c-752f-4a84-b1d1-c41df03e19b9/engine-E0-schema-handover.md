# Engine E0: schema contract hand-over (2026-11-03)

Contract: `F:\Github Repos\projects\email-automation\app\supabase\migrations\0001_init.sql` (commit 94736c4), summary `app\docs\SCHEMA.md`. Read SCHEMA.md first; it is one page.

## For the Design / web binding session
- Read `v_overview`, `v_account_stats`, `v_account_daily|weekly|monthly`, `v_funnel`, `v_reply_rate`, `v_outreach`, `v_queue`, `v_lead_supply`, plus tables `alerts`, `replies`, `accounts`, `settings`, `templates`, `signatures`, `sources`, `suppression`, `audit_log` (admin).
- Writes are column-limited (see SCHEMA.md "App can write"). Caps: write `accounts.daily_cap` as typed; the engine clamps, DB hard ceiling 70/650 regardless. Pause = `status='paused'` or `pause_until`. Kill switch = settings `PAUSE_ALL` value `true` (DB refuses every new send while on).
- Login: after `signInWithPassword` call `rpc('claim_session', {p_user_agent})`; poll/subscribe `rpc('session_status')` -> `replaced` means sign out. Realtime on `active_sessions`, `alerts`, `replies`, `sends`, `accounts`, `run_log`.
- Revert: `rpc('revert_audit', {p_audit_id})` (admin).
- Times: all UTC `timestamptz`; lead-local display uses `leads.tz` / `v_outreach.tz`. "Today" = setting `REPORT_TZ` (default Asia/Karachi).
- Creating employees needs the Supabase Auth admin API (service key) -> an Edge Function, not the browser. Profile row is created by trigger; role comes from `app_metadata.role`.

## For the AI-layer session (WS2)
- Write drafts into `drafts` (UNIQUE lead_id+touch_no): `subject`, `body` (no greeting/sign-off/signature), `generated_by` ai|ai_light|template, `provider`, `model`, `tokens_in/out`, `rules_version`, `input_hash`, `variant`, `season_until`. Status `draft`; the planner flips to `ready` with `send_at`.
- Per-day provider usage + daily-quota disable: `ai_usage(day, provider, model)` with `disabled_until`, `last_status`.
- Templates: `templates(kind, variant, body)`; signature: `signatures` (account_id null = default). Lead data for prompts: use an explicit allowlist of `leads` columns; never `extra_data` (holds subscribers/score).
- Follow-up subjects: the claim writes `Re: <touch 1 subject>` itself; draft subject for touch 2-5 is ignored unless `new_thread`.

## Facts checked
- Supabase now requires explicit GRANTs for the Data API (default for new projects since 2026-05-30, enforced 2026-10-30). The migration grants explicitly; anon gets nothing.
- JWT carries `session_id`. Triggers on `auth.users` and FKs to it are still allowed after the 2025-04-21 auth-schema lockdown.
- Not verified: Supabase CLI accepting the `0001_` filename prefix (rename to a timestamp prefix if `db push` refuses; content unchanged); whether Gmail API keeps our pre-set Message-ID (schema stores both ours and the delivered one, so either way works).
