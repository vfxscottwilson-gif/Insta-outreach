# full-cycle-emails

**Docs-only app.** The master spec for the full hunt > email > follow-up cycle: lead import, accounts and caps, sending through the Gmail API, drafts, follow-ups, scheduling on GitHub Actions, all driven from Google Sheets. There is no code and nothing to install here. The spec is `docs\CLAUDE_MAX_BUILD_PROMPT.md` (a build prompt for Claude, delivered in phases).

## Start here
1. Read `docs\CLAUDE_MAX_BUILD_PROMPT.md` (sections 1-3 give the business context and the architecture).
2. See `SETUP-GUIDE.md` for which finished app covers which part of the cycle.

## The cycle and the apps that implement it
| Stage | App folder (in `F:\Github Repos\projects\`) |
|---|---|
| Hunt (find leads) | `lead-bot-worldwide`, `lead-bot-au`, `yt-creator-finder`, `ig-outreach`, `scraper-tools` |
| Organise leads | `sheet-organizer` |
| Draft emails | `local-drafter` (local AI), `outreach-bot` |
| Send, follow-up, track | `email-automation` |
| CRM / dashboard | `levelup-crm`, `database` |

## Folder map
| Folder / file | What is inside |
|---|---|
| `docs\` | `CLAUDE_MAX_BUILD_PROMPT.md` (the master spec) |
| `install\` | `INSTALL.cmd` + `install.ps1`: stub that only checks the spec exists |
| `GUIDE\`, `SETUP-GUIDE.md` | Short guides (no accounts or keys are needed) |
| `app\`, `database\` | Empty on purpose (docs only) |
| `secrets\` | Empty, gitignored (none needed) |
| `backups\backup.ps1` | Folder zip |
| `notes\`, `proof\`, `reference\`, `archive\` | Empty / for later |

Source: `D:\All Automations Records\Full Cycle Emails Outreach File\CLAUDE_MAX_BUILD_PROMPT.md` (copied 2026-11-05, not moved).
