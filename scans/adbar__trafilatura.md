# SkillSpector Security Report

**Skill:** unknown  
**Source:** `F:\Github Repos\repos\adbar__trafilatura`  
**Scanned:** 2026-11-11 16:17:58 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 100/100 |
| Severity | CRITICAL |
| Recommendation | DO NOT INSTALL |

## Components (28)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `.git/HEAD` | other | 0 | No |
| `.git/description` | other | 0 | No |
| `.git/hooks/applypatch-msg.sample` | other | 0 | No |
| `.git/hooks/commit-msg.sample` | other | 0 | No |
| `.git/hooks/fsmonitor-watchman.sample` | other | 0 | No |
| `.git/hooks/post-update.sample` | other | 0 | No |
| `.git/hooks/pre-applypatch.sample` | other | 0 | No |
| `.git/hooks/pre-commit.sample` | other | 0 | No |
| `.git/hooks/pre-merge-commit.sample` | other | 0 | No |
| `.git/hooks/pre-push.sample` | other | 0 | No |
| `.git/hooks/pre-rebase.sample` | other | 0 | No |
| `.git/hooks/pre-receive.sample` | other | 0 | No |
| `.git/hooks/prepare-commit-msg.sample` | other | 0 | No |
| `.git/hooks/push-to-checkout.sample` | other | 0 | No |
| `.git/hooks/sendemail-validate.sample` | other | 0 | No |
| `.git/hooks/update.sample` | other | 0 | No |
| `.git/index` | other | 0 | No |
| `.git/info/exclude` | other | 0 | No |
| `.git/logs/HEAD` | other | 0 | No |
| `.git/logs/refs/heads/master` | other | 0 | No |
| `.git/logs/refs/remotes/origin/HEAD` | other | 0 | No |
| `.git/objects/pack/pack-b05a52a0552dcfd9811f1715d8cf1cc1fdda78a3.idx` | other | 0 | No |
| `.git/objects/pack/pack-b05a52a0552dcfd9811f1715d8cf1cc1fdda78a3.pack` | other | 0 | No |
| `.git/objects/pack/pack-b05a52a0552dcfd9811f1715d8cf1cc1fdda78a3.rev` | other | 0 | No |
| `.git/packed-refs` | other | 0 | No |
| `.git/refs/heads/master` | other | 0 | No |
| `.git/refs/remotes/origin/HEAD` | other | 0 | No |
| `.git/shallow` | other | 0 | No |

## Issues (73)

### 🔴 CRITICAL: YR1

**Location:** `tests/cache/faz.net.streaming.html:546`  
**Confidence:** 85%  

**Message:** YARA rule 'c2\_framework\_indicators': Command\-and\-control framework indicators \(Cobalt Strike, Metasploit, Sliver, etc\.\) \[malware\]

**Remediation:** Remove the malware payload or compromised file entirely\. Investigate how it entered the skill and audit all other artifacts for additional indicators of compromise\.

---

### 🔴 HIGH: SC9

**Location:** `.git/HEAD:1`  
**Confidence:** 100%  

**Message:** An excluded artifact could not be completely inspected\.

**Remediation:** Review the artifact provenance and the reason executable content is packaged in this location; keep executable files explicit and directly reviewable\.

**Evidence:**
- **concealment:** `vcs_metadata`
- **concealment\_reasons:** `['vcs_metadata']`
- **container\_ancestry:** `['filesystem']`
- **container\_depth:** `0`
- **container\_type:** `filesystem`
- **excluded\_from\_analysis:** `True`
- **excluded\_inspection\_incomplete:** `True`
- **inherited\_exclusion\_reason:** `vcs_metadata`
- **inspection\_limitation\_reason:** `runtime_limit`
- **local\_only:** `True`
- **nested\_path:** `.git/HEAD`
- **outer\_path:** `.git/HEAD`
- **partially\_analyzed\_executable:** `False`
- **referenced:** `False`

---

### 🔴 HIGH: SC9

**Location:** `.git/description:1`  
**Confidence:** 100%  

**Message:** An excluded artifact could not be completely inspected\.

**Remediation:** Review the artifact provenance and the reason executable content is packaged in this location; keep executable files explicit and directly reviewable\.

**Evidence:**
- **concealment:** `vcs_metadata`
- **concealment\_reasons:** `['vcs_metadata']`
- **container\_ancestry:** `['filesystem']`
- **container\_depth:** `0`
- **container\_type:** `filesystem`
- **excluded\_from\_analysis:** `True`
- **excluded\_inspection\_incomplete:** `True`
- **inherited\_exclusion\_reason:** `vcs_metadata`
- **inspection\_limitation\_reason:** `runtime_limit`
- **local\_only:** `True`
- **nested\_path:** `.git/description`
- **outer\_path:** `.git/description`
- **partially\_analyzed\_executable:** `False`
- **referenced:** `False`

---

### 🔴 HIGH: SC9

**Location:** `.git/hooks/applypatch-msg.sample:1`  
**Confidence:** 100%  

**Message:** An excluded artifact could not be completely inspected\.

**Remediation:** Review the artifact provenance and the reason executable content is packaged in this location; keep executable files explicit and directly reviewable\.

**Evidence:**
- **concealment:** `vcs_metadata`
- **concealment\_reasons:** `['vcs_metadata']`
- **container\_ancestry:** `['filesystem']`
- **container\_depth:** `0`
- **container\_type:** `filesystem`
- **excluded\_from\_analysis:** `True`
- **excluded\_inspection\_incomplete:** `True`
- **inherited\_exclusion\_reason:** `vcs_metadata`
- **inspection\_limitation\_reason:** `runtime_limit`
- **local\_only:** `True`
- **nested\_path:** `.git/hooks/applypatch-msg.sample`
- **outer\_path:** `.git/hooks/applypatch-msg.sample`
- **partially\_analyzed\_executable:** `False`
- **referenced:** `False`

---

### 🔴 HIGH: SC9

**Location:** `.git/hooks/commit-msg.sample:1`  
**Confidence:** 100%  

**Message:** An excluded artifact could not be completely inspected\.

**Remediation:** Review the artifact provenance and the reason executable content is packaged in this location; keep executable files explicit and directly reviewable\.

**Evidence:**
- **concealment:** `vcs_metadata`
- **concealment\_reasons:** `['vcs_metadata']`
- **container\_ancestry:** `['filesystem']`
- **container\_depth:** `0`
- **container\_type:** `filesystem`
- **excluded\_from\_analysis:** `True`
- **excluded\_inspection\_incomplete:** `True`
- **inherited\_exclusion\_reason:** `vcs_metadata`
- **inspection\_limitation\_reason:** `runtime_limit`
- **local\_only:** `True`
- **nested\_path:** `.git/hooks/commit-msg.sample`
- **outer\_path:** `.git/hooks/commit-msg.sample`
- **partially\_analyzed\_executable:** `False`
- **referenced:** `False`

---

### 🔴 HIGH: SC9

**Location:** `.git/hooks/fsmonitor-watchman.sample:1`  
**Confidence:** 100%  

**Message:** An excluded artifact could not be completely inspected\.

**Remediation:** Review the artifact provenance and the reason executable content is packaged in this location; keep executable files explicit and directly reviewable\.

**Evidence:**
- **concealment:** `vcs_metadata`
- **concealment\_reasons:** `['vcs_metadata']`
- **container\_ancestry:** `['filesystem']`
- **container\_depth:** `0`
- **container\_type:** `filesystem`
- **excluded\_from\_analysis:** `True`
- **excluded\_inspection\_incomplete:** `True`
- **inherited\_exclusion\_reason:** `vcs_metadata`
- **inspection\_limitation\_reason:** `runtime_limit`
- **local\_only:** `True`
- **nested\_path:** `.git/hooks/fsmonitor-watchman.sample`
- **outer\_path:** `.git/hooks/fsmonitor-watchman.sample`
- **partially\_analyzed\_executable:** `False`
- **referenced:** `False`

---

### 🔴 HIGH: SC9

**Location:** `.git/hooks/post-update.sample:1`  
**Confidence:** 100%  

**Message:** An excluded artifact could not be completely inspected\.

**Remediation:** Review the artifact provenance and the reason executable content is packaged in this location; keep executable files explicit and directly reviewable\.

