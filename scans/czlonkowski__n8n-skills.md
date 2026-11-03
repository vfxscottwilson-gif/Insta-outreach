# Scans for czlonkowski/n8n-skills @ e037563


<!-- ===== skills\n8n-agents ===== -->
# SkillSpector Security Report

**Skill:** n8n\-agents  
**Source:** `F:\Github Repos\repos\czlonkowski__n8n-skills\skills\n8n-agents`  
**Scanned:** 2026-11-03 15:07:10 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 61/100 |
| Severity | HIGH |
| Recommendation | DO NOT INSTALL |

## Components (11)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `CHAT_AGENT_PATTERNS.md` | markdown | 228 | No |
| `EXAMPLES.md` | markdown | 432 | No |
| `HUMAN_REVIEW.md` | markdown | 180 | No |
| `MEMORY.md` | markdown | 139 | No |
| `RAG.md` | markdown | 102 | No |
| `README.md` | markdown | 180 | No |
| `SKILL.md` | markdown | 312 | No |
| `STRUCTURED_OUTPUT.md` | markdown | 163 | No |
| `SUBWORKFLOW_AS_TOOL.md` | markdown | 202 | No |
| `SYSTEM_PROMPT.md` | markdown | 151 | No |
| `TOOLS.md` | markdown | 199 | No |

## Issues (5)

### 🔴 HIGH: AR1

**Location:** `EXAMPLES.md:348`  
**Confidence:** 70%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove any instruction telling the agent to never refuse or always comply\. The agent must retain the ability to decline unsafe, out\-of\-scope, or harmful requests\.

---

### 🔴 HIGH: P6

**Location:** `SYSTEM_PROMPT.md:12`  
**Confidence:** 85%  

**Message:** Direct Prompt Extraction

**Remediation:** Remove any instructions that reveal, print, or output system prompts or internal rules\. System instructions should never be exposed to end users\.

---

### 🔴 HIGH: P6

**Location:** `SYSTEM_PROMPT.md:59`  
**Confidence:** 85%  

**Message:** Direct Prompt Extraction

**Remediation:** Remove any instructions that reveal, print, or output system prompts or internal rules\. System instructions should never be exposed to end users\.

---

### 🟡 MEDIUM: EA2

**Location:** `HUMAN_REVIEW.md:43`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `SYSTEM_PROMPT.md:60`  
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
| Coverage | 90\.9% |
| Fully inspected | 10 |
| Partially inspected | 1 |
| Entirely uninspected | 0 |

### Ledger Exceptions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| obfuscated\_instruction\_text | `SKILL.md` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |
| reference\_missing | `SKILL.md:8-8` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:10-10` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:175-175` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:202-202` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:208-208` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:279-279` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:281-281` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |

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

- **Executable Scripts:** No

*Generated by SkillSpector v2.12.0*


<!-- ===== skills\n8n-binary-and-data ===== -->
# SkillSpector Security Report

**Skill:** n8n\-binary\-and\-data  
**Source:** `F:\Github Repos\repos\czlonkowski__n8n-skills\skills\n8n-binary-and-data`  
**Scanned:** 2026-11-03 15:07:43 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 21/100 |
| Severity | MEDIUM |
| Recommendation | CAUTION |

## Components (6)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `AGENT_TOOL_BINARY.md` | markdown | 227 | No |
| `BINARY_BASICS.md` | markdown | 187 | No |
| `CDN_REQUIREMENT.md` | markdown | 109 | No |
| `MERGE_FOR_CONTEXT.md` | markdown | 130 | No |
| `README.md` | markdown | 208 | No |
| `SKILL.md` | markdown | 249 | No |

## Issues (1)

### 🔴 HIGH: E4

**Location:** `CDN_REQUIREMENT.md:46`  
**Confidence:** 85%  

**Message:** Context Leakage

**Remediation:** Remove any code that sends prompts, responses, or session data externally\. Preserve user privacy; never exfiltrate conversation content\.

---

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | complete\_with\_caveats |
| Dependency contents | not\_requested |
| Coverage | 100\.0% |
| Fully inspected | 6 |
| Partially inspected | 0 |
| Entirely uninspected | 0 |

