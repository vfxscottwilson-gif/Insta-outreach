# 03 How to change things

1. Writing style: open the Outreach sheet > tab "Email Rules" > edit rows. The next run uses them.
2. Daily target and switches: tab "Options" (all switches default Off).
3. After any code change run the tests; you should see `58/58 passed`:
```
powershell -ExecutionPolicy Bypass -File install\run-bot.ps1 -SelfTest
```
4. Back up the folder:
```
powershell -ExecutionPolicy Bypass -File backups\backup.ps1
```
5. Move to another PC: `SETUP-GUIDE.md` section 10.
6. Code changes reach the cloud only when pushed to the GitHub repo (`app\` has its own git; ask before pushing).
