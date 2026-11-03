# Scans for pbakaus/impeccable @ 9fadc41


<!-- ===== plugin\skills\impeccable ===== -->
# SkillSpector Security Report

**Skill:** impeccable  
**Source:** `F:\Github Repos\repos\pbakaus__impeccable\plugin\skills\impeccable`  
**Scanned:** 2026-11-03 15:14:55 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 100/100 |
| Severity | CRITICAL |
| Recommendation | DO NOT INSTALL |

## Components (58)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `SKILL.md` | markdown | 88 | No |
| `reference/adapt.md` | markdown | 318 | No |
| `reference/adapt.native.md` | markdown | 58 | No |
| `reference/android.md` | markdown | 46 | No |
| `reference/animate.md` | markdown | 89 | No |
| `reference/audit.md` | markdown | 139 | No |
| `reference/audit.native.md` | markdown | 139 | No |
| `reference/bolder.md` | markdown | 33 | No |
| `reference/clarify.md` | markdown | 94 | No |
| `reference/colorize.md` | markdown | 86 | No |
| `reference/component-review.md` | markdown | 63 | No |
| `reference/craft-floor.md` | markdown | 44 | No |
| `reference/craft.md` | markdown | 5 | No |
| `reference/critique.md` | markdown | 819 | No |
| `reference/degraded/asset-producer.md` | markdown | 42 | No |
| `reference/degraded/documenter.md` | markdown | 24 | No |
| `reference/degraded/finish-reviewer.md` | markdown | 38 | No |
| `reference/degraded/manual-edit-applier.md` | markdown | 93 | No |
| `reference/delight.md` | markdown | 70 | No |
| `reference/distill.md` | markdown | 111 | No |
| `reference/doctor.md` | markdown | 54 | No |
| `reference/document.md` | markdown | 416 | No |
| `reference/extract.md` | markdown | 69 | No |
| `reference/generate.md` | markdown | 101 | No |
| `reference/harden.md` | markdown | 362 | No |
| `reference/hooks.md` | markdown | 114 | No |
| `reference/init.md` | markdown | 131 | No |
| `reference/ios.md` | markdown | 51 | No |
| `reference/layout.md` | markdown | 84 | No |
| `reference/live-setup.md` | markdown | 104 | No |
| `reference/live.md` | markdown | 327 | No |
| `reference/mode-operate.md` | markdown | 21 | No |
| `reference/mode-persuade.md` | markdown | 19 | No |
| `reference/mode-read.md` | markdown | 21 | No |
| `reference/new-work.md` | markdown | 154 | No |
| `reference/onboard.md` | markdown | 234 | No |
| `reference/operate.md` | markdown | 61 | No |
| `reference/optimize.md` | markdown | 257 | No |
| `reference/overdrive.md` | markdown | 127 | No |
| `reference/polish.md` | markdown | 105 | No |
| `reference/quieter.md` | markdown | 99 | No |
| `reference/region-map.md` | markdown | 26 | No |
| `reference/routing.md` | markdown | 24 | No |
| `reference/shape.md` | markdown | 59 | No |
| `reference/typeset.md` | markdown | 90 | No |
| `reference/visualize.md` | markdown | 47 | No |
| `scripts/VERSION` | other | 1 | No |
| `scripts/command-metadata.json` | json | 98 | No |
| `scripts/data/font-index-failures.json` | json | 121 | No |
| `scripts/data/font-index.json` | json | 1 | No |
| `scripts/engine-checksums.txt` | text | 9 | No |
| `scripts/impeccable` | other | 266 | Yes |
| `scripts/impeccable.cmd` | other | 306 | Yes |
| `scripts/live-browser-dom.js` | javascript | 320 | Yes |
| `scripts/live-browser-ignores.js` | javascript | 246 | Yes |
| `scripts/live-browser-session.js` | javascript | 183 | Yes |
| `scripts/live-browser.js` | javascript | 13862 | Yes |
| `scripts/modern-screenshot.umd.js` | javascript | 14 | Yes |