### Ledger Exceptions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| reference\_missing | `SKILL.md:35-35` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:64-64` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:96-96` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |

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


<!-- ===== skills\n8n-code-javascript ===== -->
# SkillSpector Security Report

**Skill:** n8n\-code\-javascript  
**Source:** `F:\Github Repos\repos\czlonkowski__n8n-skills\skills\n8n-code-javascript`  
**Scanned:** 2026-11-03 15:08:34 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 73/100 |
| Severity | HIGH |
| Recommendation | DO NOT INSTALL |

## Components (6)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `BUILTIN_FUNCTIONS.md` | markdown | 849 | No |
| `COMMON_PATTERNS.md` | markdown | 1233 | No |
| `DATA_ACCESS.md` | markdown | 894 | No |
| `ERROR_PATTERNS.md` | markdown | 857 | No |
| `README.md` | markdown | 340 | No |
| `SKILL.md` | markdown | 428 | No |

## Issues (29)

### 🔴 HIGH: AR1

**Location:** `SKILL.md:64`  
**Confidence:** 85%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove any instruction telling the agent to never refuse or always comply\. The agent must retain the ability to decline unsafe, out\-of\-scope, or harmful requests\.

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:149`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `DATA_ACCESS.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:166`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `DATA_ACCESS.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:190`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `DATA_ACCESS.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:330`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `DATA_ACCESS.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:416`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `DATA_ACCESS.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:266`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `ERROR_PATTERNS.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:289`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `ERROR_PATTERNS.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:418`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `ERROR_PATTERNS.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:274`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `COMMON_PATTERNS.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:324`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `COMMON_PATTERNS.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:417`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `COMMON_PATTERNS.md`

---

### 🟡 MEDIUM: E1

**Location:** `BUILTIN_FUNCTIONS.md:71`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `BUILTIN_FUNCTIONS.md:82`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `BUILTIN_FUNCTIONS.md:109`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `BUILTIN_FUNCTIONS.md:119`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `BUILTIN_FUNCTIONS.md:142`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `BUILTIN_FUNCTIONS.md:163`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `BUILTIN_FUNCTIONS.md:179`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `BUILTIN_FUNCTIONS.md:195`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `BUILTIN_FUNCTIONS.md:205`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `BUILTIN_FUNCTIONS.md:217`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `BUILTIN_FUNCTIONS.md:231`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `BUILTIN_FUNCTIONS.md:261`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `COMMON_PATTERNS.md:1163`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `DATA_ACCESS.md:354`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `ERROR_PATTERNS.md:659`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `ERROR_PATTERNS.md:674`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `SKILL.md:297`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | partial |
| Dependency contents | not\_requested |
| Coverage | 50\.0% |
| Fully inspected | 3 |
| Partially inspected | 3 |
| Entirely uninspected | 0 |

### Ledger Exceptions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| static\_parse\_limit | `COMMON_PATTERNS.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| static\_parse\_limit | `DATA_ACCESS.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| static\_parse\_limit | `ERROR_PATTERNS.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| reference\_missing | `SKILL.md:31-31` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:164-164` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:375-375` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:376-376` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |

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


<!-- ===== skills\n8n-code-python ===== -->
# SkillSpector Security Report

**Skill:** n8n\-code\-python  
**Source:** `F:\Github Repos\repos\czlonkowski__n8n-skills\skills\n8n-code-python`  
**Scanned:** 2026-11-03 15:08:54 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 7/100 |
| Severity | LOW |
| Recommendation | SAFE |

## Components (3)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `COMMON_PATTERNS.md` | markdown | 251 | No |
| `README.md` | markdown | 81 | No |
| `SKILL.md` | markdown | 213 | No |

## Issues (1)

### 🟡 MEDIUM: EA1

**Location:** `SKILL.md:85`  
**Confidence:** 70%  

**Message:** Unrestricted Tool Access

**Remediation:** Restrict tool access to only the tools required for the skill's stated purpose\. Use an explicit allowlist rather than granting blanket access\.

---

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | complete\_with\_caveats |
| Dependency contents | not\_requested |
| Coverage | 100\.0% |
| Fully inspected | 3 |
| Partially inspected | 0 |
| Entirely uninspected | 0 |

### Ledger Exceptions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| reference\_missing | `SKILL.md:19-19` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:44-44` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:57-57` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:74-74` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:78-78` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:94-94` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:174-174` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |

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


<!-- ===== skills\n8n-code-tool ===== -->
# SkillSpector Security Report

**Skill:** n8n\-code\-tool  
**Source:** `F:\Github Repos\repos\czlonkowski__n8n-skills\skills\n8n-code-tool`  
**Scanned:** 2026-11-03 15:09:11 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 0/100 |
| Severity | LOW |
| Recommendation | CAUTION |

## Components (4)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `ERROR_PATTERNS.md` | markdown | 178 | No |
| `INPUT_SCHEMA.md` | markdown | 132 | No |
| `README.md` | markdown | 192 | No |
| `SKILL.md` | markdown | 338 | No |

## Issues (0)

No security issues detected.

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | partial |
| Dependency contents | not\_requested |
| Coverage | 75\.0% |
| Fully inspected | 3 |
| Partially inspected | 1 |
| Entirely uninspected | 0 |

### Ledger Exceptions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| static\_parse\_limit | `SKILL.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| reference\_missing | `SKILL.md:18-18` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:24-24` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:264-264` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:314-314` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |

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


<!-- ===== skills\n8n-error-handling ===== -->
# SkillSpector Security Report

**Skill:** n8n\-error\-handling  
**Source:** `F:\Github Repos\repos\czlonkowski__n8n-skills\skills\n8n-error-handling`  
**Scanned:** 2026-11-03 15:09:35 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 17/100 |
| Severity | LOW |
| Recommendation | CAUTION |

## Components (6)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `API_WORKFLOWS.md` | markdown | 349 | No |
| `ERROR_WORKFLOWS.md` | markdown | 178 | No |
| `NODE_ERROR_OUTPUTS.md` | markdown | 171 | No |
| `README.md` | markdown | 196 | No |
| `RESPONSE_SHAPES.md` | markdown | 218 | No |
| `SKILL.md` | markdown | 284 | No |

## Issues (1)

### 🔴 HIGH: PE3

**Location:** `ERROR_WORKFLOWS.md:109`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | partial |
| Dependency contents | not\_requested |
| Coverage | 66\.7% |
| Fully inspected | 4 |
| Partially inspected | 2 |
| Entirely uninspected | 0 |

### Ledger Exceptions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| static\_parse\_limit | `API_WORKFLOWS.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| static\_parse\_limit | `ERROR_WORKFLOWS.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| reference\_missing | `SKILL.md:83-83` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:133-133` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:162-162` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:228-228` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:270-270` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |

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
| degraded | `static_patterns_tool_misuse` |  |
| completed | `static_yara` |  |

### Limitations

- Analyzer static\_patterns\_tool\_misuse status: degraded\.

## Metadata

- **Executable Scripts:** No

*Generated by SkillSpector v2.12.0*


<!-- ===== skills\n8n-expression-syntax ===== -->
# SkillSpector Security Report

**Skill:** n8n\-expression\-syntax  
**Source:** `F:\Github Repos\repos\czlonkowski__n8n-skills\skills\n8n-expression-syntax`  
**Scanned:** 2026-11-03 15:09:58 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 46/100 |
| Severity | MEDIUM |
| Recommendation | CAUTION |

## Components (4)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `COMMON_MISTAKES.md` | markdown | 446 | No |
| `EXAMPLES.md` | markdown | 486 | No |
| `README.md` | markdown | 97 | No |
| `SKILL.md` | markdown | 697 | No |

## Issues (7)

### 🔴 HIGH: AE1

**Location:** `SKILL.md:391`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `COMMON_MISTAKES.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:692`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `COMMON_MISTAKES.md`

---

### 🟡 MEDIUM: E1

**Location:** `EXAMPLES.md:122`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `EXAMPLES.md:421`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `EXAMPLES.md:423`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `SKILL.md:158`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `EXAMPLES.md:455`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | partial |
| Dependency contents | not\_requested |
| Coverage | 50\.0% |
| Fully inspected | 2 |
| Partially inspected | 2 |
| Entirely uninspected | 0 |

### Ledger Exceptions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| static\_parse\_limit | `COMMON_MISTAKES.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| static\_parse\_limit | `SKILL.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |

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


<!-- ===== skills\n8n-mcp-tools-expert ===== -->
# SkillSpector Security Report

**Skill:** n8n\-mcp\-tools\-expert  
**Source:** `F:\Github Repos\repos\czlonkowski__n8n-skills\skills\n8n-mcp-tools-expert`  
**Scanned:** 2026-11-03 15:10:40 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 77/100 |
| Severity | HIGH |
| Recommendation | DO NOT INSTALL |

## Components (6)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `OPERATIONS_GUIDE.md` | markdown | 221 | No |
| `README.md` | markdown | 99 | No |
| `SEARCH_GUIDE.md` | markdown | 385 | No |
| `SKILL.md` | markdown | 482 | No |
| `VALIDATION_GUIDE.md` | markdown | 661 | No |
| `WORKFLOW_GUIDE.md` | markdown | 1285 | No |

## Issues (17)

### 🔴 HIGH: AE1

**Location:** `SKILL.md:17`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `VALIDATION_GUIDE.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:197`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `VALIDATION_GUIDE.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:206`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `VALIDATION_GUIDE.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:220`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `VALIDATION_GUIDE.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:393`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `VALIDATION_GUIDE.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:470`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `VALIDATION_GUIDE.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:18`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the target's analysis\-completeness ledger and resolve all limitations\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_agent_snooping']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_anti_refusal']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_deserialization']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_excessive_agency']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_harmful_content']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_memory_poisoning']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_privilege_escalation']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_prompt_injection']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_rogue_agent']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_ssrf']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_supply_chain']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_system_prompt_leakage']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `WORKFLOW_GUIDE.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:207`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the target's analysis\-completeness ledger and resolve all limitations\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_agent_snooping']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_anti_refusal']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_deserialization']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_excessive_agency']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_harmful_content']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_memory_poisoning']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_privilege_escalation']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_prompt_injection']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_rogue_agent']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_ssrf']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_supply_chain']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_system_prompt_leakage']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `WORKFLOW_GUIDE.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:228`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the target's analysis\-completeness ledger and resolve all limitations\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_agent_snooping']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_anti_refusal']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_deserialization']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_excessive_agency']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_harmful_content']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_memory_poisoning']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_privilege_escalation']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_prompt_injection']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_rogue_agent']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_ssrf']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_supply_chain']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_system_prompt_leakage']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `WORKFLOW_GUIDE.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:279`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the target's analysis\-completeness ledger and resolve all limitations\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_agent_snooping']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_anti_refusal']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_deserialization']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_excessive_agency']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_harmful_content']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_memory_poisoning']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_privilege_escalation']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_prompt_injection']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_rogue_agent']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_ssrf']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_supply_chain']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_system_prompt_leakage']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `WORKFLOW_GUIDE.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:294`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the target's analysis\-completeness ledger and resolve all limitations\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_agent_snooping']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_anti_refusal']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_deserialization']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_excessive_agency']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_harmful_content']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_memory_poisoning']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_privilege_escalation']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_prompt_injection']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_rogue_agent']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_ssrf']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_supply_chain']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_system_prompt_leakage']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `WORKFLOW_GUIDE.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:314`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the target's analysis\-completeness ledger and resolve all limitations\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_agent_snooping']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_anti_refusal']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_deserialization']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_excessive_agency']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_harmful_content']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_memory_poisoning']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_privilege_escalation']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_prompt_injection']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_rogue_agent']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_ssrf']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_supply_chain']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_system_prompt_leakage']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `WORKFLOW_GUIDE.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:322`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the target's analysis\-completeness ledger and resolve all limitations\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_agent_snooping']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_anti_refusal']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_deserialization']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_excessive_agency']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_harmful_content']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_memory_poisoning']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_privilege_escalation']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_prompt_injection']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_rogue_agent']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_ssrf']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_supply_chain']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_system_prompt_leakage']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `WORKFLOW_GUIDE.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:340`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the target's analysis\-completeness ledger and resolve all limitations\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_agent_snooping']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_anti_refusal']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_deserialization']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_excessive_agency']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_harmful_content']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_memory_poisoning']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_privilege_escalation']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_prompt_injection']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_rogue_agent']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_ssrf']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_supply_chain']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_system_prompt_leakage']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `WORKFLOW_GUIDE.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:471`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the target's analysis\-completeness ledger and resolve all limitations\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_agent_snooping']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_anti_refusal']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_deserialization']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_excessive_agency']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_harmful_content']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_memory_poisoning']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_privilege_escalation']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_prompt_injection']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_rogue_agent']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_ssrf']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_supply_chain']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_system_prompt_leakage']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `WORKFLOW_GUIDE.md`

---

### 🔴 HIGH: MP3

**Location:** `VALIDATION_GUIDE.md:256`  
**Confidence:** 90%  

**Message:** Memory Manipulation

**Remediation:** Protect agent memory and state from modification by untrusted content\. Use read\-only memory for critical instructions and validate all state changes\.

---

### 🔴 HIGH: MP3

**Location:** `VALIDATION_GUIDE.md:544`  
**Confidence:** 90%  

**Message:** Memory Manipulation

**Remediation:** Protect agent memory and state from modification by untrusted content\. Use read\-only memory for critical instructions and validate all state changes\.

---

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | partial |
| Dependency contents | not\_requested |
| Coverage | 50\.0% |
| Fully inspected | 3 |
| Partially inspected | 3 |
| Entirely uninspected | 0 |

### Ledger Exceptions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| obfuscated\_instruction\_text | `SKILL.md` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |
| reference\_missing | `SKILL.md:62-62` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:63-63` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:73-73` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:77-77` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:134-134` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:135-135` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:136-136` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:137-137` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:149-149` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:150-150` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:151-151` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:164-164` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:165-165` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:178-178` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:179-179` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:290-290` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:300-300` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| static\_parse\_limit | `VALIDATION_GUIDE.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| obfuscated\_instruction\_text | `WORKFLOW_GUIDE.md` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |

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