**Evidence:**
- **concealment:** `vcs_metadata`
- **concealment\_reasons:** `['vcs_metadata']`
- **container\_ancestry:** `['filesystem']`
- **container\_depth:** `0`
- **container\_type:** `filesystem`
- **excluded\_from\_analysis:** `True`
- **excluded\_inspection\_incomplete:** `True`
- **inherited\_exclusion\_reason:** `vcs_metadata`
- **inspection\_limitation\_reason:** `runtime_limit`
- **local\_only:** `True`
- **nested\_path:** `.git/hooks/post-update.sample`
- **outer\_path:** `.git/hooks/post-update.sample`
- **partially\_analyzed\_executable:** `False`
- **referenced:** `False`

---

### 🔴 HIGH: SC9

**Location:** `.git/hooks/pre-applypatch.sample:1`  
**Confidence:** 100%  

**Message:** An excluded artifact could not be completely inspected\.

**Remediation:** Review the artifact provenance and the reason executable content is packaged in this location; keep executable files explicit and directly reviewable\.

**Evidence:**
- **concealment:** `vcs_metadata`
- **concealment\_reasons:** `['vcs_metadata']`
- **container\_ancestry:** `['filesystem']`
- **container\_depth:** `0`
- **container\_type:** `filesystem`
- **excluded\_from\_analysis:** `True`
- **excluded\_inspection\_incomplete:** `True`
- **inherited\_exclusion\_reason:** `vcs_metadata`
- **inspection\_limitation\_reason:** `runtime_limit`
- **local\_only:** `True`
- **nested\_path:** `.git/hooks/pre-applypatch.sample`
- **outer\_path:** `.git/hooks/pre-applypatch.sample`
- **partially\_analyzed\_executable:** `False`
- **referenced:** `False`

---

### 🔴 HIGH: SC9

**Location:** `.git/hooks/pre-commit.sample:1`  
**Confidence:** 100%  

**Message:** An excluded artifact could not be completely inspected\.

**Remediation:** Review the artifact provenance and the reason executable content is packaged in this location; keep executable files explicit and directly reviewable\.

**Evidence:**
- **concealment:** `vcs_metadata`
- **concealment\_reasons:** `['vcs_metadata']`
- **container\_ancestry:** `['filesystem']`
- **container\_depth:** `0`
- **container\_type:** `filesystem`
- **excluded\_from\_analysis:** `True`
- **excluded\_inspection\_incomplete:** `True`
- **inherited\_exclusion\_reason:** `vcs_metadata`
- **inspection\_limitation\_reason:** `runtime_limit`
- **local\_only:** `True`
- **nested\_path:** `.git/hooks/pre-commit.sample`
- **outer\_path:** `.git/hooks/pre-commit.sample`
- **partially\_analyzed\_executable:** `False`
- **referenced:** `False`

---

### 🔴 HIGH: SC9

**Location:** `.git/hooks/pre-merge-commit.sample:1`  
**Confidence:** 100%  

**Message:** An excluded artifact could not be completely inspected\.

**Remediation:** Review the artifact provenance and the reason executable content is packaged in this location; keep executable files explicit and directly reviewable\.

**Evidence:**
- **concealment:** `vcs_metadata`
- **concealment\_reasons:** `['vcs_metadata']`
- **container\_ancestry:** `['filesystem']`
- **container\_depth:** `0`
- **container\_type:** `filesystem`
- **excluded\_from\_analysis:** `True`
- **excluded\_inspection\_incomplete:** `True`
- **inherited\_exclusion\_reason:** `vcs_metadata`
- **inspection\_limitation\_reason:** `runtime_limit`
- **local\_only:** `True`
- **nested\_path:** `.git/hooks/pre-merge-commit.sample`
- **outer\_path:** `.git/hooks/pre-merge-commit.sample`
- **partially\_analyzed\_executable:** `False`
- **referenced:** `False`

---

### 🔴 HIGH: SC9

**Location:** `.git/hooks/pre-push.sample:1`  
**Confidence:** 100%  

**Message:** An excluded artifact could not be completely inspected\.

**Remediation:** Review the artifact provenance and the reason executable content is packaged in this location; keep executable files explicit and directly reviewable\.

**Evidence:**
- **concealment:** `vcs_metadata`
- **concealment\_reasons:** `['vcs_metadata']`
- **container\_ancestry:** `['filesystem']`
- **container\_depth:** `0`
- **container\_type:** `filesystem`
- **excluded\_from\_analysis:** `True`
- **excluded\_inspection\_incomplete:** `True`
- **inherited\_exclusion\_reason:** `vcs_metadata`
- **inspection\_limitation\_reason:** `runtime_limit`
- **local\_only:** `True`
- **nested\_path:** `.git/hooks/pre-push.sample`
- **outer\_path:** `.git/hooks/pre-push.sample`
- **partially\_analyzed\_executable:** `False`
- **referenced:** `False`

---

### 🔴 HIGH: SC9

**Location:** `.git/hooks/pre-rebase.sample:1`  
**Confidence:** 100%  

**Message:** An excluded artifact could not be completely inspected\.

**Remediation:** Review the artifact provenance and the reason executable content is packaged in this location; keep executable files explicit and directly reviewable\.

**Evidence:**
- **concealment:** `vcs_metadata`
- **concealment\_reasons:** `['vcs_metadata']`
- **container\_ancestry:** `['filesystem']`
- **container\_depth:** `0`
- **container\_type:** `filesystem`
- **excluded\_from\_analysis:** `True`
- **excluded\_inspection\_incomplete:** `True`
- **inherited\_exclusion\_reason:** `vcs_metadata`
- **inspection\_limitation\_reason:** `runtime_limit`
- **local\_only:** `True`
- **nested\_path:** `.git/hooks/pre-rebase.sample`
- **outer\_path:** `.git/hooks/pre-rebase.sample`
- **partially\_analyzed\_executable:** `False`
- **referenced:** `False`

---

### 🔴 HIGH: SC9

**Location:** `.git/hooks/pre-receive.sample:1`  
**Confidence:** 100%  

**Message:** An excluded artifact could not be completely inspected\.

**Remediation:** Review the artifact provenance and the reason executable content is packaged in this location; keep executable files explicit and directly reviewable\.

**Evidence:**
- **concealment:** `vcs_metadata`
- **concealment\_reasons:** `['vcs_metadata']`
- **container\_ancestry:** `['filesystem']`
- **container\_depth:** `0`
- **container\_type:** `filesystem`
- **excluded\_from\_analysis:** `True`
- **excluded\_inspection\_incomplete:** `True`
- **inherited\_exclusion\_reason:** `vcs_metadata`
- **inspection\_limitation\_reason:** `runtime_limit`
- **local\_only:** `True`
- **nested\_path:** `.git/hooks/pre-receive.sample`
- **outer\_path:** `.git/hooks/pre-receive.sample`
- **partially\_analyzed\_executable:** `False`
- **referenced:** `False`

---

### 🔴 HIGH: SC9

**Location:** `.git/hooks/prepare-commit-msg.sample:1`  
**Confidence:** 100%  

**Message:** An excluded artifact could not be completely inspected\.

**Remediation:** Review the artifact provenance and the reason executable content is packaged in this location; keep executable files explicit and directly reviewable\.

**Evidence:**
- **concealment:** `vcs_metadata`
- **concealment\_reasons:** `['vcs_metadata']`
- **container\_ancestry:** `['filesystem']`
- **container\_depth:** `0`
- **container\_type:** `filesystem`
- **excluded\_from\_analysis:** `True`
- **excluded\_inspection\_incomplete:** `True`
- **inherited\_exclusion\_reason:** `vcs_metadata`
- **inspection\_limitation\_reason:** `runtime_limit`
- **local\_only:** `True`
- **nested\_path:** `.git/hooks/prepare-commit-msg.sample`
- **outer\_path:** `.git/hooks/prepare-commit-msg.sample`
- **partially\_analyzed\_executable:** `False`
- **referenced:** `False`

---

### 🔴 HIGH: SC9

**Location:** `.git/hooks/push-to-checkout.sample:1`  
**Confidence:** 100%  

**Message:** An excluded artifact could not be completely inspected\.

**Remediation:** Review the artifact provenance and the reason executable content is packaged in this location; keep executable files explicit and directly reviewable\.

