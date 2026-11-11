# Moving the database off Supabase

Short version: the **data and the table design move easily**. The **login system, the token safe, the server functions and the live updates are Supabase features** and must be replaced. Plan a few days of engineering for those, not an afternoon.

## What moves as it is
| Part | How |
|---|---|
| Table design (all tables, views, rules, triggers) | The migration files `app\supabase\migrations\0001` to the latest. Apply them to the new database with `uv run python -m outreach.tools.migrate` (from `app\engine`, with `DATABASE_URL` pointing at the new database) |
| The data (accounts, leads, sends, mail events, replies, settings, reports...) | `database\move_data.py export` then `import` (below) |
| The engine (sender, sync, planner) | Only `DATABASE_URL` in `app\.env` changes |

## What does NOT move, and what replaces it
| Supabase feature | Used for | Replacement on a plain Postgres host |
|---|---|---|
| **Auth** (`auth.users`, passwords, sessions, Google sign-in, password-reset emails) | Every login to the app | Another login service (for example a self-hosted Supabase Auth / GoTrue, Auth.js, Keycloak). Passwords cannot be exported in readable form: everyone gets a reset. `auth.uid()` and `auth.jwt()` in our rules must be supplied by the new service (the test file `app\supabase\tests\supabase_shim.sql` shows the minimum those two functions need) |
| **Roles** `anon`, `authenticated`, `service_role`, `supabase_auth_admin` and the REST API (PostgREST) the web app calls | The web app reads and writes through them; our row-level security depends on them | Run PostgREST yourself with the same role names, or put a small API server in front of the database. The row-level security rules themselves are plain Postgres and move with the migrations |
| **Vault** (`vault.secrets`) | The Gmail refresh tokens, encrypted | Not exportable as files. Either re-connect every mailbox on the new system (safest), or read each token with `engine.get_gmail_token` and store it in the new secret store. Never write tokens to disk in plain text |
| **Edge Functions** (`admin-users`, `gmail-connect`, `sign-in`) | Creating logins, the Connect button, the sign-in lock | Deno code: run it on Deno Deploy / Cloudflare Workers, or rewrite as routes of the API server. Their settings (Google client, app address) must be set again there |
| **Realtime** | Live badge and Sync button updates | The app falls back to its one-minute refresh; or run Supabase Realtime yourself / use Postgres LISTEN/NOTIFY through the API server |
| **Custom Access Token hook** | Refusing a locked login | A check in the new login service that calls `public.custom_access_token_hook` |
| Dashboard extras (daily backups, SQL editor, logs) | Convenience | The new host's own tools; `backups\backup.ps1` keeps working once `DATABASE_URL` changes |

## Steps for the data
All commands in PowerShell from `F:\Github Repos\projects\email-automation\app\engine`.

1. See what will move (names and row counts only):
   ```
   uv run python ..\..\database\move_data.py list
   ```
2. Export (the folder will hold personal data: keep it private, delete it after the move):
   ```
   uv run python ..\..\database\move_data.py export ..\..\database\export
   ```
3. Create the new database. It needs the roles and the two `auth` functions first (see the table above), then apply the migrations to it.
4. Import into the new database (it empties each table there first):
   ```
   uv run python ..\..\database\move_data.py import ..\..\database\export --to "postgresql://USER:PASSWORD@HOST:5432/DBNAME"
   ```
5. Point the engine at it: change `DATABASE_URL` in `app\.env`, then `uv run python -m outreach healthcheck`.
6. Delete the `export` folder.

## Status
- `list` was run against the live database on 2026-11-11 (read-only).
- `export` and `import` are written but **have not been run end to end against a second host**: test them on a spare database before relying on them.
- `profiles` rows keep their user ids. Logins must be recreated in the new login service **with the same ids**, or the ids in `profiles` and every `owner_user_id` must be remapped.
