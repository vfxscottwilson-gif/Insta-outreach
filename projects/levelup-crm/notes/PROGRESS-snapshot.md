# LevelUp CRM → ClickUp-style upgrade: Progress

| Workstream | Session | Status | % | Last update | Blocker | Next step |
|---|---|---|---|---|---|---|
| Roadmap | (earlier) | Done | 100 | 2026-11-03 | — | — |
| Clone + branch `upgrade/clickup` | Lead architect | Done | 100 | 2026-11-03 | — | — |
| Inventory existing app | Lead architect (Sonnet subagent) | Done | 100 | 2026-11-03 | — | In BRIEF.md §2 |
| Verify Supabase/Resend/Vercel facts | Lead architect (Sonnet subagent) | Done | 100 | 2026-11-03 | — | FACTS-CHECKED.md |
| Collect user inputs | Lead architect | Waiting on user | 0 | 2026-11-03 | User answers to INPUTS.md | User answers + sets up Supabase/Resend |
| Brief + Phase 0 plan | Lead architect | Done (approved) | 100 | 2026-11-03 | — | — |
| P0.1 scaffold | Lead architect | Done (app `75f57b7`) | 100 | 2026-11-03 | — | — |
| P0.2-P0.3 schema + RLS + hardening + review fixes | Lead architect (Opus subagents) | Done offline (app `7bfa622`, check:db 101 PASS / 0 FAIL) | 90 | 2026-11-03 | Docker (restart) | Run 48 pgTAP on local Supabase; app must call rpc('claim_session') |
| Dev tools | Lead architect | WSL2 + Docker Desktop installed but unused (user: no restart); Supabase CLI + Playwright in app | 100 | 2026-11-03 | — | pgTAP to run against hosted Supabase later |
| P0.4-P0.7 auth UI, admin fn, Tasks, pilot proof | Lead architect | Auth UI redesigned (Google button, code reset), admin-users deployed, admin bootstrapped (role admin, forced change) | 70 | 2026-11-04 | SMTP_PASS (free plan blocks template edit without custom SMTP); Google OAuth client | Gmail SMTP + 6-digit code template, then real login/reset proof |
| Hosted Supabase (`laxxqmtwowitopbqnejs`, Mumbai, Free) | Lead architect | Migrations + seed live, pgTAP 54/54, sign-up off, min password 8, URL+anon in .env and Vercel Preview | 100 | 2026-11-04 | — | P0.4 auth UI; admin bootstrap needs service role (Edge Function) |
| Phase 0 rest (P0.8-P0.9) | — | Not started | 0 | 2026-11-03 | Pilot sign-off | — |
| Old CRM online (GitHub public + Vercel prod from `main`) | Lead architect | Done: https://levelup-vfx-crm.vercel.app (200, screenshot proof/vercel-main.png); `upgrade/clickup` pushed → preview https://levelup-vfx-crm-git-upgrade-clickup-vfxscottwilson-gif.vercel.app | 100 | 2026-11-03 | — | Old app opens straight into Admin (no real login) until Phase 0 ships |
| Phase 1-UI (ClickUp look + motion) | Lead architect (Opus U1, Sonnet U2 + branding, Sonnet charts + UI audit) | U1, U2, branding, login redesign, logo v3 (`af6d55f`), smooth charts (`4722ae7`), old views on tokens + dialogs + phone sidebar (`277b750`,`a1d11cd`,`5dd8ee3`). Preview https://levelup-vfx-4lg5q573q-vfxscottwilson-gif.vercel.app | 60 | 2026-11-04 | Logged-in visual check (needs user login) | U3 Home dashboard + Inbox + My Tasks |
| ClickUp paid-feature map | Lead architect | FEATURES.md written (all paid features → Phases 1-6) | 100 | 2026-11-03 | — | Decided: defaults (see FEATURES.md) |
| Phases 1-4 | — | Not started | 0 | 2026-11-03 | Phase 0 sign-off | — |
| Production release (new CRM) | Lead architect + control room | LIVE: app `6dc5442` at https://levelup-vfx-crm-sigma.vercel.app (Fable: GO WITH CONDITIONS) | 95 | 2026-11-04 | Gmail app password (SMTP_PASS) for 6-digit reset codes | User picks next item; low-data/offline PWA queued |
