# Database options research (checked 2026-11-04)

Verdict up front: D1 is SQLite and cannot run this app. Cloudflare's "1 GB" claim is also wrong for D1 (Free = 500 MB per DB, 5 GB per account), and Supabase Free is the same 500 MB class. Best 1 GB+ Postgres alternatives: Neon Free, Aiven Free, Prisma Postgres Free (2 GB), Nile Free. But Supabase Auth/Vault/Realtime would be lost if the DB leaves Supabase.

## 1. Supabase Free and Pro
- Free DB size: https://supabase.com/pricing : "500 MB database size per project included". Also https://supabase.com/docs/guides/platform/database-size (Free disk fixed 2 GB, quota 500 MB).
- Exceeded: SOURCES DISAGREE.
  - Docs page (fetched today): "The 500 MB database size quota does not trigger it" (read-only). Instead Fair Use restriction, requests return 402. Read-only is at "When disk usage reaches 95%" of the 2 GB disk.
  - Older docs wording and 2026 third parties (dev.to, designrevision, metacto per search results): Free enters read-only above 500 MB.
  - GitHub issue https://github.com/supabase/supabase/issues/43487 (opened 2026-03-06, closed 2026-04-13) reports the pricing page, compute/disk page ("1 GB of disk size") and docs were inconsistent. Final behaviour: not verified. Plan for read-only or 402 after 500 MB.
- Pro: https://supabase.com/pricing : "from $25/month"; "8 GB disk size per project included, then $0.125 per GB".
- Extra GB: https://supabase.com/docs/guides/platform/manage-your-usage/disk-size : gp3 "$0.125 per GB per month", first 8 GB included on Pro/Team (io2 $0.195/GB). Three sources agree (pricing page, disk-size doc, database-size doc says 8 GB autoscaling disk).
- Free projects pause: pricing page "Free projects are paused after 1 week of inactivity."

