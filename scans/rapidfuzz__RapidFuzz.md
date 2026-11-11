# SkillSpector Security Report

**Skill:** unknown  
**Source:** `F:\Github Repos\repos\rapidfuzz__RapidFuzz`  
**Scanned:** 2026-11-11 16:00:23 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 100/100 |
| Severity | CRITICAL |
| Recommendation | DO NOT INSTALL |

## Components (209)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `.clang-format` | other | 29 | No |
| `.codespell-ignore-lines` | other | 1 | No |
| `.coveragerc` | other | 8 | No |
| `.git/config` | other | 13 | No |
| `.gitattributes` | other | 4 | No |
| `.github/FUNDING.yml` | yaml | 2 | No |
| `.github/dependabot.yml` | yaml | 13 | No |
| `.github/workflows/branchbuild.yml` | yaml | 221 | No |
| `.github/workflows/coverage.yml` | yaml | 46 | No |
| `.github/workflows/docs.yml` | yaml | 52 | No |
| `.github/workflows/releasebuild.yml` | yaml | 191 | No |
| `.github/workflows/submodule.yml` | yaml | 33 | No |
| `.gitignore` | other | 32 | No |
| `.gitmodules` | other | 6 | No |
| `.pre-commit-config.yaml` | yaml | 142 | No |
| `CHANGELOG.rst` | other | 1332 | No |
| `CITATION.bib` | other | 10 | No |
| `CMakeLists.txt` | text | 145 | No |
| `CODE_OF_CONDUCT.md` | markdown | 132 | No |
| `LICENSE` | other | 21 | No |
| `README.md` | markdown | 247 | No |
| `SECURITY.md` | markdown | 19 | No |
| `api_differences.md` | markdown | 66 | No |
| `bench/__init__.py` | python | 0 | Yes |
| `bench/benchmark.py` | python | 295 | Yes |
| `bench/benchmark_cdist.py` | python | 154 | Yes |
| `bench/benchmark_cpdist.py` | python | 135 | Yes |
| `bench/benchmark_fuzz.py` | python | 117 | Yes |
| `bench/benchmark_partial_ratio_long_needle.py` | python | 57 | Yes |
| `bench/benchmark_partial_ratio_short_needle.py` | python | 57 | Yes |
| `bench/benchmark_scorer.py` | python | 124 | Yes |
| `bench/benchmark_visualize.py` | python | 23 | Yes |
| `bench/common.py` | python | 29 | Yes |
| `bench/requirements.txt` | text | 10 | No |
| `cmake/CheckCPUArch.c.in` | other | 7 | No |
| `cmake/CheckCPUArch.cmake` | other | 45 | No |
| `docs/Contributing/index.rst` | other | 52 | No |
| `docs/Installation.rst` | other | 50 | No |
| `docs/License.rst` | other | 11 | No |
| `docs/References.rst` | other | 4 | No |
| `docs/Usage/distance/DamerauLevenshtein.rst` | other | 31 | No |
| `docs/Usage/distance/Hamming.rst` | other | 21 | No |
| `docs/Usage/distance/Indel.rst` | other | 77 | No |
| `docs/Usage/distance/Jaro.rst` | other | 30 | No |
| `docs/Usage/distance/JaroWinkler.rst` | other | 30 | No |
| `docs/Usage/distance/LCSseq.rst` | other | 29 | No |
| `docs/Usage/distance/Levenshtein.rst` | other | 114 | No |
| `docs/Usage/distance/OSA.rst` | other | 31 | No |
| `docs/Usage/distance/Postfix.rst` | other | 21 | No |
| `docs/Usage/distance/Prefix.rst` | other | 21 | No |
| `docs/Usage/distance/img/damerau_levenshtein.svg` | other | 1461 | Yes |
| `docs/Usage/distance/img/indel_levenshtein.svg` | other | 1597 | Yes |
| `docs/Usage/distance/img/jaro.svg` | other | 1341 | Yes |
| `docs/Usage/distance/img/jaro_winkler.svg` | other | 1378 | Yes |
| `docs/Usage/distance/img/osa.svg` | other | 1455 | Yes |
| `docs/Usage/distance/img/uniform_levenshtein.svg` | other | 1 | Yes |
| `docs/Usage/distance/index.rst` | other | 36 | No |
| `docs/Usage/fuzz.rst` | other | 46 | No |
| `docs/Usage/img/WRatio.svg` | other | 1 | Yes |
| `docs/Usage/img/indel_levenshtein.svg` | other | 1597 | Yes |
| `docs/Usage/img/partial_ratio_long_needle.svg` | other | 1617 | Yes |
| `docs/Usage/img/partial_ratio_short_needle.svg` | other | 1599 | Yes |
| `docs/Usage/img/partial_token_ratio.svg` | other | 1 | Yes |
| `docs/Usage/img/partial_token_set_ratio.svg` | other | 1 | Yes |
| `docs/Usage/img/partial_token_sort_ratio.svg` | other | 1 | Yes |
| `docs/Usage/img/ratio.svg` | other | 1 | Yes |
| `docs/Usage/img/token_ratio.svg` | other | 1 | Yes |
| `docs/Usage/img/token_set_ratio.svg` | other | 1 | Yes |
| `docs/Usage/img/token_sort_ratio.svg` | other | 1 | Yes |
| `docs/Usage/img/uniform_levenshtein.svg` | other | 1 | Yes |
| `docs/Usage/index.rst` | other | 10 | No |
| `docs/Usage/process.rst` | other | 22 | No |
| `docs/Usage/utils.rst` | other | 6 | No |
| `docs/changelog_link.rst` | other | 2 | No |
| `docs/conf.py` | python | 65 | Yes |
| `docs/img/RapidFuzz.svg` | other | 195 | Yes |
| `docs/img/cdist.svg` | other | 1941 | Yes |
| `docs/img/scorer.svg` | other | 1902 | Yes |
| `docs/index.rst` | other | 47 | No |
| `docs/refs.bib` | other | 45 | No |
| `docs/requirements.txt` | text | 5 | No |
| `pyproject.toml` | toml | 193 | No |
| `src/rapidfuzz/CMakeLists.txt` | text | 202 | No |
| `src/rapidfuzz/FeatureDetector/CpuInfo.cpp` | other | 78 | No |
| `src/rapidfuzz/FeatureDetector/CpuInfo.hpp` | other | 32 | No |
| `src/rapidfuzz/__init__.pxd` | other | 89 | No |
| `src/rapidfuzz/__init__.py` | python | 33 | Yes |
| `src/rapidfuzz/__init__.pyi` | other | 14 | No |
| `src/rapidfuzz/__pyinstaller/__init__.py` | python | 7 | Yes |
| `src/rapidfuzz/__pyinstaller/test_rapidfuzz_packaging.py` | python | 38 | Yes |
| `src/rapidfuzz/_common_py.py` | python | 73 | Yes |
| `src/rapidfuzz/_feature_detector.py` | python | 15 | Yes |
| `src/rapidfuzz/_feature_detector_cpp.pyx` | other | 17 | No |
| `src/rapidfuzz/_utils.py` | python | 85 | Yes |
| `src/rapidfuzz/cpp_common.hpp` | other | 692 | No |
| `src/rapidfuzz/cpp_common.pxd` | other | 458 | No |
| `src/rapidfuzz/distance/CMakeLists.txt` | text | 106 | No |
| `src/rapidfuzz/distance/DamerauLevenshtein.py` | python | 93 | Yes |
| `src/rapidfuzz/distance/DamerauLevenshtein.pyi` | other | 75 | No |
| `src/rapidfuzz/distance/DamerauLevenshtein_py.py` | python | 233 | Yes |
| `src/rapidfuzz/distance/Hamming.py` | python | 116 | Yes |
| `src/rapidfuzz/distance/Hamming.pyi` | other | 113 | No |
| `src/rapidfuzz/distance/Hamming_py.py` | python | 322 | Yes |
| `src/rapidfuzz/distance/Indel.py` | python | 116 | Yes |
| `src/rapidfuzz/distance/Indel.pyi` | other | 105 | No |
| `src/rapidfuzz/distance/Indel_py.py` | python | 358 | Yes |
| `src/rapidfuzz/distance/Jaro.py` | python | 93 | Yes |
| `src/rapidfuzz/distance/Jaro.pyi` | other | 75 | No |
| `src/rapidfuzz/distance/JaroWinkler.py` | python | 93 | Yes |
| `src/rapidfuzz/distance/JaroWinkler.pyi` | other | 83 | No |
| `src/rapidfuzz/distance/JaroWinkler_py.py` | python | 235 | Yes |
| `src/rapidfuzz/distance/Jaro_py.py` | python | 256 | Yes |
| `src/rapidfuzz/distance/LCSseq.py` | python | 116 | Yes |
| `src/rapidfuzz/distance/LCSseq.pyi` | other | 105 | No |
| `src/rapidfuzz/distance/LCSseq_py.py` | python | 426 | Yes |
| `src/rapidfuzz/distance/Levenshtein.py` | python | 116 | Yes |
| `src/rapidfuzz/distance/Levenshtein.pyi` | other | 131 | No |
| `src/rapidfuzz/distance/Levenshtein_py.py` | python | 571 | Yes |
| `src/rapidfuzz/distance/OSA.py` | python | 93 | Yes |
| `src/rapidfuzz/distance/OSA.pyi` | other | 75 | No |
| `src/rapidfuzz/distance/OSA_py.py` | python | 232 | Yes |
| `src/rapidfuzz/distance/Postfix.py` | python | 93 | Yes |
| `src/rapidfuzz/distance/Postfix.pyi` | other | 75 | No |
| `src/rapidfuzz/distance/Postfix_py.py` | python | 182 | Yes |
| `src/rapidfuzz/distance/Prefix.py` | python | 93 | Yes |
| `src/rapidfuzz/distance/Prefix.pyi` | other | 75 | No |
| `src/rapidfuzz/distance/Prefix_py.py` | python | 182 | Yes |
| `src/rapidfuzz/distance/__init__.py` | python | 37 | Yes |
| `src/rapidfuzz/distance/__init__.pyi` | other | 25 | No |
| `src/rapidfuzz/distance/_initialize.py` | python | 109 | Yes |
| `src/rapidfuzz/distance/_initialize.pyi` | other | 133 | No |
| `src/rapidfuzz/distance/_initialize_cpp.pxd` | other | 17 | No |
| `src/rapidfuzz/distance/_initialize_cpp.pyx` | other | 892 | No |
| `src/rapidfuzz/distance/_initialize_py.py` | python | 892 | Yes |
| `src/rapidfuzz/distance/metrics.hpp` | other | 1231 | No |
| `src/rapidfuzz/distance/metrics_cpp.pyx` | other | 1191 | No |
| `src/rapidfuzz/distance/metrics_cpp_avx2.pyx` | other | 4 | No |
| `src/rapidfuzz/distance/metrics_cpp_sse2.pyx` | other | 4 | No |
| `src/rapidfuzz/distance/metrics_py.py` | python | 299 | Yes |
| `src/rapidfuzz/fuzz.py` | python | 161 | Yes |
| `src/rapidfuzz/fuzz.pyi` | other | 189 | No |
| `src/rapidfuzz/fuzz_cpp.hpp` | other | 255 | No |
| `src/rapidfuzz/fuzz_cpp.pyx` | other | 264 | No |
| `src/rapidfuzz/fuzz_cpp_avx2.pyx` | other | 4 | No |
| `src/rapidfuzz/fuzz_cpp_sse2.pyx` | other | 4 | No |
| `src/rapidfuzz/fuzz_py.py` | python | 889 | Yes |
| `src/rapidfuzz/process.py` | python | 95 | Yes |
| `src/rapidfuzz/process.pyi` | other | 518 | No |
| `src/rapidfuzz/process_cpp.hpp` | other | 718 | No |
| `src/rapidfuzz/process_cpp.py` | python | 125 | Yes |
| `src/rapidfuzz/process_cpp_impl.pyx` | other | 2074 | No |
| `src/rapidfuzz/process_py.py` | python | 683 | Yes |
| `src/rapidfuzz/py.typed` | other | 0 | No |
| `src/rapidfuzz/rapidfuzz.h` | other | 239 | No |
| `src/rapidfuzz/unicodetype_db.h` | other | 4630 | No |
| `src/rapidfuzz/utils.cpp` | other | 74 | No |
| `src/rapidfuzz/utils.hpp` | other | 89 | No |
| `src/rapidfuzz/utils.py` | python | 65 | Yes |
| `src/rapidfuzz/utils.pyi` | other | 11 | No |
| `src/rapidfuzz/utils_cpp.hpp` | other | 61 | No |
| `src/rapidfuzz/utils_cpp.pyx` | other | 41 | No |
| `src/rapidfuzz/utils_py.py` | python | 32 | Yes |
| `tests/__init__.py` | python | 0 | Yes |
| `tests/common.py` | python | 394 | Yes |
| `tests/distance/__init__.py` | python | 0 | Yes |
| `tests/distance/common.py` | python | 154 | Yes |
| `tests/distance/test_DamerauLevenshtein.py` | python | 35 | Yes |
| `tests/distance/test_Hamming.py` | python | 95 | Yes |
| `tests/distance/test_Indel.py` | python | 61 | Yes |
| `tests/distance/test_Jaro.py` | python | 64 | Yes |
| `tests/distance/test_JaroWinkler.py` | python | 67 | Yes |
| `tests/distance/test_LCSseq.py` | python | 63 | Yes |
| `tests/distance/test_Levenshtein.py` | python | 139 | Yes |
| `tests/distance/test_OSA.py` | python | 81 | Yes |
| `tests/distance/test_Postfix.py` | python | 27 | Yes |
| `tests/distance/test_Prefix.py` | python | 27 | Yes |
| `tests/distance/test_distance.py` | python | 149 | Yes |
| `tests/distance/test_init.py` | python | 453 | Yes |
| `tests/distance/test_levenshtein_zero_deletion.py` | python | 56 | Yes |
| `tests/freezeTools/script.py` | python | 8 | Yes |
| `tests/test_cpp_fallback.py` | python | 7 | Yes |
| `tests/test_fuzz.py` | python | 419 | Yes |
| `tests/test_hypothesis.py` | python | 468 | Yes |
| `tests/test_process.py` | python | 839 | Yes |
| `tests/test_pure_python_fallback.py` | python | 7 | Yes |
| `tests/test_utils.py` | python | 28 | Yes |
| `tools/backtrace` | other | 2 | No |
| `tools/generate_cython.sh` | shell | 27 | Yes |
| `tools/generate_python.py` | python | 261 | Yes |
| `tools/pyrightconfig.json` | json | 11 | No |
| `tools/sdist.patch` | other | 13 | No |
| `tools/seg_wrapper.sh` | shell | 8 | Yes |
| `tools/test_process_typing.py` | python | 196 | Yes |
| `tools/test_scorer_typing.py` | python | 113 | Yes |
| `tools/test_submodules.py` | python | 42 | Yes |
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

