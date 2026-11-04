# SkillSpector Security Report

**Skill:** graphify  
**Source:** `F:\Github Repos\repos\Graphify-Labs__graphify\graphify`  
**Scanned:** 2026-11-04 17:13:30 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 100/100 |
| Severity | CRITICAL |
| Recommendation | DO NOT INSTALL |

## Components (235)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `__init__.py` | python | 30 | Yes |
| `__main__.py` | python | 1120 | Yes |
| `_minhash.py` | python | 107 | Yes |
| `affected.py` | python | 473 | Yes |
| `always_on/agents-md.md` | markdown | 13 | No |
| `always_on/antigravity-rules.md` | markdown | 14 | No |
| `always_on/claude-md.md` | markdown | 10 | No |
| `always_on/gemini-md.md` | markdown | 10 | No |
| `always_on/kiro-steering.md` | markdown | 5 | No |
| `always_on/vscode-instructions.md` | markdown | 17 | No |
| `analyze.py` | python | 855 | Yes |
| `benchmark.py` | python | 121 | Yes |
| `build.py` | python | 3307 | Yes |
| `cache.py` | python | 1957 | Yes |
| `callflow_html.py` | python | 2051 | Yes |
| `cargo_introspect.py` | python | 190 | Yes |
| `cli.py` | python | 5767 | Yes |
| `cluster.py` | python | 507 | Yes |
| `command-kilo.md` | markdown | 15 | No |
| `cross_repo_calls.py` | python | 325 | Yes |
| `cross_repo_types.py` | python | 75 | Yes |
| `csharp_dispatch.py` | python | 39 | Yes |
| `dedup.py` | python | 1844 | Yes |
| `detect.py` | python | 3282 | Yes |
| `diagnostics.py` | python | 422 | Yes |
| `export.py` | python | 1481 | Yes |
| `exporters/__init__.py` | python | 1 | Yes |
| `exporters/base.py` | python | 14 | Yes |
| `exporters/graphdb.py` | python | 210 | Yes |
| `exporters/html.py` | python | 781 | Yes |
| `extract.py` | python | 12138 | Yes |
| `extractors/MIGRATION.md` | markdown | 107 | No |
| `extractors/__init__.py` | python | 76 | Yes |
| `extractors/apex.py` | python | 215 | Yes |
| `extractors/base.py` | python | 181 | Yes |
| `extractors/bash.py` | python | 627 | Yes |
| `extractors/blade.py` | python | 80 | Yes |
| `extractors/cobol.py` | python | 314 | Yes |
| `extractors/commonlisp.py` | python | 582 | Yes |
| `extractors/csharp.py` | python | 654 | Yes |
| `extractors/dart.py` | python | 628 | Yes |
| `extractors/dm.py` | python | 507 | Yes |
| `extractors/elixir.py` | python | 481 | Yes |
| `extractors/engine.py` | python | 11364 | Yes |
| `extractors/erlang.py` | python | 353 | Yes |
| `extractors/fortran.py` | python | 453 | Yes |
| `extractors/go.py` | python | 1043 | Yes |
| `extractors/json_config.py` | python | 300 | Yes |
| `extractors/julia.py` | python | 503 | Yes |
| `extractors/markdown.py` | python | 634 | Yes |
| `extractors/models.py` | python | 131 | Yes |
| `extractors/objc.py` | python | 815 | Yes |
| `extractors/ocaml.py` | python | 372 | Yes |
| `extractors/pascal.py` | python | 720 | Yes |
| `extractors/pascal_forms.py` | python | 196 | Yes |
| `extractors/powershell.py` | python | 617 | Yes |
| `extractors/r.py` | python | 485 | Yes |
| `extractors/razor.py` | python | 205 | Yes |
| `extractors/resolution.py` | python | 4691 | Yes |
| `extractors/robot.py` | python | 315 | Yes |
| `extractors/rust.py` | python | 1120 | Yes |
| `extractors/sln.py` | python | 92 | Yes |
| `extractors/solidity.py` | python | 722 | Yes |
| `extractors/sql.py` | python | 993 | Yes |
| `extractors/terraform.py` | python | 515 | Yes |
| `extractors/vbnet.py` | python | 437 | Yes |
| `extractors/verilog.py` | python | 401 | Yes |
| `extractors/yaml_config.py` | python | 247 | Yes |
| `extractors/zig.py` | python | 251 | Yes |
| `file_slice.py` | python | 250 | Yes |
| `global_graph.py` | python | 201 | Yes |
| `go_dispatch.py` | python | 129 | Yes |
| `google_workspace.py` | python | 271 | Yes |
| `hooks.py` | python | 1254 | Yes |
| `ids.py` | python | 174 | Yes |
| `ingest.py` | python | 382 | Yes |
| `install.py` | python | 2953 | Yes |
| `interface_dispatch.py` | python | 224 | Yes |
| `llm.py` | python | 3979 | Yes |
| `manifest.py` | python | 4 | Yes |
| `manifest_ingest.py` | python | 340 | Yes |
| `markdown_resolution.py` | python | 290 | Yes |
| `mcp_ingest.py` | python | 386 | Yes |
| `multigraph_compat.py` | python | 212 | Yes |
| `pascal_resolution.py` | python | 129 | Yes |
| `paths.py` | python | 648 | Yes |
| `pg_introspect.py` | python | 165 | Yes |
| `pi/index.ts` | typescript | 190 | Yes |
| `pi/package.json` | json | 10 | No |
| `prs.py` | python | 822 | Yes |
| `querylog.py` | python | 80 | Yes |
| `rcfile.py` | python | 272 | Yes |
| `reflect.py` | python | 882 | Yes |
| `report.py` | python | 423 | Yes |
| `resolver_registry.py` | python | 88 | Yes |
| `ruby_resolution.py` | python | 524 | Yes |
| `scip_ingest.py` | python | 363 | Yes |
| `security.py` | python | 518 | Yes |
| `semantic_cleanup.py` | python | 336 | Yes |
| `serve.py` | python | 3525 | Yes |
| `skill-agents.md` | markdown | 795 | No |
| `skill-aider.md` | markdown | 1341 | No |
| `skill-amp.md` | markdown | 795 | No |
| `skill-claw.md` | markdown | 798 | No |
| `skill-codex.md` | markdown | 799 | No |
| `skill-copilot.md` | markdown | 798 | No |
| `skill-devin.md` | markdown | 1468 | No |
| `skill-droid.md` | markdown | 795 | No |
| `skill-kilo.md` | markdown | 807 | No |
| `skill-kiro.md` | markdown | 798 | No |
| `skill-opencode.md` | markdown | 790 | No |
| `skill-pi.md` | markdown | 792 | No |
| `skill-trae.md` | markdown | 796 | No |
| `skill-vscode.md` | markdown | 794 | No |
| `skill-windows.md` | markdown | 841 | No |
| `skill.md` | markdown | 798 | No |
| `skills/agents/references/add-watch.md` | markdown | 56 | No |
| `skills/agents/references/exports.md` | markdown | 91 | No |
| `skills/agents/references/extraction-spec.md` | markdown | 86 | No |
| `skills/agents/references/github-and-merge.md` | markdown | 46 | No |
| `skills/agents/references/hooks.md` | markdown | 33 | No |
| `skills/agents/references/query.md` | markdown | 319 | No |
| `skills/agents/references/transcribe.md` | markdown | 52 | No |
| `skills/agents/references/update.md` | markdown | 231 | No |
| `skills/amp/references/add-watch.md` | markdown | 56 | No |
| `skills/amp/references/exports.md` | markdown | 91 | No |
| `skills/amp/references/extraction-spec.md` | markdown | 86 | No |
| `skills/amp/references/github-and-merge.md` | markdown | 46 | No |
| `skills/amp/references/hooks.md` | markdown | 33 | No |
| `skills/amp/references/query.md` | markdown | 319 | No |
| `skills/amp/references/transcribe.md` | markdown | 52 | No |
| `skills/amp/references/update.md` | markdown | 231 | No |
| `skills/claude/references/add-watch.md` | markdown | 56 | No |
| `skills/claude/references/exports.md` | markdown | 91 | No |
| `skills/claude/references/extraction-spec.md` | markdown | 86 | No |
| `skills/claude/references/github-and-merge.md` | markdown | 46 | No |
| `skills/claude/references/hooks.md` | markdown | 48 | No |
| `skills/claude/references/query.md` | markdown | 319 | No |
| `skills/claude/references/transcribe.md` | markdown | 52 | No |
| `skills/claude/references/update.md` | markdown | 231 | No |
| `skills/claw/references/add-watch.md` | markdown | 56 | No |
| `skills/claw/references/exports.md` | markdown | 91 | No |
| `skills/claw/references/extraction-spec.md` | markdown | 39 | No |
| `skills/claw/references/github-and-merge.md` | markdown | 46 | No |
| `skills/claw/references/hooks.md` | markdown | 48 | No |
| `skills/claw/references/query.md` | markdown | 319 | No |
| `skills/claw/references/transcribe.md` | markdown | 52 | No |
| `skills/claw/references/update.md` | markdown | 231 | No |
| `skills/codex/references/add-watch.md` | markdown | 56 | No |
| `skills/codex/references/exports.md` | markdown | 91 | No |
| `skills/codex/references/extraction-spec.md` | markdown | 39 | No |
| `skills/codex/references/github-and-merge.md` | markdown | 46 | No |
| `skills/codex/references/hooks.md` | markdown | 48 | No |
| `skills/codex/references/query.md` | markdown | 319 | No |
| `skills/codex/references/transcribe.md` | markdown | 52 | No |
| `skills/codex/references/update.md` | markdown | 231 | No |
| `skills/copilot/references/add-watch.md` | markdown | 56 | No |
| `skills/copilot/references/exports.md` | markdown | 91 | No |
| `skills/copilot/references/extraction-spec.md` | markdown | 86 | No |
| `skills/copilot/references/github-and-merge.md` | markdown | 46 | No |
| `skills/copilot/references/hooks.md` | markdown | 48 | No |
| `skills/copilot/references/query.md` | markdown | 319 | No |
| `skills/copilot/references/transcribe.md` | markdown | 52 | No |
| `skills/copilot/references/update.md` | markdown | 231 | No |
| `skills/droid/references/add-watch.md` | markdown | 56 | No |
| `skills/droid/references/exports.md` | markdown | 91 | No |
| `skills/droid/references/extraction-spec.md` | markdown | 86 | No |
| `skills/droid/references/github-and-merge.md` | markdown | 46 | No |
| `skills/droid/references/hooks.md` | markdown | 48 | No |
| `skills/droid/references/query.md` | markdown | 319 | No |
| `skills/droid/references/transcribe.md` | markdown | 52 | No |
| `skills/droid/references/update.md` | markdown | 231 | No |
| `skills/kilo/references/add-watch.md` | markdown | 56 | No |
| `skills/kilo/references/exports.md` | markdown | 91 | No |
| `skills/kilo/references/extraction-spec.md` | markdown | 86 | No |
| `skills/kilo/references/github-and-merge.md` | markdown | 46 | No |
| `skills/kilo/references/hooks.md` | markdown | 48 | No |
| `skills/kilo/references/query.md` | markdown | 319 | No |
| `skills/kilo/references/transcribe.md` | markdown | 52 | No |
| `skills/kilo/references/update.md` | markdown | 231 | No |
| `skills/kiro/references/add-watch.md` | markdown | 56 | No |
| `skills/kiro/references/exports.md` | markdown | 91 | No |
| `skills/kiro/references/extraction-spec.md` | markdown | 39 | No |
| `skills/kiro/references/github-and-merge.md` | markdown | 46 | No |
| `skills/kiro/references/hooks.md` | markdown | 48 | No |
| `skills/kiro/references/query.md` | markdown | 319 | No |
| `skills/kiro/references/transcribe.md` | markdown | 52 | No |
| `skills/kiro/references/update.md` | markdown | 231 | No |
| `skills/opencode/references/add-watch.md` | markdown | 56 | No |
| `skills/opencode/references/exports.md` | markdown | 91 | No |
| `skills/opencode/references/extraction-spec.md` | markdown | 86 | No |
| `skills/opencode/references/github-and-merge.md` | markdown | 46 | No |
| `skills/opencode/references/hooks.md` | markdown | 48 | No |
| `skills/opencode/references/query.md` | markdown | 319 | No |
| `skills/opencode/references/transcribe.md` | markdown | 52 | No |
| `skills/opencode/references/update.md` | markdown | 231 | No |
| `skills/pi/references/add-watch.md` | markdown | 56 | No |
| `skills/pi/references/exports.md` | markdown | 91 | No |
| `skills/pi/references/extraction-spec.md` | markdown | 39 | No |
| `skills/pi/references/github-and-merge.md` | markdown | 46 | No |
| `skills/pi/references/hooks.md` | markdown | 48 | No |
| `skills/pi/references/query.md` | markdown | 319 | No |
| `skills/pi/references/transcribe.md` | markdown | 52 | No |
| `skills/pi/references/update.md` | markdown | 231 | No |
| `skills/trae/references/add-watch.md` | markdown | 56 | No |
| `skills/trae/references/exports.md` | markdown | 91 | No |
| `skills/trae/references/extraction-spec.md` | markdown | 86 | No |
| `skills/trae/references/github-and-merge.md` | markdown | 46 | No |
| `skills/trae/references/hooks.md` | markdown | 35 | No |
| `skills/trae/references/query.md` | markdown | 319 | No |
| `skills/trae/references/transcribe.md` | markdown | 52 | No |
| `skills/trae/references/update.md` | markdown | 231 | No |
| `skills/vscode/references/add-watch.md` | markdown | 56 | No |
| `skills/vscode/references/exports.md` | markdown | 91 | No |
| `skills/vscode/references/extraction-spec.md` | markdown | 86 | No |
| `skills/vscode/references/github-and-merge.md` | markdown | 46 | No |
| `skills/vscode/references/hooks.md` | markdown | 48 | No |
| `skills/vscode/references/query.md` | markdown | 319 | No |
| `skills/vscode/references/transcribe.md` | markdown | 52 | No |
| `skills/vscode/references/update.md` | markdown | 231 | No |
| `skills/windows/references/add-watch.md` | markdown | 56 | No |
| `skills/windows/references/exports.md` | markdown | 91 | No |
| `skills/windows/references/extraction-spec.md` | markdown | 86 | No |
| `skills/windows/references/github-and-merge.md` | markdown | 46 | No |
| `skills/windows/references/hooks.md` | markdown | 48 | No |
| `skills/windows/references/query.md` | markdown | 319 | No |
| `skills/windows/references/transcribe.md` | markdown | 52 | No |
| `skills/windows/references/update.md` | markdown | 231 | No |
| `swift_dispatch.py` | python | 46 | Yes |
| `symbol_resolution.py` | python | 710 | Yes |
| `transcribe.py` | python | 186 | Yes |
| `tree_html.py` | python | 689 | Yes |
| `validate.py` | python | 95 | Yes |
| `watch.py` | python | 3621 | Yes |
| `wiki.py` | python | 483 | Yes |