- **Executable Scripts:** No

*Generated by SkillSpector v2.12.0*


<!-- ===== skills\n8n-multi-instance ===== -->
# SkillSpector Security Report

**Skill:** n8n\-multi\-instance  
**Source:** `F:\Github Repos\repos\czlonkowski__n8n-skills\skills\n8n-multi-instance`  
**Scanned:** 2026-11-03 15:11:01 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 0/100 |
| Severity | LOW |
| Recommendation | SAFE |

## Components (2)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `README.md` | markdown | 142 | No |
| `SKILL.md` | markdown | 233 | No |

## Issues (0)

No security issues detected.

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
| reference\_missing | `SKILL.md:184-184` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |

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


<!-- ===== skills\n8n-node-configuration ===== -->
# SkillSpector Security Report

**Skill:** n8n\-node\-configuration  
**Source:** `F:\Github Repos\repos\czlonkowski__n8n-skills\skills\n8n-node-configuration`  
**Scanned:** 2026-11-03 15:11:38 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 92/100 |
| Severity | CRITICAL |
| Recommendation | DO NOT INSTALL |

## Components (6)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `DEPENDENCIES.md` | markdown | 943 | No |
| `NATIVE_NODES.md` | markdown | 490 | No |
| `NODE_FAMILY_GOTCHAS.md` | markdown | 243 | No |
| `OPERATION_PATTERNS.md` | markdown | 1269 | No |
| `README.md` | markdown | 364 | No |
| `SKILL.md` | markdown | 559 | No |

