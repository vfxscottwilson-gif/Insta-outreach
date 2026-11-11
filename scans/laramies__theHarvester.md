# SkillSpector Security Report

**Skill:** unknown  
**Source:** `F:\Github Repos\repos\laramies__theHarvester`  
**Scanned:** 2026-11-11 16:07:14 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 100/100 |
| Severity | CRITICAL |
| Recommendation | DO NOT INSTALL |

## Components (349)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `.dockerignore` | other | 30 | No |
| `.git-blame-ignore-revs` | other | 2 | No |
| `.git/config` | other | 13 | No |
| `.gitattributes` | other | 27 | No |
| `.github/FUNDING.yml` | yaml | 11 | No |
| `.github/ISSUE_TEMPLATE/bug_report.yml` | yaml | 95 | No |
| `.github/ISSUE_TEMPLATE/config.yml` | yaml | 5 | No |
| `.github/ISSUE_TEMPLATE/feature_request.yml` | yaml | 69 | No |
| `.github/dependabot.yml` | yaml | 39 | No |
| `.github/workflows/codeql-analysis.yml` | yaml | 59 | No |
| `.github/workflows/dependency-review.yml` | yaml | 29 | No |
| `.github/workflows/docker-build-push.yml` | yaml | 57 | No |
| `.github/workflows/dockerci.yml` | yaml | 23 | No |
| `.github/workflows/harvestview-container.yml` | yaml | 94 | No |
| `.github/workflows/harvestview-e2e.yml` | yaml | 64 | No |
| `.github/workflows/provider-smoke.yml` | yaml | 158 | No |
| `.github/workflows/scorecards.yml` | yaml | 81 | No |
| `.github/workflows/theHarvester.yml` | yaml | 63 | No |
| `.github/zizmor.yml` | yaml | 5 | No |
| `.gitignore` | other | 58 | No |
| `.python-version` | other | 1 | No |
| `AGENTS.md` | markdown | 50 | No |
| `CHANGELOG.md` | markdown | 217 | No |
| `CODING_STANDARDS.md` | markdown | 67 | No |
| `CONTRIBUTING.md` | markdown | 125 | No |
| `DESIGN.md` | markdown | 57 | No |
| `Dockerfile` | other | 51 | No |
| `GLOSSARY.md` | markdown | 274 | No |
| `LICENSE` | other | 117 | No |
| `PRODUCT.md` | markdown | 34 | No |
| `README.md` | markdown | 410 | No |
| `README/LICENSES` | other | 15 | No |
| `SECURITY.md` | markdown | 33 | No |
| `bin/harvestview` | other | 5 | Yes |
| `bin/theHarvester` | other | 17 | Yes |
| `docker-compose.yml` | yaml | 34 | No |
| `docs/adr/0003-run-worker-lifecycle.md` | markdown | 21 | No |
| `docs/adr/0004-keep-network-evidence-typed-and-external.md` | markdown | 23 | No |
| `docs/adr/0005-persist-asn-organization-attribution-as-sourced-evidence.md` | markdown | 15 | No |
| `docs/adr/0006-schedule-finite-runs-through-a-private-control-plane.md` | markdown | 5 | No |
| `docs/adr/0007-keep-operator-hostname-as-exact-scope.md` | markdown | 19 | No |
| `docs/adr/0008-fail-closed-when-explicit-proxy-mode-is-unavailable.md` | markdown | 27 | No |
| `docs/adr/0009-scope-proxy-mode-to-http-transport.md` | markdown | 5 | No |
| `docs/adr/0010-own-api-background-state-in-the-app-lifespan.md` | markdown | 31 | No |
| `docs/agents/domain.md` | markdown | 15 | No |
| `docs/agents/issue-tracker.md` | markdown | 60 | No |
| `docs/agents/triage-labels.md` | markdown | 15 | No |
| `docs/architecture.md` | markdown | 49 | No |
| `docs/coding-standards-research.md` | markdown | 51 | No |
| `docs/context-glossary-research.md` | markdown | 19 | No |
| `docs/images/harvestview-architecture.html` | other | 133 | No |
| `docs/images/harvestview-architecture.svg` | other | 118 | Yes |
| `docs/images/run-evidence-architecture.html` | other | 119 | No |
| `docs/images/run-evidence-architecture.svg` | other | 104 | Yes |
| `docs/images/vhost-classifier.svg` | other | 120 | Yes |
| `docs/images/vhost-sweep-overview.svg` | other | 80 | Yes |
| `docs/wiki/Configuration-and-API-Keys.md` | markdown | 93 | No |
| `docs/wiki/Contributing-and-Security.md` | markdown | 11 | No |
| `docs/wiki/Home.md` | markdown | 34 | No |
| `docs/wiki/How-to-add-a-new-module.md` | markdown | 89 | No |
| `docs/wiki/Installation.md` | markdown | 101 | No |
| `docs/wiki/Moving-from-4.11-to-5.0.md` | markdown | 210 | No |
| `docs/wiki/Operator-Workflows.md` | markdown | 178 | No |
| `docs/wiki/Quick-Start.md` | markdown | 55 | No |
| `docs/wiki/Responsible-Use-and-Scope.md` | markdown | 59 | No |
| `docs/wiki/Rest-API.md` | markdown | 284 | No |
| `docs/wiki/Results-and-Local-Data.md` | markdown | 250 | No |
| `docs/wiki/Roadmap.md` | markdown | 14 | No |
| `docs/wiki/Troubleshooting.md` | markdown | 118 | No |
| `docs/wiki/Virtual-Host-Discovery.md` | markdown | 288 | No |
| `docs/wiki/_Footer.md` | markdown | 3 | No |
| `docs/wiki/_Sidebar.md` | markdown | 28 | No |
| `pyproject.toml` | toml | 146 | No |
| `tests/__init__.py` | python | 0 | Yes |
| `tests/conftest.py` | python | 181 | Yes |
| `tests/discovery/__init__.py` | python | 0 | Yes |
| `tests/discovery/test_api_endpoints.py` | python | 1266 | Yes |
| `tests/discovery/test_apisguru.py` | python | 968 | Yes |
| `tests/discovery/test_arquivo.py` | python | 169 | Yes |
| `tests/discovery/test_baidusearch.py` | python | 425 | Yes |
| `tests/discovery/test_bevigil.py` | python | 181 | Yes |
| `tests/discovery/test_brave.py` | python | 506 | Yes |
| `tests/discovery/test_bufferoverun.py` | python | 141 | Yes |
| `tests/discovery/test_builtwith.py` | python | 344 | Yes |
| `tests/discovery/test_censys.py` | python | 367 | Yes |
| `tests/discovery/test_certspotter.py` | python | 393 | Yes |
| `tests/discovery/test_commoncrawl.py` | python | 836 | Yes |
| `tests/discovery/test_criminalip.py` | python | 278 | Yes |
| `tests/discovery/test_crtname.py` | python | 319 | Yes |
| `tests/discovery/test_crtsh.py` | python | 181 | Yes |
| `tests/discovery/test_darkeye.py` | python | 747 | Yes |
| `tests/discovery/test_dnsdb.py` | python | 262 | Yes |
| `tests/discovery/test_dnsdumpster.py` | python | 143 | Yes |
| `tests/discovery/test_duckduckgo.py` | python | 156 | Yes |
| `tests/discovery/test_dymosearch.py` | python | 102 | Yes |
| `tests/discovery/test_fofa.py` | python | 216 | Yes |
| `tests/discovery/test_fullhuntsearch.py` | python | 329 | Yes |
| `tests/discovery/test_githubcode.py` | python | 92 | Yes |
| `tests/discovery/test_githubcode_additions.py` | python | 79 | Yes |
| `tests/discovery/test_githubcode_contract.py` | python | 436 | Yes |
| `tests/discovery/test_githubcode_logging.py` | python | 23 | Yes |
| `tests/discovery/test_gitlabsearch.py` | python | 334 | Yes |
| `tests/discovery/test_hackertarget_apikey.py` | python | 295 | Yes |
| `tests/discovery/test_haveibeenpwned.py` | python | 215 | Yes |
| `tests/discovery/test_hibpverified.py` | python | 195 | Yes |
| `tests/discovery/test_hudsonrock.py` | python | 336 | Yes |
| `tests/discovery/test_hunterhow.py` | python | 206 | Yes |
| `tests/discovery/test_huntersearch.py` | python | 330 | Yes |
| `tests/discovery/test_intelxsearch.py` | python | 245 | Yes |
| `tests/discovery/test_jsmon.py` | python | 189 | Yes |
| `tests/discovery/test_leakix.py` | python | 143 | Yes |
| `tests/discovery/test_leaklookup.py` | python | 198 | Yes |
| `tests/discovery/test_mojeek.py` | python | 699 | Yes |
| `tests/discovery/test_netlas.py` | python | 219 | Yes |
| `tests/discovery/test_onyphe.py` | python | 290 | Yes |
| `tests/discovery/test_otilabs.py` | python | 197 | Yes |
| `tests/discovery/test_otx.py` | python | 227 | Yes |
| `tests/discovery/test_outcrawl.py` | python | 498 | Yes |
| `tests/discovery/test_pentesttools.py` | python | 308 | Yes |
| `tests/discovery/test_post_provider_outcomes.py` | python | 135 | Yes |
| `tests/discovery/test_profundis.py` | python | 218 | Yes |
| `tests/discovery/test_projectdiscovery.py` | python | 210 | Yes |
| `tests/discovery/test_provider_failure_outcomes.py` | python | 214 | Yes |
| `tests/discovery/test_provider_session_lifecycle.py` | python | 422 | Yes |
| `tests/discovery/test_rapiddns.py` | python | 381 | Yes |
| `tests/discovery/test_robtex.py` | python | 166 | Yes |
| `tests/discovery/test_rocketreach.py` | python | 192 | Yes |
| `tests/discovery/test_scanmalware.py` | python | 561 | Yes |
| `tests/discovery/test_search_dehashed.py` | python | 156 | Yes |
| `tests/discovery/test_securityscorecard.py` | python | 224 | Yes |
| `tests/discovery/test_securitytrails.py` | python | 132 | Yes |
| `tests/discovery/test_serply.py` | python | 504 | Yes |
| `tests/discovery/test_sherlockeye.py` | python | 270 | Yes |
| `tests/discovery/test_shodan_engine.py` | python | 884 | Yes |
| `tests/discovery/test_shodanct.py` | python | 106 | Yes |
| `tests/discovery/test_sourcegraph.py` | python | 486 | Yes |
| `tests/discovery/test_subdomainapi.py` | python | 116 | Yes |
| `tests/discovery/test_subdomaincenter.py` | python | 106 | Yes |
| `tests/discovery/test_subdomainfinderc99.py` | python | 166 | Yes |
| `tests/discovery/test_takeover.py` | python | 1102 | Yes |
| `tests/discovery/test_thc.py` | python | 515 | Yes |
| `tests/discovery/test_tombasearch.py` | python | 410 | Yes |
| `tests/discovery/test_urlscan.py` | python | 509 | Yes |
| `tests/discovery/test_virustotal.py` | python | 243 | Yes |
| `tests/discovery/test_waybackarchive.py` | python | 353 | Yes |
| `tests/discovery/test_whoisxml.py` | python | 246 | Yes |
| `tests/discovery/test_windvane.py` | python | 188 | Yes |
| `tests/discovery/test_yahoosearch.py` | python | 135 | Yes |
| `tests/discovery/test_zoomeyesearch.py` | python | 291 | Yes |
| `tests/e2e/conftest.py` | python | 180 | Yes |
| `tests/e2e/test_harvestview.py` | python | 2172 | Yes |
| `tests/fixtures/takeover_can_i_take_over_xyz_5bd4e128.fixture` | other | 28 | No |
| `tests/lib/test_active_evidence.py` | python | 110 | Yes |
| `tests/lib/test_api_v1.py` | python | 2147 | Yes |
| `tests/lib/test_completed_persistence.py` | python | 1752 | Yes |
| `tests/lib/test_completed_result.py` | python | 1494 | Yes |
| `tests/lib/test_configuration_contract.py` | python | 209 | Yes |
| `tests/lib/test_core.py` | python | 1594 | Yes |
| `tests/lib/test_dns_consensus.py` | python | 336 | Yes |
| `tests/lib/test_enumeration.py` | python | 107 | Yes |
| `tests/lib/test_harvestview_ui.py` | python | 253 | Yes |
| `tests/lib/test_hostchecker.py` | python | 767 | Yes |
| `tests/lib/test_hostnames.py` | python | 22 | Yes |
| `tests/lib/test_output.py` | python | 17 | Yes |
| `tests/lib/test_recursive_dns.py` | python | 334 | Yes |
| `tests/lib/test_routeviews.py` | python | 714 | Yes |
| `tests/lib/test_run_backend.py` | python | 1578 | Yes |
| `tests/lib/test_runtime_services.py` | python | 237 | Yes |
| `tests/lib/test_schedules.py` | python | 999 | Yes |
| `tests/lib/test_source_catalog.py` | python | 126 | Yes |
| `tests/lib/test_source_runner.py` | python | 1237 | Yes |
| `tests/lib/test_target_identity.py` | python | 44 | Yes |
| `tests/lib/test_virtual_host.py` | python | 1234 | Yes |
| `tests/runtime_helpers.py` | python | 46 | Yes |
| `tests/screenshot_helpers.py` | python | 38 | Yes |
| `tests/test_agent_guidance.py` | python | 14 | Yes |
| `tests/test_all_source_orchestration.py` | python | 356 | Yes |
| `tests/test_bootstrap.py` | python | 133 | Yes |
| `tests/test_docker.py` | python | 73 | Yes |
| `tests/test_harness.py` | python | 61 | Yes |
| `tests/test_harvestview_launcher.py` | python | 27 | Yes |
| `tests/test_harvestview_log_level.py` | python | 48 | Yes |
| `tests/test_logging.py` | python | 203 | Yes |
| `tests/test_main.py` | python | 4936 | Yes |
| `tests/test_myparser.py` | python | 51 | Yes |
| `tests/test_no_hosts.py` | python | 137 | Yes |
| `tests/test_provider_contract_coverage.py` | python | 34 | Yes |
| `tests/test_readme.py` | python | 483 | Yes |
| `tests/test_release_artifacts.py` | python | 42 | Yes |
| `tests/test_runtime_dependencies.py` | python | 80 | Yes |
| `tests/test_saved_run_report_cli.py` | python | 995 | Yes |
| `tests/test_screenshot.py` | python | 611 | Yes |
| `tests/test_security.py` | python | 351 | Yes |
| `tests/test_workflow_contract.py` | python | 113 | Yes |
| `theHarvester-logo.png` | other | 522 | No |
| `theHarvester-logo.webp` | other | 196 | No |
| `theHarvester/__init__.py` | python | 1 | Yes |
| `theHarvester/__main__.py` | python | 2203 | Yes |
| `theHarvester/data/api-keys.yaml` | yaml | 132 | No |
| `theHarvester/data/proxies.yaml` | yaml | 4 | No |
| `theHarvester/data/wordlists/api_endpoints.txt` | text | 920 | No |
| `theHarvester/data/wordlists/dns-names.txt` | text | 4989 | No |
| `theHarvester/discovery/__init__.py` | python | 0 | Yes |
| `theHarvester/discovery/api_endpoints.py` | python | 1074 | Yes |
| `theHarvester/discovery/apisguru.py` | python | 363 | Yes |
| `theHarvester/discovery/arquivo.py` | python | 98 | Yes |
| `theHarvester/discovery/baidusearch.py` | python | 194 | Yes |
| `theHarvester/discovery/bevigil.py` | python | 94 | Yes |
| `theHarvester/discovery/bravesearch.py` | python | 174 | Yes |
| `theHarvester/discovery/bufferoverun.py` | python | 76 | Yes |
| `theHarvester/discovery/builtwith.py` | python | 215 | Yes |
| `theHarvester/discovery/censysearch.py` | python | 143 | Yes |
| `theHarvester/discovery/certspottersearch.py` | python | 148 | Yes |
| `theHarvester/discovery/commoncrawl.py` | python | 249 | Yes |
| `theHarvester/discovery/constants.py` | python | 23 | Yes |
| `theHarvester/discovery/criminalip.py` | python | 358 | Yes |
| `theHarvester/discovery/crtname.py` | python | 96 | Yes |
| `theHarvester/discovery/crtsh.py` | python | 74 | Yes |
| `theHarvester/discovery/darkeye.py` | python | 247 | Yes |
| `theHarvester/discovery/dnsdb.py` | python | 116 | Yes |
| `theHarvester/discovery/dnssearch.py` | python | 299 | Yes |
| `theHarvester/discovery/duckduckgosearch.py` | python | 126 | Yes |
| `theHarvester/discovery/dymosearch.py` | python | 100 | Yes |
| `theHarvester/discovery/fofa.py` | python | 143 | Yes |
| `theHarvester/discovery/fullhuntsearch.py` | python | 290 | Yes |
| `theHarvester/discovery/githubcode.py` | python | 251 | Yes |
| `theHarvester/discovery/gitlabsearch.py` | python | 262 | Yes |
| `theHarvester/discovery/hackertarget.py` | python | 153 | Yes |
| `theHarvester/discovery/haveibeenpwned.py` | python | 83 | Yes |
| `theHarvester/discovery/hibpverified.py` | python | 79 | Yes |
| `theHarvester/discovery/hudsonrocksearch.py` | python | 478 | Yes |
| `theHarvester/discovery/huntersearch.py` | python | 139 | Yes |
| `theHarvester/discovery/intelxsearch.py` | python | 180 | Yes |
| `theHarvester/discovery/jsmon.py` | python | 99 | Yes |
| `theHarvester/discovery/leakix.py` | python | 107 | Yes |
| `theHarvester/discovery/leaklookup.py` | python | 93 | Yes |
| `theHarvester/discovery/mojeek.py` | python | 240 | Yes |
| `theHarvester/discovery/netlas.py` | python | 124 | Yes |
| `theHarvester/discovery/onyphe.py` | python | 253 | Yes |
| `theHarvester/discovery/otilabs.py` | python | 102 | Yes |
| `theHarvester/discovery/otxsearch.py` | python | 102 | Yes |
| `theHarvester/discovery/outcrawlsearch.py` | python | 157 | Yes |
| `theHarvester/discovery/pentesttools.py` | python | 143 | Yes |
| `theHarvester/discovery/profundis.py` | python | 93 | Yes |
| `theHarvester/discovery/projectdiscovery.py` | python | 103 | Yes |
| `theHarvester/discovery/provider_response.py` | python | 19 | Yes |
| `theHarvester/discovery/rapiddns.py` | python | 99 | Yes |
| `theHarvester/discovery/robtex.py` | python | 101 | Yes |
| `theHarvester/discovery/rocketreach.py` | python | 136 | Yes |
| `theHarvester/discovery/scanmalware.py` | python | 188 | Yes |
| `theHarvester/discovery/search_dehashed.py` | python | 136 | Yes |
| `theHarvester/discovery/search_dnsdumpster.py` | python | 105 | Yes |
| `theHarvester/discovery/searchhunterhow.py` | python | 115 | Yes |
| `theHarvester/discovery/securityscorecard.py` | python | 164 | Yes |
| `theHarvester/discovery/securitytrailssearch.py` | python | 110 | Yes |
| `theHarvester/discovery/serplysearch.py` | python | 164 | Yes |
| `theHarvester/discovery/sherlockeye.py` | python | 169 | Yes |
| `theHarvester/discovery/shodan_internetdb.py` | python | 106 | Yes |
| `theHarvester/discovery/shodanct.py` | python | 61 | Yes |
| `theHarvester/discovery/shodansearch.py` | python | 576 | Yes |
| `theHarvester/discovery/sourcegraph.py` | python | 220 | Yes |
| `theHarvester/discovery/subdomainapi.py` | python | 75 | Yes |
| `theHarvester/discovery/subdomaincenter.py` | python | 54 | Yes |
| `theHarvester/discovery/subdomainfinderc99.py` | python | 90 | Yes |
| `theHarvester/discovery/takeover.py` | python | 640 | Yes |
| `theHarvester/discovery/thc.py` | python | 89 | Yes |
| `theHarvester/discovery/tombasearch.py` | python | 149 | Yes |
| `theHarvester/discovery/urlscan.py` | python | 209 | Yes |
| `theHarvester/discovery/virustotal.py` | python | 127 | Yes |
| `theHarvester/discovery/waybackarchive.py` | python | 158 | Yes |
| `theHarvester/discovery/whoisxml.py` | python | 84 | Yes |
| `theHarvester/discovery/windvane.py` | python | 264 | Yes |
| `theHarvester/discovery/yahoosearch.py` | python | 101 | Yes |
| `theHarvester/discovery/zoomeyesearch.py` | python | 235 | Yes |
| `theHarvester/harvestview.py` | python | 49 | Yes |
| `theHarvester/lib/__init__.py` | python | 1 | Yes |
| `theHarvester/lib/active_evidence.py` | python | 157 | Yes |
| `theHarvester/lib/api/__init__.py` | python | 0 | Yes |
| `theHarvester/lib/api/api.py` | python | 65 | Yes |
| `theHarvester/lib/api/auth.py` | python | 61 | Yes |
| `theHarvester/lib/api/harvestview.py` | python | 77 | Yes |
| `theHarvester/lib/api/run_artifacts.py` | python | 67 | Yes |
| `theHarvester/lib/api/run_evidence.py` | python | 296 | Yes |
| `theHarvester/lib/api/run_models.py` | python | 724 | Yes |
| `theHarvester/lib/api/run_projection.py` | python | 104 | Yes |
| `theHarvester/lib/api/run_store.py` | python | 620 | Yes |
| `theHarvester/lib/api/run_worker.py` | python | 513 | Yes |
| `theHarvester/lib/api/runs.py` | python | 318 | Yes |
| `theHarvester/lib/api/runtime.py` | python | 50 | Yes |
| `theHarvester/lib/api/schedule_models.py` | python | 279 | Yes |
| `theHarvester/lib/api/schedule_service.py` | python | 351 | Yes |
| `theHarvester/lib/api/schedule_store.py` | python | 612 | Yes |
| `theHarvester/lib/api/schedules.py` | python | 192 | Yes |
| `theHarvester/lib/api/static/.gitkeep` | other | 0 | No |
| `theHarvester/lib/api/static/harvestview/app.css` | other | 905 | No |
| `theHarvester/lib/api/static/harvestview/app.js` | javascript | 1527 | Yes |
| `theHarvester/lib/api/static/harvestview/index.html` | other | 461 | No |
| `theHarvester/lib/api/static/harvestview/logo.webp` | other | 196 | No |
| `theHarvester/lib/api/static/harvestview/schedules.css` | other | 208 | No |
| `theHarvester/lib/api/static/harvestview/schedules.html` | other | 212 | No |
| `theHarvester/lib/api/static/harvestview/schedules.js` | javascript | 776 | Yes |
| `theHarvester/lib/asn_attribution.py` | python | 165 | Yes |
| `theHarvester/lib/cancellation.py` | python | 31 | Yes |
| `theHarvester/lib/completed_result.py` | python | 566 | Yes |
| `theHarvester/lib/configuration.py` | python | 34 | Yes |
| `theHarvester/lib/core.py` | python | 1209 | Yes |
| `theHarvester/lib/database.py` | python | 1372 | Yes |
| `theHarvester/lib/dns_consensus.py` | python | 328 | Yes |
| `theHarvester/lib/enumeration.py` | python | 109 | Yes |
| `theHarvester/lib/evidence_types.py` | python | 37 | Yes |
| `theHarvester/lib/hostchecker.py` | python | 235 | Yes |
| `theHarvester/lib/hostname_comparison.py` | python | 168 | Yes |
| `theHarvester/lib/hostnames.py` | python | 42 | Yes |
| `theHarvester/lib/network_evidence.py` | python | 403 | Yes |
| `theHarvester/lib/output.py` | python | 68 | Yes |
| `theHarvester/lib/recursive_dns.py` | python | 244 | Yes |
| `theHarvester/lib/resolver_selection.py` | python | 27 | Yes |
| `theHarvester/lib/result_values.py` | python | 63 | Yes |
| `theHarvester/lib/routeviews.py` | python | 510 | Yes |
| `theHarvester/lib/shodan_evidence.py` | python | 221 | Yes |
| `theHarvester/lib/source_catalog.py` | python | 258 | Yes |
| `theHarvester/lib/source_execution.py` | python | 18 | Yes |
| `theHarvester/lib/source_runner.py` | python | 540 | Yes |
| `theHarvester/lib/takeover_evidence.py` | python | 418 | Yes |
| `theHarvester/lib/takeover_rules.py` | python | 244 | Yes |
| `theHarvester/lib/target_identity.py` | python | 44 | Yes |
| `theHarvester/lib/virtual_host.py` | python | 1163 | Yes |
| `theHarvester/parsers/__init__.py` | python | 0 | Yes |
| `theHarvester/parsers/intelxparser.py` | python | 31 | Yes |
| `theHarvester/parsers/myparser.py` | python | 59 | Yes |
| `theHarvester/saved_run_report.py` | python | 365 | Yes |
| `theHarvester/screenshot/__init__.py` | python | 0 | Yes |
| `theHarvester/screenshot/screenshot.py` | python | 279 | Yes |
| `theHarvester/theHarvester.py` | python | 36 | Yes |
| `uv.lock` | other | 1271 | No |
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