## 2. Cloudflare D1
- Limits: https://developers.cloudflare.com/d1/platform/limits/ . Free: 10 databases, 500 MB max per database, 5 GB per account. Paid: 10 GB per database, 1 TB per account, 1,000,000 databases. Queries per Worker invocation: 50 Free / 1,000 Paid.
- Pricing: https://developers.cloudflare.com/d1/platform/pricing/ . Free: "5 million per day" rows read, "100,000 per day" rows written, 5 GB total. Paid: 25 billion reads and 50 million writes per month included, 5 GB storage included then $0.75 per GB-month. Free limits reset 00:00 UTC; over limit queries are blocked.
- Workers Paid: https://developers.cloudflare.com/workers/platform/pricing/ : "a minimum charge of $5 USD per month for an account." (D1 pricing page itself does not state the price.)
- So "1 GB vs 500 MB" is not a D1 fact: per-database cap is 500 MB Free (same as Supabase). 5 GB is account-wide across up to 10 DBs.
- SQLite: https://developers.cloudflare.com/d1/ : "managed, serverless database with SQLite's SQL semantics". Not Postgres.
- Feature support for the app:
  - RLS: not in D1 docs (SQLite has none). Not supported.
  - Triggers: SQLite triggers exist (docs mention CREATE TRIGGER, recursive_triggers). PL/pgSQL functions, stored procedures, security-definer RPC: not available (SQLite has none; not documented).
  - FOR UPDATE / SKIP LOCKED: no row locks (effect-biz issue #128 via search; not on official page). Advisory locks: not available.
  - Transactions: https://developers.cloudflare.com/d1/worker-api/d1-database/ : only `batch()` is atomic ("aborts or rolls back the entire sequence"). Interactive BEGIN/COMMIT across calls: not documented as supported; third parties (dev.to "Cloudflare D1 has no BEGIN TRANSACTION", event-driven.io, DbGate) say rejected. Official page silent, so "not supported" is strongly indicated but not officially quoted.
- Python outside Cloudflare: REST API only. https://developers.cloudflare.com/api/resources/d1/subresources/database/methods/query/ : sql "Supports multiple statements, joined by semicolons, which will be executed as a batch." Rate limit: global API limit 1,200 requests per 5 minutes per user (https://developers.cloudflare.com/fundamentals/api/reference/limits/ and Cloudflare community thread "Query D1 outside of a worker"); exceeding gives 429 for 5 minutes. Not stated on D1 pages specifically (third-party/community-sourced). No interactive transactions via REST (batch only).

## 3. Cloudflare Postgres
- No Cloudflare-native Postgres.
- Hyperdrive: https://developers.cloudflare.com/hyperdrive/ : "Turn your existing regional database into a globally distributed database"; pooling + query caching for existing Postgres/MySQL (Supabase, Neon, PlanetScale...). "Available on Free and Paid plans." Free limit: 100,000 database queries per day (Workers pricing page). Not a host.
- Resold Postgres: PlanetScale Postgres can be created from the Cloudflare dashboard and billed via Cloudflare (changelog https://developers.cloudflare.com/changelog/post/2026-06-18-planetscale-databases-cloudflare-billing/ , blog https://blog.cloudflare.com/deploy-planetscale-postgres-with-workers/). Single node reportedly from $5/month (search summary of April 2026 blog). Paid, no free tier found. Pricing figure: single source, not verified on PlanetScale's page.

## 4. Free Postgres with 1 GB+
| Host | Storage | Compute / sleep | Card | Commercial use | Source |
|---|---|---|---|---|---|
| Neon Free | "1 GB/project, 20 GB account total", 100 projects | "100 CU-hours/project"; "suspends after 5 min, cannot be turned off" | "no credit card required" | not stated on pricing/plans pages; docs advise Free for experimentation, not production (via GitHub issue quoting docs). Not verified | https://neon.com/pricing , https://neon.com/docs/introduction/plans . Note a 2025-era third party said 0.5 GB; official says 1 GB. |
| Aiven Free PG | "1GB of storage, 1GB of RAM, and 1 CPU", single node, no HA | "Service powers off after a period of inactivity" (can power back on) | "requires no credit card" | "personal or professional use", "not recommended for high-traffic production" (page paraphrase). Terms not verified | https://aiven.io/free-postgresql-database ; search results (2026 comparisons) agree on 1 GB, 20 connections |
| Prisma Postgres Free | 2 GB, 200k operations/month, 50 DBs, direct connection limit 10 | pausing not described; "no time limit" | "No credit card required" | not stated. Not verified. RLS not mentioned | https://www.prisma.io/pricing |
| Nile Free | 1 GB (then $1.50/GB), 50M query tokens, 500 connections | "the db never pauses" | not stated | "For prototyping or side projects"; commercial not stated. Not verified | https://www.thenile.dev/pricing |
| Xata | no free tier: 14-day trial only, then $0.28/GB/month | scale to zero | trial no card | n/a | https://xata.io/pricing |
| CockroachDB | free Basic (10 GiB) closed to new deployments 2026-09-15; now 30-day trial, $400 credit | trial clusters pause after trial | no card for Standard trial | n/a | https://www.cockroachlabs.com/pricing/ (trial text) ; closure date from third party agentdeals.dev / GitHub robhunter/agentdeals#1933 only. Also not full Postgres (no PL/pgSQL parity, SKIP LOCKED/advisory lock/RLS support not verified) |

Notes: Neon and Aiven are real Postgres (RLS, PL/pgSQL, FOR UPDATE SKIP LOCKED, advisory locks should work; not individually verified with docs here, standard Postgres). Aiven free plan is shut down when idle and a 1 CPU/1 GB box; Neon wakes in about a second but caps 100 CU-hours per month. Python worker connects via normal connection string on all. Prisma/Nile Postgres feature coverage (RLS, advisory locks) not verified. Neon commercial-use terms: read https://neon.com/terms before committing.

## 5. Supabase Auth, Vault, Realtime with external Postgres
- Hosted Supabase: they live inside the project's own Postgres. Auth: docs say "User metadata is stored on the `raw_user_meta_data` column of the `auth.users` table" (https://supabase.com/docs/guides/auth/managing-user-data). Vault: "Vault is a Postgres extension" storing encrypted secrets in a table (https://supabase.com/docs/guides/database/vault). Realtime Postgres Changes also reads that DB's WAL. No official "bring your own database" option for hosted projects (absence; not verified beyond these pages).
- Only self-hosted Supabase can be pointed at an external Postgres (compose comments in github.com/supabase/supabase/issues/27587, requires manual roles/schemas/extensions; unsupported path). Verdict: no for hosted, DIY for self-host.