## Issues (28)

### 🔴 HIGH: TM1

**Location:** `DEPENDENCIES.md:640`  
**Confidence:** 80%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: AR2

**Location:** `NODE_FAMILY_GOTCHAS.md:20`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:114`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `OPERATION_PATTERNS.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:301`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `OPERATION_PATTERNS.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:533`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `OPERATION_PATTERNS.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:203`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the target's analysis\-completeness ledger and resolve all limitations\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_agent_snooping']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_anti_refusal']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_deserialization']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_excessive_agency']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_harmful_content']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_memory_poisoning']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_privilege_escalation']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_prompt_injection']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_rogue_agent']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_ssrf']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_supply_chain']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_system_prompt_leakage']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `DEPENDENCIES.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:307`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the target's analysis\-completeness ledger and resolve all limitations\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_agent_snooping']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_anti_refusal']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_deserialization']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_excessive_agency']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_harmful_content']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_memory_poisoning']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_privilege_escalation']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_prompt_injection']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_rogue_agent']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_ssrf']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_supply_chain']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_system_prompt_leakage']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `DEPENDENCIES.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:532`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the target's analysis\-completeness ledger and resolve all limitations\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_agent_snooping']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_anti_refusal']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_deserialization']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_excessive_agency']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_harmful_content']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_memory_poisoning']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_privilege_escalation']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_prompt_injection']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_rogue_agent']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_ssrf']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_supply_chain']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_system_prompt_leakage']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `DEPENDENCIES.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:497`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `NATIVE_NODES.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:534`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `NATIVE_NODES.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:524`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Review the target's analysis\-completeness ledger and resolve all limitations\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_agent_snooping']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_anti_refusal']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_deserialization']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_excessive_agency']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_harmful_content']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_memory_poisoning']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_privilege_escalation']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_prompt_injection']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_rogue_agent']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_ssrf']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_supply_chain']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_system_prompt_leakage']}, {'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `NODE_FAMILY_GOTCHAS.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:535`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Review the target's analysis\-completeness ledger and resolve all limitations\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_agent_snooping']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_anti_refusal']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_deserialization']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_excessive_agency']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_harmful_content']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_memory_poisoning']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_privilege_escalation']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_prompt_injection']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_rogue_agent']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_ssrf']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_supply_chain']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_system_prompt_leakage']}, {'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `NODE_FAMILY_GOTCHAS.md`

---

### 🟡 MEDIUM: E1

**Location:** `NATIVE_NODES.md:324`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `OPERATION_PATTERNS.md:33`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `OPERATION_PATTERNS.md:42`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `OPERATION_PATTERNS.md:64`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `OPERATION_PATTERNS.md:76`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `OPERATION_PATTERNS.md:93`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `OPERATION_PATTERNS.md:118`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `OPERATION_PATTERNS.md:136`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `OPERATION_PATTERNS.md:145`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `OPERATION_PATTERNS.md:1104`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `OPERATION_PATTERNS.md:1123`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `OPERATION_PATTERNS.md:1139`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `OPERATION_PATTERNS.md:1206`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `OPERATION_PATTERNS.md:1225`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `README.md:205`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `README.md:218`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | partial |
| Dependency contents | not\_requested |
| Coverage | 16\.7% |
| Fully inspected | 1 |
| Partially inspected | 5 |
| Entirely uninspected | 0 |

### Ledger Exceptions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| obfuscated\_instruction\_text | `DEPENDENCIES.md` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |
| static\_parse\_limit | `NATIVE_NODES.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| obfuscated\_instruction\_text | `NODE_FAMILY_GOTCHAS.md` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |
| static\_parse\_limit | `NODE_FAMILY_GOTCHAS.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| static\_parse\_limit | `OPERATION_PATTERNS.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| obfuscated\_instruction\_text | `SKILL.md` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |
| reference\_missing | `SKILL.md:125-125` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:144-144` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:161-161` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:183-183` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:332-332` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:410-410` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:432-432` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:519-519` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:521-521` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |

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

