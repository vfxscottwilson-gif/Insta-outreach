# 04 Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `No AI key found` | All AI keys empty in `secrets\.env` | Add at least one key |
| `GOOGLE_SA ... missing or not the full service-account JSON` | No `.json` key in `secrets\` | Put the whole key file in `secrets\` |
| `Cannot open the sheet` | Wrong SHEET_ID, API not enabled, or Sheet not shared | Check the ID, enable Google Sheets API, share (Editor) with the `client_email` |
| `python` not recognised after install | PATH not refreshed | Close the window, run `INSTALL.cmd` again |
| Same note filed twice | Very differently worded notes | Delete the extra row by hand in the filing tab |
| Daily run stops | GitHub pauses workflows after 60 days of no repo activity | Re-enable in the Actions tab |
| Only ~150 notes filed | Free AI tiers cap per run | The rest wait for the next run |
