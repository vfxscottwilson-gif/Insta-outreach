# Scans for vercel-labs/agent-skills @ 1a2c79d


<!-- ===== skills\react-best-practices ===== -->
# SkillSpector Security Report

**Skill:** vercel\-react\-best\-practices  
**Source:** `F:\Github Repos\repos\vercel-labs__agent-skills\skills\react-best-practices`  
**Scanned:** 2026-11-03 15:02:37 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 59/100 |
| Severity | HIGH |
| Recommendation | DO NOT INSTALL |

## Components (76)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `AGENTS.md` | markdown | 3810 | No |
| `README.md` | markdown | 123 | No |
| `SKILL.md` | markdown | 149 | No |
| `metadata.json` | json | 15 | No |
| `rules/_sections.md` | markdown | 46 | No |
| `rules/_template.md` | markdown | 28 | No |
| `rules/advanced-effect-event-deps.md` | markdown | 56 | No |
| `rules/advanced-event-handler-refs.md` | markdown | 55 | No |
| `rules/advanced-init-once.md` | markdown | 42 | No |
| `rules/advanced-use-latest.md` | markdown | 39 | No |
| `rules/async-api-routes.md` | markdown | 38 | No |
| `rules/async-cheap-condition-before-await.md` | markdown | 37 | No |
| `rules/async-defer-await.md` | markdown | 82 | No |
| `rules/async-dependencies.md` | markdown | 51 | No |
| `rules/async-parallel.md` | markdown | 28 | No |
| `rules/async-suspense-boundaries.md` | markdown | 99 | No |
| `rules/bundle-analyzable-paths.md` | markdown | 63 | No |
| `rules/bundle-barrel-imports.md` | markdown | 60 | No |
| `rules/bundle-conditional.md` | markdown | 31 | No |
| `rules/bundle-defer-third-party.md` | markdown | 49 | No |
| `rules/bundle-dynamic-imports.md` | markdown | 35 | No |
| `rules/bundle-preload.md` | markdown | 50 | No |
| `rules/client-event-listeners.md` | markdown | 74 | No |
| `rules/client-localstorage-schema.md` | markdown | 71 | No |
| `rules/client-passive-event-listeners.md` | markdown | 48 | No |
| `rules/client-swr-dedup.md` | markdown | 56 | No |
| `rules/js-batch-dom-css.md` | markdown | 107 | No |
| `rules/js-cache-function-results.md` | markdown | 80 | No |
| `rules/js-cache-property-access.md` | markdown | 28 | No |
| `rules/js-cache-storage.md` | markdown | 70 | No |
| `rules/js-combine-iterations.md` | markdown | 32 | No |
| `rules/js-early-exit.md` | markdown | 50 | No |
| `rules/js-flatmap-filter.md` | markdown | 60 | No |
| `rules/js-hoist-regexp.md` | markdown | 45 | No |
| `rules/js-index-maps.md` | markdown | 37 | No |
| `rules/js-length-check-first.md` | markdown | 49 | No |
| `rules/js-min-max-loop.md` | markdown | 82 | No |
| `rules/js-request-idle-callback.md` | markdown | 105 | No |
| `rules/js-set-map-lookups.md` | markdown | 24 | No |
| `rules/js-tosorted-immutable.md` | markdown | 57 | No |
| `rules/rendering-activity.md` | markdown | 26 | No |
| `rules/rendering-animate-svg-wrapper.md` | markdown | 47 | No |
| `rules/rendering-conditional-render.md` | markdown | 40 | No |
| `rules/rendering-content-visibility.md` | markdown | 38 | No |
| `rules/rendering-hoist-jsx.md` | markdown | 46 | No |
| `rules/rendering-hydration-no-flicker.md` | markdown | 82 | No |
| `rules/rendering-hydration-suppress-warning.md` | markdown | 30 | No |
| `rules/rendering-resource-hints.md` | markdown | 85 | No |
| `rules/rendering-script-defer-async.md` | markdown | 68 | No |
| `rules/rendering-svg-precision.md` | markdown | 28 | No |
| `rules/rendering-usetransition-loading.md` | markdown | 75 | No |
| `rules/rerender-defer-reads.md` | markdown | 39 | No |
| `rules/rerender-dependencies.md` | markdown | 45 | No |
| `rules/rerender-derived-state-no-effect.md` | markdown | 40 | No |
| `rules/rerender-derived-state.md` | markdown | 29 | No |
| `rules/rerender-functional-setstate.md` | markdown | 74 | No |
| `rules/rerender-lazy-state-init.md` | markdown | 58 | No |
| `rules/rerender-memo-with-default-value.md` | markdown | 38 | No |
| `rules/rerender-memo.md` | markdown | 44 | No |
| `rules/rerender-move-effect-to-event.md` | markdown | 45 | No |
| `rules/rerender-no-inline-components.md` | markdown | 82 | No |
| `rules/rerender-simple-expression-in-memo.md` | markdown | 35 | No |
| `rules/rerender-split-combined-hooks.md` | markdown | 64 | No |
| `rules/rerender-transitions.md` | markdown | 40 | No |
| `rules/rerender-use-deferred-value.md` | markdown | 59 | No |
| `rules/rerender-use-ref-transient-values.md` | markdown | 73 | No |
| `rules/server-after-nonblocking.md` | markdown | 73 | No |
| `rules/server-auth-actions.md` | markdown | 96 | No |
| `rules/server-cache-lru.md` | markdown | 41 | No |
| `rules/server-cache-react.md` | markdown | 76 | No |
| `rules/server-dedup-props.md` | markdown | 65 | No |
| `rules/server-hoist-static-io.md` | markdown | 149 | No |
| `rules/server-no-shared-module-state.md` | markdown | 50 | No |
| `rules/server-parallel-fetching.md` | markdown | 83 | No |
| `rules/server-parallel-nested-fetching.md` | markdown | 34 | No |
| `rules/server-serialization.md` | markdown | 38 | No |

