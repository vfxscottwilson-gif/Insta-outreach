# SkillSpector Security Report

**Skill:** unknown  
**Source:** `F:\Github Repos\repos\scrapinghub__extruct`  
**Scanned:** 2026-11-11 15:57:12 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 100/100 |
| Severity | CRITICAL |
| Recommendation | DO NOT INSTALL |

## Components (195)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `.coveragerc` | other | 4 | No |
| `.git-blame-ignore-revs` | other | 6 | No |
| `.git/config` | other | 13 | No |
| `.gitattributes` | other | 1 | No |
| `.github/dependabot.yml` | yaml | 10 | No |
| `.github/workflows/python-package.yml` | yaml | 59 | No |
| `.github/workflows/python-publish.yml` | yaml | 32 | No |
| `.gitignore` | other | 17 | No |
| `.isort.cfg` | other | 2 | No |
| `.pre-commit-config.yaml` | yaml | 18 | No |
| `AUTHORS` | other | 6 | No |
| `HISTORY.rst` | other | 240 | No |
| `LICENSE` | other | 27 | No |
| `README.rst` | other | 747 | No |
| `extruct/VERSION` | other | 1 | No |
| `extruct/__init__.py` | python | 7 | Yes |
| `extruct/__main__.py` | python | 4 | Yes |
| `extruct/_extruct.py` | python | 201 | Yes |
| `extruct/dublincore.py` | python | 160 | Yes |
| `extruct/jsonld.py` | python | 232 | Yes |
| `extruct/microformat.py` | python | 10 | Yes |
| `extruct/opengraph.py` | python | 44 | Yes |
| `extruct/rdfa.py` | python | 172 | Yes |
| `extruct/tool.py` | python | 81 | Yes |
| `extruct/uniform.py` | python | 118 | Yes |
| `extruct/utils.py` | python | 16 | Yes |
| `extruct/w3cmicrodata.py` | python | 257 | Yes |
| `extruct/xmldom.py` | python | 185 | Yes |
| `pyproject.toml` | toml | 23 | No |
| `pytest.ini` | other | 8 | No |
| `requirements-dev.txt` | text | 14 | No |
| `requirements.txt` | text | 11 | No |
| `setup.cfg` | other | 9 | No |
| `setup.py` | python | 71 | Yes |
| `tests/__init__.py` | python | 30 | Yes |
| `tests/samples/custom.invalid/AllocateAction.001.html` | other | 32 | No |
| `tests/samples/custom.invalid/AllocateAction.001.jsonld` | other | 19 | No |
| `tests/samples/custom.invalid/JSONLD_with_CDATA.html` | other | 32 | No |
| `tests/samples/custom.invalid/JSONLD_with_CDATA.jsonld` | other | 23 | No |
| `tests/samples/custom.invalid/JSONLD_with_JS_comment.html` | other | 24 | No |
| `tests/samples/custom.invalid/JSONLD_with_JS_comment.jsonld` | other | 12 | No |
| `tests/samples/custom.invalid/JSONLD_with_control_characters.html` | other | 17 | No |
| `tests/samples/custom.invalid/JSONLD_with_control_characters.jsonld` | other | 5 | No |
| `tests/samples/custom.invalid/JSONLD_with_control_characters_comment.html` | other | 15 | No |
| `tests/samples/custom.invalid/JSONLD_with_control_characters_comment.jsonld` | other | 5 | No |
| `tests/samples/custom.invalid/JSONLD_with_invalid_escapes.html` | other | 19 | No |
| `tests/samples/custom.invalid/JSONLD_with_invalid_escapes.jsonld` | other | 10 | No |
| `tests/samples/custom.invalid/JSONLD_with_trailing_brace.html` | other | 28 | No |
| `tests/samples/custom.invalid/JSONLD_with_trailing_brace.jsonld` | other | 19 | No |
| `tests/samples/custom.invalid/JSONLD_with_unescaped_quotes.html` | other | 27 | No |
| `tests/samples/custom.invalid/JSONLD_with_unescaped_quotes.jsonld` | other | 16 | No |
| `tests/samples/custom.invalid/JoinAction.001.html` | other | 28 | No |
| `tests/samples/custom.invalid/JoinAction.001.jsonld` | other | 9 | No |
| `tests/samples/misc/Portfolio_Niels_Lubberman.html` | other | 519 | No |
| `tests/samples/misc/Portfolio_Niels_Lubberman.json` | json | 106 | No |
| `tests/samples/misc/dublincore_test.html` | other | 21 | No |
| `tests/samples/misc/dublincore_test.json` | json | 22 | No |
| `tests/samples/misc/expanded_OG_support_test.html` | other | 40 | No |
| `tests/samples/misc/expanded_OG_support_test.json` | json | 100 | No |
| `tests/samples/misc/microformat_flat_test.json` | json | 78 | No |
| `tests/samples/misc/microformat_test.html` | other | 49 | No |
| `tests/samples/misc/microformat_test.json` | json | 87 | No |
| `tests/samples/misc/null_ld_mock.html` | other | 1 | No |
| `tests/samples/misc/null_ld_mock.jsonld` | other | 25 | No |
| `tests/samples/misc/opengraph_body_test.html` | other | 23 | No |
| `tests/samples/misc/opengraph_body_test.json` | json | 34 | No |
| `tests/samples/misc/opengraph_flat_test.json` | json | 18 | No |
| `tests/samples/misc/opengraph_head_and_body_test.html` | other | 17 | No |
| `tests/samples/misc/opengraph_head_and_body_test.json` | json | 26 | No |
| `tests/samples/misc/opengraph_ns_product_test.html` | other | 21773 | No |
| `tests/samples/misc/opengraph_ns_product_test.json` | json | 54 | No |
| `tests/samples/misc/opengraph_test.html` | other | 37 | No |
| `tests/samples/misc/opengraph_test.json` | json | 50 | No |
| `tests/samples/misc/product_microdata.html` | other | 28 | No |
| `tests/samples/schema.org.invalid/AllocateAction.001.html` | other | 31 | No |
| `tests/samples/schema.org.invalid/AllocateAction.001.jsonld` | other | 18 | No |
| `tests/samples/schema.org.invalid/JoinAction.001.html` | other | 27 | No |
| `tests/samples/schema.org.invalid/JoinAction.001.jsonld` | other | 8 | No |
| `tests/samples/schema.org/CreativeWork.001.html` | other | 79 | No |
| `tests/samples/schema.org/CreativeWork.001.json` | json | 26 | No |
| `tests/samples/schema.org/CreativeWork.001.jsonld` | other | 51 | No |
| `tests/samples/schema.org/CreativeWork_flat.001.json` | json | 100 | No |
| `tests/samples/schema.org/CreativeWork_flat_with_node_id.001.json` | json | 107 | No |
| `tests/samples/schema.org/Event.001.html` | other | 36 | No |
| `tests/samples/schema.org/Event.001.json` | json | 12 | No |
| `tests/samples/schema.org/Event.002.html` | other | 92 | No |
| `tests/samples/schema.org/Event.002.json` | json | 45 | No |
| `tests/samples/schema.org/Event.003.html` | other | 33 | No |
| `tests/samples/schema.org/Event.003.json` | json | 16 | No |
| `tests/samples/schema.org/Event.004.html` | other | 34 | No |
| `tests/samples/schema.org/Event.004.json` | json | 18 | No |
| `tests/samples/schema.org/Event.008.html` | other | 34 | No |
| `tests/samples/schema.org/Event.008.json` | json | 16 | No |
| `tests/samples/schema.org/LocalBusiness.002.html` | other | 41 | No |
| `tests/samples/schema.org/LocalBusiness.002.json` | json | 18 | No |
| `tests/samples/schema.org/LocalBusiness.003.html` | other | 49 | No |
| `tests/samples/schema.org/LocalBusiness.003.json` | json | 26 | No |
| `tests/samples/schema.org/MusicRecording.001.html` | other | 92 | No |
| `tests/samples/schema.org/MusicRecording.001.json` | json | 45 | No |
| `tests/samples/schema.org/SearchAction.001.html` | other | 8 | No |
| `tests/samples/schema.org/SearchAction.001.json` | json | 1 | No |
| `tests/samples/schema.org/product-ref.html` | other | 55 | No |
| `tests/samples/schema.org/product-ref.json` | json | 69 | No |
| `tests/samples/schema.org/product.html` | other | 38 | No |
| `tests/samples/schema.org/product.json` | json | 19 | No |
| `tests/samples/schema.org/product_custom_url.json` | json | 19 | No |
| `tests/samples/schema.org/product_custom_url_and_node_id.json` | json | 23 | No |
| `tests/samples/songkick/Elysian Fields Brooklyn Tickets, The Owl Music Parlor, 31 Oct 2015.html` | other | 722 | No |
| `tests/samples/songkick/Elysian Fields Brooklyn Tickets, The Owl Music Parlor, 31 Oct 2015.jsonld` | other | 34 | No |
| `tests/samples/songkick/Maxïmo Park Gigography, Tour History & Past Concerts.html` | other | 2703 | No |
| `tests/samples/songkick/Maxïmo Park Gigography, Tour History & Past Concerts.jsonld` | other | 3731 | No |
| `tests/samples/songkick/Years & Years Tickets, Tour Dates 2015 & Concerts.html` | other | 2457 | No |
| `tests/samples/songkick/Years & Years Tickets, Tour Dates 2015 & Concerts.jsonld` | other | 18 | No |
| `tests/samples/songkick/elysianfields.html` | other | 1267 | No |
| `tests/samples/songkick/elysianfields.json` | json | 287 | No |
| `tests/samples/songkick/elysianfields_1.html` | other | 1273 | No |
| `tests/samples/songkick/elysianfields_1.json` | json | 306 | No |
| `tests/samples/songkick/jsonld_empty_item_test.html` | other | 1417 | No |
| `tests/samples/songkick/jsonld_empty_item_test.jsonld` | other | 307 | No |
| `tests/samples/songkick/tovestyrke.html` | other | 754 | No |
| `tests/samples/songkick/tovestyrke.json` | json | 206 | No |
| `tests/samples/w3c/microdata.4.2.data.html` | other | 11 | No |
| `tests/samples/w3c/microdata.4.2.data.json` | json | 3 | No |
| `tests/samples/w3c/microdata.4.2.meter.html` | other | 17 | No |
| `tests/samples/w3c/microdata.4.2.meter.json` | json | 8 | No |
| `tests/samples/w3c/microdata.4.2.strings.html` | other | 13 | No |
| `tests/samples/w3c/microdata.4.2.strings.json` | json | 5 | No |
| `tests/samples/w3c/microdata.4.2.strings.unclean.html` | other | 23 | No |
| `tests/samples/w3c/microdata.4.2.strings.unclean.json` | json | 5 | No |
| `tests/samples/w3c/microdata.5.2.flat.json` | json | 19 | No |
| `tests/samples/w3c/microdata.5.2.html` | other | 42 | No |
| `tests/samples/w3c/microdata.5.2.json` | json | 16 | No |
| `tests/samples/w3c/microdata.5.2.withtext.json` | json | 19 | No |
| `tests/samples/w3c/microdata.5.3.html` | other | 36 | No |
| `tests/samples/w3c/microdata.5.3.json` | json | 7 | No |
| `tests/samples/w3c/microdata.5.5.html` | other | 22 | No |
| `tests/samples/w3c/microdata.5.5.json` | json | 8 | No |
| `tests/samples/w3c/microdata.7.1.flat.json` | json | 43 | No |
| `tests/samples/w3c/microdata.7.1.html` | other | 34 | No |
| `tests/samples/w3c/microdata.7.1.json` | json | 42 | No |
| `tests/samples/w3c/microdata.object.html` | other | 13 | No |
| `tests/samples/w3c/microdata.object.json` | json | 4 | No |
| `tests/samples/w3crdfa/w3c.rdf11primer.example014.expanded.json` | json | 45 | No |
| `tests/samples/w3crdfa/w3c.rdf11primer.example014.html` | other | 25 | No |
| `tests/samples/w3crdfa/w3c.rdfalite.example003.expanded.json` | json | 31 | No |
| `tests/samples/w3crdfa/w3c.rdfalite.example003.html` | other | 8 | No |
| `tests/samples/w3crdfa/w3c.rdfalite.example004.expanded.json` | json | 31 | No |
| `tests/samples/w3crdfa/w3c.rdfalite.example004.html` | other | 7 | No |
| `tests/samples/w3crdfa/w3c.rdfalite.example005.expanded.json` | json | 36 | No |
| `tests/samples/w3crdfa/w3c.rdfalite.example005.html` | other | 8 | No |
| `tests/samples/w3crdfa/w3c.rdfaprimer.example005.expanded.json` | json | 15 | No |
| `tests/samples/w3crdfa/w3c.rdfaprimer.example005.html` | other | 10 | No |
| `tests/samples/w3crdfa/w3c.rdfaprimer.example006.expanded.json` | json | 20 | No |
| `tests/samples/w3crdfa/w3c.rdfaprimer.example006.html` | other | 12 | No |
| `tests/samples/w3crdfa/w3c.rdfaprimer.example007.expanded.json` | json | 20 | No |
| `tests/samples/w3crdfa/w3c.rdfaprimer.example007.html` | other | 11 | No |
| `tests/samples/w3crdfa/w3c.rdfaprimer.example008.expanded.json` | json | 25 | No |
| `tests/samples/w3crdfa/w3c.rdfaprimer.example008.html` | other | 11 | No |
| `tests/samples/w3crdfa/w3c.rdfaprimer.example009.expanded.json` | json | 28 | No |
| `tests/samples/w3crdfa/w3c.rdfaprimer.example009.html` | other | 11 | No |
| `tests/samples/w3crdfa/w3c.rdfaprimer.example010.expanded.json` | json | 46 | No |
| `tests/samples/w3crdfa/w3c.rdfaprimer.example010.html` | other | 17 | No |
| `tests/samples/w3crdfa/w3c.rdfaprimer.example011.expanded.json` | json | 49 | No |
| `tests/samples/w3crdfa/w3c.rdfaprimer.example011.html` | other | 22 | No |
| `tests/samples/w3crdfa/w3c.rdfaprimer.example015.expanded.json` | json | 31 | No |
| `tests/samples/w3crdfa/w3c.rdfaprimer.example015.html` | other | 7 | No |
| `tests/samples/websites/microdata-with-description.html` | other | 3036 | No |
| `tests/samples/websites/microdata-with-description.json` | json | 44 | No |
| `tests/samples/wikipedia/xhtml+rdfa.expanded.json` | json | 45 | No |
| `tests/samples/wikipedia/xhtml+rdfa.html` | other | 47 | No |
| `tests/test_dublincore.py` | python | 21 | Yes |
| `tests/test_extruct.py` | python | 94 | Yes |
| `tests/test_extruct_uniform.py` | python | 71 | Yes |
| `tests/test_jsonld.py` | python | 351 | Yes |
| `tests/test_microdata.py` | python | 255 | Yes |
| `tests/test_microformat.py` | python | 21 | Yes |
| `tests/test_opengraph.py` | python | 44 | Yes |
| `tests/test_rdfa.py` | python | 134 | Yes |
| `tests/test_tool.py` | python | 194 | Yes |
| `tests/test_uniform.py` | python | 372 | Yes |
| `tox.ini` | other | 26 | No |
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

