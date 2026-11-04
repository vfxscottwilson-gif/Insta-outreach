# 00 Start here: set up Harvey on a PC

## A. Install
1. Copy the whole folder (with `secrets\`) to the new PC.
2. Double-click `install\INSTALL.cmd`. Click **Yes** if Windows asks.
3. Expected: a CHECKLIST with OK / SKIP lines and `Done.` FAIL lines point to `04-TROUBLESHOOTING.md`.

## B. Keys
1. Decide your email option (`secrets\SECRETS-CHECKLIST.md`). Gmail is recommended, on a dedicated secondary domain.
2. Open `secrets\.env` in Notepad and fill the values after each `=` for your chosen option (the installer may already have asked you).
3. Delete `app\.env` if it exists, then run `install\INSTALL.cmd` again so the new keys are copied.

## C. Log in to Claude
1. Install the Claude CLI if the installer warned (needs Node.js):
```
npm install -g @anthropic-ai/claude-code
```
2. Log in:
```
claude login
```
You should see a browser window; sign in with the Claude Pro/Max account.

## D. Teach Harvey your product (first run)
Open PowerShell in the `app` folder, then:
1. Activate the environment:
```
.\.venv\Scripts\Activate.ps1
```
2. Learn your product from your website (writes `harvey.local.yaml`):
```
harvey train https://your-company.com
```
3. Choose the facts that make a good prospect (free ones):
```
harvey signals --confirm free
```
4. Find businesses (free source):
```
harvey discover
```
5. Gmail users only, once:
```
harvey gmail auth
```
6. Open the dashboard (or use the Desktop shortcut) and open the private link it prints:
```
harvey dashboard
```
7. Only when you are happy with the limits and the Outbox, start the sending loop (or double-click `install\Run Harvey.cmd`):
```
harvey run
```

Not verified here: steps D1 to D7 need a real Claude login and a mailbox, which were not available during packaging.
