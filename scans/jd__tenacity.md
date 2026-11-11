# SkillSpector Security Report

**Skill:** unknown  
**Source:** `F:\Github Repos\repos\jd__tenacity`  
**Scanned:** 2026-11-11 15:51:51 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 47/100 |
| Severity | MEDIUM |
| Recommendation | CAUTION |

## Components (112)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `.editorconfig` | other | 22 | No |
| `.git/config` | other | 13 | No |
| `.github/dependabot.yml` | yaml | 21 | No |
| `.github/workflows/ci.yaml` | yaml | 81 | No |
| `.github/workflows/release.yml` | yaml | 26 | No |
| `.gitignore` | other | 13 | No |
| `.mergify.yml` | yaml | 6 | No |
| `.readthedocs.yml` | yaml | 11 | No |
| `LICENSE` | other | 202 | No |
| `README.rst` | other | 1 | No |
| `doc/source/api.rst` | other | 84 | No |
| `doc/source/changelog.rst` | other | 4 | No |
| `doc/source/conf.py` | python | 29 | Yes |
| `doc/source/index.rst` | other | 790 | No |
| `pyproject.toml` | toml | 151 | No |
| `releasenotes/notes/Fix-tests-for-typeguard-3.x-6eebfea546b6207e.yaml` | yaml | 3 | No |
| `releasenotes/notes/Use--for-formatting-and-validate-using-black-39ec9d57d4691778.yaml` | yaml | 4 | No |
| `releasenotes/notes/add-async-actions-b249c527d99723bb.yaml` | yaml | 5 | No |
| `releasenotes/notes/add-re-pattern-to-match-types-6a4c1d9e64e2a5e1.yaml` | yaml | 4 | No |
| `releasenotes/notes/add-reno-d1ab5710f272650a.yaml` | yaml | 3 | No |
| `releasenotes/notes/add-retry_except_exception_type-31b31da1924d55f4.yaml` | yaml | 3 | No |
| `releasenotes/notes/add-stop-before-delay-a775f88ac872c923.yaml` | yaml | 7 | No |
| `releasenotes/notes/add-test-extra-55e869261b03e56d.yaml` | yaml | 3 | No |
| `releasenotes/notes/add_omitted_modules_to_import_all-2ab282f20a2c22f7.yaml` | yaml | 3 | No |
| `releasenotes/notes/add_retry_if_exception_cause_type-d16b918ace4ae0ad.yaml` | yaml | 5 | No |
| `releasenotes/notes/added_a_link_to_documentation-eefaf8f074b539f8.yaml` | yaml | 5 | No |
| `releasenotes/notes/after_log-50f4d73b24ce9203.yaml` | yaml | 3 | No |
| `releasenotes/notes/allow-mocking-of-nap-sleep-6679c50e702446f1.yaml` | yaml | 3 | No |
| `releasenotes/notes/annotate_code-197b93130df14042.yaml` | yaml | 3 | No |
| `releasenotes/notes/async-sleep-retrying-32de5866f5d041.yaml` | yaml | 7 | No |
| `releasenotes/notes/before_sleep_log-improvements-d8149274dfb37d7c.yaml` | yaml | 3 | No |
| `releasenotes/notes/clarify-reraise-option-6829667eacf4f599.yaml` | yaml | 3 | No |
| `releasenotes/notes/dependabot-for-github-actions-4d2464f3c0928463.yaml` | yaml | 5 | No |
| `releasenotes/notes/deprecate-initial-for-multiplier-c7b4e2d9f1a83065.yaml` | yaml | 10 | No |
| `releasenotes/notes/do_not_package_tests-fe5ac61940b0a5ed.yaml` | yaml | 3 | No |
| `releasenotes/notes/docs-asyncio-getaddrinfo-b8a1e40370dc.yaml` | yaml | 3 | No |
| `releasenotes/notes/docs-retry-with-statistics-a713ed405a19.yaml` | yaml | 3 | No |
| `releasenotes/notes/drop-deprecated-python-versions-69a05cb2e0f1034c.yaml` | yaml | 4 | No |
| `releasenotes/notes/drop-python-3.9-ecfa2d7db9773e96.yaml` | yaml | 5 | No |
| `releasenotes/notes/drop_deprecated-7ea90b212509b082.yaml` | yaml | 5 | No |
| `releasenotes/notes/export-convenience-symbols-981d9611c8b754f3.yaml` | yaml | 3 | No |
| `releasenotes/notes/falsy-callable-wait-3c1e7d2a9b5f4e60.yaml` | yaml | 6 | No |
| `releasenotes/notes/fix-async-loop-with-result-f68e913ccb425aca.yaml` | yaml | 4 | No |
| `releasenotes/notes/fix-async-retry-type-overloads-27f3e0c239ed6b.yaml` | yaml | 9 | No |
| `releasenotes/notes/fix-decorated-method-binding-729ace6e58a9fefa.yaml` | yaml | 11 | No |
| `releasenotes/notes/fix-exception-message-empty-string-7b1e9c4a2f6d0835.yaml` | yaml | 9 | No |
| `releasenotes/notes/fix-exponential-max-computation-526.yaml` | yaml | 5 | No |
| `releasenotes/notes/fix-exponential-multiplier-underflow-4fd1d6d6b9c8e2a1.yaml` | yaml | 5 | No |
| `releasenotes/notes/fix-falsy-wait-regression-3b7e91c4a5d20f68.yaml` | yaml | 17 | No |
| `releasenotes/notes/fix-local-context-overwrite-94190ba06a481631.yaml` | yaml | 4 | No |
| `releasenotes/notes/fix-reraise-tryagain-underlying-exc-e21a26ee95bad0b3.yaml` | yaml | 8 | No |
| `releasenotes/notes/fix-retry-wrapper-attributes-f7a3a45b8e90f257.yaml` | yaml | 6 | No |
| `releasenotes/notes/fix-setuptools-config-3af71aa3592b6948.yaml` | yaml | 3 | No |
| `releasenotes/notes/fix-statistics-through-outer-decorator-b8a6d6b9a6a70833.yaml` | yaml | 8 | No |
| `releasenotes/notes/fix-tornado-global-desync-8c2d40fa71b9e35a.yaml` | yaml | 7 | No |
| `releasenotes/notes/fix-wait-chain-empty-strategies-d3a8f7c2b1e4f569.yaml` | yaml | 8 | No |
| `releasenotes/notes/fix-wait-typing-b26eecdb6cc0a1de.yaml` | yaml | 5 | No |
| `releasenotes/notes/fix_async-52b6594c8e75c4bc.yaml` | yaml | 3 | No |
| `releasenotes/notes/logging-protocol-a4cf0f786f21e4ee.yaml` | yaml | 5 | No |
| `releasenotes/notes/make-logger-more-compatible-5da1ddf1bab77047.yaml` | yaml | 4 | No |
| `releasenotes/notes/no-async-iter-6132a42e52348a75.yaml` | yaml | 7 | No |
| `releasenotes/notes/pr320-py3-only-wheel-tag.yaml` | yaml | 5 | No |
| `releasenotes/notes/py36_plus-c425fb3aa17c6682.yaml` | yaml | 4 | No |
| `releasenotes/notes/pypi-description-6ec0eae827f64adc.yaml` | yaml | 5 | No |
| `releasenotes/notes/remove-py36-876c0416cf279d15.yaml` | yaml | 4 | No |
| `releasenotes/notes/retrycallstate-repr-94947f7b00ee15e1.yaml` | yaml | 3 | No |
| `releasenotes/notes/some-slug-for-preserve-defaults-86682846dfa18005.yaml` | yaml | 4 | No |
| `releasenotes/notes/sphinx_define_error-642c9cd5c165d39a.yaml` | yaml | 2 | No |
| `releasenotes/notes/support-py3.14-14928188cab53b99.yaml` | yaml | 3 | No |
| `releasenotes/notes/support-py3.15-a1ed09aae1bf19b0.yaml` | yaml | 3 | No |
| `releasenotes/notes/support-timedelta-wait-unit-type-5ba1e9fc0fe45523.yaml` | yaml | 3 | No |
| `releasenotes/notes/timedelta-for-stop-ef6bf71b88ce9988.yaml` | yaml | 4 | No |
| `releasenotes/notes/trio-support-retry-22bd544800cd1f36.yaml` | yaml | 6 | No |
| `releasenotes/notes/wait-exponential-jitter-min-timedelta-a8e3c1f4b7d29e50.yaml` | yaml | 6 | No |
| `releasenotes/notes/wait-radd-int-6f1a3c9d84b2e057.yaml` | yaml | 8 | No |
| `releasenotes/notes/wait-random-exponential-min-2a4b7eed9f002436.yaml` | yaml | 4 | No |
| `releasenotes/notes/wait_exponential_jitter-6ffc81dddcbaa6d3.yaml` | yaml | 5 | No |
| `reno.yaml` | yaml | 2 | No |
| `tenacity/__init__.py` | python | 872 | Yes |
| `tenacity/_utils.py` | python | 132 | Yes |
| `tenacity/after.py` | python | 46 | Yes |
| `tenacity/asyncio/__init__.py` | python | 249 | Yes |
| `tenacity/asyncio/retry.py` | python | 148 | Yes |
| `tenacity/before.py` | python | 42 | Yes |
| `tenacity/before_sleep.py` | python | 66 | Yes |
| `tenacity/nap.py` | python | 43 | Yes |
| `tenacity/py.typed` | other | 0 | No |
| `tenacity/retry.py` | python | 315 | Yes |
| `tenacity/stop.py` | python | 138 | Yes |
| `tenacity/tornadoweb.py` | python | 64 | Yes |
| `tenacity/wait.py` | python | 327 | Yes |
| `tests/__init__.py` | python | 0 | Yes |
| `tests/test_after.py` | python | 86 | Yes |
| `tests/test_asyncio.py` | python | 662 | Yes |
| `tests/test_issue_478.py` | python | 116 | Yes |
| `tests/test_tenacity.py` | python | 2427 | Yes |
| `tests/test_tornado.py` | python | 91 | Yes |
| `tests/test_utils.py` | python | 57 | Yes |
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