## Issues (137)

### 🔴 CRITICAL: P5

**Location:** `tests/samples/songkick/Maxïmo Park Gigography, Tour History & Past Concerts.html:1538`  
**Confidence:** 70%  

**Message:** Harmful Content Injection

**Remediation:** Remove all content that could lead to harmful outcomes\. Add safety guardrails and human oversight for any high\-risk operations\.

---

### 🔴 CRITICAL: P5

**Location:** `tests/samples/songkick/Maxïmo Park Gigography, Tour History & Past Concerts.html:1628`  
**Confidence:** 70%  

**Message:** Harmful Content Injection

**Remediation:** Remove all content that could lead to harmful outcomes\. Add safety guardrails and human oversight for any high\-risk operations\.

---

### 🔴 CRITICAL: P5

**Location:** `tests/samples/songkick/Maxïmo Park Gigography, Tour History & Past Concerts.jsonld:2433`  
**Confidence:** 70%  

**Message:** Harmful Content Injection

**Remediation:** Remove all content that could lead to harmful outcomes\. Add safety guardrails and human oversight for any high\-risk operations\.

---

### 🔴 CRITICAL: P5

**Location:** `tests/samples/songkick/Maxïmo Park Gigography, Tour History & Past Concerts.jsonld:2768`  
**Confidence:** 70%  

