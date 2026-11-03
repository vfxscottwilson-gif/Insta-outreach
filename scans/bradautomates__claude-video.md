# SkillSpector Security Report

**Skill:** watch  
**Source:** `F:\Github Repos\repos\bradautomates__claude-video\skills\watch`  
**Scanned:** 2026-11-03 13:25:42 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 100/100 |
| Severity | CRITICAL |
| Recommendation | DO NOT INSTALL |

## Components (14)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `.gitattributes` | other | 6 | No |
| `.skillignore` | other | 3 | No |
| `SKILL.md` | markdown | 168 | No |
| `scripts/build-skill.sh` | shell | 39 | Yes |
| `scripts/config.py` | python | 174 | Yes |
| `scripts/download.py` | python | 207 | Yes |
| `scripts/frames.py` | python | 758 | Yes |
| `scripts/gemini.py` | python | 162 | Yes |
| `scripts/local_whisperx.py` | python | 147 | Yes |
| `scripts/runtime.py` | python | 35 | Yes |
| `scripts/setup.py` | python | 338 | Yes |
| `scripts/transcribe.py` | python | 113 | Yes |
| `scripts/watch.py` | python | 430 | Yes |
| `scripts/whisper.py` | python | 425 | Yes |

## Issues (22)

### 🔴 HIGH: LP1

**Location:** `scripts/config.py:1`  
**Confidence:** 75%  

**Message:** Code capability 'env' detected in scripts/config\.py but not covered by declared permissions\.

**Remediation:** Review whether the 'env' capability is required and whether the host runtime policy permits it; runtime permissions are unknown unless separately verified\. Remove code that does not need the capability; do not broaden 'allowed\-tools' preapproval solely to silence this finding\.

---

### 🔴 HIGH: LP1

**Location:** `scripts/config.py:1`  
**Confidence:** 75%  

**Message:** Code capability 'file\_write' detected in scripts/config\.py but not covered by declared permissions\.

**Remediation:** Review whether the 'file\_write' capability is required and whether the host runtime policy permits it; runtime permissions are unknown unless separately verified\. Remove code that does not need the capability; do not broaden 'allowed\-tools' preapproval solely to silence this finding\.

---

### 🔴 HIGH: PE3

**Location:** `scripts/config.py:12`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `scripts/config.py:103`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `scripts/config.py:116`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: LP1

**Location:** `scripts/download.py:1`  
**Confidence:** 75%  

**Message:** Code capability 'network' detected in scripts/download\.py but not covered by declared permissions\.

**Remediation:** Review whether the 'network' capability is required and whether the host runtime policy permits it; runtime permissions are unknown unless separately verified\. Remove code that does not need the capability; do not broaden 'allowed\-tools' preapproval solely to silence this finding\.

---

### 🔴 HIGH: E4

**Location:** `scripts/gemini.py:133`  
**Confidence:** 85%  

**Message:** Context Leakage

**Remediation:** Remove any code that sends prompts, responses, or session data externally\. Preserve user privacy; never exfiltrate conversation content\.

---

### 🔴 HIGH: E2

**Location:** `scripts/local_whisperx.py:66`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🟡 MEDIUM: PE2

**Location:** `SKILL.md:34`  
**Confidence:** 70%  

**Message:** Sudo/Root Execution

**Remediation:** Avoid sudo/root unless strictly required\. Prefer least\-privilege patterns\. If elevation is needed, document the justification and scope\.

---

### 🟡 MEDIUM: EA2

**Location:** `SKILL.md:72`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `SKILL.md:104`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: AST4

**Location:** `scripts/frames.py:457`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `scripts/local_whisperx.py:74`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: EA4

**Location:** `scripts/local_whisperx.py:93`  
**Confidence:** 75%  

**Message:** Unbounded Resource Access

**Remediation:** Set explicit rate limits, timeouts, and resource quotas for API calls, file operations, and compute\. Implement circuit breakers for runaway loops\.

---

### 🟡 MEDIUM: EA4

**Location:** `scripts/local_whisperx.py:115`  
**Confidence:** 75%  

**Message:** Unbounded Resource Access

**Remediation:** Set explicit rate limits, timeouts, and resource quotas for API calls, file operations, and compute\. Implement circuit breakers for runaway loops\.

---

### 🟡 MEDIUM: AST4

**Location:** `scripts/runtime.py:28`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `scripts/setup.py:86`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: PE2

**Location:** `scripts/setup.py:104`  
**Confidence:** 70%  

**Message:** Sudo/Root Execution

**Remediation:** Avoid sudo/root unless strictly required\. Prefer least\-privilege patterns\. If elevation is needed, document the justification and scope\.

---

### 🟡 MEDIUM: E5

**Location:** `scripts/watch.py:52`  
**Confidence:** 55%  

**Message:** Cloud Storage Exfiltration

**Remediation:** Verify the destination bucket is trusted and owned by you\. Never upload credentials, secrets, or workspace contents to external or unverified cloud storage\.

---

### 🟡 MEDIUM: E1

**Location:** `scripts/whisper.py:31`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `scripts/whisper.py:34`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟢 LOW: AST7

**Location:** `scripts/watch.py:35`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

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
| reference\_missing | `SKILL.md:7-7` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:21-21` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |

### Analyzer Statuses

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| completed | `artifact_integrity` |  |
| completed | `behavioral_ast` |  |
| completed | `behavioral_taint_tracking` |  |
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
