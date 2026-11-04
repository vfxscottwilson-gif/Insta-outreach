# Build session (Phases 1-4) — working notes

- Helper scripts (scratchpad, not in repo): gate.ps1 (clone + per-skill SkillSpector scan -> scans/<owner>__<repo>.md), findings.py (lists HIGH/CRITICAL), log.sh (registry row + PROGRESS + commit).
- Skill-only repos installed by copying the *scanned* folder into ~/.claude/skills (installed = scanned commit). Plugins installed via bundled claude.exe; installed gitCommitSha checked against scanned commit.
- Telemetry opt-outs set in ~/.claude/settings.json env: SUPERPOWERS_DISABLE_TELEMETRY, HYPERFRAMES_NO_TELEMETRY, CHROME_DEVTOOLS_MCP_NO_USAGE_STATISTICS.
- hyperframes marketplace clone times out at 120s (repo is large): use CLAUDE_CODE_PLUGIN_GIT_TIMEOUT_MS=600000.
- CAUTION (ask user): pbakaus/impeccable (hooks run downloaded prebuilt binary on every edit), D4Vinci/Scrapling (built to bypass anti-bot/Cloudflare).
- n8n-skills: copied as skills only; plugin hooks only matter once n8n-mcp (keyed) is added.
