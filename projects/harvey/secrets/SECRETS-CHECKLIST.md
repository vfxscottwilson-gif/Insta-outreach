# Secrets checklist (names only; NEVER write values here)

Master file: `secrets\.env` (the installer creates it from `app\.env.example` and copies it to `app\.env`, which is where Harvey reads it). Full explanations of every key are inline in `app\.env.example`.
Also needed but NOT a file secret: the Claude login (`claude login`, stored by the Claude CLI in your Windows user profile).

## Required (Harvey cannot run without these)
| Secret / login | Used by | Where to get it |
|---|---|---|
| Claude CLI login (Claude Pro/Max subscription) | the AI brain | 1. Install: `npm install -g @anthropic-ai/claude-code` 2. Run `claude login` 3. Sign in in the browser |
| ONE email provider (pick one below) | sending + reading replies | see next rows |
| GMAIL_CLIENT_ID, GMAIL_CLIENT_SECRET (Option A, recommended) | Gmail/Workspace sending | Google Cloud Console > new project > enable Gmail API > Credentials > OAuth client ID type Desktop app; then run `harvey gmail auth` |
| SMTP_HOST, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD, IMAP_HOST, IMAP_PORT, IMAP_USERNAME, IMAP_PASSWORD (Option B) | any SMTP+IMAP mailbox (IMAP_* default to SMTP_*) | your mailbox provider (app password) |
| M365_CLIENT_ID, M365_TENANT_ID (Option B2) | Microsoft 365 mailbox | entra.microsoft.com > App registrations; then `harvey microsoft auth` |
| INSTANTLY_API_KEY (Option C, legacy) | Instantly sending | app.instantly.ai > Settings > Integrations > API Keys (Growth plan or higher) |

## Strongly recommended
| Secret | Used by | Where |
|---|---|---|
| REOON_API_KEY or ZEROBOUNCE_API_KEY | email verification before sending | reoon.com / zerobounce.net dashboard > API |
| TRULYINBOX_API_KEY, TRULYINBOX_WORKSPACE_ID | mailbox warmup status | trulyinbox.com (or run `harvey trulyinbox connect`) |

## Optional (leave blank to skip)
| Secret | Used by |
|---|---|
| HUNTER_API_KEY, HUNTER_MONTHLY_SEARCHES | email pattern lookup (free tier ok) |
| PRECLEARED_API_KEY | per-recipient compliance check |
| LINKEDIN_EMAIL, LINKEDIN_PASSWORD | LinkedIn automation (risk of account ban) |
| CLOUDFLARE_ACCOUNT_ID, CLOUDFLARE_API_TOKEN | deep website crawling during training |
| DATAFORSEO_LOGIN, DATAFORSEO_PASSWORD, DATAFORSEO_SANDBOX | paid discovery source |
| SERPER_API_KEY, SCAVIO_API_KEY, TINYFISH_API_KEY | alternative discovery / search sources |
| CALENDLY_API_KEY (commented out in the template) | meeting booking |
| CLAUDE_CONFIG_DIR, CODEX_HOME | advanced paths (Codex is NOT supported on Windows) |

Status: no real `.env` existed on the original PC (only `.env.example`), so `secrets\` holds no keys yet. All boxes below are open.
- [ ] Claude CLI login   - [ ] one email provider   - [ ] email verifier   - [ ] warmup (TrulyInbox)
