# Skills Registry

Verdict = SkillSpector score/verdict + manual review. Route: `plugin` (claude plugin), `skills-cli` (npx skills -g), `copy` (~/.claude/skills), `mcp` (claude mcp add), `tool` (system/CLI).

| Skill / tool | Phase | Source repo | Commit | Route | Scan | Manual review | Installed | Notes |
|---|---|---|---|---|---|---|---|---|
| find-skills | pre | vercel-labs/skills | n/a | copy | not scanned | n/a | yes (before 2026-11-03) | already present |
| uv, FFmpeg 9.0.2, yt-dlp 2026.10.26, Deno 2.9.8 | 0 | winget | n/a | tool | n/a (official packages) | n/a | yes 2026-11-03 | user scope |
| SkillSpector 2.12.0 (+MCP) | 0 | NVIDIA/SkillSpector | e14c450 | tool (uv) + mcp (user) | n/a (the scanner) | hatchling build, no install hooks | yes 2026-11-03 | LLM stage off: claude CLI not signed in |
| watch (/watch) 0.3.2 | 0 | bradautomates/claude-video | 03ceb42 | plugin | 100/100 static, DO NOT INSTALL | SAFE: all HIGH = expected capabilities (yt-dlp download, own API keys, optional Gemini upload, local whisperx env). SessionStart hook = advisory setup check only | yes 2026-11-03 | `setup.py --json` = ready; captions only until WhisperX or a Groq/OpenAI key |
| Council | 1 | danielmiessler/Personal_AI_Infrastructure (LifeOS/install/skills/Council) | b7efec9 | copy | 0/100 SAFE | SAFE: markdown only, no scripts/hooks. Cross-vendor lane needs LifeOS Inference.ts + codex (not installed) | yes 2026-11-03 | Added standalone note: run members as Agent subagents (Anthropic only) |
| RedTeam | 1 | danielmiessler/Personal_AI_Infrastructure (LifeOS/install/skills/RedTeam) | b7efec9 | copy | 17/100 SAFE | SAFE: markdown only; 1 HIGH PE3 = example text about auth design (AdversarialValidation.md:47) | yes 2026-11-03 | Same standalone note; world models saved under ~/.claude/LIFEOS/MEMORY when used |
| ponytail 5.3.3 | 1 | DietrichGebert/ponytail | 96608e0 | plugin (ponytail@ponytail) | 0/100 SAFE (all 6 skills) | SAFE: hooks (SessionStart/SubagentStart/UserPromptSubmit) run local node scripts: inject rules, git ls-files map, mode flag. Band ledger writes local CSV in ~/.config/ponytail. Webhook opt-in, empty by default: nothing leaves PC. Star count not checked further: code is clean | yes 2026-11-03 | Always-on in every chat; '/ponytail off' or 'normal mode' to stop. Installed commit = scanned commit |
| unslop | 1 | cursor/plugins (pstack/skills/unslop) | ae5650f | copy | 0/100 SAFE | SAFE: one SKILL.md, no code | yes 2026-11-03 | disable-model-invocation: call it as /unslop |
| frontend-design 1.1.1 | 1 | anthropics/claude-plugins-official (plugins/frontend-design) | a7ba5b9 | plugin (frontend-design@anthropic-plugin-directory) | 13/100 SAFE | SAFE: one SKILL.md; 1 HIGH AR2 = UX writing advice (false positive) | yes 2026-11-03 | Anthropic-reviewed commit = scanned commit |
| superpowers 7.0.1 | 1 | obra/superpowers (via obra/superpowers-marketplace) | 2ce8aa1 | plugin (superpowers@superpowers-marketplace) | 0-100/100 static per skill (writing-skills 100, systematic-debugging 77, brainstorming 52) | SAFE: all HIGH = docs/examples (git clean warnings, macOS keychain debug example, skills that edit skills = their purpose). SessionStart hook only injects using-superpowers SKILL.md. Brainstorm server is local; only 'telemetry' = remote logo image | yes 2026-11-03 | SUPERPOWERS_DISABLE_TELEMETRY=1 set in ~/.claude/settings.json env. Installed commit = scanned |
| gsap-skills 1.0.0 (8 skills) | 2 | greensock/gsap-skills | aed9cfd | plugin (gsap-skills@gsap-skills) | 0-17/100 SAFE | SAFE: markdown only; 1 HIGH PE3 = advice NOT to use auth tokens (false positive) | yes 2026-11-03 | Installed commit = scanned |
| shadcn | 2 | shadcn-ui/ui (skills/shadcn) | 4aaea19 | copy | 100/100 static | SAFE: docs for the shadcn CLI/MCP (flags = CLI flags, mcp config docs, chat UI examples); 1 local helper script (fs only) | yes 2026-11-03 | Runs 'npx shadcn@latest' in projects when used |
| react-best-practices | 2 | vercel-labs/agent-skills | 1a2c79d | copy | 59/100 | SAFE: markdown rules; HIGH OH1 = dangerouslySetInnerHTML code examples | yes 2026-11-03 | |
| web-design-guidelines | 2 | vercel-labs/agent-skills | 1a2c79d | copy | 0/100 SAFE | SAFE, note: fetches its rules at run time from raw.githubusercontent.com/vercel-labs/web-interface-guidelines (content can change after this review) | yes 2026-11-03 | |
| playwright (MCP) | 2 | anthropics/claude-plugins-official (external_plugins/playwright) | 7d7dbbd (Anthropic-reviewed) | plugin (playwright@anthropic-plugin-directory) | n/a (no skill files; .mcp.json only) | SAFE: runs Microsoft's npx @playwright/mcp@latest locally | yes 2026-11-03 | Unpinned @latest: npm fetches newest on start |
| context7 (MCP) | 2 | anthropics/claude-plugins-official (external_plugins/context7) | a7ba5b9 | plugin (context7@anthropic-plugin-directory) | n/a (.mcp.json only) | SAFE: remote HTTP MCP https://mcp.context7.com (docs lookup); library names you query are sent to Upstash | yes 2026-11-03 | Free without key (rate-limited); key optional later |

## Queue (approved, waiting to install)
_Skill Scout appends here while the Build session is running._

## Blocked / skipped
| Item | Why |
|---|---|
| Caveman | User chose skip (terse style clashes with step-by-step rule) |
| Full LifeOS / PAI | curl\|bash + rewrites ~/.claude hooks/settings; only Council + RedTeam extracted |
| taste-skill | 30-45 min + very high tokens per build |
| fal-ai-community/skills | curl\|bash / irm\|iex install, telemetry, certificate warning |
| AgriciDaniel/banana-claude | No native Windows |
| addyosmani/agent-skills, mattpocock/skills | Overlap with Superpowers |
| Blender MCP | Runs arbitrary code, telemetry on by default; add later only if user wants Blender |