## Issues (1211)

### 🔴 HIGH: TM2

**Location:** `.github/workflows/branchbuild.yml:172`  
**Confidence:** 75%  

**Message:** Chaining Abuse

**Remediation:** Limit tool chaining depth and validate the output of each tool before passing it to the next\. Require explicit user approval for multi\-step chains\.

---

### 🔴 HIGH: TM2

**Location:** `.github/workflows/branchbuild.yml:173`  
**Confidence:** 75%  

**Message:** Chaining Abuse

**Remediation:** Limit tool chaining depth and validate the output of each tool before passing it to the next\. Require explicit user approval for multi\-step chains\.

---

### 🟡 MEDIUM: PE2

**Location:** `.github/workflows/branchbuild.yml:67`  
**Confidence:** 70%  

**Message:** Sudo/Root Execution

**Remediation:** Avoid sudo/root unless strictly required\. Prefer least\-privilege patterns\. If elevation is needed, document the justification and scope\.

---

### 🟡 MEDIUM: PE2

**Location:** `.github/workflows/branchbuild.yml:77`  
**Confidence:** 70%  

**Message:** Sudo/Root Execution

**Remediation:** Avoid sudo/root unless strictly required\. Prefer least\-privilege patterns\. If elevation is needed, document the justification and scope\.

