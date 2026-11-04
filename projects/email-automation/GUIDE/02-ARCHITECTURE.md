# 02 Architecture

```
Lead sheets (Google Sheets, read-only)        Gmail accounts (OAuth, per owner)
          |                                              ^   |
          v                                              |   v
  engine (Python worker: tick every 1-2 min) ---> Supabase Postgres (single source of truth)
   import > dedupe > plan > AI draft > send           ^   (RLS, Auth, Vault, Edge Functions)
   mailbox sync > replies/bounces > reports           |
                                                      v
                       web (React PWA on Cloudflare Workers) + phone install
```

| Layer | Where | Tech | Notes |
|---|---|---|---|
| Front end | `app/web/` | Vite + React + TS + Tailwind + shadcn, PWA | Hosted: Cloudflare Workers static assets, worker name `levelup-outreach`. Local: `Start Outreach App.vbs` serves `dist/` on port 4180 |
| Back end (logic) | `app/engine/` | Python 3.12, `uv` | Stateless `tick()`. CLI: `uv run python -m outreach healthcheck | tick | seed-settings`. Tools in `src/outreach/tools/` |
| Back end (data) | `app/supabase/` | Postgres migrations + 3 Edge Functions | Project `haroonvfx-outreach`, ref `bnivytzudrpjlscwdxuh`, Mumbai |
| Hosting | Cloudflare (web), this PC for the pilot (engine) | free tiers | 24/7 engine host still to choose (roadmap #10) |
| Keys | `app/.env` (copy in `secrets/`) | gitignored | Never in git or chat |

## Data flow
1. Source sheets > `importer.py` > `leads` (unique canonical email). 2. `planner.py` makes `sends` with jittered `send_at`. 3. `drafts.py` + `ai/` write; `validator.py` checks. 4. `sender.py` claims rows (`FOR UPDATE SKIP LOCKED`), writes `sending` with our Message-ID, then calls Gmail. 5. `mailbox/` syncs inboxes, classifies replies/bounces. 6. Web reads views/RPCs with the user's login; admin vs employee scoping by RLS.

## Which file to change for what
| Want to change | File |
|---|---|
| Colours, theme | `web/src/styles/theme.css`, `web/DESIGN.md` |
| Company name / logo | `web/src/lib/brand.ts`, `web/public/*.svg`, `npm run icons` (app icons from `public/logo.svg`) |
| Daily caps (70 / 650), ramp | `engine/src/outreach/caps.py` (+ `web/src/lib/caps.ts`); tests in `tests/test_caps.py` |
| Runtime settings (TEST_MODE, PAUSE_ALL, address, signature) | DB table `settings` (web: Settings), seed in `engine/config/` |
| Email templates / wording rules | `engine/templates/`, `engine/rules/`, `engine/src/outreach/validator.py` |
| Sheet column mapping | `engine/src/outreach/mapping.py` |
| Database schema | new file in `supabase/migrations/` (never edit applied ones), then `docs/SCHEMA.md` |
| Edge Functions | `supabase/functions/<name>/` |
| Local launcher | `app/Start Outreach App.vbs` |
