# Skills Hub

**Purpose:** Central place for every Claude skill / plugin / MCP repo installed on this PC: source copies, safety scans, and the install registry. Skills are installed **globally** (user scope) so every chat can use them.

**Use cases the toolkit serves:** motion graphics & cartoon animation, graphics, 3D / scroll-linked / animated websites, full-stack apps with working backends, testing, data scrapers, automations & end-to-end pipelines.

## Layout
| Path | What |
|---|---|
| `repos/<owner>__<repo>/` | Cloned source, pinned commit (gitignored) |
| `scans/<owner>__<repo>.txt` | SkillSpector report |
| `SKILLS-REGISTRY.md` | Every skill: source, commit, scan verdict, install route, date |
| `PROGRESS.md` | Workstream tracker |
| `scripts/` | Helper scripts (scan, update) |
| `backups/` | Copy of `~/.claude` config before installs (gitignored) |

## Safety gate (every repo, no exceptions)
1. `git clone` into `repos/<owner>__<repo>` and note the commit hash.
2. `skillspector scan repos/<owner>__<repo>` → save output to `scans/`.
3. Read SKILL.md, every script, hook and `.mcp.json` by hand.
4. SAFE → install globally. CAUTION → ask the user. DO NOT INSTALL → block.
5. Turn telemetry off where possible. Log in `SKILLS-REGISTRY.md`, commit.

## How to run
- Bundled Claude CLI (for plugin installs): `C:\Users\Khizar Malik\AppData\Roaming\Claude\claude-code\2.1.309\9078b9c1d466\claude.exe` (path changes when the app updates: find it under `%APPDATA%\Claude\claude-code\`).
- Plugins: `claude.exe plugin marketplace add <owner/repo>` then `claude.exe plugin install <name>@<marketplace>` (user scope).
- Skills CLI: `npx skills add <owner/repo> -g --agent claude-code -y` with `DISABLE_TELEMETRY=1`.

## Secrets
None yet. API keys (Firecrawl, Apify, Gemini, n8n) go only in `.env` (gitignored), added later when needed.

## Status / next step
- 2026-11-03: Plan approved (all phases; Council + RedTeam only; no Caveman; free tools now, keyed tools later). Config backed up. Next: Phase 0 (uv, FFmpeg, yt-dlp, Deno, SkillSpector, /watch).