- **Executable Scripts:** No

*Generated by SkillSpector v2.12.0*


<!-- ===== skills\n8n-self-hosting ===== -->
# SkillSpector Security Report

**Skill:** n8n\-self\-hosting  
**Source:** `F:\Github Repos\repos\czlonkowski__n8n-skills\skills\n8n-self-hosting`  
**Scanned:** 2026-11-03 15:12:05 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 60/100 |
| Severity | HIGH |
| Recommendation | DO NOT INSTALL |

## Components (14)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `CREDENTIAL_OVERWRITES.md` | markdown | 157 | No |
| `DAY2.md` | markdown | 176 | No |
| `QUEUE_MODE.md` | markdown | 173 | No |
| `README.md` | markdown | 110 | No |
| `SECURITY.md` | markdown | 92 | No |
| `SINGLE_MODE.md` | markdown | 72 | No |
| `SKILL.md` | markdown | 189 | No |
| `TASK_RUNNERS.md` | markdown | 186 | No |
| `assets/.env.queue.example` | other | 41 | No |
| `assets/.env.single.example` | other | 32 | No |
| `assets/Caddyfile` | other | 31 | No |
| `assets/docker-compose.queue.yml` | yaml | 185 | No |
| `assets/docker-compose.single.yml` | yaml | 84 | No |
| `assets/init-data.sh` | shell | 17 | Yes |

