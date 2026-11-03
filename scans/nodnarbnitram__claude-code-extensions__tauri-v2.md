# SkillSpector Security Report

**Skill:** tauri\-v2  
**Source:** `F:\Github Repos\repos\nodnarbnitram__claude-code-extensions\plugins\cce-tauri\skills\tauri-v2`  
**Scanned:** 2026-11-03 17:20:03 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 84/100 |
| Severity | CRITICAL |
| Recommendation | DO NOT INSTALL |

## Components (8)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `README.md` | markdown | 193 | No |
| `SKILL.md` | markdown | 497 | No |
| `references/README.md` | markdown | 23 | No |
| `references/advanced-runtime-reference.md` | markdown | 196 | No |
| `references/capabilities-reference.md` | markdown | 394 | No |
| `references/ipc-patterns.md` | markdown | 505 | No |
| `references/plugin-reference.md` | markdown | 382 | No |
| `references/updater-distribution-reference.md` | markdown | 137 | No |

## Issues (24)

### 🔴 HIGH: AE1

**Location:** `SKILL.md:142`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `references/ipc-patterns.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:237`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `references/ipc-patterns.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:297`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `references/ipc-patterns.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:321`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `references/ipc-patterns.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:346`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `references/ipc-patterns.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:398`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `references/ipc-patterns.md`

---

### 🟡 MEDIUM: RP1

**Location:** `README.md:101`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx tauri'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:493`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx tauri'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: TR2

**Location:** `SKILL.md:2`  
**Confidence:** 70%  

**Message:** Shadow Command Trigger: description clause 'command\]\), setting up IPC patterns \(invoke, emit, channels\), configuring permissions/capabilities, troubleshooting build issues, or deploying desktop/mobile apps' conflicts with built\-in command 'build'

**Remediation:** Choose triggers that do not conflict with built\-in commands or other skills\. Prefix with a unique namespace if necessary\.

---

### 🟡 MEDIUM: RA2

**Location:** `references/advanced-runtime-reference.md:169`  
**Confidence:** 75%  

**Message:** Session Persistence

**Remediation:** Remove any persistence mechanisms \(cron jobs, startup scripts, state files\)\. Skills should not maintain state across sessions without explicit user consent\.

---

### 🟡 MEDIUM: RA2

**Location:** `references/advanced-runtime-reference.md:172`  
**Confidence:** 75%  

**Message:** Session Persistence

**Remediation:** Remove any persistence mechanisms \(cron jobs, startup scripts, state files\)\. Skills should not maintain state across sessions without explicit user consent\.

---

### 🟡 MEDIUM: E1

**Location:** `references/capabilities-reference.md:177`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟢 LOW: PE1

**Location:** `references/plugin-reference.md:59`  
**Confidence:** 80%  

**Message:** Excessive Permissions

**Remediation:** Request only the minimum permissions required\. Document why each permission is needed\. Remove broad permissions like '\*' or 'all'\.

---

### 🟢 LOW: PE1

**Location:** `references/plugin-reference.md:92`  
**Confidence:** 80%  

**Message:** Excessive Permissions

**Remediation:** Request only the minimum permissions required\. Document why each permission is needed\. Remove broad permissions like '\*' or 'all'\.

---

### 🟢 LOW: PE1

**Location:** `references/plugin-reference.md:121`  
**Confidence:** 80%  

**Message:** Excessive Permissions

**Remediation:** Request only the minimum permissions required\. Document why each permission is needed\. Remove broad permissions like '\*' or 'all'\.

---

### 🟢 LOW: PE1

**Location:** `references/plugin-reference.md:152`  
**Confidence:** 80%  

**Message:** Excessive Permissions

**Remediation:** Request only the minimum permissions required\. Document why each permission is needed\. Remove broad permissions like '\*' or 'all'\.

---

### 🟢 LOW: PE1

**Location:** `references/plugin-reference.md:182`  
**Confidence:** 80%  

**Message:** Excessive Permissions

**Remediation:** Request only the minimum permissions required\. Document why each permission is needed\. Remove broad permissions like '\*' or 'all'\.

---

### 🟢 LOW: PE1

**Location:** `references/plugin-reference.md:210`  
**Confidence:** 80%  

**Message:** Excessive Permissions

**Remediation:** Request only the minimum permissions required\. Document why each permission is needed\. Remove broad permissions like '\*' or 'all'\.

---

### 🟢 LOW: PE1

**Location:** `references/plugin-reference.md:237`  
**Confidence:** 80%  

**Message:** Excessive Permissions

**Remediation:** Request only the minimum permissions required\. Document why each permission is needed\. Remove broad permissions like '\*' or 'all'\.

---

### 🟢 LOW: PE1

**Location:** `references/plugin-reference.md:264`  
**Confidence:** 80%  

**Message:** Excessive Permissions

**Remediation:** Request only the minimum permissions required\. Document why each permission is needed\. Remove broad permissions like '\*' or 'all'\.

---

### 🟢 LOW: PE1

**Location:** `references/plugin-reference.md:293`  
**Confidence:** 80%  

**Message:** Excessive Permissions

**Remediation:** Request only the minimum permissions required\. Document why each permission is needed\. Remove broad permissions like '\*' or 'all'\.

---

### 🟢 LOW: PE1

**Location:** `references/plugin-reference.md:323`  
**Confidence:** 80%  

**Message:** Excessive Permissions

**Remediation:** Request only the minimum permissions required\. Document why each permission is needed\. Remove broad permissions like '\*' or 'all'\.

---

### 🟢 LOW: PE1

**Location:** `references/plugin-reference.md:349`  
**Confidence:** 80%  

**Message:** Excessive Permissions

**Remediation:** Request only the minimum permissions required\. Document why each permission is needed\. Remove broad permissions like '\*' or 'all'\.

---

### 🟢 LOW: PE1

**Location:** `references/plugin-reference.md:376`  
**Confidence:** 80%  

**Message:** Excessive Permissions

**Remediation:** Request only the minimum permissions required\. Document why each permission is needed\. Remove broad permissions like '\*' or 'all'\.

---

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | partial |
| Dependency contents | not\_requested |
| Coverage | 62\.5% |
| Fully inspected | 5 |
| Partially inspected | 3 |
| Entirely uninspected | 0 |

### Ledger Exceptions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| static\_parse\_limit | `README.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| static\_parse\_limit | `SKILL.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| reference\_missing | `SKILL.md:34-34` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:51-51` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:53-53` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:75-75` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:94-94` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:95-95` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:129-129` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:130-130` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:132-132` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:153-153` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:155-155` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:156-156` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:178-178` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:184-184` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:185-185` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:187-187` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:206-206` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:213-213` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:494-494` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:496-496` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| static\_parse\_limit | `references/ipc-patterns.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |

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

- **Executable Scripts:** No

*Generated by SkillSpector v2.12.0*
