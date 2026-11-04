# 05 Accounts and keys (names and IDs only; values live in `secrets/`)

| Service | Name | Account | Where used | Secret lives in |
|---|---|---|---|---|
| Google Cloud | project + service account ("robot") | your Google account | Sheets access | `secrets\*.json` (local) / GitHub secret `GOOGLE_SA` |
| Google Sheets | SHEET_ID_AU_ONLY (old name SHEET_ID still works) | your Google account; each sheet shared with the robot email as Editor | where leads are written | `secrets\.env` / GitHub secrets |
| GitHub | repo for this app (its OWN repo, separate from worldwide) | your GitHub account | daily Actions run | repo secrets + variables |
| AI + data APIs | see `secrets\SECRETS-CHECKLIST.md` | various, all optional | better insights / more leads | `secrets\.env` / GitHub secrets |

Not verified: the GitHub repo URL and the Google project name (no git remote is set in `app\.git`; the key file was not opened). Write them into `secrets\SECRETS-CHECKLIST.md` once known.
