# 04 Troubleshooting
| Problem | Fix |
|---|---|
| `Python ... not on PATH yet` | Close the window, run INSTALL.cmd again |
| winget not available | Install "App Installer" from the Microsoft Store, or install Python 3.12 from python.org |
| yt-dlp download: SHA-256 mismatch | The installer deleted the file. Re-run; if it repeats, download by hand (`docs\TOOLS-MANIFEST.md` section 2) |
| yt-dlp suddenly returns nothing | Update it: `app\yt-dlp\yt-dlp.exe -U` |
| crawl4ai-setup very slow or stalls | Normal on slow links (an earlier pip run stalled). Re-run INSTALL.cmd; it resumes |
| `/contact` page blocked by a site | Expected for some sites; the script continues |
| gmaps.exe: Google blocks / CAPTCHA | Lower `-c`, fewer queries, run from a home IP; Google Maps scraping breaks Google ToS |
| Antivirus flags gmaps.exe or yt-dlp.exe | They are unsigned downloads; verify the source URLs in `docs\TOOLS-MANIFEST.md`, then allow |