## Issues (295)

### 🔴 HIGH: TM2

**Location:** `.github/workflows/theHarvester.yml:42`  
**Confidence:** 75%  

**Message:** Chaining Abuse

**Remediation:** Limit tool chaining depth and validate the output of each tool before passing it to the next\. Require explicit user approval for multi\-step chains\.

---

### 🔴 HIGH: PE3

**Location:** `CHANGELOG.md:61`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `docs/wiki/Configuration-and-API-Keys.md:50`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/discovery/test_censys.py:22`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/discovery/test_censys.py:33`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `theHarvester/discovery/censysearch.py:21`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: E2

**Location:** `tests/e2e/conftest.py:152`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/lib/test_configuration_contract.py:56`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: PE3

**Location:** `tests/test_docker.py:65`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/test_security.py:249`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_logging.py:136`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_logging.py:196`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: PE3

**Location:** `tests/test_security.py:45`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/test_security.py:200`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/test_security.py:202`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/test_security.py:206`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `tests/test_security.py:280`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: TM1

**Location:** `tests/test_security.py:63`  
**Confidence:** 100%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `tests/test_security.py:225`  
**Confidence:** 100%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `tests/test_security.py:63`  
**Confidence:** 100%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `tests/test_security.py:63`  
**Confidence:** 95%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `tests/test_security.py:225`  
**Confidence:** 95%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM2

**Location:** `tests/test_security.py:63`  
**Confidence:** 75%  

**Message:** Chaining Abuse

**Remediation:** Limit tool chaining depth and validate the output of each tool before passing it to the next\. Require explicit user approval for multi\-step chains\.

---

### 🔴 HIGH: TM2

**Location:** `tests/test_security.py:225`  
**Confidence:** 75%  

**Message:** Chaining Abuse

**Remediation:** Limit tool chaining depth and validate the output of each tool before passing it to the next\. Require explicit user approval for multi\-step chains\.

---

### 🔴 HIGH: TM1

**Location:** `tests/test_security.py:225`  
**Confidence:** 100%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `theHarvester/data/wordlists/api_endpoints.txt:83`  
**Confidence:** 80%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `theHarvester/data/wordlists/api_endpoints.txt:145`  
**Confidence:** 80%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `theHarvester/data/wordlists/api_endpoints.txt:194`  
**Confidence:** 80%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `theHarvester/data/wordlists/api_endpoints.txt:687`  
**Confidence:** 80%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `theHarvester/data/wordlists/api_endpoints.txt:702`  
**Confidence:** 80%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `theHarvester/data/wordlists/api_endpoints.txt:712`  
**Confidence:** 80%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `theHarvester/data/wordlists/api_endpoints.txt:719`  
**Confidence:** 80%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `theHarvester/data/wordlists/api_endpoints.txt:727`  
**Confidence:** 80%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `theHarvester/data/wordlists/api_endpoints.txt:732`  
**Confidence:** 80%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `theHarvester/data/wordlists/api_endpoints.txt:738`  
**Confidence:** 80%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `theHarvester/data/wordlists/api_endpoints.txt:744`  
**Confidence:** 80%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `theHarvester/data/wordlists/api_endpoints.txt:748`  
**Confidence:** 80%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `theHarvester/data/wordlists/api_endpoints.txt:753`  
**Confidence:** 80%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `theHarvester/data/wordlists/api_endpoints.txt:764`  
**Confidence:** 80%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `theHarvester/data/wordlists/api_endpoints.txt:776`  
**Confidence:** 80%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: TM1

**Location:** `theHarvester/data/wordlists/api_endpoints.txt:805`  
**Confidence:** 80%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🟡 MEDIUM: RP1

**Location:** `.github/workflows/dockerci.yml:23`  
**Confidence:** 75%  

**Message:** Docker image referenced without tag or digest: 'docker run \-\-rm'\.

**Remediation:** Pin the image: image:tag or image@sha256:abc123

---

### 🟡 MEDIUM: E1

**Location:** `.github/workflows/harvestview-container.yml:54`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: PE2

**Location:** `.github/workflows/theHarvester.yml:43`  
**Confidence:** 70%  

**Message:** Sudo/Root Execution

**Remediation:** Avoid sudo/root unless strictly required\. Prefer least\-privilege patterns\. If elevation is needed, document the justification and scope\.

---

### 🟡 MEDIUM: PE2

**Location:** `.github/workflows/theHarvester.yml:44`  
**Confidence:** 70%  

**Message:** Sudo/Root Execution

**Remediation:** Avoid sudo/root unless strictly required\. Prefer least\-privilege patterns\. If elevation is needed, document the justification and scope\.

---

### 🟡 MEDIUM: PE2

**Location:** `.github/workflows/theHarvester.yml:45`  
**Confidence:** 70%  

**Message:** Sudo/Root Execution

**Remediation:** Avoid sudo/root unless strictly required\. Prefer least\-privilege patterns\. If elevation is needed, document the justification and scope\.

---

### 🟡 MEDIUM: PE2

**Location:** `docs/wiki/Installation.md:10`  
**Confidence:** 70%  

**Message:** Sudo/Root Execution

**Remediation:** Avoid sudo/root unless strictly required\. Prefer least\-privilege patterns\. If elevation is needed, document the justification and scope\.

---

### 🟡 MEDIUM: PE2

**Location:** `docs/wiki/Installation.md:11`  
**Confidence:** 70%  

**Message:** Sudo/Root Execution

**Remediation:** Avoid sudo/root unless strictly required\. Prefer least\-privilege patterns\. If elevation is needed, document the justification and scope\.

---

### 🟡 MEDIUM: E1

**Location:** `docs/wiki/Moving-from-4.11-to-5.0.md:61`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `docs/wiki/Moving-from-4.11-to-5.0.md:81`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `docs/wiki/Rest-API.md:80`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `docs/wiki/Rest-API.md:110`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `docs/wiki/Rest-API.md:182`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `docs/wiki/Rest-API.md:231`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `docs/wiki/Rest-API.md:246`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/discovery/test_api_endpoints.py:46–66`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: TM3