## Issues (25)

### 🔴 HIGH: PE3

**Location:** `CREDENTIAL_OVERWRITES.md:44`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `DAY2.md:12`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `DAY2.md:49`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `DAY2.md:91`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `DAY2.md:105`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `DAY2.md:131`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `SECURITY.md:28`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `SECURITY.md:35`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `SECURITY.md:36`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `TASK_RUNNERS.md:44`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `assets/.env.queue.example:1`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `assets/.env.single.example:1`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `assets/docker-compose.queue.yml:6`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `assets/docker-compose.single.yml:5`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🟡 MEDIUM: E1

**Location:** `CREDENTIAL_OVERWRITES.md:51`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: RP1

**Location:** `DAY2.md:26`  
**Confidence:** 75%  

**Message:** Docker image referenced without tag or digest: 'docker run \-\-rm'\.

**Remediation:** Pin the image: image:tag or image@sha256:abc123

---

### 🟡 MEDIUM: RP1

**Location:** `DAY2.md:88`  
**Confidence:** 75%  

**Message:** Docker image referenced without tag or digest: 'docker run \-\-rm'\.

**Remediation:** Pin the image: image:tag or image@sha256:abc123

---

### 🟡 MEDIUM: RP1

**Location:** `DAY2.md:103`  
**Confidence:** 75%  

