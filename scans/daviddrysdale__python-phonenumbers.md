# SkillSpector Security Report

**Skill:** unknown  
**Source:** `C:\Users\KHIZAR~1\AppData\Local\Temp\claude\42cf0048dc063c0d\b840f765-60a8-4e1f-a070-0a7e8f2665d3\scratchpad\pn`  
**Scanned:** 2026-11-11 16:06:23 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 100/100 |
| Severity | CRITICAL |
| Recommendation | DO NOT INSTALL |

## Components (29)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `python/appspot.py` | python | 210 | Yes |
| `python/phonenumbers/__init__.py` | python | 228 | Yes |
| `python/phonenumbers/asyoutypeformatter.py` | python | 609 | Yes |
| `python/phonenumbers/carrier.py` | python | 145 | Yes |
| `python/phonenumbers/geocoder.py` | python | 225 | Yes |
| `python/phonenumbers/phonemetadata.py` | python | 640 | Yes |
| `python/phonenumbers/phonenumber.py` | python | 277 | Yes |
| `python/phonenumbers/phonenumbermatcher.py` | python | 787 | Yes |
| `python/phonenumbers/phonenumberutil.py` | python | 3405 | Yes |
| `python/phonenumbers/prefix.py` | python | 89 | Yes |
| `python/phonenumbers/re_util.py` | python | 84 | Yes |
| `python/phonenumbers/shortnumberinfo.py` | python | 462 | Yes |
| `python/phonenumbers/timezone.py` | python | 121 | Yes |
| `python/phonenumbers/unicode_util.py` | python | 414 | Yes |
| `python/phonenumbers/util.py` | python | 184 | Yes |
| `python/pyproject.toml` | toml | 56 | No |
| `python/run_stubtest.py` | python | 13 | Yes |
| `python/setup.py` | python | 19 | Yes |
| `python/testpb2.py` | python | 9 | Yes |
| `python/testwrapper.py` | python | 29 | Yes |
| `tools/python/.gitignore` | other | 2 | No |
| `tools/python/DumpLocale.java` | other | 109 | No |
| `tools/python/README.md` | markdown | 151 | No |
| `tools/python/allcheck.py` | python | 55 | Yes |
| `tools/python/buildmetadatafromxml.py` | python | 729 | Yes |
| `tools/python/buildprefixdata.py` | python | 270 | Yes |
| `tools/python/checkupstreamversion.py` | python | 47 | Yes |
| `tools/python/issue294.py` | python | 2 | Yes |
| `tools/python/makefile` | other | 184 | No |

## Issues (44)

### 🔴 HIGH: E4

**Location:** `python/phonenumbers/phonenumberutil.py:3133`  
**Confidence:** 75%  

**Message:** Context Leakage

**Remediation:** Remove any code that sends prompts, responses, or session data externally\. Preserve user privacy; never exfiltrate conversation content\.

---

### 🔴 HIGH: TM2

**Location:** `tools/python/README.md:140`  
**Confidence:** 75%  

**Message:** Chaining Abuse

**Remediation:** Limit tool chaining depth and validate the output of each tool before passing it to the next\. Require explicit user approval for multi\-step chains\.

---

### 🔴 HIGH: TM2

**Location:** `tools/python/README.md:147`  
**Confidence:** 75%  

**Message:** Chaining Abuse

**Remediation:** Limit tool chaining depth and validate the output of each tool before passing it to the next\. Require explicit user approval for multi\-step chains\.

---

### 🔴 HIGH: TM2

**Location:** `tools/python/makefile:106`  
**Confidence:** 75%  

**Message:** Chaining Abuse

**Remediation:** Limit tool chaining depth and validate the output of each tool before passing it to the next\. Require explicit user approval for multi\-step chains\.

---

### 🔴 HIGH: TM1