## Issues (302)

### 🔴 HIGH: P9

**Location:** `__main__.py:599`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `__main__.py:664`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: E2

**Location:** `__main__.py:782`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: AST5

**Location:** `__main__.py:805`  
**Confidence:** 85%  

**Message:** os\.system\(\) or os exec\-family call

**Remediation:** Replace os\.system\(\) with subprocess\.run\(shell=False\)\. Use explicit argument lists and validate all command inputs\.

---

### 🔴 HIGH: AR2

**Location:** `__main__.py:842`  
**Confidence:** 85%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: RA1

**Location:** `__main__.py:1083`  
**Confidence:** 85%  

**Message:** Self\-Modification

**Remediation:** Prevent the skill from modifying its own code, SKILL\.md, or configuration files\. Treat skill files as read\-only at runtime\.

---

### 🔴 HIGH: RA1

**Location:** `__main__.py:1087`  
**Confidence:** 85%  

**Message:** Self\-Modification

**Remediation:** Prevent the skill from modifying its own code, SKILL\.md, or configuration files\. Treat skill files as read\-only at runtime\.

---

### 🔴 HIGH: RA1

**Location:** `__main__.py:1090`  
**Confidence:** 85%  

**Message:** Self\-Modification

**Remediation:** Prevent the skill from modifying its own code, SKILL\.md, or configuration files\. Treat skill files as read\-only at runtime\.

