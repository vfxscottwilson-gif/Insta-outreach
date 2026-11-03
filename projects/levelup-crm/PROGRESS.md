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
| Dev tools | Lead architect | WSL2 + Docker Desktop installed; Supabase CLI + Playwright in app | 90 | 2026-11-03 | **User must restart PC** | After restart: start Docker, `npx supabase start`, `supabase test db` |
| P0.4-P0.7 auth UI, admin fn, Tasks, pilot proof | — | Not started | 0 | 2026-11-03 | Supabase project + Resend (INPUTS.md) | After P0.3 |
| Phase 0 rest (P0.8-P0.9) | — | Not started | 0 | 2026-11-03 | Pilot sign-off | — |
| Old CRM online (GitHub private + Vercel prod from `main`) | Lead architect | gh 2.103.3 + Vercel CLI 65.10.0 installed, telemetry off; `main` builds (worktree `app-main`) | 40 | 2026-11-03 | User: `gh auth login`, `vercel login`, confirm private repo | Push upgrade/clickup, `vercel --prod` from app-main, screenshot |
| Phases 1-4 | — | Not started | 0 | 2026-11-03 | Phase 0 sign-off | — |
