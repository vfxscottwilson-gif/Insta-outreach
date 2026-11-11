# SkillSpector Security Report

**Skill:** unknown  
**Source:** `F:\Github Repos\repos\JoshData__python-email-validator`  
**Scanned:** 2026-11-11 15:57:50 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 88/100 |
| Severity | CRITICAL |
| Recommendation | DO NOT INSTALL |

## Components (44)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `.git/config` | other | 13 | No |
| `.github/workflows/test_and_build.yaml` | yaml | 31 | No |
| `.gitignore` | other | 22 | No |
| `CHANGELOG.md` | markdown | 187 | No |
| `CONTRIBUTING.md` | markdown | 7 | No |
| `LICENSE` | other | 27 | No |
| `MANIFEST.in` | other | 2 | No |
| `Makefile` | other | 44 | No |
| `README.md` | markdown | 440 | No |
| `email_validator/__init__.py` | python | 103 | Yes |
| `email_validator/__main__.py` | python | 66 | Yes |
| `email_validator/deliverability.py` | python | 159 | Yes |
| `email_validator/exceptions.py` | python | 13 | Yes |
| `email_validator/py.typed` | other | 0 | No |
| `email_validator/rfc_constants.py` | python | 63 | Yes |
| `email_validator/syntax.py` | python | 855 | Yes |
| `email_validator/types.py` | python | 127 | Yes |
| `email_validator/validate_email.py` | python | 207 | Yes |
| `email_validator/version.py` | python | 1 | Yes |
| `pyproject.toml` | toml | 17 | No |
| `release_to_pypi.sh` | shell | 6 | Yes |
| `setup.cfg` | other | 48 | No |
| `setup.py` | python | 2 | Yes |
| `test_requirements.txt` | text | 29 | No |
| `tests/conftest.py` | python | 21 | Yes |
| `tests/mocked-dns-answers.json` | json | 192 | No |
| `tests/mocked_dns_response.py` | python | 127 | Yes |
| `tests/test_deliverability.py` | python | 92 | Yes |
| `tests/test_main.py` | python | 154 | Yes |
| `tests/test_syntax.py` | python | 886 | Yes |
| `.git/hooks/applypatch-msg.sample` | other | 0 | Yes |
| `.git/hooks/commit-msg.sample` | other | 0 | Yes |
| `.git/hooks/fsmonitor-watchman.sample` | other | 0 | Yes |
| `.git/hooks/post-update.sample` | other | 0 | Yes |
| `.git/hooks/pre-applypatch.sample` | other | 0 | Yes |
| `.git/hooks/pre-commit.sample` | other | 0 | Yes |
| `.git/hooks/pre-merge-commit.sample` | other | 0 | Yes |
| `.git/hooks/pre-push.sample` | other | 0 | Yes |
| `.git/hooks/pre-rebase.sample` | other | 0 | Yes |
| `.git/hooks/pre-receive.sample` | other | 0 | Yes |
| `.git/hooks/prepare-commit-msg.sample` | other | 0 | Yes |
| `.git/hooks/push-to-checkout.sample` | other | 0 | Yes |
| `.git/hooks/sendemail-validate.sample` | other | 0 | Yes |
| `.git/hooks/update.sample` | other | 0 | Yes |

## Issues (8)

### 🔴 HIGH: P3

**Location:** `README.md:378`  
**Confidence:** 90%  

**Message:** Exfiltration Commands

**Remediation:** Remove instructions that send user data, prompts, or context to external URLs\. If telemetry is needed, use documented, privacy\-preserving methods\.

---

### 🔴 HIGH: P3

**Location:** `email_validator/types.py:37–38`  
**Confidence:** 90%  

**Message:** Exfiltration Commands

**Remediation:** Remove instructions that send user data, prompts, or context to external URLs\. If telemetry is needed, use documented, privacy\-preserving methods\.

---

### 🔴 HIGH: PE5

**Location:** `test_requirements.txt:2`  
**Confidence:** 80%  

**Message:** Privileged Container / Container Escape

**Remediation:** Review the flagged content for security risks\. Ensure no credentials, secrets, or sensitive data are exposed\.

---

### 🟡 MEDIUM: PE2

**Location:** `test_requirements.txt:2`  
**Confidence:** 70%  

**Message:** Sudo/Root Execution

