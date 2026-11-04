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
| `projects/` | One self-contained folder per app (`README.md` = the standard, `APPS-STANDARD.md` = session rules, `_TEMPLATE/` = skeleton: SETUP-GUIDE, GUIDE, INSTALL.cmd, secrets/, backups) |

## Safety gate (every repo, no exceptions)
1. `git clone` into `repos/<owner>__<repo>` and note the commit hash.
2. `skillspector scan repos/<owner>__<repo>` → save output to `scans/`.
3. Read SKILL.md, every script, hook and `.mcp.json` by hand.
4. SAFE → install globally. CAUTION → ask the user. DO NOT INSTALL → block.
5. Turn telemetry off where possible. Log in `SKILLS-REGISTRY.md`, commit.

**Reading the scan:** the static scan gives 100/100 "DO NOT INSTALL" to almost any skill that uses the network, files or subprocesses (even `/watch`). The score alone decides nothing. Open every HIGH/CRITICAL finding at its file:line and classify it:
- **Expected capability** (downloads what the skill is for, reads its *own* API key, calls its own documented API, runs ffmpeg/node) → fine.
- **Red flag** → CAUTION/BLOCK: sends data to undocumented hosts, reads other secrets (~/.ssh, browser stores, all env vars sent out), obfuscated/encoded code, `curl|bash` / `irm|iex` at runtime, hidden instructions in SKILL.md that tell Claude to ignore the user, hooks that do more than they claim.

**SkillSpector on Windows:** no `--output`; redirect stdout instead. Use `--no-llm` until the Claude CLI is signed in.
```powershell
$env:Path = [Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [Environment]::GetEnvironmentVariable('Path','User')
$env:PYTHONIOENCODING = 'utf-8'
skillspector scan "F:\Github Repos\repos\<owner>__<repo>\<skill dir>" --no-llm --format markdown 2>$null | Out-File -Encoding utf8 "F:\Github Repos\scans\<owner>__<repo>.md"
```

## How to run
- Bundled Claude CLI (for plugin installs): `C:\Users\Khizar Malik\AppData\Roaming\Claude\claude-code\2.1.309\9078b9c1d466\claude.exe` (path changes when the app updates: find it under `%APPDATA%\Claude\claude-code\`).
- Plugins: `claude.exe plugin marketplace add <owner/repo>` then `claude.exe plugin install <name>@<marketplace>` (user scope).
- Skills CLI: `npx skills add <owner/repo> -g --agent claude-code -y` with `DISABLE_TELEMETRY=1`.

## Secrets
None yet. API keys (Firecrawl, Apify, Gemini, n8n) go only in `.env` (gitignored), added later when needed.

## Status / next step
- 2026-11-03: Plan approved (all phases; Council + RedTeam only; no Caveman; free tools now, keyed tools later). Config backed up.
- 2026-11-03: Phase 0 done: uv, FFmpeg, yt-dlp, Deno, SkillSpector (+MCP), /watch installed and checked. Next: Build session runs Phases 1-4; Skill Scout session takes the user's links.
- 2026-11-04: Phases 1-4 done: impeccable + Scrapling installed and verified. Open: context7 and supabase MCP need /mcp sign-in; skillspector MCP times out on connect (CLI works). Keyed tools still waiting for keys.