**Evidence:**
- **concealment:** `vcs_metadata`
- **concealment\_reasons:** `['vcs_metadata']`
- **container\_ancestry:** `['filesystem']`
- **container\_depth:** `0`
- **container\_type:** `filesystem`
- **excluded\_from\_analysis:** `True`
- **excluded\_inspection\_incomplete:** `True`
- **inherited\_exclusion\_reason:** `vcs_metadata`
- **inspection\_limitation\_reason:** `runtime_limit`
- **local\_only:** `True`
- **nested\_path:** `.git/hooks/push-to-checkout.sample`
- **outer\_path:** `.git/hooks/push-to-checkout.sample`
- **partially\_analyzed\_executable:** `False`
- **referenced:** `False`

---

### 🔴 HIGH: SC9

**Location:** `.git/hooks/sendemail-validate.sample:1`  
**Confidence:** 100%  

**Message:** An excluded artifact could not be completely inspected\.

**Remediation:** Review the artifact provenance and the reason executable content is packaged in this location; keep executable files explicit and directly reviewable\.

**Evidence:**
- **concealment:** `vcs_metadata`
- **concealment\_reasons:** `['vcs_metadata']`
- **container\_ancestry:** `['filesystem']`
- **container\_depth:** `0`
- **container\_type:** `filesystem`
- **excluded\_from\_analysis:** `True`
- **excluded\_inspection\_incomplete:** `True`
- **inherited\_exclusion\_reason:** `vcs_metadata`
- **inspection\_limitation\_reason:** `runtime_limit`
- **local\_only:** `True`
- **nested\_path:** `.git/hooks/sendemail-validate.sample`
- **outer\_path:** `.git/hooks/sendemail-validate.sample`
- **partially\_analyzed\_executable:** `False`
- **referenced:** `False`

---

### 🔴 HIGH: SC9

**Location:** `.git/hooks/update.sample:1`  
**Confidence:** 100%  

**Message:** An excluded artifact could not be completely inspected\.

**Remediation:** Review the artifact provenance and the reason executable content is packaged in this location; keep executable files explicit and directly reviewable\.

**Evidence:**
- **concealment:** `vcs_metadata`
- **concealment\_reasons:** `['vcs_metadata']`
- **container\_ancestry:** `['filesystem']`
- **container\_depth:** `0`
- **container\_type:** `filesystem`
- **excluded\_from\_analysis:** `True`
- **excluded\_inspection\_incomplete:** `True`
- **inherited\_exclusion\_reason:** `vcs_metadata`
- **inspection\_limitation\_reason:** `runtime_limit`
- **local\_only:** `True`
- **nested\_path:** `.git/hooks/update.sample`
- **outer\_path:** `.git/hooks/update.sample`
- **partially\_analyzed\_executable:** `False`
- **referenced:** `False`

---

### 🔴 HIGH: SC9

**Location:** `.git/index:1`  
**Confidence:** 100%  

**Message:** An excluded artifact could not be completely inspected\.

**Remediation:** Review the artifact provenance and the reason executable content is packaged in this location; keep executable files explicit and directly reviewable\.

**Evidence:**
- **concealment:** `vcs_metadata`
- **concealment\_reasons:** `['vcs_metadata']`
- **container\_ancestry:** `['filesystem']`
- **container\_depth:** `0`
- **container\_type:** `filesystem`
- **excluded\_from\_analysis:** `True`
- **excluded\_inspection\_incomplete:** `True`
- **inherited\_exclusion\_reason:** `vcs_metadata`
- **inspection\_limitation\_reason:** `runtime_limit`
- **local\_only:** `True`
- **nested\_path:** `.git/index`
- **outer\_path:** `.git/index`
- **partially\_analyzed\_executable:** `False`
- **referenced:** `False`

---

### 🔴 HIGH: SC9

**Location:** `.git/info/exclude:1`  
**Confidence:** 100%  

**Message:** An excluded artifact could not be completely inspected\.

**Remediation:** Review the artifact provenance and the reason executable content is packaged in this location; keep executable files explicit and directly reviewable\.

**Evidence:**
- **concealment:** `vcs_metadata`
- **concealment\_reasons:** `['vcs_metadata']`
- **container\_ancestry:** `['filesystem']`
- **container\_depth:** `0`
- **container\_type:** `filesystem`
- **excluded\_from\_analysis:** `True`
- **excluded\_inspection\_incomplete:** `True`
- **inherited\_exclusion\_reason:** `vcs_metadata`
- **inspection\_limitation\_reason:** `runtime_limit`
- **local\_only:** `True`
- **nested\_path:** `.git/info/exclude`
- **outer\_path:** `.git/info/exclude`
- **partially\_analyzed\_executable:** `False`
- **referenced:** `False`

---

### 🔴 HIGH: SC9

**Location:** `.git/logs/HEAD:1`  
**Confidence:** 100%  

**Message:** An excluded artifact could not be completely inspected\.

**Remediation:** Review the artifact provenance and the reason executable content is packaged in this location; keep executable files explicit and directly reviewable\.

**Evidence:**
- **concealment:** `vcs_metadata`
- **concealment\_reasons:** `['vcs_metadata']`
- **container\_ancestry:** `['filesystem']`
- **container\_depth:** `0`
- **container\_type:** `filesystem`
- **excluded\_from\_analysis:** `True`
- **excluded\_inspection\_incomplete:** `True`
- **inherited\_exclusion\_reason:** `vcs_metadata`
- **inspection\_limitation\_reason:** `runtime_limit`
- **local\_only:** `True`
- **nested\_path:** `.git/logs/HEAD`
- **outer\_path:** `.git/logs/HEAD`
- **partially\_analyzed\_executable:** `False`
- **referenced:** `False`

---

### 🔴 HIGH: SC9

**Location:** `.git/logs/refs/heads/master:1`  
**Confidence:** 100%  

**Message:** An excluded artifact could not be completely inspected\.

**Remediation:** Review the artifact provenance and the reason executable content is packaged in this location; keep executable files explicit and directly reviewable\.

**Evidence:**
- **concealment:** `vcs_metadata`
- **concealment\_reasons:** `['vcs_metadata']`
- **container\_ancestry:** `['filesystem']`
- **container\_depth:** `0`
- **container\_type:** `filesystem`
- **excluded\_from\_analysis:** `True`
- **excluded\_inspection\_incomplete:** `True`
- **inherited\_exclusion\_reason:** `vcs_metadata`
- **inspection\_limitation\_reason:** `runtime_limit`
- **local\_only:** `True`
- **nested\_path:** `.git/logs/refs/heads/master`
- **outer\_path:** `.git/logs/refs/heads/master`
- **partially\_analyzed\_executable:** `False`
- **referenced:** `False`

---

### 🔴 HIGH: SC9

**Location:** `.git/logs/refs/remotes/origin/HEAD:1`  
**Confidence:** 100%  

**Message:** An excluded artifact could not be completely inspected\.

**Remediation:** Review the artifact provenance and the reason executable content is packaged in this location; keep executable files explicit and directly reviewable\.

**Evidence:**
- **concealment:** `vcs_metadata`
- **concealment\_reasons:** `['vcs_metadata']`
- **container\_ancestry:** `['filesystem']`
- **container\_depth:** `0`
- **container\_type:** `filesystem`
- **excluded\_from\_analysis:** `True`
- **excluded\_inspection\_incomplete:** `True`
- **inherited\_exclusion\_reason:** `vcs_metadata`
- **inspection\_limitation\_reason:** `runtime_limit`
- **local\_only:** `True`
- **nested\_path:** `.git/logs/refs/remotes/origin/HEAD`
- **outer\_path:** `.git/logs/refs/remotes/origin/HEAD`
- **partially\_analyzed\_executable:** `False`
- **referenced:** `False`

---

### 🔴 HIGH: SC9

**Location:** `.git/objects/pack/pack-b05a52a0552dcfd9811f1715d8cf1cc1fdda78a3.idx:1`  
**Confidence:** 100%  

**Message:** An excluded artifact could not be completely inspected\.

**Remediation:** Review the artifact provenance and the reason executable content is packaged in this location; keep executable files explicit and directly reviewable\.

**Evidence:**
- **concealment:** `vcs_metadata`
- **concealment\_reasons:** `['vcs_metadata']`
- **container\_ancestry:** `['filesystem']`
- **container\_depth:** `0`
- **container\_type:** `filesystem`
- **excluded\_from\_analysis:** `True`
- **excluded\_inspection\_incomplete:** `True`
- **inherited\_exclusion\_reason:** `vcs_metadata`
- **inspection\_limitation\_reason:** `runtime_limit`
- **local\_only:** `True`
- **nested\_path:** `.git/objects/pack/pack-b05a52a0552dcfd9811f1715d8cf1cc1fdda78a3.idx`
- **outer\_path:** `.git/objects/pack/pack-b05a52a0552dcfd9811f1715d8cf1cc1fdda78a3.idx`
- **partially\_analyzed\_executable:** `False`
- **referenced:** `False`

