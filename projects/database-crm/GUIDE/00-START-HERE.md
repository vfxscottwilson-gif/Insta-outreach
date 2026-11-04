# 00 Start here: set up the Lead Dashboard on a PC

## A. Install
1. Copy the whole `database-crm` folder (with `secrets\`) to the PC.
2. Double-click `install\INSTALL.cmd`. Click **Yes** if Windows asks.
3. Expected: a CHECKLIST of OK / SKIP lines and "Done". FAIL lines point to `04-TROUBLESHOOTING.md`.

## B. Keys
1. The two random keys are created for you. Google service account and Gmail app password: `05-ACCOUNTS-AND-KEYS.md`.
2. Sheets can be read only after the service account JSON is in `secrets\` and each sheet is shared with its email.

## C. Open the app
1. Double-click `install\create-admin.cmd` (once): email, name, password twice.
2. Double-click **Database Dashboard** on the Desktop. The browser opens http://127.0.0.1:8080; sign in.
3. You should see the dashboard (empty until sheets are connected: Sources & sync -> Add a sheet).

Safety: the app only READS the sheets unless you set `DASH_WRITEBACK=on`. Do not run tests against real sheets; tests use fixtures.