---

### 🟡 MEDIUM: PE2

**Location:** `.github/workflows/branchbuild.yml:111`  
**Confidence:** 70%  

**Message:** Sudo/Root Execution

**Remediation:** Avoid sudo/root unless strictly required\. Prefer least\-privilege patterns\. If elevation is needed, document the justification and scope\.

---

### 🟡 MEDIUM: PE2

**Location:** `.github/workflows/branchbuild.yml:121`  
**Confidence:** 70%  

**Message:** Sudo/Root Execution

**Remediation:** Avoid sudo/root unless strictly required\. Prefer least\-privilege patterns\. If elevation is needed, document the justification and scope\.

---

### 🟡 MEDIUM: PE2

**Location:** `.github/workflows/branchbuild.yml:173`  
**Confidence:** 70%  

**Message:** Sudo/Root Execution

**Remediation:** Avoid sudo/root unless strictly required\. Prefer least\-privilege patterns\. If elevation is needed, document the justification and scope\.

---

### 🟡 MEDIUM: PE2

**Location:** `.github/workflows/branchbuild.yml:173`  
**Confidence:** 70%  

**Message:** Sudo/Root Execution

**Remediation:** Avoid sudo/root unless strictly required\. Prefer least\-privilege patterns\. If elevation is needed, document the justification and scope\.

