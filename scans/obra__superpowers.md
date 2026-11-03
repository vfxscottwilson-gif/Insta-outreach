# Scans for obra/superpowers @ 2ce8aa1


<!-- ===== skills\brainstorming ===== -->
# SkillSpector Security Report

**Skill:** brainstorming  
**Source:** `F:\Github Repos\repos\obra__superpowers\skills\brainstorming`  
**Scanned:** 2026-11-03 14:48:43 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 52/100 |
| Severity | HIGH |
| Recommendation | DO NOT INSTALL |

## Components (8)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `SKILL.md` | markdown | 294 | No |
| `builder-check-prompt.md` | markdown | 23 | No |
| `scripts/frame-template.html` | other | 213 | No |
| `scripts/helper.js` | javascript | 167 | Yes |
| `scripts/server.cjs` | javascript | 723 | Yes |
| `scripts/start-server.sh` | shell | 209 | Yes |
| `scripts/stop-server.sh` | shell | 120 | Yes |
| `visual-companion.md` | markdown | 299 | No |

## Issues (7)

### 🔴 HIGH: TM1

**Location:** `scripts/stop-server.sh:22`  
**Confidence:** 95%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🟡 MEDIUM: LP3

**Location:** `SKILL.md:1`  
**Confidence:** 70%  

**Message:** Skill declares no tool scope \('permissions' or 'allowed\-tools'\) but code capabilities were detected: env, network, shell\.

**Remediation:** Clarify the skill's intended tool scope and review how the host runtime enforces it; runtime permissions are unknown unless separately verified\. For Claude Code / Agent Skills SKILL\.md, 'allowed\-tools' records preapproved tools, not a permission ceiling; add a tool only when it is independently approved as necessary, not to silence this finding\. For MCP server manifests, use a 'permissions' list naming the required capabilities\.

---

### 🟡 MEDIUM: RA2

**Location:** `scripts/start-server.sh:102`  
**Confidence:** 65%  

**Message:** Session Persistence

**Remediation:** Remove any persistence mechanisms \(cron jobs, startup scripts, state files\)\. Skills should not maintain state across sessions without explicit user consent\.

---

### 🟡 MEDIUM: RA2

**Location:** `scripts/start-server.sh:179`  
**Confidence:** 65%  

**Message:** Session Persistence

**Remediation:** Remove any persistence mechanisms \(cron jobs, startup scripts, state files\)\. Skills should not maintain state across sessions without explicit user consent\.

---

### 🟡 MEDIUM: RA2

**Location:** `scripts/start-server.sh:180`  
**Confidence:** 65%  

**Message:** Session Persistence

**Remediation:** Remove any persistence mechanisms \(cron jobs, startup scripts, state files\)\. Skills should not maintain state across sessions without explicit user consent\.

---

### 🟡 MEDIUM: RA2

**Location:** `scripts/start-server.sh:179`  
**Confidence:** 65%  

**Message:** Session Persistence

**Remediation:** Remove any persistence mechanisms \(cron jobs, startup scripts, state files\)\. Skills should not maintain state across sessions without explicit user consent\.

---

### 🟡 MEDIUM: RA2

**Location:** `scripts/start-server.sh:182`  
**Confidence:** 65%  

**Message:** Session Persistence

**Remediation:** Remove any persistence mechanisms \(cron jobs, startup scripts, state files\)\. Skills should not maintain state across sessions without explicit user consent\.

---

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | partial |
| Dependency contents | not\_requested |
| Coverage | 87\.5% |
| Fully inspected | 7 |
| Partially inspected | 1 |
| Entirely uninspected | 0 |

### Ledger Exceptions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| static\_parse\_limit | `scripts/server.cjs` | A security\-relevant expression exceeded a bounded static parser's span limit\. |

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
| disabled\_by\_configuration | `semantic_developer_intent` | Analyzer was disabled by the requested configuration\. |
| disabled\_by\_configuration | `semantic_quality_policy` | Analyzer was disabled by the requested configuration\. |
| disabled\_by\_configuration | `semantic_security_discovery` | Analyzer was disabled by the requested configuration\. |
| completed | `static_patterns_agent_snooping` |  |
| completed | `static_patterns_anti_refusal` |  |
| completed | `static_patterns_data_exfiltration` |  |
| completed | `static_patterns_deserialization` |  |
| completed | `static_patterns_excessive_agency` |  |
| completed | `static_patterns_harmful_content` |  |
| completed | `static_patterns_memory_poisoning` |  |
| completed | `static_patterns_output_handling` |  |
| completed | `static_patterns_privilege_escalation` |  |
| completed | `static_patterns_prompt_injection` |  |
| completed | `static_patterns_rogue_agent` |  |
| completed | `static_patterns_ssrf` |  |
| completed | `static_patterns_supply_chain` |  |
| completed | `static_patterns_system_prompt_leakage` |  |
| degraded | `static_patterns_tool_misuse` |  |
| completed | `static_yara` |  |

### Limitations

- Analyzer static\_patterns\_tool\_misuse status: degraded\.

## Metadata

- **Executable Scripts:** Yes

*Generated by SkillSpector v2.12.0*


<!-- ===== skills\diagnosing-superpowers ===== -->
# SkillSpector Security Report

**Skill:** diagnosing\-superpowers  
**Source:** `F:\Github Repos\repos\obra__superpowers\skills\diagnosing-superpowers`  
**Scanned:** 2026-11-03 14:49:14 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 26/100 |
| Severity | MEDIUM |
| Recommendation | CAUTION |

## Components (20)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `SKILL.md` | markdown | 120 | No |
| `prompts/analyst-common.md` | markdown | 38 | No |
| `prompts/cost-and-time.md` | markdown | 28 | No |
| `prompts/plan-adherence.md` | markdown | 29 | No |
| `prompts/quality-evidence.md` | markdown | 26 | No |
| `prompts/repeated-work.md` | markdown | 30 | No |
| `prompts/request-conflicts.md` | markdown | 20 | No |
| `prompts/scrub-audit.md` | markdown | 33 | No |
| `prompts/scrub.md` | markdown | 29 | No |
| `prompts/similar-session.md` | markdown | 38 | No |
| `prompts/skill-timeline.md` | markdown | 30 | No |
| `prompts/stumbles.md` | markdown | 28 | No |
| `references/context-safety.md` | markdown | 22 | No |
| `references/github-issues.md` | markdown | 47 | No |
| `references/redaction-policy.md` | markdown | 34 | No |
| `references/session-discovery.md` | markdown | 31 | No |
| `templates/bundle-README.md` | markdown | 77 | No |
| `templates/case.md` | markdown | 64 | No |
| `templates/issue.md` | markdown | 70 | No |
| `templates/report.md` | markdown | 82 | No |

