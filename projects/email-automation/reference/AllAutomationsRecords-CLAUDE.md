# All Automations Records: Workspace Index

**Business:** a video-editing and social-media agency. **End goal:** fully automated hunt → email → follow-up pipeline.
**Tracker:** `PROGRESS.md` (update it after every work session).

| Project | Code folder (git repo) | What it does |
|---|---|---|
| Lead generation | `Lead generation/au-lead-bot/au-lead-bot` | Worldwide lead bot → Google Sheets (GitHub Actions daily) |
| Lead generation (AU) | `Lead generation/au-only-lead-bot` | AU-only edition |
| Draft emails | `Draft Creating automation Code/outreach-bot` (**current, v3**; `outreach-bot-v2` is superseded) | Drafts outreach emails from lead facts |
| Instagram outreach | `Insta outreach Automation/ig-outreach` | IG lead/DM assist |
| Figma organizer | `Figma Organizer/sheet-organizer` | Sheet organizer |
| Scraper tools | `Scraper Tools/` (not a git repo; third-party binaries) | gosom, yt-dlp, scrapetube, crawl4ai |
| YouTube leads | `YT Leads Autmation/` (zip only) | YouTube creator leads |
| Harvey | `Harvey/` (third-party clone, own git + CLAUDE.md) | Autonomous sales agent |

Each code folder has its own `CLAUDE.md`; read it before working there.

## Workspace rules
- `*.zip` files are old snapshots/backups; never edit them, and never treat them as current.
- `*Keys*.txt`, `*all info*.txt` and `.env` hold secrets: never read them aloud, print them or commit them.
- Commit each working step in that bot's git repo. Never push without approval.