**Message:** Docker image referenced without tag or digest: 'docker run \-\-rm'\.

**Remediation:** Pin the image: image:tag or image@sha256:abc123

---

### 🟡 MEDIUM: RP1

**Location:** `DAY2.md:133`  
**Confidence:** 75%  

**Message:** Docker image referenced without tag or digest: 'docker run \-\-rm'\.

**Remediation:** Pin the image: image:tag or image@sha256:abc123

---

### 🟡 MEDIUM: RP1

**Location:** `TASK_RUNNERS.md:131`  
**Confidence:** 75%  

**Message:** Docker image referenced without tag or digest: 'docker run \-\-rm'\.

**Remediation:** Pin the image: image:tag or image@sha256:abc123

---

### 🟡 MEDIUM: PE2

**Location:** `SKILL.md:8`  
**Confidence:** 70%  

**Message:** Sudo/Root Execution

**Remediation:** Avoid sudo/root unless strictly required\. Prefer least\-privilege patterns\. If elevation is needed, document the justification and scope\.

---

### 🟡 MEDIUM: PE2

**Location:** `SKILL.md:58`  
**Confidence:** 70%  

**Message:** Sudo/Root Execution

**Remediation:** Avoid sudo/root unless strictly required\. Prefer least\-privilege patterns\. If elevation is needed, document the justification and scope\.

---

### 🟡 MEDIUM: E1

**Location:** `SKILL.md:80`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟢 LOW: TM1

**Location:** `DAY2.md:103`  
**Confidence:** 15%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🟢 LOW: TM1

**Location:** `DAY2.md:133`  
**Confidence:** 15%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | complete\_with\_caveats |
| Dependency contents | not\_requested |
| Coverage | 100\.0% |
| Fully inspected | 14 |
| Partially inspected | 0 |
| Entirely uninspected | 0 |

### Ledger Exceptions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| reference\_missing | `SKILL.md:44-44` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:59-59` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:90-90` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:162-162` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |

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

