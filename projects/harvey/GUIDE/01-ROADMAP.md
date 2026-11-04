# 01 Roadmap: honest status

Date of this status: 2026-11-05 (packaging day). Source of truth for upstream features: `app\README.md`, `app\CHANGELOG.md`.

## Done (verified)
| Item | Proof |
|---|---|
| Upstream clone copied with its own `.git` (commit 6b6a23a, harvey 0.3.0, MIT) | `docs\UPSTREAM.md` |
| Installer tested in a temp copy: venv, `pip install -e`, `import harvey`, tests | `proof\install-temp-copy-2026-11-05.log`, `proof\pytest-temp-copy-2026-11-05.log` |
| `install\install.ps1 -Check` (dry run) works and changes nothing | run it; lines are OK / SKIP / DRY / WARN |
| Desktop + Start-menu shortcut "Harvey Dashboard" made by the installer | `install\install.ps1`, section 6 |
| Guides, secrets checklist, `backups\backup.ps1`, database restore notes | `GUIDE\`, `secrets\SECRETS-CHECKLIST.md`, `database\README.md` |

## Open (needs you, not code)
| # | Item | Blocker |
|---|---|---|
| 1 | Claude CLI installed and `claude login` done | Claude Pro/Max subscription |
| 2 | Secondary sending domain and mailbox | Domain + mailbox purchase |
| 3 | Mailbox keys in `secrets\.env` (names in `05-ACCOUNTS-AND-KEYS.md`) | Step 2 |
| 4 | An email verifier key (Reoon or ZeroBounce) | Free tier signup |
| 5 | Mailbox warmup (TrulyInbox, paid, or another service) for 2 to 4 weeks | Step 2 |
| 6 | `compliance.postal_address` filled in `harvey.local.yaml` (US CAN-SPAM; until set, mail still sends with a warning) | You |
| 7 | Quiet hours timezone set to yours (default in `app\harvey.yaml` is `America/New_York`) | You |

## Not verified (never run end to end here)
- A real `harvey train`, `discover`, `gmail auth` and `harvey run` cycle: no Claude login or mailbox existed in the packaging session.
- Real email send and reply handling.
- The full test suite on this PC (`-RunTests` is very long); only the temp-copy run in `proof\` exists.
- Prices of paid services (not re-checked for these guides).

## Next steps, in order
1. Complete open items 1 to 4.
2. `harvey train`, `signals --confirm free`, `discover` (`00-START-HERE.md`, step D).
3. Review a first batch in the Outbox and approve a few by hand. Do not switch to autopilot yet.
4. Wait for warmup (item 5), then `harvey run`.
5. After a week: look at the **Usage** and **Activity** tabs, and bounces in `harvey status`.

## Later / optional
| Idea | Where |
|---|---|
| Use Harvey only as a list builder (no sending) | `harvey export` (CSV of deliverable prospects); `app\CLAUDE.md` "After Setup" |
| Paid discovery sources (DataForSEO, Serper) | `harvey discover --providers`, `app\CLAUDE.md` Step 5 |
| Cold-email compliance check (Precleared; only for sender country GB or US) | `app\docs\precleared.md` |
| Microsoft 365 mailbox instead of Gmail | `app\docs\microsoft365.md` |
| Pull newer Harvey versions | `docs\UPSTREAM.md` (git pull, then delete `app\.venv`, re-run installer) |

## Known limits
- Codex (ChatGPT) brain is refused on Windows by upstream design. Claude only.
- Third-party clone: do not edit `app\`. Put your settings in `app\harvey.local.yaml` and `secrets\.env`.
- Harvey only works while its window is open on a PC that is awake. It is not a cloud service.
- Upstream `app\CLAUDE.md` still says Instantly is the only paid integration; the newer docs list Gmail, SMTP and Microsoft 365 as native providers. Trust `app\README.md` and `app\harvey.yaml` where they differ.
