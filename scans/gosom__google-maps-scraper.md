# SkillSpector Security Report

**Skill:** unknown  
**Source:** `C:\Users\KHIZAR~1\AppData\Local\Temp\claude\42cf0048dc063c0d\b840f765-60a8-4e1f-a070-0a7e8f2665d3\scratchpad\gm`  
**Scanned:** 2026-11-11 16:17:51 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 100/100 |
| Severity | CRITICAL |
| Recommendation | DO NOT INSTALL |

## Components (119)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `.github/FUNDING.yaml` | yaml | 1 | No |
| `.golangci.yaml` | yaml | 77 | No |
| `.pre-commit-config.yaml` | yaml | 24 | No |
| `Dockerfile` | other | 65 | No |
| `Dockerfile.saas` | other | 65 | No |
| `Makefile` | other | 120 | No |
| `admin/admin.go` | go | 126 | Yes |
| `admin/constants.go` | go | 16 | Yes |
| `admin/handlers_2fa.go` | go | 448 | Yes |
| `admin/handlers_apikeys.go` | go | 132 | Yes |
| `admin/handlers_auth.go` | go | 174 | Yes |
| `admin/handlers_dashboard.go` | go | 94 | Yes |
| `admin/handlers_jobs.go` | go | 270 | Yes |
| `admin/handlers_settings.go` | go | 92 | Yes |
| `admin/handlers_terminal.go` | go | 290 | Yes |
| `admin/handlers_workers.go` | go | 491 | Yes |
| `admin/middleware.go` | go | 161 | Yes |
| `admin/postgres/postgres.go` | go | 580 | Yes |
| `admin/render.go` | go | 51 | Yes |
| `admin/routes.go` | go | 78 | Yes |
| `admin/state.go` | go | 40 | Yes |
| `api/api.go` | go | 305 | Yes |
| `api/doc.go` | go | 17 | Yes |
| `api/docs/docs.go` | go | 468 | Yes |
| `api/docs/swagger.yaml` | yaml | 321 | No |
| `api/middleware.go` | go | 61 | Yes |
| `api/postgres/postgres.go` | go | 73 | Yes |
| `api/responses.go` | go | 207 | Yes |
| `cli/prompt.go` | go | 80 | Yes |
| `cli/ui.go` | go | 66 | Yes |
| `cmd/gmapssaas/cmdadmin/cmd_admin.go` | go | 110 | Yes |
| `cmd/gmapssaas/cmdcommon/common.go` | go | 92 | Yes |
| `cmd/gmapssaas/cmdprovision/provision.go` | go | 964 | Yes |
| `cmd/gmapssaas/cmdprovision/state.go` | go | 148 | Yes |
| `cmd/gmapssaas/cmdserve/cmd_serve.go` | go | 175 | Yes |
| `cmd/gmapssaas/cmdupdate/cmd_update.go` | go | 263 | Yes |
| `cmd/gmapssaas/cmdworker/cmd_worker.go` | go | 283 | Yes |
| `cmd/gmapssaas/main.go` | go | 56 | Yes |
| `cmd/tools/tools.go` | go | 10 | Yes |
| `cryptoext/cryptoext.go` | go | 220 | Yes |
| `deduper/deduper.go` | go | 17 | Yes |
| `deduper/hashmap.go` | go | 43 | Yes |
| `docker-compose.dev.yaml` | yaml | 31 | No |
| `docker-compose.saas.yaml` | yaml | 19 | No |
| `env/env.go` | go | 24 | Yes |
| `examples/examples-api/go/main.go` | go | 266 | Yes |
| `examples/plugins/example_writer.go` | go | 85 | Yes |
| `exiter/exiter.go` | go | 93 | Yes |
| `gmaps/completion.go` | go | 6 | Yes |
| `gmaps/emailjob.go` | go | 176 | Yes |
| `gmaps/entry.go` | go | 1049 | Yes |
| `gmaps/job.go` | go | 422 | Yes |
| `gmaps/multiple.go` | go | 90 | Yes |
| `gmaps/place.go` | go | 358 | Yes |
| `gmaps/reviews.go` | go | 841 | Yes |
| `gmaps/searchjob.go` | go | 170 | Yes |
| `go.mod` | other | 345 | No |
| `grid/grid.go` | go | 165 | Yes |
| `httpext/httpext.go` | go | 89 | Yes |
| `httpext/middleware.go` | go | 74 | Yes |
| `infra/cloudinit/cloudinit.go` | go | 335 | Yes |
| `infra/digitalocean/appplatform.go` | go | 382 | Yes |
| `infra/digitalocean/digitalocean.go` | go | 246 | Yes |
| `infra/hetzner/hetzner.go` | go | 277 | Yes |
| `infra/infra.go` | go | 83 | Yes |
| `infra/planetscale/planetscale.go` | go | 127 | Yes |
| `infra/ssh_tofu.go` | go | 161 | Yes |
| `infra/vps/provisioner.go` | go | 178 | Yes |
| `infra/vps/scripts.go` | go | 213 | Yes |
| `infra/worker.go` | go | 92 | Yes |
| `internal/jsonbsanitize/entry.go` | go | 177 | Yes |
| `internal/proxyconfig/proxyconfig.go` | go | 60 | Yes |
| `leadsdb/leadsdb.go` | go | 209 | Yes |
| `lint.go` | go | 6 | Yes |
| `local/cloud-init-test.yaml` | yaml | 2 | No |
| `log/log.go` | go | 72 | Yes |
| `main.go` | go | 84 | Yes |
| `migrations/migrations.go` | go | 40 | Yes |
| `postgres/pool.go` | go | 87 | Yes |
| `postgres/provider.go` | go | 281 | Yes |
| `postgres/resultwriter.go` | go | 209 | Yes |
| `ratelimit/postgres/postgres.go` | go | 125 | Yes |
| `ratelimit/ratelimit.go` | go | 40 | Yes |
| `rqueue/jobs.go` | go | 76 | Yes |
| `rqueue/rqueue.go` | go | 924 | Yes |
| `rqueue/ui.go` | go | 28 | Yes |
| `rqueue/worker_jobs.go` | go | 817 | Yes |
| `runner/databaserunner/databaserunner.go` | go | 189 | Yes |
| `runner/filerunner/filerunner.go` | go | 414 | Yes |
| `runner/installplaywright/installplaywright.go` | go | 34 | Yes |
| `runner/jobs.go` | go | 391 | Yes |
| `runner/lambdaaws/invoker.go` | go | 170 | Yes |
| `runner/lambdaaws/io.go` | go | 16 | Yes |
| `runner/lambdaaws/lambdaaws.go` | go | 195 | Yes |
| `runner/resume/progress.go` | go | 98 | Yes |
| `runner/resume/results.go` | go | 291 | Yes |
| `runner/resume/state.go` | go | 156 | Yes |
| `runner/resume/writer.go` | go | 206 | Yes |
| `runner/runner.go` | go | 361 | Yes |
| `runner/webrunner/webrunner.go` | go | 316 | Yes |
| `s3uploader/s3uploader.go` | go | 48 | Yes |
| `saas/constants.go` | go | 24 | Yes |
| `scraper/centralwriter.go` | go | 254 | Yes |
| `scraper/provider.go` | go | 117 | Yes |
| `scraper/scraper.go` | go | 271 | Yes |
| `skills/google-maps-scraper/scripts/configure-proxy.sh` | shell | 54 | Yes |
| `skills/google-maps-scraper/scripts/ensure-latest.sh` | shell | 15 | Yes |
| `skills/google-maps-scraper/scripts/helpers_test.sh` | shell | 190 | Yes |
| `skills/google-maps-scraper/scripts/run-local.sh` | shell | 220 | Yes |
| `tlmt/gonoop/gonoop.go` | go | 22 | Yes |
| `tlmt/goposthog/goposthog.go` | go | 47 | Yes |
| `tlmt/tlmt.go` | go | 138 | Yes |
| `web/errors.go` | go | 8 | Yes |
| `web/job.go` | go | 118 | Yes |
| `web/places.go` | go | 141 | Yes |
| `web/service.go` | go | 150 | Yes |
| `web/sqlite/sqlite.go` | go | 253 | Yes |
| `web/static/spec/spec.yaml` | yaml | 252 | No |
| `web/web.go` | go | 719 | Yes |

