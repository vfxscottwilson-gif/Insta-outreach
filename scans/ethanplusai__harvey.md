# SkillSpector Security Report

**Skill:** unknown  
**Source:** `F:\Github Repos\repos\ethanplusai__harvey`  
**Scanned:** 2026-11-03 16:16:53 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 100/100 |
| Severity | CRITICAL |
| Recommendation | DO NOT INSTALL |

## Components (210)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `.dockerignore` | other | 14 | No |
| `.env.example` | other | 153 | No |
| `.git/config` | other | 13 | No |
| `.github/workflows/tests.yml` | yaml | 46 | No |
| `.gitignore` | other | 64 | No |
| `CHANGELOG.md` | markdown | 835 | No |
| `CLAUDE.md` | markdown | 355 | No |
| `CONTRIBUTING.md` | markdown | 60 | No |
| `Dockerfile` | other | 59 | No |
| `LICENSE` | other | 21 | No |
| `README.md` | markdown | 839 | No |
| `docker-compose.yml` | yaml | 33 | No |
| `docs/dashboard.gif` | other | 207111 | No |
| `docs/microsoft365.md` | markdown | 189 | No |
| `docs/precleared.md` | markdown | 141 | No |
| `docs/screenshots/conversations-dark.png` | other | 2903 | No |
| `docs/screenshots/conversations-light.png` | other | 2902 | No |
| `docs/screenshots/outbox-dark.png` | other | 3955 | No |
| `docs/screenshots/outbox-light.png` | other | 3919 | No |
| `docs/screenshots/today-dark.png` | other | 4228 | No |
| `docs/screenshots/today-light.png` | other | 4043 | No |
| `harvey.yaml` | yaml | 149 | No |
| `harvey/__init__.py` | python | 19 | Yes |
| `harvey/__main__.py` | python | 6 | Yes |
| `harvey/agents/__init__.py` | python | 0 | Yes |
| `harvey/agents/analyst.py` | python | 187 | Yes |
| `harvey/agents/handler.py` | python | 1336 | Yes |
| `harvey/agents/scout.py` | python | 2178 | Yes |
| `harvey/agents/sender.py` | python | 1133 | Yes |
| `harvey/agents/writer.py` | python | 625 | Yes |
| `harvey/brain.py` | python | 741 | Yes |
| `harvey/claude_runtime.py` | python | 273 | Yes |
| `harvey/cli.py` | python | 1182 | Yes |
| `harvey/codex.py` | python | 1561 | Yes |
| `harvey/collectors/__init__.py` | python | 9 | Yes |
| `harvey/collectors/ats.py` | python | 338 | Yes |
| `harvey/collectors/discover.py` | python | 2009 | Yes |
| `harvey/collectors/people.py` | python | 870 | Yes |
| `harvey/collectors/profile.py` | python | 1341 | Yes |
| `harvey/config.py` | python | 1072 | Yes |
| `harvey/dashboard.py` | python | 2692 | Yes |
| `harvey/dashboard_auth.py` | python | 382 | Yes |
| `harvey/deliverability.py` | python | 307 | Yes |
| `harvey/export.py` | python | 154 | Yes |
| `harvey/fit.py` | python | 119 | Yes |
| `harvey/gate.py` | python | 470 | Yes |
| `harvey/humanize.py` | python | 138 | Yes |
| `harvey/integrations/__init__.py` | python | 8 | Yes |
| `harvey/integrations/calendar.py` | python | 26 | Yes |
| `harvey/integrations/email_finder.py` | python | 822 | Yes |
| `harvey/integrations/gmail.py` | python | 634 | Yes |
| `harvey/integrations/instantly.py` | python | 302 | Yes |
| `harvey/integrations/linkedin.py` | python | 433 | Yes |
| `harvey/integrations/mail_provider.py` | python | 162 | Yes |
| `harvey/integrations/microsoft.py` | python | 536 | Yes |
| `harvey/integrations/precleared.py` | python | 745 | Yes |
| `harvey/integrations/quota.py` | python | 196 | Yes |
| `harvey/integrations/signature.py` | python | 197 | Yes |
| `harvey/integrations/smtp_mail.py` | python | 193 | Yes |
| `harvey/integrations/tech_detect.py` | python | 92 | Yes |
| `harvey/integrations/trulyinbox.py` | python | 294 | Yes |
| `harvey/main.py` | python | 574 | Yes |
| `harvey/models/__init__.py` | python | 16 | Yes |
| `harvey/models/campaign.py` | python | 42 | Yes |
| `harvey/models/company.py` | python | 41 | Yes |
| `harvey/models/conversation.py` | python | 56 | Yes |
| `harvey/models/prospect.py` | python | 72 | Yes |
| `harvey/paths.py` | python | 12 | Yes |
| `harvey/pidfile.py` | python | 172 | Yes |
| `harvey/pipeline.py` | python | 130 | Yes |
| `harvey/public_http.py` | python | 127 | Yes |
| `harvey/register.py` | python | 203 | Yes |
| `harvey/send_window.py` | python | 632 | Yes |
| `harvey/sending_mode.py` | python | 64 | Yes |
| `harvey/setup.py` | python | 875 | Yes |
| `harvey/signals.py` | python | 407 | Yes |
| `harvey/startups.py` | python | 106 | Yes |
| `harvey/state.py` | python | 2649 | Yes |
| `harvey/textio.py` | python | 48 | Yes |
| `harvey/trainer.py` | python | 949 | Yes |
| `harvey/untrusted.py` | python | 39 | Yes |
| `harvey/usage.py` | python | 27 | Yes |
| `harvey/web/app.css` | other | 1034 | No |
| `harvey/web/app.js` | javascript | 2701 | Yes |
| `harvey/web/auth.js` | javascript | 63 | Yes |
| `harvey/web/fonts/geist-mono.woff2` | other | 646 | No |
| `harvey/web/fonts/geist.woff2` | other | 823 | No |
| `harvey/web/fonts/newsreader.woff2` | other | 3649 | No |
| `harvey/web/index.html` | other | 566 | No |
| `prompts/handler.md` | markdown | 36 | No |
| `prompts/scout.md` | markdown | 36 | No |
| `prompts/system.md` | markdown | 21 | No |
| `prompts/writer.md` | markdown | 71 | No |
| `pyproject.toml` | toml | 57 | No |
| `requirements.txt` | text | 15 | No |
| `scripts/diagnose_overpass.py` | python | 244 | Yes |
| `skills/README.md` | markdown | 52 | No |
| `skills/account_navigation.md` | markdown | 108 | No |
| `skills/email_frameworks.md` | markdown | 301 | No |
| `skills/lead_qualification.md` | markdown | 82 | No |
| `skills/linkedin_outreach.md` | markdown | 141 | No |
| `skills/objection_handling.md` | markdown | 110 | No |
| `skills/offer_strategy.md` | markdown | 144 | No |
| `skills/prospecting_tactics.md` | markdown | 148 | No |
| `skills/sales_methodology.md` | markdown | 150 | No |
| `skills/selling_to_startups.md` | markdown | 100 | No |
| `skills/signal_playbook.md` | markdown | 131 | No |
| `tests/__init__.py` | python | 0 | Yes |
| `tests/conftest.py` | python | 52 | Yes |
| `tests/fake_anthropic.py` | python | 105 | Yes |
| `tests/fake_codex.py` | python | 343 | Yes |
| `tests/fixtures/pre_codex_harvey_0_2_1.sql` | other | 232 | No |
| `tests/test_accelerators_funding.py` | python | 671 | Yes |
| `tests/test_ats_hiring.py` | python | 612 | Yes |
| `tests/test_brain_no_tools.py` | python | 303 | Yes |
| `tests/test_brain_provider.py` | python | 753 | Yes |
| `tests/test_claude_cli_isolation.py` | python | 204 | Yes |
| `tests/test_codex.py` | python | 892 | Yes |
| `tests/test_codex_cli_surface.py` | python | 441 | Yes |
| `tests/test_codex_e2e.py` | python | 821 | Yes |
| `tests/test_codex_platform.py` | python | 195 | Yes |
| `tests/test_codex_soak.py` | python | 230 | Yes |
| `tests/test_collectors_profile.py` | python | 291 | Yes |
| `tests/test_company_inbox.py` | python | 302 | Yes |
| `tests/test_company_stop.py` | python | 240 | Yes |
| `tests/test_compliance_footer.py` | python | 918 | Yes |
| `tests/test_config.py` | python | 62 | Yes |
| `tests/test_config_extra.py` | python | 178 | Yes |
| `tests/test_dashboard_auth.py` | python | 874 | Yes |
| `tests/test_dashboard_companies.py` | python | 105 | Yes |
| `tests/test_dashboard_conversations.py` | python | 225 | Yes |
| `tests/test_dashboard_live_status.py` | python | 181 | Yes |
| `tests/test_dashboard_manual_send.py` | python | 376 | Yes |
| `tests/test_dashboard_opt_out.py` | python | 173 | Yes |
| `tests/test_dashboard_pipeline.py` | python | 71 | Yes |
| `tests/test_dashboard_signals.py` | python | 553 | Yes |
| `tests/test_dashboard_trend.py` | python | 56 | Yes |
| `tests/test_dashboard_trulyinbox.py` | python | 78 | Yes |
| `tests/test_dashboard_usage_date.py` | python | 37 | Yes |
| `tests/test_discover.py` | python | 1745 | Yes |
| `tests/test_do_not_contact.py` | python | 348 | Yes |
| `tests/test_docker_config.py` | python | 61 | Yes |
| `tests/test_email_evidence.py` | python | 224 | Yes |
| `tests/test_email_finder.py` | python | 256 | Yes |
| `tests/test_email_wiring.py` | python | 140 | Yes |
| `tests/test_export_suppression.py` | python | 128 | Yes |
| `tests/test_fit.py` | python | 95 | Yes |
| `tests/test_followup_spacing.py` | python | 140 | Yes |
| `tests/test_gmail.py` | python | 150 | Yes |
| `tests/test_gmail_history.py` | python | 392 | Yes |
| `tests/test_gmail_inbox.py` | python | 202 | Yes |
| `tests/test_gmail_send_outcomes.py` | python | 201 | Yes |
| `tests/test_hand_sent_guard.py` | python | 92 | Yes |
| `tests/test_humanize.py` | python | 144 | Yes |
| `tests/test_local_rank.py` | python | 585 | Yes |
| `tests/test_microsoft.py` | python | 644 | Yes |
| `tests/test_models.py` | python | 62 | Yes |
| `tests/test_models_extra.py` | python | 145 | Yes |
| `tests/test_outbox_claim.py` | python | 273 | Yes |
| `tests/test_outbox_native.py` | python | 542 | Yes |
| `tests/test_outbox_review.py` | python | 236 | Yes |
| `tests/test_outreach_fixes.py` | python | 23 | Yes |
| `tests/test_packaging.py` | python | 142 | Yes |
| `tests/test_people_finder.py` | python | 418 | Yes |
| `tests/test_pidfile.py` | python | 350 | Yes |
| `tests/test_pipeline.py` | python | 289 | Yes |
| `tests/test_precleared.py` | python | 842 | Yes |
| `tests/test_precleared_checkout.py` | python | 97 | Yes |
| `tests/test_precleared_hold.py` | python | 528 | Yes |
| `tests/test_precleared_pause.py` | python | 959 | Yes |
| `tests/test_prompt_injection.py` | python | 433 | Yes |
| `tests/test_prospecting_stall.py` | python | 324 | Yes |
| `tests/test_public_http.py` | python | 287 | Yes |
| `tests/test_register.py` | python | 147 | Yes |
| `tests/test_reply_history.py` | python | 142 | Yes |
| `tests/test_scout_decision_maker.py` | python | 429 | Yes |
| `tests/test_scout_profile_search_gate.py` | python | 48 | Yes |
| `tests/test_security_defaults.py` | python | 190 | Yes |
| `tests/test_send_window.py` | python | 986 | Yes |
| `tests/test_sending_held.py` | python | 199 | Yes |
| `tests/test_sending_mode.py` | python | 370 | Yes |
| `tests/test_setup_precleared.py` | python | 354 | Yes |
| `tests/test_signals_export.py` | python | 157 | Yes |
| `tests/test_signature.py` | python | 322 | Yes |
| `tests/test_smtp_header_injection.py` | python | 77 | Yes |
| `tests/test_state.py` | python | 115 | Yes |
| `tests/test_state_extra.py` | python | 309 | Yes |
| `tests/test_trainer_config.py` | python | 201 | Yes |
| `tests/test_trulyinbox.py` | python | 295 | Yes |
| `tests/test_usage.py` | python | 164 | Yes |
| `tests/test_warmup.py` | python | 225 | Yes |
| `tests/test_windows_support.py` | python | 239 | Yes |
| `tests/test_writer_email_rules.py` | python | 278 | Yes |
| `tests/test_writer_feedback.py` | python | 107 | Yes |
| `tests/test_writer_retry.py` | python | 199 | Yes |
| `tests/test_yc_startups.py` | python | 515 | Yes |
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

