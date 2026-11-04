# 03 How to change things
| I want to... | Do this |
|---|---|
| Change which versions get installed | Edit the version variables at the top of `install\install.ps1`, update `docs\TOOLS-MANIFEST.md` |
| Add a new query | gosom: add a line to your `queries.txt`. yt-dlp: change `-Query` |
| Filter YouTube by subscribers | `yt_leads.ps1 -MinSubs / -MaxSubs` |
| Slow down (avoid IP blocks) | `yt_leads.ps1 -DelayMs 3000`; gosom `-c 1` |
| Add a tool | Put it in `app\<tool>\`, add install steps to `install.ps1` and a row in `docs\TOOLS-MANIFEST.md` |