## Issues (45)

### 🔴 HIGH: AE1

**Location:** `SKILL.md:58`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `reference/harden.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:69`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `reference/live.md`

---

### 🔴 HIGH: MP3

**Location:** `reference/colorize.md:23`  
**Confidence:** 80%  

**Message:** Memory Manipulation

**Remediation:** Protect agent memory and state from modification by untrusted content\. Use read\-only memory for critical instructions and validate all state changes\.

---

### 🔴 HIGH: AR2

**Location:** `reference/critique.md:256`  
**Confidence:** 85%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `reference/degraded/finish-reviewer.md:10`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AS1

**Location:** `reference/hooks.md:17`  
**Confidence:** 90%  

**Message:** Agent Config Directory Access

**Remediation:** Remove all code or instructions that access agent configuration directories \(\.claude/, \.codex/, \.gemini/\)\. If configuration values are needed, pass them explicitly as parameters or environment variables — never read the agent's own config files\.

---

### 🔴 HIGH: AS1

**Location:** `reference/hooks.md:109`  
**Confidence:** 90%  

**Message:** Agent Config Directory Access

**Remediation:** Remove all code or instructions that access agent configuration directories \(\.claude/, \.codex/, \.gemini/\)\. If configuration values are needed, pass them explicitly as parameters or environment variables — never read the agent's own config files\.

---

### 🔴 HIGH: MP3

**Location:** `reference/mode-operate.md:15`  
**Confidence:** 80%  

**Message:** Memory Manipulation

**Remediation:** Protect agent memory and state from modification by untrusted content\. Use read\-only memory for critical instructions and validate all state changes\.

---

### 🔴 HIGH: AR2

**Location:** `reference/new-work.md:138`  
**Confidence:** 85%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: TM1

**Location:** `scripts/live-browser.js:8372`  
**Confidence:** 90%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🟡 MEDIUM: LP3

**Location:** `SKILL.md:1`  
**Confidence:** 70%  

**Message:** Skill declares no tool scope \('permissions' or 'allowed\-tools'\) but code capabilities were detected: network, shell\.

**Remediation:** Clarify the skill's intended tool scope and review how the host runtime enforces it; runtime permissions are unknown unless separately verified\. For Claude Code / Agent Skills SKILL\.md, 'allowed\-tools' records preapproved tools, not a permission ceiling; add a tool only when it is independently approved as necessary, not to silence this finding\. For MCP server manifests, use a 'permissions' list naming the required capabilities\.

---

### 🟡 MEDIUM: EA2

**Location:** `reference/audit.md:139`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `reference/audit.native.md:139`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `reference/critique.md:700`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `reference/degraded/finish-reviewer.md:19`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `reference/new-work.md:53`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `reference/visualize.md:31`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `reference/degraded/finish-reviewer.md:20`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `reference/degraded/finish-reviewer.md:20`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `reference/degraded/finish-reviewer.md:34`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `reference/delight.md:55`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: RP1

**Location:** `reference/doctor.md:9`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx impeccable'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `reference/hooks.md:49`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx impeccable'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: EA2

**Location:** `reference/document.md:411`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `reference/new-work.md:55`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `reference/visualize.md:37`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `reference/init.md:112`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `reference/live.md:76`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: MP1

**Location:** `scripts/live-browser.js:1031`  
**Confidence:** 80%  

**Message:** Persistent Context Injection

**Remediation:** Do not allow untrusted input to persist in agent memory or context\. Validate all content before storing and implement memory isolation between sessions\.

---

### 🟡 MEDIUM: SSRF2

**Location:** `scripts/live-browser.js:3947`  
**Confidence:** 70%  

**Message:** Internal Network Request

**Remediation:** Avoid requests to loopback/link\-local/private hosts from skill code\. If internal access is intended, document it and validate the target against an allowlist\.

---

### 🟡 MEDIUM: SSRF2

**Location:** `scripts/live-browser.js:4059`  
**Confidence:** 70%  

**Message:** Internal Network Request