---

### 🔴 HIGH: RA1

**Location:** `__main__.py:1095`  
**Confidence:** 85%  

**Message:** Self\-Modification

**Remediation:** Prevent the skill from modifying its own code, SKILL\.md, or configuration files\. Treat skill files as read\-only at runtime\.

---

### 🔴 HIGH: PE3

**Location:** `detect.py:140`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `detect.py:141`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `detect.py:143`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `detect.py:142`  
**Confidence:** 90%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `detect.py:143`  
**Confidence:** 90%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `detect.py:143`  
**Confidence:** 80%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `detect.py:166`  
**Confidence:** 80%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `detect.py:167`  
**Confidence:** 80%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `detect.py:199`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `detect.py:282`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `detect.py:314`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `detect.py:199`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `detect.py:282`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `detect.py:314`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `detect.py:206`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `detect.py:976`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `detect.py:1227`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `detect.py:304`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: AR2

**Location:** `detect.py:1114`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `extractors/engine.py:1369–1370`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `extractors/sql.py:923`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `file_slice.py:37`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `install.py:482`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `llm.py:3012`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: E2

**Location:** `detect.py:1413`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `detect.py:1555`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: MP3

**Location:** `export.py:84`  
**Confidence:** 85%  

**Message:** Memory Manipulation

**Remediation:** Protect agent memory and state from modification by untrusted content\. Use read\-only memory for critical instructions and validate all state changes\.

---

### 🔴 HIGH: PE3

**Location:** `extractors/bash.py:48`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `extractors/bash.py:331`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `extractors/bash.py:383`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `extractors/fortran.py:23`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `extractors/resolution.py:583`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: OH1

**Location:** `google_workspace.py:144–150`  
**Confidence:** 95%  