## Issues (15)

### 🟡 MEDIUM: RP1

**Location:** `.github/workflows/ci.yaml:68`  
**Confidence:** 65%  

**Message:** MCP server referenced without pinned version: 'uvx twine'\.

**Remediation:** Pin the version: uvx package\-name==1\.2\.3

---

### 🟡 MEDIUM: E1

**Location:** `doc/source/index.rst:12`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: EA4

**Location:** `doc/source/index.rst:97`  
**Confidence:** 75%  

**Message:** Unbounded Resource Access

**Remediation:** Set explicit rate limits, timeouts, and resource quotas for API calls, file operations, and compute\. Implement circuit breakers for runaway loops\.

---

### 🟡 MEDIUM: EA4

**Location:** `doc/source/index.rst:104`  
**Confidence:** 75%  

**Message:** Unbounded Resource Access

**Remediation:** Set explicit rate limits, timeouts, and resource quotas for API calls, file operations, and compute\. Implement circuit breakers for runaway loops\.

---

### 🟡 MEDIUM: EA4

**Location:** `doc/source/index.rst:228`  
**Confidence:** 75%  

**Message:** Unbounded Resource Access

**Remediation:** Set explicit rate limits, timeouts, and resource quotas for API calls, file operations, and compute\. Implement circuit breakers for runaway loops\.

