# Scans for diffusionstudio/lottie @ 3c72912


<!-- ===== skills\text-to-lottie ===== -->
# SkillSpector Security Report

**Skill:** text\-to\-lottie  
**Source:** `F:\Github Repos\repos\diffusionstudio__lottie\skills\text-to-lottie`  
**Scanned:** 2026-11-03 15:01:11 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 27/100 |
| Severity | MEDIUM |
| Recommendation | CAUTION |

## Components (23)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `SKILL.md` | markdown | 162 | No |
| `evals/output-rubric.md` | markdown | 208 | No |
| `evals/reference-loading-prompts.json` | json | 183 | No |
| `evals/routing-prompts.json` | json | 288 | No |
| `evals/trigger-prompts.json` | json | 97 | No |
| `references/chapterization-transition-grammar.md` | markdown | 132 | No |
| `references/design-taste.md` | markdown | 292 | No |
| `references/lottie-spec-map.md` | markdown | 82 | No |
| `references/motion-taste.md` | markdown | 260 | No |
| `references/player-contract.md` | markdown | 325 | No |
| `references/recipe-camera-scene-motion.md` | markdown | 65 | No |
| `references/recipe-data-stats.md` | markdown | 104 | No |
| `references/recipe-diagram-technical.md` | markdown | 106 | No |
| `references/recipe-loaders-icons.md` | markdown | 70 | No |
| `references/recipe-logo.md` | markdown | 72 | No |
| `references/recipe-lower-thirds.md` | markdown | 62 | No |
| `references/recipe-product-promo.md` | markdown | 99 | No |
| `references/recipe-starter-projects.md` | markdown | 53 | No |
| `references/recipe-svg-animation.md` | markdown | 67 | No |
| `references/recipe-typography.md` | markdown | 158 | No |
| `references/recipe-ui-microinteractions.md` | markdown | 68 | No |
| `references/recipe-visual-effects.md` | markdown | 109 | No |
| `references/svg-compatibility.md` | markdown | 81 | No |

## Issues (2)

### 🔴 HIGH: MP3

**Location:** `references/recipe-ui-microinteractions.md:17`  
**Confidence:** 80%  

**Message:** Memory Manipulation

**Remediation:** Protect agent memory and state from modification by untrusted content\. Use read\-only memory for critical instructions and validate all state changes\.

---

### 🟡 MEDIUM: RP1

**Location:** `references/player-contract.md:13`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx degit'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | complete\_with\_caveats |
| Dependency contents | not\_requested |
| Coverage | 100\.0% |
| Fully inspected | 23 |
| Partially inspected | 0 |
| Entirely uninspected | 0 |

### Ledger Exceptions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| reference\_missing | `SKILL.md:71-71` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:111-111` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:120-120` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:125-125` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:126-126` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |

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