## Issues (2)

### 🔴 HIGH: AR2

**Location:** `prompts/request-conflicts.md:19`  
**Confidence:** 85%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🟡 MEDIUM: E1

**Location:** `references/github-issues.md:18`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | complete |
| Dependency contents | not\_requested |
| Coverage | 100\.0% |
| Fully inspected | 20 |
| Partially inspected | 0 |
| Entirely uninspected | 0 |

### Analyzer Statuses

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| completed | `artifact_integrity` |  |
| no\_applicable\_files | `behavioral_ast` | No files matched this analyzer's applicability contract\. |
| no\_applicable\_files | `behavioral_taint_tracking` | No files matched this analyzer's applicability contract\. |
| no\_applicable\_files | `bundled_execution_surface` | No files matched this analyzer's applicability contract\. |
| no\_applicable\_files | `mcp_least_privilege` | No files matched this analyzer's applicability contract\. |
| completed | `mcp_rug_pull` |  |
| completed | `mcp_tool_poisoning` |  |
| disabled\_by\_configuration | `meta_analyzer` | Analyzer was disabled by the requested configuration\. |
| disabled\_by\_configuration | `semantic_developer_intent` | Analyzer was disabled by the requested configuration\. |
| disabled\_by\_configuration | `semantic_quality_policy` | Analyzer was disabled by the requested configuration\. |
| disabled\_by\_configuration | `semantic_security_discovery` | Analyzer was disabled by the requested configuration\. |
| completed | `static_patterns_agent_snooping` |  |
| completed | `static_patterns_anti_refusal` |  |
| completed | `static_patterns_data_exfiltration` |  |
| completed | `static_patterns_deserialization` |  |
| completed | `static_patterns_excessive_agency` |  |
| completed | `static_patterns_harmful_content` |  |
| completed | `static_patterns_memory_poisoning` |  |
| completed | `static_patterns_output_handling` |  |
| completed | `static_patterns_privilege_escalation` |  |
| completed | `static_patterns_prompt_injection` |  |
| completed | `static_patterns_rogue_agent` |  |
| completed | `static_patterns_ssrf` |  |
| completed | `static_patterns_supply_chain` |  |
| completed | `static_patterns_system_prompt_leakage` |  |
| completed | `static_patterns_tool_misuse` |  |
| completed | `static_yara` |  |

## Metadata

- **Executable Scripts:** No

*Generated by SkillSpector v2.12.0*


<!-- ===== skills\dispatching-parallel-agents ===== -->
# SkillSpector Security Report

**Skill:** dispatching\-parallel\-agents  
**Source:** `F:\Github Repos\repos\obra__superpowers\skills\dispatching-parallel-agents`  
**Scanned:** 2026-11-03 14:49:35 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 0/100 |
| Severity | LOW |
| Recommendation | SAFE |

## Components (1)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `SKILL.md` | markdown | 167 | No |

## Issues (0)

No security issues detected.

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | complete\_with\_caveats |
| Dependency contents | not\_requested |
| Coverage | 100\.0% |
| Fully inspected | 1 |
| Partially inspected | 0 |
| Entirely uninspected | 0 |

### Ledger Exceptions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| reference\_missing | `SKILL.md:95-95` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |

### Analyzer Statuses

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| completed | `artifact_integrity` |  |
| no\_applicable\_files | `behavioral_ast` | No files matched this analyzer's applicability contract\. |
| no\_applicable\_files | `behavioral_taint_tracking` | No files matched this analyzer's applicability contract\. |
| no\_applicable\_files | `bundled_execution_surface` | No files matched this analyzer's applicability contract\. |
| no\_applicable\_files | `mcp_least_privilege` | No files matched this analyzer's applicability contract\. |
| completed | `mcp_rug_pull` |  |
| completed | `mcp_tool_poisoning` |  |
| no\_applicable\_files | `meta_analyzer` | No files matched this analyzer's applicability contract\. |
| disabled\_by\_configuration | `semantic_developer_intent` | Analyzer was disabled by the requested configuration\. |
| disabled\_by\_configuration | `semantic_quality_policy` | Analyzer was disabled by the requested configuration\. |
| disabled\_by\_configuration | `semantic_security_discovery` | Analyzer was disabled by the requested configuration\. |
| completed | `static_patterns_agent_snooping` |  |
| completed | `static_patterns_anti_refusal` |  |
| completed | `static_patterns_data_exfiltration` |  |
| completed | `static_patterns_deserialization` |  |
| completed | `static_patterns_excessive_agency` |  |
| completed | `static_patterns_harmful_content` |  |
| completed | `static_patterns_memory_poisoning` |  |
| completed | `static_patterns_output_handling` |  |
| completed | `static_patterns_privilege_escalation` |  |
| completed | `static_patterns_prompt_injection` |  |
| completed | `static_patterns_rogue_agent` |  |
| completed | `static_patterns_ssrf` |  |
| completed | `static_patterns_supply_chain` |  |
| completed | `static_patterns_system_prompt_leakage` |  |
| completed | `static_patterns_tool_misuse` |  |
| completed | `static_yara` |  |

## Metadata

- **Executable Scripts:** No

*Generated by SkillSpector v2.12.0*


<!-- ===== skills\executing-plans ===== -->
# SkillSpector Security Report

**Skill:** executing\-plans  
**Source:** `F:\Github Repos\repos\obra__superpowers\skills\executing-plans`  
**Scanned:** 2026-11-03 14:49:58 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 17/100 |
| Severity | LOW |
| Recommendation | CAUTION |

## Components (3)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `SKILL.md` | markdown | 321 | No |
| `scripts/task-done` | other | 52 | Yes |
| `scripts/task-start` | other | 28 | Yes |

## Issues (1)

### 🔴 HIGH: TM1