## Issues (66)

### 🔴 HIGH: TM2

**Location:** `Dockerfile:61`  
**Confidence:** 75%  

**Message:** Chaining Abuse

**Remediation:** Limit tool chaining depth and validate the output of each tool before passing it to the next\. Require explicit user approval for multi\-step chains\.

---

### 🔴 HIGH: TM1

**Location:** `Dockerfile.saas:52`  
**Confidence:** 90%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `Dockerfile.saas:52`  
**Confidence:** 90%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `Dockerfile.saas:52`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM2

**Location:** `Dockerfile.saas:52`  
**Confidence:** 75%  

**Message:** Chaining Abuse

**Remediation:** Limit tool chaining depth and validate the output of each tool before passing it to the next\. Require explicit user approval for multi\-step chains\.

---

### 🔴 HIGH: PE4

**Location:** `Makefile:68`  
**Confidence:** 90%  

**Message:** Docker Socket Access

**Remediation:** Review the flagged content for security risks\. Ensure no credentials, secrets, or sensitive data are exposed\.

---

### 🔴 HIGH: TM1

**Location:** `Makefile:120`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: PE3

**Location:** `admin/handlers_terminal.go:108`  
**Confidence:** 80%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `cmd/gmapssaas/cmdcommon/common.go:65`  
**Confidence:** 80%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `cmd/gmapssaas/cmdprovision/provision.go:685`  
**Confidence:** 80%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: MP3