## Issues (223)

### 🔴 HIGH: PE3

**Location:** `.env.example:3`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `.env.example:3`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `.env.example:4`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `README.md:134`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `README.md:134`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `README.md:164`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `README.md:164`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `docker-compose.yml:15`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/cli.py:449`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/cli.py:602`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/cli.py:625`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/collectors/discover.py:965`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/config.py:848`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/dashboard.py:93`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/dashboard.py:119`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/dashboard.py:121`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/dashboard.py:122`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/dashboard.py:398`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/dashboard.py:427`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/dashboard.py:434`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/dashboard.py:476`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/integrations/gmail.py:6`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/integrations/gmail.py:560`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/integrations/microsoft.py:11`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/integrations/microsoft.py:448`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/integrations/precleared.py:711`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/main.py:492`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/setup.py:73`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/setup.py:369`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/setup.py:748`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/setup.py:751`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/setup.py:839`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/trainer.py:489`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/web/app.js:863`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/test_config_extra.py:163`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/test_dashboard_auth.py:7`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/test_dashboard_auth.py:384`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/test_setup_precleared.py:66`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `CHANGELOG.md:562`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/codex.py:101`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/integrations/gmail.py:118`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/integrations/gmail.py:160`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/integrations/microsoft.py:128`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/integrations/microsoft.py:157`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/integrations/quota.py:51`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/test_codex.py:261`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: EA5

**Location:** `README.md:631`  
**Confidence:** 90%  

**Message:** External Model or Provider Selection

**Remediation:** Remove the model/provider override or disclose it prominently and require explicit operator approval before invoking an external coding CLI or billed model\.

**Evidence:**
- **selection\_surface:** `command`

---

### 🔴 HIGH: AS1

**Location:** `README.md:673`  
**Confidence:** 90%  

**Message:** Agent Config Directory Access

**Remediation:** Remove all code or instructions that access agent configuration directories \(\.claude/, \.codex/, \.gemini/\)\. If configuration values are needed, pass them explicitly as parameters or environment variables — never read the agent's own config files\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/claude_runtime.py:12`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/claude_runtime.py:14`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/integrations/quota.py:31`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/integrations/quota.py:54`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/integrations/quota.py:82`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/integrations/quota.py:99`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/integrations/quota.py:100`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/integrations/quota.py:104`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/test_brain_no_tools.py:87`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/test_claude_cli_isolation.py:20`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/test_claude_cli_isolation.py:203`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/cli.py:801`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/cli.py:892`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/collectors/discover.py:915`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/collectors/discover.py:1732`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/dashboard.py:33`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/integrations/gmail.py:542`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/integrations/microsoft.py:384`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/integrations/precleared.py:355`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/integrations/smtp_mail.py:163`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/main.py:490`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/setup.py:22`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/test_dashboard_auth.py:43`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/test_dashboard_auth.py:726`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/test_dashboard_auth.py:775`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/test_dashboard_companies.py:28`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/test_dashboard_live_status.py:28`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/test_dashboard_manual_send.py:25`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/test_discover.py:760`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/test_docker_config.py:41`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/test_setup_precleared.py:26`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/test_setup_precleared.py:206`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/test_windows_support.py:179`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/codex.py:306`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: E2

**Location:** `harvey/collectors/ats.py:138`  
**Confidence:** 80%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `harvey/dashboard.py:680`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/integrations/quota.py:32`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/integrations/quota.py:101`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/integrations/quota.py:113`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/integrations/quota.py:56`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/integrations/quota.py:66`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/integrations/quota.py:89`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `harvey/integrations/quota.py:116`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: P6

**Location:** `prompts/handler.md:33`  
**Confidence:** 85%  

**Message:** Direct Prompt Extraction

**Remediation:** Remove any instructions that reveal, print, or output system prompts or internal rules\. System instructions should never be exposed to end users\.

---

### 🔴 HIGH: P6

**Location:** `prompts/scout.md:31`  
**Confidence:** 85%  

**Message:** Direct Prompt Extraction

**Remediation:** Remove any instructions that reveal, print, or output system prompts or internal rules\. System instructions should never be exposed to end users\.

---

### 🔴 HIGH: AR1

**Location:** `skills/sales_methodology.md:104`  
**Confidence:** 70%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove any instruction telling the agent to never refuse or always comply\. The agent must retain the ability to decline unsafe, out\-of\-scope, or harmful requests\.

---

### 🔴 HIGH: TM1

**Location:** `tests/fake_codex.py:173`  
**Confidence:** 100%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `tests/test_brain_provider.py:59`  
**Confidence:** 100%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `tests/fake_codex.py:173`  
**Confidence:** 95%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: P1

**Location:** `tests/test_brain_no_tools.py:66`  
**Confidence:** 80%  

**Message:** Instruction Override

**Remediation:** Remove or rewrite any text that instructs the agent to ignore prompts, override safety rules, or trust unverified content\. Ensure skill content cannot be injected to alter agent behavior\.

---

### 🔴 HIGH: TM1

**Location:** `tests/test_brain_provider.py:59`  
**Confidence:** 100%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `tests/test_brain_provider.py:59`  
**Confidence:** 95%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM2

**Location:** `tests/test_brain_provider.py:59`  
**Confidence:** 75%  

**Message:** Chaining Abuse

**Remediation:** Limit tool chaining depth and validate the output of each tool before passing it to the next\. Require explicit user approval for multi\-step chains\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_claude_cli_isolation.py:111`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: P1

