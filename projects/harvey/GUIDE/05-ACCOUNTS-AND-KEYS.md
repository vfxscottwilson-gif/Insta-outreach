# 05 Accounts and keys (names and IDs only; values live in `secrets\`)

Never write a key value in this folder's guides, in chat, or in a commit. The master file is `secrets\.env` (gitignored). The installer copies it to `app\.env`, which is what Harvey reads. Full per-key notes: `secrets\SECRETS-CHECKLIST.md` and the comments in `app\.env.example`.

## Login (not a file)
| Service | Account | Used for | Stored in |
|---|---|---|---|
| Claude Pro/Max | not recorded (your account) | AI brain via `claude login`; required | Claude CLI profile in your Windows user folder. Does NOT travel when the folder is copied: log in again on a new PC |

## Required: pick ONE mailbox option
| Option | Env var names | Setup | Status |
|---|---|---|---|
| A. Gmail / Workspace (recommended upstream) | `GMAIL_CLIENT_ID`, `GMAIL_CLIENT_SECRET` | Google Cloud project, enable Gmail API, OAuth client type Desktop app; set `channels.email.provider: gmail`; run `harvey gmail auth` | not set yet |
| B. SMTP + IMAP | `SMTP_HOST`, `SMTP_PORT`, `SMTP_USERNAME`, `SMTP_PASSWORD`, `IMAP_HOST`, `IMAP_PORT`, `IMAP_USERNAME`, `IMAP_PASSWORD` (IMAP_* default to SMTP_*) | Mailbox provider app password; `provider: smtp` | not set yet |
| B2. Microsoft 365 | `M365_CLIENT_ID`, `M365_TENANT_ID` | Entra app registration, `harvey microsoft auth`; see `app\docs\microsoft365.md`; `provider: microsoft` | not set yet |
| C. Instantly (legacy) | `INSTANTLY_API_KEY` | Growth plan or higher; `provider: instantly` | not set yet |

## Strongly recommended
| Service | Env var names | Why |
|---|---|---|
| Reoon or ZeroBounce | `REOON_API_KEY`, `ZEROBOUNCE_API_KEY` | Verify emails. Without one, addresses stay "guess" and are never sent |
| TrulyInbox | `TRULYINBOX_API_KEY`, `TRULYINBOX_WORKSPACE_ID` | Warmup status in `harvey warmup`. Easier: `harvey trulyinbox connect` |

## Optional
| Service | Env var names | Why |
|---|---|---|
| Hunter | `HUNTER_API_KEY`, `HUNTER_MONTHLY_SEARCHES` | Email pattern lookup |
| Precleared | `PRECLEARED_API_KEY` | Per-recipient cold-email rule check (`app\docs\precleared.md`) |
| DataForSEO | `DATAFORSEO_LOGIN`, `DATAFORSEO_PASSWORD`, `DATAFORSEO_SANDBOX` | Paid discovery (any value in the sandbox var routes to the free sandbox) |
| Serper / Scavio / TinyFish | `SERPER_API_KEY`, `SCAVIO_API_KEY`, `TINYFISH_API_KEY` | Search and discovery |
| Cloudflare | `CLOUDFLARE_ACCOUNT_ID`, `CLOUDFLARE_API_TOKEN` | Deep website crawling during training |
| LinkedIn | `LINKEDIN_EMAIL`, `LINKEDIN_PASSWORD` | LinkedIn automation (risk of account ban; also needs `channels.linkedin.enabled: true`) |
| Calendly | `CALENDLY_API_KEY` (commented out in the template) | Meeting booking |
| Advanced paths | `CLAUDE_CONFIG_DIR`, `CODEX_HOME` | Leave unset (Codex is not supported on Windows). Listed in the checklist; not found in `.env.example` in this check |

## Which keys the installer asks for
`SMTP_HOST`, `SMTP_USERNAME`, `SMTP_PASSWORD`, `GMAIL_CLIENT_ID`, `GMAIL_CLIENT_SECRET`, `INSTANTLY_API_KEY`, `REOON_API_KEY`, `ZEROBOUNCE_API_KEY`, `HUNTER_API_KEY`, `TRULYINBOX_API_KEY` (hidden typing, Enter to skip). Anything else you add by editing `secrets\.env` in Notepad.

## Not needed
No GitHub, Supabase or Google Sheets login. Prices and free tiers were not re-checked for these guides; check each vendor's pricing page before paying.