**Message:** Harmful Content Injection

**Remediation:** Remove all content that could lead to harmful outcomes\. Add safety guardrails and human oversight for any high\-risk operations\.

---

### 🔴 CRITICAL: P5

**Location:** `tests/samples/songkick/Maxïmo Park Gigography, Tour History & Past Concerts.html:1538`  
**Confidence:** 70%  

**Message:** Harmful Content Injection

**Remediation:** Remove all content that could lead to harmful outcomes\. Add safety guardrails and human oversight for any high\-risk operations\.

---

### 🔴 CRITICAL: P5

**Location:** `tests/samples/songkick/Maxïmo Park Gigography, Tour History & Past Concerts.html:1628`  
**Confidence:** 70%  

**Message:** Harmful Content Injection

**Remediation:** Remove all content that could lead to harmful outcomes\. Add safety guardrails and human oversight for any high\-risk operations\.

---

### 🔴 CRITICAL: P5

**Location:** `tests/samples/songkick/Maxïmo Park Gigography, Tour History & Past Concerts.jsonld:2434`  
**Confidence:** 70%  

**Message:** Harmful Content Injection

**Remediation:** Remove all content that could lead to harmful outcomes\. Add safety guardrails and human oversight for any high\-risk operations\.

---

### 🔴 CRITICAL: P5