---

### 🟡 MEDIUM: AE4

**Location:** `bench/benchmark.py:1`  
**Confidence:** 80%  

**Message:** Suspicious Unicode normalization or mixed\-script content

**Remediation:** Review the flagged content for security risks\. Ensure no credentials, secrets, or sensitive data are exposed\.

---

### 🟡 MEDIUM: AST4

**Location:** `bench/benchmark.py:120–125`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AE4

**Location:** `bench/benchmark_visualize.py:1`  
**Confidence:** 80%  

**Message:** Suspicious Unicode normalization or mixed\-script content

**Remediation:** Review the flagged content for security risks\. Ensure no credentials, secrets, or sensitive data are exposed\.

---

### 🟡 MEDIUM: AE4

**Location:** `docs/Usage/distance/img/damerau_levenshtein.svg:1`  
**Confidence:** 80%  

**Message:** Suspicious Unicode normalization or mixed\-script content

**Remediation:** Review the flagged content for security risks\. Ensure no credentials, secrets, or sensitive data are exposed\.

---

### 🟡 MEDIUM: AE4

**Location:** `docs/Usage/distance/img/jaro.svg:1`  
**Confidence:** 80%  

**Message:** Suspicious Unicode normalization or mixed\-script content

**Remediation:** Review the flagged content for security risks\. Ensure no credentials, secrets, or sensitive data are exposed\.

---

### 🟡 MEDIUM: AE4

**Location:** `docs/Usage/distance/img/jaro_winkler.svg:1`  
**Confidence:** 80%  

**Message:** Suspicious Unicode normalization or mixed\-script content

**Remediation:** Review the flagged content for security risks\. Ensure no credentials, secrets, or sensitive data are exposed\.

---

### 🟡 MEDIUM: AE4

**Location:** `docs/Usage/distance/img/osa.svg:1`  
**Confidence:** 80%  

**Message:** Suspicious Unicode normalization or mixed\-script content

**Remediation:** Review the flagged content for security risks\. Ensure no credentials, secrets, or sensitive data are exposed\.

---

### 🟡 MEDIUM: AE4

**Location:** `docs/Usage/img/partial_ratio_long_needle.svg:1`  
**Confidence:** 80%  

**Message:** Suspicious Unicode normalization or mixed\-script content

**Remediation:** Review the flagged content for security risks\. Ensure no credentials, secrets, or sensitive data are exposed\.

---

### 🟡 MEDIUM: AE4

**Location:** `docs/Usage/img/partial_ratio_short_needle.svg:1`  
**Confidence:** 80%  

**Message:** Suspicious Unicode normalization or mixed\-script content

**Remediation:** Review the flagged content for security risks\. Ensure no credentials, secrets, or sensitive data are exposed\.

---

### 🟡 MEDIUM: AST4

**Location:** `src/rapidfuzz/__pyinstaller/test_rapidfuzz_packaging.py:38`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: P9

**Location:** `src/rapidfuzz/cpp_common.hpp:103`  
**Confidence:** 70%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🟡 MEDIUM: P9

**Location:** `src/rapidfuzz/cpp_common.hpp:640`  
**Confidence:** 70%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🟡 MEDIUM: P9

**Location:** `src/rapidfuzz/cpp_common.hpp:643`  
**Confidence:** 70%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🟡 MEDIUM: P9

**Location:** `src/rapidfuzz/cpp_common.hpp:646`  
**Confidence:** 70%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🟡 MEDIUM: P9

**Location:** `src/rapidfuzz/cpp_common.hpp:104`  
**Confidence:** 70%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🟡 MEDIUM: P9

