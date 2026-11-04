# 04 Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `MISSING SETTING: GOOGLE_SERVICE_ACCOUNT_JSON` | No `.json` key in `secrets\` | Put the Google key file in `secrets\` |
| `MISSING SETTING: SHEET_ID` or `AI_API_KEYS` | Empty value in `secrets\.env` | Open `secrets\.env` in Notepad and fill it |
| Cannot open the sheet / permission error | Sheet not shared with the service account | Share (Editor) with the `client_email` inside the JSON |
| `python` not recognised after install | PATH not refreshed | Close the window, run `INSTALL.cmd` again |
| AI notes say a key is not recognised | Typo or extra characters | Re-copy the key |
| Instagram "Action blocked" | Too many messages or same network | Set that account to Paused for 3 to 7 days |
| Scheduled run stops | GitHub pauses workflows after 60 days of no repo activity | Re-enable in the Actions tab |
