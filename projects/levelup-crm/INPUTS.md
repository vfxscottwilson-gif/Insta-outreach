# Inputs needed from you

Answer in chat by number. **Never paste keys, passwords or tokens into chat.** Keys go into files or commands on your own PC, as shown below.

## A. Quick answers (type in chat)

| # | Question | Required? | Default if you say "pick for me" |
|---|---|---|---|
| 1 | **Admin email(s)** (who gets full access) | Required | `khizarvfx@gmail.com` (the admin in today's seed data) |
| 2 | **Employee emails + display names** | Required | none: I need a real list for real logins |
| 3 | **Brand**: name, logo file path (SVG/PNG), primary + accent colour | Required | Name "LevelUp", lucide mark, colours picked by the design subagent |
| 4 | **Top 5 ClickUp features** you want first (orders Phases 2-3) | Required | Board, Calendar, Gantt + dependencies, Docs, Dashboards |
| 5 | **Hierarchy names** (ClickUp: Space / Folder / List) | Optional | Department / Client / Project |
| 6 | **Migrate today's browser data?** (yes/no) If yes, I'll give you a one-line console snippet to copy it out of each browser | Required | no (start clean, re-seed priorities/statuses/projects) |
| 7 | **Credential vault visibility**: everyone (as today) or admin-only? | Required | admin-only, encrypted |
| 8 | **Add real CRM entities** (clients, leads, deals pipeline)? yes/no | Required | no for now (Later) |
| 9 | **Workday**: timezone + target hours/day | Optional | from today's settings (09:00-18:00, 8 h) |
| 10 | **Multiple assignees per task?** | Optional | yes (ClickUp behaviour) |
| 11 | **Hosting**: Vercel (see the note under step C), or "local only for now"? | Required | local only until Phase 4 |
| 12 | **Supabase plan**: Free while building, Pro ($25/mo) at go-live? | Required | Free now, Pro at go-live |
| 13 | **OK to add a Claude API key later** for AI features? | Optional | no (Later) |

Facts behind 7, 11 and 12 are in `FACTS-CHECKED.md` (checked 2026-11-03).

## B. Supabase (required): about 10 minutes

1. Open https://supabase.com, then click **Start your project**. Sign up with GitHub or email.
2. Click **New project**. Set Organization: yours. Name: `levelup-crm`. Database password: click **Generate**, then save it in your password manager (do not paste it in chat). Region: the one nearest your team. Plan: Free.
3. Wait until the dashboard says the project is ready (about 2 minutes).
4. Go to **Project Settings → API**. You will see the **Project URL** and **anon / publishable key**. Leave this tab open.
5. On your PC, create the file `F:\Github Repos\projects\levelup-crm\app\.env` in Notepad with exactly these two lines:
   ```
   VITE_SUPABASE_URL=<paste Project URL>
   VITE_SUPABASE_ANON_KEY=<paste anon key>
   ```
   Save it. (It is gitignored, so it never reaches GitHub.)
6. **Do not** copy the `service_role` key anywhere. I will ask you to run one command for it later (Phase 0 step 6), and it goes straight into Supabase.
7. Install the Supabase CLI and log in. In PowerShell:
   ```powershell
   npm install -g supabase
   ```
   ```powershell
   supabase login
   ```
   A browser opens. Click **Authorize**. The terminal then shows "You are now logged in".
8. Tell me in chat: "Supabase ready" plus the **project ref**. The ref is the `xxxx` part of `https://xxxx.supabase.co`. It is not secret.
9. Optional: in Claude Code, run `/mcp`, then authorize **supabase**. That lets me read the schema directly. (I can't start this login myself.)

## C. Resend email (required for reset codes): about 15 minutes, plus DNS wait

Supabase's built-in email reaches only your own team account (2 emails/hour), so employees would never get reset codes.

1. Open https://resend.com and sign up.
2. You need a domain you own (for example `levelupvfx.com`). Go to **Domains → Add Domain** and type it.
3. Resend shows 3-4 DNS records (TXT/MX). Add each one at your domain registrar (GoDaddy, Namecheap, Cloudflare and so on) exactly as shown.
4. Back in Resend, click **Verify**. Wait until the status says **Verified** (minutes to a few hours).
5. Go to **API Keys → Create API Key**. Name: `supabase-smtp`. Permission: **Sending access**. Copy the key once.
6. In Supabase, go to **Project Settings → Authentication → SMTP Settings** and turn on **Enable custom SMTP**. Fill in:
   - Sender email: `no-reply@<your domain>`
   - Sender name: your brand
   - Host: `smtp.resend.com`
   - Port: `465`
   - Username: `resend`
   - Password: paste the Resend API key
   Click **Save**.
7. Tell me in chat: "Resend ready, sender = no-reply@yourdomain". Do not paste the key.

No domain? Say so. I'll build and test everything with emails sent only to your own address, and reset codes for employees wait until a domain is verified.

## D. Vercel (optional now, needed in Phase 4)

Vercel's free Hobby plan is **non-commercial only**, and a company CRM counts as commercial, so plan on Vercel Pro (about $20/user/month, not 3-source verified). Also, once Vercel is linked, **every branch push creates a preview deploy**, so I will never push without your OK.

1. Open https://vercel.com, sign up with GitHub, then **Add New → Project** and import `levelup-vfx-crm`.
2. Do not add environment variables yet. I'll give exact steps in Phase 4.
3. Tell me in chat: "Vercel linked" or "local only for now".

## E. Security note (action for you, 2 minutes)

The repo is **public**, and `src/utils/initialData.ts` contains vault values (API keys, render-farm passwords, for example `VFX_RenderFarm_Pass!2026`). If any of these are real, **change those passwords/keys now**. Removing them from the code (Phase 0 does that) does not remove them from GitHub history. Tell me "rotated" or "they were fake".
