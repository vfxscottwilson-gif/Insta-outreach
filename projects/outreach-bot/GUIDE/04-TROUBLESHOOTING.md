# 04 Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `python` not recognised | Python installed but PATH not refreshed | Close the window, run `install\INSTALL.cmd` again |
| "running scripts is disabled" | PowerShell policy | Start with `powershell -ExecutionPolicy Bypass -File ...` |
| GOOGLE_SA missing | No key file | Save the JSON as `secrets\google-sa.json` |
| 401 on Groq/OpenRouter | Dead or wrong key | Make a new key; see `app\DIAGNOSIS.md` |
| Gemini quota hit after few emails | Keys share one Google project | Create each key in its own new project |
| Few drafts per day | Free quota | Normal: 400-700 a day with free keys; the rest waits |
