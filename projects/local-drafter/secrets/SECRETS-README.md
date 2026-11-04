# secrets/ : SECRETS. Do not share, upload or commit.

Gitignored folder. Holds what the installer needs on a new PC.

| File | What | Used by |
|---|---|---|
| `.env` | The 3 settings in SECRETS-CHECKLIST.md. Created by the installer; copied to `app\.env` | the drafter |
| `*.json` (your Google service-account key) | Lets the tool read/write your Google Sheet | path stored in `.env` as `GOOGLE_SERVICE_ACCOUNT_FILE` |

The original folder contained no secrets when it was packaged (file mode needs none). Re-copy after any key change.