**Location:** `cmd/gmapssaas/cmdprovision/provision.go:65`  
**Confidence:** 80%  

**Message:** Memory Manipulation

**Remediation:** Protect agent memory and state from modification by untrusted content\. Use read\-only memory for critical instructions and validate all state changes\.

---

### 🔴 HIGH: PE3

**Location:** `cmd/gmapssaas/cmdprovision/provision.go:659`  
**Confidence:** 90%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `cmd/gmapssaas/cmdupdate/cmd_update.go:195`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `infra/cloudinit/cloudinit.go:87`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `infra/cloudinit/cloudinit.go:148`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `infra/cloudinit/cloudinit.go:166`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `infra/cloudinit/cloudinit.go:216`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `infra/cloudinit/cloudinit.go:247`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `infra/cloudinit/cloudinit.go:283`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `infra/cloudinit/cloudinit.go:300`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `infra/vps/scripts.go:169`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `infra/vps/scripts.go:170`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `infra/vps/scripts.go:176`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `infra/vps/scripts.go:187`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `rqueue/worker_jobs.go:702`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: P1

**Location:** `cmd/gmapssaas/cmdworker/cmd_worker.go:61`  
**Confidence:** 70%  

**Message:** Instruction Override

**Remediation:** Remove or rewrite any text that instructs the agent to ignore prompts, override safety rules, or trust unverified content\. Ensure skill content cannot be injected to alter agent behavior\.

---

### 🔴 HIGH: TM2

**Location:** `infra/cloudinit/cloudinit.go:206`  
**Confidence:** 70%  

**Message:** Chaining Abuse

**Remediation:** Limit tool chaining depth and validate the output of each tool before passing it to the next\. Require explicit user approval for multi\-step chains\.

---

### 🔴 HIGH: TM2

**Location:** `infra/cloudinit/cloudinit.go:271`  
**Confidence:** 70%  

**Message:** Chaining Abuse

**Remediation:** Limit tool chaining depth and validate the output of each tool before passing it to the next\. Require explicit user approval for multi\-step chains\.

---

### 🔴 HIGH: TM2

**Location:** `infra/vps/scripts.go:31`  
**Confidence:** 70%  

**Message:** Chaining Abuse

**Remediation:** Limit tool chaining depth and validate the output of each tool before passing it to the next\. Require explicit user approval for multi\-step chains\.

---

### 🔴 HIGH: PE3

**Location:** `infra/vps/scripts.go:27`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `infra/vps/scripts.go:27`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `infra/vps/scripts.go:49`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `infra/vps/scripts.go:49`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: TM1

