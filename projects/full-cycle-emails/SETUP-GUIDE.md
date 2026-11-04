# full-cycle-emails: Setup guide
This is a docs-only app. Nothing to install, no accounts, no keys.

## 1. What this app is
The master spec (`docs\CLAUDE_MAX_BUILD_PROMPT.md`) for the full hunt > email > follow-up cycle on Google Sheets + Gmail API + GitHub Actions.

## 2. Accounts needed
None to read the spec. The apps that implement it need Google, GitHub and others; see each app's own SETUP-GUIDE (listed in `README.md`).

## 3. How it fits together
It is documentation only: no frontend, backend or database. The architecture the spec describes is in its section 2.

## 4. Folder map
See `README.md`.

## 5. First-time install
1. Nothing is required. To confirm the spec file is present, open PowerShell in `install\` and run:
```
.\install.ps1 -Check
```
You should see `OK      docs only: master spec found`.

## 6. Secrets
None.

## 7. Use it
1. Open `docs\CLAUDE_MAX_BUILD_PROMPT.md` in any text editor.
2. To build or review a stage, give the relevant section to Claude together with the finished app folder from the table in `README.md`.

## 8. How to change common things
| I want to... | Do this |
|---|---|
| Update the plan | Edit `docs\CLAUDE_MAX_BUILD_PROMPT.md` (keep the old copy in `archive\`) |

## 9. Troubleshooting
| Problem | Fix |
|---|---|
| Installer says MISSING | The spec file was moved; copy it back to `docs\` |

## 10. Move to a new PC
1. Copy the whole folder.
2. Optional check:
```
.\install\install.ps1 -Check
```