**Location:** `src/rapidfuzz/cpp_common.hpp:268`  
**Confidence:** 70%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🟡 MEDIUM: P9

**Location:** `src/rapidfuzz/utils_cpp.hpp:55`  
**Confidence:** 70%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🟡 MEDIUM: P9

**Location:** `src/rapidfuzz/distance/metrics.hpp:71`  
**Confidence:** 70%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🟡 MEDIUM: P9

**Location:** `src/rapidfuzz/distance/metrics.hpp:253`  
**Confidence:** 70%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🟡 MEDIUM: P9

**Location:** `src/rapidfuzz/distance/metrics.hpp:949`  
**Confidence:** 70%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🟡 MEDIUM: P9

**Location:** `src/rapidfuzz/fuzz_cpp.hpp:81`  
**Confidence:** 70%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🟡 MEDIUM: P9

**Location:** `src/rapidfuzz/distance/metrics.hpp:982`  
**Confidence:** 70%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:609`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:620`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:621`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:622`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:639`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:653`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:654`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:656`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:658`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:659`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:660`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:662`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:663`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:664`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:665`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:666`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:668`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:670`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:672`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:673`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:624`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:625`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:969`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:970`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:971`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:972`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:973`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:974`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:975`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:976`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:977`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:978`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:979`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:980`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:981`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:982`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:983`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:984`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:985`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:986`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:987`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:988`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:989`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:990`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:991`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:992`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:994`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:995`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:996`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:997`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:998`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:999`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1000`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1001`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1002`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1003`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1004`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1005`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1006`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1007`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1008`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1009`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1010`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1011`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1012`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1013`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1014`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1015`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1016`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:635`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:636`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:641`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:642`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:643`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:646`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:678`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:679`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:680`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:681`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:682`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:683`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:684`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:685`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:686`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:687`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:688`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:689`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:690`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:691`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:692`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:693`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:694`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:695`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:696`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:697`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:698`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:699`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:700`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:701`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:702`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:703`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:704`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:705`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:706`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:707`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:708`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:709`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:710`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:711`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:712`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:713`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:714`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:715`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:716`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:717`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:718`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:719`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:720`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:721`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:722`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:723`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:724`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:725`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:726`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:727`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:728`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:729`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:730`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:731`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:732`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:733`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:734`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:735`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:736`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:737`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:738`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:739`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:740`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:741`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:742`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:743`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:744`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:745`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:746`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:747`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:748`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:749`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:750`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:751`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:752`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:753`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:754`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:755`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:756`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:757`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:758`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:759`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:760`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:761`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:762`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:763`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:764`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:765`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:766`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:767`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:768`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:769`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:770`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:771`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:772`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:773`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:774`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:775`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:776`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:777`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:778`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:779`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:780`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:781`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:782`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:783`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:784`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:785`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:786`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:787`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:788`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:789`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:790`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:791`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:792`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:793`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:794`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:795`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:796`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:797`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:798`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:799`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:800`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:801`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:802`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:803`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:804`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:805`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:806`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:807`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:808`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:809`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:810`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:811`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:812`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:813`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:814`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:815`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:816`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:817`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:818`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:819`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:820`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:821`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:822`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:823`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:824`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:825`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:826`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:827`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:828`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:829`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:830`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:831`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:832`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:833`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:834`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:835`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:836`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:837`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:838`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:839`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:840`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:841`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:842`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:843`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:844`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:845`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:846`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:847`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:848`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:849`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:850`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:851`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:852`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:853`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:854`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:855`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:856`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:857`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:858`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:859`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:860`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:861`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:862`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:863`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:864`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:865`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:866`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:867`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:868`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:869`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:870`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:871`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:872`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:873`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:874`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:875`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:876`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:877`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:878`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:879`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:880`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:881`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:882`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:883`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:884`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:885`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:886`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:887`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:888`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:889`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:890`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:891`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:892`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:893`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:894`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:895`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:896`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:897`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:898`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:899`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:900`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:901`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:902`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:903`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:904`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:905`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:906`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:907`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:908`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:909`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:910`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:911`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:912`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:913`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:914`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:915`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:916`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:917`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:918`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:919`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:920`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:921`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:922`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:923`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:924`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:925`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:926`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:927`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:928`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:929`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:930`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:931`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:932`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:933`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:934`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:935`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:936`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:937`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:938`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:939`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:940`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:941`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:942`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:943`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:945`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:946`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:947`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:948`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:949`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:950`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:951`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:952`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:953`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:954`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:955`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:956`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:957`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:958`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:959`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:960`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:961`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:962`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:963`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:964`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:965`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:966`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:967`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: P9

