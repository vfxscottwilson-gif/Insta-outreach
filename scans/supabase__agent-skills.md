# Scans for supabase/agent-skills @ c9be0e9


<!-- ===== skills\supabase ===== -->
# SkillSpector Security Report

**Skill:** supabase  
**Source:** `F:\Github Repos\repos\supabase__agent-skills\skills\supabase`  
**Scanned:** 2026-11-03 15:04:37 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 64/100 |
| Severity | HIGH |
| Recommendation | DO NOT INSTALL |

## Components (4)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `CHANGELOG.md` | markdown | 97 | No |
| `SKILL.md` | markdown | 155 | No |
| `assets/feedback-issue-template.md` | markdown | 17 | No |
| `references/skill-feedback.md` | markdown | 17 | No |

## Issues (13)

### 🔴 HIGH: PE3

**Location:** `CHANGELOG.md:8`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `CHANGELOG.md:20`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `SKILL.md:38`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `SKILL.md:43`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `SKILL.md:43`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `SKILL.md:115`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `SKILL.md:43`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `SKILL.md:92`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `SKILL.md:112`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `SKILL.md:115`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: AS2

**Location:** `SKILL.md:108`  
**Confidence:** 90%  

**Message:** MCP Config Access

**Remediation:** Remove all code or instructions that read MCP configuration files \(such as mcp\.json or claude\_desktop\_config\.json\)\. MCP server details should be managed by the agent runtime, not read by individual skills\.

---

### 🟡 MEDIUM: EA2

**Location:** `SKILL.md:19`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟢 LOW: PE1

**Location:** `SKILL.md:114`  
**Confidence:** 80%  

**Message:** Excessive Permissions

**Remediation:** Request only the minimum permissions required\. Document why each permission is needed\. Remove broad permissions like '\*' or 'all'\.

---

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | complete\_with\_caveats |
| Dependency contents | not\_requested |
| Coverage | 100\.0% |
| Fully inspected | 4 |
| Partially inspected | 0 |
| Entirely uninspected | 0 |

### Ledger Exceptions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| reference\_missing | `SKILL.md:6-6` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:38-38` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:107-107` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:108-108` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:111-111` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:131-131` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |

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


<!-- ===== skills\supabase-postgres-best-practices ===== -->
# SkillSpector Security Report

**Skill:** supabase\-postgres\-best\-practices  
**Source:** `F:\Github Repos\repos\supabase__agent-skills\skills\supabase-postgres-best-practices`  
**Scanned:** 2026-11-03 15:05:14 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 0/100 |
| Severity | LOW |
| Recommendation | SAFE |

## Components (36)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `CHANGELOG.md` | markdown | 73 | No |
| `SKILL.md` | markdown | 64 | No |
| `references/_contributing.md` | markdown | 170 | No |
| `references/_sections.md` | markdown | 39 | No |
| `references/_template.md` | markdown | 34 | No |
| `references/advanced-full-text-search.md` | markdown | 55 | No |
| `references/advanced-jsonb-indexing.md` | markdown | 49 | No |
| `references/conn-idle-timeout.md` | markdown | 46 | No |
| `references/conn-limits.md` | markdown | 44 | No |
| `references/conn-pooling.md` | markdown | 41 | No |
| `references/conn-prepared-statements.md` | markdown | 46 | No |
| `references/data-batch-inserts.md` | markdown | 54 | No |
| `references/data-n-plus-one.md` | markdown | 53 | No |
| `references/data-pagination.md` | markdown | 50 | No |
| `references/data-upsert.md` | markdown | 50 | No |
| `references/lock-advisory.md` | markdown | 56 | No |
| `references/lock-deadlock-prevention.md` | markdown | 68 | No |
| `references/lock-short-transactions.md` | markdown | 50 | No |
| `references/lock-skip-locked.md` | markdown | 54 | No |
| `references/monitor-explain-analyze.md` | markdown | 45 | No |
| `references/monitor-pg-stat-statements.md` | markdown | 55 | No |
| `references/monitor-vacuum-analyze.md` | markdown | 55 | No |
| `references/query-composite-indexes.md` | markdown | 44 | No |
| `references/query-covering-indexes.md` | markdown | 40 | No |
| `references/query-index-types.md` | markdown | 48 | No |
| `references/query-missing-indexes.md` | markdown | 43 | No |
| `references/query-partial-indexes.md` | markdown | 45 | No |
| `references/schema-constraints.md` | markdown | 80 | No |
| `references/schema-data-types.md` | markdown | 46 | No |
| `references/schema-foreign-key-indexes.md` | markdown | 59 | No |
| `references/schema-lowercase-identifiers.md` | markdown | 55 | No |
| `references/schema-partitioning.md` | markdown | 55 | No |
| `references/schema-primary-keys.md` | markdown | 61 | No |
| `references/security-privileges.md` | markdown | 54 | No |
| `references/security-rls-basics.md` | markdown | 50 | No |
| `references/security-rls-performance.md` | markdown | 63 | No |

## Issues (0)

No security issues detected.

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | complete\_with\_caveats |
| Dependency contents | not\_requested |
| Coverage | 100\.0% |
| Fully inspected | 36 |
| Partially inspected | 0 |
| Entirely uninspected | 0 |

### Ledger Exceptions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| reference\_missing | `SKILL.md:7-7` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |

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

