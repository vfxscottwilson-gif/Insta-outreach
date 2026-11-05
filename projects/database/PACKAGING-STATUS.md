# Packaging status (add to CLAUDE.md "Status / next step" when the lead merges)

- 2026-11-05: packaged around the existing folder. Added README, SETUP-GUIDE, GUIDE\00-05, install\ (INSTALL.cmd, install.ps1 with -Check/-DryRun/-Uninstall/-WithPreview/-RunTests/-NoPrompt, start-dashboard.cmd, create-admin.cmd), backups\backup.ps1, database\README+RESTORE, docs\, notes\ (copies only), secrets\ (demo logins copied unread, SECRETS-CHECKLIST, .gitignore). No existing file edited; app\ untouched.
- Tested in a temp copy: -Check OK; real install OK (venv, pip, init, health check HTTP 200, shortcut, idempotent re-run); backup.ps1 -DryRun and real run OK; -Uninstall removes shortcuts only; temp copy deleted.
- Test suite in the copy: 389 passed, 1 failed (`tests/test_theme.py::test_employee_sees_no_admin_nav_items`: nav now shows "Add leads"; stale test). The "327 tests" figure in CLAUDE.md is out of date.
- Not tested: live Google Sheets (needs service account + sheet links, deliberately not run), Gmail reset email, `-WithPreview` (npm ci/build), winget install paths (Python was already present).
- Next: user supplies service_account.json + sheet links (Q1) and Gmail app password (Q6) into secrets\; dashboard chat fixes the stale test; lead commits the hub.