## Issues (5)

### 🔴 HIGH: OH1

**Location:** `AGENTS.md:2537`  
**Confidence:** 65%  

**Message:** Unvalidated Output Injection

**Remediation:** Validate and sanitize all model output before using it in downstream contexts\. Use parameterized queries for SQL, shell quoting for commands, and HTML encoding for web output\.

---

### 🔴 HIGH: OH1

**Location:** `rules/rendering-hydration-no-flicker.md:63`  
**Confidence:** 65%  

**Message:** Unvalidated Output Injection

**Remediation:** Validate and sanitize all model output before using it in downstream contexts\. Use parameterized queries for SQL, shell quoting for commands, and HTML encoding for web output\.

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:149`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `AGENTS.md`

---

### 🟡 MEDIUM: RP1

**Location:** `AGENTS.md:2477`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx svgo'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `rules/rendering-svg-precision.md:27`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx svgo'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | partial |
| Dependency contents | not\_requested |
| Coverage | 98\.7% |
| Fully inspected | 75 |
| Partially inspected | 1 |
| Entirely uninspected | 0 |

### Ledger Exceptions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| static\_parse\_limit | `AGENTS.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| reference\_missing | `SKILL.md:3-3` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:7-7` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:20-20` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |

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


<!-- ===== skills\web-design-guidelines ===== -->
# SkillSpector Security Report

**Skill:** web\-design\-guidelines  
**Source:** `F:\Github Repos\repos\vercel-labs__agent-skills\skills\web-design-guidelines`  
**Scanned:** 2026-11-03 15:02:58 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 0/100 |
| Severity | LOW |
| Recommendation | SAFE |

## Components (1)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `SKILL.md` | markdown | 39 | No |

## Issues (0)

No security issues detected.

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | complete\_with\_caveats |
| Dependency contents | not\_requested |
| Coverage | 100\.0% |
| Fully inspected | 1 |
| Partially inspected | 0 |
| Entirely uninspected | 0 |

### Ledger Exceptions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| reference\_missing | `SKILL.md:6-6` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |

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