---

### 🟡 MEDIUM: EA4

**Location:** `doc/source/index.rst:233`  
**Confidence:** 75%  

**Message:** Unbounded Resource Access

**Remediation:** Set explicit rate limits, timeouts, and resource quotas for API calls, file operations, and compute\. Implement circuit breakers for runaway loops\.

---

### 🟡 MEDIUM: EA4

**Location:** `doc/source/index.rst:273`  
**Confidence:** 75%  

**Message:** Unbounded Resource Access

**Remediation:** Set explicit rate limits, timeouts, and resource quotas for API calls, file operations, and compute\. Implement circuit breakers for runaway loops\.

---

### 🟡 MEDIUM: AST10

**Location:** `tests/test_tenacity.py:2271`  
**Confidence:** 70%  

**Message:** Insecure deserialization: pickle\.loads\(\)

**Remediation:** Never deserialize untrusted input with pickle/marshal/dill/jsonpickle/joblib\. Use a data\-only format such as JSON\. For YAML use yaml\.safe\_load; for PyTorch use torch\.load\(\.\.\., weights\_only=True\); for numpy avoid allow\_pickle=True\. If a binary format is unavoidable, verify an HMAC/signature over the bytes before loading\.

---

### 🟡 MEDIUM: AST10

**Location:** `tests/test_tenacity.py:2375`  
**Confidence:** 70%  

