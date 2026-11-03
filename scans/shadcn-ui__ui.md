# Scans for shadcn-ui/ui @ 4aaea19


<!-- ===== skills\shadcn ===== -->
# SkillSpector Security Report

**Skill:** shadcn  
**Source:** `F:\Github Repos\repos\shadcn-ui__ui\skills\shadcn`  
**Scanned:** 2026-11-03 15:02:02 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 100/100 |
| Severity | CRITICAL |
| Recommendation | DO NOT INSTALL |

## Components (21)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `SKILL.md` | markdown | 296 | No |
| `agents/openai.yml` | yaml | 5 | No |
| `assets/shadcn-small.png` | other | 26 | No |
| `assets/shadcn.png` | other | 111 | No |
| `assets/showcase/color-pair.tsx` | other | 126 | Yes |
| `assets/showcase/preview-states.css` | other | 14 | No |
| `assets/showcase/state-matrix.tsx` | other | 72 | Yes |
| `cli.md` | markdown | 290 | No |
| `customization.md` | markdown | 211 | No |
| `design-system-page.md` | markdown | 268 | No |
| `design-system.md` | markdown | 386 | No |
| `evals/evals.json` | json | 126 | No |
| `mcp.md` | markdown | 105 | No |
| `registry.md` | markdown | 277 | No |
| `rules/base-vs-radix.md` | markdown | 306 | No |
| `rules/chat.md` | markdown | 507 | No |
| `rules/composition.md` | markdown | 213 | No |
| `rules/forms.md` | markdown | 192 | No |
| `rules/icons.md` | markdown | 101 | No |
| `rules/styling.md` | markdown | 185 | No |
| `scripts/showcase-coverage.mjs` | javascript | 53 | Yes |

## Issues (136)

### 🔴 HIGH: AE1

**Location:** `SKILL.md:55`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `rules/base-vs-radix.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:291`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `rules/base-vs-radix.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:205`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `scripts/showcase-coverage.mjs`

---

### 🔴 HIGH: MP3

**Location:** `SKILL.md:246`  
**Confidence:** 80%  

**Message:** Memory Manipulation

**Remediation:** Protect agent memory and state from modification by untrusted content\. Use read\-only memory for critical instructions and validate all state changes\.

---

### 🔴 HIGH: RA1

**Location:** `cli.md:34`  
**Confidence:** 85%  

**Message:** Self\-Modification

**Remediation:** Prevent the skill from modifying its own code, SKILL\.md, or configuration files\. Treat skill files as read\-only at runtime\.

---

### 🔴 HIGH: RA1

**Location:** `cli.md:77`  
**Confidence:** 85%  

**Message:** Self\-Modification

**Remediation:** Prevent the skill from modifying its own code, SKILL\.md, or configuration files\. Treat skill files as read\-only at runtime\.

---

### 🔴 HIGH: AS1

**Location:** `mcp.md:22`  
**Confidence:** 90%  

**Message:** Agent Config Directory Access

**Remediation:** Remove all code or instructions that access agent configuration directories \(\.claude/, \.codex/, \.gemini/\)\. If configuration values are needed, pass them explicitly as parameters or environment variables — never read the agent's own config files\.

---

### 🔴 HIGH: OH1

**Location:** `rules/chat.md:490`  
**Confidence:** 65%  

**Message:** Unvalidated Output Injection

**Remediation:** Validate and sanitize all model output before using it in downstream contexts\. Use parameterized queries for SQL, shell quoting for commands, and HTML encoding for web output\.

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:1`  
**Confidence:** 70%  

**Message:** Manifest references MCP server without version pin: 'npx shadcn'\.

**Remediation:** Always pin MCP server versions in manifest references\.

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:5`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:12`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:17`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:20`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:24`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:55`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:89`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:90`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:164`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:170`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:173`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:176`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:180`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:182`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:183`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:184`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:185`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:189`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:190`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:191`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:192`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:193`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:194`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:212`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:213`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:224`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:225`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:228`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:229`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:230`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:233`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:234`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:237`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:238`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:241`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:242`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:243`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:244`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:247`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:248`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:249`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:250`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:251`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:254`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:255`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:256`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:257`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:260`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:261`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:262`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:263`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:266`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:267`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:268`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:269`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:270`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:273`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:276`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `SKILL.md:277`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `cli.md:5`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `cli.md:23`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `cli.md:43`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `cli.md:48`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `cli.md:65`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `cli.md:68`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `cli.md:92`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `cli.md:95`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `cli.md:98`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `cli.md:101`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `cli.md:104`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `cli.md:107`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `cli.md:110`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `cli.md:113`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `cli.md:124`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `cli.md:133`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `cli.md:136`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `cli.md:153`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `cli.md:157`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `cli.md:158`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `cli.md:163`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `cli.md:168`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `cli.md:186`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `cli.md:191`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `cli.md:236`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `cli.md:241`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `cli.md:279`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `cli.md:280`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `cli.md:286`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `cli.md:287`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `cli.md:288`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `customization.md:68`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `customization.md:71`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `customization.md:74`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `customization.md:77`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `customization.md:80`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `customization.md:89`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `customization.md:111`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `customization.md:201`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `customization.md:207`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `customization.md:208`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `design-system.md:40`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `design-system.md:46`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `design-system.md:53`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `design-system.md:78`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `mcp.md:28`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `registry.md:13`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `registry.md:244`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `registry.md:245`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `registry.md:251`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `registry.md:252`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `registry.md:253`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `registry.md:254`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `registry.md:255`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `registry.md:261`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `registry.md:262`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `registry.md:263`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `registry.md:264`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `registry.md:265`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `rules/base-vs-radix.md:3`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `rules/chat.md:6`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx shadcn'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: EA2

**Location:** `cli.md:32`  
**Confidence:** 85%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `cli.md:56`  
**Confidence:** 85%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `cli.md:76`  
**Confidence:** 85%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: E1

**Location:** `cli.md:107`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: RP1

**Location:** `design-system.md:92`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx tsc'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `design-system.md:93`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx tsc'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟢 LOW: EA3

**Location:** `registry.md:18`  
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
| Coverage | 89\.5% |
| Fully inspected | 17 |
| Partially inspected | 2 |
| Entirely uninspected | 0 |

### Scope Exclusions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| binary\_content | `assets/shadcn-small.png` | Binary content is unsupported by this analyzer\. |
| binary\_content | `assets/shadcn.png` | Binary content is unsupported by this analyzer\. |

### Ledger Exceptions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| reference\_missing | `SKILL.md:156-156` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:181-181` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:195-195` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:199-199` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| static\_parse\_limit | `rules/base-vs-radix.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| static\_parse\_limit | `scripts/showcase-coverage.mjs` | A security\-relevant expression exceeded a bounded static parser's span limit\. |

### Analyzer Statuses

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| completed | `artifact_integrity` |  |
| no\_applicable\_files | `behavioral_ast` | No files matched this analyzer's applicability contract\. |
| no\_applicable\_files | `behavioral_taint_tracking` | No files matched this analyzer's applicability contract\. |
| no\_applicable\_files | `bundled_execution_surface` | No files matched this analyzer's applicability contract\. |
| completed | `mcp_least_privilege` |  |
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

- **Executable Scripts:** Yes

*Generated by SkillSpector v2.12.0*