**Location:** `tests/discovery/test_api_endpoints.py:360`  
**Confidence:** 80%  

**Message:** Unsafe Defaults

**Remediation:** Override unsafe defaults with secure settings \(verify=True, auth required, restrictive permissions\)\. Review and harden all tool configurations\.

---

### 🟡 MEDIUM: TM3

**Location:** `tests/discovery/test_api_endpoints.py:425`  
**Confidence:** 80%  

**Message:** Unsafe Defaults

**Remediation:** Override unsafe defaults with secure settings \(verify=True, auth required, restrictive permissions\)\. Review and harden all tool configurations\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:14`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:26`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:31`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:87`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:100`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:139`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:196`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:241`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:251`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:264`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:278`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:288`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:289`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:303`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:318`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:329`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:330`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:344`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:359`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:370`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:371`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:385`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:394`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:401`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:443`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:455`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:456`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:497`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:567`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:604`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:613`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:715`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:754`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:755`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:756`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:757`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:758`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:815`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:849`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:936`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `theHarvester/discovery/apisguru.py:24`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `README.md:340`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:43`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:45`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:81`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:116`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:186`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:225`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:474`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:517`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:768`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:769`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:770`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:771`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_arquivo.py:28`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_commoncrawl.py:47`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_commoncrawl.py:101`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_commoncrawl.py:447`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_commoncrawl.py:518`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_commoncrawl.py:552`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_commoncrawl.py:581`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_sherlockeye.py:111`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_sherlockeye.py:225`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_urlscan.py:139`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_waybackarchive.py:55`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_waybackarchive.py:103`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_waybackarchive.py:125`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_waybackarchive.py:217`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_waybackarchive.py:341`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_zoomeyesearch.py:256`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_zoomeyesearch.py:266`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_apisguru.py:185`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_arquivo.py:26`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_builtwith.py:70`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `theHarvester/discovery/builtwith.py:16`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_censys.py:101`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_censys.py:102`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `theHarvester/discovery/censysearch.py:15`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: EA4