**Location:** `src/rapidfuzz/unicodetype_db.h:678`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1058`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1059`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1061`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1089`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1090`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1360`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1361`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1477`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2399`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2400`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2402`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2679`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2680`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2681`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2682`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2683`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2684`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2685`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2686`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2687`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2688`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2689`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1071`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2126`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1085`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1454`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1455`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1087`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1457`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1092`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1096`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1100`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1101`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1102`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1103`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1110`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1111`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1112`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1113`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1116`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1131`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1132`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1156`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1181`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1192`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1193`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1208`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1217`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1229`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1230`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1231`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1232`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1233`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1234`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1235`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1236`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1239`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1245`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1246`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1248`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1249`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1259`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1260`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1261`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1262`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1263`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1264`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1265`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1266`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1267`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1268`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1269`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1271`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1273`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1274`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1275`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1284`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1291`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1293`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1296`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1298`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1299`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1308`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1310`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1316`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1326`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1327`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1332`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1335`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1338`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1469`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1500`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1501`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1502`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1505`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1506`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1507`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1509`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1511`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1512`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1513`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1514`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1534`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1535`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1536`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1537`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1538`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1540`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1541`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1542`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1543`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1544`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1545`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1546`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1548`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1549`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1550`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1551`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1552`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1553`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1555`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1556`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1557`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1558`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1559`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1564`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1565`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1566`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1568`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1569`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1571`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1573`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1575`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1577`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1578`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1579`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1580`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1582`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1583`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1584`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1587`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1588`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1589`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1592`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1593`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1594`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1595`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1596`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1598`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1599`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1600`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1601`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1602`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1603`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1605`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1606`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1607`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1608`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1609`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1610`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1612`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1613`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1614`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1615`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1616`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1617`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1619`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1620`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1621`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1622`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1623`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1626`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1627`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1628`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1629`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1630`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1631`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1632`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1633`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1634`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1635`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1637`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1638`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1639`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1641`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1642`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1643`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1644`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1645`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1647`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1648`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1650`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1651`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1652`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1653`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1654`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1656`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1657`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1658`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1659`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1660`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1661`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1662`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1664`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1665`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1666`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1667`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1668`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1670`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1671`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1672`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1673`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1674`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1676`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1677`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1678`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1679`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1681`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1683`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1684`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1686`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1687`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1688`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1689`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1690`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1692`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1693`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1694`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1695`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1696`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1699`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1700`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1701`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1702`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1703`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1708`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1718`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1719`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1738`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1741`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1747`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1751`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1753`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1759`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1765`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1780`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1783`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1787`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1796`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1797`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1798`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1799`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1801`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1802`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1804`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1806`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1808`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1809`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1810`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1811`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1813`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1814`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1815`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1816`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1823`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1824`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1825`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1826`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1830`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1831`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1832`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1833`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1834`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1835`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1837`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1838`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1839`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1842`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1843`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1845`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1846`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1856`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1857`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1858`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1859`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1860`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1861`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1868`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1870`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1875`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1881`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1882`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1883`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1884`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1885`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1905`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1907`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1911`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1915`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1917`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1919`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1927`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1928`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1929`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1936`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1938`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1939`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1942`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1943`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1948`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1949`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1954`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1966`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1967`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1978`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1985`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1997`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1998`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2009`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2021`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2027`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2029`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2040`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2046`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2049`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2055`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2058`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2072`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2082`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2083`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2088`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2094`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2095`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2100`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2101`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2106`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2107`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2119`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2139`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2147`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2148`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2152`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2153`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2168`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2172`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2204`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2205`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2210`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2216`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2217`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2218`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2222`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2223`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2225`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2232`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2234`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2235`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2259`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2260`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2271`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2272`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2273`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2274`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2275`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2277`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2278`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2279`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2289`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2295`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2296`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2297`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2298`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2299`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2301`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2302`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2303`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2304`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2305`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2417`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2426`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2427`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2429`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2430`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2431`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2460`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2570`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2571`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2572`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2574`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2575`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2576`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2577`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2578`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2580`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2581`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2583`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2584`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2585`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2586`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2589`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2590`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2591`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2592`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2593`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2594`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2595`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2596`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2597`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2601`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2602`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2603`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2604`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2605`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2607`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2608`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2609`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2610`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2611`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2612`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2614`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2615`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2616`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2617`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2618`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2620`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2621`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2622`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2623`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2624`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2625`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2626`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2627`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2628`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2630`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2631`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2632`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2633`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2637`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2640`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2641`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2642`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2644`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2645`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2646`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2647`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2648`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2649`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2651`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2652`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2653`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2654`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2655`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2656`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2657`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2658`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2661`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2667`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2668`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2669`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1124`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1125`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1215`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1323`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1324`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1483`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1732`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1818`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1848`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1879`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1895`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1899`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1900`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1901`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1902`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1903`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1922`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1956`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1957`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1963`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1964`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1980`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1993`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1994`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1995`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2000`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2001`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2012`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2013`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2014`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2015`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2016`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2017`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2018`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2023`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2024`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2025`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2031`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2032`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2033`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2034`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2067`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2068`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2092`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2110`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2111`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2116`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2117`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2121`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2122`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2123`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2124`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2135`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2136`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2164`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2165`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2175`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2176`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2177`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2178`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2179`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2180`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2181`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2182`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2185`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2186`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2193`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2194`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2195`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2196`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2207`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2208`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2213`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2214`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2220`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2228`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2229`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2230`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2241`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2242`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2243`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2244`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2245`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2246`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2247`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2248`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2254`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2255`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2256`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2257`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2266`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2267`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2268`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2281`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2284`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2285`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2286`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2287`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2291`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2309`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2310`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2311`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2312`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2335`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2336`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2337`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2338`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2339`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2340`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2341`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2407`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2408`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2409`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2413`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2414`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2415`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2421`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2422`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2423`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2424`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2434`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2440`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2441`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2442`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2443`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2444`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2445`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2450`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2451`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2452`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2457`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2458`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2469`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2493`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2501`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2535`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2536`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2537`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2562`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2567`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2635`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2663`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2664`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2665`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2671`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2673`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1204`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1312`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1406`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1407`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1408`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1409`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1410`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1411`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1412`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1413`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1414`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1415`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1416`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1417`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1418`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1430`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1431`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1432`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1433`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1434`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1437`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1438`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1439`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1440`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1441`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1442`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1443`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1444`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1445`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1446`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1449`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1450`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1451`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1452`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1479`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1481`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1486`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1487`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1488`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1491`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1492`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1493`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1497`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1518`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1521`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1523`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1528`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1530`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1531`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1532`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1561`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1562`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1705`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1706`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1897`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2314`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2315`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2316`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2317`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2320`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2322`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2323`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2326`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2328`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2329`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2332`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2333`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2344`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2345`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2346`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2472`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2474`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2475`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2476`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2477`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2482`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2485`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2491`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2495`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2497`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2503`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2504`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2505`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2506`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2507`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2509`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2510`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2511`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2515`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2516`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2517`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2518`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2521`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2522`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2523`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2528`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2532`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2539`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2540`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2541`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2542`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2543`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2545`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2546`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2547`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2549`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2550`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2551`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2552`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2553`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2565`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1224`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1226`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1227`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1345`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1351`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1773`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2351`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2356`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2361`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2366`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2371`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2376`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2381`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2389`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1353`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1354`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1358`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1426`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1466`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1722`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1789`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1790`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1791`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1792`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1793`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1794`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2692`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2693`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2694`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2695`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2696`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1887`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1888`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1970`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2447`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2448`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2454`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1890`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1891`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2198`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2199`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2200`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2201`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1924`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1932`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1925`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:1934`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2003`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2006`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2251`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2263`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2350`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2377`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2385`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2437`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2675`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2676`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `src/rapidfuzz/unicodetype_db.h:2677`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: AST4

**Location:** `tools/generate_python.py:89`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tools/generate_python.py:90`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tools/test_scorer_typing.py:67–78`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tools/test_scorer_typing.py:79–89`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟢 LOW: EA3

