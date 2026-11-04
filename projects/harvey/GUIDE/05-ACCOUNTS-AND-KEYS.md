# 05 Accounts and keys (names and IDs only; values live in `secrets/`)

| Service | Name | ID / account email | Where used | Secret lives in |
|---|---|---|---|---|
| Anthropic Claude (CLI login) | Claude Pro/Max | not recorded (your account) | AI brain (required) | Claude CLI profile, not this folder |
| Gmail / Workspace | GMAIL_CLIENT_ID, GMAIL_CLIENT_SECRET | not set yet | send/read email, option A | secrets\.env |
| SMTP+IMAP mailbox | SMTP_HOST/PORT/USERNAME/PASSWORD, IMAP_* | not set yet | option B | secrets\.env |
| Microsoft 365 | M365_CLIENT_ID, M365_TENANT_ID | not set yet | option B2 | secrets\.env |
| Instantly | INSTANTLY_API_KEY | not set yet | option C (legacy) | secrets\.env |
| Reoon / ZeroBounce | REOON_API_KEY / ZEROBOUNCE_API_KEY | not set yet | email verification (recommended) | secrets\.env |
| TrulyInbox | TRULYINBOX_API_KEY, TRULYINBOX_WORKSPACE_ID | not set yet | warmup (recommended) | secrets\.env |
| Hunter, Precleared, Cloudflare, LinkedIn, DataForSEO, Serper, Scavio, TinyFish | see checklist | optional | extras | secrets\.env |

Required vs optional: `secrets\SECRETS-CHECKLIST.md`.