**Location:** `SKILL.md:140`  
**Confidence:** 70%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | partial |
| Dependency contents | not\_requested |
| Coverage | 66\.7% |
| Fully inspected | 2 |
| Partially inspected | 1 |
| Entirely uninspected | 0 |

### Ledger Exceptions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| obfuscated\_instruction\_text | `SKILL.md` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |

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


<!-- ===== skills\finishing-a-development-branch ===== -->
# SkillSpector Security Report

**Skill:** finishing\-a\-development\-branch  
**Source:** `F:\Github Repos\repos\obra__superpowers\skills\finishing-a-development-branch`  
**Scanned:** 2026-11-03 14:50:18 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 17/100 |
| Severity | LOW |
| Recommendation | CAUTION |

## Components (1)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `SKILL.md` | markdown | 225 | No |

## Issues (1)

### 🔴 HIGH: TM1

**Location:** `SKILL.md:116`  
**Confidence:** 70%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | partial |
| Dependency contents | not\_requested |
| Coverage | 100\.0% |
| Fully inspected | 1 |
| Partially inspected | 0 |
| Entirely uninspected | 0 |

### Ledger Exceptions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| referenced\_uninspected | `SKILL.md:16-16` | A referenced artifact was not completely inspected\. |

### Analyzer Statuses

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| completed | `artifact_integrity` |  |
| no\_applicable\_files | `behavioral_ast` | No files matched this analyzer's applicability contract\. |
| no\_applicable\_files | `behavioral_taint_tracking` | No files matched this analyzer's applicability contract\. |
| no\_applicable\_files | `bundled_execution_surface` | No files matched this analyzer's applicability contract\. |
| no\_applicable\_files | `mcp_least_privilege` | No files matched this analyzer's applicability contract\. |
| completed | `mcp_rug_pull` |  |
| completed | `mcp_tool_poisoning` |  |
| disabled\_by\_configuration | `meta_analyzer` | Analyzer was disabled by the requested configuration\. |
| disabled\_by\_configuration | `semantic_developer_intent` | Analyzer was disabled by the requested configuration\. |
| disabled\_by\_configuration | `semantic_quality_policy` | Analyzer was disabled by the requested configuration\. |
| disabled\_by\_configuration | `semantic_security_discovery` | Analyzer was disabled by the requested configuration\. |
| completed | `static_patterns_agent_snooping` |  |
| completed | `static_patterns_anti_refusal` |  |
| completed | `static_patterns_data_exfiltration` |  |
| completed | `static_patterns_deserialization` |  |
| completed | `static_patterns_excessive_agency` |  |
| completed | `static_patterns_harmful_content` |  |
| completed | `static_patterns_memory_poisoning` |  |
| completed | `static_patterns_output_handling` |  |
| completed | `static_patterns_privilege_escalation` |  |
| completed | `static_patterns_prompt_injection` |  |
| completed | `static_patterns_rogue_agent` |  |
| completed | `static_patterns_ssrf` |  |
| completed | `static_patterns_supply_chain` |  |
| completed | `static_patterns_system_prompt_leakage` |  |
| completed | `static_patterns_tool_misuse` |  |
| completed | `static_yara` |  |

## Metadata

- **Executable Scripts:** No

*Generated by SkillSpector v2.12.0*


<!-- ===== skills\receiving-code-review ===== -->
# SkillSpector Security Report

**Skill:** receiving\-code\-review  
**Source:** `F:\Github Repos\repos\obra__superpowers\skills\receiving-code-review`  
**Scanned:** 2026-11-03 14:50:40 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 0/100 |
| Severity | LOW |
| Recommendation | SAFE |

## Components (1)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `SKILL.md` | markdown | 205 | No |

## Issues (0)

No security issues detected.

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | complete |
| Dependency contents | not\_requested |
| Coverage | 100\.0% |
| Fully inspected | 1 |
| Partially inspected | 0 |
| Entirely uninspected | 0 |

### Analyzer Statuses

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| completed | `artifact_integrity` |  |
| no\_applicable\_files | `behavioral_ast` | No files matched this analyzer's applicability contract\. |
| no\_applicable\_files | `behavioral_taint_tracking` | No files matched this analyzer's applicability contract\. |
| no\_applicable\_files | `bundled_execution_surface` | No files matched this analyzer's applicability contract\. |
| no\_applicable\_files | `mcp_least_privilege` | No files matched this analyzer's applicability contract\. |
| completed | `mcp_rug_pull` |  |
| completed | `mcp_tool_poisoning` |  |
| no\_applicable\_files | `meta_analyzer` | No files matched this analyzer's applicability contract\. |
| disabled\_by\_configuration | `semantic_developer_intent` | Analyzer was disabled by the requested configuration\. |
| disabled\_by\_configuration | `semantic_quality_policy` | Analyzer was disabled by the requested configuration\. |
| disabled\_by\_configuration | `semantic_security_discovery` | Analyzer was disabled by the requested configuration\. |
| completed | `static_patterns_agent_snooping` |  |
| completed | `static_patterns_anti_refusal` |  |
| completed | `static_patterns_data_exfiltration` |  |
| completed | `static_patterns_deserialization` |  |
| completed | `static_patterns_excessive_agency` |  |
| completed | `static_patterns_harmful_content` |  |
| completed | `static_patterns_memory_poisoning` |  |
| completed | `static_patterns_output_handling` |  |
| completed | `static_patterns_privilege_escalation` |  |
| completed | `static_patterns_prompt_injection` |  |
| completed | `static_patterns_rogue_agent` |  |
| completed | `static_patterns_ssrf` |  |
| completed | `static_patterns_supply_chain` |  |
| completed | `static_patterns_system_prompt_leakage` |  |
| completed | `static_patterns_tool_misuse` |  |
| completed | `static_yara` |  |

## Metadata

- **Executable Scripts:** No

*Generated by SkillSpector v2.12.0*


<!-- ===== skills\requesting-code-review ===== -->
# SkillSpector Security Report

**Skill:** requesting\-code\-review  
**Source:** `F:\Github Repos\repos\obra__superpowers\skills\requesting-code-review`  
**Scanned:** 2026-11-03 14:50:56 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 7/100 |
| Severity | LOW |
| Recommendation | SAFE |

