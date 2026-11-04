# Engine E1: interfaces for the AI-layer session (WS2), 2026-11-03

Repo `F:\Github Repos\projects\email-automation\app`, package `engine/src/outreach/` (Python 3.12, uv). Commits 5e69c4f, 150c5f4.
Run tests: `cd engine` then `uv run pytest -q` (local Postgres via pgserver, ~40 s first start). DB fixtures: `tests/conftest.py` (`conn` = owner connection on a fresh migrated DB), row helpers `tests/db_helpers.py` (use, don't edit).

## Plug-in points
| Need | Use |
|---|---|
| Run inside the engine | `from outreach.tick import Phase, register, Ctx`; at module import: `register(Phase("drafts", run, every_minutes=30))`; `run(ctx)` must be idempotent, short, honour `ctx.dry_run`. Add ONE line `from . import <module>  # noqa: F401` in the marked block of `engine/src/outreach/__main__.py` (the only edit allowed there). |
| Settings | `ctx.settings["KEY"]` (validated; bad values already fell back to defaults). Your keys already exist in `settings.SPECS` "Writing (WS2)" block: ALLOW_WORD_FREE, FOLLOWUP_AI, GENERATION_MODE, DRAFT_MAX_AGE_DAYS, LOW_DATA_USE_TEMPLATE, AI_DAILY_TOKEN_BUDGET, USD_TO_PKR, SIGNATURE_HTML, LIST_UNSUBSCRIBE_MAILTO, BRAND_NAME, OPT_OUT_LINE, SIGNATURE_ADDRESS / _WEBSITE / _PHONE. New keys: add `Spec(...)` lines inside that block only (seeded automatically next tick). |
| Secrets | `os.environ` (CLI calls `config.load_env()` which reads `app/.env`). `providers.yml` names the env var per provider. Never log keys, prompts, bodies or addresses. |
| Alerts | `from outreach.alerts import alert, resolve, resolve_kind`; `alert(conn, "warning", "ai_quota", "Provider X is out of daily quota", dedupe_key="ai:x:quota")`. No lead addresses or email text in messages. |
| DB | `ctx.conn` (psycopg 3, autocommit; wrap writes in `with ctx.conn.transaction():`); `from outreach.db import rows` -> list of dicts. |
| Health Check | `from outreach.healthcheck import EXTRA_CHECKS, Check`; `EXTRA_CHECKS.append(check_ai_keys)` where `check_ai_keys(conn, settings) -> Check(name, ok, blocks_sending=False, detail)`. |
| Logging | `logging.getLogger("outreach.ai")`; the root handler redacts addresses anyway. |

## Data contract
- Lead fields for prompts (allowlist): `first_name, company, website, youtube_url, city, region, country_code, niche, angle, low_data, style_index, latest_video, insight, socials`. Never `extra_data` (subscribers, scores).
- Drafts: planner (WS3) creates the shell row `drafts(lead_id, touch_no, account_id, send_at, status='draft')`; the writer fills `subject`, `body` (body only: no greeting / opt-out / sign-off / signature), `generated_by`, `provider`, `model`, `tokens_in`, `tokens_out`, `rules_version`, `input_hash`, `variant`, `season_until`. Status `ready` requires subject + body (DB check). Follow-up subjects are replaced at claim time by `Re: <touch 1 subject>`.
- `templates(kind, variant, body)`, `signatures` (account_id null = default), `ai_usage(day, provider, model)` upsert for tokens / cost / `disabled_until`.
- Send-time rendering (E3 calls it): please provide `outreach.compose.render(settings, lead: dict, account: dict, draft: dict, signature: dict) -> Rendered` with `Rendered.subject: str`, `.text: str` (greeting + body + opt-out + "Best regards," + signature), `.html: str | None` (minimal div/br, inline signature style, None when SIGNATURE_HTML is off). E3 adds every header (From, To, Message-ID, In-Reply-To, References, List-Unsubscribe) and the MIME envelope; it takes `render` as an injected function so it does not block on you.

## WS2 owns
`engine/src/outreach/ai/` (providers, discovery, router), `compose.py`, `validator.py`, `signature.py`, `templates.py`, `drafts.py` (generation phase), `engine/config/providers.yml`, `engine/rules/email_rules.md`, `engine/templates/`, tests `tests/test_ai_*.py`, `test_compose*.py`, `test_validator*.py`, `test_signature*.py`, `test_templates*.py`, `test_drafts*.py`. Add runtime deps to `engine/pyproject.toml` `[project] dependencies` only (one line each, then `uv lock`).

## Do not touch
`supabase/` (schema changes: message the Engine session with the need; it writes migration 0003+), `engine/src/outreach/{tick,settings (except the WS2 Spec block),caps,alerts,db,config,log,healthcheck,emails,mapping,geo,sheets,importer,sender,gmail,accounts}.py`, `engine/src/outreach/tools/`, `engine/tests/{conftest.py,db_helpers.py,test_db_*.py,test_caps.py,test_settings.py,test_tick.py,test_healthcheck.py,test_emails.py,test_mapping.py,test_geo.py,test_import*.py,test_send*.py}`, `web/`.
