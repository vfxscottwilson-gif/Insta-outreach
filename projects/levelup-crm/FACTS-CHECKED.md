# Facts checked (2026-11-03, Sonnet research subagent; official docs first)

| # | Fact | Verdict | Source |
|---|---|---|---|
| 1 | Built-in Supabase SMTP only reaches org team members; 2 emails/hour; testing only | True | supabase.com/docs/guides/auth/auth-smtp |
| 2 | Free plan pauses after 1 week idle; 500 MB DB, 50k MAU; Pro $25/mo per org (+$10 compute credit) | True (Edge Function quota + 2-project cap not independently confirmed) | supabase.com/pricing |
| 3 | Built-in "single session per user" is Pro+ only, enforced at next refresh | True | supabase.com/docs/guides/auth/sessions |
| 4 | `signOut({scope:'others'})` revokes refresh tokens only; access tokens live until expiry (default 1 h); JWT has `session_id` = `auth.sessions.id` | True | supabase.com/docs/reference/javascript/auth-signout |
| 5 | Recovery by 6-digit code (`{{ .Token }}` + `verifyOtp({email, token, type:'recovery'})`) | Partly: `{{ .Token }}` and `recovery` type documented; exact combo not shown in docs → must test in pilot. OTP 6-10 digits (default 6), expiry default 1 h (CLI config ref) | supabase.com/docs/guides/auth/auth-email-templates |
| 6 | Use Supabase Vault (`vault.create_secret`, `vault.decrypted_secrets`); pgsodium "pending deprecation" | Partly true (pending, not yet deprecated) | supabase.com/docs/guides/database/vault |
| 7 | Resend free: 3,000/mo, 100/day, 3 domains; SMTP `smtp.resend.com:465`, user `resend`, pass = API key; verified domain required for arbitrary recipients | True | resend.com/pricing, resend.com/docs/send-with-supabase-smtp |
| 8 | Vercel Hobby = free, non-commercial only; pushing any non-production branch auto-creates a preview deploy | True | vercel.com/docs/plans/hobby |

Design consequences:
- Single session on Free plan: our own `active_sessions` + RLS `is_current_session()` is required (built-in setting is Pro only and lags up to 1 h anyway). Shorten JWT expiry (e.g. 10 min) as defence in depth.
- Resend + verified domain is mandatory before any employee can get a reset code.
- A business CRM on Vercel Hobby breaks Vercel's terms → Vercel Pro ($20/user/mo, per Hobby page; not 3-source verified) or another host.
- Supabase Free pauses after 1 week idle → Pro for daily production use.

## Dev tools (checked 2026-11-03, official pages; third-party corroboration not done)

| Tool | Free? | License | Notes |
|---|---|---|---|
| Docker Desktop | Free if company < 250 employees AND < $10M revenue | Proprietary (Docker SSA) | Supports Win 10 Pro 22H2 (build 19045) today; needs WSL ≥ 2.1.5, 8 GB RAM. Win 10 is out of Microsoft support → may be dropped later. Fallback: Rancher Desktop / Podman (open source, listed by Supabase docs). |
| Supabase CLI 3.0.0 | Free | MIT | Installed per-project as npm devDependency (`npx supabase ...`). |
| Playwright 1.64.1 | Free | Apache-2.0 | Installed + Chromium. |
| Local mail catcher | Free | — | `supabase start` includes Mailpit at http://127.0.0.1:54324: reset codes readable locally, no Resend needed for dev. |
| pgTAP (`supabase test db`) | Free | — | Runs pg_prove in a container → needs Docker even for `--linked`. |