**Message:** Unvalidated Output Injection

**Remediation:** Validate and sanitize all model output before using it in downstream contexts\. Use parameterized queries for SQL, shell quoting for commands, and HTML encoding for web output\.

---

### 🔴 HIGH: TM1

**Location:** `hooks.py:481`  
**Confidence:** 75%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: AS1

**Location:** `install.py:251`  
**Confidence:** 90%  

**Message:** Agent Config Directory Access

**Remediation:** Remove all code or instructions that access agent configuration directories \(\.claude/, \.codex/, \.gemini/\)\. If configuration values are needed, pass them explicitly as parameters or environment variables — never read the agent's own config files\.

---

### 🔴 HIGH: AS1

**Location:** `install.py:1506`  
**Confidence:** 90%  

**Message:** Agent Config Directory Access

**Remediation:** Remove all code or instructions that access agent configuration directories \(\.claude/, \.codex/, \.gemini/\)\. If configuration values are needed, pass them explicitly as parameters or environment variables — never read the agent's own config files\.

---

### 🔴 HIGH: YR4

**Location:** `llm.py:638`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: EA5

**Location:** `llm.py:966`  
**Confidence:** 90%  

**Message:** External Model or Provider Selection

**Remediation:** Remove the model/provider override or disclose it prominently and require explicit operator approval before invoking an external coding CLI or billed model\.

**Evidence:**
- **selection\_surface:** `command`

---

### 🔴 HIGH: P6

**Location:** `llm.py:1964`  
**Confidence:** 80%  

**Message:** Direct Prompt Extraction

**Remediation:** Remove any instructions that reveal, print, or output system prompts or internal rules\. System instructions should never be exposed to end users\.

---

### 🔴 HIGH: SSRF1

**Location:** `llm.py:3390`  
**Confidence:** 90%  

**Message:** Cloud Metadata Access

**Remediation:** Remove access to cloud metadata endpoints unless strictly required\. If metadata is needed, restrict it \(e\.g\. IMDSv2 with hop limit\) and never expose returned credentials\.

---

### 🔴 HIGH: SSRF1

**Location:** `security.py:169`  
**Confidence:** 90%  

**Message:** Cloud Metadata Access

**Remediation:** Remove access to cloud metadata endpoints unless strictly required\. If metadata is needed, restrict it \(e\.g\. IMDSv2 with hop limit\) and never expose returned credentials\.

---

### 🔴 HIGH: SSRF1

**Location:** `llm.py:3396`  
**Confidence:** 90%  

**Message:** Cloud Metadata Access

**Remediation:** Remove access to cloud metadata endpoints unless strictly required\. If metadata is needed, restrict it \(e\.g\. IMDSv2 with hop limit\) and never expose returned credentials\.

---

### 🔴 HIGH: SSRF1

**Location:** `security.py:69`  
**Confidence:** 90%  

**Message:** Cloud Metadata Access

**Remediation:** Remove access to cloud metadata endpoints unless strictly required\. If metadata is needed, restrict it \(e\.g\. IMDSv2 with hop limit\) and never expose returned credentials\.

---

### 🔴 HIGH: TM1

**Location:** `skill-agents.md:419`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-amp.md:419`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-claw.md:422`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-codex.md:423`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-copilot.md:422`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-devin.md:437`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-droid.md:419`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-kilo.md:422`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-kiro.md:422`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-opencode.md:414`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-pi.md:416`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-trae.md:420`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-vscode.md:418`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill.md:422`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-agents.md:701`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-amp.md:701`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-claw.md:704`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-codex.md:705`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-copilot.md:704`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-devin.md:874`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-droid.md:701`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-kilo.md:704`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-kiro.md:704`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-opencode.md:696`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-pi.md:698`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-trae.md:702`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-vscode.md:700`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill.md:704`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-agents.md:703`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-aider.md:757`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-amp.md:703`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-claw.md:706`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-codex.md:707`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-copilot.md:706`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-devin.md:875`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-droid.md:703`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-kilo.md:706`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-kiro.md:706`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-opencode.md:698`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-pi.md:700`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-trae.md:704`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill-vscode.md:702`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skill.md:706`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: AR2

**Location:** `skill-agents.md:795`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `skill-aider.md:1341`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `skill-amp.md:795`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `skill-claw.md:798`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `skill-codex.md:799`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `skill-copilot.md:798`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `skill-droid.md:795`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `skill-kilo.md:807`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `skill-kiro.md:798`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `skill-opencode.md:790`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `skill-pi.md:792`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `skill-trae.md:796`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `skill-vscode.md:794`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `skill-windows.md:841`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `skill.md:798`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AS1

**Location:** `skill-codex.md:278`  
**Confidence:** 90%  

**Message:** Agent Config Directory Access

**Remediation:** Remove all code or instructions that access agent configuration directories \(\.claude/, \.codex/, \.gemini/\)\. If configuration values are needed, pass them explicitly as parameters or environment variables — never read the agent's own config files\.

---

### 🔴 HIGH: TM1

