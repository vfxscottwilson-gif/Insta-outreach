# 02 Architecture
Four independent command-line tools, all local, no shared state.
| Tool | Runtime | Input | Output |
|---|---|---|---|
| gosom gmaps.exe | single Windows program (downloads Chromium) | `queries.txt` | CSV, 36 columns |
| yt-dlp.exe + `yt_leads.ps1` | single program + PowerShell script | search text | CSV (title, website, email, subscribers, ...) |
| scrapetube | Python 3.12 venv | search text | JSON list of channels |
| crawl4ai | Python 3.12 venv + Chromium | a website URL | JSON (emails, socials) |

Typical chain: scrapetube or yt-dlp finds creators, crawl4ai reads a lead website for emails, gosom finds local businesses. The lead bot imports the CSV files. `app\` is a git repo; programs and venvs are ignored by git and restored by `install\install.ps1`.