---

### 🔴 HIGH: SC9

**Location:** `.git/objects/pack/pack-b05a52a0552dcfd9811f1715d8cf1cc1fdda78a3.pack:1`  
**Confidence:** 100%  

**Message:** An excluded artifact could not be completely inspected\.

**Remediation:** Review the artifact provenance and the reason executable content is packaged in this location; keep executable files explicit and directly reviewable\.

**Evidence:**
- **concealment:** `vcs_metadata`
- **concealment\_reasons:** `['vcs_metadata']`
- **container\_ancestry:** `['filesystem']`
- **container\_depth:** `0`
- **container\_type:** `filesystem`
- **excluded\_from\_analysis:** `True`
- **excluded\_inspection\_incomplete:** `True`
- **inherited\_exclusion\_reason:** `vcs_metadata`
- **inspection\_limitation\_reason:** `runtime_limit`
- **local\_only:** `True`
- **nested\_path:** `.git/objects/pack/pack-b05a52a0552dcfd9811f1715d8cf1cc1fdda78a3.pack`
- **outer\_path:** `.git/objects/pack/pack-b05a52a0552dcfd9811f1715d8cf1cc1fdda78a3.pack`
- **partially\_analyzed\_executable:** `False`
- **referenced:** `False`

---

### 🔴 HIGH: SC9

**Location:** `.git/objects/pack/pack-b05a52a0552dcfd9811f1715d8cf1cc1fdda78a3.rev:1`  
**Confidence:** 100%  

**Message:** An excluded artifact could not be completely inspected\.

**Remediation:** Review the artifact provenance and the reason executable content is packaged in this location; keep executable files explicit and directly reviewable\.

**Evidence:**
- **concealment:** `vcs_metadata`
- **concealment\_reasons:** `['vcs_metadata']`
- **container\_ancestry:** `['filesystem']`
- **container\_depth:** `0`
- **container\_type:** `filesystem`
- **excluded\_from\_analysis:** `True`
- **excluded\_inspection\_incomplete:** `True`
- **inherited\_exclusion\_reason:** `vcs_metadata`
- **inspection\_limitation\_reason:** `runtime_limit`
- **local\_only:** `True`
- **nested\_path:** `.git/objects/pack/pack-b05a52a0552dcfd9811f1715d8cf1cc1fdda78a3.rev`
- **outer\_path:** `.git/objects/pack/pack-b05a52a0552dcfd9811f1715d8cf1cc1fdda78a3.rev`
- **partially\_analyzed\_executable:** `False`
- **referenced:** `False`

---

### 🔴 HIGH: SC9

**Location:** `.git/packed-refs:1`  
**Confidence:** 100%  

**Message:** An excluded artifact could not be completely inspected\.

**Remediation:** Review the artifact provenance and the reason executable content is packaged in this location; keep executable files explicit and directly reviewable\.

**Evidence:**
- **concealment:** `vcs_metadata`
- **concealment\_reasons:** `['vcs_metadata']`
- **container\_ancestry:** `['filesystem']`
- **container\_depth:** `0`
- **container\_type:** `filesystem`
- **excluded\_from\_analysis:** `True`
- **excluded\_inspection\_incomplete:** `True`
- **inherited\_exclusion\_reason:** `vcs_metadata`
- **inspection\_limitation\_reason:** `runtime_limit`
- **local\_only:** `True`
- **nested\_path:** `.git/packed-refs`
- **outer\_path:** `.git/packed-refs`
- **partially\_analyzed\_executable:** `False`
- **referenced:** `False`

---

### 🔴 HIGH: SC9

**Location:** `.git/refs/heads/master:1`  
**Confidence:** 100%  

**Message:** An excluded artifact could not be completely inspected\.

**Remediation:** Review the artifact provenance and the reason executable content is packaged in this location; keep executable files explicit and directly reviewable\.

**Evidence:**
- **concealment:** `vcs_metadata`
- **concealment\_reasons:** `['vcs_metadata']`
- **container\_ancestry:** `['filesystem']`
- **container\_depth:** `0`
- **container\_type:** `filesystem`
- **excluded\_from\_analysis:** `True`
- **excluded\_inspection\_incomplete:** `True`
- **inherited\_exclusion\_reason:** `vcs_metadata`
- **inspection\_limitation\_reason:** `runtime_limit`
- **local\_only:** `True`
- **nested\_path:** `.git/refs/heads/master`
- **outer\_path:** `.git/refs/heads/master`
- **partially\_analyzed\_executable:** `False`
- **referenced:** `False`

---

### 🔴 HIGH: SC9

**Location:** `.git/refs/remotes/origin/HEAD:1`  
**Confidence:** 100%  

**Message:** An excluded artifact could not be completely inspected\.

**Remediation:** Review the artifact provenance and the reason executable content is packaged in this location; keep executable files explicit and directly reviewable\.

**Evidence:**
- **concealment:** `vcs_metadata`
- **concealment\_reasons:** `['vcs_metadata']`
- **container\_ancestry:** `['filesystem']`
- **container\_depth:** `0`
- **container\_type:** `filesystem`
- **excluded\_from\_analysis:** `True`
- **excluded\_inspection\_incomplete:** `True`
- **inherited\_exclusion\_reason:** `vcs_metadata`
- **inspection\_limitation\_reason:** `runtime_limit`
- **local\_only:** `True`
- **nested\_path:** `.git/refs/remotes/origin/HEAD`
- **outer\_path:** `.git/refs/remotes/origin/HEAD`
- **partially\_analyzed\_executable:** `False`
- **referenced:** `False`

---

### 🔴 HIGH: SC9

**Location:** `.git/shallow:1`  
**Confidence:** 100%  

**Message:** An excluded artifact could not be completely inspected\.

**Remediation:** Review the artifact provenance and the reason executable content is packaged in this location; keep executable files explicit and directly reviewable\.

**Evidence:**
- **concealment:** `vcs_metadata`
- **concealment\_reasons:** `['vcs_metadata']`
- **container\_ancestry:** `['filesystem']`
- **container\_depth:** `0`
- **container\_type:** `filesystem`
- **excluded\_from\_analysis:** `True`
- **excluded\_inspection\_incomplete:** `True`
- **inherited\_exclusion\_reason:** `vcs_metadata`
- **inspection\_limitation\_reason:** `runtime_limit`
- **local\_only:** `True`
- **nested\_path:** `.git/shallow`
- **outer\_path:** `.git/shallow`
- **partially\_analyzed\_executable:** `False`
- **referenced:** `False`

---

### 🔴 HIGH: YR4

**Location:** `tests/cache/aljazeera.com.malawians.html:1`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/cache/befifty.montauk.html:40`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/cache/blog.wordpress.com.diverse.html:82`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/cache/brigitte.de.ikigai.html:1479`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/cache/buchperlen.wordpress.com.html:47`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/cache/chineselyrics4u.com.zhineng.html:458`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/cache/chip.de.beef.html:234`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/cache/faz.net.streaming.html:243`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/cache/franceculture.fr.idees.html:37`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/cache/github.blog.spiceland.html:34`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/cache/kulu-media.com.meta-outage.html:2`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/cache/lady50plus.de.sekre.html:41`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/cache/luxuryhaven.co.hyatt.html:267`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/cache/reuters.com.parasite.html:84`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/cache/scmp.com.playbook.html:95`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/cache/spiegel.de.albtraum.html:1234`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/cache/vancouversun.com.microsoft.html:177`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/cache/vice.com.amazon.html:602`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/cache/zeit.de.zugverkehr.html:147`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/eval/0ac0531f1f0543f4a3f68159e5fd1875.html:37`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/eval/1000things.at-Wellnessoasen.html:3`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/eval/1337kultur.de.picard.html:487`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/eval/24ora.com-internationalschol.html:31`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/eval/7mind.de.grenzen.html:9`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/eval/Dezubekizacja – reaktywacja. Czyli daty mają znaczenie - Dziennik.pl.html:263`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/eval/Ile jest warta godzina pracy_ W tych krajach praca popłaca - Forsal.pl.html:275`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/eval/Ile jest warta godzina pracy_ W tych krajach praca popłaca - Forsal.pl.html:848`  
**Confidence:** 75%  