**Location:** `tests/test_codex.py:28`  
**Confidence:** 80%  

**Message:** Instruction Override

**Remediation:** Remove or rewrite any text that instructs the agent to ignore prompts, override safety rules, or trust unverified content\. Ensure skill content cannot be injected to alter agent behavior\.

---

### 🔴 HIGH: TM1

**Location:** `tests/test_codex.py:28`  
**Confidence:** 100%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: YR4

**Location:** `tests/test_codex.py:28`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_prompt\_injection\_hidden\_instructions': Prompt injection or hidden instructions embedded in AI agent skill text \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: P6

**Location:** `tests/test_codex.py:106`  
**Confidence:** 85%  

**Message:** Direct Prompt Extraction

**Remediation:** Remove any instructions that reveal, print, or output system prompts or internal rules\. System instructions should never be exposed to end users\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_dashboard_auth.py:745`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: YR4

**Location:** `tests/test_prompt_injection.py:81`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: SSRF1

**Location:** `tests/test_public_http.py:43`  
**Confidence:** 90%  

**Message:** Cloud Metadata Access

**Remediation:** Remove access to cloud metadata endpoints unless strictly required\. If metadata is needed, restrict it \(e\.g\. IMDSv2 with hop limit\) and never expose returned credentials\.

---

### 🔴 HIGH: SSRF1

**Location:** `tests/test_public_http.py:96`  
**Confidence:** 90%  

**Message:** Cloud Metadata Access

**Remediation:** Remove access to cloud metadata endpoints unless strictly required\. If metadata is needed, restrict it \(e\.g\. IMDSv2 with hop limit\) and never expose returned credentials\.

---

### 🔴 HIGH: SSRF1

**Location:** `tests/test_public_http.py:44`  
**Confidence:** 85%  

**Message:** Cloud Metadata Access

**Remediation:** Remove access to cloud metadata endpoints unless strictly required\. If metadata is needed, restrict it \(e\.g\. IMDSv2 with hop limit\) and never expose returned credentials\.

---

### 🟡 MEDIUM: EA2

**Location:** `CHANGELOG.md:253`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: AS3

**Location:** `README.md:615`  
**Confidence:** 80%  

**Message:** Skill Enumeration

**Remediation:** Remove all code or instructions that list or read other skills' files or directories\. Skills should operate independently; cross\-skill access is a privilege escalation\.

---

### 🟡 MEDIUM: AS3

**Location:** `harvey/config.py:660`  
**Confidence:** 80%  

**Message:** Skill Enumeration

**Remediation:** Remove all code or instructions that list or read other skills' files or directories\. Skills should operate independently; cross\-skill access is a privilege escalation\.

---

### 🟡 MEDIUM: EA2

**Location:** `harvey/agents/handler.py:907`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `harvey/config.py:328`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: SSRF3

**Location:** `harvey/agents/scout.py:1950`  
**Confidence:** 60%  

**Message:** Dynamic Request Target

**Remediation:** Do not build request URLs from untrusted input\. Validate the host against an allowlist and reject internal/metadata addresses before issuing the request\.

---

### 🟡 MEDIUM: SSRF3

**Location:** `harvey/agents/scout.py:1996`  
**Confidence:** 60%  

**Message:** Dynamic Request Target

**Remediation:** Do not build request URLs from untrusted input\. Validate the host against an allowlist and reject internal/metadata addresses before issuing the request\.

---

### 🟡 MEDIUM: SSRF3

**Location:** `harvey/agents/scout.py:2045`  
**Confidence:** 60%  

**Message:** Dynamic Request Target

**Remediation:** Do not build request URLs from untrusted input\. Validate the host against an allowlist and reject internal/metadata addresses before issuing the request\.

---

### 🟡 MEDIUM: AST4

**Location:** `harvey/claude_runtime.py:225–230`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `harvey/cli.py:52–55`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `harvey/cli.py:66–69`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `harvey/cli.py:91–94`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `harvey/cli.py:105–108`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `harvey/codex.py:423–427`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: E1

**Location:** `harvey/collectors/ats.py:153`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/test_ats_hiring.py:95`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/test_ats_hiring.py:132`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/test_ats_hiring.py:218`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/test_ats_hiring.py:311`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/test_ats_hiring.py:321`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/test_ats_hiring.py:333`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/test_ats_hiring.py:353`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/test_ats_hiring.py:470`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/test_ats_hiring.py:482`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `harvey/collectors/ats.py:154`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/test_ats_hiring.py:133`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `harvey/collectors/ats.py:155`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/test_ats_hiring.py:134`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/test_ats_hiring.py:298`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/test_ats_hiring.py:537`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `harvey/collectors/discover.py:559`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `harvey/collectors/discover.py:1222`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/test_discover.py:531`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `CLAUDE.md:118`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `harvey/dashboard.py:507`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `harvey/integrations/instantly.py:12`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `harvey/setup.py:171`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: AST4

**Location:** `harvey/dashboard.py:688–696`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: EA2

**Location:** `harvey/dashboard.py:1133`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `tests/test_precleared_hold.py:156`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: E1

**Location:** `harvey/integrations/email_finder.py:312`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `harvey/integrations/email_finder.py:426`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `harvey/integrations/email_finder.py:565`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `harvey/integrations/email_finder.py:542`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `harvey/integrations/quota.py:25`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: AST4

**Location:** `harvey/integrations/quota.py:84–87`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `harvey/integrations/quota.py:103–106`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST3

**Location:** `harvey/setup.py:332`  
**Confidence:** 75%  

**Message:** Dynamic import via \_\_import\_\_\(\)

**Remediation:** Use standard import statements instead of \_\_import\_\_\(\)\. If dynamic loading is needed, use importlib with an allowlist of permitted modules\.

---

### 🟡 MEDIUM: MP2

**Location:** `harvey/state.py:773`  
**Confidence:** 80%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: E1

**Location:** `harvey/trainer.py:48`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: EA2

**Location:** `skills/sales_methodology.md:140`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: TT2

**Location:** `tests/fake_codex.py:92`  
**Confidence:** 65%  

**Message:** Tainted flow: 'AUTH' from os\.environ \(line 38, credential/environment\) → open \(file write\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: AST3

**Location:** `tests/fake_codex.py:337`  
**Confidence:** 75%  

**Message:** Dynamic import via \_\_import\_\_\(\)

**Remediation:** Use standard import statements instead of \_\_import\_\_\(\)\. If dynamic loading is needed, use importlib with an allowlist of permitted modules\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_brain_provider.py:607–608`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_dashboard_auth.py:862–863`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_claude_cli_isolation.py:102`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_claude_cli_isolation.py:156–157`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_claude_cli_isolation.py:172–173`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: EA4

