# FIX REPORT - USA YT Leads (2026-11-10)

## Failing line in your log
`Sheets HTTP 403 during GET spreadsheet metadata` (src/sheets.py setup -> call). Config, secrets format and all 29 tests PASSED.
So the code reads your 3 secrets correctly; Google itself refused the first Sheets call.

## Map of the run
checkout -> pip install -> check-config OK -> tests OK -> preflight OK (secrets present, JSON valid)
-> run.py -> Sheets.setup() GET spreadsheet -> **403 (Google refuses)** -> stop (no data touched)

## Why 403 (code is not the cause; cause is on Google's side). Check in this order
1. **Google Sheets API not enabled** in project `possible-dream-514310-h8` (the project of your service account).
   Console > APIs & Services > Library > "Google Sheets API" > Enable. (YouTube Data API being enabled does NOT cover this.)
   Both APIs must be enabled in the SAME project that owns the service account.
2. **GitHub secret holds a key from a different service account** than the one shared on the sheet.
   New preflight log line prints the key's email + project: it must be exactly
   `usa-yt-leads@possible-dream-514310-h8.iam.gserviceaccount.com`.
   If not: IAM > Service Accounts > usa-yt-leads > Keys > Add key > JSON, paste the WHOLE file in secret GOOGLE_SERVICE_ACCOUNT_JSON.
3. Sheet ID secret (must end `...ZSAl1kIk`; preflight prints last 6 chars). A wrong ID gives 404, not 403.
Your screenshots show sharing is correct (Editor), so #1 is the most likely.

## What I changed (3 small edits)
| File | Change | Why |
|---|---|---|
| src/sheets.py | 403/other errors now append Google's own reason (e.g. SERVICE_DISABLED / PERMISSION_DENIED + message) | Old message was a generic guess; now the log names the exact cause |
| src/preflight.py | Prints service-account email, project and last 6 chars of sheet ID (no secrets) | Lets you confirm the secret matches the shared email |
| .github/workflows/daily.yml | Removed leftover git merge-conflict markers (<<<<<<< / >>>>>>>) | The local file was invalid YAML; kept the "Check repository secrets" step |

## What I did NOT change
Qualification rules, discovery, contacts, YouTube calls, sheet layout, tests, schedule, secrets handling. I found no unneeded code that causes errors, so I removed nothing (removing working code would add risk).

## Not verified
I cannot reach your Google project or GitHub secrets from here, so the 403 fix (enable API / correct key) is on your side; run the workflow after.

## Expected result once fixed
Run creates missing tabs (Dashboard, Daily Report, All Leads, Needs Review, niche tabs, Settings, hidden memory tabs) with headers,
searches YouTube within quota budget, qualifies US channels (subs/uploads/views rules), appends new leads + emails at the bottom,
writes Dashboard/Daily Report, uploads output/ as artifact. Daily at 08:30 PKT. First run may be small; reruns never duplicate (Contact ID reconcile).

## Apply
Push these files (or paste src/sheets.py, src/preflight.py, workflows/daily.yml), then Actions > USA YT Leads > Run workflow.
