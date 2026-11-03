# Scans for D4Vinci/Scrapling @ 95cf901


<!-- ===== agent-skill\Scrapling-Skill ===== -->
# SkillSpector Security Report

**Skill:** scrapling\-official  
**Source:** `F:\Github Repos\repos\D4Vinci__Scrapling\agent-skill\Scrapling-Skill`  
**Scanned:** 2026-11-03 15:06:27 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 61/100 |
| Severity | HIGH |
| Recommendation | DO NOT INSTALL |

## Components (25)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `LICENSE.txt` | text | 28 | No |
| `SKILL.md` | markdown | 424 | No |
| `examples/01_fetcher_session.py` | python | 26 | Yes |
| `examples/02_browser_session.py` | python | 26 | Yes |
| `examples/03_stealthy_session.py` | python | 26 | Yes |
| `examples/04_spider.py` | python | 58 | Yes |
| `examples/README.md` | markdown | 33 | No |
| `references/building-rag-systems.md` | markdown | 104 | No |
| `references/fetching/choosing.md` | markdown | 88 | No |
| `references/fetching/static.md` | markdown | 438 | No |
| `references/fetching/stealthy.md` | markdown | 523 | No |
| `references/integrations/scrapy.md` | markdown | 59 | No |
| `references/mcp-server.md` | markdown | 456 | No |
| `references/migrating_from_beautifulsoup.md` | markdown | 91 | No |
| `references/parsing/adaptive.md` | markdown | 219 | No |
| `references/parsing/main_classes.md` | markdown | 556 | No |
| `references/parsing/selection.md` | markdown | 513 | No |
| `references/spiders/advanced.md` | markdown | 427 | No |
| `references/spiders/architecture.md` | markdown | 91 | No |
| `references/spiders/generic-templates.md` | markdown | 271 | No |
| `references/spiders/getting-started.md` | markdown | 179 | No |
| `references/spiders/platform-templates.md` | markdown | 50 | No |
| `references/spiders/proxy-blocking.md` | markdown | 239 | No |
| `references/spiders/requests-responses.md` | markdown | 196 | No |
| `references/spiders/sessions.md` | markdown | 221 | No |

## Issues (19)

### 🟡 MEDIUM: LP3

**Location:** `SKILL.md:1`  
**Confidence:** 70%  

**Message:** Skill declares no tool scope \('permissions' or 'allowed\-tools'\) but code capabilities were detected: network\.

**Remediation:** Clarify the skill's intended tool scope and review how the host runtime enforces it; runtime permissions are unknown unless separately verified\. For Claude Code / Agent Skills SKILL\.md, 'allowed\-tools' records preapproved tools, not a permission ceiling; add a tool only when it is independently approved as necessary, not to silence this finding\. For MCP server manifests, use a 'permissions' list naming the required capabilities\.

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:57`  
**Confidence:** 75%  

**Message:** Docker image referenced without tag or digest: 'docker pull pyd4vinci/scrapling'\.

**Remediation:** Pin the image: image:tag or image@sha256:abc123

---

### 🟡 MEDIUM: RP1

**Location:** `references/mcp-server.md:97`  
**Confidence:** 75%  

**Message:** Docker image referenced without tag or digest: 'docker pull pyd4vinci/scrapling'\.

**Remediation:** Pin the image: image:tag or image@sha256:abc123

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:61`  
**Confidence:** 75%  

**Message:** Docker image referenced without tag or digest: 'docker pull ghcr\.io/d4vinci/scrapling:latest'\.

**Remediation:** Pin the image: image:tag or image@sha256:abc123

---

### 🟡 MEDIUM: RP1

**Location:** `references/mcp-server.md:101`  
**Confidence:** 75%  

**Message:** Docker image referenced without tag or digest: 'docker pull ghcr\.io/d4vinci/scrapling:latest'\.

**Remediation:** Pin the image: image:tag or image@sha256:abc123

---

### 🟡 MEDIUM: TM3

**Location:** `SKILL.md:308`  
**Confidence:** 60%  

**Message:** Unsafe Defaults

**Remediation:** Override unsafe defaults with secure settings \(verify=True, auth required, restrictive permissions\)\. Review and harden all tool configurations\.

---

### 🟡 MEDIUM: TM3

**Location:** `references/spiders/advanced.md:165`  
**Confidence:** 60%  

**Message:** Unsafe Defaults

**Remediation:** Override unsafe defaults with secure settings \(verify=True, auth required, restrictive permissions\)\. Review and harden all tool configurations\.

---

### 🟡 MEDIUM: TM3

**Location:** `references/spiders/advanced.md:171`  
**Confidence:** 60%  

**Message:** Unsafe Defaults

**Remediation:** Override unsafe defaults with secure settings \(verify=True, auth required, restrictive permissions\)\. Review and harden all tool configurations\.

---

### 🟡 MEDIUM: TM3

**Location:** `references/spiders/advanced.md:187`  
**Confidence:** 60%  

**Message:** Unsafe Defaults

**Remediation:** Override unsafe defaults with secure settings \(verify=True, auth required, restrictive permissions\)\. Review and harden all tool configurations\.

---

### 🟡 MEDIUM: TM3

**Location:** `references/spiders/advanced.md:204`  
**Confidence:** 60%  

**Message:** Unsafe Defaults

**Remediation:** Override unsafe defaults with secure settings \(verify=True, auth required, restrictive permissions\)\. Review and harden all tool configurations\.

---

### 🟡 MEDIUM: P9

**Location:** `references/fetching/choosing.md:19`  
**Confidence:** 70%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🟡 MEDIUM: E1

**Location:** `references/fetching/static.md:96`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `references/fetching/static.md:104`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `references/fetching/static.md:189`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: P9

**Location:** `references/fetching/stealthy.md:91`  
**Confidence:** 70%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🟡 MEDIUM: RP1

**Location:** `references/mcp-server.md:248`  
**Confidence:** 75%  

**Message:** Docker image referenced without tag or digest: 'docker run \-p'\.

**Remediation:** Pin the image: image:tag or image@sha256:abc123

---

### 🟡 MEDIUM: EA1

**Location:** `references/mcp-server.md:253`  
**Confidence:** 80%  

**Message:** Unrestricted Tool Access

**Remediation:** Restrict tool access to only the tools required for the skill's stated purpose\. Use an explicit allowlist rather than granting blanket access\.

---

### 🟡 MEDIUM: E1

**Location:** `references/spiders/sessions.md:145`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟢 LOW: EA3

**Location:** `LICENSE.txt:24`  
**Confidence:** 70%  

**Message:** Scope Creep

**Remediation:** Limit the skill's scope to its documented purpose\. Remove instructions that enable the agent to perform actions outside its stated functionality\.

---

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | partial |
| Dependency contents | not\_requested |
| Coverage | 96\.0% |
| Fully inspected | 24 |
| Partially inspected | 1 |
| Entirely uninspected | 0 |

### Ledger Exceptions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| reference\_missing | `SKILL.md:4-4` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:279-279` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:304-304` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:327-327` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| static\_parse\_limit | `references/spiders/requests-responses.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |

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
| degraded | `static_patterns_tool_misuse` |  |
| completed | `static_yara` |  |

### Limitations

- Analyzer static\_patterns\_tool\_misuse status: degraded\.

## Metadata

- **Executable Scripts:** Yes

*Generated by SkillSpector v2.12.0*