**Location:** `tests/test_claude_cli_isolation.py:185`  
**Confidence:** 80%  

**Message:** Unbounded Resource Access

**Remediation:** Set explicit rate limits, timeouts, and resource quotas for API calls, file operations, and compute\. Implement circuit breakers for runaway loops\.

---

### 🟡 MEDIUM: EA4

**Location:** `tests/test_codex_soak.py:156`  
**Confidence:** 80%  

**Message:** Unbounded Resource Access

**Remediation:** Set explicit rate limits, timeouts, and resource quotas for API calls, file operations, and compute\. Implement circuit breakers for runaway loops\.

---

### 🟡 MEDIUM: EA4

**Location:** `tests/test_codex.py:564`  
**Confidence:** 75%  

**Message:** Unbounded Resource Access

**Remediation:** Set explicit rate limits, timeouts, and resource quotas for API calls, file operations, and compute\. Implement circuit breakers for runaway loops\.

---

### 🟡 MEDIUM: EA4

**Location:** `tests/test_codex.py:565`  
**Confidence:** 75%  

**Message:** Unbounded Resource Access

**Remediation:** Set explicit rate limits, timeouts, and resource quotas for API calls, file operations, and compute\. Implement circuit breakers for runaway loops\.

---

### 🟡 MEDIUM: EA4