**Location:** `tests/samples/songkick/Maxïmo Park Gigography, Tour History & Past Concerts.jsonld:2769`  
**Confidence:** 70%  

**Message:** Harmful Content Injection

**Remediation:** Remove all content that could lead to harmful outcomes\. Add safety guardrails and human oversight for any high\-risk operations\.

---

### 🔴 HIGH: P2

**Location:** `tests/samples/misc/Portfolio_Niels_Lubberman.html:49–51`  
**Confidence:** 70%  

**Message:** Hidden Instructions

**Remediation:** Audit all comments and invisible characters\. Remove any instructions that direct the agent to perform unauthorized actions\. Use plain, reviewable content\.

---

### 🔴 HIGH: P2

**Location:** `tests/samples/misc/Portfolio_Niels_Lubberman.html:49–51`  
**Confidence:** 70%  

**Message:** Hidden Instructions

**Remediation:** Audit all comments and invisible characters\. Remove any instructions that direct the agent to perform unauthorized actions\. Use plain, reviewable content\.

---

### 🔴 HIGH: P2

**Location:** `tests/samples/misc/Portfolio_Niels_Lubberman.html:59–61`  
**Confidence:** 70%  

**Message:** Hidden Instructions

**Remediation:** Audit all comments and invisible characters\. Remove any instructions that direct the agent to perform unauthorized actions\. Use plain, reviewable content\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:12`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:88`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:21284`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:256`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P2

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:400–441`  
**Confidence:** 70%  

**Message:** Hidden Instructions

**Remediation:** Audit all comments and invisible characters\. Remove any instructions that direct the agent to perform unauthorized actions\. Use plain, reviewable content\.

---

### 🔴 HIGH: P2

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:442–507`  
**Confidence:** 70%  