## Components (2)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `SKILL.md` | markdown | 95 | No |
| `code-reviewer.md` | markdown | 198 | No |

## Issues (1)

### 🟡 MEDIUM: EA2

**Location:** `code-reviewer.md:147`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | complete\_with\_caveats |
| Dependency contents | not\_requested |
| Coverage | 100\.0% |
| Fully inspected | 2 |
| Partially inspected | 0 |
| Entirely uninspected | 0 |

### Ledger Exceptions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| reference\_missing | `SKILL.md:60-60` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |

### Analyzer Statuses

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| completed | `artifact_integrity` |  |
| no\_applicable\_files | `behavioral_ast` | No files matched this analyzer's applicability contract\. |
| no\_applicable\_files | `behavioral_taint_tracking` | No files matched this analyzer's applicability contract\. |
| no\_applicable\_files | `bundled_execution_surface` | No files matched this analyzer's applicability contract\. |
| no\_applicable\_files | `mcp_least_privilege` | No files matched this analyzer's applicability contract\. |
| completed | `mcp_rug_pull` |  |
| completed | `mcp_tool_poisoning` |  |
| disabled\_by\_configuration | `meta_analyzer` | Analyzer was disabled by the requested configuration\. |
| disabled\_by\_configuration | `semantic_developer_intent` | Analyzer was disabled by the requested configuration\. |
| disabled\_by\_configuration | `semantic_quality_policy` | Analyzer was disabled by the requested configuration\. |
| disabled\_by\_configuration | `semantic_security_discovery` | Analyzer was disabled by the requested configuration\. |
| completed | `static_patterns_agent_snooping` |  |
| completed | `static_patterns_anti_refusal` |  |
| completed | `static_patterns_data_exfiltration` |  |
| completed | `static_patterns_deserialization` |  |
| completed | `static_patterns_excessive_agency` |  |
| completed | `static_patterns_harmful_content` |  |
| completed | `static_patterns_memory_poisoning` |  |
| completed | `static_patterns_output_handling` |  |
| completed | `static_patterns_privilege_escalation` |  |
| completed | `static_patterns_prompt_injection` |  |
| completed | `static_patterns_rogue_agent` |  |
| completed | `static_patterns_ssrf` |  |
| completed | `static_patterns_supply_chain` |  |
| completed | `static_patterns_system_prompt_leakage` |  |
| completed | `static_patterns_tool_misuse` |  |
| completed | `static_yara` |  |

## Metadata

- **Executable Scripts:** No

*Generated by SkillSpector v2.12.0*


<!-- ===== skills\subagent-driven-development ===== -->
# SkillSpector Security Report

**Skill:** subagent\-driven\-development  
**Source:** `F:\Github Repos\repos\obra__superpowers\skills\subagent-driven-development`  
**Scanned:** 2026-11-03 14:51:26 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 17/100 |
| Severity | LOW |
| Recommendation | SAFE |

## Components (14)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `SKILL.md` | markdown | 336 | No |
| `implementer-prompt.md` | markdown | 154 | No |
| `re-review-prompt.md` | markdown | 115 | No |
| `references/batching.md` | markdown | 11 | No |
| `references/cannot-verify.md` | markdown | 10 | No |
| `references/final-review.md` | markdown | 47 | No |
| `references/fix-loop.md` | markdown | 77 | No |
| `references/handling-reports.md` | markdown | 15 | No |
| `references/preflight.md` | markdown | 26 | No |
| `references/resuming.md` | markdown | 12 | No |
| `scripts/review-package` | other | 53 | Yes |
| `scripts/sdd-workspace` | other | 87 | Yes |
| `scripts/task-brief` | other | 43 | Yes |
| `task-reviewer-prompt.md` | markdown | 207 | No |

## Issues (1)

### 🔴 HIGH: TM1

**Location:** `SKILL.md:126`  
**Confidence:** 70%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | complete |
| Dependency contents | not\_requested |
| Coverage | 100\.0% |
| Fully inspected | 14 |
| Partially inspected | 0 |
| Entirely uninspected | 0 |

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
| disabled\_by\_configuration | `semantic_developer_intent` | Analyzer was disabled by the requested configuration\. |
| disabled\_by\_configuration | `semantic_quality_policy` | Analyzer was disabled by the requested configuration\. |
| disabled\_by\_configuration | `semantic_security_discovery` | Analyzer was disabled by the requested configuration\. |
| completed | `static_patterns_agent_snooping` |  |
| completed | `static_patterns_anti_refusal` |  |
| completed | `static_patterns_data_exfiltration` |  |
| completed | `static_patterns_deserialization` |  |
| completed | `static_patterns_excessive_agency` |  |
| completed | `static_patterns_harmful_content` |  |
| completed | `static_patterns_memory_poisoning` |  |
| completed | `static_patterns_output_handling` |  |
| completed | `static_patterns_privilege_escalation` |  |
| completed | `static_patterns_prompt_injection` |  |
| completed | `static_patterns_rogue_agent` |  |
| completed | `static_patterns_ssrf` |  |
| completed | `static_patterns_supply_chain` |  |
| completed | `static_patterns_system_prompt_leakage` |  |
| completed | `static_patterns_tool_misuse` |  |
| completed | `static_yara` |  |

## Metadata

- **Executable Scripts:** Yes

*Generated by SkillSpector v2.12.0*


<!-- ===== skills\systematic-debugging ===== -->
# SkillSpector Security Report

**Skill:** systematic\-debugging  
**Source:** `F:\Github Repos\repos\obra__superpowers\skills\systematic-debugging`  
**Scanned:** 2026-11-03 14:51:46 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 77/100 |
| Severity | HIGH |
| Recommendation | DO NOT INSTALL |

## Components (11)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `CREATION-LOG.md` | markdown | 119 | No |
| `SKILL.md` | markdown | 283 | No |
| `condition-based-waiting-example.ts` | typescript | 158 | Yes |
| `condition-based-waiting.md` | markdown | 115 | No |
| `defense-in-depth.md` | markdown | 122 | No |
| `find-polluter.sh` | shell | 72 | Yes |
| `root-cause-tracing.md` | markdown | 169 | No |
| `test-academic.md` | markdown | 14 | No |
| `test-pressure-1.md` | markdown | 58 | No |
| `test-pressure-2.md` | markdown | 68 | No |
| `test-pressure-3.md` | markdown | 69 | No |