**Remediation:** Avoid sudo/root unless strictly required\. Prefer least\-privilege patterns\. If elevation is needed, document the justification and scope\.

---

### 🟡 MEDIUM: RP1

**Location:** `test_requirements.txt:2`  
**Confidence:** 75%  

**Message:** Docker image referenced without tag or digest: 'docker run \-\-rm'\.

**Remediation:** Pin the image: image:tag or image@sha256:abc123

---

### 🟡 MEDIUM: AE4

**Location:** `tests/test_syntax.py:1`  
**Confidence:** 80%  

**Message:** Suspicious Unicode normalization or mixed\-script content

**Remediation:** Review the flagged content for security risks\. Ensure no credentials, secrets, or sensitive data are exposed\.

---

### 🟢 LOW: EA3

**Location:** `LICENSE:19`  
**Confidence:** 70%  

**Message:** Scope Creep

**Remediation:** Limit the skill's scope to its documented purpose\. Remove instructions that enable the agent to perform actions outside its stated functionality\.

---

### 🟢 LOW: AST7

**Location:** `email_validator/types.py:113`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | complete |
| Dependency contents | not\_requested |
| Coverage | 100\.0% |
| Fully inspected | 30 |
| Partially inspected | 0 |
| Entirely uninspected | 0 |

### Scope Exclusions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| vcs\_metadata | `.git/HEAD` | VCS object and history metadata is outside the bounded artifact inspection profile\. |
| vcs\_metadata | `.git/description` | VCS object and history metadata is outside the bounded artifact inspection profile\. |
| vcs\_metadata | `.git/hooks/applypatch-msg.sample` | VCS object and history metadata is outside the bounded artifact inspection profile\. |
| vcs\_metadata | `.git/hooks/commit-msg.sample` | VCS object and history metadata is outside the bounded artifact inspection profile\. |
| vcs\_metadata | `.git/hooks/fsmonitor-watchman.sample` | VCS object and history metadata is outside the bounded artifact inspection profile\. |
| vcs\_metadata | `.git/hooks/post-update.sample` | VCS object and history metadata is outside the bounded artifact inspection profile\. |
| vcs\_metadata | `.git/hooks/pre-applypatch.sample` | VCS object and history metadata is outside the bounded artifact inspection profile\. |
| vcs\_metadata | `.git/hooks/pre-commit.sample` | VCS object and history metadata is outside the bounded artifact inspection profile\. |
| vcs\_metadata | `.git/hooks/pre-merge-commit.sample` | VCS object and history metadata is outside the bounded artifact inspection profile\. |
| vcs\_metadata | `.git/hooks/pre-push.sample` | VCS object and history metadata is outside the bounded artifact inspection profile\. |
| vcs\_metadata | `.git/hooks/pre-rebase.sample` | VCS object and history metadata is outside the bounded artifact inspection profile\. |
| vcs\_metadata | `.git/hooks/pre-receive.sample` | VCS object and history metadata is outside the bounded artifact inspection profile\. |
| vcs\_metadata | `.git/hooks/prepare-commit-msg.sample` | VCS object and history metadata is outside the bounded artifact inspection profile\. |
| vcs\_metadata | `.git/hooks/push-to-checkout.sample` | VCS object and history metadata is outside the bounded artifact inspection profile\. |
| vcs\_metadata | `.git/hooks/sendemail-validate.sample` | VCS object and history metadata is outside the bounded artifact inspection profile\. |
| vcs\_metadata | `.git/hooks/update.sample` | VCS object and history metadata is outside the bounded artifact inspection profile\. |
| vcs\_metadata | `.git/index` | VCS object and history metadata is outside the bounded artifact inspection profile\. |
| vcs\_metadata | `.git/info/` | VCS object and history metadata is outside the bounded artifact inspection profile\. |
| vcs\_metadata | `.git/logs/` | VCS object and history metadata is outside the bounded artifact inspection profile\. |
| vcs\_metadata | `.git/objects/` | VCS object and history metadata is outside the bounded artifact inspection profile\. |
| vcs\_metadata | `.git/packed-refs` | VCS object and history metadata is outside the bounded artifact inspection profile\. |
| vcs\_metadata | `.git/refs/` | VCS object and history metadata is outside the bounded artifact inspection profile\. |
| vcs\_metadata | `.git/shallow` | VCS object and history metadata is outside the bounded artifact inspection profile\. |

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
