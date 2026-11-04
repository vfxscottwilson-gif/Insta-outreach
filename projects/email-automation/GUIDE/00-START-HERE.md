# 00 Start here: set up Outreach on a PC

Checked on the build PC 2026-11-05 (dry run). A full fresh-PC install is **not verified**.

## A. Install (about 10 minutes)
1. Copy the whole `email-automation` folder to the new PC. Keep the `secrets` folder inside it (it has your keys).
2. Open the folder, double-click `install\INSTALL.cmd`. A black window opens.
   - First time you may add `-DryRun` to preview: right-click the folder background > Open in Terminal, type `install\INSTALL.cmd -DryRun`, press Enter. Nothing is changed.
3. If Windows asks "Allow this app to make changes", click **Yes** (winget installing Node, Python, uv, Git).
4. Wait for **CHECKLIST**. You should see `OK` for Node.js, Python, uv, Git, and `OK`/`SKIP` for npm install, build, uv sync, `.env`.
5. If it says `Notepad opened app\.env`: do part B, then double-click `INSTALL.cmd` again.
6. If a tool shows `WARN ... not on PATH yet`: close the window, open `INSTALL.cmd` again.

## B. Fill in the keys (only if `secrets\.env` was missing)
1. In Notepad (`app\.env`) paste each value right after the `=` (no quotes, no spaces). Where each comes from: `GUIDE\05-ACCOUNTS-AND-KEYS.md`.
2. If the database password contains `@`, write it as `%40` inside `DATABASE_URL`.
3. Save (Ctrl+S), close. Run `INSTALL.cmd` again.
4. Copy the finished `app\.env` into `secrets\.env` so the next install has it.

## C. Open the app
1. Double-click **Outreach** on the Desktop. It opens as its own window.
2. Sign in with the owner login (email + password; the app asks you to choose a new password the first time).
3. You should see the dashboard. A "Sample data" badge means the web app is not connected to the database (see roadmap).

## D. Check the engine
1. Open Terminal in `app\engine`.
2. Type `uv run python -m outreach healthcheck` and press Enter.
3. Expected: schema and settings OK. Postal address, a connected account and TEST_ADDRESSES may still fail; those are your steps (roadmap, phase C).

## E. Remove the shortcuts later
`install\INSTALL.cmd -Uninstall` removes only the Desktop and Start-menu shortcuts.