## Issues (5)

### 🔴 HIGH: PE3

**Location:** `SKILL.md:98`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `SKILL.md:99`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:283`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `condition-based-waiting.md`

---

### 🔴 HIGH: E4

**Location:** `defense-in-depth.md:73`  
**Confidence:** 75%  

**Message:** Context Leakage

**Remediation:** Remove any code that sends prompts, responses, or session data externally\. Preserve user privacy; never exfiltrate conversation content\.

---

### 🟡 MEDIUM: EA4

**Location:** `condition-based-waiting.md:89`  
**Confidence:** 75%  

**Message:** Unbounded Resource Access

**Remediation:** Set explicit rate limits, timeouts, and resource quotas for API calls, file operations, and compute\. Implement circuit breakers for runaway loops\.

---

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | partial |
| Dependency contents | not\_requested |
| Coverage | 90\.9% |
| Fully inspected | 10 |
| Partially inspected | 1 |
| Entirely uninspected | 0 |

### Ledger Exceptions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| static\_parse\_limit | `condition-based-waiting.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |

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
| completed | `static_patterns_agent_snooping` |  |
| completed | `static_patterns_anti_refusal` |  |
| completed | `static_patterns_data_exfiltration` |  |
| completed | `static_patterns_deserialization` |  |
| completed | `static_patterns_excessive_agency` |  |
| completed | `static_patterns_harmful_content` |  |
| completed | `static_patterns_memory_poisoning` |  |
| completed | `static_patterns_output_handling` |  |
| completed | `static_patterns_privilege_escalation` |  |
| completed | `static_patterns_prompt_injection` |  |
| completed | `static_patterns_rogue_agent` |  |
| completed | `static_patterns_ssrf` |  |
| completed | `static_patterns_supply_chain` |  |
| completed | `static_patterns_system_prompt_leakage` |  |
| degraded | `static_patterns_tool_misuse` |  |
| completed | `static_yara` |  |

### Limitations

- Analyzer static\_patterns\_tool\_misuse status: degraded\.

## Metadata

- **Executable Scripts:** Yes

*Generated by SkillSpector v2.12.0*


<!-- ===== skills\test-driven-development ===== -->
# SkillSpector Security Report

**Skill:** test\-driven\-development  
**Source:** `F:\Github Repos\repos\obra__superpowers\skills\test-driven-development`  
**Scanned:** 2026-11-03 14:52:06 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 0/100 |
| Severity | LOW |
| Recommendation | CAUTION |

## Components (2)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `SKILL.md` | markdown | 330 | No |
| `writing-good-tests.md` | markdown | 198 | No |

## Issues (0)

No security issues detected.

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | partial |
| Dependency contents | not\_requested |
| Coverage | 50\.0% |
| Fully inspected | 1 |
| Partially inspected | 1 |
| Entirely uninspected | 0 |

### Ledger Exceptions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| static\_parse\_limit | `SKILL.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| reference\_missing | `SKILL.md:118-118` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:173-173` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |

### Analyzer Statuses

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| completed | `artifact_integrity` |  |
| no\_applicable\_files | `behavioral_ast` | No files matched this analyzer's applicability contract\. |
| no\_applicable\_files | `behavioral_taint_tracking` | No files matched this analyzer's applicability contract\. |
| no\_applicable\_files | `bundled_execution_surface` | No files matched this analyzer's applicability contract\. |
| no\_applicable\_files | `mcp_least_privilege` | No files matched this analyzer's applicability contract\. |
| completed | `mcp_rug_pull` |  |
| completed | `mcp_tool_poisoning` |  |
| no\_applicable\_files | `meta_analyzer` | No files matched this analyzer's applicability contract\. |
| disabled\_by\_configuration | `semantic_developer_intent` | Analyzer was disabled by the requested configuration\. |
| disabled\_by\_configuration | `semantic_quality_policy` | Analyzer was disabled by the requested configuration\. |
| disabled\_by\_configuration | `semantic_security_discovery` | Analyzer was disabled by the requested configuration\. |
| completed | `static_patterns_agent_snooping` |  |
| completed | `static_patterns_anti_refusal` |  |
| completed | `static_patterns_data_exfiltration` |  |
| completed | `static_patterns_deserialization` |  |
| completed | `static_patterns_excessive_agency` |  |
| completed | `static_patterns_harmful_content` |  |
| completed | `static_patterns_memory_poisoning` |  |
| completed | `static_patterns_output_handling` |  |
| completed | `static_patterns_privilege_escalation` |  |
| completed | `static_patterns_prompt_injection` |  |
| completed | `static_patterns_rogue_agent` |  |
| completed | `static_patterns_ssrf` |  |
| completed | `static_patterns_supply_chain` |  |
| completed | `static_patterns_system_prompt_leakage` |  |
| degraded | `static_patterns_tool_misuse` |  |
| completed | `static_yara` |  |

### Limitations

- Analyzer static\_patterns\_tool\_misuse status: degraded\.

## Metadata

- **Executable Scripts:** No

*Generated by SkillSpector v2.12.0*


<!-- ===== skills\using-git-worktrees ===== -->
# SkillSpector Security Report

**Skill:** using\-git\-worktrees  
**Source:** `F:\Github Repos\repos\obra__superpowers\skills\using-git-worktrees`  
**Scanned:** 2026-11-03 14:52:21 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 11/100 |
| Severity | LOW |
| Recommendation | CAUTION |

## Components (1)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `SKILL.md` | markdown | 167 | No |

## Issues (2)

### 🟡 MEDIUM: EA2

**Location:** `SKILL.md:45`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `SKILL.md:67`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | partial |
| Dependency contents | not\_requested |
| Coverage | 100\.0% |
| Fully inspected | 1 |
| Partially inspected | 0 |
| Entirely uninspected | 0 |

### Ledger Exceptions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| referenced\_uninspected | `SKILL.md:127-127` | A referenced artifact was not completely inspected\. |
| reference\_missing | `SKILL.md:157-157` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |

### Analyzer Statuses

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| completed | `artifact_integrity` |  |
| no\_applicable\_files | `behavioral_ast` | No files matched this analyzer's applicability contract\. |
| no\_applicable\_files | `behavioral_taint_tracking` | No files matched this analyzer's applicability contract\. |
| no\_applicable\_files | `bundled_execution_surface` | No files matched this analyzer's applicability contract\. |
| no\_applicable\_files | `mcp_least_privilege` | No files matched this analyzer's applicability contract\. |
| completed | `mcp_rug_pull` |  |
| completed | `mcp_tool_poisoning` |  |
| disabled\_by\_configuration | `meta_analyzer` | Analyzer was disabled by the requested configuration\. |
| disabled\_by\_configuration | `semantic_developer_intent` | Analyzer was disabled by the requested configuration\. |
| disabled\_by\_configuration | `semantic_quality_policy` | Analyzer was disabled by the requested configuration\. |
| disabled\_by\_configuration | `semantic_security_discovery` | Analyzer was disabled by the requested configuration\. |
| completed | `static_patterns_agent_snooping` |  |
| completed | `static_patterns_anti_refusal` |  |
| completed | `static_patterns_data_exfiltration` |  |
| completed | `static_patterns_deserialization` |  |
| completed | `static_patterns_excessive_agency` |  |
| completed | `static_patterns_harmful_content` |  |
| completed | `static_patterns_memory_poisoning` |  |
| completed | `static_patterns_output_handling` |  |
| completed | `static_patterns_privilege_escalation` |  |
| completed | `static_patterns_prompt_injection` |  |
| completed | `static_patterns_rogue_agent` |  |
| completed | `static_patterns_ssrf` |  |
| completed | `static_patterns_supply_chain` |  |
| completed | `static_patterns_system_prompt_leakage` |  |
| completed | `static_patterns_tool_misuse` |  |
| completed | `static_yara` |  |

## Metadata

- **Executable Scripts:** No

*Generated by SkillSpector v2.12.0*


<!-- ===== skills\using-superpowers ===== -->
# SkillSpector Security Report

**Skill:** using\-superpowers  
**Source:** `F:\Github Repos\repos\obra__superpowers\skills\using-superpowers`  
**Scanned:** 2026-11-03 14:52:41 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 49/100 |
| Severity | MEDIUM |
| Recommendation | CAUTION |

## Components (8)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `SKILL.md` | markdown | 65 | No |
| `references/antigravity-tools.md` | markdown | 23 | No |
| `references/claude-code-tools.md` | markdown | 29 | No |
| `references/codex-tools.md` | markdown | 108 | No |
| `references/gemini-tools.md` | markdown | 63 | No |
| `references/hermes-tools.md` | markdown | 56 | No |
| `references/muse-tools.md` | markdown | 35 | No |
| `references/pi-tools.md` | markdown | 16 | No |

## Issues (4)

### 🔴 HIGH: AS1

**Location:** `references/codex-tools.md:3`  
**Confidence:** 90%  

**Message:** Agent Config Directory Access

**Remediation:** Remove all code or instructions that access agent configuration directories \(\.claude/, \.codex/, \.gemini/\)\. If configuration values are needed, pass them explicitly as parameters or environment variables — never read the agent's own config files\.

---

### 🔴 HIGH: AS1

**Location:** `references/codex-tools.md:71`  
**Confidence:** 90%  

**Message:** Agent Config Directory Access

**Remediation:** Remove all code or instructions that access agent configuration directories \(\.claude/, \.codex/, \.gemini/\)\. If configuration values are needed, pass them explicitly as parameters or environment variables — never read the agent's own config files\.

---

### 🟡 MEDIUM: EA2

**Location:** `references/codex-tools.md:35`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: MP2

**Location:** `references/muse-tools.md:31`  
**Confidence:** 85%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | complete |
| Dependency contents | not\_requested |
| Coverage | 100\.0% |
| Fully inspected | 8 |
| Partially inspected | 0 |
| Entirely uninspected | 0 |

### Analyzer Statuses

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| completed | `artifact_integrity` |  |
| no\_applicable\_files | `behavioral_ast` | No files matched this analyzer's applicability contract\. |
| no\_applicable\_files | `behavioral_taint_tracking` | No files matched this analyzer's applicability contract\. |
| no\_applicable\_files | `bundled_execution_surface` | No files matched this analyzer's applicability contract\. |
| no\_applicable\_files | `mcp_least_privilege` | No files matched this analyzer's applicability contract\. |
| completed | `mcp_rug_pull` |  |
| completed | `mcp_tool_poisoning` |  |
| disabled\_by\_configuration | `meta_analyzer` | Analyzer was disabled by the requested configuration\. |
| disabled\_by\_configuration | `semantic_developer_intent` | Analyzer was disabled by the requested configuration\. |
| disabled\_by\_configuration | `semantic_quality_policy` | Analyzer was disabled by the requested configuration\. |
| disabled\_by\_configuration | `semantic_security_discovery` | Analyzer was disabled by the requested configuration\. |
| completed | `static_patterns_agent_snooping` |  |
| completed | `static_patterns_anti_refusal` |  |
| completed | `static_patterns_data_exfiltration` |  |
| completed | `static_patterns_deserialization` |  |
| completed | `static_patterns_excessive_agency` |  |
| completed | `static_patterns_harmful_content` |  |
| completed | `static_patterns_memory_poisoning` |  |
| completed | `static_patterns_output_handling` |  |
| completed | `static_patterns_privilege_escalation` |  |
| completed | `static_patterns_prompt_injection` |  |
| completed | `static_patterns_rogue_agent` |  |
| completed | `static_patterns_ssrf` |  |
| completed | `static_patterns_supply_chain` |  |
| completed | `static_patterns_system_prompt_leakage` |  |
| completed | `static_patterns_tool_misuse` |  |
| completed | `static_yara` |  |

## Metadata

- **Executable Scripts:** No

*Generated by SkillSpector v2.12.0*


<!-- ===== skills\verification-before-completion ===== -->
# SkillSpector Security Report

**Skill:** verification\-before\-completion  
**Source:** `F:\Github Repos\repos\obra__superpowers\skills\verification-before-completion`  
**Scanned:** 2026-11-03 14:52:56 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 7/100 |
| Severity | LOW |
| Recommendation | SAFE |

## Components (1)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `SKILL.md` | markdown | 120 | No |