**Location:** `infra/vps/scripts.go:64`  
**Confidence:** 70%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `infra/vps/scripts.go:80`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM2

**Location:** `infra/vps/scripts.go:80`  
**Confidence:** 75%  

**Message:** Chaining Abuse

**Remediation:** Limit tool chaining depth and validate the output of each tool before passing it to the next\. Require explicit user approval for multi\-step chains\.

---

### 🔴 HIGH: TM2

**Location:** `infra/vps/scripts.go:80`  
**Confidence:** 75%  

**Message:** Chaining Abuse

**Remediation:** Limit tool chaining depth and validate the output of each tool before passing it to the next\. Require explicit user approval for multi\-step chains\.

---

### 🟡 MEDIUM: RP1

**Location:** `Makefile:66`  
**Confidence:** 75%  

**Message:** Docker image referenced without tag or digest: 'docker run \-\-rm'\.

**Remediation:** Pin the image: image:tag or image@sha256:abc123

---

### 🟡 MEDIUM: EA4

**Location:** `gmaps/emailjob.go:29`  
**Confidence:** 80%  

**Message:** Unbounded Resource Access

**Remediation:** Set explicit rate limits, timeouts, and resource quotas for API calls, file operations, and compute\. Implement circuit breakers for runaway loops\.

---

### 🟡 MEDIUM: RA2

**Location:** `infra/cloudinit/cloudinit.go:207`  
**Confidence:** 80%  

**Message:** Session Persistence

**Remediation:** Remove any persistence mechanisms \(cron jobs, startup scripts, state files\)\. Skills should not maintain state across sessions without explicit user consent\.

---

### 🟡 MEDIUM: RA2

**Location:** `infra/cloudinit/cloudinit.go:272`  
**Confidence:** 80%  

**Message:** Session Persistence

**Remediation:** Remove any persistence mechanisms \(cron jobs, startup scripts, state files\)\. Skills should not maintain state across sessions without explicit user consent\.

---

### 🟡 MEDIUM: RA2

**Location:** `infra/vps/scripts.go:32`  
**Confidence:** 80%  

**Message:** Session Persistence

**Remediation:** Remove any persistence mechanisms \(cron jobs, startup scripts, state files\)\. Skills should not maintain state across sessions without explicit user consent\.

---

### 🟡 MEDIUM: RA2

**Location:** `infra/vps/scripts.go:60`  
**Confidence:** 80%  

**Message:** Session Persistence

**Remediation:** Remove any persistence mechanisms \(cron jobs, startup scripts, state files\)\. Skills should not maintain state across sessions without explicit user consent\.

---

### 🟡 MEDIUM: E1

**Location:** `infra/planetscale/planetscale.go:16`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: PE2

**Location:** `infra/vps/scripts.go:41`  
**Confidence:** 70%  

**Message:** Sudo/Root Execution

**Remediation:** Avoid sudo/root unless strictly required\. Prefer least\-privilege patterns\. If elevation is needed, document the justification and scope\.

---

### 🟡 MEDIUM: PE2

**Location:** `infra/vps/scripts.go:80`  
**Confidence:** 70%  

**Message:** Sudo/Root Execution

**Remediation:** Avoid sudo/root unless strictly required\. Prefer least\-privilege patterns\. If elevation is needed, document the justification and scope\.

---

### 🟡 MEDIUM: RP1

**Location:** `skills/google-maps-scraper/scripts/ensure-latest.sh:6`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx is'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `skills/google-maps-scraper/scripts/ensure-latest.sh:10`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx \-\-yes skills'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `skills/google-maps-scraper/scripts/helpers_test.sh:181`  
**Confidence:** 75%  

**Message:** Docker image referenced without tag or digest: 'Docker pull after'\.

**Remediation:** Pin the image: image:tag or image@sha256:abc123

---

### 🟡 MEDIUM: RP1

**Location:** `skills/google-maps-scraper/scripts/run-local.sh:198`  
**Confidence:** 75%  

**Message:** Docker image referenced without tag or digest: 'docker pull "$image\_name";'\.

**Remediation:** Pin the image: image:tag or image@sha256:abc123

---

### 🟡 MEDIUM: RP1