**Location:** `tests/test_dashboard_auth.py:750`  
**Confidence:** 75%  

**Message:** Unbounded Resource Access

**Remediation:** Set explicit rate limits, timeouts, and resource quotas for API calls, file operations, and compute\. Implement circuit breakers for runaway loops\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/test_codex_cli_surface.py:58`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: EA4

**Location:** `tests/test_codex_cli_surface.py:141`  
**Confidence:** 80%  

**Message:** Unbounded Resource Access

**Remediation:** Set explicit rate limits, timeouts, and resource quotas for API calls, file operations, and compute\. Implement circuit breakers for runaway loops\.

---

### 🟡 MEDIUM: EA4

**Location:** `tests/test_codex_cli_surface.py:141`  
**Confidence:** 80%  

**Message:** Unbounded Resource Access

**Remediation:** Set explicit rate limits, timeouts, and resource quotas for API calls, file operations, and compute\. Implement circuit breakers for runaway loops\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_codex_cli_surface.py:394–397`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST3

**Location:** `tests/test_codex_e2e.py:705`  
**Confidence:** 75%  

**Message:** Dynamic import via \_\_import\_\_\(\)

**Remediation:** Use standard import statements instead of \_\_import\_\_\(\)\. If dynamic loading is needed, use importlib with an allowlist of permitted modules\.