## Issues (1)

### 🟡 MEDIUM: EA2

**Location:** `SKILL.md:54`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | complete |
| Dependency contents | not\_requested |
| Coverage | 100\.0% |
| Fully inspected | 1 |
| Partially inspected | 0 |
| Entirely uninspected | 0 |

### Analyzer Statuses

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| completed | `artifact_integrity` |  |
| no\_applicable\_files | `behavioral_ast` | No files matched this analyzer's applicability contract\. |
| no\_applicable\_files | `behavioral_taint_tracking` | No files matched this analyzer's applicability contract\. |
| no\_applicable\_files | `bundled_execution_surface` | No files matched this analyzer's applicability contract\. |
| no\_applicable\_files | `mcp_least_privilege` | No files matched this analyzer's applicability contract\. |
| completed | `mcp_rug_pull` |  |
| completed | `mcp_tool_poisoning` |  |
| disabled\_by\_configuration | `meta_analyzer` | Analyzer was disabled by the requested configuration\. |
| disabled\_by\_configuration | `semantic_developer_intent` | Analyzer was disabled by the requested configuration\. |
| disabled\_by\_configuration | `semantic_quality_policy` | Analyzer was disabled by the requested configuration\. |
| disabled\_by\_configuration | `semantic_security_discovery` | Analyzer was disabled by the requested configuration\. |
| completed | `static_patterns_agent_snooping` |  |
| completed | `static_patterns_anti_refusal` |  |
| completed | `static_patterns_data_exfiltration` |  |
| completed | `static_patterns_deserialization` |  |
| completed | `static_patterns_excessive_agency` |  |
| completed | `static_patterns_harmful_content` |  |
| completed | `static_patterns_memory_poisoning` |  |
| completed | `static_patterns_output_handling` |  |
| completed | `static_patterns_privilege_escalation` |  |
| completed | `static_patterns_prompt_injection` |  |
| completed | `static_patterns_rogue_agent` |  |
| completed | `static_patterns_ssrf` |  |
| completed | `static_patterns_supply_chain` |  |
| completed | `static_patterns_system_prompt_leakage` |  |
| completed | `static_patterns_tool_misuse` |  |
| completed | `static_yara` |  |

## Metadata

- **Executable Scripts:** No

*Generated by SkillSpector v2.12.0*


<!-- ===== skills\writing-plans ===== -->
# SkillSpector Security Report

**Skill:** writing\-plans  
**Source:** `F:\Github Repos\repos\obra__superpowers\skills\writing-plans`  
**Scanned:** 2026-11-03 14:53:14 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 0/100 |
| Severity | LOW |
| Recommendation | SAFE |

## Components (1)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `SKILL.md` | markdown | 204 | No |

## Issues (0)

No security issues detected.

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | complete\_with\_caveats |
| Dependency contents | not\_requested |
| Coverage | 100\.0% |
| Fully inspected | 1 |
| Partially inspected | 0 |
| Entirely uninspected | 0 |

### Ledger Exceptions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| reference\_missing | `SKILL.md:98-98` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:99-99` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:100-100` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:118-118` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:121-121` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:129-129` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:135-135` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |

### Analyzer Statuses

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| completed | `artifact_integrity` |  |
| no\_applicable\_files | `behavioral_ast` | No files matched this analyzer's applicability contract\. |
| no\_applicable\_files | `behavioral_taint_tracking` | No files matched this analyzer's applicability contract\. |
| no\_applicable\_files | `bundled_execution_surface` | No files matched this analyzer's applicability contract\. |
| no\_applicable\_files | `mcp_least_privilege` | No files matched this analyzer's applicability contract\. |
| completed | `mcp_rug_pull` |  |
| completed | `mcp_tool_poisoning` |  |
| no\_applicable\_files | `meta_analyzer` | No files matched this analyzer's applicability contract\. |
| disabled\_by\_configuration | `semantic_developer_intent` | Analyzer was disabled by the requested configuration\. |
| disabled\_by\_configuration | `semantic_quality_policy` | Analyzer was disabled by the requested configuration\. |
| disabled\_by\_configuration | `semantic_security_discovery` | Analyzer was disabled by the requested configuration\. |
| completed | `static_patterns_agent_snooping` |  |
| completed | `static_patterns_anti_refusal` |  |
| completed | `static_patterns_data_exfiltration` |  |
| completed | `static_patterns_deserialization` |  |
| completed | `static_patterns_excessive_agency` |  |
| completed | `static_patterns_harmful_content` |  |
| completed | `static_patterns_memory_poisoning` |  |
| completed | `static_patterns_output_handling` |  |
| completed | `static_patterns_privilege_escalation` |  |
| completed | `static_patterns_prompt_injection` |  |
| completed | `static_patterns_rogue_agent` |  |
| completed | `static_patterns_ssrf` |  |
| completed | `static_patterns_supply_chain` |  |
| completed | `static_patterns_system_prompt_leakage` |  |
| completed | `static_patterns_tool_misuse` |  |
| completed | `static_yara` |  |

## Metadata

- **Executable Scripts:** No

*Generated by SkillSpector v2.12.0*


<!-- ===== skills\writing-skills ===== -->
# SkillSpector Security Report

**Skill:** writing\-skills  
**Source:** `F:\Github Repos\repos\obra__superpowers\skills\writing-skills`  
**Scanned:** 2026-11-03 14:53:47 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 100/100 |
| Severity | CRITICAL |
| Recommendation | DO NOT INSTALL |

## Components (10)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `SKILL.md` | markdown | 399 | No |
| `references/CLAUDE_MD_TESTING.md` | markdown | 189 | No |
| `references/anthropic-best-practices.md` | markdown | 1150 | No |
| `references/bulletproofing.md` | markdown | 80 | No |
| `references/discovery.md` | markdown | 201 | No |
| `references/flowcharts.md` | markdown | 37 | No |
| `references/graphviz-conventions.dot` | other | 172 | No |
| `references/persuasion-principles.md` | markdown | 187 | No |
| `references/testing-skills-with-subagents.md` | markdown | 384 | No |
| `render-graphs.js` | javascript | 169 | Yes |

## Issues (18)

### 🔴 HIGH: RA1

**Location:** `SKILL.md:41`  
**Confidence:** 85%  