**Location:** `tools/python/makefile:111`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `tools/python/makefile:112`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `tools/python/makefile:113`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `tools/python/makefile:114`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `tools/python/makefile:115`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `tools/python/makefile:133`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `tools/python/makefile:116`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `tools/python/makefile:117`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `tools/python/makefile:118`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `tools/python/makefile:119`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `tools/python/makefile:120`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `tools/python/makefile:121`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `tools/python/makefile:134`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `tools/python/makefile:122`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `tools/python/makefile:123`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `tools/python/makefile:124`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `tools/python/makefile:125`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `tools/python/makefile:126`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `tools/python/makefile:127`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `tools/python/makefile:142`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `tools/python/makefile:130`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `tools/python/makefile:131`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `tools/python/makefile:132`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `tools/python/makefile:135`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `tools/python/makefile:136`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `tools/python/makefile:137`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `tools/python/makefile:140`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `tools/python/makefile:141`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `tools/python/makefile:184`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🟡 MEDIUM: P9

**Location:** `python/phonenumbers/phonenumberutil.py:2685`  
**Confidence:** 70%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🟡 MEDIUM: P9

**Location:** `python/phonenumbers/phonenumberutil.py:2991`  
**Confidence:** 70%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🟡 MEDIUM: P9

**Location:** `python/phonenumbers/phonenumberutil.py:2992`  
**Confidence:** 70%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🟡 MEDIUM: P9

**Location:** `python/phonenumbers/phonenumberutil.py:2993`  
**Confidence:** 70%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🟡 MEDIUM: P9

**Location:** `python/phonenumbers/phonenumberutil.py:3023`  
**Confidence:** 70%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🟡 MEDIUM: PE2

**Location:** `tools/python/README.md:16`  
**Confidence:** 70%  

**Message:** Sudo/Root Execution

**Remediation:** Avoid sudo/root unless strictly required\. Prefer least\-privilege patterns\. If elevation is needed, document the justification and scope\.

---

### 🟡 MEDIUM: P9

**Location:** `tools/python/buildmetadatafromxml.py:256`  
**Confidence:** 70%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🟡 MEDIUM: P9

**Location:** `tools/python/buildmetadatafromxml.py:271`  
**Confidence:** 70%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🟡 MEDIUM: E1

**Location:** `tools/python/checkupstreamversion.py:12`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: PE2

**Location:** `tools/python/makefile:106`  
**Confidence:** 70%  

**Message:** Sudo/Root Execution

**Remediation:** Avoid sudo/root unless strictly required\. Prefer least\-privilege patterns\. If elevation is needed, document the justification and scope\.

---

### 🟢 LOW: SC4

**Location:** `python/pyproject.toml:36`  
**Confidence:** 40%  

**Message:** Unverifiable Dependency: setuptools has 11 known advisory\(ies\) \(CVE\-2013\-1633 \(Setuptools vulnerable to Man\-in\-the\-middle attacks\); CVE\-2025\-47273 \(setuptools has a path traversal vulnerability in PackageIndex\.download that lead\); CVE\-2024\-6345 \(setuptools vulnerable to Command Injection via package URL\) \+8 more\), but the manifest does not pin a version, so it is unknown whether the installed release is affected

**Remediation:** Determine the dependency's exact resolved version from the environment or lockfile and compare it with the advisories in OSV \(osv\.dev\)\. If it is affected, use a verified fixed release or remove or replace the dependency when no fix is available\.

---

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | complete |
| Dependency contents | not\_requested |
| Coverage | 100\.0% |
| Fully inspected | 29 |
| Partially inspected | 0 |
| Entirely uninspected | 0 |

### Analyzer Statuses

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| completed | `artifact_integrity` |  |
| completed | `behavioral_ast` |  |
| completed | `behavioral_taint_tracking` |  |
| no\_applicable\_files | `bundled_execution_surface` | No files matched this analyzer's applicability contract\. |
| manifest\_absent | `mcp_least_privilege` | No compatible manifest was present for this analyzer\. |
| completed | `mcp_rug_pull` |  |
| manifest\_absent | `mcp_tool_poisoning` | No compatible manifest was present for this analyzer\. |
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