**Message:** YARA rule 'privilege\_escalation\_tools': Privilege escalation tools and techniques \[hacktools\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/eval/Jest zgoda PE na umowę handlową między UE a Londynem.html:27`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/eval/KATAPULT-Magazin.de-parteien.html:12`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/eval/Popkultur.de-Schauspieler.html:40`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/eval/Raptastisch.net-Seitenhieb.html:31`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/eval/Windows 10 od lipca przestanie obsługiwać Adobe Flash.html:9`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/eval/abookshelffullofsunshine.blogspot.com.interview.html:35`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/eval/ambito.com-paritarias.html:4`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/eval/angelmagazin.de-schmerzen.html:38`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/eval/archive.org.swap-stop.org.shuji.html:29`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/eval/backen.de.maulwurfkuchen.html:1902`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/eval/bauemotion.de-schneereampflicht.html:165`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/eval/baumeister.de.sportzentrum.html:63`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/eval/bettycrocker.com.pineapple.html:18`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/eval/bewusster-leben.de.hope.html:61`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/eval/beyssonmanagement.com.innovation.html:204`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/eval/biathlonword.com-chinesisch.html:261`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: YR4

**Location:** `tests/eval/blog.teufel.de.leistung.html:1`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | partial |
| Dependency contents | not\_requested |
| Coverage | 0\.0% |
| Fully inspected | 0 |
| Partially inspected | 391 |
| Entirely uninspected | 816 |

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
| binary\_text\_projection | `docs/trafilatura-demo.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |

### Ledger Exceptions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| runtime\_limit | `.coveragerc` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `.coveragerc` | Inspection reached its configured runtime limit\. |
| archive\_time\_limit | `.coveragerc` | Cumulative archive inspection time limit was reached\. |
| runtime\_limit | `.coveragerc` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `.coveragerc` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `.coveragerc` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `.coveragerc` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `.git/HEAD` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `.git/config` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `.git/config` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `.gitattributes` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `.gitattributes` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `.github/FUNDING.yml` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `.github/FUNDING.yml` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `.github/ISSUE_TEMPLATE/bug_report.yml` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `.github/ISSUE_TEMPLATE/bug_report.yml` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `.github/ISSUE_TEMPLATE/feature_request.yml` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `.github/ISSUE_TEMPLATE/feature_request.yml` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `.github/pull_request_template.md` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `.github/pull_request_template.md` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `.github/workflows/codeql.yml` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `.github/workflows/codeql.yml` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `.github/workflows/tests.yml` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `.github/workflows/tests.yml` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `.gitignore` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `.gitignore` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `.readthedocs.yaml` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `.readthedocs.yaml` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `AGENTS.md` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `AGENTS.md` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `CITATION.cff` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `CITATION.cff` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `CONTRIBUTING.md` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `CONTRIBUTING.md` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `HISTORY.md` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `HISTORY.md` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `LICENSE` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `LICENSE` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `MANIFEST.in` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `MANIFEST.in` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `README.md` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `README.md` | Inspection reached its configured runtime limit\. |
| manifest\_parse\_limit | `SKILL.md` | Manifest frontmatter could not be completely examined within its resource limits\. |
| runtime\_limit | `docs/Makefile` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/Makefile` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/Trafilatura_Overview.ipynb` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/Trafilatura_Overview.ipynb` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/background.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/background.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/compendium.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/compendium.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/conf.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/conf.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/corefunctions.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/corefunctions.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/corpus-data.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/corpus-data.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/crawls.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/crawls.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/deduplication.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/deduplication.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/deprecations.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/deprecations.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/docs_tests.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/docs_tests.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/downloads.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/downloads.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/dwds-count-exportieren.jpg` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/dwds-count-exportieren.jpg` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/dwds-exportieren.jpg` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/dwds-exportieren.jpg` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/dwds-treffer-exportieren.jpg` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/dwds-treffer-exportieren.jpg` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/evaluation.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/evaluation.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/extraction-overview.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/extraction-overview.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/faq.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/faq.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/gui-screenshot.png` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/gui-screenshot.png` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/index.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/index.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/installation.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/installation.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/make.bat` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/make.bat` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/quickstart.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/quickstart.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/robots.txt` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/robots.txt` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/settings.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/settings.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/software-ecosystem.png` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/software-ecosystem.png` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/sources.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/sources.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/tests.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/tests.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/trafilatura-demo.gif` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/trafilatura-demo.gif` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/trafilatura-logo.png` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/trafilatura-logo.png` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/troubleshooting.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/troubleshooting.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/tutorial-chromadb.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/tutorial-chromadb.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/tutorial-corpus.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/tutorial-corpus.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/tutorial-datasets.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/tutorial-datasets.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/tutorial-dwds.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/tutorial-dwds.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/tutorial-epsilla.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/tutorial-epsilla.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/tutorial-frequencies.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/tutorial-frequencies.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/tutorial-rag.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/tutorial-rag.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/tutorial-tei.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/tutorial-tei.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/tutorial0.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/tutorial0.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/tutorial1.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/tutorial1.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/tutorial2.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/tutorial2.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/tutorials.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/tutorials.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/url-management.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/url-management.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/usage-api.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/usage-api.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/usage-cli.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/usage-cli.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/usage-gui.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/usage-gui.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/usage-python.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/usage-python.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/usage-r.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/usage-r.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/usage.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/usage.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/used-by.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/used-by.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `pyproject.toml` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `pyproject.toml` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/README.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/README.rst` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/__init__.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/__init__.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/baseline_tests.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/baseline_tests.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/adac.de.kindersitze.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/adac.de.kindersitze.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/aljazeera.com.malawians.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/aljazeera.com.malawians.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/austria.info.radfahren.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/austria.info.radfahren.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/basicthinking.de.tweets.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/basicthinking.de.tweets.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/befifty.montauk.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/befifty.montauk.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/blog.python.org.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/blog.python.org.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/blog.wordpress.com.diverse.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/blog.wordpress.com.diverse.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/bmjv.de.konsum.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/bmjv.de.konsum.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/boingboing.net.millenials.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/boingboing.net.millenials.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/brandenburg.de.homo-brandenburgensis.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/brandenburg.de.homo-brandenburgensis.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/brigitte.de.ikigai.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/brigitte.de.ikigai.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/buchperlen.wordpress.com.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/buchperlen.wordpress.com.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/caktusgroup.com.django.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/caktusgroup.com.django.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/cdu-fraktion-erfurt.de.waldorfschule.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/cdu-fraktion-erfurt.de.waldorfschule.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/changelog.blog.zwischenbilanz.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/changelog.blog.zwischenbilanz.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/chineselyrics4u.com.zhineng.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/chineselyrics4u.com.zhineng.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/chip.de.beef.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/chip.de.beef.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/chip.de.tests.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/chip.de.tests.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/cnet.de.schutz.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/cnet.de.schutz.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/computerbase.de.htc.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/computerbase.de.htc.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/correctiv.org.zusage.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/correctiv.org.zusage.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/crazy-julia.de.tipps.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/crazy-julia.de.tipps.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/creativecommons.at.faircoin.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/creativecommons.at.faircoin.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/creativecommons.org.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/creativecommons.org.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/de.creativecommons.org.endlich.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/de.creativecommons.org.endlich.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/demokratiewebstatt.at.luft.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/demokratiewebstatt.at.luft.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/denkanstoos.com.2012.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/denkanstoos.com.2012.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/die-partei.net.luebeck.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/die-partei.net.luebeck.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/dw.com.colonial.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/dw.com.colonial.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/dw.com.uncork.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/dw.com.uncork.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/ebrosia.de.zinfandel.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/ebrosia.de.zinfandel.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/eluniverso.com.repatriar.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/eluniverso.com.repatriar.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/en.wikipedia.org.tsne.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/en.wikipedia.org.tsne.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/erp-news.info.interview.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/erp-news.info.interview.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/fairkom.eu.about.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/fairkom.eu.about.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/faz.net.streaming.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/faz.net.streaming.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/franceculture.fr.idees.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/franceculture.fr.idees.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/franziska-elea.de.vuitton.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/franziska-elea.de.vuitton.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/futurezone.at.lyft.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/futurezone.at.lyft.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/github.blog.spiceland.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/github.blog.spiceland.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/gofeminin.de.abnehmen.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/gofeminin.de.abnehmen.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/gregoryszorc.com.python3.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/gregoryszorc.com.python3.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/gruen-digital.de.jahrestagung.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/gruen-digital.de.jahrestagung.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/heise.de.lithium.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/heise.de.lithium.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/hundeverein-kreisunna.de.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/hundeverein-kreisunna.de.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/iloveponysmag.com.barbour.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/iloveponysmag.com.barbour.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/incurvy.de.wellness.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/incurvy.de.wellness.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/infobae.com.terremoto.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/infobae.com.terremoto.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/internet-law.de.pseudonymen.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/internet-law.de.pseudonymen.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/jolie.de.adele.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/jolie.de.adele.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/jovelstefan.de.gefallt.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/jovelstefan.de.gefallt.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/knowtechie.com.rally.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/knowtechie.com.rally.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/kulinariaathome.com.mandelplätzchen.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/kulinariaathome.com.mandelplätzchen.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/kulu-media.com.meta-outage.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/kulu-media.com.meta-outage.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/lady50plus.de.sekre.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/lady50plus.de.sekre.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/landwirt.com.sensortechnik.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/landwirt.com.sensortechnik.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/lanouvellerepublique.fr.martin.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/lanouvellerepublique.fr.martin.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/laviedesidees.fr.evaluation.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/laviedesidees.fr.evaluation.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/lemire.me.json.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/lemire.me.json.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/love-hina.ch.0409.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/love-hina.ch.0409.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/luxuriousmagazine.com.polo.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/luxuriousmagazine.com.polo.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/luxuryhaven.co.hyatt.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/luxuryhaven.co.hyatt.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/majkaswelt.com.fashion.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/majkaswelt.com.fashion.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/meedia.de.freenet.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/meedia.de.freenet.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/mercurynews.com.2023.01.16.letters-1119.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/mercurynews.com.2023.01.16.letters-1119.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/mixed.de.vrodo.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/mixed.de.vrodo.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/modepilot.de.duschkopf.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/modepilot.de.duschkopf.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/moritz-meyer.net.vreni.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/moritz-meyer.net.vreni.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/nationalgeographic.co.uk.goats.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/nationalgeographic.co.uk.goats.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/nature.com.telescope.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/nature.com.telescope.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/ndr.de.podcastcoronavirus140.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/ndr.de.podcastcoronavirus140.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/netzpolitik.org.abmahnungen.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/netzpolitik.org.abmahnungen.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/novalanalove.com.ear-candy.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/novalanalove.com.ear-candy.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/otto.de.twoforfashion.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/otto.de.twoforfashion.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/pcgamer.com.skyrim.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/pcgamer.com.skyrim.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/phys.org.tool.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/phys.org.tool.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/piratenpartei-mv.de.grundeinkommen.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/piratenpartei-mv.de.grundeinkommen.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/plentylife.blogspot.pamela-reif.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/plentylife.blogspot.pamela-reif.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/pluralsight.com.python.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/pluralsight.com.python.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/psl.eu.luniversite.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/psl.eu.luniversite.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/rechtambild.de.kochbuch.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/rechtambild.de.kochbuch.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/reuters.com.parasite.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/reuters.com.parasite.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/rnz.de.witzel.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/rnz.de.witzel.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/rs-ingenieure.de.tragwerksplanung.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/rs-ingenieure.de.tragwerksplanung.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/salon.com.emissions.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/salon.com.emissions.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/sauvonsluniversite.com.spip.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/sauvonsluniversite.com.spip.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/schleifen.ucoz.de.briefe.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/schleifen.ucoz.de.briefe.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/scmp.com.playbook.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/scmp.com.playbook.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/shingon-reiki.de.schamanismus.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/shingon-reiki.de.schamanismus.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/simplyscience.ch.erdoel.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/simplyscience.ch.erdoel.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/skateboardmsm.de.dormhagen.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/skateboardmsm.de.dormhagen.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/sonntag-sachsen.de.emanuel.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/sonntag-sachsen.de.emanuel.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/soundofscience.fr.1927.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/soundofscience.fr.1927.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/speicherguide.de.schwierige.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/speicherguide.de.schwierige.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/spektrum.de.engelbart.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/spektrum.de.engelbart.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/spiegel.de.albtraum.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/spiegel.de.albtraum.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/spreeblick.com.habeck.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/spreeblick.com.habeck.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/stackoverflow.com.rust.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/stackoverflow.com.rust.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/stuttgart.de.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/stuttgart.de.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/sueddeutsche.de.flixtrain.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/sueddeutsche.de.flixtrain.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/telemedicus.info.rezension.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/telemedicus.info.rezension.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/theguardian.com.academics.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/theguardian.com.academics.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/theplanetarypress.com.forestlands.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/theplanetarypress.com.forestlands.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/theverge.com.ios13.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/theverge.com.ios13.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/threatpost.com.android.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/threatpost.com.android.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/toralin.de.schmierfett.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/toralin.de.schmierfett.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/vancouversun.com.microsoft.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/vancouversun.com.microsoft.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/vice.com.amazon.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/vice.com.amazon.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/viehbacher.com.steuerrecht.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/viehbacher.com.steuerrecht.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/wehranlage-horka.de.887.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/wehranlage-horka.de.887.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/wikimediafoundation.org.turkey.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/wikimediafoundation.org.turkey.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/womencantalksports.com.top10.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/womencantalksports.com.top10.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/zeit.de.zugverkehr.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cache/zeit.de.zugverkehr.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cli_tests.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/cli_tests.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/conftest.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/conftest.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/deduplication_tests.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/deduplication_tests.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/downloads_tests.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/downloads_tests.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/0a12df42d1764095989ab078ee0f940b.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/0a12df42d1764095989ab078ee0f940b.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/0a24692a9ea846c1819bd6a5f92a8874.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/0a24692a9ea846c1819bd6a5f92a8874.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/0a29620f9c4347758c146ed06dab6f3e.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/0a29620f9c4347758c146ed06dab6f3e.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/0a3108e507c54157a95fe7a1338f5e9c.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/0a3108e507c54157a95fe7a1338f5e9c.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/0a4a8ab61c054192b1ec70cc3570cf45.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/0a4a8ab61c054192b1ec70cc3570cf45.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/0a6291ebbce449b3b04256b43c73e39d.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/0a6291ebbce449b3b04256b43c73e39d.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/0a962f6bcd5649f7a7e6effa338df80d.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/0a962f6bcd5649f7a7e6effa338df80d.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/0ac0531f1f0543f4a3f68159e5fd1875.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/0ac0531f1f0543f4a3f68159e5fd1875.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/0af99c85f22b451a93a75bbf99ac412e.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/0af99c85f22b451a93a75bbf99ac412e.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/0afd671fc2b64f3caa83a91537e8d343.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/0afd671fc2b64f3caa83a91537e8d343.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/0b4609a864eb4fa0bbcb2b395f6be9eb.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/0b4609a864eb4fa0bbcb2b395f6be9eb.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/0b5db24739704283849ca3ed20ce09d4.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/0b5db24739704283849ca3ed20ce09d4.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/0b66696af800472190a76b26faa845d4.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/0b66696af800472190a76b26faa845d4.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/0b96fc66e2c94f45a1b923ec9a31fcf2.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/0b96fc66e2c94f45a1b923ec9a31fcf2.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/1000things.at-Wellnessoasen.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/1000things.at-Wellnessoasen.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/100noticias.com-millones.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/100noticias.com-millones.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/1337kultur.de.picard.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/1337kultur.de.picard.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/1hundetagebuch.wordpress.com.langer.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/1hundetagebuch.wordpress.com.langer.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/24horas.cl-segundo.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/24horas.cl-segundo.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/24ora.com-internationalschol.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/24ora.com-internationalschol.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/2gewinnt.wordpress.com.uns.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/2gewinnt.wordpress.com.uns.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/5min.at-Villachs.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/5min.at-Villachs.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/7mind.de.grenzen.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/7mind.de.grenzen.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/90min.de-Bundesliga-Tabelle.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/90min.de-Bundesliga-Tabelle.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Angus Barbieri. Nie jadł przez 382 dni - Menway w INTERIA.PL.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Angus Barbieri. Nie jadł przez 382 dni - Menway w INTERIA.PL.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Dezubekizacja – reaktywacja. Czyli daty mają znaczenie - Dziennik.pl.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Dezubekizacja – reaktywacja. Czyli daty mają znaczenie - Dziennik.pl.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Eurocash rusza z Innowacyjną Platformą Handlu - Handel dystrybucja.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Eurocash rusza z Innowacyjną Platformą Handlu - Handel dystrybucja.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Eurostat_ Polska z najniższym bezrobociem w całej UE.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Eurostat_ Polska z najniższym bezrobociem w całej UE.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Finowie odkrywają wino _ Res Publica Nowa.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Finowie odkrywają wino _ Res Publica Nowa.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Ile jest warta godzina pracy_ W tych krajach praca popłaca - Forsal.pl.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Ile jest warta godzina pracy_ W tych krajach praca popłaca - Forsal.pl.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Jest zgoda PE na umowę handlową między UE a Londynem.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Jest zgoda PE na umowę handlową między UE a Londynem.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Journalistenwatch.com-Ladensterben.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Journalistenwatch.com-Ladensterben.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/KATAPULT-Magazin.de-parteien.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/KATAPULT-Magazin.de-parteien.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Koncesjonowana opozycja -Leszek Jażdżewski - Liberté!.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Koncesjonowana opozycja -Leszek Jażdżewski - Liberté!.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Lebensmittelpraxis.de-Stadtzentrum.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Lebensmittelpraxis.de-Stadtzentrum.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Maciej Krzysztoszek rzecznik prasowy Amica menedżer komunikacji zewnętrznej.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Maciej Krzysztoszek rzecznik prasowy Amica menedżer komunikacji zewnętrznej.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Nowa Zelandia_ płatny urlop dla rodziców poronionego dziecka. Jak to wygląda w Polsce_ — Klub Jagielloński.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Nowa Zelandia_ płatny urlop dla rodziców poronionego dziecka. Jak to wygląda w Polsce_ — Klub Jagielloński.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/OnlineMarketing.de-Instagram.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/OnlineMarketing.de-Instagram.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Ostbelgiendirekt.be-ARD-Doku.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Ostbelgiendirekt.be-ARD-Doku.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Osthessen-news.de-Buergermeisterwahl.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Osthessen-news.de-Buergermeisterwahl.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Popkultur.de-Schauspieler.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Popkultur.de-Schauspieler.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Raptastisch.net-Seitenhieb.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Raptastisch.net-Seitenhieb.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Rosjanie sugerują natychmiastowe odcięcie Polski od gazu - Energetyka24.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Rosjanie sugerują natychmiastowe odcięcie Polski od gazu - Energetyka24.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Rosyjskie zamachy w Czechach – kontekst krajowy, implikacje, perspektywy.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Rosyjskie zamachy w Czechach – kontekst krajowy, implikacje, perspektywy.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/SW1.News-Heimat.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/SW1.News-Heimat.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Solarserver.de.solarthermisches kraftwerk dubai.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Solarserver.de.solarthermisches kraftwerk dubai.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Sprzeciw wobec ataków na Fundację Lux Veritatis – RadioMaryja.pl.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Sprzeciw wobec ataków na Fundację Lux Veritatis – RadioMaryja.pl.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Tageswoche.ch-weg.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Tageswoche.ch-weg.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Unijne fundusze coraz bliżej. Sejm zagłosował _za_ - Polityka - rp.pl.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Unijne fundusze coraz bliżej. Sejm zagłosował _za_ - Polityka - rp.pl.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Volksstimme.ch-loehne.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Volksstimme.ch-loehne.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Winda w chmurach _ Obyczaje _ Dwutygodnik _ Dwutygodnik.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Winda w chmurach _ Obyczaje _ Dwutygodnik _ Dwutygodnik.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Windows 10 od lipca przestanie obsługiwać Adobe Flash.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/Windows 10 od lipca przestanie obsługiwać Adobe Flash.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/_Ziemniaki na szóstej, surówka na dziesiątej_. Jak pomagać, żeby nie zaszkodzić_ [PORADNIK W PIGUŁCE].html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/_Ziemniaki na szóstej, surówka na dziesiątej_. Jak pomagać, żeby nie zaszkodzić_ [PORADNIK W PIGUŁCE].html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/abc13.com-Copperfield.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/abc13.com-Copperfield.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/abc7news.com-Napa.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/abc7news.com-Napa.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/abenteuer-astronomie.de.plejaden.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/abenteuer-astronomie.de.plejaden.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/abookshelffullofsunshine.blogspot.com.interview.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/abookshelffullofsunshine.blogspot.com.interview.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/achgut.com-coronalage.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/achgut.com-coronalage.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/achtundvierzig.hypotheses.org.822.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/achtundvierzig.hypotheses.org.822.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/aclu.org-grades.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/aclu.org-grades.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/acpjournals.org.3075.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/acpjournals.org.3075.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/ad-magazin.de.wellness.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/ad-magazin.de.wellness.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/advents-shopping.de.weihnachtsmaerkte.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/advents-shopping.de.weihnachtsmaerkte.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/aerobuzz.de-bremen.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/aerobuzz.de-bremen.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/agrarheute.com.abfallholz.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/agrarheute.com.abfallholz.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/ahlen.de.reparaturcafe.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/ahlen.de.reparaturcafe.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/aktion-hummelschutz.de.hummeln.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/aktion-hummelschutz.de.hummeln.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/alacarte.at-purzelbaum.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/alacarte.at-purzelbaum.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/alexander-klier.net.zeitphilosophie.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/alexander-klier.net.zeitphilosophie.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/alexanderlasch.wordpress.com.sprachgeschichte.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/alexanderlasch.wordpress.com.sprachgeschichte.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/alpin.de-freeride.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/alpin.de-freeride.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/amazedmag.de.meinleben.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/amazedmag.de.meinleben.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/ambito.com-paritarias.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/ambito.com-paritarias.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/amnesty.de-waffensysteme.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/amnesty.de-waffensysteme.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/anarc.at.cdpath.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/anarc.at.cdpath.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/anchor.ch.lanka.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/anchor.ch.lanka.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/andreabottlinger.wordpress.com.arent.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/andreabottlinger.wordpress.com.arent.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/angelmagazin.de-schmerzen.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/angelmagazin.de-schmerzen.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/anglerboard.de-rute.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/anglerboard.de-rute.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/antary.de.wireshark.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/antary.de.wireshark.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/anwaltniemeyer.de.index.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/anwaltniemeyer.de.index.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/aoc.media.archaisme.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/aoc.media.archaisme.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/apolut.net-Sonja-Silberhorn.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/apolut.net-Sonja-Silberhorn.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/arbeit-und-arbeitsrecht.de.urlaub.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/arbeit-und-arbeitsrecht.de.urlaub.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/arbeitsagentur.de-arbeitsmarkt.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/arbeitsagentur.de-arbeitsmarkt.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archiv.krimiblog.de.2895.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archiv.krimiblog.de.2895.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.modabot.de.serkan.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.modabot.de.serkan.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.ordnungsrausch.com.orga-life.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.ordnungsrausch.com.orga-life.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.org-travaillent.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.org-travaillent.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.org.bewegliche-lettern.de.typography.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.org.bewegliche-lettern.de.typography.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.org.dimido.de.marketing.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.org.dimido.de.marketing.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.org.dzs-clan.de.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.org.dzs-clan.de.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.org.he.xinhuanet.com.25340717.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.org.he.xinhuanet.com.25340717.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.org.juergenheitmann.com.aggression.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.org.juergenheitmann.com.aggression.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.org.medialepfade.de.medienpaedagogin.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.org.medialepfade.de.medienpaedagogin.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.org.muffinrezept.net.grundrezept.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.org.muffinrezept.net.grundrezept.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.org.nesselsetzer.wordpress.com.antipoden.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.org.nesselsetzer.wordpress.com.antipoden.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.org.przepisy.pl.pierogi.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.org.przepisy.pl.pierogi.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.org.rent-a-pastor.com.hochzeitslokation.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.org.rent-a-pastor.com.hochzeitslokation.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.org.steinzeitwissen.de.werkzeuge.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.org.steinzeitwissen.de.werkzeuge.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.org.stol.it.berlusconi.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.org.stol.it.berlusconi.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.org.swap-stop.org.shuji.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.org.swap-stop.org.shuji.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.org.the-pain.net.silkroad.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.org.the-pain.net.silkroad.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.org.time4talks.com.kinos.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.org.time4talks.com.kinos.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.org.tv-orange.de.future.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.org.tv-orange.de.future.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.org.welpenkaufen24.de.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.org.welpenkaufen24.de.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.peptalks.de.schulnoten.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/archive.peptalks.de.schulnoten.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/arsnova.thm.de.frag.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/arsnova.thm.de.frag.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/arteradio.com-nuls.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/arteradio.com-nuls.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/assabah.com.tn.article.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/assabah.com.tn.article.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/aussengedanken.de.feuerholz.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/aussengedanken.de.feuerholz.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/auswaertiges-amt.de-Italien.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/auswaertiges-amt.de-Italien.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/auto-motor.at-hyundaitest.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/auto-motor.at-hyundaitest.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/auto-presse.de-minisuv.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/auto-presse.de-minisuv.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/auto-wirtschaft.ch-camping.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/auto-wirtschaft.ch-camping.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/auto.oe24.at-golfchina.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/auto.oe24.at-golfchina.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/autohaus.de-skode.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/autohaus.de-skode.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/automobilwoche.de-VW-Betriebsversammlung.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/automobilwoche.de-VW-Betriebsversammlung.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/autonews.ch-Tesla.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/autonews.ch-Tesla.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/autosprint.ch-pistenstopp.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/autosprint.ch-pistenstopp.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/autozeitung.de-adblue.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/autozeitung.de-adblue.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/awo.org-Menschenrechte.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/awo.org-Menschenrechte.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/axios.com.future.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/axios.com.future.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/backen.de.maulwurfkuchen.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/backen.de.maulwurfkuchen.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/backenmachtgluecklich.de.zitronenkuchen.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/backenmachtgluecklich.de.zitronenkuchen.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/badische-zeitung.de-Wohnungssuche.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/badische-zeitung.de-Wohnungssuche.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/baechli-bergsport.ch-lawinen.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/baechli-bergsport.ch-lawinen.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bafa.de-mineraloelabsatz.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bafa.de-mineraloelabsatz.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bahamaslocal.com-atlantis.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bahamaslocal.com-atlantis.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/baike.baidu.com.tanya.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/baike.baidu.com.tanya.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/banyuetan.org.1000200033136171577956287380194268_1.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/banyuetan.org.1000200033136171577956287380194268_1.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/barbadostoday.bb-contest.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/barbadostoday.bb-contest.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/battery-news.de.ultium-cells.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/battery-news.de.ultium-cells.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bauemotion.de-schneereampflicht.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bauemotion.de-schneereampflicht.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/baumeister.de.sportzentrum.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/baumeister.de.sportzentrum.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/baumev.de.Transformationslabor.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/baumev.de.Transformationslabor.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bayrische-bembel.de.504.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bayrische-bembel.de.504.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bbc.com.52241221.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bbc.com.52241221.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bdzv.de.eliasson.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bdzv.de.eliasson.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/be.ch-impfen.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/be.ch-impfen.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/beige.de.suedfrankreich.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/beige.de.suedfrankreich.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bergsteigen.com-skibergsteigen.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bergsteigen.com-skibergsteigen.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/berkutschi.com-willingen.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/berkutschi.com-willingen.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/berliner-feuerwehr.de-Ehrenzeichen.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/berliner-feuerwehr.de-Ehrenzeichen.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bettycrocker.com.pineapple.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bettycrocker.com.pineapple.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bewusster-leben.de.hope.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bewusster-leben.de.hope.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/beyssonmanagement.com.innovation.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/beyssonmanagement.com.innovation.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bfn.de-verden.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bfn.de-verden.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bfs.de-radon.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bfs.de-radon.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/biathlon-antholz.it-jubeln.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/biathlon-antholz.it-jubeln.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/biathlonword.com-chinesisch.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/biathlonword.com-chinesisch.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bibliothek2null.de.mai.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bibliothek2null.de.mai.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bigdata.ypart.eu.datenerhebung.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bigdata.ypart.eu.datenerhebung.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bike-magazin.de-strava.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bike-magazin.de-strava.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/biobiochile.cl-gremios.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/biobiochile.cl-gremios.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bka.de-messengerdienste.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bka.de-messengerdienste.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/blinker.de-Rostock.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/blinker.de-Rostock.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/blog.amp.dev.axios.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/blog.amp.dev.axios.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/blog.gaijinpot.com.chikan.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/blog.gaijinpot.com.chikan.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/blog.mondediplo.net.turpitude.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/blog.mondediplo.net.turpitude.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/blog.teufel.de.leistung.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/blog.teufel.de.leistung.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bloghaus.hypotheses.org.2320.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bloghaus.hypotheses.org.2320.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/blogoff.de.i-htm.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/blogoff.de.i-htm.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bmas.de-anforderungen.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bmas.de-anforderungen.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bmbf.de.energiewende.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bmbf.de.energiewende.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bmel.de-zukunftsforum.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bmel.de-zukunftsforum.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bmfsfj.de-praesidentschaft.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bmfsfj.de-praesidentschaft.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bmwi.de-neubau.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bmwi.de-neubau.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bmz.de-schulze.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bmz.de-schulze.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bondyblog.fr.paris-8.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bondyblog.fr.paris-8.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bos-fahrzeuge.info-haubenfahrzeuge.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bos-fahrzeuge.info-haubenfahrzeuge.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bostonherald.com-Brothel-catering.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/bostonherald.com-Brothel-catering.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/boxen.de-staatsanwaltschaft.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/boxen.de-staatsanwaltschaft.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/eval/boxen1.com-ring-rückkehr.html` | Inspection reached its configured runtime limit\. |

### Analyzer Statuses

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| completed | `artifact_integrity` |  |
| degraded | `behavioral_ast` |  |
| degraded | `behavioral_taint_tracking` |  |
| no\_applicable\_files | `bundled_execution_surface` | No files matched this analyzer's applicability contract\. |
| manifest\_absent | `mcp_least_privilege` | No compatible manifest was present for this analyzer\. |
| manifest\_absent | `mcp_rug_pull` | No compatible manifest was present for this analyzer\. |
| manifest\_absent | `mcp_tool_poisoning` | No compatible manifest was present for this analyzer\. |
| disabled\_by\_configuration | `meta_analyzer` | Analyzer was disabled by the requested configuration\. |
| disabled\_by\_configuration | `semantic_developer_intent` | Analyzer was disabled by the requested configuration\. |
| disabled\_by\_configuration | `semantic_quality_policy` | Analyzer was disabled by the requested configuration\. |
| disabled\_by\_configuration | `semantic_security_discovery` | Analyzer was disabled by the requested configuration\. |
| degraded | `static_patterns_agent_snooping` |  |
| degraded | `static_patterns_anti_refusal` |  |
| degraded | `static_patterns_data_exfiltration` |  |
| degraded | `static_patterns_deserialization` |  |
| degraded | `static_patterns_excessive_agency` |  |
| degraded | `static_patterns_harmful_content` |  |
| degraded | `static_patterns_memory_poisoning` |  |
| degraded | `static_patterns_output_handling` |  |
| degraded | `static_patterns_privilege_escalation` |  |
| degraded | `static_patterns_prompt_injection` |  |
| degraded | `static_patterns_rogue_agent` |  |
| degraded | `static_patterns_ssrf` |  |
| degraded | `static_patterns_supply_chain` |  |
| degraded | `static_patterns_system_prompt_leakage` |  |
| degraded | `static_patterns_tool_misuse` |  |
| completed | `static_yara` |  |

### Limitations

- Analyzer behavioral\_ast status: degraded\.
- Analyzer behavioral\_taint\_tracking status: degraded\.
- Analyzer static\_patterns\_agent\_snooping status: degraded\.
- Analyzer static\_patterns\_anti\_refusal status: degraded\.
- Analyzer static\_patterns\_data\_exfiltration status: degraded\.
- Analyzer static\_patterns\_deserialization status: degraded\.
- Analyzer static\_patterns\_excessive\_agency status: degraded\.
- Analyzer static\_patterns\_harmful\_content status: degraded\.
- Analyzer static\_patterns\_memory\_poisoning status: degraded\.
- Analyzer static\_patterns\_output\_handling status: degraded\.
- Analyzer static\_patterns\_privilege\_escalation status: degraded\.
- Analyzer static\_patterns\_prompt\_injection status: degraded\.
- Analyzer static\_patterns\_rogue\_agent status: degraded\.
- Analyzer static\_patterns\_ssrf status: degraded\.
- Analyzer static\_patterns\_supply\_chain status: degraded\.
- Analyzer static\_patterns\_system\_prompt\_leakage status: degraded\.
- Analyzer static\_patterns\_tool\_misuse status: degraded\.

## Metadata

- **Executable Scripts:** No

*Generated by SkillSpector v2.12.0*
