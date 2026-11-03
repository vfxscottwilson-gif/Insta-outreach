# Scans for microsoft/playwright-cli @ c2d8d19


<!-- ===== skills\playwright-cli ===== -->
# SkillSpector Security Report

**Skill:** playwright\-cli  
**Source:** `F:\Github Repos\repos\microsoft__playwright-cli\skills\playwright-cli`  
**Scanned:** 2026-11-03 15:05:22 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 87/100 |
| Severity | CRITICAL |
| Recommendation | DO NOT INSTALL |

## Components (11)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `SKILL.md` | markdown | 493 | No |
| `references/element-attributes.md` | markdown | 23 | No |
| `references/playwright-tests.md` | markdown | 39 | No |
| `references/pr-attachments.md` | markdown | 60 | No |
| `references/request-mocking.md` | markdown | 87 | No |
| `references/running-code.md` | markdown | 245 | No |
| `references/session-management.md` | markdown | 227 | No |
| `references/storage-state.md` | markdown | 278 | No |
| `references/test-generation.md` | markdown | 433 | No |
| `references/tracing.md` | markdown | 146 | No |
| `references/video-recording.md` | markdown | 216 | No |

## Issues (20)

### 🔴 HIGH: AE1

**Location:** `SKILL.md:480`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `references/pr-attachments.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:492`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `references/pr-attachments.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:489`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `references/test-generation.md`

---

### 🔴 HIGH: MP3

**Location:** `references/storage-state.md:276`  
**Confidence:** 80%  

**Message:** Memory Manipulation

**Remediation:** Protect agent memory and state from modification by untrusted content\. Use read\-only memory for critical instructions and validate all state changes\.

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:1`  
**Confidence:** 70%  

**Message:** Manifest references MCP server without version pin: 'npx playwright'\.

**Remediation:** Always pin MCP server versions in manifest references\.

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:4`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx playwright'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:406`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx playwright'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:412`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx playwright'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `references/playwright-tests.md:3`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx playwright'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `references/playwright-tests.md:7`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx playwright'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `references/playwright-tests.md:23`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx playwright'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `references/pr-attachments.md:46`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx playwright'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `references/test-generation.md:10`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx playwright'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `references/test-generation.md:208`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx playwright'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `references/test-generation.md:296`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx playwright'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `references/test-generation.md:359`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx playwright'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `references/test-generation.md:373`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx playwright'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `references/test-generation.md:383`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx playwright'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: E1

**Location:** `SKILL.md:172`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: RA2

**Location:** `references/storage-state.md:261`  
**Confidence:** 60%  

**Message:** Session Persistence

**Remediation:** Remove any persistence mechanisms \(cron jobs, startup scripts, state files\)\. Skills should not maintain state across sessions without explicit user consent\.

---

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | partial |
| Dependency contents | not\_requested |
| Coverage | 81\.8% |
| Fully inspected | 9 |
| Partially inspected | 2 |
| Entirely uninspected | 0 |

### Ledger Exceptions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| reference\_missing | `SKILL.md:18-18` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:42-42` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:46-46` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:57-57` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:311-311` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:331-331` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:477-477` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| static\_parse\_limit | `references/pr-attachments.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| static\_parse\_limit | `references/test-generation.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |

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

