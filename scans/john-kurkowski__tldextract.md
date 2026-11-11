# SkillSpector Security Report

**Skill:** unknown  
**Source:** `F:\Github Repos\repos\john-kurkowski__tldextract`  
**Scanned:** 2026-11-11 16:01:56 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 100/100 |
| Severity | CRITICAL |
| Recommendation | DO NOT INSTALL |

## Components (50)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `.git/config` | other | 13 | No |
| `.github/FUNDING.yml` | yaml | 1 | No |
| `.github/dependabot.yml` | yaml | 19 | No |
| `.github/workflows/ci.yml` | yaml | 63 | No |
| `.gitignore` | other | 11 | No |
| `AGENTS.md` | markdown | 34 | No |
| `CHANGELOG.md` | markdown | 575 | No |
| `CLAUDE.md` | markdown | 1 | No |
| `LICENSE` | other | 29 | No |
| `README.md` | markdown | 283 | No |
| `conftest.py` | python | 13 | Yes |
| `pyproject.toml` | toml | 120 | No |
| `scripts/release.py` | python | 242 | Yes |
| `tests/__init__.py` | python | 1 | Yes |
| `tests/__snapshots__/test_release.ambr` | other | 247 | No |
| `tests/cli_test.py` | python | 92 | Yes |
| `tests/conftest.py` | python | 17 | Yes |
| `tests/custom_suffix_test.py` | python | 135 | Yes |
| `tests/fixtures/fake_suffix_list_fixture.dat` | other | 6 | No |
| `tests/main_test.py` | python | 859 | Yes |
| `tests/test_cache.py` | python | 112 | Yes |
| `tests/test_parallel.py` | python | 55 | Yes |
| `tests/test_release.py` | python | 94 | Yes |
| `tests/test_suffix_list_env.py` | python | 151 | Yes |
| `tests/test_trie.py` | python | 47 | Yes |
| `tldextract/.tld_set_snapshot` | other | 15771 | No |
| `tldextract/__init__.py` | python | 14 | Yes |
| `tldextract/__main__.py` | python | 6 | Yes |
| `tldextract/cache.py` | python | 238 | Yes |
| `tldextract/cli.py` | python | 119 | Yes |
| `tldextract/py.typed` | other | 0 | No |
| `tldextract/remote.py` | python | 69 | Yes |
| `tldextract/suffix_list.py` | python | 118 | Yes |
| `tldextract/tldextract.py` | python | 801 | Yes |
| `tox.ini` | other | 23 | No |
| `uv.lock` | other | 1342 | No |
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

## Issues (44)

### 🔴 CRITICAL: TT5

**Location:** `scripts/release.py:45`  
**Confidence:** 90%  

**Message:** Tainted flow: 'version' from input \(line 232, user input\) → subprocess\.run \(code execution\)

**Remediation:** Never pass external input to exec\(\), eval\(\), os\.system\(\), or subprocess without strict validation\. Use allowlists and parameterized commands instead\.

---

### 🔴 CRITICAL: TT5

**Location:** `scripts/release.py:50`  
**Confidence:** 90%  

**Message:** Tainted flow: 'version' from input \(line 232, user input\) → subprocess\.run \(code execution\)

**Remediation:** Never pass external input to exec\(\), eval\(\), os\.system\(\), or subprocess without strict validation\. Use allowlists and parameterized commands instead\.

---

### 🔴 CRITICAL: TT3

**Location:** `scripts/release.py:95–103`  
**Confidence:** 90%  

**Message:** Tainted flow: 'token' from os\.environ\.get \(line 138, credential/environment\) → requests\.post \(network output\)

**Remediation:** Never send credentials or environment variables over the network\. Use secure credential stores and avoid transmitting secrets in request bodies or URLs\.

---

### 🔴 CRITICAL: TT3

**Location:** `scripts/release.py:142–156`  
**Confidence:** 90%  

**Message:** Tainted flow: 'release\_body' from os\.environ\.get \(line 140, credential/environment\) → requests\.post \(network output\)

**Remediation:** Never send credentials or environment variables over the network\. Use secure credential stores and avoid transmitting secrets in request bodies or URLs\.

---

### 🔴 CRITICAL: SC4

**Location:** `uv.lock:86`  
**Confidence:** 90%  

**Message:** Known Vulnerable Dependency: certifi==2026\.7\.22 — 2 advisory\(ies\): GHSA\-6q48\-6c7w\-9gw2 \(certifi bundles emSign root CAs with compromised intermediate CA keys\); PYSEC\-2026\-4320 \(certifi bundles emSign root CAs with compromised intermediate CA keys\)

**Remediation:** Review the matched advisories in OSV \(osv\.dev\) for affected and fixed releases\. If a fixed release is available, update to a release that addresses the matched advisories; otherwise remove or replace the affected dependency\.

---

### 🔴 CRITICAL: SC4

**Location:** `uv.lock:1293`  
**Confidence:** 90%  

**Message:** Known Vulnerable Dependency: uv==0\.12\.1 — 2 advisory\(ies\): GHSA\-hq85\-5cpj\-mr62 \(uv's bundled CA store trusts an emSign root whose intermediate CA keys are compr\); PYSEC\-2026\-4321 \(uv's bundled CA store trusts an emSign root whose intermediate CA keys are compr\)

**Remediation:** Review the matched advisories in OSV \(osv\.dev\) for affected and fixed releases\. If a fixed release is available, update to a release that addresses the matched advisories; otherwise remove or replace the affected dependency\.

---

### 🔴 HIGH: SC4

**Location:** `pyproject.toml:40`  
**Confidence:** 80%  

