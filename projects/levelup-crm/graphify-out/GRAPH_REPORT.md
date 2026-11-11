# Graph Report - levelup-crm  (2026-11-04)

## Corpus Check
- 12 files · ~10,932 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 73 nodes · 63 edges · 11 communities (8 shown, 3 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `bc0514cc`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Level Up VFX CRM: how to use it
- ClickUp paid features → LevelUp CRM build map
- LevelUp VFX CRM → ClickUp-style Work OS: Upgrade Plan
- LevelUp CRM upgrade: Brief + Phase 0 plan (for approval)
- Inputs needed from you
- ClickUp-style UI plan (Phase 1-UI), for approval
- 4. Roadmap
- Who can write what (audit 2026-11-04)
- Facts checked (2026-11-03, Sonnet research subagent; official docs first)
- clean-check.cjs
- PROGRESS.md

## God Nodes (most connected - your core abstractions)
1. `Level Up VFX CRM: how to use it` - 12 edges
2. `ClickUp paid features → LevelUp CRM build map` - 11 edges
3. `LevelUp VFX CRM → ClickUp-style Work OS: Upgrade Plan` - 8 edges
4. `LevelUp CRM upgrade: Brief + Phase 0 plan (for approval)` - 6 edges
5. `Inputs needed from you` - 6 edges
6. `4. Roadmap` - 6 edges
7. `ClickUp-style UI plan (Phase 1-UI), for approval` - 6 edges
8. `Who can write what (audit 2026-11-04)` - 4 edges
9. `Facts checked (2026-11-03, Sonnet research subagent; official docs first)` - 2 edges
10. `{chromium}` - 1 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Import Cycles
- None detected.

## Communities (11 total, 3 thin omitted)

### Community 0 - "Level Up VFX CRM: how to use it"
Cohesion: 0.15
Nodes (12): 1. First login and your password, 2. Forgot your password, 3. Set duty hours (admin), 4. Add team members (admin), 5. Create teams (admin), 6. Assign tasks (admin), 7. Clock in and out, 8. Reports (+4 more)

### Community 1 - "ClickUp paid features → LevelUp CRM build map"
Cohesion: 0.17
Nodes (11): ClickUp paid features → LevelUp CRM build map, Decisions needed, Decisions (user, 2026-11-03: "use the defaults"), Not copied, Phase 1: Shell, hierarchy, core tasks (U1-U5, in progress), Phase 2: Views, fields, time, agile, Phase 3: Docs, collaboration, reporting, automation, Phase 4: Polish, tests, deploy (as in the roadmap) (+3 more)

### Community 2 - "LevelUp VFX CRM → ClickUp-style Work OS: Upgrade Plan"
Cohesion: 0.25
Nodes (7): 1. Where the CRM is today, 2. Target stack, 3. Gap table, 5. What I need from you, 6. Copy-paste prompt for Claude Code, 7. Risks and open questions, LevelUp VFX CRM → ClickUp-style Work OS: Upgrade Plan

### Community 3 - "LevelUp CRM upgrade: Brief + Phase 0 plan (for approval)"
Cohesion: 0.29
Nodes (6): 1. Brief, 2. Inventory: every existing feature (must all still work), 3. Phase 0 plan: Foundation (pilot first), 4. Then (outline only, each gets its own plan + approval), 5. Risks / unknowns, LevelUp CRM upgrade: Brief + Phase 0 plan (for approval)

### Community 4 - "Inputs needed from you"
Cohesion: 0.29
Nodes (6): A. Quick answers (type in chat), B. Supabase (required): about 10 minutes, C. Resend email (required for reset codes): about 15 minutes, plus DNS wait, D. Vercel (optional now, needed in Phase 4), E. Security note (action for you, 2 minutes), Inputs needed from you

### Community 5 - "ClickUp-style UI plan (Phase 1-UI), for approval"
Cohesion: 0.29
Nodes (6): ClickUp-style UI plan (Phase 1-UI), for approval, Does the preview look like ClickUp? No., Order change vs ROADMAP, Risks, What we build, Workstreams (pilot first)

### Community 6 - "4. Roadmap"
Cohesion: 0.33
Nodes (6): 4. Roadmap, Phase 0: Foundation (size L, pilot gate), Phase 1: ClickUp shell + hierarchy + List/Board + task panel (size L), Phase 2: More views, custom fields, dependencies, unified time (size L), Phase 3: Docs, Dashboards, Automations, Inbox, Chat, Goals, Forms (size L), Phase 4: Polish, motion, performance, tests, deploy (size M)

### Community 7 - "Who can write what (audit 2026-11-04)"
Cohesion: 0.40
Nodes (4): Decision taken by default (say if you want it changed), RPCs (functions an employee can call), Tables, Who can write what (audit 2026-11-04)

## Knowledge Gaps
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `LevelUp VFX CRM → ClickUp-style Work OS: Upgrade Plan` connect `LevelUp VFX CRM → ClickUp-style Work OS: Upgrade Plan` to `4. Roadmap`?**
  _High betweenness centrality (0.025) - this node is a cross-community bridge._