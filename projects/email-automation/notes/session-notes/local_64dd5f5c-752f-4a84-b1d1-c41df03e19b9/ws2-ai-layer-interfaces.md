# WS2 (AI layer, composer, validator, templates, drafts): interfaces for other sessions, 2026-11-04

Repo `F:\Github Repos\projects\email-automation\app`, package `engine/src/outreach/`. Run: `cd engine`, `uv run pytest -q`.

## For E3 / sender
`outreach.compose.render(settings, lead, account, draft, signature=None, *, now=None) -> compose.Rendered(subject, text, html)`.
`signature` = the signatures row you already pass (account row or default). `accounts.signature_override` is merged on top.
`render` does not change the subject. Never send `draft["body"]` directly: it may hold `[[s]]..[[/s]]` (a seasonal sentence that
render keeps or drops by `draft.season_until`). Follow-up drafts carry `Re: <touch 1 subject>` (or "Following up"); you replace it at claim.

## For WS3 (planner): the draft shell contract
Create `drafts(lead_id, touch_no, account_id, send_at, status='draft')` with `subject`/`body` null. The `drafts` phase (every tick,
after the send phase) fills text, sets `status='ready'` when `send_at` is set, and records generated_by (ai | ai_light | template),
provider, model, tokens, rules_version, input_hash, variant, season_until.
- It only looks at shells due within 8 days; AI text (touch 1, or follow-ups when FOLLOWUP_AI is light/full) is written on
  Saturday/Sunday UTC (GENERATION_MODE=weekend_only), or any time for drafts due within 36 h. Template text is written any day.
- Change `send_at` freely: a draft whose season ended before its new send date, or older than DRAFT_MAX_AGE_DAYS and due within 3 days,
  is rewritten (never with the same template variant).
- Cancelling a draft (status skipped/cancelled) is respected; claimed drafts are never touched.
- A draft with no valid text becomes `skipped` with `skip_reason='no_valid_text'` plus an alert: re-plan or fix templates.

## For WS6 (reports / dashboard)
`outreach.ai.usage.summary(conn, settings, day=None) -> {requests, tokens_in, tokens_out, cost_usd, cost_pkr}` (UTC day, PKR via USD_TO_PKR).
`ai_usage.last_status` holds the last real HTTP status + short message per provider (no secrets, no prompts); `disabled_until` shows a
provider switched off. Alerts raised: kinds `ai_quota`, `ai_key`, `ai_down`, `ai_budget` (80% of AI_DAILY_TOKEN_BUDGET), `ai_keys` (info: no key at all),
`draft_failed`. Health Check `ai_providers` fails only when every provider with a key is switched off; it never blocks sending.

## Config and CLI
- `engine/config/providers.yml` (six providers, no model names; a provider is used only when its env var exists), `engine/rules/email_rules.md`
  (+ `touch_hints.yml`), `engine/templates/*.txt` + `niches.yml` (seeds; the live copy is the `templates` table, seeded once per kind).
- `uv run python -m outreach.ai check` / `smoke`: lists providers, discovered models and (smoke) one tiny prompt. No DB needed.
- New settings in the WS2 block: SIGNATURE_TITLE, SIGNATURE_ROLE_LINE.
- Deps added: anthropic, pyyaml.

## Not verified
No API key exists in `app/.env`, so no live model was called: the Anthropic request shape (cache_control system block, `thinking: disabled`
via extra_body), Gemini `thinkingBudget: 0`, and discovery on real model lists are tested with fakes only. First live step: put one key in
`.env`, run `python -m outreach.ai smoke`, then `pytest tests/test_ai_live.py -s`.
