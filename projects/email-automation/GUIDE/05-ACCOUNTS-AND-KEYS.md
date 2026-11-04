# 05 Accounts and keys (names and IDs only; values live in `secrets/`)

| Service | What it is / name | ID or account | Where used | Secret lives in |
|---|---|---|---|---|
| Supabase | Project `haroonvfx-outreach` (Mumbai, free) | ref `bnivytzudrpjlscwdxuh`; dashboard https://supabase.com/dashboard/project/bnivytzudrpjlscwdxuh | database, auth, edge functions | `DATABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY`, `SUPABASE_ACCESS_TOKEN` in `.env` |
| Supabase account email | owner of the project | fill in: _(the Gmail you signed in with)_ | login to dashboard | password manager |
| App owner login | first admin in the app | k***@gmail.com (owner, must change password at first sign-in) | web app | the user |
| Cloudflare | Worker `levelup-outreach` (static assets) | URL https://levelup-outreach.outreach-web.workers.dev; workers.dev subdomain `outreach-web` | web hosting | wrangler OAuth login on the PC; optional `CLOUDFLARE_API_TOKEN` + `CLOUDFLARE_ACCOUNT_ID` in `.env` |
| Cloudflare account email | fill in: run `npx wrangler@4.157.0 whoami` | | | |
| Google Cloud | Project `trans-campus-513315-v0` (service account for Sheets) | service account `mail-tracking@trans-campus-513315-v0.iam.gserviceaccount.com` | read lead sheets, write the backup sheet | key file `secrets\sheet-reader.json` (copied to `%USERPROFILE%\.secrets\`); path in `GOOGLE_SA_JSON` |
| Google OAuth (Gmail connect) | Desktop + Web OAuth clients, consent screen "In production" | not created yet (roadmap #3) | connect Gmail accounts | `GOOGLE_OAUTH_CLIENT_ID/SECRET` in `.env` |
| AI | Gemini and/or Groq key (free) | | AI writer | `GEMINI_API_KEY`, `GROQ_API_KEY` in `.env` |
| Google Sheets | lead sources, export/backup sheet | IDs are set inside the app (Settings > sources, `EXPORT_SHEET_ID`) and in the DB; the lead bot's sheets: see `reference/au-lead-bot/` | import / backup | n/a |
| Mail accounts (14+) | senders | `secrets\accounts.local.csv` | engine | OAuth tokens in Supabase Vault |

**Related code (not moved):** `D:\All Automations Records\Draft Creating automation Code\outreach-bot` (v3), `...\Lead generation\au-lead-bot\au-lead-bot`, `...\Full Cycle Emails Outreach File\CLAUDE_MAX_BUILD_PROMPT.md`. Doc snapshots are in `reference\`.

**Sibling apps:** `projects\levelup-crm` (CRM), `projects\database` (lead dashboard).

Where to get each key: `app\docs\START_HERE.md`, `app\docs\GOOGLE-SHEETS-SETUP.md`, `notes\session-notes\*\credential-setup-paths-2026-11-03.md`.