**Location:** `tests/discovery/test_censys.py:341`  
**Confidence:** 75%  

**Message:** Unbounded Resource Access

**Remediation:** Set explicit rate limits, timeouts, and resource quotas for API calls, file operations, and compute\. Implement circuit breakers for runaway loops\.

---

### 🟡 MEDIUM: EA4

**Location:** `tests/discovery/test_commoncrawl.py:453`  
**Confidence:** 75%  

**Message:** Unbounded Resource Access

**Remediation:** Set explicit rate limits, timeouts, and resource quotas for API calls, file operations, and compute\. Implement circuit breakers for runaway loops\.

---

### 🟡 MEDIUM: EA4

**Location:** `tests/discovery/test_commoncrawl.py:470`  
**Confidence:** 75%  

**Message:** Unbounded Resource Access

**Remediation:** Set explicit rate limits, timeouts, and resource quotas for API calls, file operations, and compute\. Implement circuit breakers for runaway loops\.

---

### 🟡 MEDIUM: EA4

**Location:** `tests/discovery/test_waybackarchive.py:244`  
**Confidence:** 75%  

**Message:** Unbounded Resource Access

**Remediation:** Set explicit rate limits, timeouts, and resource quotas for API calls, file operations, and compute\. Implement circuit breakers for runaway loops\.