---

### 🟡 MEDIUM: AST3

**Location:** `tests/test_codex_e2e.py:717`  
**Confidence:** 75%  

**Message:** Dynamic import via \_\_import\_\_\(\)

**Remediation:** Use standard import statements instead of \_\_import\_\_\(\)\. If dynamic loading is needed, use importlib with an allowlist of permitted modules\.

---

### 🟡 MEDIUM: AST3

**Location:** `tests/test_collectors_profile.py:147`  
**Confidence:** 75%  

**Message:** Dynamic import via \_\_import\_\_\(\)

**Remediation:** Use standard import statements instead of \_\_import\_\_\(\)\. If dynamic loading is needed, use importlib with an allowlist of permitted modules\.

---

### 🟡 MEDIUM: AST3

**Location:** `tests/test_collectors_profile.py:148`  
**Confidence:** 75%  

**Message:** Dynamic import via \_\_import\_\_\(\)

**Remediation:** Use standard import statements instead of \_\_import\_\_\(\)\. If dynamic loading is needed, use importlib with an allowlist of permitted modules\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_dashboard_auth.py:743–745`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_dashboard_auth.py:819–820`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_dashboard_conversations.py:212–213`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_dashboard_opt_out.py:123–124`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_sending_mode.py:230–231`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST3

**Location:** `tests/test_dashboard_pipeline.py:55`  
**Confidence:** 75%  

**Message:** Dynamic import via \_\_import\_\_\(\)

**Remediation:** Use standard import statements instead of \_\_import\_\_\(\)\. If dynamic loading is needed, use importlib with an allowlist of permitted modules\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_dashboard_signals.py:440–441`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_dashboard_signals.py:498–499`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: TM3

**Location:** `tests/test_email_evidence.py:88`  
**Confidence:** 75%  

**Message:** Unsafe Defaults

**Remediation:** Override unsafe defaults with secure settings \(verify=True, auth required, restrictive permissions\)\. Review and harden all tool configurations\.

---

### 🟡 MEDIUM: TM3

**Location:** `tests/test_email_evidence.py:221`  
**Confidence:** 75%  

**Message:** Unsafe Defaults

**Remediation:** Override unsafe defaults with secure settings \(verify=True, auth required, restrictive permissions\)\. Review and harden all tool configurations\.

---

### 🟡 MEDIUM: TM3

**Location:** `tests/test_email_finder.py:146`  
**Confidence:** 75%  

**Message:** Unsafe Defaults

**Remediation:** Override unsafe defaults with secure settings \(verify=True, auth required, restrictive permissions\)\. Review and harden all tool configurations\.

---

### 🟡 MEDIUM: EA2

**Location:** `tests/test_email_finder.py:150`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_packaging.py:131–133`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_packaging.py:135–136`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_packaging.py:139–140`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: SSRF2

**Location:** `tests/test_public_http.py:279`  
**Confidence:** 70%  

**Message:** Internal Network Request

**Remediation:** Avoid requests to loopback/link\-local/private hosts from skill code\. If internal access is intended, document it and validate the target against an allowlist\.

---

### 🟡 MEDIUM: EA4