**Location:** `skill-devin.md:1064`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skills/agents/references/update.md:219`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skills/amp/references/update.md:219`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skills/claude/references/update.md:219`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skills/claw/references/update.md:219`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skills/codex/references/update.md:219`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skills/copilot/references/update.md:219`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skills/droid/references/update.md:219`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skills/kilo/references/update.md:219`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skills/kiro/references/update.md:219`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skills/opencode/references/update.md:219`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skills/pi/references/update.md:219`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skills/trae/references/update.md:219`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skills/vscode/references/update.md:219`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `skills/windows/references/update.md:219`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: AR2

**Location:** `skills/agents/references/extraction-spec.md:13`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `skills/amp/references/extraction-spec.md:13`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `skills/claude/references/extraction-spec.md:13`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `skills/copilot/references/extraction-spec.md:13`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `skills/droid/references/extraction-spec.md:13`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `skills/kilo/references/extraction-spec.md:13`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `skills/opencode/references/extraction-spec.md:13`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `skills/trae/references/extraction-spec.md:13`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `skills/vscode/references/extraction-spec.md:13`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `skills/windows/references/extraction-spec.md:13`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `watch.py:2474`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🟡 MEDIUM: LP3

**Location:** `SKILL.md:1`  
**Confidence:** 70%  

**Message:** Skill declares no tool scope \('permissions' or 'allowed\-tools'\) but code capabilities were detected: env, file\_read, file\_write, network, shell\.

**Remediation:** Clarify the skill's intended tool scope and review how the host runtime enforces it; runtime permissions are unknown unless separately verified\. For Claude Code / Agent Skills SKILL\.md, 'allowed\-tools' records preapproved tools, not a permission ceiling; add a tool only when it is independently approved as necessary, not to silence this finding\. For MCP server manifests, use a 'permissions' list naming the required capabilities\.

---

### 🟡 MEDIUM: AST4

**Location:** `__main__.py:402`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: P9

**Location:** `__main__.py:502`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🟡 MEDIUM: MP1

**Location:** `__main__.py:563`  
**Confidence:** 80%  

**Message:** Persistent Context Injection

**Remediation:** Do not allow untrusted input to persist in agent memory or context\. Validate all content before storing and implement memory isolation between sessions\.

---

### 🟡 MEDIUM: P9

**Location:** `__main__.py:575`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🟡 MEDIUM: AST4

**Location:** `__main__.py:804`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: RA2

**Location:** `__main__.py:1083`  
**Confidence:** 60%  

**Message:** Session Persistence

**Remediation:** Remove any persistence mechanisms \(cron jobs, startup scripts, state files\)\. Skills should not maintain state across sessions without explicit user consent\.

---

### 🟡 MEDIUM: RA2

**Location:** `__main__.py:1090`  
**Confidence:** 60%  

**Message:** Session Persistence

**Remediation:** Remove any persistence mechanisms \(cron jobs, startup scripts, state files\)\. Skills should not maintain state across sessions without explicit user consent\.

---

### 🟡 MEDIUM: RA2

**Location:** `__main__.py:1095`  
**Confidence:** 60%  

**Message:** Session Persistence

**Remediation:** Remove any persistence mechanisms \(cron jobs, startup scripts, state files\)\. Skills should not maintain state across sessions without explicit user consent\.

---

### 🟡 MEDIUM: AST4

**Location:** `cli.py:1608`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `cli.py:1618`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `detect.py:1406–1414`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `detect.py:1548–1556`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: TM3

**Location:** `detect.py:1572`  
**Confidence:** 80%  

**Message:** Unsafe Defaults

**Remediation:** Override unsafe defaults with secure settings \(verify=True, auth required, restrictive permissions\)\. Review and harden all tool configurations\.

---

### 🟡 MEDIUM: TM3

**Location:** `detect.py:1615`  
**Confidence:** 80%  

**Message:** Unsafe Defaults

**Remediation:** Override unsafe defaults with secure settings \(verify=True, auth required, restrictive permissions\)\. Review and harden all tool configurations\.

---

### 🟡 MEDIUM: TM3

**Location:** `detect.py:1616`  
**Confidence:** 80%  

**Message:** Unsafe Defaults

**Remediation:** Override unsafe defaults with secure settings \(verify=True, auth required, restrictive permissions\)\. Review and harden all tool configurations\.

---

### 🟡 MEDIUM: AST4

**Location:** `export.py:244–248`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `watch.py:472–476`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: EA4

**Location:** `extract.py:508`  
**Confidence:** 75%  

**Message:** Unbounded Resource Access

**Remediation:** Set explicit rate limits, timeouts, and resource quotas for API calls, file operations, and compute\. Implement circuit breakers for runaway loops\.

---

### 🟡 MEDIUM: EA2

**Location:** `extract.py:2150`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: AST4

**Location:** `extractors/fortran.py:60–65`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: EA2

**Location:** `extractors/go.py:962`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: RA2

**Location:** `extractors/resolution.py:2992`  
**Confidence:** 75%  

**Message:** Session Persistence

**Remediation:** Remove any persistence mechanisms \(cron jobs, startup scripts, state files\)\. Skills should not maintain state across sessions without explicit user consent\.

---

### 🟡 MEDIUM: AST4

**Location:** `google_workspace.py:144–150`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: TT2

**Location:** `google_workspace.py:144–150`  
**Confidence:** 65%  

**Message:** Tainted flow: 'timeout' from os\.environ\.get \(line 143, credential/environment\) → subprocess\.run \(code execution\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: RA2

**Location:** `hooks.py:343`  
**Confidence:** 65%  

**Message:** Session Persistence

**Remediation:** Remove any persistence mechanisms \(cron jobs, startup scripts, state files\)\. Skills should not maintain state across sessions without explicit user consent\.

---

### 🟡 MEDIUM: RA2

**Location:** `hooks.py:344`  
**Confidence:** 65%  

**Message:** Session Persistence

**Remediation:** Remove any persistence mechanisms \(cron jobs, startup scripts, state files\)\. Skills should not maintain state across sessions without explicit user consent\.

---

### 🟡 MEDIUM: RA2

**Location:** `hooks.py:388`  
**Confidence:** 65%  

**Message:** Session Persistence

**Remediation:** Remove any persistence mechanisms \(cron jobs, startup scripts, state files\)\. Skills should not maintain state across sessions without explicit user consent\.

---

### 🟡 MEDIUM: RA2

**Location:** `hooks.py:349`  
**Confidence:** 65%  

**Message:** Session Persistence

**Remediation:** Remove any persistence mechanisms \(cron jobs, startup scripts, state files\)\. Skills should not maintain state across sessions without explicit user consent\.

---

### 🟡 MEDIUM: AST4

**Location:** `hooks.py:777–780`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `hooks.py:839–842`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `hooks.py:1029–1032`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `hooks.py:1057–1060`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `hooks.py:1085–1088`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: TT2

**Location:** `install.py:125`  
**Confidence:** 65%  

**Message:** Tainted flow: 'path' from os\.environ \(line 118, credential/environment\) → open \(file write\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: RP1

**Location:** `install.py:242`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx skills'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `install.py:847`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx skills'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: TT2

**Location:** `install.py:382`  
**Confidence:** 65%  

**Message:** Tainted flow: 'skill\_dst' from os\.environ \(line 356, credential/environment\) → shutil\.copy2 \(file write\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: AST4

**Location:** `install.py:2885`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: E1

**Location:** `llm.py:156`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `llm.py:193`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: AST4

**Location:** `llm.py:1857–1866`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `llm.py:1973–1983`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: TT2

**Location:** `llm.py:1973–1983`  
**Confidence:** 65%  

**Message:** Tainted flow: 'combined\_message' from os\.environ\.get \(line 1941, credential/environment\) → subprocess\.run \(code execution\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: AST4

**Location:** `llm.py:3246–3256`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: TT2

**Location:** `llm.py:3246–3256`  
**Confidence:** 65%  

**Message:** Tainted flow: '\_resolve\_api\_timeout\(\)' from os\.environ\.get \(line 460, credential/environment\) → subprocess\.run \(code execution\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: RP1

**Location:** `mcp_ingest.py:278`  
**Confidence:** 65%  

**Message:** MCP server referenced without pinned version: 'uvx direct'\.

**Remediation:** Pin the version: uvx package\-name==1\.2\.3

---

### 🟡 MEDIUM: TM3

**Location:** `paths.py:181`  
**Confidence:** 70%  

**Message:** Unsafe Defaults

**Remediation:** Override unsafe defaults with secure settings \(verify=True, auth required, restrictive permissions\)\. Review and harden all tool configurations\.

---

### 🟡 MEDIUM: AST4

**Location:** `prs.py:143–150`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `prs.py:171–175`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `prs.py:282–286`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `prs.py:355–359`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `prs.py:714–718`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: EA4

**Location:** `serve.py:3369`  
**Confidence:** 75%  

**Message:** Unbounded Resource Access

**Remediation:** Set explicit rate limits, timeouts, and resource quotas for API calls, file operations, and compute\. Implement circuit breakers for runaway loops\.

---

### 🟡 MEDIUM: EA1

**Location:** `skill-agents.md:56`  
**Confidence:** 80%  

**Message:** Unrestricted Tool Access

**Remediation:** Restrict tool access to only the tools required for the skill's stated purpose\. Use an explicit allowlist rather than granting blanket access\.

---

### 🟡 MEDIUM: EA1

**Location:** `skill-aider.md:57`  
**Confidence:** 80%  

**Message:** Unrestricted Tool Access

**Remediation:** Restrict tool access to only the tools required for the skill's stated purpose\. Use an explicit allowlist rather than granting blanket access\.

---

### 🟡 MEDIUM: EA1

**Location:** `skill-amp.md:56`  
**Confidence:** 80%  

**Message:** Unrestricted Tool Access

**Remediation:** Restrict tool access to only the tools required for the skill's stated purpose\. Use an explicit allowlist rather than granting blanket access\.

---

### 🟡 MEDIUM: EA1

**Location:** `skill-claw.md:56`  
**Confidence:** 80%  

**Message:** Unrestricted Tool Access

**Remediation:** Restrict tool access to only the tools required for the skill's stated purpose\. Use an explicit allowlist rather than granting blanket access\.

---

### 🟡 MEDIUM: EA1

**Location:** `skill-codex.md:56`  
**Confidence:** 80%  

**Message:** Unrestricted Tool Access

**Remediation:** Restrict tool access to only the tools required for the skill's stated purpose\. Use an explicit allowlist rather than granting blanket access\.

---

### 🟡 MEDIUM: EA1

**Location:** `skill-copilot.md:56`  
**Confidence:** 80%  

**Message:** Unrestricted Tool Access

**Remediation:** Restrict tool access to only the tools required for the skill's stated purpose\. Use an explicit allowlist rather than granting blanket access\.

---

### 🟡 MEDIUM: EA1

**Location:** `skill-devin.md:68`  
**Confidence:** 80%  

**Message:** Unrestricted Tool Access

**Remediation:** Restrict tool access to only the tools required for the skill's stated purpose\. Use an explicit allowlist rather than granting blanket access\.

---

### 🟡 MEDIUM: EA1

**Location:** `skill-droid.md:56`  
**Confidence:** 80%  

**Message:** Unrestricted Tool Access

**Remediation:** Restrict tool access to only the tools required for the skill's stated purpose\. Use an explicit allowlist rather than granting blanket access\.

---

### 🟡 MEDIUM: EA1

**Location:** `skill-kilo.md:56`  
**Confidence:** 80%  

**Message:** Unrestricted Tool Access

**Remediation:** Restrict tool access to only the tools required for the skill's stated purpose\. Use an explicit allowlist rather than granting blanket access\.

---

### 🟡 MEDIUM: EA1

**Location:** `skill-kiro.md:56`  
**Confidence:** 80%  

**Message:** Unrestricted Tool Access

**Remediation:** Restrict tool access to only the tools required for the skill's stated purpose\. Use an explicit allowlist rather than granting blanket access\.

---

### 🟡 MEDIUM: EA1

**Location:** `skill-opencode.md:56`  
**Confidence:** 80%  

**Message:** Unrestricted Tool Access

**Remediation:** Restrict tool access to only the tools required for the skill's stated purpose\. Use an explicit allowlist rather than granting blanket access\.

---

### 🟡 MEDIUM: EA1

**Location:** `skill-pi.md:56`  
**Confidence:** 80%  

**Message:** Unrestricted Tool Access

**Remediation:** Restrict tool access to only the tools required for the skill's stated purpose\. Use an explicit allowlist rather than granting blanket access\.

---

### 🟡 MEDIUM: EA1

**Location:** `skill-trae.md:56`  
**Confidence:** 80%  

**Message:** Unrestricted Tool Access

**Remediation:** Restrict tool access to only the tools required for the skill's stated purpose\. Use an explicit allowlist rather than granting blanket access\.

---

### 🟡 MEDIUM: EA1

**Location:** `skill-vscode.md:56`  
**Confidence:** 80%  

**Message:** Unrestricted Tool Access

**Remediation:** Restrict tool access to only the tools required for the skill's stated purpose\. Use an explicit allowlist rather than granting blanket access\.

---

### 🟡 MEDIUM: EA1

**Location:** `skill-windows.md:56`  
**Confidence:** 80%  

**Message:** Unrestricted Tool Access

**Remediation:** Restrict tool access to only the tools required for the skill's stated purpose\. Use an explicit allowlist rather than granting blanket access\.

---

### 🟡 MEDIUM: EA1

**Location:** `skill.md:56`  
**Confidence:** 80%  

**Message:** Unrestricted Tool Access

**Remediation:** Restrict tool access to only the tools required for the skill's stated purpose\. Use an explicit allowlist rather than granting blanket access\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-agents.md:58`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-agents.md:60`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-aider.md:59`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-amp.md:58`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-amp.md:60`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-claw.md:58`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-claw.md:60`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-codex.md:58`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-codex.md:60`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-copilot.md:58`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-copilot.md:60`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-devin.md:70`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-droid.md:58`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-droid.md:60`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-kilo.md:58`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-kilo.md:60`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-kiro.md:58`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-kiro.md:60`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-opencode.md:58`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-opencode.md:60`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-pi.md:58`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-pi.md:60`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-trae.md:58`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-trae.md:60`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-vscode.md:58`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-vscode.md:60`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-windows.md:58`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-windows.md:60`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill.md:58`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill.md:60`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: RP1

**Location:** `skill-agents.md:78`  
**Confidence:** 65%  

**Message:** MCP server referenced without pinned version: 'uv tool run \-\-from graphifyy'\.

**Remediation:** Pin the version: uvx package\-name==1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `skill-agents.md:94`  
**Confidence:** 65%  

**Message:** MCP server referenced without pinned version: 'uv tool run \-\-from graphifyy'\.

**Remediation:** Pin the version: uvx package\-name==1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `skill-aider.md:71`  
**Confidence:** 65%  

**Message:** MCP server referenced without pinned version: 'uv tool run \-\-from graphifyy'\.

**Remediation:** Pin the version: uvx package\-name==1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `skill-aider.md:87`  
**Confidence:** 65%  

**Message:** MCP server referenced without pinned version: 'uv tool run \-\-from graphifyy'\.

**Remediation:** Pin the version: uvx package\-name==1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `skill-amp.md:78`  
**Confidence:** 65%  

**Message:** MCP server referenced without pinned version: 'uv tool run \-\-from graphifyy'\.

**Remediation:** Pin the version: uvx package\-name==1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `skill-amp.md:94`  
**Confidence:** 65%  

**Message:** MCP server referenced without pinned version: 'uv tool run \-\-from graphifyy'\.

**Remediation:** Pin the version: uvx package\-name==1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `skill-claw.md:78`  
**Confidence:** 65%  

**Message:** MCP server referenced without pinned version: 'uv tool run \-\-from graphifyy'\.

**Remediation:** Pin the version: uvx package\-name==1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `skill-claw.md:94`  
**Confidence:** 65%  

**Message:** MCP server referenced without pinned version: 'uv tool run \-\-from graphifyy'\.

**Remediation:** Pin the version: uvx package\-name==1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `skill-codex.md:78`  
**Confidence:** 65%  

**Message:** MCP server referenced without pinned version: 'uv tool run \-\-from graphifyy'\.

**Remediation:** Pin the version: uvx package\-name==1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `skill-codex.md:94`  
**Confidence:** 65%  

**Message:** MCP server referenced without pinned version: 'uv tool run \-\-from graphifyy'\.

**Remediation:** Pin the version: uvx package\-name==1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `skill-copilot.md:78`  
**Confidence:** 65%  

**Message:** MCP server referenced without pinned version: 'uv tool run \-\-from graphifyy'\.

**Remediation:** Pin the version: uvx package\-name==1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `skill-copilot.md:94`  
**Confidence:** 65%  

**Message:** MCP server referenced without pinned version: 'uv tool run \-\-from graphifyy'\.

**Remediation:** Pin the version: uvx package\-name==1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `skill-devin.md:82`  
**Confidence:** 65%  

**Message:** MCP server referenced without pinned version: 'uv tool run \-\-from graphifyy'\.

**Remediation:** Pin the version: uvx package\-name==1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `skill-devin.md:98`  
**Confidence:** 65%  

**Message:** MCP server referenced without pinned version: 'uv tool run \-\-from graphifyy'\.

**Remediation:** Pin the version: uvx package\-name==1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `skill-droid.md:78`  
**Confidence:** 65%  

**Message:** MCP server referenced without pinned version: 'uv tool run \-\-from graphifyy'\.

**Remediation:** Pin the version: uvx package\-name==1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `skill-droid.md:94`  
**Confidence:** 65%  

**Message:** MCP server referenced without pinned version: 'uv tool run \-\-from graphifyy'\.

**Remediation:** Pin the version: uvx package\-name==1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `skill-kilo.md:78`  
**Confidence:** 65%  

**Message:** MCP server referenced without pinned version: 'uv tool run \-\-from graphifyy'\.

**Remediation:** Pin the version: uvx package\-name==1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `skill-kilo.md:94`  
**Confidence:** 65%  

**Message:** MCP server referenced without pinned version: 'uv tool run \-\-from graphifyy'\.

**Remediation:** Pin the version: uvx package\-name==1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `skill-kiro.md:78`  
**Confidence:** 65%  

**Message:** MCP server referenced without pinned version: 'uv tool run \-\-from graphifyy'\.

**Remediation:** Pin the version: uvx package\-name==1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `skill-kiro.md:94`  
**Confidence:** 65%  

**Message:** MCP server referenced without pinned version: 'uv tool run \-\-from graphifyy'\.

**Remediation:** Pin the version: uvx package\-name==1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `skill-opencode.md:78`  
**Confidence:** 65%  

**Message:** MCP server referenced without pinned version: 'uv tool run \-\-from graphifyy'\.

**Remediation:** Pin the version: uvx package\-name==1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `skill-opencode.md:94`  
**Confidence:** 65%  

**Message:** MCP server referenced without pinned version: 'uv tool run \-\-from graphifyy'\.

**Remediation:** Pin the version: uvx package\-name==1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `skill-pi.md:78`  
**Confidence:** 65%  

**Message:** MCP server referenced without pinned version: 'uv tool run \-\-from graphifyy'\.

**Remediation:** Pin the version: uvx package\-name==1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `skill-pi.md:94`  
**Confidence:** 65%  

**Message:** MCP server referenced without pinned version: 'uv tool run \-\-from graphifyy'\.

**Remediation:** Pin the version: uvx package\-name==1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `skill-trae.md:78`  
**Confidence:** 65%  

**Message:** MCP server referenced without pinned version: 'uv tool run \-\-from graphifyy'\.

**Remediation:** Pin the version: uvx package\-name==1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `skill-trae.md:94`  
**Confidence:** 65%  

**Message:** MCP server referenced without pinned version: 'uv tool run \-\-from graphifyy'\.

**Remediation:** Pin the version: uvx package\-name==1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `skill-vscode.md:78`  
**Confidence:** 65%  

**Message:** MCP server referenced without pinned version: 'uv tool run \-\-from graphifyy'\.

**Remediation:** Pin the version: uvx package\-name==1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `skill-vscode.md:94`  
**Confidence:** 65%  

**Message:** MCP server referenced without pinned version: 'uv tool run \-\-from graphifyy'\.

**Remediation:** Pin the version: uvx package\-name==1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `skill.md:78`  
**Confidence:** 65%  

**Message:** MCP server referenced without pinned version: 'uv tool run \-\-from graphifyy'\.

**Remediation:** Pin the version: uvx package\-name==1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `skill.md:94`  
**Confidence:** 65%  

**Message:** MCP server referenced without pinned version: 'uv tool run \-\-from graphifyy'\.

**Remediation:** Pin the version: uvx package\-name==1\.2\.3

---

### 🟡 MEDIUM: EA2

**Location:** `skill-agents.md:170`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-aider.md:194`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-amp.md:170`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-claw.md:170`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-codex.md:170`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-copilot.md:170`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-devin.md:207`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-droid.md:170`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-kilo.md:170`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-kiro.md:170`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-opencode.md:170`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-pi.md:170`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-trae.md:170`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-vscode.md:170`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-windows.md:198`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill.md:170`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-aider.md:1271`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skill-devin.md:1403`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skills/agents/references/add-watch.md:27`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skills/amp/references/add-watch.md:27`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skills/claude/references/add-watch.md:27`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skills/claw/references/add-watch.md:27`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skills/codex/references/add-watch.md:27`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skills/copilot/references/add-watch.md:27`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skills/droid/references/add-watch.md:27`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skills/kilo/references/add-watch.md:27`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skills/kiro/references/add-watch.md:27`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skills/opencode/references/add-watch.md:27`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skills/pi/references/add-watch.md:27`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skills/trae/references/add-watch.md:27`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skills/vscode/references/add-watch.md:27`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `skills/windows/references/add-watch.md:27`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: TT2

**Location:** `watch.py:171`  
**Confidence:** 65%  

**Message:** Tainted flow: 'config' from pathlib\.Path\.read\_text \(line 160, file read\) → pathlib\.Path\.write\_text \(file write\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟢 LOW: AST7

**Location:** `__init__.py:29`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `extractors/engine.py:6397`  
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
| Coverage | 87\.7% |
| Fully inspected | 206 |
| Partially inspected | 29 |
| Entirely uninspected | 0 |

### Ledger Exceptions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| obfuscated\_instruction\_text | `build.py` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |
| obfuscated\_instruction\_text | `cache.py` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |
| static\_parse\_limit | `callflow_html.py` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| static\_parse\_limit | `cli.py` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| static\_parse\_limit | `detect.py` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| obfuscated\_instruction\_text | `extract.py` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |
| static\_parse\_limit | `extract.py` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| obfuscated\_instruction\_text | `extractors/bash.py` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |
| static\_parse\_limit | `extractors/bash.py` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| obfuscated\_instruction\_text | `extractors/dm.py` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |
| obfuscated\_instruction\_text | `extractors/engine.py` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |
| static\_parse\_limit | `extractors/engine.py` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| obfuscated\_instruction\_text | `extractors/go.py` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |
| obfuscated\_instruction\_text | `extractors/objc.py` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |
| obfuscated\_instruction\_text | `extractors/powershell.py` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |
| obfuscated\_instruction\_text | `extractors/resolution.py` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |
| static\_parse\_limit | `install.py` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| static\_parse\_limit | `skill-windows.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| reference\_missing | `skill.md:28-28` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:30-30` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:36-36` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:58-58` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:68-68` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:130-130` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:162-162` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:195-195` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:204-204` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:207-207` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:214-214` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:220-220` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:227-227` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:236-236` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:244-244` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:255-255` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:257-257` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:258-258` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:267-267` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:271-271` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:299-299` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:304-304` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:337-337` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:347-347` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:349-349` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:365-365` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:380-380` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:381-381` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:385-385` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:392-392` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:398-398` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:399-399` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:418-418` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:422-422` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:431-431` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:432-432` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:463-463` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:485-485` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:486-486` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:510-510` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:512-512` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:516-516` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:524-524` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:543-543` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:561-561` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:575-575` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:576-576` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:577-577` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:592-592` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:593-593` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:597-597` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:599-599` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:630-630` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:644-644` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:645-645` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:665-665` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:685-685` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:704-704` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:764-764` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:770-770` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:776-776` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:782-782` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `skill.md:788-788` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| static\_parse\_limit | `skills/agents/references/exports.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| static\_parse\_limit | `skills/amp/references/exports.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| static\_parse\_limit | `skills/claude/references/exports.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| static\_parse\_limit | `skills/claw/references/exports.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| static\_parse\_limit | `skills/codex/references/exports.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| static\_parse\_limit | `skills/copilot/references/exports.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| static\_parse\_limit | `skills/droid/references/exports.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| static\_parse\_limit | `skills/kilo/references/exports.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| static\_parse\_limit | `skills/kiro/references/exports.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| static\_parse\_limit | `skills/opencode/references/exports.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| static\_parse\_limit | `skills/pi/references/exports.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| static\_parse\_limit | `skills/trae/references/exports.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| static\_parse\_limit | `skills/vscode/references/exports.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| static\_parse\_limit | `skills/windows/references/exports.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |

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
