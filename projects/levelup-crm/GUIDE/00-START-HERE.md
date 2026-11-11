# 00 Start here

Level Up VFX CRM: a private website where staff clock in/out, see tasks and write reports, and the admin manages people and work. Data is in Supabase (cloud), the site is on Vercel (cloud), a copy goes to a Google Sheet every 5 minutes. This folder holds the code, the installer, the backups and the keys.

## What you need
Windows 10, internet, and these logins (see `05-ACCOUNTS-AND-KEYS.md`): GitHub, Vercel, Supabase, Google (only for the Sheet key).

## If you only want to check it is healthy
1. Open File Explorer, go into the `install` folder, click the address bar, type `cmd`, press Enter.
2. Run:
```
INSTALL.cmd -Check
```
3. You should see green `PASS` lines and a final `RESULT:` line. Yellow `MISSING` lines tell you what to fix.

## If you are on a new PC
Follow `SETUP-GUIDE.md` section 5, then `INSTALL.cmd -Local` and open http://localhost:5173.

## Where to go next
| I want to | Read |
|---|---|
| Understand the plan and status | `01-ROADMAP.md` |
| Know how the parts fit | `02-ARCHITECTURE.md` |
| Change something | `03-HOW-TO-CHANGE-THINGS.md` |
| Fix a problem | `04-TROUBLESHOOTING.md` |
| Know which keys/accounts exist | `05-ACCOUNTS-AND-KEYS.md` |
| Publish a change | `..\DEPLOYMENT.md` |
| Back up / restore | `..\database\RESTORE.md` |