**Location:** `tests/test_writer_retry.py:1`  
**Confidence:** 75%  

**Message:** Unbounded Resource Access

**Remediation:** Set explicit rate limits, timeouts, and resource quotas for API calls, file operations, and compute\. Implement circuit breakers for runaway loops\.

---

### 🟢 LOW: TM1

**Location:** `Dockerfile:11`  
**Confidence:** 15%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🟢 LOW: TM1

**Location:** `Dockerfile:20`  
**Confidence:** 15%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🟢 LOW: TM1

**Location:** `Dockerfile:11`  
**Confidence:** 15%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🟢 LOW: TM1

**Location:** `Dockerfile:20`  
**Confidence:** 15%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🟢 LOW: TM2

**Location:** `Dockerfile:11`  
**Confidence:** 15%  

**Message:** Chaining Abuse

**Remediation:** Limit tool chaining depth and validate the output of each tool before passing it to the next\. Require explicit user approval for multi\-step chains\.

---

### 🟢 LOW: TM2

**Location:** `Dockerfile:20`  
**Confidence:** 15%  

**Message:** Chaining Abuse

**Remediation:** Limit tool chaining depth and validate the output of each tool before passing it to the next\. Require explicit user approval for multi\-step chains\.

---

### 🟢 LOW: TM1

**Location:** `Dockerfile:20`  
**Confidence:** 15%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🟢 LOW: TM2

**Location:** `Dockerfile:29`  
**Confidence:** 15%  

**Message:** Chaining Abuse

**Remediation:** Limit tool chaining depth and validate the output of each tool before passing it to the next\. Require explicit user approval for multi\-step chains\.

---

### 🟢 LOW: AST7

**Location:** `harvey/collectors/discover.py:1934`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: EA3

**Location:** `harvey/gate.py:193`  
**Confidence:** 70%  

**Message:** Scope Creep

**Remediation:** Limit the skill's scope to its documented purpose\. Remove instructions that enable the agent to perform actions outside its stated functionality\.

---

### 🟢 LOW: AST7

**Location:** `harvey/startups.py:85`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: SC4

**Location:** `pyproject.toml:2`  
**Confidence:** 40%  

**Message:** Unverifiable Dependency: setuptools has 11 known advisory\(ies\) \(GHSA\-27x4\-j476\-jp5f; GHSA\-5rjg\-fvgr\-3xxf; GHSA\-cx63\-2mw6\-8hw5 \+8 more\), but the manifest does not pin a version, so it is unknown whether the installed release is affected

**Remediation:** Determine the dependency's exact resolved version from the environment or lockfile and compare it with the advisories in OSV \(osv\.dev\)\. If it is affected, use a verified fixed release or remove or replace the dependency when no fix is available\.

---

### 🟢 LOW: SC4

**Location:** `pyproject.toml:23`  
**Confidence:** 40%  

**Message:** Unverifiable Dependency: pyyaml has 8 known advisory\(ies\) \(CVE\-2019\-20477 \(Deserialization of Untrusted Data in PyYAML\); CVE\-2020\-1747 \(Improper Input Validation in PyYAML\); CVE\-2020\-14343 \(Improper Input Validation in PyYAML\) \+5 more\), but the manifest does not pin a version, so it is unknown whether the installed release is affected

**Remediation:** Determine the dependency's exact resolved version from the environment or lockfile and compare it with the advisories in OSV \(osv\.dev\)\. If it is affected, use a verified fixed release or remove or replace the dependency when no fix is available\.

---

### 🟢 LOW: SC4

**Location:** `pyproject.toml:24`  
**Confidence:** 40%  

**Message:** Unverifiable Dependency: python\-dotenv has 2 known advisory\(ies\) \(GHSA\-mf9w\-mj56\-hr94; PYSEC\-2026\-2270\), but the manifest does not pin a version, so it is unknown whether the installed release is affected

**Remediation:** Determine the dependency's exact resolved version from the environment or lockfile and compare it with the advisories in OSV \(osv\.dev\)\. If it is affected, use a verified fixed release or remove or replace the dependency when no fix is available\.

---

### 🟢 LOW: SC4

**Location:** `pyproject.toml:25`  
**Confidence:** 40%  

**Message:** Unverifiable Dependency: httpx has 2 known advisory\(ies\) \(GHSA\-h8pj\-cxx2\-jfg2; PYSEC\-2022\-183\), but the manifest does not pin a version, so it is unknown whether the installed release is affected

**Remediation:** Determine the dependency's exact resolved version from the environment or lockfile and compare it with the advisories in OSV \(osv\.dev\)\. If it is affected, use a verified fixed release or remove or replace the dependency when no fix is available\.

---

### 🟢 LOW: SC4

**Location:** `pyproject.toml:28`  
**Confidence:** 40%  

**Message:** Unverifiable Dependency: dnspython has 3 known advisory\(ies\) \(GHSA\-3rq5\-2g8h\-59hc; GHSA\-45c3\-73f7\-pv4m; PYSEC\-2026\-1307\), but the manifest does not pin a version, so it is unknown whether the installed release is affected

**Remediation:** Determine the dependency's exact resolved version from the environment or lockfile and compare it with the advisories in OSV \(osv\.dev\)\. If it is affected, use a verified fixed release or remove or replace the dependency when no fix is available\.