**Message:** Self\-Modification

**Remediation:** Prevent the skill from modifying its own code, SKILL\.md, or configuration files\. Treat skill files as read\-only at runtime\.

---

### 🔴 HIGH: RA1

**Location:** `SKILL.md:171`  
**Confidence:** 85%  

**Message:** Self\-Modification

**Remediation:** Prevent the skill from modifying its own code, SKILL\.md, or configuration files\. Treat skill files as read\-only at runtime\.

---

### 🔴 HIGH: RA1

**Location:** `SKILL.md:287`  
**Confidence:** 85%  

**Message:** Self\-Modification

**Remediation:** Prevent the skill from modifying its own code, SKILL\.md, or configuration files\. Treat skill files as read\-only at runtime\.

---

### 🔴 HIGH: RA1

**Location:** `references/testing-skills-with-subagents.md:36`  
**Confidence:** 85%  

**Message:** Self\-Modification

**Remediation:** Prevent the skill from modifying its own code, SKILL\.md, or configuration files\. Treat skill files as read\-only at runtime\.

---

### 🔴 HIGH: RA1

**Location:** `references/testing-skills-with-subagents.md:84`  
**Confidence:** 85%  

**Message:** Self\-Modification

**Remediation:** Prevent the skill from modifying its own code, SKILL\.md, or configuration files\. Treat skill files as read\-only at runtime\.

---

### 🔴 HIGH: RA1

**Location:** `references/testing-skills-with-subagents.md:364`  
**Confidence:** 85%  

**Message:** Self\-Modification

**Remediation:** Prevent the skill from modifying its own code, SKILL\.md, or configuration files\. Treat skill files as read\-only at runtime\.

---

### 🔴 HIGH: RA1

**Location:** `SKILL.md:172`  
**Confidence:** 85%  

**Message:** Self\-Modification

**Remediation:** Prevent the skill from modifying its own code, SKILL\.md, or configuration files\. Treat skill files as read\-only at runtime\.

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:307`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the target's analysis\-completeness ledger and resolve all limitations\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_agent_snooping']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_anti_refusal']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_deserialization']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_excessive_agency']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_harmful_content']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_memory_poisoning']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_privilege_escalation']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_prompt_injection']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_rogue_agent']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_ssrf']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_supply_chain']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_system_prompt_leakage']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `references/testing-skills-with-subagents.md`

---

### 🔴 HIGH: AS1

**Location:** `references/CLAUDE_MD_TESTING.md:85`  
**Confidence:** 85%  

**Message:** Agent Config Directory Access

**Remediation:** Remove all code or instructions that access agent configuration directories \(\.claude/, \.codex/, \.gemini/\)\. If configuration values are needed, pass them explicitly as parameters or environment variables — never read the agent's own config files\.

---

### 🔴 HIGH: AS1

**Location:** `references/CLAUDE_MD_TESTING.md:95`  
**Confidence:** 85%  

**Message:** Agent Config Directory Access

**Remediation:** Remove all code or instructions that access agent configuration directories \(\.claude/, \.codex/, \.gemini/\)\. If configuration values are needed, pass them explicitly as parameters or environment variables — never read the agent's own config files\.

---

### 🔴 HIGH: AS1

**Location:** `references/CLAUDE_MD_TESTING.md:123`  
**Confidence:** 85%  

**Message:** Agent Config Directory Access

**Remediation:** Remove all code or instructions that access agent configuration directories \(\.claude/, \.codex/, \.gemini/\)\. If configuration values are needed, pass them explicitly as parameters or environment variables — never read the agent's own config files\.

---

### 🔴 HIGH: RA1

**Location:** `references/anthropic-best-practices.md:5`  
**Confidence:** 85%  

**Message:** Self\-Modification

**Remediation:** Prevent the skill from modifying its own code, SKILL\.md, or configuration files\. Treat skill files as read\-only at runtime\.

---

### 🔴 HIGH: RA1

**Location:** `references/testing-skills-with-subagents.md:9`  
**Confidence:** 85%  

**Message:** Self\-Modification

**Remediation:** Prevent the skill from modifying its own code, SKILL\.md, or configuration files\. Treat skill files as read\-only at runtime\.

---

### 🟡 MEDIUM: AS3

**Location:** `references/CLAUDE_MD_TESTING.md:84`  
**Confidence:** 85%  

**Message:** Skill Enumeration

**Remediation:** Remove all code or instructions that list or read other skills' files or directories\. Skills should operate independently; cross\-skill access is a privilege escalation\.

---

### 🟡 MEDIUM: AS3

**Location:** `references/CLAUDE_MD_TESTING.md:94`  
**Confidence:** 85%  

**Message:** Skill Enumeration

**Remediation:** Remove all code or instructions that list or read other skills' files or directories\. Skills should operate independently; cross\-skill access is a privilege escalation\.

---

### 🟡 MEDIUM: AS3

**Location:** `references/CLAUDE_MD_TESTING.md:107`  
**Confidence:** 85%  

**Message:** Skill Enumeration

**Remediation:** Remove all code or instructions that list or read other skills' files or directories\. Skills should operate independently; cross\-skill access is a privilege escalation\.

---

### 🟡 MEDIUM: AS3

**Location:** `references/CLAUDE_MD_TESTING.md:122`  
**Confidence:** 85%  

**Message:** Skill Enumeration

**Remediation:** Remove all code or instructions that list or read other skills' files or directories\. Skills should operate independently; cross\-skill access is a privilege escalation\.

---

### 🟡 MEDIUM: AS3

**Location:** `references/discovery.md:176`  
**Confidence:** 80%  

**Message:** Skill Enumeration

**Remediation:** Remove all code or instructions that list or read other skills' files or directories\. Skills should operate independently; cross\-skill access is a privilege escalation\.

---

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | partial |
| Dependency contents | not\_requested |
| Coverage | 80\.0% |
| Fully inspected | 8 |
| Partially inspected | 2 |
| Entirely uninspected | 0 |

### Ledger Exceptions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| reference\_missing | `SKILL.md:161-161` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| obfuscated\_instruction\_text | `references/testing-skills-with-subagents.md` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |
| static\_parse\_limit | `render-graphs.js` | A security\-relevant expression exceeded a bounded static parser's span limit\. |

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