**Message:** Hidden Instructions

**Remediation:** Audit all comments and invisible characters\. Remove any instructions that direct the agent to perform unauthorized actions\. Use plain, reviewable content\.

---

### 🔴 HIGH: YR4

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:503`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:557`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:719`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:791`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:968`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:10489`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:21569`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:1486`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:2009`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:2653`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:3111`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:3686`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:4309`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:4912`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:5900`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:6425`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:7071`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:7531`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:8108`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:8733`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:9338`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:11007`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:11530`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:12174`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:12632`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:13207`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:13830`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:14433`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:15421`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:15946`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:16592`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:17052`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:17629`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:18254`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:18859`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:1662`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:2185`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:3287`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:3862`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:4485`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:5088`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:6076`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:6601`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:7707`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:8284`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:8909`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:9514`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:11183`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:11706`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:12808`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:13383`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:14006`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:14609`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:15597`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:16122`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:17228`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:17805`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:18430`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:19035`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: PE3

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:2648`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:3058`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:7066`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:7478`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:12169`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:12579`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:16587`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:16999`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:2648`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:3058`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:7066`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:7478`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:12169`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:12579`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:16587`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:16999`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:10029`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:10282`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:19578`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:19708`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:19856`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:20045`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:20229`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:20659`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:20497`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🔴 HIGH: P2

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:21751–21765`  
**Confidence:** 70%  

**Message:** Hidden Instructions

**Remediation:** Audit all comments and invisible characters\. Remove any instructions that direct the agent to perform unauthorized actions\. Use plain, reviewable content\.

---

### 🔴 HIGH: P2

**Location:** `tests/samples/websites/microdata-with-description.html:2404`  
**Confidence:** 70%  

**Message:** Hidden Instructions

**Remediation:** Audit all comments and invisible characters\. Remove any instructions that direct the agent to perform unauthorized actions\. Use plain, reviewable content\.

---

### 🟡 MEDIUM: E1

**Location:** `README.rst:174`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/samples/songkick/jsonld_empty_item_test.html:162`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: AE4