**Message:** Known Vulnerable Dependency: filelock==4\.0\.5 — 14 advisory\(ies\): CVE\-2026\-112907 \(filelock: On Windows an oplock on a soft lock's marker holds SoftFileLock\.acquir\); CVE\-2026\-112908 \(filelock: StrictSoftFileLock creates its claim directories without the lock mode\); CVE\-2026\-112909 \(filelock: UnixFileLock truncates and chmods any regular file another user rename\) \+11 more

**Remediation:** Review the matched advisories in OSV \(osv\.dev\) for affected and fixed releases\. If a fixed release is available, update to a release that addresses the matched advisories; otherwise remove or replace the affected dependency\.

---

### 🔴 HIGH: SC4

**Location:** `uv.lock:319`  
**Confidence:** 80%  

**Message:** Known Vulnerable Dependency: filelock==4\.0\.5 — 14 advisory\(ies\): CVE\-2026\-112907 \(filelock: On Windows an oplock on a soft lock's marker holds SoftFileLock\.acquir\); CVE\-2026\-112908 \(filelock: StrictSoftFileLock creates its claim directories without the lock mode\); CVE\-2026\-112909 \(filelock: UnixFileLock truncates and chmods any regular file another user rename\) \+11 more

**Remediation:** Review the matched advisories in OSV \(osv\.dev\) for affected and fixed releases\. If a fixed release is available, update to a release that addresses the matched advisories; otherwise remove or replace the affected dependency\.

---

### 🔴 HIGH: PE3

**Location:** `scripts/release.py:17`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: E2

**Location:** `tests/main_test.py:631`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_suffix_list_env.py:136`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: PE3

**Location:** `uv.lock:415`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `uv.lock:427`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `uv.lock:429`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `uv.lock:1239`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: SC4

**Location:** `uv.lock:1319`  
**Confidence:** 80%  

**Message:** Known Vulnerable Dependency: virtualenv==21\.14\.2 — 13 advisory\(ies\): CVE\-2026\-113718 \(virtualenv: Xonsh activation literals depend on the script decoding codec\); CVE\-2026\-113724 \(virtualenv: Deletion recovery can change a symlink target's mode\); CVE\-2026\-113714 \(virtualenv: Downloaded wheel selection and caching precede verification\) \+10 more

**Remediation:** Review the matched advisories in OSV \(osv\.dev\) for affected and fixed releases\. If a fixed release is available, update to a release that addresses the matched advisories; otherwise remove or replace the affected dependency\.

---

### 🟡 MEDIUM: RP1

**Location:** `.github/workflows/ci.yml:48`  
**Confidence:** 65%  

**Message:** MCP server referenced without pinned version: 'uv tool run \-\-with tox\-uv'\.

**Remediation:** Pin the version: uvx package\-name==1\.2\.3

---

### 🟡 MEDIUM: AST4

**Location:** `scripts/release.py:45`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `scripts/release.py:50`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `scripts/release.py:56`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `scripts/release.py:62`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `scripts/release.py:78`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `scripts/release.py:81`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: E1

**Location:** `scripts/release.py:95`  
**Confidence:** 80%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `scripts/release.py:95`  
**Confidence:** 70%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `scripts/release.py:142`  
**Confidence:** 70%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: TT2

**Location:** `scripts/release.py:95–103`  
**Confidence:** 65%  

**Message:** Tainted flow: 'version' from input \(line 138, user input\) → requests\.post \(network output\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: E1

**Location:** `scripts/release.py:96`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `scripts/release.py:143`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/__snapshots__/test_release.ambr:44`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/__snapshots__/test_release.ambr:60`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `scripts/release.py:142`  
**Confidence:** 80%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: TT2

**Location:** `scripts/release.py:142–156`  
**Confidence:** 65%  

**Message:** Tainted flow: 'version' from input \(line 238, user input\) → requests\.post \(network output\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: AST4

**Location:** `scripts/release.py:182–185`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `scripts/release.py:190`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `scripts/release.py:195–197`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/main_test.py:627–633`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_suffix_list_env.py:138–149`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: E1

**Location:** `tldextract/.tld_set_snapshot:5535`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟢 LOW: EA3

**Location:** `LICENSE:25`  
**Confidence:** 70%  

**Message:** Scope Creep

**Remediation:** Limit the skill's scope to its documented purpose\. Remove instructions that enable the agent to perform actions outside its stated functionality\.

---

### 🟢 LOW: TM1

**Location:** `README.md:81`  
**Confidence:** 15%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🟢 LOW: SC4

**Location:** `pyproject.toml:77`  
**Confidence:** 40%  

**Message:** Unverifiable Dependency: setuptools has 11 known advisory\(ies\) \(CVE\-2013\-1633 \(Setuptools vulnerable to Man\-in\-the\-middle attacks\); CVE\-2025\-47273 \(setuptools has a path traversal vulnerability in PackageIndex\.download that lead\); CVE\-2024\-6345 \(setuptools vulnerable to Command Injection via package URL\) \+8 more\), but the manifest does not pin a version, so it is unknown whether the installed release is affected

**Remediation:** Determine the dependency's exact resolved version from the environment or lockfile and compare it with the advisories in OSV \(osv\.dev\)\. If it is affected, use a verified fixed release or remove or replace the dependency when no fix is available\.

---

### 🟢 LOW: AST7

**Location:** `tests/test_release.py:28`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `tldextract/cli.py:114`  
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
| Coverage | 97\.2% |
| Fully inspected | 35 |
| Partially inspected | 1 |
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
| static\_parse\_limit | `CHANGELOG.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |

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
| degraded | `static_patterns_tool_misuse` |  |
| completed | `static_yara` |  |

### Limitations

- Analyzer static\_patterns\_tool\_misuse status: degraded\.

## Metadata

- **Executable Scripts:** Yes

*Generated by SkillSpector v2.12.0*