**Location:** `LICENSE:16`  
**Confidence:** 70%  

**Message:** Scope Creep

**Remediation:** Limit the skill's scope to its documented purpose\. Remove instructions that enable the agent to perform actions outside its stated functionality\.

---

### 🟢 LOW: AST7

**Location:** `bench/benchmark_cdist.py:48`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `bench/benchmark_cpdist.py:37`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `bench/benchmark_scorer.py:37`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: SC1

**Location:** `bench/requirements.txt:1`  
**Confidence:** 60%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements\.txt or pyproject\.toml\. Use exact versions \(==\) or compatible ranges\. Run pip\-audit regularly\.

---

### 🟢 LOW: SC1

**Location:** `bench/requirements.txt:2`  
**Confidence:** 60%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements\.txt or pyproject\.toml\. Use exact versions \(==\) or compatible ranges\. Run pip\-audit regularly\.

---

### 🟢 LOW: SC1

**Location:** `bench/requirements.txt:3`  
**Confidence:** 60%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements\.txt or pyproject\.toml\. Use exact versions \(==\) or compatible ranges\. Run pip\-audit regularly\.

---

### 🟢 LOW: SC1

**Location:** `bench/requirements.txt:4`  
**Confidence:** 60%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements\.txt or pyproject\.toml\. Use exact versions \(==\) or compatible ranges\. Run pip\-audit regularly\.

---

### 🟢 LOW: SC1

**Location:** `bench/requirements.txt:5`  
**Confidence:** 60%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements\.txt or pyproject\.toml\. Use exact versions \(==\) or compatible ranges\. Run pip\-audit regularly\.

---

### 🟢 LOW: SC1

**Location:** `docs/requirements.txt:3`  
**Confidence:** 60%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements\.txt or pyproject\.toml\. Use exact versions \(==\) or compatible ranges\. Run pip\-audit regularly\.

---

### 🟢 LOW: SC4

**Location:** `bench/requirements.txt:5`  
**Confidence:** 40%  

**Message:** Unverifiable Dependency: numpy has 16 known advisory\(ies\) \(CVE\-2014\-1859 \(Numpy arbitrary file write via symlink attack\); CVE\-2021\-41495 \(NumPy NULL Pointer Dereference\); CVE\-2021\-33430 \(NumPy Buffer Overflow \(Disputed\)\) \+13 more\), but the manifest does not pin a version, so it is unknown whether the installed release is affected

**Remediation:** Determine the dependency's exact resolved version from the environment or lockfile and compare it with the advisories in OSV \(osv\.dev\)\. If it is affected, use a verified fixed release or remove or replace the dependency when no fix is available\.

---

### 🟢 LOW: SC4

**Location:** `docs/requirements.txt:3`  
**Confidence:** 40%  

**Message:** Unverifiable Dependency: numpy has 16 known advisory\(ies\) \(CVE\-2014\-1859 \(Numpy arbitrary file write via symlink attack\); CVE\-2021\-41495 \(NumPy NULL Pointer Dereference\); CVE\-2021\-33430 \(NumPy Buffer Overflow \(Disputed\)\) \+13 more\), but the manifest does not pin a version, so it is unknown whether the installed release is affected

**Remediation:** Determine the dependency's exact resolved version from the environment or lockfile and compare it with the advisories in OSV \(osv\.dev\)\. If it is affected, use a verified fixed release or remove or replace the dependency when no fix is available\.

