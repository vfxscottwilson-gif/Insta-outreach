# Supabase facts, verified 2026-11-03

Method: raw `.md` doc pages and the full changelog were downloaded with curl on 2026-11-03 and searched. Quotes are verbatim from those files. "Not found" means no official page states it.

1. **Breaking changes 2025-2026** (https://supabase.com/changelog). 21 entries are labeled Breaking Change in 2025-2026. Relevant ones:
   - **Data API / new tables** (2026-04-28, https://supabase.com/changelog/45329-breaking-change-tables-not-exposed-to-data-and-graphql-api-automatically): "Opt-in today, default for new projects on 2026-05-30, enforced on all projects on 2026-10-30."
   - **Vault**: not found. No 2025-2026 breaking-change entry.
   - **RLS**: no RLS breaking change. Realtime lockdown (2026-07-14, https://supabase.com/changelog/realtime-schema-locked-down-against-modification): "RLS policies on `realtime.messages` still work."
   - **auth schema** (2025-03-18, https://supabase.com/changelog/34270-restricting-access-on-auth-storage-and-realtime-schemas-on-april-21-2025): "On 2025-04-21 Supabase restricts SQL on the `auth`, `storage`, and `realtime` schemas."
   - **pg_cron**: not found in 2025-2026. The 2023 `cron.job` write restriction is outside the range.
   - **Postgres version**: 2026-09-25 (https://supabase.com/changelog/postgres-15-19-17-11-breaking-changes): "ltree and btree_gist indexes may need reindexing, and pgcrypto data encrypted with legacy ciphers needs re-encryption." Also 2026-07-22 (https://supabase.com/changelog/extension-version-pinning-ignored): "From 2026-08-05 the version clause is ignored and the extension's default version is installed, with a warning."
   - **Upcoming, not on your list**: 2026-10-12 (https://supabase.com/changelog/cbc-tls-ciphers-deprecated): "Supabase will be disabling a subset of TLS 1.2 ciphers on project HTTP APIs on November 10, 2026."

2. **Vault** (https://supabase.com/docs/guides/database/vault)
   - Create: `vault.create_secret(secret, name, description)`. The page shows positional examples only, with no formal signature: `select vault.create_secret('another_s3kre3t', 'unique_name', 'This is the description');`. Name and description are optional: "Secrets can also have an optional *unique* name and an optional description." It returns a UUID: "The function returns the UUID of the new secret."
   - Update: `vault.update_secret(secret_uuid, new_secret, new_name, new_description)`. Quote: "Provide the secret UUID as the first argument, followed by an updated secret, name, or description:" No formal signature is given, and behavior for omitted arguments is not found.
   - Read: `vault.decrypted_secrets`. Columns from the example output: id, name, description, secret, decrypted_secret, key_id, nonce, created_at, updated_at. Quote: "Notice how this view has a `decrypted_secret` column that contains the decrypted secrets."
   - Who can read by default (anon, authenticated, others): not found. Closest quotes: "anyone that has access to the view has access to decrypted secrets." and "Which roles should have access to the `vault.secrets` table should be carefully considered."

3. **Securing the Data API** (https://supabase.com/docs/guides/api/securing-your-api)
   - Grants needed for `authenticated`: "A table isn't reachable through the Data API unless you have granted a role privileges on it." Example: `grant select, insert, update, delete on table public.your_table to authenticated;`. Also add RLS policies. Quote: "Grant the minimum privileges each role needs."
   - Setting: "In the Data API settings, disable **Automatically expose new tables** to revoke the privileges the Data API uses."
   - Conflict: the same page says "On existing projects, new objects in `public` receive the following default privileges:" and lists automatic grants to anon, authenticated and service_role. It also says "Supabase is changing the platform default to revoke these automatic grants so that exposure becomes opt-in." No date is given. The RLS page (https://supabase.com/docs/guides/database/postgres/row-level-security) says "Not every project grants these automatically."
   - The changelog says enforcement on all projects was 2026-10-30, which has passed, but the docs do not confirm the current state of any project. Check per project with the query in "Check your default privileges" on the securing page. Quote: "When the query returns no rows, new objects grant nothing to the Data API roles until you grant access explicitly."

4. **session_id claim and auth.sessions**
   - Claim: yes. "Every access token contains a `session_id` claim, a UUID, uniquely identifying the session of the user." (https://supabase.com/docs/guides/auth/sessions) It is listed under "## Required claims" on https://supabase.com/docs/guides/auth/jwt-fields as "**Session ID** - Unique session identifier".
   - `auth.sessions` readability: not found. No page states SELECT rights on it. The auth schema is not on the Data API: "For security, this schema is not exposed on the auto-generated API." (https://supabase.com/docs/guides/auth/architecture) The sessions page says: "You can check that the `session_id` claim in the JWT corresponds to a row in the `auth.sessions` table."

5. **Default Postgres major version, new projects**
   - Managed projects: not found as an explicit default statement. The changelog implies Postgres 17 for new projects: "New projects on Postgres 17.6.1.016 and later ship pgmq 1.5.1" (2025-10-08, https://supabase.com/changelog/39378-potential-breaking-change-in-pgmq-from-1-4-4-to-1-5-1-and-temporary-halt-on-upgrade-for-existing-projects). This is an inference, not a stated default.
   - Self-hosted only: "Postgres 17 is the default, so a new self-hosted instance with **no existing data** starts on Postgres 17" (https://supabase.com/docs/guides/self-hosting/postgres-upgrade-17).
   - Postgres 14 ends: "Supabase support for Postgres 14 ends on 2026-07-01." (https://supabase.com/changelog/45827-deprecation-notice-support-for-postgres-14-ending-on-1st-july-2026)

6. **pg_cron and pg_net on Free**
   - pg_cron: plan availability not found. The Cron docs (https://supabase.com/docs/guides/cron) have no plan notice.
   - pg_net: plan availability not found. The extension page (https://supabase.com/docs/guides/database/extensions/pg_net) says: "The pg\_net API is in beta. Functions signatures may change."
   - Related pricing fact (https://supabase.com/pricing): "Free projects are paused after 1 week of inactivity." Whether a paused project runs scheduled jobs is not stated in the docs.

**Not verified:** Plan-level extension availability is not in the docs. Check Database > Extensions in the dashboard on a Free project. The changelog and the securing page disagree on the default-grant state, and I could not resolve that from the docs.