---

### 🟡 MEDIUM: EA4

**Location:** `tests/e2e/conftest.py:63`  
**Confidence:** 75%  

**Message:** Unbounded Resource Access

**Remediation:** Set explicit rate limits, timeouts, and resource quotas for API calls, file operations, and compute\. Implement circuit breakers for runaway loops\.

---

### 🟡 MEDIUM: EA4

**Location:** `theHarvester/lib/api/run_worker.py:378`  
**Confidence:** 75%  

**Message:** Unbounded Resource Access

**Remediation:** Set explicit rate limits, timeouts, and resource quotas for API calls, file operations, and compute\. Implement circuit breakers for runaway loops\.

---

### 🟡 MEDIUM: EA4

**Location:** `theHarvester/lib/api/run_worker.py:394`  
**Confidence:** 75%  

**Message:** Unbounded Resource Access

**Remediation:** Set explicit rate limits, timeouts, and resource quotas for API calls, file operations, and compute\. Implement circuit breakers for runaway loops\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_certspotter.py:27`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `theHarvester/discovery/certspottersearch.py:28`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_commoncrawl.py:97`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_criminalip.py:95`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_criminalip.py:119`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_criminalip.py:120`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_criminalip.py:121`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `theHarvester/discovery/criminalip.py:120`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `theHarvester/discovery/criminalip.py:147`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `theHarvester/discovery/criminalip.py:190`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_dnsdb.py:74`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `theHarvester/discovery/dnsdb.py:22`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_duckduckgo.py:65`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `theHarvester/discovery/duckduckgosearch.py:86`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_githubcode_contract.py:91`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_githubcode_contract.py:92`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_githubcode_contract.py:110`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_githubcode_contract.py:111`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_githubcode_contract.py:129`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_githubcode_contract.py:130`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_githubcode_contract.py:138`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_githubcode_contract.py:190`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_githubcode_contract.py:211`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_githubcode_contract.py:212`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_githubcode_contract.py:221`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_githubcode_contract.py:231`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_githubcode_contract.py:235`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_githubcode_contract.py:243`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_githubcode_contract.py:244`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_githubcode_contract.py:261`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_githubcode_contract.py:269`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_githubcode_contract.py:277`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_githubcode_contract.py:278`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_hackertarget_apikey.py:43`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_hackertarget_apikey.py:44`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_hackertarget_apikey.py:74`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_hackertarget_apikey.py:75`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_hackertarget_apikey.py:238`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_hackertarget_apikey.py:239`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_hackertarget_apikey.py:271`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_hunterhow.py:72`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `theHarvester/discovery/searchhunterhow.py:67`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_huntersearch.py:141`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_huntersearch.py:142`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_huntersearch.py:143`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_huntersearch.py:144`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_huntersearch.py:222`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_huntersearch.py:223`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_huntersearch.py:321`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_huntersearch.py:322`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_huntersearch.py:323`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `theHarvester/discovery/huntersearch.py:25`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `theHarvester/discovery/huntersearch.py:54`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `theHarvester/discovery/huntersearch.py:80`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `theHarvester/discovery/huntersearch.py:102`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_mojeek.py:390`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_mojeek.py:391`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_mojeek.py:392`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_mojeek.py:638`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_mojeek.py:645`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_mojeek.py:695`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_outcrawl.py:337`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_outcrawl.py:338`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `theHarvester/discovery/outcrawlsearch.py:41`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_rocketreach.py:87`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_rocketreach.py:88`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `theHarvester/discovery/rocketreach.py:20`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_securityscorecard.py:66`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_securityscorecard.py:71`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_securityscorecard.py:72`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_securityscorecard.py:73`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_securityscorecard.py:74`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_securitytrails.py:62`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_securitytrails.py:63`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `theHarvester/discovery/securitytrailssearch.py:19`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_shodan_engine.py:83`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_shodan_engine.py:286`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_shodan_engine.py:287`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_shodan_engine.py:390`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/test_main.py:3645`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `theHarvester/discovery/shodansearch.py:38`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `README.md:284`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_subdomainapi.py:47`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/test_readme.py:77`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `theHarvester/discovery/subdomainapi.py:15`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_subdomaincenter.py:44`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `theHarvester/discovery/subdomaincenter.py:14`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_tombasearch.py:157`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_tombasearch.py:158`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_tombasearch.py:159`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_tombasearch.py:160`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_tombasearch.py:161`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_tombasearch.py:205`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_tombasearch.py:206`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_tombasearch.py:207`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_tombasearch.py:257`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_tombasearch.py:289`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_tombasearch.py:290`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_tombasearch.py:400`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_tombasearch.py:401`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_tombasearch.py:402`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/discovery/test_tombasearch.py:403`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `theHarvester/discovery/tombasearch.py:56`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `theHarvester/discovery/tombasearch.py:71`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `theHarvester/discovery/tombasearch.py:92`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/e2e/conftest.py:38–56`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/lib/test_configuration_contract.py:59–66`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: TM3

