# 01 Roadmap: from zero to the daily run

Owner: **You** = needs your login or decision. **Installer** = the script does it. **Claude** = can be done by an assistant on this PC. "Done" = verified on 2026-11-05 from files; "Not verified" = needs your accounts.

## Status now

| Step | State |
|---|---|
| Bot code v5 (append-only sheets, Lead Insight, Stats, one secret per key) | done; `app\CLAUDE.md` records 60 self-test checks and 92 unit tests (not re-run here: system Python lacks the packages, the installer's venv has them) |
| Packaged in this standard folder, installer, guides | done |
| `install\install.ps1 -Check` | passes; only `app\.venv` and `secrets\.env` show MISSING until the first install |
| Google robot key file present in `secrets\` | present (contents not opened) |
| GitHub repo, secrets, first green run | **not verified** (no git remote is set in `app\`) |
| Google Sheets created and shared | **not verified** |

## Steps

| # | Step | Owner | Time | Done when |
|---|---|---|---|---|
| 1 | Install on this PC: double-click `install\INSTALL.cmd`; skip all key prompts for now | You (click) + Installer | 5-10 min | `install.ps1 -Check` shows only `OK` |
| 2 | Local trial: Desktop shortcut "Lead Bot Worldwide (local test)" | You | 5 min | CSV files appear in `app\local_sheet\` |
| 3 | Google robot: Google Cloud Console, new project, enable **Google Sheets API** and **Google Drive API**, Service Accounts, create, Keys, Add key, JSON. (A key file may already be in `secrets\`.) Copy its `client_email` | You | 10 min | you have the .json and the robot email |
| 4 | Create Google Sheets: sheets.new, one per country you want (start with `US` only). Share each with the robot email as **Editor**. Copy each id (between `/d/` and `/edit`). Leave them empty | You | 3 min each | ids noted in `secrets\.env` |
| 5 | Create a GitHub repository and push `app\` (commands in `SETUP-GUIDE.md` section 6). Make it PUBLIC: no secrets are stored in the repo and two daily runs need more free minutes than a private repo has (per the workflow comment) | You | 10 min | code visible on GitHub |
| 6 | Add GitHub secrets (Settings > Secrets and variables > Actions): `GOOGLE_SA` (whole .json text), `SHEET_ID_US`, other sheet ids you made | You | 5 min | secrets listed (values hidden) |
| 7 | First run: Actions > "Run Lead Bot" > Run workflow. Read the `collect (us)` log: registration report, then `Done: ...` | You | 45 min wait | green ticks; a `Run Log` row; new rows in the US niche tabs |
| 8 | Add optional keys one at a time (AI first: `GEMINI_API_KEY_1`), re-run, check the registration report says `registered` | You | 5 min each | Lead Insight text instead of fact-only |
| 9 | Review leads, tune `Rules` / `Niches` / `Locations` in the sheet (`GUIDE\03`) | You (+ Claude) | ongoing | leads look right after 2-3 days |
| 10 | Connect the outreach bot using `docs\CONTRACT.md` | Claude | separate project | outreach bot reads the sheets by header name |

## Known limits (from `app\CLAUDE.md`)

| Limit | What it means |
|---|---|
| Free AI limits | a 429 gives fact-only insights |
| Decision-maker / personal email coverage | only about 20-35% on free sources |
| Gulf sheets (UAE, Saudi, Qatar) | thin without Serper or Apify keys |
| Tomba | not wired. Prospeo, Snov, NZBN, Disify, Reacher are wired but untested live |
| `Seen` tab | nears Google's 10M-cell limit in about a year |

More ideas: `docs\HIGH_QUALITY_LEADS_SPEC.md`, `docs\FREE_TOOLS_RESEARCH.md`, `app\UPGRADE_V5.md`.
