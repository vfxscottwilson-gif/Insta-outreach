# Cloud move plan: run the whole Database app on an always-on server (PC can be off)

Written 2026-11-05. Facts come from the hosting research of the same day (see `HOSTING-PLAN.md`, `archive/research-raw/hosting-research.json`); items marked NOT VERIFIED must be tested during the move.

## What moves
The app is one Flask program that serves the website AND runs the 2-minute Google Sheets scan, plus one SQLite file (`data/dash.db`). Moving means: the same program + the same file run on a small always-on Linux server instead of the owner's PC. No rewrite, no new database. The public address stays `https://levelup-database.outreach-web.workers.dev` (same Worker, same tunnel idea, started on the server instead of the PC).

## Option ranking (from the research)
| # | Option | Cost | Needs | Catch |
|---|---|---|---|---|
| 1 | **Oracle Cloud Always Free VM** (AMD micro, 1 GB RAM, or Ampere A1 if capacity exists) | $0 | Credit/debit card at sign-up (verification only, not charged; prepaid and virtual cards are often rejected) | Idle-reclaim rule (CPU, network and for A1 memory all under 20% for 7 days can get the VM reclaimed); reports of account closures; A1 often "out of capacity"; outbound SMTP port 587 NOT VERIFIED |
| 2 | Hetzner Cloud CX23 | about EUR 5.99/month ex VAT (partly verified) | Card | Paid; stock sometimes limited |
| 3 | Google Cloud e2-micro | about USD 3.65/month for the IPv4 address (not covered by the free tier) | Card | Not fully free; region rules |
| 4 | Render Starter + disk | about USD 7.25/month | Card, code pushed to GitHub | Paid; 512 MB RAM tight |
Ruled out earlier: Render/Koyeb/Fly/Railway free, PythonAnywhere free, Vercel, Netlify, Cloudflare Pages/Workers (no persistent disk, no background thread, sleeping, or non-commercial).
**Pick: Oracle Always Free (AMD micro). Fallback: Hetzner.** If the owner will not add any card, the only choice is to stay on the PC and use the nightly cloud backup.

## Steps, who does what
| # | Step | Owner | Time |
|---|---|---|---|
| 0 | Decide: card yes or no; finish the UI merge and connect the real sheets first (moving a half-built app twice wastes time) | Owner | now |
| 1 | Create the Oracle account at https://signup.cloud.oracle.com (home region cannot be changed later: choose the nearest region that offers Always Free, for example Mumbai or a Gulf region; capacity differs by region, NOT VERIFIED) | **Owner** (account, card, passwords) | 15-30 min |
| 2 | Create the VM: Compute > Instances > Create, shape VM.Standard.E2.1.Micro (Always Free eligible), image Ubuntu 24.04, download the SSH key, public IP on | Owner clicks, Claude guides in the browser pane | 15 min |
| 3 | Open the SSH connection from the PC; harden: non-root user, updates, firewall allows only SSH, add a 1 GB swap file | Claude | 20 min |
| 4 | Install Python 3.12, Node 22, cloudflared (Linux build, owner approves the download, checksum checked) | Claude | 20 min |
| 5 | Copy the app (git archive of the final commit) and create the virtual environment; copy `.env` and the Google service account file by a secure copy that Claude never prints (owner approves) | Claude | 20 min |
| 6 | Test the Google Sheets API and Gmail SMTP port 587 FROM the server. If 587 is blocked: send reset codes through an HTTPS mail API (Resend free tier, 3,000 mails/month per the CRM research) with a small code change by the build chat | Claude, build chat if needed | 30 min |
| 7 | Run the app and the tunnel supervisor as systemd services (start at boot, restart on failure, logs to files) | Claude | 30 min |
| 8 | Cut over: stop the app on the PC (final copy of `dash.db`), start on the server, the supervisor writes the new tunnel address into KV, run the end-to-end login check on the public link | Claude | 20 min |
| 9 | Nightly backup of `dash.db` (SQLite online backup) to cloud storage and to the PC; one restore test | Claude | 30 min |
| 10 | Keep-alive for Oracle's idle rule: light scheduled work so CPU/network stay above the threshold, or upgrade the account to Pay As You Go (still $0 inside the free limits, exempt from reclaim per third-party reports, NOT VERIFIED) | Owner decides | later |
Total after the account exists: about 3 to 4 hours of work. A week-long soak (watch uptime, scan lag, backups) before switching the PC off for good.

## Updates later
`install/deploy-to-server` script (to be written in step 7): copy the new commit with `git archive`, run migrations, restart the service, run the login check, roll back to the previous folder if the check fails.

## Risks
- Oracle can reclaim or close a free account without notice: keep the nightly backup off Oracle (PC plus a second cloud store) and know the 1-hour restore steps.
- The tunnel in use is Cloudflare's testing tier: when a free domain (dpdns.org) or a paid .com exists, switch to a named tunnel.
- 1 GB RAM is enough for the app (about 150-250 MB) but wrangler/npm spikes need the swap file.
- Gmail SMTP from Oracle NOT VERIFIED; fallback above.

## Decision needed from the owner
Add a card to Oracle (verification only, not charged)? Yes: start at step 1. No: stay on the PC with the nightly cloud backup; or pay about EUR 6 a month for Hetzner (also needs a card).