---

### 🟢 LOW: SC4

**Location:** `pyproject.toml:36`  
**Confidence:** 40%  

**Message:** Unverifiable Dependency: numpy has 16 known advisory\(ies\) \(CVE\-2014\-1859 \(Numpy arbitrary file write via symlink attack\); CVE\-2021\-41495 \(NumPy NULL Pointer Dereference\); CVE\-2021\-33430 \(NumPy Buffer Overflow \(Disputed\)\) \+13 more\), but the manifest does not pin a version, so it is unknown whether the installed release is affected

**Remediation:** Determine the dependency's exact resolved version from the environment or lockfile and compare it with the advisories in OSV \(osv\.dev\)\. If it is affected, use a verified fixed release or remove or replace the dependency when no fix is available\.

---

### 🟢 LOW: SC1

**Location:** `bench/requirements.txt:6`  
**Confidence:** 60%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements\.txt or pyproject\.toml\. Use exact versions \(==\) or compatible ranges\. Run pip\-audit regularly\.

---

### 🟢 LOW: SC4

**Location:** `bench/requirements.txt:6`  
**Confidence:** 40%  

**Message:** Unverifiable Dependency: pandas has 1 known advisory\(ies\) \(CVE\-2020\-13091 \(\*\* DISPUTED \*\* pandas through 1\.0\.3 can unserialize and execute commands from an\)\), but the manifest does not pin a version, so it is unknown whether the installed release is affected

**Remediation:** Determine the dependency's exact resolved version from the environment or lockfile and compare it with the advisories in OSV \(osv\.dev\)\. If it is affected, use a verified fixed release or remove or replace the dependency when no fix is available\.

---

### 🟢 LOW: SC1

**Location:** `bench/requirements.txt:7`  
**Confidence:** 60%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements\.txt or pyproject\.toml\. Use exact versions \(==\) or compatible ranges\. Run pip\-audit regularly\.

---

### 🟢 LOW: SC1

**Location:** `bench/requirements.txt:8`  
**Confidence:** 60%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements\.txt or pyproject\.toml\. Use exact versions \(==\) or compatible ranges\. Run pip\-audit regularly\.

---

### 🟢 LOW: SC1

**Location:** `bench/requirements.txt:9`  
**Confidence:** 60%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements\.txt or pyproject\.toml\. Use exact versions \(==\) or compatible ranges\. Run pip\-audit regularly\.

---

### 🟢 LOW: SC1

**Location:** `bench/requirements.txt:10`  
**Confidence:** 60%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements\.txt or pyproject\.toml\. Use exact versions \(==\) or compatible ranges\. Run pip\-audit regularly\.

---

### 🟢 LOW: SC4

**Location:** `bench/requirements.txt:10`  
**Confidence:** 40%  

**Message:** Unverifiable Dependency: tqdm has 4 known advisory\(ies\) \(CVE\-2024\-34062 \(tqdm CLI arguments injection attack\); CVE\-2016\-10075 \(TDQM Arbitrary Code Execution\); CVE\-2016\-10075 \(The tqdm\.\_version module in tqdm versions 4\.4\.1 and 4\.10 allows local users to e\) \+1 more\), but the manifest does not pin a version, so it is unknown whether the installed release is affected

**Remediation:** Determine the dependency's exact resolved version from the environment or lockfile and compare it with the advisories in OSV \(osv\.dev\)\. If it is affected, use a verified fixed release or remove or replace the dependency when no fix is available\.

---

### 🟢 LOW: SC1

**Location:** `docs/requirements.txt:2`  
**Confidence:** 60%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements\.txt or pyproject\.toml\. Use exact versions \(==\) or compatible ranges\. Run pip\-audit regularly\.

---

### 🟢 LOW: SC1

**Location:** `docs/requirements.txt:4`  
**Confidence:** 60%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements\.txt or pyproject\.toml\. Use exact versions \(==\) or compatible ranges\. Run pip\-audit regularly\.

---

### 🟢 LOW: SC1

**Location:** `docs/requirements.txt:5`  
**Confidence:** 60%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements\.txt or pyproject\.toml\. Use exact versions \(==\) or compatible ranges\. Run pip\-audit regularly\.

---

### 🟢 LOW: AST7

**Location:** `tests/distance/common.py:20`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `tests/distance/common.py:21`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `tests/distance/common.py:22`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `tests/distance/common.py:23`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `tests/distance/common.py:24`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `tests/distance/common.py:25`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `tests/distance/common.py:31`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `tests/distance/common.py:32`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `tests/distance/common.py:33`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `tests/distance/common.py:34`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `tests/distance/common.py:35`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `tests/distance/common.py:36`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `tests/test_fuzz.py:249`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `tests/test_process.py:812`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `tests/test_process.py:838`  
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
| Coverage | 99\.5% |
| Fully inspected | 194 |
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
| runtime\_limit | `pyproject.toml` | Inspection reached its configured runtime limit\. |

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
| degraded | `static_patterns_supply_chain` |  |
| completed | `static_patterns_system_prompt_leakage` |  |
| completed | `static_patterns_tool_misuse` |  |
| completed | `static_yara` |  |

### Limitations

- Analyzer static\_patterns\_supply\_chain status: degraded\.

## Metadata

- **Executable Scripts:** Yes

*Generated by SkillSpector v2.12.0*