**Location:** `tests/samples/misc/Portfolio_Niels_Lubberman.html:1`  
**Confidence:** 80%  

**Message:** Suspicious Unicode normalization or mixed\-script content

**Remediation:** Review the flagged content for security risks\. Ensure no credentials, secrets, or sensitive data are exposed\.

---

### 🟡 MEDIUM: P9

**Location:** `tests/samples/misc/opengraph_ns_product_test.html:19995`  
**Confidence:** 80%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🟡 MEDIUM: P9

**Location:** `tests/samples/schema.org/LocalBusiness.003.json:15`  
**Confidence:** 70%  

**Message:** Whitespace Padding

**Remediation:** Remove the large whitespace padding \(blank\-line blocks or long space runs\) and review any content hidden below or to the right of it\. Keep skill files compact and reviewable so no instructions can be concealed off\-screen\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/samples/songkick/Elysian Fields Brooklyn Tickets, The Owl Music Parlor, 31 Oct 2015.html:695`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/samples/songkick/Maxïmo Park Gigography, Tour History & Past Concerts.html:2676`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/samples/songkick/Years & Years Tickets, Tour Dates 2015 & Concerts.html:2430`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/samples/songkick/elysianfields.html:1225`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/samples/songkick/elysianfields_1.html:1231`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/samples/songkick/jsonld_empty_item_test.html:1372`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/samples/w3crdfa/w3c.rdf11primer.example014.expanded.json:3`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/samples/w3crdfa/w3c.rdf11primer.example014.html:19`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/samples/w3crdfa/w3c.rdf11primer.example014.html:22`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟢 LOW: EA3

**Location:** `LICENSE:19`  
**Confidence:** 70%  

**Message:** Scope Creep

**Remediation:** Limit the skill's scope to its documented purpose\. Remove instructions that enable the agent to perform actions outside its stated functionality\.

---

### 🟢 LOW: EA3

**Location:** `LICENSE:23`  
**Confidence:** 70%  

**Message:** Scope Creep

**Remediation:** Limit the skill's scope to its documented purpose\. Remove instructions that enable the agent to perform actions outside its stated functionality\.

---

### 🟢 LOW: SC4

**Location:** `requirements-dev.txt:1`  
**Confidence:** 100%  

**Message:** 🟡 SC4: OSV\.dev unreachable, using static fallback \(15 packages\)\. Results may be incomplete\. Set SKILLSPECTOR\_OSV\_TIMEOUT to increase timeout or check network connectivity to api\.osv\.dev\.

**Remediation:** Retry the scan and verify dependency versions against current advisories before relying on the incomplete results\. If the lookup timed out or the network was unavailable, check connectivity to api\.osv\.dev or adjust SKILLSPECTOR\_OSV\_TIMEOUT before retrying\.

---

### 🟢 LOW: SC1

**Location:** `requirements-dev.txt:6`  
**Confidence:** 60%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements\.txt or pyproject\.toml\. Use exact versions \(==\) or compatible ranges\. Run pip\-audit regularly\.

---

### 🟢 LOW: SC1

**Location:** `requirements-dev.txt:7`  
**Confidence:** 60%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements\.txt or pyproject\.toml\. Use exact versions \(==\) or compatible ranges\. Run pip\-audit regularly\.

---

### 🟢 LOW: SC1

**Location:** `requirements-dev.txt:9`  
**Confidence:** 60%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements\.txt or pyproject\.toml\. Use exact versions \(==\) or compatible ranges\. Run pip\-audit regularly\.

---

### 🟢 LOW: SC1

**Location:** `requirements-dev.txt:10`  
**Confidence:** 60%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements\.txt or pyproject\.toml\. Use exact versions \(==\) or compatible ranges\. Run pip\-audit regularly\.

---

### 🟢 LOW: SC1

**Location:** `requirements-dev.txt:11`  
**Confidence:** 60%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements\.txt or pyproject\.toml\. Use exact versions \(==\) or compatible ranges\. Run pip\-audit regularly\.

---

### 🟢 LOW: SC1

**Location:** `requirements-dev.txt:12`  
**Confidence:** 60%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements\.txt or pyproject\.toml\. Use exact versions \(==\) or compatible ranges\. Run pip\-audit regularly\.

---

### 🟢 LOW: SC1

**Location:** `requirements-dev.txt:13`  
**Confidence:** 60%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements\.txt or pyproject\.toml\. Use exact versions \(==\) or compatible ranges\. Run pip\-audit regularly\.

---

### 🟢 LOW: SC1

**Location:** `requirements-dev.txt:14`  
**Confidence:** 60%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements\.txt or pyproject\.toml\. Use exact versions \(==\) or compatible ranges\. Run pip\-audit regularly\.

---

### 🟢 LOW: SC1

**Location:** `requirements.txt:3`  
**Confidence:** 60%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements\.txt or pyproject\.toml\. Use exact versions \(==\) or compatible ranges\. Run pip\-audit regularly\.

---

### 🟢 LOW: SC1

**Location:** `requirements.txt:4`  
**Confidence:** 60%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements\.txt or pyproject\.toml\. Use exact versions \(==\) or compatible ranges\. Run pip\-audit regularly\.

---

### 🟢 LOW: SC1

**Location:** `requirements.txt:5`  
**Confidence:** 60%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements\.txt or pyproject\.toml\. Use exact versions \(==\) or compatible ranges\. Run pip\-audit regularly\.

---

### 🟢 LOW: SC1

**Location:** `requirements.txt:6`  
**Confidence:** 50%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements\.txt or pyproject\.toml\. Use exact versions \(==\) or compatible ranges\. Run pip\-audit regularly\.

---

### 🟢 LOW: SC1

**Location:** `requirements.txt:7`  
**Confidence:** 60%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements\.txt or pyproject\.toml\. Use exact versions \(==\) or compatible ranges\. Run pip\-audit regularly\.

---

### 🟢 LOW: SC1

**Location:** `requirements.txt:8`  
**Confidence:** 50%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements\.txt or pyproject\.toml\. Use exact versions \(==\) or compatible ranges\. Run pip\-audit regularly\.

---

### 🟢 LOW: SC1

**Location:** `requirements.txt:9`  
**Confidence:** 60%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements\.txt or pyproject\.toml\. Use exact versions \(==\) or compatible ranges\. Run pip\-audit regularly\.

---

### 🟢 LOW: SC1

**Location:** `requirements.txt:10`  
**Confidence:** 60%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements\.txt or pyproject\.toml\. Use exact versions \(==\) or compatible ranges\. Run pip\-audit regularly\.

---

### 🟢 LOW: SC1

**Location:** `requirements.txt:11`  
**Confidence:** 60%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements\.txt or pyproject\.toml\. Use exact versions \(==\) or compatible ranges\. Run pip\-audit regularly\.

---

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | partial |
| Dependency contents | not\_requested |
| Coverage | 96\.7% |
| Fully inspected | 175 |
| Partially inspected | 6 |
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
| static\_parse\_limit | `extruct/dublincore.py` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| runtime\_limit | `requirements-dev.txt` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `requirements.txt` | Inspection reached its configured runtime limit\. |
| obfuscated\_instruction\_text | `tests/samples/misc/opengraph_ns_product_test.html` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |
| static\_parse\_limit | `tests/samples/misc/opengraph_ns_product_test.html` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| obfuscated\_instruction\_text | `tests/samples/songkick/jsonld_empty_item_test.html` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |
| static\_parse\_limit | `tests/samples/songkick/jsonld_empty_item_test.html` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| obfuscated\_instruction\_text | `tests/samples/websites/microdata-with-description.html` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |

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