**Remediation:** Avoid requests to loopback/link\-local/private hosts from skill code\. If internal access is intended, document it and validate the target against an allowlist\.

---

### 🟡 MEDIUM: SSRF2

**Location:** `scripts/live-browser.js:7431`  
**Confidence:** 70%  

**Message:** Internal Network Request

**Remediation:** Avoid requests to loopback/link\-local/private hosts from skill code\. If internal access is intended, document it and validate the target against an allowlist\.

---

### 🟡 MEDIUM: SSRF2

**Location:** `scripts/live-browser.js:7553`  
**Confidence:** 70%  

**Message:** Internal Network Request

**Remediation:** Avoid requests to loopback/link\-local/private hosts from skill code\. If internal access is intended, document it and validate the target against an allowlist\.

---

### 🟡 MEDIUM: SSRF2

**Location:** `scripts/live-browser.js:8078`  
**Confidence:** 70%  

**Message:** Internal Network Request

**Remediation:** Avoid requests to loopback/link\-local/private hosts from skill code\. If internal access is intended, document it and validate the target against an allowlist\.

---

### 🟡 MEDIUM: SSRF2

**Location:** `scripts/live-browser.js:11885`  
**Confidence:** 70%  

**Message:** Internal Network Request

**Remediation:** Avoid requests to loopback/link\-local/private hosts from skill code\. If internal access is intended, document it and validate the target against an allowlist\.

---

### 🟡 MEDIUM: SSRF2

**Location:** `scripts/live-browser.js:11897`  
**Confidence:** 70%  

**Message:** Internal Network Request

**Remediation:** Avoid requests to loopback/link\-local/private hosts from skill code\. If internal access is intended, document it and validate the target against an allowlist\.

---

### 🟡 MEDIUM: SSRF2

**Location:** `scripts/live-browser.js:3982`  
**Confidence:** 70%  

**Message:** Internal Network Request

**Remediation:** Avoid requests to loopback/link\-local/private hosts from skill code\. If internal access is intended, document it and validate the target against an allowlist\.

---

### 🟡 MEDIUM: SSRF2

**Location:** `scripts/live-browser.js:4375`  
**Confidence:** 70%  

**Message:** Internal Network Request

**Remediation:** Avoid requests to loopback/link\-local/private hosts from skill code\. If internal access is intended, document it and validate the target against an allowlist\.

---

### 🟡 MEDIUM: SSRF2

**Location:** `scripts/live-browser.js:4395`  
**Confidence:** 70%  

**Message:** Internal Network Request

**Remediation:** Avoid requests to loopback/link\-local/private hosts from skill code\. If internal access is intended, document it and validate the target against an allowlist\.

---

### 🟡 MEDIUM: SSRF2

**Location:** `scripts/live-browser.js:4439`  
**Confidence:** 70%  

**Message:** Internal Network Request

**Remediation:** Avoid requests to loopback/link\-local/private hosts from skill code\. If internal access is intended, document it and validate the target against an allowlist\.

---

### 🟡 MEDIUM: SSRF2

**Location:** `scripts/live-browser.js:4488`  
**Confidence:** 70%  

**Message:** Internal Network Request

**Remediation:** Avoid requests to loopback/link\-local/private hosts from skill code\. If internal access is intended, document it and validate the target against an allowlist\.

---

### 🟡 MEDIUM: SSRF2

**Location:** `scripts/live-browser.js:4507`  
**Confidence:** 70%  

**Message:** Internal Network Request

**Remediation:** Avoid requests to loopback/link\-local/private hosts from skill code\. If internal access is intended, document it and validate the target against an allowlist\.

---

### 🟡 MEDIUM: SSRF2

**Location:** `scripts/live-browser.js:9026`  
**Confidence:** 70%  

**Message:** Internal Network Request

**Remediation:** Avoid requests to loopback/link\-local/private hosts from skill code\. If internal access is intended, document it and validate the target against an allowlist\.

---

### 🟡 MEDIUM: E1