**Location:** `skills/google-maps-scraper/scripts/run-local.sh:200`  
**Confidence:** 75%  

**Message:** Docker image referenced without tag or digest: 'docker pull "$image\_name";'\.

**Remediation:** Pin the image: image:tag or image@sha256:abc123

---

### 🟡 MEDIUM: E1

**Location:** `web/static/spec/spec.yaml:14`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟢 LOW: TM1

**Location:** `Dockerfile:14`  
**Confidence:** 15%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🟢 LOW: TM1

**Location:** `Dockerfile:55`  
**Confidence:** 15%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🟢 LOW: TM1

**Location:** `Dockerfile.saas:53`  
**Confidence:** 15%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🟢 LOW: TM1

**Location:** `Dockerfile:14`  
**Confidence:** 15%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🟢 LOW: TM1

**Location:** `Dockerfile:55`  
**Confidence:** 15%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🟢 LOW: TM1

**Location:** `Dockerfile:14`  
**Confidence:** 15%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🟢 LOW: TM2

**Location:** `Dockerfile:14`  
**Confidence:** 15%  

**Message:** Chaining Abuse

**Remediation:** Limit tool chaining depth and validate the output of each tool before passing it to the next\. Require explicit user approval for multi\-step chains\.

---

### 🟢 LOW: TM2

**Location:** `Dockerfile:55`  
**Confidence:** 15%  

**Message:** Chaining Abuse

**Remediation:** Limit tool chaining depth and validate the output of each tool before passing it to the next\. Require explicit user approval for multi\-step chains\.

---

### 🟢 LOW: TM2

**Location:** `Dockerfile.saas:53`  
**Confidence:** 15%  

**Message:** Chaining Abuse

**Remediation:** Limit tool chaining depth and validate the output of each tool before passing it to the next\. Require explicit user approval for multi\-step chains\.

---

### 🟢 LOW: TM1

**Location:** `Dockerfile.saas:53`  
**Confidence:** 15%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🟢 LOW: TM1

**Location:** `Dockerfile.saas:53`  
**Confidence:** 15%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🟢 LOW: SC2

**Location:** `infra/cloudinit/cloudinit.go:206`  
**Confidence:** 15%  

**Message:** External Script Fetching

**Remediation:** Avoid downloading and executing remote scripts\. Use trusted packages from PyPI/npm\. If remote fetch is required, verify checksums and use HTTPS\.

---

### 🟢 LOW: SC2

**Location:** `infra/cloudinit/cloudinit.go:271`  
**Confidence:** 15%  

**Message:** External Script Fetching

**Remediation:** Avoid downloading and executing remote scripts\. Use trusted packages from PyPI/npm\. If remote fetch is required, verify checksums and use HTTPS\.

---

### 🟢 LOW: SC2

**Location:** `infra/vps/scripts.go:27`  
**Confidence:** 15%  

**Message:** External Script Fetching

**Remediation:** Avoid downloading and executing remote scripts\. Use trusted packages from PyPI/npm\. If remote fetch is required, verify checksums and use HTTPS\.

---

## Inspection Completeness

| Metric | Value |
|--------|-------|
| Execution | successful |
| Status | partial |
| Dependency contents | not\_requested |
| Coverage | 95\.0% |
| Fully inspected | 113 |
| Partially inspected | 6 |
| Entirely uninspected | 0 |

### Ledger Exceptions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| static\_parse\_limit | `Makefile` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| obfuscated\_instruction\_text | `api/docs/docs.go` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |
| obfuscated\_instruction\_text | `cmd/gmapssaas/cmdprovision/provision.go` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |
| static\_parse\_limit | `rqueue/rqueue.go` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| obfuscated\_instruction\_text | `rqueue/worker_jobs.go` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |
| static\_parse\_limit | `rqueue/worker_jobs.go` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| obfuscated\_instruction\_text | `web/web.go` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |

### Analyzer Statuses

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| completed | `artifact_integrity` |  |
| no\_applicable\_files | `behavioral_ast` | No files matched this analyzer's applicability contract\. |
| no\_applicable\_files | `behavioral_taint_tracking` | No files matched this analyzer's applicability contract\. |
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