**Message:** Insecure deserialization: pickle\.loads\(\)

**Remediation:** Never deserialize untrusted input with pickle/marshal/dill/jsonpickle/joblib\. Use a data\-only format such as JSON\. For YAML use yaml\.safe\_load; for PyTorch use torch\.load\(\.\.\., weights\_only=True\); for numpy avoid allow\_pickle=True\. If a binary format is unavoidable, verify an HMAC/signature over the bytes before loading\.

---

### 🟡 MEDIUM: AST10

**Location:** `tests/test_tenacity.py:2385`  
**Confidence:** 70%  

**Message:** Insecure deserialization: pickle\.loads\(\)

**Remediation:** Never deserialize untrusted input with pickle/marshal/dill/jsonpickle/joblib\. Use a data\-only format such as JSON\. For YAML use yaml\.safe\_load; for PyTorch use torch\.load\(\.\.\., weights\_only=True\); for numpy avoid allow\_pickle=True\. If a binary format is unavoidable, verify an HMAC/signature over the bytes before loading\.

---

### 🟡 MEDIUM: AST10

**Location:** `tests/test_tenacity.py:2400`  
**Confidence:** 70%  

**Message:** Insecure deserialization: pickle\.loads\(\)

**Remediation:** Never deserialize untrusted input with pickle/marshal/dill/jsonpickle/joblib\. Use a data\-only format such as JSON\. For YAML use yaml\.safe\_load; for PyTorch use torch\.load\(\.\.\., weights\_only=True\); for numpy avoid allow\_pickle=True\. If a binary format is unavoidable, verify an HMAC/signature over the bytes before loading\.

---

### 🟡 MEDIUM: AST10

**Location:** `tests/test_tenacity.py:2410`  
**Confidence:** 70%  

**Message:** Insecure deserialization: pickle\.loads\(\)

**Remediation:** Never deserialize untrusted input with pickle/marshal/dill/jsonpickle/joblib\. Use a data\-only format such as JSON\. For YAML use yaml\.safe\_load; for PyTorch use torch\.load\(\.\.\., weights\_only=True\); for numpy avoid allow\_pickle=True\. If a binary format is unavoidable, verify an HMAC/signature over the bytes before loading\.

---

### 🟢 LOW: SC4

**Location:** `pyproject.toml:58`  
**Confidence:** 40%  

**Message:** Unverifiable Dependency: pytest has 2 known advisory\(ies\) \(CVE\-2025\-71176 \(pytest has vulnerable tmpdir handling\); CVE\-2025\-71176 \(pytest has vulnerable tmpdir handling\)\), but the manifest does not pin a version, so it is unknown whether the installed release is affected

**Remediation:** Determine the dependency's exact resolved version from the environment or lockfile and compare it with the advisories in OSV \(osv\.dev\)\. If it is affected, use a verified fixed release or remove or replace the dependency when no fix is available\.

---

### 🟢 LOW: SC4

**Location:** `pyproject.toml:59`  
**Confidence:** 40%  

**Message:** Unverifiable Dependency: tornado has 16 known advisory\(ies\) \(CVE\-2026\-103261 \(Tornado: Unbounded query\-string argument count allows event\-loop\-stalling DoS\); CVE\-2026\-49853 \(Tornado: Authorization header forwarded across cross\-origin redirects in SimpleA\); CVE\-2024\-14029 \(Inconsistent Interpretation of HTTP Requests \('HTTP Request/Response Smuggling'\)\) \+13 more\), but the manifest does not pin a version, so it is unknown whether the installed release is affected

**Remediation:** Determine the dependency's exact resolved version from the environment or lockfile and compare it with the advisories in OSV \(osv\.dev\)\. If it is affected, use a verified fixed release or remove or replace the dependency when no fix is available\.

---

### 🟢 LOW: AST7

**Location:** `tenacity/__init__.py:166`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | partial |
| Dependency contents | not\_requested |
| Coverage | 96\.9% |
| Fully inspected | 95 |
| Partially inspected | 3 |
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

### Ledger Exceptions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| obfuscated\_instruction\_text | `doc/source/index.rst` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |
| output\_limit | `pyproject.toml` | Inspection reached its configured output limit\. |
| obfuscated\_instruction\_text | `tenacity/wait.py` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |

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