**Location:** `scripts/live-browser.js:7431`  
**Confidence:** 70%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `scripts/live-browser.js:7553`  
**Confidence:** 70%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | partial |
| Dependency contents | not\_requested |
| Coverage | 86\.2% |
| Fully inspected | 50 |
| Partially inspected | 8 |
| Entirely uninspected | 0 |

### Ledger Exceptions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| static\_parse\_limit | `reference/harden.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| static\_parse\_limit | `reference/live-setup.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| static\_parse\_limit | `reference/live.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| static\_parse\_limit | `scripts/data/font-index.json` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| static\_parse\_limit | `scripts/impeccable.cmd` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| static\_parse\_limit | `scripts/live-browser-ignores.js` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| obfuscated\_instruction\_text | `scripts/live-browser.js` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |
| static\_parse\_limit | `scripts/live-browser.js` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| obfuscated\_instruction\_text | `scripts/modern-screenshot.umd.js` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |
| static\_parse\_limit | `scripts/modern-screenshot.umd.js` | A security\-relevant expression exceeded a bounded static parser's span limit\. |

### Analyzer Statuses

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| completed | `artifact_integrity` |  |
| no\_applicable\_files | `behavioral_ast` | No files matched this analyzer's applicability contract\. |
| no\_applicable\_files | `behavioral_taint_tracking` | No files matched this analyzer's applicability contract\. |
| no\_applicable\_files | `bundled_execution_surface` | No files matched this analyzer's applicability contract\. |
| completed | `mcp_least_privilege` |  |
| completed | `mcp_rug_pull` |  |
| completed | `mcp_tool_poisoning` |  |
| disabled\_by\_configuration | `meta_analyzer` | Analyzer was disabled by the requested configuration\. |
| completed | `reference_coverage` |  |
| disabled\_by\_configuration | `semantic_developer_intent` | Analyzer was disabled by the requested configuration\. |
| disabled\_by\_configuration | `semantic_quality_policy` | Analyzer was disabled by the requested configuration\. |
| disabled\_by\_configuration | `semantic_security_discovery` | Analyzer was disabled by the requested configuration\. |
| degraded | `static_patterns_agent_snooping` |  |
| degraded | `static_patterns_anti_refusal` |  |
| completed | `static_patterns_data_exfiltration` |  |
| degraded | `static_patterns_deserialization` |  |
| degraded | `static_patterns_excessive_agency` |  |
| degraded | `static_patterns_harmful_content` |  |
| degraded | `static_patterns_memory_poisoning` |  |
| completed | `static_patterns_output_handling` |  |
| degraded | `static_patterns_privilege_escalation` |  |
| degraded | `static_patterns_prompt_injection` |  |
| degraded | `static_patterns_rogue_agent` |  |
| degraded | `static_patterns_ssrf` |  |
| degraded | `static_patterns_supply_chain` |  |
| degraded | `static_patterns_system_prompt_leakage` |  |
| degraded | `static_patterns_tool_misuse` |  |
| completed | `static_yara` |  |

### Limitations

- Analyzer static\_patterns\_agent\_snooping status: degraded\.
- Analyzer static\_patterns\_anti\_refusal status: degraded\.
- Analyzer static\_patterns\_deserialization status: degraded\.
- Analyzer static\_patterns\_excessive\_agency status: degraded\.
- Analyzer static\_patterns\_harmful\_content status: degraded\.
- Analyzer static\_patterns\_memory\_poisoning status: degraded\.
- Analyzer static\_patterns\_privilege\_escalation status: degraded\.
- Analyzer static\_patterns\_prompt\_injection status: degraded\.
- Analyzer static\_patterns\_rogue\_agent status: degraded\.
- Analyzer static\_patterns\_ssrf status: degraded\.
- Analyzer static\_patterns\_supply\_chain status: degraded\.
- Analyzer static\_patterns\_system\_prompt\_leakage status: degraded\.
- Analyzer static\_patterns\_tool\_misuse status: degraded\.

## Metadata

- **Executable Scripts:** Yes

*Generated by SkillSpector v2.12.0*

