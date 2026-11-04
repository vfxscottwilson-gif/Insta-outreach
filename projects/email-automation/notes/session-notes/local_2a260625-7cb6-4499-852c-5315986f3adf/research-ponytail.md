# Research: "Ponytail" / concise-answer tools for Claude Code
Checked 2026-11-03. Read-only: nothing installed, downloaded or run. Files were read via WebFetch (a small model summarises each raw file), so the "audits" below are summaries of the raw files, not my own line-by-line reading.

## Verdict
- "Ponytail" is REAL: github.com/DietrichGebert/ponytail. But it makes Claude write LESS CODE ("laziest senior dev"), it does NOT shorten chat answers.
- The tool that matches "short answers, fewer tokens" is **caveman** (JuliusBrussee/caveman). Likely the user mixed the two up (both viral, both "lazy/minimal" skills).
- Best choice for the stated goal: Claude Code's **built-in Concise output style** (no install, official, free).

## Facts (GitHub API, 2026-11-03)
| | ponytail | caveman | claude-token-efficient |
|---|---|---|---|
| Repo | DietrichGebert/ponytail | JuliusBrussee/caveman | drona23/claude-token-efficient |
| Stars | 183,326 | 117,079 | 6,141 |
| Created | 2026-06-12 | 2026-04-04 | 2026-03-30 |
| Last push | 2026-10-29 | 2026-11-03 | 2026-06-16 |
| Licence | MIT | Apache-2.0 (LICENSE-MIT also present) | MIT |
| Archived | no | no | no |

Star counts quoted by third-party blogs (54k, 128k) were stale/inconsistent; the API numbers above are the only ones I trust.

## Ponytail (what it really is)
- Plugin v5.3.3 (plugin.json). Adds SKILL.md ruleset: reuse code/stdlib first, smallest diff, end each reply with a short "what I skipped" note. README does not claim shorter prose.
- Claude Code install: `/plugin marketplace add DietrichGebert/ponytail` then `/plugin install ponytail@ponytail`.
- Hooks (3, all `node -e require(...)`): SessionStart, SubagentStart, UserPromptSubmit -> hooks/ponytail-activate.js, ponytail-subagent.js, ponytail-mode-tracker.js.
  - activate.js: no network, no eval; runs `execFileSync(node, ponytail-map.js)` (3 s, no shell); writes `.ponytail-active` flag + copies a statusline script into ~/.claude; injects text telling the model to offer editing settings.json (statusLine).
  - mode-tracker.js: no network; detached `spawn(node, band-import.js)` only for `/ponytail band import`.
- "Band" (Claude Code >= 2.1.290) = status band + local board; writes CSV ledgers + board.html under `~/.config/ponytail/band/`. register.tsx spawns git, grep, uname, open/xdg-open.
- Optional webhook: plugin.json userConfig `webhookUrl` (default empty) + `webhookToken` (keychain). Only when URL is set does register.tsx do `$.http.fetch(...)` with the task row (cost, tokens, names unless sendNames=false). Default = nothing leaves the machine. board.ts: no server, no network.
- NOT read: hooks/ponytail-runtime.js, ponytail-config.js, ponytail-band-import.js, hooks/band/metrics.ts, logo.ts (49 KB), pi-extension, .opencode, __init__.py.
- Web-search summary said "README recommends running with caveman". README read directly does NOT mention caveman -> treat as unverified/likely wrong.

## Caveman
- Plugin v4.0.1. plugin.json declares ONLY 4 hooks (no mcpServers/agents/userConfig/statusLine): SessionStart + SubagentStart -> src/hooks/caveman-activate.js, UserPromptSubmit -> caveman-mode-tracker.js, SessionEnd -> caveman-stats.js --record.
- Audited (summaries): activate.js no network/no eval, writes `.caveman-active` etc. in ~/.claude, reads settings.json but does not modify; mode-tracker.js no network, one execFileSync of caveman-stats.js; stats.js no network, no child_process, writes `.caveman-history.jsonl` (reads session transcripts under ~/.claude/projects).
- Skill (skills/caveman/SKILL.md): drops greetings/hedging/filler/articles; keeps code, paths, errors, negations; falls back to plain prose for security warnings, irreversible actions, step sequences, confused user, anything saved outside chat.
- Install (Claude Code plugin path, recommended if used): `claude plugin marketplace add JuliusBrussee/caveman` then `claude plugin install caveman@caveman`.
- AVOID: `npx @caveman-ai/cli@latest` (CLI telemetry ON by default: content-free events stored with IP; off via `caveman telemetry off` or DO_NOT_TRACK=1; routing commands can set ANTHROPIC_BASE_URL), and `install.sh`/`install.ps1` (pipe-to-shell; merges hooks + statusline into settings.json with .bak). INSTALL.md says the installer itself sends no telemetry and checks files against a SHA-256 list.
- Repo is huge (proxy, engine, supabase, go.mod, Dockerfile, extension, mcp...). Plugin install only uses the hooks, but the surface is big. NOT read: caveman-config.js, cavecrew-model-overrides.js, proxy/, mcp/, supabase/, installer/.
- Savings: vendor claims ~65-75% fewer OUTPUT tokens. Independent: Implicator.ai measured 12-23%; another blog said 15-25%. Thinking tokens untouched. Output is a small share of a session bill, so real saving on the total is small.

## Built-in alternatives
1. **Concise output style** (Claude Code >= v2.1.237, 2026-08-19). Sources: docs code.claude.com/docs/en/output-styles, official What's New wk34 page, third-party (classmethod.jp, wmedia.es). Leads with result, no preamble/narration/recap, simple answers in 1-3 sentences; error output, security warnings, destructive-action confirmations stay full; full answers when asked. Applies to main chat and forks, NOT to other subagents.
   - Enable: `/output-style concise`, or `/config` -> Output style, or `"outputStyle": "Concise"` in ~/.claude/settings.json (value is CASE-SENSITIVE; "concise" in a settings file silently gives Default). Desktop app: use the settings-file route (its /config opens app Settings instead of the menu). Takes effect on next message (v2.1.251+) or after /clear.
   - ~/.claude/settings*.json currently has no `outputStyle` key (grep, 2026-11-03). Installed Claude Code version NOT checked (changelog top = 2.1.317).
2. **Custom output style**: markdown file in `~/.claude/output-styles/NAME.md` with frontmatter (`name`, `description`, `keep-coding-instructions: true`). Not applied to subagents. Need restart to pick up edits.
3. **CLAUDE.md rules**: always loaded, cheapest, survives style changes. Example repo: drona23/claude-token-efficient = 11-line CLAUDE.md (read raw: terse output, no sycophancy, no emojis/em-dashes, read before write, don't guess APIs). No commands/URLs. Safe.
- Not verified: "Communicating Concisely" skill on claudskills.com (registry listing, no repo found), so excluded.

## Unverified / limits
- Installed Claude Code version on the user's PC.
- Real token saving on the user's workload (no benchmark run).
- Caveman "Auto routing" is opt-in, needs sign-in; pricing/paywall NOT checked (not needed).
- Files not read are listed per tool above. WebFetch summaries are model-generated; for a real install, skim hooks/*.js and plugin.json yourself first.
