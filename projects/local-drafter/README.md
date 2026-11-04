# local-drafter

Writes cold-email BODIES for your leads using an AI model that runs on your own PC (Ollama + qwen3:8b on the GPU). It reads a leads sheet, looks up public facts, checks every rule in code and writes `Email | First Name | Subject | Body` to the **Ready to Send** tab. **It never sends email**: your Apps Script makes the Gmail drafts. Part of the hunt > email > follow-up cycle (see `..\full-cycle-emails`).

## Start here
1. New PC? Read `SETUP-GUIDE.md` section 10, then double-click `install\INSTALL.cmd`.
2. Just using it? See `SETUP-GUIDE.md` section 7 (`app\run.bat --check`, then `app\run.bat --dry-run --limit 5`).

## Folder map
| Folder / file | What is inside |
|---|---|
| `SETUP-GUIDE.md` | The 10-section roadmap for a non-expert |
| `GUIDE\` | 00 start, 01 roadmap, 02 architecture, 03 how to change, 04 troubleshooting, 05 accounts and keys |
| `install\` | `INSTALL.cmd` calls `install.ps1` (`-Check` preview, `-Uninstall` removes the shortcut only, `-SkipModel`, `-SkipTests`, `-NonInteractive`) |
| `app\` | The code, with its own git history |
| `database\` | No database (see its README) |
| `secrets\` | Gitignored: `.env`, Google key, `SECRETS-CHECKLIST.md` (names only) |
| `docs\` | Spec: `LOCAL_DRAFT_GENERATOR_PROMPT.md`, `AMENDMENTS.md` (amendments win), `UNIVERSAL_PREFLIGHT_PROMPT.md` |
| `archive\` | Old zips (never deleted) |
| `backups\` | `backup.ps1` (folder zip) |
| `notes\`, `proof\`, `reference\` | Notes, test output, read-only references |

Original build folder (another chat may still edit it): `D:\All Automations Records\Local Draft File\local-drafter`. This folder is a copy made 2026-11-05 from git commit `7ad603c`.
