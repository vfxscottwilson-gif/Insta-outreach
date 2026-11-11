# <App name>: Setup guide

Write for a non-expert on Windows 10. Numbered steps. NEVER write secret values.

## 1. What this app is
(What it does, who uses it, main screens.)

## 2. Accounts needed
| Service | Why | Free? | Sign-up link |
|---|---|---|---|
| | | | |

## 3. How it fits together (backend vs frontend)
(Frontend = ... hosted on ... | Backend = ... | Database = ... | Functions = ...)

## 4. Folder map
(Point to the README.md table; add app-specific notes.)

## 5. First-time install
1. Open `install\` and double-click `INSTALL.cmd`.
2. (Steps and what you should see.) Pattern for every step: one action, the exact command in its own code block, then what the user should see.
3. Example step: check nothing is missing before installing.
```
INSTALL.cmd -Check
```
You should see green `PASS` lines; `MISSING` lines tell you what the installer will add.

## 6. Secrets
See `secrets\SECRETS-CHECKLIST.md`. Where to put them: (file path, names only).

## 7. Run it / use it
(Start command or link, login.)

## 8. How to change common things
| I want to... | Do this |
|---|---|
| | |

## 9. Troubleshooting
| Problem | Fix |
|---|---|
| | |

## 10. Move to a new PC
1. Copy the whole app folder.
2. Put the secrets back in `secrets\` (from your password manager).
3. Double-click `install\INSTALL.cmd`.
4. Check: open PowerShell in `install\` and run `.\install.ps1 -Check`. Every line should say OK.