---

### 🟢 LOW: SC4

**Location:** `pyproject.toml:29`  
**Confidence:** 40%  

**Message:** Unverifiable Dependency: aiosmtplib has 4 known advisory\(ies\) \(GHSA\-v3q9\-hj7j\-63hq; GHSA\-vxj7\-4xrp\-5vr4; PYSEC\-2026\-2338 \+1 more\), but the manifest does not pin a version, so it is unknown whether the installed release is affected

**Remediation:** Determine the dependency's exact resolved version from the environment or lockfile and compare it with the advisories in OSV \(osv\.dev\)\. If it is affected, use a verified fixed release or remove or replace the dependency when no fix is available\.

---

### 🟢 LOW: SC4

**Location:** `pyproject.toml:31`  
**Confidence:** 40%  

**Message:** Unverifiable Dependency: pydantic has 4 known advisory\(ies\) \(GHSA\-5jqp\-qgf6\-3pvh; GHSA\-mr82\-8j83\-vxmv; PYSEC\-2021\-47 \+1 more\), but the manifest does not pin a version, so it is unknown whether the installed release is affected

**Remediation:** Determine the dependency's exact resolved version from the environment or lockfile and compare it with the advisories in OSV \(osv\.dev\)\. If it is affected, use a verified fixed release or remove or replace the dependency when no fix is available\.

---

### 🟢 LOW: SC4

**Location:** `pyproject.toml:33`  
**Confidence:** 40%  

**Message:** Unverifiable Dependency: fastapi has 3 known advisory\(ies\) \(GHSA\-8h2j\-cgx8\-6xv7; PYSEC\-2021\-100; PYSEC\-2024\-38\), but the manifest does not pin a version, so it is unknown whether the installed release is affected

**Remediation:** Determine the dependency's exact resolved version from the environment or lockfile and compare it with the advisories in OSV \(osv\.dev\)\. If it is affected, use a verified fixed release or remove or replace the dependency when no fix is available\.

---

### 🟢 LOW: SC4

**Location:** `pyproject.toml:34`  
**Confidence:** 40%  

**Message:** Unverifiable Dependency: uvicorn has 4 known advisory\(ies\) \(GHSA\-33c7\-2mpw\-hg34; GHSA\-f97h\-2pfx\-f59f; PYSEC\-2020\-150 \+1 more\), but the manifest does not pin a version, so it is unknown whether the installed release is affected

**Remediation:** Determine the dependency's exact resolved version from the environment or lockfile and compare it with the advisories in OSV \(osv\.dev\)\. If it is affected, use a verified fixed release or remove or replace the dependency when no fix is available\.

---

### 🟢 LOW: SC4

**Location:** `pyproject.toml:39`  
**Confidence:** 40%  

**Message:** Unverifiable Dependency: pytest has 2 known advisory\(ies\) \(GHSA\-6w46\-j5rx\-g56g; PYSEC\-2026\-1845\), but the manifest does not pin a version, so it is unknown whether the installed release is affected

**Remediation:** Determine the dependency's exact resolved version from the environment or lockfile and compare it with the advisories in OSV \(osv\.dev\)\. If it is affected, use a verified fixed release or remove or replace the dependency when no fix is available\.

---

### 🟢 LOW: SC1

**Location:** `requirements.txt:13`  
**Confidence:** 50%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements\.txt or pyproject\.toml\. Use exact versions \(==\) or compatible ranges\. Run pip\-audit regularly\.

---

### 🟢 LOW: AST7

**Location:** `tests/test_models_extra.py:50`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `tests/test_smtp_header_injection.py:58`  
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
| Coverage | 96\.8% |
| Fully inspected | 180 |
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
| binary\_text\_projection | `docs/dashboard.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_content | `docs/screenshots/conversations-dark.png` | Binary content is unsupported by this analyzer\. |
| binary\_content | `docs/screenshots/conversations-light.png` | Binary content is unsupported by this analyzer\. |
| binary\_content | `docs/screenshots/outbox-dark.png` | Binary content is unsupported by this analyzer\. |
| binary\_content | `docs/screenshots/outbox-light.png` | Binary content is unsupported by this analyzer\. |
| binary\_content | `docs/screenshots/today-dark.png` | Binary content is unsupported by this analyzer\. |
| binary\_content | `docs/screenshots/today-light.png` | Binary content is unsupported by this analyzer\. |
| binary\_content | `harvey/web/fonts/geist-mono.woff2` | Binary content is unsupported by this analyzer\. |
| binary\_content | `harvey/web/fonts/geist.woff2` | Binary content is unsupported by this analyzer\. |
| binary\_content | `harvey/web/fonts/newsreader.woff2` | Binary content is unsupported by this analyzer\. |

### Ledger Exceptions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| static\_parse\_limit | `CLAUDE.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| obfuscated\_instruction\_text | `README.md` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |
| static\_parse\_limit | `harvey/web/app.js` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| runtime\_limit | `pyproject.toml` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `requirements.txt` | Inspection reached its configured runtime limit\. |
| obfuscated\_instruction\_text | `skills/email_frameworks.md` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |

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