**Location:** `tests/lib/test_core.py:595`  
**Confidence:** 75%  

**Message:** Unsafe Defaults

**Remediation:** Override unsafe defaults with secure settings \(verify=True, auth required, restrictive permissions\)\. Review and harden all tool configurations\.

---

### 🟡 MEDIUM: EA4

**Location:** `tests/lib/test_core.py:1130`  
**Confidence:** 75%  

**Message:** Unbounded Resource Access

**Remediation:** Set explicit rate limits, timeouts, and resource quotas for API calls, file operations, and compute\. Implement circuit breakers for runaway loops\.

---

### 🟡 MEDIUM: EA4

**Location:** `tests/lib/test_core.py:1158`  
**Confidence:** 75%  

**Message:** Unbounded Resource Access

**Remediation:** Set explicit rate limits, timeouts, and resource quotas for API calls, file operations, and compute\. Implement circuit breakers for runaway loops\.

---

### 🟡 MEDIUM: EA4

**Location:** `tests/lib/test_core.py:1180`  
**Confidence:** 75%  

**Message:** Unbounded Resource Access

**Remediation:** Set explicit rate limits, timeouts, and resource quotas for API calls, file operations, and compute\. Implement circuit breakers for runaway loops\.

---

### 🟡 MEDIUM: EA4

