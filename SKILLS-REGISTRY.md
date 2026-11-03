# Skills Registry

Verdict = SkillSpector score/verdict + manual review. Route: `plugin` (claude plugin), `skills-cli` (npx skills -g), `copy` (~/.claude/skills), `mcp` (claude mcp add), `tool` (system/CLI).

| Skill / tool | Phase | Source repo | Commit | Route | Scan | Manual review | Installed | Notes |
|---|---|---|---|---|---|---|---|---|
| find-skills | pre | vercel-labs/skills | n/a | copy | not scanned | n/a | yes (before 2026-11-03) | already present |

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