**Location:** `theHarvester/discovery/thc.py:39`  
**Confidence:** 75%  

**Message:** Unbounded Resource Access

**Remediation:** Set explicit rate limits, timeouts, and resource quotas for API calls, file operations, and compute\. Implement circuit breakers for runaway loops\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/lib/test_routeviews.py:93`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/lib/test_routeviews.py:94`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/lib/test_routeviews.py:114`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/lib/test_routeviews.py:115`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/lib/test_routeviews.py:170`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/lib/test_routeviews.py:193`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/lib/test_routeviews.py:201`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/lib/test_routeviews.py:258`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/lib/test_routeviews.py:309`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/test_main.py:4258`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/lib/test_source_runner.py:262`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/lib/test_source_runner.py:262`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `tests/lib/test_source_runner.py:278`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/lib/test_virtual_host.py:79–99`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_logging.py:16–21`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_logging.py:138`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_logging.py:198`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_logging.py:139`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_logging.py:140`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_logging.py:199`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_release_artifacts.py:23–27`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_runtime_dependencies.py:73–78`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: E1

**Location:** `theHarvester/discovery/bravesearch.py:41`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `theHarvester/discovery/dymosearch.py:26`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `theHarvester/discovery/profundis.py:13`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `theHarvester/discovery/search_dehashed.py:25`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `theHarvester/discovery/serplysearch.py:46`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `theHarvester/discovery/sherlockeye.py:24`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `theHarvester/discovery/zoomeyesearch.py:49`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟢 LOW: TM2

**Location:** `Dockerfile:40`  
**Confidence:** 15%  

**Message:** Chaining Abuse

**Remediation:** Limit tool chaining depth and validate the output of each tool before passing it to the next\. Require explicit user approval for multi\-step chains\.

---

### 🟢 LOW: TM1

**Location:** `Dockerfile:41`  
**Confidence:** 15%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🟢 LOW: TM1

**Location:** `Dockerfile:41`  
**Confidence:** 15%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🟢 LOW: TM2

**Location:** `Dockerfile:41`  
**Confidence:** 15%  

**Message:** Chaining Abuse

**Remediation:** Limit tool chaining depth and validate the output of each tool before passing it to the next\. Require explicit user approval for multi\-step chains\.

---

### 🟢 LOW: EA3

**Location:** `LICENSE:69`  
**Confidence:** 70%  

**Message:** Scope Creep

**Remediation:** Limit the skill's scope to its documented purpose\. Remove instructions that enable the agent to perform actions outside its stated functionality\.

---

### 🟢 LOW: EA3

**Location:** `LICENSE:87`  
**Confidence:** 70%  

**Message:** Scope Creep

**Remediation:** Limit the skill's scope to its documented purpose\. Remove instructions that enable the agent to perform actions outside its stated functionality\.

---

### 🟢 LOW: EA3

**Location:** `LICENSE:89`  
**Confidence:** 70%  

**Message:** Scope Creep

**Remediation:** Limit the skill's scope to its documented purpose\. Remove instructions that enable the agent to perform actions outside its stated functionality\.

---

### 🟢 LOW: AST7

**Location:** `tests/lib/test_configuration_contract.py:152`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `tests/lib/test_core.py:404`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `theHarvester/lib/source_runner.py:266`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `theHarvester/lib/source_runner.py:271`  
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
| Coverage | 84\.9% |
| Fully inspected | 282 |
| Partially inspected | 50 |
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
| binary\_content | `theHarvester-logo.png` | Binary content is unsupported by this analyzer\. |
| binary\_content | `theHarvester-logo.webp` | Binary content is unsupported by this analyzer\. |
| binary\_content | `theHarvester/lib/api/static/harvestview/logo.webp` | Binary content is unsupported by this analyzer\. |

### Ledger Exceptions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| python\_source\_ambiguous | `bin/harvestview` | Python execution intent depends on runtime or platform\-specific shebang semantics\. |
| python\_source\_ambiguous | `bin/harvestview` | Python execution intent depends on runtime or platform\-specific shebang semantics\. |
| python\_source\_ambiguous | `bin/harvestview` | Python execution intent depends on runtime or platform\-specific shebang semantics\. |
| python\_source\_ambiguous | `bin/theHarvester` | Python execution intent depends on runtime or platform\-specific shebang semantics\. |
| python\_source\_ambiguous | `bin/theHarvester` | Python execution intent depends on runtime or platform\-specific shebang semantics\. |
| python\_source\_ambiguous | `bin/theHarvester` | Python execution intent depends on runtime or platform\-specific shebang semantics\. |
| static\_parse\_limit | `tests/discovery/test_apisguru.py` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| static\_parse\_limit | `tests/lib/test_source_runner.py` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| static\_parse\_limit | `tests/test_main.py` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| syntax\_error | `theHarvester/__main__.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/__main__.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/api_endpoints.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/api_endpoints.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/apisguru.py` | Python source could not be parsed\. |
| obfuscated\_instruction\_text | `theHarvester/discovery/apisguru.py` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |
| syntax\_error | `theHarvester/discovery/apisguru.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/arquivo.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/arquivo.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/bravesearch.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/bravesearch.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/bufferoverun.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/bufferoverun.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/builtwith.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/builtwith.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/censysearch.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/censysearch.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/commoncrawl.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/commoncrawl.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/darkeye.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/darkeye.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/dnsdb.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/dnsdb.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/githubcode.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/githubcode.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/haveibeenpwned.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/haveibeenpwned.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/hibpverified.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/hibpverified.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/hudsonrocksearch.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/hudsonrocksearch.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/huntersearch.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/huntersearch.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/intelxsearch.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/intelxsearch.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/leakix.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/leakix.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/otxsearch.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/otxsearch.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/outcrawlsearch.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/outcrawlsearch.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/pentesttools.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/pentesttools.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/profundis.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/profundis.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/robtex.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/robtex.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/rocketreach.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/rocketreach.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/search_dehashed.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/search_dehashed.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/search_dnsdumpster.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/search_dnsdumpster.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/serplysearch.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/serplysearch.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/shodan_internetdb.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/shodan_internetdb.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/shodansearch.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/shodansearch.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/sourcegraph.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/sourcegraph.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/subdomaincenter.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/subdomaincenter.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/takeover.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/takeover.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/tombasearch.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/tombasearch.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/windvane.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/discovery/windvane.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/lib/api/harvestview.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/lib/api/harvestview.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/lib/api/run_store.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/lib/api/run_store.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/lib/api/run_worker.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/lib/api/run_worker.py` | Python source could not be parsed\. |
| static\_parse\_limit | `theHarvester/lib/api/static/harvestview/app.js` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| static\_parse\_limit | `theHarvester/lib/api/static/harvestview/index.html` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| obfuscated\_instruction\_text | `theHarvester/lib/api/static/harvestview/schedules.js` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |
| static\_parse\_limit | `theHarvester/lib/api/static/harvestview/schedules.js` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| syntax\_error | `theHarvester/lib/core.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/lib/core.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/lib/database.py` | Python source could not be parsed\. |
| obfuscated\_instruction\_text | `theHarvester/lib/database.py` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |
| syntax\_error | `theHarvester/lib/database.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/lib/hostchecker.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/lib/hostchecker.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/lib/routeviews.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/lib/routeviews.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/lib/virtual_host.py` | Python source could not be parsed\. |
| syntax\_error | `theHarvester/lib/virtual_host.py` | Python source could not be parsed\. |

### Analyzer Statuses

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| completed | `artifact_integrity` |  |
| degraded | `behavioral_ast` |  |
| degraded | `behavioral_taint_tracking` |  |
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

- **Executable Scripts:** Yes

*Generated by SkillSpector v2.12.0*
