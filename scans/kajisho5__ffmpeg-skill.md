# Scans for kajisho5/ffmpeg-skill @ 1ce2c18

<!-- ===== (root) ===== -->
# SkillSpector Security Report

**Skill:** ffmpeg\-skill  
**Source:** `F:\Github Repos\repos\kajisho5__ffmpeg-skill`  
**Scanned:** 2026-11-03 15:18:48 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 100/100 |
| Severity | CRITICAL |
| Recommendation | DO NOT INSTALL |

## Components (385)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `.claude-plugin/marketplace.json` | json | 15 | No |
| `.claude-plugin/plugin.json` | json | 34 | No |
| `.claude/settings.json` | json | 15 | No |
| `.claude/skills/build-artifacts/SKILL.md` | markdown | 182 | No |
| `.claude/skills/ci-pipeline-synthesizer/SKILL.md` | markdown | 128 | No |
| `.claude/skills/ci-pipeline-synthesizer/assets/github-actions-go.yml` | yaml | 34 | No |
| `.claude/skills/ci-pipeline-synthesizer/assets/github-actions-nodejs.yml` | yaml | 34 | No |
| `.claude/skills/ci-pipeline-synthesizer/assets/github-actions-python.yml` | yaml | 36 | No |
| `.claude/skills/ci-pipeline-synthesizer/assets/github-actions-rust.yml` | yaml | 48 | No |
| `.claude/skills/code-review/SKILL.md` | markdown | 159 | No |
| `.claude/skills/code-review/references/result-honesty.md` | markdown | 93 | No |
| `.claude/skills/code-review/references/review-checklist.md` | markdown | 86 | No |
| `.claude/skills/code-review/references/surfaces.md` | markdown | 63 | No |
| `.claude/skills/concurrent-branches/SKILL.md` | markdown | 244 | No |
| `.claude/skills/cross-surface-changes/SKILL.md` | markdown | 227 | No |
| `.claude/skills/defect-reports/SKILL.md` | markdown | 222 | No |
| `.claude/skills/destructive-operations/SKILL.md` | markdown | 211 | No |
| `.claude/skills/git-hygiene/SKILL.md` | markdown | 216 | No |
| `.claude/skills/github-actions/SKILL.md` | markdown | 317 | No |
| `.claude/skills/mcp-server-design/SKILL.md` | markdown | 286 | No |
| `.claude/skills/release-management/SKILL.md` | markdown | 147 | No |
| `.claude/skills/reproducing-ci-locally/SKILL.md` | markdown | 250 | No |
| `.claude/skills/verifying-external-behavior/SKILL.md` | markdown | 217 | No |
| `.git/config` | other | 13 | No |
| `.github/FUNDING.yml` | yaml | 1 | No |
| `.github/ISSUE_TEMPLATE/bug_report.md` | markdown | 31 | No |
| `.github/ISSUE_TEMPLATE/config.yml` | yaml | 5 | No |
| `.github/ISSUE_TEMPLATE/feature_request.md` | markdown | 20 | No |
| `.github/dependabot.yml` | yaml | 15 | No |
| `.github/pull_request_template.md` | markdown | 12 | No |
| `.github/release-drafter.yml` | yaml | 77 | No |
| `.github/scripts/build_pages.py` | python | 189 | Yes |
| `.github/scripts/bump_contract_md.py` | python | 55 | Yes |
| `.github/scripts/bump_roadmap_md.py` | python | 58 | Yes |
| `.github/scripts/design_decisions_index.py` | python | 62 | Yes |
| `.github/scripts/pages_layout.html` | other | 70 | No |
| `.github/scripts/resolve_version.py` | python | 126 | Yes |
| `.github/workflows/ci.yml` | yaml | 161 | No |
| `.github/workflows/codeql.yml` | yaml | 42 | No |
| `.github/workflows/dependabot-auto-merge.yml` | yaml | 37 | No |
| `.github/workflows/pages.yml` | yaml | 52 | No |
| `.github/workflows/release-drafter.yml` | yaml | 53 | No |
| `.github/workflows/release.yml` | yaml | 313 | No |
| `.gitignore` | other | 28 | No |
| `.npmignore` | other | 8 | No |
| `.snyk` | other | 11 | No |
| `AGENTS.md` | markdown | 14 | No |
| `CHANGELOG.md` | markdown | 3081 | No |
| `CODE_OF_CONDUCT.md` | markdown | 9 | No |
| `CONTRIBUTING.md` | markdown | 111 | No |
| `LICENSE` | other | 21 | No |
| `README.md` | markdown | 679 | No |
| `SECURITY.md` | markdown | 22 | No |
| `SKILL.md` | markdown | 209 | No |
| `assets/demo.gif` | other | 47430 | No |
| `assets/icon.png` | other | 15533 | No |
| `assets/logo.png` | other | 9427 | No |
| `assets/social-preview.png` | other | 16638 | No |
| `bin/install.js` | javascript | 222 | Yes |
| `brand/app-icon-dark.png` | other | 2100 | No |
| `brand/app-icon.png` | other | 1871 | No |
| `brand/ffmpeg-skill.icon/Assets/in-out.svg` | other | 1 | Yes |
| `brand/ffmpeg-skill.icon/Assets/playhead.svg` | other | 1 | Yes |
| `brand/ffmpeg-skill.icon/icon.json` | json | 84 | No |
| `brand/logo/ffmpeg-skill-wordmark-black.svg` | other | 1 | Yes |
| `brand/logo/ffmpeg-skill-wordmark-white.svg` | other | 1 | Yes |
| `demos/CI.md` | markdown | 127 | No |
| `demos/build.py` | python | 1947 | Yes |
| `demos/footage/README.md` | markdown | 10 | No |
| `demos/footage/ai_talk.mp4` | other | 5982 | No |
| `demos/footage/ai_talk_en.mp4` | other | 17948 | No |
| `demos/footage/ai_talk_en.words.json` | json | 80 | No |
| `demos/pages_videos.py` | python | 60 | Yes |
| `docs/contract.md` | markdown | 1037 | No |
| `docs/demos.md` | markdown | 822 | No |
| `docs/demos/audiogram.gif` | other | 6682 | No |
| `docs/demos/beats_snap.gif` | other | 255 | No |
| `docs/demos/bgm_ducking.gif` | other | 427 | No |
| `docs/demos/broll_cutaway.gif` | other | 6531 | No |
| `docs/demos/captions_ar.gif` | other | 7388 | No |
| `docs/demos/captions_emoji.gif` | other | 6267 | No |
| `docs/demos/captions_en.gif` | other | 6230 | No |
| `docs/demos/captions_fitsize.gif` | other | 4257 | No |
| `docs/demos/captions_ja.gif` | other | 5687 | No |
| `docs/demos/captions_ko.gif` | other | 7439 | No |
| `docs/demos/captions_multitrack.gif` | other | 6344 | No |
| `docs/demos/captions_phrase.gif` | other | 5670 | No |
| `docs/demos/captions_pop_karaoke.gif` | other | 6355 | No |
| `docs/demos/captions_zh.gif` | other | 7471 | No |
| `docs/demos/color_correct.gif` | other | 7132 | No |
| `docs/demos/color_lut.gif` | other | 6947 | No |
| `docs/demos/contact_sheet.gif` | other | 6587 | No |
| `docs/demos/crop_rect.gif` | other | 4114 | No |
| `docs/demos/cropdetect_crop.gif` | other | 7019 | No |
| `docs/demos/cut_accurate.gif` | other | 4635 | No |
| `docs/demos/cut_edit_list.gif` | other | 4744 | No |
| `docs/demos/cut_remove.gif` | other | 4383 | No |
| `docs/demos/deinterlace.gif` | other | 6662 | No |
| `docs/demos/delogo.gif` | other | 7051 | No |
| `docs/demos/denoise.gif` | other | 7282 | No |
| `docs/demos/downmix_51.gif` | other | 395 | No |
| `docs/demos/export_reels.gif` | other | 5673 | No |
| `docs/demos/filler_en.gif` | other | 5206 | No |
| `docs/demos/filler_korean.gif` | other | 233 | No |
| `docs/demos/fit_blur.gif` | other | 4923 | No |
| `docs/demos/freeze_hold.gif` | other | 6205 | No |
| `docs/demos/greenscreen.gif` | other | 6845 | No |
| `docs/demos/grid_2x2.gif` | other | 5888 | No |
| `docs/demos/hdr_tonemap.gif` | other | 5476 | No |
| `docs/demos/insert_still.gif` | other | 7295 | No |
| `docs/demos/join_fade.gif` | other | 5772 | No |
| `docs/demos/join_fadeblack.gif` | other | 5772 | No |
| `docs/demos/logo_overlay.gif` | other | 7552 | No |
| `docs/demos/loop_times.gif` | other | 6010 | No |
| `docs/demos/loudness.gif` | other | 403 | No |
| `docs/demos/lower_third.gif` | other | 6093 | No |
| `docs/demos/lower_third_hindi.gif` | other | 6047 | No |
| `docs/demos/metadata_auto_chapters.gif` | other | 6143 | No |
| `docs/demos/metadata_chapters.gif` | other | 6258 | No |
| `docs/demos/motion_centre_crop.gif` | other | 1211 | No |
| `docs/demos/multicam_switch.gif` | other | 6816 | No |
| `docs/demos/multicam_switch_energy.gif` | other | 6324 | No |
| `docs/demos/overlay_place.gif` | other | 4782 | No |
| `docs/demos/pad_timeline.gif` | other | 7180 | No |
| `docs/demos/proxy.gif` | other | 3955 | No |
| `docs/demos/redact_blur.gif` | other | 5053 | No |
| `docs/demos/reframe_crop.gif` | other | 5285 | No |
| `docs/demos/reframe_pad.gif` | other | 5131 | No |
| `docs/demos/reframe_talk.gif` | other | 5099 | No |
| `docs/demos/render_pip.gif` | other | 6321 | No |
| `docs/demos/render_project.gif` | other | 4968 | No |
| `docs/demos/reverse.gif` | other | 6506 | No |
| `docs/demos/scenes_highlights.gif` | other | 6401 | No |
| `docs/demos/scenes_shots.gif` | other | 6052 | No |
| `docs/demos/sequence_frames.gif` | other | 5473 | No |
| `docs/demos/silence_removal.gif` | other | 5720 | No |
| `docs/demos/silence_speech_aware.gif` | other | 342 | No |
| `docs/demos/speed_up.gif` | other | 5599 | No |
| `docs/demos/speedramp.gif` | other | 3834 | No |
| `docs/demos/sphere_flat.gif` | other | 5671 | No |
| `docs/demos/stabilize.gif` | other | 5380 | No |
| `docs/demos/straighten.gif` | other | 3740 | No |
| `docs/demos/sync_mic.gif` | other | 351 | No |
| `docs/demos/template_tiktok.gif` | other | 5726 | No |
| `docs/demos/title_card.gif` | other | 3306 | No |
| `docs/demos/waveform_render.gif` | other | 4855 | No |
| `docs/design-decisions.md` | markdown | 2483 | No |
| `docs/roadmap.md` | markdown | 687 | No |
| `evals/README.md` | markdown | 297 | No |
| `evals/agent_prompts.json` | json | 14 | No |
| `evals/agent_prompts_24.json` | json | 1122 | No |
| `evals/agent_prompts_25.json` | json | 102 | No |
| `evals/agent_prompts_26.json` | json | 59 | No |
| `evals/agent_prompts_audio.json` | json | 62 | No |
| `evals/agent_prompts_audio2.json` | json | 62 | No |
| `evals/agent_prompts_exec.json` | json | 110 | No |
| `evals/contract/README.md` | markdown | 18 | No |
| `evals/contract/check.py` | python | 72 | Yes |
| `evals/contract/questions.json` | json | 12 | No |
| `evals/grade_runs.py` | python | 32 | Yes |
| `evals/grade_runs_24.py` | python | 327 | Yes |
| `evals/grade_runs_25.py` | python | 154 | Yes |
| `evals/results/audio-2.json` | json | 21 | No |
| `evals/results/audio-only-1.json` | json | 22 | No |
| `evals/results/contract-2026-09-04.json` | json | 30 | No |
| `evals/results/corpus-2026-09-13-1.10.0.md` | markdown | 158 | No |
| `evals/results/exec-1.json` | json | 27 | No |
| `evals/results/iteration-1.json` | json | 34 | No |
| `evals/results/iteration-10-independent-grades.json` | json | 612 | No |
| `evals/results/iteration-10.json` | json | 132 | No |
| `evals/results/iteration-11-independent-grades.json` | json | 266 | No |
| `evals/results/iteration-11.json` | json | 295 | No |
| `evals/results/iteration-12-independent-grades.json` | json | 81 | No |
| `evals/results/iteration-12.json` | json | 304 | No |
| `evals/results/iteration-13-independent-grades.json` | json | 85 | No |
| `evals/results/iteration-13.json` | json | 167 | No |
| `evals/results/iteration-14-independent-grades.json` | json | 120 | No |
| `evals/results/iteration-14.json` | json | 194 | No |
| `evals/results/iteration-15-independent-grades.json` | json | 411 | No |
| `evals/results/iteration-15.json` | json | 203 | No |
| `evals/results/iteration-16-independent-grades.json` | json | 477 | No |
| `evals/results/iteration-16.json` | json | 233 | No |
| `evals/results/iteration-17-independent-grades.json` | json | 201 | No |
| `evals/results/iteration-17.json` | json | 236 | No |
| `evals/results/iteration-18-independent-grades.json` | json | 68 | No |
| `evals/results/iteration-18.json` | json | 233 | No |
| `evals/results/iteration-19-independent-grades.json` | json | 323 | No |
| `evals/results/iteration-19.json` | json | 145 | No |
| `evals/results/iteration-2-4-independent-grades.json` | json | 806 | No |
| `evals/results/iteration-2-4.json` | json | 52 | No |
| `evals/results/iteration-2.json` | json | 33 | No |
| `evals/results/iteration-20-independent-grades.json` | json | 35 | No |
| `evals/results/iteration-20.json` | json | 124 | No |
| `evals/results/iteration-21.json` | json | 69 | No |
| `evals/results/iteration-22.json` | json | 42 | No |
| `evals/results/iteration-23-partial.json` | json | 53 | No |
| `evals/results/iteration-23b.json` | json | 46 | No |
| `evals/results/iteration-23b/ff1/with_skill/outputs/run.md` | markdown | 20 | No |
| `evals/results/iteration-23b/kw1/with_skill/outputs/run.md` | markdown | 34 | No |
| `evals/results/iteration-24.json` | json | 48 | No |
| `evals/results/iteration-24/h1/with_skill/outputs/run.md` | markdown | 44 | No |
| `evals/results/iteration-24/h2/with_skill/outputs/run.md` | markdown | 58 | No |
| `evals/results/iteration-24/ow1/with_skill/outputs/run.md` | markdown | 58 | No |
| `evals/results/iteration-24/ow2/with_skill/outputs/run.md` | markdown | 34 | No |
| `evals/results/iteration-24/q1/with_skill/outputs/run.md` | markdown | 54 | No |
| `evals/results/iteration-25.json` | json | 96 | No |
| `evals/results/iteration-5.json` | json | 56 | No |
| `evals/results/iteration-6.json` | json | 63 | No |
| `evals/results/iteration-7-independent-grades.json` | json | 1217 | No |
| `evals/results/iteration-7.json` | json | 93 | No |
| `evals/results/iteration-8-independent-grades.json` | json | 1264 | No |
| `evals/results/iteration-8.json` | json | 160 | No |
| `evals/results/iteration-9-independent-grades.json` | json | 1320 | No |
| `evals/results/iteration-9.json` | json | 195 | No |
| `evals/results/routing-skill-md-restructure.json` | json | 1286 | No |
| `evals/run.py` | python | 168 | Yes |
| `evals/run_agents_25.sh` | shell | 21 | Yes |
| `evals/tasks.json` | json | 34 | No |
| `evals/trigger/README.md` | markdown | 9 | No |
| `evals/trigger/prompts.json` | json | 332 | No |
| `evals/trigger/prompts_25.json` | json | 17 | No |
| `evals/trigger/results-2026-09-04.json` | json | 209 | No |
| `evals/trigger/results-2026-09-11.json` | json | 231 | No |
| `evals/trigger/results-2026-09-12-it7.json` | json | 231 | No |
| `evals/trigger/results-2026-09-12-it8.json` | json | 33 | No |
| `evals/trigger/results-2026-09-12-it9.json` | json | 33 | No |
| `evals/trigger/results-2026-09-12.json` | json | 229 | No |
| `evals/trigger/results-2026-09-13-it10.json` | json | 33 | No |
| `evals/trigger/results-2026-09-13-it11.json` | json | 34 | No |
| `evals/trigger/results-2026-09-13-it12.json` | json | 34 | No |
| `evals/trigger/results-2026-09-13-it13.json` | json | 42 | No |
| `evals/trigger/results-2026-09-13-it14.json` | json | 40 | No |
| `evals/trigger/results-2026-09-13-it15.json` | json | 52 | No |
| `evals/trigger/results-2026-09-13-it16.json` | json | 49 | No |
| `evals/trigger/results-2026-09-14-it17.json` | json | 59 | No |
| `evals/trigger/results-2026-09-14-it18.json` | json | 64 | No |
| `evals/trigger/results-2026-09-14-it19.json` | json | 59 | No |
| `evals/trigger/results-2026-09-14-it20.json` | json | 512 | No |
| `evals/trigger/results-2026-09-24-it25.json` | json | 30 | No |
| `evals/trigger/results-2026-10-31.json` | json | 19 | No |
| `evals/write_fixtures.py` | python | 184 | Yes |
| `examples/README.md` | markdown | 257 | No |
| `examples/brand.json` | json | 28 | No |
| `examples/make_demo.sh` | shell | 107 | Yes |
| `mcp/server.py` | python | 281 | Yes |
| `package.json` | json | 69 | No |
| `references/ci-platform-pitfalls.md` | markdown | 213 | No |
| `references/devices.md` | markdown | 24 | No |
| `references/flags.md` | markdown | 16 | No |
| `references/gotchas.md` | markdown | 381 | No |
| `references/process-pitfalls.md` | markdown | 238 | No |
| `references/report.md` | markdown | 43 | No |
| `references/requests.md` | markdown | 95 | No |
| `references/scripts.md` | markdown | 1956 | No |
| `references/timestamps.md` | markdown | 3 | No |
| `references/workflow.md` | markdown | 53 | No |
| `scripts/_ass_overlay.py` | python | 157 | Yes |
| `scripts/_common/__init__.py` | python | 233 | Yes |
| `scripts/_common/asr.py` | python | 1159 | Yes |
| `scripts/_common/color.py` | python | 285 | Yes |
| `scripts/_common/decision.py` | python | 1415 | Yes |
| `scripts/_common/drawtext.py` | python | 279 | Yes |
| `scripts/_common/emit.py` | python | 857 | Yes |
| `scripts/_common/emoji.py` | python | 372 | Yes |
| `scripts/_common/fonts.py` | python | 545 | Yes |
| `scripts/_common/probe.py` | python | 961 | Yes |
| `scripts/_common/runner.py` | python | 1871 | Yes |
| `scripts/_common/text.py` | python | 73 | Yes |
| `scripts/_common/timeline.py` | python | 551 | Yes |
| `scripts/_common/wrap.py` | python | 834 | Yes |
| `scripts/_contract.py` | python | 1993 | Yes |
| `scripts/_platforms.py` | python | 258 | Yes |
| `scripts/audio.py` | python | 428 | Yes |
| `scripts/background.py` | python | 89 | Yes |
| `scripts/batch.py` | python | 739 | Yes |
| `scripts/broll.py` | python | 169 | Yes |
| `scripts/caption.py` | python | 1680 | Yes |
| `scripts/check.py` | python | 464 | Yes |
| `scripts/color.py` | python | 476 | Yes |
| `scripts/crop.py` | python | 81 | Yes |
| `scripts/cropdetect.py` | python | 191 | Yes |
| `scripts/cut.py` | python | 1736 | Yes |
| `scripts/deinterlace.py` | python | 85 | Yes |
| `scripts/denoise.py` | python | 94 | Yes |
| `scripts/export.py` | python | 593 | Yes |
| `scripts/fit.py` | python | 251 | Yes |
| `scripts/freeze.py` | python | 118 | Yes |
| `scripts/graphics.py` | python | 731 | Yes |
| `scripts/grid.py` | python | 170 | Yes |
| `scripts/insert.py` | python | 133 | Yes |
| `scripts/join.py` | python | 818 | Yes |
| `scripts/look.py` | python | 312 | Yes |
| `scripts/loop.py` | python | 166 | Yes |
| `scripts/loudness.py` | python | 215 | Yes |
| `scripts/metadata.py` | python | 275 | Yes |
| `scripts/multicam.py` | python | 343 | Yes |
| `scripts/overlay.py` | python | 500 | Yes |
| `scripts/pad.py` | python | 87 | Yes |
| `scripts/probe.py` | python | 69 | Yes |
| `scripts/proxy.py` | python | 81 | Yes |
| `scripts/redact.py` | python | 128 | Yes |
| `scripts/render.py` | python | 1690 | Yes |
| `scripts/report.py` | python | 301 | Yes |
| `scripts/reverse.py` | python | 61 | Yes |
| `scripts/scenes.py` | python | 308 | Yes |
| `scripts/sequence.py` | python | 153 | Yes |
| `scripts/silence.py` | python | 649 | Yes |
| `scripts/speedramp.py` | python | 129 | Yes |
| `scripts/sphere.py` | python | 126 | Yes |
| `scripts/stabilize.py` | python | 103 | Yes |
| `scripts/straighten.py` | python | 99 | Yes |
| `scripts/sync.py` | python | 431 | Yes |
| `scripts/verify.py` | python | 274 | Yes |
| `scripts/waveform.py` | python | 350 | Yes |
| `site/brand/apple-touch-icon.png` | other | 106 | No |
| `site/brand/favicon.ico` | other | 56 | No |
| `site/brand/favicon.svg` | other | 1 | Yes |
| `site/brand/ffmpeg-skill-horizontal-on-dark.svg` | other | 1 | Yes |
| `site/brand/ffmpeg-skill-symbol-on-dark.svg` | other | 1 | Yes |
| `site/brand/og.png` | other | 2259 | No |
| `site/brand/velisa-horizontal-on-dark.svg` | other | 1 | Yes |
| `site/brand/velisa-horizontal.svg` | other | 1 | Yes |
| `site/index.html` | other | 670 | No |
| `site/media/filler_en.jpg` | other | 1326 | No |
| `site/media/filler_en.mp4` | other | 37739 | No |
| `site/media/reframe_talk.jpg` | other | 778 | No |
| `site/media/reframe_talk.mp4` | other | 31897 | No |
| `templates/audiogram.json` | json | 31 | No |
| `templates/facebook.json` | json | 47 | No |
| `templates/linkedin.json` | json | 47 | No |
| `templates/podcast.json` | json | 22 | No |
| `templates/reels.json` | json | 47 | No |
| `templates/shorts.json` | json | 47 | No |
| `templates/tiktok.json` | json | 47 | No |
| `templates/x.json` | json | 47 | No |
| `templates/youtube-shorts.json` | json | 47 | No |
| `templates/youtube.json` | json | 47 | No |
| `tests/_fixtures.py` | python | 428 | Yes |
| `tests/bench_scenes.py` | python | 107 | Yes |
| `tests/bench_silence.py` | python | 120 | Yes |
| `tests/bench_sync.py` | python | 116 | Yes |
| `tests/bench_vt.py` | python | 220 | Yes |
| `tests/corpus.py` | python | 177 | Yes |
| `tests/fixtures/README.md` | markdown | 28 | No |
| `tests/fixtures/caption_1_16_1_fitsize_off.ass` | other | 18 | No |
| `tests/fixtures/ffmpeg_bsfs_6.1.txt` | text | 46 | No |
| `tests/fixtures/ffmpeg_bsfs_8.1.2_macos.txt` | text | 52 | No |
| `tests/fixtures/ffmpeg_bsfs_9.0.1_windows.txt` | text | 53 | No |
| `tests/fixtures/ffmpeg_encoders_6.1.txt` | text | 233 | No |
| `tests/fixtures/ffmpeg_encoders_6.1_no_aac.txt` | text | 232 | No |
| `tests/fixtures/ffmpeg_encoders_8.1.2_macos.txt` | text | 202 | No |
| `tests/fixtures/ffmpeg_encoders_9.0.1_windows.txt` | text | 231 | No |
| `tests/fixtures/ffmpeg_filters_6.1.txt` | text | 563 | No |
| `tests/fixtures/ffmpeg_filters_7.1_constructed.txt` | text | 563 | No |
| `tests/fixtures/ffmpeg_filters_8.1.2_macos.txt` | text | 489 | No |
| `tests/fixtures/ffmpeg_filters_9.0.1_windows.txt` | text | 535 | No |
| `tests/fixtures/ffmpeg_filters_garbage.txt` | text | 4 | No |
| `tests/fixtures/mcp_tools.json` | json | 1279 | No |
| `tests/release_check.sh` | shell | 110 | Yes |
| `tests/run_parallel.py` | python | 126 | Yes |
| `tests/test_accel.py` | python | 1368 | Yes |
| `tests/test_all.py` | python | 41 | Yes |
| `tests/test_analysis.py` | python | 1394 | Yes |
| `tests/test_asr.py` | python | 1214 | Yes |
| `tests/test_audio.py` | python | 813 | Yes |
| `tests/test_contract.py` | python | 6368 | Yes |
| `tests/test_cut_copy.py` | python | 2041 | Yes |
| `tests/test_delivery.py` | python | 620 | Yes |
| `tests/test_editing.py` | python | 2754 | Yes |
| `tests/test_orchestration.py` | python | 2450 | Yes |
| `tests/test_picture.py` | python | 4902 | Yes |
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

## Issues (444)

### 🔴 HIGH: AR2

**Location:** `.claude/skills/destructive-operations/SKILL.md:21`  
**Confidence:** 85%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: PE3

**Location:** `.claude/skills/git-hygiene/SKILL.md:107`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `.claude/skills/git-hygiene/SKILL.md:183`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: MP3

**Location:** `.claude/skills/mcp-server-design/SKILL.md:102`  
**Confidence:** 80%  

**Message:** Memory Manipulation

**Remediation:** Protect agent memory and state from modification by untrusted content\. Use read\-only memory for critical instructions and validate all state changes\.

---

### 🔴 HIGH: SC9

**Location:** `.github/scripts/build_pages.py:1`  
**Confidence:** 100%  

**Message:** Executable content is concealed inside a document, hidden, or disguised artifact\.

**Remediation:** Review the artifact provenance and the reason executable content is packaged in this location; keep executable files explicit and directly reviewable\.

**Evidence:**
- **concealment:** `hidden_artifact`
- **concealment\_reasons:** `['hidden_artifact']`
- **container\_ancestry:** `['filesystem']`
- **container\_depth:** `0`
- **container\_type:** `filesystem`
- **excluded\_from\_analysis:** `False`
- **excluded\_inspection\_incomplete:** `False`
- **inherited\_exclusion\_reason:** `None`
- **inspection\_limitation\_reason:** `None`
- **local\_only:** `True`
- **nested\_path:** `.github/scripts/build_pages.py`
- **outer\_path:** `.github/scripts/build_pages.py`
- **partially\_analyzed\_executable:** `False`
- **referenced:** `False`

---

### 🔴 HIGH: SC9

**Location:** `.github/scripts/bump_contract_md.py:1`  
**Confidence:** 100%  

**Message:** Executable content is concealed inside a document, hidden, or disguised artifact\.

**Remediation:** Review the artifact provenance and the reason executable content is packaged in this location; keep executable files explicit and directly reviewable\.

**Evidence:**
- **concealment:** `hidden_artifact`
- **concealment\_reasons:** `['hidden_artifact']`
- **container\_ancestry:** `['filesystem']`
- **container\_depth:** `0`
- **container\_type:** `filesystem`
- **excluded\_from\_analysis:** `False`
- **excluded\_inspection\_incomplete:** `False`
- **inherited\_exclusion\_reason:** `None`
- **inspection\_limitation\_reason:** `None`
- **local\_only:** `True`
- **nested\_path:** `.github/scripts/bump_contract_md.py`
- **outer\_path:** `.github/scripts/bump_contract_md.py`
- **partially\_analyzed\_executable:** `False`
- **referenced:** `False`

---

### 🔴 HIGH: SC9

**Location:** `.github/scripts/bump_roadmap_md.py:1`  
**Confidence:** 100%  

**Message:** Executable content is concealed inside a document, hidden, or disguised artifact\.

**Remediation:** Review the artifact provenance and the reason executable content is packaged in this location; keep executable files explicit and directly reviewable\.

**Evidence:**
- **concealment:** `hidden_artifact`
- **concealment\_reasons:** `['hidden_artifact']`
- **container\_ancestry:** `['filesystem']`
- **container\_depth:** `0`
- **container\_type:** `filesystem`
- **excluded\_from\_analysis:** `False`
- **excluded\_inspection\_incomplete:** `False`
- **inherited\_exclusion\_reason:** `None`
- **inspection\_limitation\_reason:** `None`
- **local\_only:** `True`
- **nested\_path:** `.github/scripts/bump_roadmap_md.py`
- **outer\_path:** `.github/scripts/bump_roadmap_md.py`
- **partially\_analyzed\_executable:** `False`
- **referenced:** `False`

---

### 🔴 HIGH: SC9

**Location:** `.github/scripts/design_decisions_index.py:1`  
**Confidence:** 100%  

**Message:** Executable content is concealed inside a document, hidden, or disguised artifact\.

**Remediation:** Review the artifact provenance and the reason executable content is packaged in this location; keep executable files explicit and directly reviewable\.

**Evidence:**
- **concealment:** `hidden_artifact`
- **concealment\_reasons:** `['hidden_artifact']`
- **container\_ancestry:** `['filesystem']`
- **container\_depth:** `0`
- **container\_type:** `filesystem`
- **excluded\_from\_analysis:** `False`
- **excluded\_inspection\_incomplete:** `False`
- **inherited\_exclusion\_reason:** `None`
- **inspection\_limitation\_reason:** `None`
- **local\_only:** `True`
- **nested\_path:** `.github/scripts/design_decisions_index.py`
- **outer\_path:** `.github/scripts/design_decisions_index.py`
- **partially\_analyzed\_executable:** `False`
- **referenced:** `False`

---

### 🔴 HIGH: SC9

**Location:** `.github/scripts/resolve_version.py:1`  
**Confidence:** 100%  

**Message:** Executable content is concealed inside a document, hidden, or disguised artifact\.

**Remediation:** Review the artifact provenance and the reason executable content is packaged in this location; keep executable files explicit and directly reviewable\.

**Evidence:**
- **concealment:** `hidden_artifact`
- **concealment\_reasons:** `['hidden_artifact']`
- **container\_ancestry:** `['filesystem']`
- **container\_depth:** `0`
- **container\_type:** `filesystem`
- **excluded\_from\_analysis:** `False`
- **excluded\_inspection\_incomplete:** `False`
- **inherited\_exclusion\_reason:** `None`
- **inspection\_limitation\_reason:** `None`
- **local\_only:** `True`
- **nested\_path:** `.github/scripts/resolve_version.py`
- **outer\_path:** `.github/scripts/resolve_version.py`
- **partially\_analyzed\_executable:** `False`
- **referenced:** `False`

---

### 🔴 HIGH: TT1

**Location:** `.github/scripts/resolve_version.py:120`  
**Confidence:** 80%  

**Message:** Direct flow: os\.environ \(credential/environment\) → open \(file write\)

**Remediation:** Add validation or sanitization between the data source and sink\. Never pass raw source data directly to a sink without checking its content\.

---

### 🔴 HIGH: TM2

**Location:** `.github/workflows/ci.yml:62`  
**Confidence:** 75%  

**Message:** Chaining Abuse

**Remediation:** Limit tool chaining depth and validate the output of each tool before passing it to the next\. Require explicit user approval for multi\-step chains\.

---

### 🔴 HIGH: TM2

**Location:** `scripts/_contract.py:971`  
**Confidence:** 75%  

**Message:** Chaining Abuse

**Remediation:** Limit tool chaining depth and validate the output of each tool before passing it to the next\. Require explicit user approval for multi\-step chains\.

---

### 🔴 HIGH: PE3

**Location:** `.github/workflows/release.yml:276`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `README.md:649`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `.github/workflows/release.yml:277`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: PE3

**Location:** `.github/workflows/release.yml:278`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths\. Use environment variables or secrets managers\. For docs, use placeholder paths \(e\.g\., /path/to/config\)\. Never load \.env or token files in production code paths\.

---

### 🔴 HIGH: AR2

**Location:** `CHANGELOG.md:498`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `CHANGELOG.md:764`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `docs/contract.md:706`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `docs/design-decisions.md:2346`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `references/scripts.md:811`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `scripts/_contract.py:678`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `scripts/_contract.py:1000`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `tests/test_asr.py:956`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `tests/test_audio.py:222`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: P2

**Location:** `CHANGELOG.md:1497`  
**Confidence:** 60%  

**Message:** Hidden Instructions

**Remediation:** Audit all comments and invisible characters\. Remove any instructions that direct the agent to perform unauthorized actions\. Use plain, reviewable content\.

---

### 🔴 HIGH: P2

**Location:** `references/gotchas.md:251`  
**Confidence:** 60%  

**Message:** Hidden Instructions

**Remediation:** Audit all comments and invisible characters\. Remove any instructions that direct the agent to perform unauthorized actions\. Use plain, reviewable content\.

---

### 🔴 HIGH: YR4

**Location:** `CHANGELOG.md:1497`  
**Confidence:** 80%  

**Message:** YARA rule 'agent\_skill\_mcp\_tool\_poisoning\_metadata': MCP/tool metadata poisoning indicators in tool schemas or skill manifests \[agent\_skills\]

**Remediation:** Remove offensive tool references and exploit code\. Legitimate agent skills should not contain penetration testing tools, exploit frameworks, or reconnaissance utilities\.

---

### 🔴 HIGH: AR2

**Location:** `README.md:381`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AR2

**Location:** `scripts/join.py:522`  
**Confidence:** 80%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove instructions that suppress warnings, disclaimers, or ethical commentary\. Let the agent surface safety\-relevant caveats to the user\.

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:28`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported analysis bounds and input size; resolve the scanner limit or provide fully inspectable source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'runtime_limit', 'message': 'Inspection reached its configured runtime limit.', 'phase': 'static', 'analyzers': ['static_patterns_prompt_injection'], 'limits': {'limit_seconds': 0.0, 'observed_seconds': 0.0}}, {'reason_code': 'runtime_limit', 'message': 'Inspection reached its configured runtime limit.', 'phase': 'meta', 'analyzers': ['meta_analyzer'], 'limits': {'limit_seconds': 0.0, 'observed_seconds': 0.0}}]`
- **target\_disposition:** `partial`
- **target\_path:** `scripts/_contract.py`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:34`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported analysis bounds and input size; resolve the scanner limit or provide fully inspectable source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'runtime_limit', 'message': 'Inspection reached its configured runtime limit.', 'phase': 'static', 'analyzers': ['static_patterns_prompt_injection'], 'limits': {'limit_seconds': 0.0, 'observed_seconds': 0.0}}, {'reason_code': 'runtime_limit', 'message': 'Inspection reached its configured runtime limit.', 'phase': 'meta', 'analyzers': ['meta_analyzer'], 'limits': {'limit_seconds': 0.0, 'observed_seconds': 0.0}}]`
- **target\_disposition:** `partial`
- **target\_path:** `scripts/render.py`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:60`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported analysis bounds and input size; resolve the scanner limit or provide fully inspectable source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'runtime_limit', 'message': 'Inspection reached its configured runtime limit.', 'phase': 'static', 'analyzers': ['static_patterns_prompt_injection'], 'limits': {'limit_seconds': 0.0, 'observed_seconds': 0.0}}]`
- **target\_disposition:** `partial`
- **target\_path:** `scripts/look.py`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:64`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported analysis bounds and input size; resolve the scanner limit or provide fully inspectable source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'runtime_limit', 'message': 'Inspection reached its configured runtime limit.', 'phase': 'static', 'analyzers': ['static_patterns_prompt_injection'], 'limits': {'limit_seconds': 0.0, 'observed_seconds': 0.0}}]`
- **target\_disposition:** `partial`
- **target\_path:** `scripts/look.py`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:92`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the target's analysis\-completeness ledger and resolve all limitations\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_agent_snooping']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_anti_refusal']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_deserialization']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_excessive_agency']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_harmful_content']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_memory_poisoning']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_privilege_escalation']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_prompt_injection']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_rogue_agent']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_ssrf']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_supply_chain']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_system_prompt_leakage']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `references/requests.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:205`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the target's analysis\-completeness ledger and resolve all limitations\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_agent_snooping']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_anti_refusal']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_deserialization']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_excessive_agency']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_harmful_content']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_memory_poisoning']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_privilege_escalation']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_prompt_injection']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_rogue_agent']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_ssrf']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_supply_chain']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_system_prompt_leakage']}, {'reason_code': 'obfuscated_instruction_text', 'message': 'Obfuscated instruction text could not be fully evaluated by the deterministic layer.', 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}]`
- **target\_disposition:** `partial`
- **target\_path:** `references/requests.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:182`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported analysis bounds and input size; resolve the scanner limit or provide fully inspectable source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'runtime_limit', 'message': 'Inspection reached its configured runtime limit.', 'phase': 'meta', 'analyzers': ['meta_analyzer'], 'limits': {'limit_seconds': 0.0, 'observed_seconds': 0.0}}]`
- **target\_disposition:** `partial`
- **target\_path:** `references/gotchas.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:184`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported analysis bounds and input size; resolve the scanner limit or provide fully inspectable source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'runtime_limit', 'message': 'Inspection reached its configured runtime limit.', 'phase': 'meta', 'analyzers': ['meta_analyzer'], 'limits': {'limit_seconds': 0.0, 'observed_seconds': 0.0}}]`
- **target\_disposition:** `partial`
- **target\_path:** `references/gotchas.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:185`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported analysis bounds and input size; resolve the scanner limit or provide fully inspectable source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'runtime_limit', 'message': 'Inspection reached its configured runtime limit.', 'phase': 'meta', 'analyzers': ['meta_analyzer'], 'limits': {'limit_seconds': 0.0, 'observed_seconds': 0.0}}]`
- **target\_disposition:** `partial`
- **target\_path:** `references/gotchas.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:186`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported analysis bounds and input size; resolve the scanner limit or provide fully inspectable source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'runtime_limit', 'message': 'Inspection reached its configured runtime limit.', 'phase': 'meta', 'analyzers': ['meta_analyzer'], 'limits': {'limit_seconds': 0.0, 'observed_seconds': 0.0}}]`
- **target\_disposition:** `partial`
- **target\_path:** `references/gotchas.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:187`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported analysis bounds and input size; resolve the scanner limit or provide fully inspectable source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'runtime_limit', 'message': 'Inspection reached its configured runtime limit.', 'phase': 'meta', 'analyzers': ['meta_analyzer'], 'limits': {'limit_seconds': 0.0, 'observed_seconds': 0.0}}]`
- **target\_disposition:** `partial`
- **target\_path:** `references/gotchas.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:188`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported analysis bounds and input size; resolve the scanner limit or provide fully inspectable source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'runtime_limit', 'message': 'Inspection reached its configured runtime limit.', 'phase': 'meta', 'analyzers': ['meta_analyzer'], 'limits': {'limit_seconds': 0.0, 'observed_seconds': 0.0}}]`
- **target\_disposition:** `partial`
- **target\_path:** `references/gotchas.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:189`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported analysis bounds and input size; resolve the scanner limit or provide fully inspectable source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'runtime_limit', 'message': 'Inspection reached its configured runtime limit.', 'phase': 'meta', 'analyzers': ['meta_analyzer'], 'limits': {'limit_seconds': 0.0, 'observed_seconds': 0.0}}]`
- **target\_disposition:** `partial`
- **target\_path:** `references/gotchas.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:190`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported analysis bounds and input size; resolve the scanner limit or provide fully inspectable source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'runtime_limit', 'message': 'Inspection reached its configured runtime limit.', 'phase': 'meta', 'analyzers': ['meta_analyzer'], 'limits': {'limit_seconds': 0.0, 'observed_seconds': 0.0}}]`
- **target\_disposition:** `partial`
- **target\_path:** `references/gotchas.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:191`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported analysis bounds and input size; resolve the scanner limit or provide fully inspectable source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'runtime_limit', 'message': 'Inspection reached its configured runtime limit.', 'phase': 'meta', 'analyzers': ['meta_analyzer'], 'limits': {'limit_seconds': 0.0, 'observed_seconds': 0.0}}]`
- **target\_disposition:** `partial`
- **target\_path:** `references/gotchas.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:192`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported analysis bounds and input size; resolve the scanner limit or provide fully inspectable source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'runtime_limit', 'message': 'Inspection reached its configured runtime limit.', 'phase': 'meta', 'analyzers': ['meta_analyzer'], 'limits': {'limit_seconds': 0.0, 'observed_seconds': 0.0}}]`
- **target\_disposition:** `partial`
- **target\_path:** `references/gotchas.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:193`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported analysis bounds and input size; resolve the scanner limit or provide fully inspectable source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'runtime_limit', 'message': 'Inspection reached its configured runtime limit.', 'phase': 'meta', 'analyzers': ['meta_analyzer'], 'limits': {'limit_seconds': 0.0, 'observed_seconds': 0.0}}]`
- **target\_disposition:** `partial`
- **target\_path:** `references/gotchas.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:194`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported analysis bounds and input size; resolve the scanner limit or provide fully inspectable source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'runtime_limit', 'message': 'Inspection reached its configured runtime limit.', 'phase': 'meta', 'analyzers': ['meta_analyzer'], 'limits': {'limit_seconds': 0.0, 'observed_seconds': 0.0}}]`
- **target\_disposition:** `partial`
- **target\_path:** `references/gotchas.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:195`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported analysis bounds and input size; resolve the scanner limit or provide fully inspectable source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'runtime_limit', 'message': 'Inspection reached its configured runtime limit.', 'phase': 'meta', 'analyzers': ['meta_analyzer'], 'limits': {'limit_seconds': 0.0, 'observed_seconds': 0.0}}]`
- **target\_disposition:** `partial`
- **target\_path:** `references/gotchas.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:196`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported analysis bounds and input size; resolve the scanner limit or provide fully inspectable source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'runtime_limit', 'message': 'Inspection reached its configured runtime limit.', 'phase': 'meta', 'analyzers': ['meta_analyzer'], 'limits': {'limit_seconds': 0.0, 'observed_seconds': 0.0}}]`
- **target\_disposition:** `partial`
- **target\_path:** `references/gotchas.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:209`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported analysis bounds and input size; resolve the scanner limit or provide fully inspectable source, then rerun the scan\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'runtime_limit', 'message': 'Inspection reached its configured runtime limit.', 'phase': 'meta', 'analyzers': ['meta_analyzer'], 'limits': {'limit_seconds': 0.0, 'observed_seconds': 0.0}}]`
- **target\_disposition:** `partial`
- **target\_path:** `references/gotchas.md`

---

### 🔴 HIGH: AE1

**Location:** `SKILL.md:207`  
**Confidence:** 100%  

**Message:** Referenced artifact was not completely inspected

**Remediation:** Review the reported expression and analyzer's parsing limitation; correct the scanner if it misinterprets valid source, then rerun the scan\. Review the reported analysis bounds and input size; resolve the scanner limit or provide fully inspectable source, then rerun the scan\. Review the target's analysis\-completeness ledger and resolve all limitations\. Keep required references; incomplete analysis is not proof of malicious evasion\.

**Evidence:**
- **reasons:** `[{'reason_code': 'static_parse_limit', 'message': "A security-relevant expression exceeded a bounded static parser's span limit.", 'phase': 'static', 'analyzers': ['static_patterns_tool_misuse']}, {'reason_code': 'runtime_limit', 'message': 'Inspection reached its configured runtime limit.', 'phase': 'meta', 'analyzers': ['meta_analyzer'], 'limits': {'limit_seconds': 0.0, 'observed_seconds': 0.0}}]`
- **target\_disposition:** `partial`
- **target\_path:** `references/scripts.md`

---

### 🔴 HIGH: TM2

**Location:** `demos/CI.md:41`  
**Confidence:** 75%  

**Message:** Chaining Abuse

**Remediation:** Limit tool chaining depth and validate the output of each tool before passing it to the next\. Require explicit user approval for multi\-step chains\.

---

### 🔴 HIGH: TM2

**Location:** `demos/CI.md:95`  
**Confidence:** 75%  

**Message:** Chaining Abuse

**Remediation:** Limit tool chaining depth and validate the output of each tool before passing it to the next\. Require explicit user approval for multi\-step chains\.

---

### 🔴 HIGH: TM1

**Location:** `demos/CI.md:104`  
**Confidence:** 85%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: MP3

**Location:** `evals/results/iteration-14-independent-grades.json:104`  
**Confidence:** 80%  

**Message:** Memory Manipulation

**Remediation:** Protect agent memory and state from modification by untrusted content\. Use read\-only memory for critical instructions and validate all state changes\.

---

### 🔴 HIGH: AS1

**Location:** `evals/results/iteration-16-independent-grades.json:144`  
**Confidence:** 85%  

**Message:** Agent Config Directory Access

**Remediation:** Remove all code or instructions that access agent configuration directories \(\.claude/, \.codex/, \.gemini/\)\. If configuration values are needed, pass them explicitly as parameters or environment variables — never read the agent's own config files\.

---

### 🔴 HIGH: TM1

**Location:** `references/process-pitfalls.md:47`  
**Confidence:** 70%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist\. Reject dangerous parameter values \(shell=True, \-\-force, \-rf /\) and use safe defaults\.

---

### 🔴 HIGH: AR1

**Location:** `references/scripts.md:812`  
**Confidence:** 85%  

**Message:** Anti\-Refusal Statement

**Remediation:** Remove any instruction telling the agent to never refuse or always comply\. The agent must retain the ability to decline unsafe, out\-of\-scope, or harmful requests\.

---

### 🔴 HIGH: P6

**Location:** `references/scripts.md:863`  
**Confidence:** 85%  

**Message:** Direct Prompt Extraction

**Remediation:** Remove any instructions that reveal, print, or output system prompts or internal rules\. System instructions should never be exposed to end users\.

---

### 🔴 HIGH: E2

**Location:** `scripts/_common/asr.py:939`  
**Confidence:** 70%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/run_parallel.py:77`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_accel.py:494`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_accel.py:1250`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_accel.py:1356`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_asr.py:921–922`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: RA1

**Location:** `tests/test_contract.py:762`  
**Confidence:** 85%  

**Message:** Self\-Modification

**Remediation:** Prevent the skill from modifying its own code, SKILL\.md, or configuration files\. Treat skill files as read\-only at runtime\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_contract.py:1269`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_contract.py:1593`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_picture.py:1666`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_contract.py:1919`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_contract.py:2563`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_contract.py:3681`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_contract.py:3702`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_contract.py:5193`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_contract.py:2002`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_contract.py:2041`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_contract.py:2058`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_contract.py:2132`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_contract.py:3823`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_contract.py:3840`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_contract.py:5588`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_contract.py:5660`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_contract.py:5684`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_contract.py:5787`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_contract.py:5902`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_contract.py:2390`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_contract.py:2447`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_contract.py:2877`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_contract.py:2888`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_picture.py:602`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_picture.py:1127`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_contract.py:3045`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_contract.py:3303`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_contract.py:3736`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_contract.py:5250`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_contract.py:5255`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_contract.py:5259`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_contract.py:5945`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_contract.py:6114–6115`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_contract.py:6169–6170`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_editing.py:2338`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_editing.py:2365`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_editing.py:2392`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_editing.py:2524`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_orchestration.py:1265`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_picture.py:635`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_picture.py:636`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_picture.py:2292`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_picture.py:3729`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_picture.py:3749`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🔴 HIGH: E2

**Location:** `tests/test_picture.py:4894–4895`  
**Confidence:** 60%  

**Message:** Env Variable Harvesting

**Remediation:** Read only explicitly required environment variables by name\. Avoid enumerating or copying the full environment, and never log or transmit credentials to untrusted destinations\.

---

### 🟡 MEDIUM: EA2

**Location:** `.claude/skills/destructive-operations/SKILL.md:204`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: E1

**Location:** `.claude/skills/github-actions/SKILL.md:51`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: PE2

**Location:** `.claude/skills/github-actions/SKILL.md:53`  
**Confidence:** 70%  

**Message:** Sudo/Root Execution

**Remediation:** Avoid sudo/root unless strictly required\. Prefer least\-privilege patterns\. If elevation is needed, document the justification and scope\.

---

### 🟡 MEDIUM: PE2

**Location:** `.github/workflows/ci.yml:62`  
**Confidence:** 70%  

**Message:** Sudo/Root Execution

**Remediation:** Avoid sudo/root unless strictly required\. Prefer least\-privilege patterns\. If elevation is needed, document the justification and scope\.

---

### 🟡 MEDIUM: PE2

**Location:** `.github/workflows/ci.yml:62`  
**Confidence:** 70%  

**Message:** Sudo/Root Execution

**Remediation:** Avoid sudo/root unless strictly required\. Prefer least\-privilege patterns\. If elevation is needed, document the justification and scope\.

---

### 🟡 MEDIUM: PE2

**Location:** `README.md:613`  
**Confidence:** 70%  

**Message:** Sudo/Root Execution

**Remediation:** Avoid sudo/root unless strictly required\. Prefer least\-privilege patterns\. If elevation is needed, document the justification and scope\.

---

### 🟡 MEDIUM: PE2

**Location:** `bin/install.js:150`  
**Confidence:** 70%  

**Message:** Sudo/Root Execution

**Remediation:** Avoid sudo/root unless strictly required\. Prefer least\-privilege patterns\. If elevation is needed, document the justification and scope\.

---

### 🟡 MEDIUM: PE2

**Location:** `demos/CI.md:42`  
**Confidence:** 70%  

**Message:** Sudo/Root Execution

**Remediation:** Avoid sudo/root unless strictly required\. Prefer least\-privilege patterns\. If elevation is needed, document the justification and scope\.

---

### 🟡 MEDIUM: PE2

**Location:** `demos/CI.md:43`  
**Confidence:** 70%  

**Message:** Sudo/Root Execution

**Remediation:** Avoid sudo/root unless strictly required\. Prefer least\-privilege patterns\. If elevation is needed, document the justification and scope\.

---

### 🟡 MEDIUM: PE2

**Location:** `demos/CI.md:96`  
**Confidence:** 70%  

**Message:** Sudo/Root Execution

**Remediation:** Avoid sudo/root unless strictly required\. Prefer least\-privilege patterns\. If elevation is needed, document the justification and scope\.

---

### 🟡 MEDIUM: PE2

**Location:** `demos/CI.md:97`  
**Confidence:** 70%  

**Message:** Sudo/Root Execution

**Remediation:** Avoid sudo/root unless strictly required\. Prefer least\-privilege patterns\. If elevation is needed, document the justification and scope\.

---

### 🟡 MEDIUM: PE2

**Location:** `scripts/_common/runner.py:25`  
**Confidence:** 70%  

**Message:** Sudo/Root Execution

**Remediation:** Avoid sudo/root unless strictly required\. Prefer least\-privilege patterns\. If elevation is needed, document the justification and scope\.

---

### 🟡 MEDIUM: PE2

**Location:** `scripts/_common/runner.py:26`  
**Confidence:** 70%  

**Message:** Sudo/Root Execution

**Remediation:** Avoid sudo/root unless strictly required\. Prefer least\-privilege patterns\. If elevation is needed, document the justification and scope\.

---

### 🟡 MEDIUM: PE2

**Location:** `scripts/_common/runner.py:27`  
**Confidence:** 70%  

**Message:** Sudo/Root Execution

**Remediation:** Avoid sudo/root unless strictly required\. Prefer least\-privilege patterns\. If elevation is needed, document the justification and scope\.

---

### 🟡 MEDIUM: PE2

**Location:** `scripts/_contract.py:971`  
**Confidence:** 70%  

**Message:** Sudo/Root Execution

**Remediation:** Avoid sudo/root unless strictly required\. Prefer least\-privilege patterns\. If elevation is needed, document the justification and scope\.

---

### 🟡 MEDIUM: PE2

**Location:** `scripts/_contract.py:971`  
**Confidence:** 70%  

**Message:** Sudo/Root Execution

**Remediation:** Avoid sudo/root unless strictly required\. Prefer least\-privilege patterns\. If elevation is needed, document the justification and scope\.

---

### 🟡 MEDIUM: PE2

**Location:** `scripts/_contract.py:978`  
**Confidence:** 70%  

**Message:** Sudo/Root Execution

**Remediation:** Avoid sudo/root unless strictly required\. Prefer least\-privilege patterns\. If elevation is needed, document the justification and scope\.

---

### 🟡 MEDIUM: PE2

**Location:** `scripts/_contract.py:978`  
**Confidence:** 70%  

**Message:** Sudo/Root Execution

**Remediation:** Avoid sudo/root unless strictly required\. Prefer least\-privilege patterns\. If elevation is needed, document the justification and scope\.

---

### 🟡 MEDIUM: PE2

**Location:** `.claude/skills/github-actions/SKILL.md:56`  
**Confidence:** 70%  

**Message:** Sudo/Root Execution

**Remediation:** Avoid sudo/root unless strictly required\. Prefer least\-privilege patterns\. If elevation is needed, document the justification and scope\.

---

### 🟡 MEDIUM: PE2

**Location:** `README.md:106`  
**Confidence:** 70%  

**Message:** Sudo/Root Execution

**Remediation:** Avoid sudo/root unless strictly required\. Prefer least\-privilege patterns\. If elevation is needed, document the justification and scope\.

---

### 🟡 MEDIUM: EA4

**Location:** `.claude/skills/mcp-server-design/SKILL.md:155`  
**Confidence:** 75%  

**Message:** Unbounded Resource Access

**Remediation:** Set explicit rate limits, timeouts, and resource quotas for API calls, file operations, and compute\. Implement circuit breakers for runaway loops\.

---

### 🟡 MEDIUM: EA4

**Location:** `tests/test_contract.py:2515`  
**Confidence:** 75%  

**Message:** Unbounded Resource Access

**Remediation:** Set explicit rate limits, timeouts, and resource quotas for API calls, file operations, and compute\. Implement circuit breakers for runaway loops\.

---

### 🟡 MEDIUM: RP1

**Location:** `.claude/skills/reproducing-ci-locally/SKILL.md:114`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx prettier'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `.claude/skills/reproducing-ci-locally/SKILL.md:115`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx prettier'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: E1

**Location:** `.claude/skills/verifying-external-behavior/SKILL.md:27`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: E1

**Location:** `.claude/skills/verifying-external-behavior/SKILL.md:28`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary\. Remove or replace with documented APIs\. Ensure no secrets, tokens, or PII are transmitted\.

---

### 🟡 MEDIUM: RP1

**Location:** `.claude/skills/verifying-external-behavior/SKILL.md:34`  
**Confidence:** 75%  

**Message:** Docker image referenced without tag or digest: 'docker run \-\-rm'\.

**Remediation:** Pin the image: image:tag or image@sha256:abc123

---

### 🟡 MEDIUM: AST4

**Location:** `.github/scripts/resolve_version.py:101–103`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: TT2

**Location:** `.github/scripts/resolve_version.py:101–103`  
**Confidence:** 65%  

**Message:** Tainted flow: 'repo' from os\.environ \(line 115, credential/environment\) → subprocess\.run \(code execution\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: AST4

**Location:** `.github/scripts/resolve_version.py:112–114`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: TT2

**Location:** `.github/scripts/resolve_version.py:112–114`  
**Confidence:** 65%  

**Message:** Tainted flow: 'rev\_range' from os\.environ \(line 111, credential/environment\) → subprocess\.run \(code execution\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: EA2

**Location:** `.github/workflows/dependabot-auto-merge.yml:1`  
**Confidence:** 85%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: AE4

**Location:** `CHANGELOG.md:1`  
**Confidence:** 80%  

**Message:** Suspicious Unicode normalization or mixed\-script content

---

### 🟡 MEDIUM: RP1

**Location:** `CHANGELOG.md:91`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx installer'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `CHANGELOG.md:3081`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx installer'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `scripts/_contract.py:1642`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx installer'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `scripts/_contract.py:1863`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx installer'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `tests/test_contract.py:1838`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx installer'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `CHANGELOG.md:94`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx   installer'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `CHANGELOG.md:316`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `CHANGELOG.md:557`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `CHANGELOG.md:2772`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `CHANGELOG.md:3018`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `README.md:36`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `README.md:66`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `README.md:109`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `README.md:112`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `README.md:115`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `README.md:120`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `README.md:333`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `README.md:334`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `README.md:373`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `README.md:374`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `README.md:465`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `README.md:580`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `README.md:581`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `README.md:582`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `README.md:583`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `README.md:584`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `README.md:585`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `README.md:586`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `README.md:599`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `README.md:604`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `README.md:605`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `bin/install.js:8`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `bin/install.js:9`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `bin/install.js:10`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `bin/install.js:11`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `bin/install.js:12`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `bin/install.js:13`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `bin/install.js:14`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `bin/install.js:15`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `bin/install.js:16`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `bin/install.js:18`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `scripts/_contract.py:1195`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `scripts/_contract.py:1954`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `site/index.html:346`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `site/index.html:468`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `site/index.html:469`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `site/index.html:470`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `site/index.html:471`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `site/index.html:472`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `site/index.html:514`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: RP1

**Location:** `README.md:465`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx remotion\-ffmpeg\-skill'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: LP3

**Location:** `SKILL.md:1`  
**Confidence:** 70%  

**Message:** Skill declares no tool scope \('permissions' or 'allowed\-tools'\) but code capabilities were detected: env, file\_read, file\_write, network, shell\.

**Remediation:** Clarify the skill's intended tool scope and review how the host runtime enforces it; runtime permissions are unknown unless separately verified\. For Claude Code / Agent Skills SKILL\.md, 'allowed\-tools' records preapproved tools, not a permission ceiling; add a tool only when it is independently approved as necessary, not to silence this finding\. For MCP server manifests, use a 'permissions' list naming the required capabilities\.

---

### 🟡 MEDIUM: AST4

**Location:** `demos/build.py:61–62`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: TT2

**Location:** `demos/build.py:61–62`  
**Confidence:** 65%  

**Message:** Tainted flow: 'cmd' from os\.environ\.get \(line 70, credential/environment\) → subprocess\.run \(code execution\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: TT2

**Location:** `demos/build.py:1863`  
**Confidence:** 65%  

**Message:** Tainted flow: 'before\_copy' from os\.environ\.get \(line 1861, credential/environment\) → shutil\.copyfile \(file write\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: AST4

**Location:** `demos/pages_videos.py:28`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AE4

**Location:** `docs/design-decisions.md:1`  
**Confidence:** 80%  

**Message:** Suspicious Unicode normalization or mixed\-script content

---

### 🟡 MEDIUM: EA4

**Location:** `docs/design-decisions.md:67`  
**Confidence:** 75%  

**Message:** Unbounded Resource Access

**Remediation:** Set explicit rate limits, timeouts, and resource quotas for API calls, file operations, and compute\. Implement circuit breakers for runaway loops\.

---

### 🟡 MEDIUM: EA2

**Location:** `docs/design-decisions.md:1362`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: AST4

**Location:** `evals/contract/check.py:23`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `evals/grade_runs_24.py:127–128`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `evals/grade_runs_24.py:248`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: OH3

**Location:** `evals/results/iteration-2-4-independent-grades.json:164`  
**Confidence:** 60%  

**Message:** Unbounded Output

**Remediation:** Set explicit limits on output length, generation count, and rate\. Use max\_tokens and truncation to prevent unbounded output\.

---

### 🟡 MEDIUM: OH3

**Location:** `evals/results/iteration-2-4-independent-grades.json:692`  
**Confidence:** 60%  

**Message:** Unbounded Output

**Remediation:** Set explicit limits on output length, generation count, and rate\. Use max\_tokens and truncation to prevent unbounded output\.

---

### 🟡 MEDIUM: OH3

**Location:** `evals/trigger/prompts.json:317`  
**Confidence:** 60%  

**Message:** Unbounded Output

**Remediation:** Set explicit limits on output length, generation count, and rate\. Use max\_tokens and truncation to prevent unbounded output\.

---

### 🟡 MEDIUM: OH3

**Location:** `references/scripts.md:1765`  
**Confidence:** 60%  

**Message:** Unbounded Output

**Remediation:** Set explicit limits on output length, generation count, and rate\. Use max\_tokens and truncation to prevent unbounded output\.

---

### 🟡 MEDIUM: EA2

**Location:** `evals/results/iteration-2-4-independent-grades.json:582`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `evals/results/iteration-2-4.json:50`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `scripts/_common/__init__.py:141`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `scripts/_common/emit.py:221`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `tests/test_contract.py:3636`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: AST4

**Location:** `evals/write_fixtures.py:67–69`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `evals/write_fixtures.py:89`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AS3

**Location:** `references/process-pitfalls.md:68`  
**Confidence:** 80%  

**Message:** Skill Enumeration

**Remediation:** Remove all code or instructions that list or read other skills' files or directories\. Skills should operate independently; cross\-skill access is a privilege escalation\.

---

### 🟡 MEDIUM: AST4

**Location:** `scripts/_common/asr.py:244–245`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: TT2

**Location:** `scripts/_common/asr.py:244–245`  
**Confidence:** 65%  

**Message:** Tainted flow: 'cmd' from os\.environ\.get \(line 1065, credential/environment\) → subprocess\.run \(code execution\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: EA2

**Location:** `scripts/_common/asr.py:311`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `scripts/_common/asr.py:814`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `scripts/_common/asr.py:827`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `scripts/graphics.py:71`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `scripts/graphics.py:259`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `scripts/graphics.py:564`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: EA2

**Location:** `tests/test_asr.py:443`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human\-in\-the\-loop confirmation for destructive, irreversible, or high\-impact operations\. Never auto\-execute commands that modify files, send data, or alter system state\.

---

### 🟡 MEDIUM: AST4

**Location:** `scripts/_common/drawtext.py:112–113`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `scripts/_common/emoji.py:191–192`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `scripts/_common/emoji.py:218–223`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `scripts/_common/fonts.py:86`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `scripts/_common/fonts.py:226–227`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `scripts/_common/fonts.py:314–315`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `scripts/_common/fonts.py:433–434`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `scripts/_common/fonts.py:467–468`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `scripts/_common/runner.py:122–123`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `scripts/_common/runner.py:160–161`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: TT2

**Location:** `scripts/_common/runner.py:122–123`  
**Confidence:** 65%  

**Message:** Tainted flow: 'found\_exe\(\)' from os\.environ\.get \(line 270, credential/environment\) → subprocess\.run \(code execution\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: TT2

**Location:** `scripts/_common/runner.py:160–161`  
**Confidence:** 65%  

**Message:** Tainted flow: 'found\_exe\(\)' from os\.environ\.get \(line 270, credential/environment\) → subprocess\.run \(code execution\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: AST4

**Location:** `scripts/_common/runner.py:1173–1175`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: TT2

**Location:** `scripts/_common/runner.py:1173–1175`  
**Confidence:** 65%  

**Message:** Tainted flow: 'safe\_which\(\)' from os\.environ\.get \(line 235, credential/environment\) → subprocess\.run \(code execution\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: AST4

**Location:** `scripts/_common/runner.py:1382`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `scripts/_common/runner.py:1420`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `scripts/_common/runner.py:1462–1464`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: TT2

**Location:** `scripts/_common/runner.py:1462–1464`  
**Confidence:** 65%  

**Message:** Tainted flow: 'found\_exe\(\)' from os\.environ\.get \(line 270, credential/environment\) → subprocess\.run \(code execution\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: AST4

**Location:** `scripts/_common/runner.py:1529–1530`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `scripts/_common/runner.py:1580–1581`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: TM3

**Location:** `scripts/_common/runner.py:1723`  
**Confidence:** 70%  

**Message:** Unsafe Defaults

**Remediation:** Override unsafe defaults with secure settings \(verify=True, auth required, restrictive permissions\)\. Review and harden all tool configurations\.

---

### 🟡 MEDIUM: AST4

**Location:** `scripts/_common/runner.py:1828–1829`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: TT2

**Location:** `scripts/_common/runner.py:1828–1829`  
**Confidence:** 65%  

**Message:** Tainted flow: 'found\_exe\(\)' from os\.environ\.get \(line 270, credential/environment\) → subprocess\.run \(code execution\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: RP1

**Location:** `scripts/_contract.py:772`  
**Confidence:** 70%  

**Message:** MCP server referenced without pinned version: 'npx skills'\.

**Remediation:** Pin the version: npx @scope/server@1\.2\.3

---

### 🟡 MEDIUM: AST4

**Location:** `scripts/_contract.py:836`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `scripts/_contract.py:900`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `scripts/_contract.py:1125–1129`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `scripts/_contract.py:1162`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `scripts/render.py:682–683`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: TT2

**Location:** `scripts/render.py:779`  
**Confidence:** 65%  

**Message:** Tainted flow: 'art' from os\.environ\.get \(line 753, credential/environment\) → shutil\.copy2 \(file write\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: TT2

**Location:** `scripts/render.py:806`  
**Confidence:** 65%  

**Message:** Tainted flow: 'art' from os\.environ\.get \(line 804, credential/environment\) → shutil\.copy2 \(file write\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: OH3

**Location:** `scripts/reverse.py:6`  
**Confidence:** 75%  

**Message:** Unbounded Output

**Remediation:** Set explicit limits on output length, generation count, and rate\. Use max\_tokens and truncation to prevent unbounded output\.

---

### 🟡 MEDIUM: AST4

**Location:** `scripts/verify.py:116–117`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/_fixtures.py:47`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: TT2

**Location:** `tests/_fixtures.py:47`  
**Confidence:** 65%  

**Message:** Tainted flow: 'cmd' from os\.environ\.get \(line 282, credential/environment\) → subprocess\.run \(code execution\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/_fixtures.py:117–118`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/_fixtures.py:119–121`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/_fixtures.py:128–131`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/_fixtures.py:145–148`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/_fixtures.py:165`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/_fixtures.py:182–185`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: TT2

**Location:** `tests/_fixtures.py:182–185`  
**Confidence:** 65%  

**Message:** Tainted flow: 'path' from os\.environ\.get \(line 172, credential/environment\) → subprocess\.run \(code execution\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/_fixtures.py:196–197`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/_fixtures.py:208`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/_fixtures.py:349–351`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/_fixtures.py:385–386`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/_fixtures.py:390–391`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/_fixtures.py:397–398`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/_fixtures.py:415–417`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/bench_scenes.py:29`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/bench_silence.py:29`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/bench_sync.py:28`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/bench_vt.py:53`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/corpus.py:109`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/corpus.py:170`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: MP2

**Location:** `tests/fixtures/ffmpeg_filters_6.1.txt:365`  
**Confidence:** 85%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `tests/fixtures/ffmpeg_filters_6.1.txt:366`  
**Confidence:** 85%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `tests/fixtures/ffmpeg_filters_7.1_constructed.txt:365`  
**Confidence:** 85%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `tests/fixtures/ffmpeg_filters_7.1_constructed.txt:366`  
**Confidence:** 85%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `tests/fixtures/ffmpeg_filters_8.1.2_macos.txt:325`  
**Confidence:** 85%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `tests/fixtures/ffmpeg_filters_9.0.1_windows.txt:342`  
**Confidence:** 85%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: MP2

**Location:** `tests/fixtures/ffmpeg_filters_9.0.1_windows.txt:482`  
**Confidence:** 85%  

**Message:** Context Window Stuffing

**Remediation:** Implement context\-window management that detects and rejects padding or stuffing attempts\. Prioritize system instructions over user\-injected content\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/run_parallel.py:81–82`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: TT2

**Location:** `tests/run_parallel.py:81–82`  
**Confidence:** 65%  

**Message:** Tainted flow: 'env' from os\.environ\.get \(line 77, credential/environment\) → subprocess\.run \(code execution\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_accel.py:495–497`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: TT2

**Location:** `tests/test_accel.py:495–497`  
**Confidence:** 65%  

**Message:** Tainted flow: 'env' from os\.environ\.get \(line 494, credential/environment\) → subprocess\.run \(code execution\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_accel.py:648–649`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_accel.py:1197–1199`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_accel.py:1236–1237`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_accel.py:1238–1239`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_accel.py:1251–1253`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: TT2

**Location:** `tests/test_accel.py:1251–1253`  
**Confidence:** 65%  

**Message:** Tainted flow: 'env' from os\.environ\.get \(line 1250, credential/environment\) → subprocess\.run \(code execution\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_accel.py:1319–1321`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_analysis.py:308–309`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_analysis.py:439–440`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_analysis.py:445–446`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_analysis.py:447–448`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_analysis.py:509–510`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_analysis.py:640–641`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_analysis.py:692–693`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST3

**Location:** `tests/test_analysis.py:878`  
**Confidence:** 75%  

**Message:** Dynamic import via \_\_import\_\_\(\)

**Remediation:** Use standard import statements instead of \_\_import\_\_\(\)\. If dynamic loading is needed, use importlib with an allowlist of permitted modules\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_audio.py:800–801`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_contract.py:62`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: TT2

**Location:** `tests/test_contract.py:62`  
**Confidence:** 65%  

**Message:** Tainted flow: 'env' from os\.environ \(line 5589, credential/environment\) → subprocess\.run \(code execution\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_contract.py:300–301`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_contract.py:1598`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_contract.py:1700–1712`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: TT2

**Location:** `tests/test_contract.py:1700–1712`  
**Confidence:** 65%  

**Message:** Tainted flow: 'self\.src' from os\.environ\.get \(line 141, credential/environment\) → subprocess\.run \(code execution\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_contract.py:1832–1833`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_contract.py:1865–1866`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_contract.py:1920–1921`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: TT2

**Location:** `tests/test_contract.py:1920–1921`  
**Confidence:** 65%  

**Message:** Tainted flow: 'env' from os\.environ \(line 1919, credential/environment\) → subprocess\.run \(code execution\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: TT2

**Location:** `tests/test_contract.py:2248`  
**Confidence:** 65%  

**Message:** Tainted flow: 'png' from os\.environ\.get \(line 2242, credential/environment\) → shutil\.copyfile \(file write\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: TT2

**Location:** `tests/test_contract.py:2408`  
**Confidence:** 65%  

**Message:** Tainted flow: 'self\.src' from os\.environ\.get \(line 141, credential/environment\) → shutil\.copyfile \(file write\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: EA4

**Location:** `tests/test_contract.py:2487`  
**Confidence:** 75%  

**Message:** Unbounded Resource Access

**Remediation:** Set explicit rate limits, timeouts, and resource quotas for API calls, file operations, and compute\. Implement circuit breakers for runaway loops\.

---

### 🟡 MEDIUM: EA4

**Location:** `tests/test_contract.py:4636`  
**Confidence:** 75%  

**Message:** Unbounded Resource Access

**Remediation:** Set explicit rate limits, timeouts, and resource quotas for API calls, file operations, and compute\. Implement circuit breakers for runaway loops\.

---

### 🟡 MEDIUM: TT2

**Location:** `tests/test_contract.py:2594`  
**Confidence:** 65%  

**Message:** Tainted flow: 'self\.src' from os\.environ\.get \(line 141, credential/environment\) → shutil\.copy \(file write\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_contract.py:2743–2744`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_contract.py:2758`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: TT2

**Location:** `tests/test_contract.py:2780`  
**Confidence:** 65%  

**Message:** Tainted flow: 'self\.src' from os\.environ\.get \(line 141, credential/environment\) → shutil\.copyfile \(file write\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: TT2

**Location:** `tests/test_contract.py:3607`  
**Confidence:** 65%  

**Message:** Tainted flow: 'self\.src' from os\.environ\.get \(line 141, credential/environment\) → shutil\.copyfile \(file write\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_contract.py:2785–2786`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: TT2

**Location:** `tests/test_contract.py:2856`  
**Confidence:** 65%  

**Message:** Tainted flow: 'self\.src' from os\.environ\.get \(line 141, credential/environment\) → shutil\.copyfile \(file write\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_contract.py:2878`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_contract.py:2904`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: TT2

**Location:** `tests/test_contract.py:2878`  
**Confidence:** 65%  

**Message:** Tainted flow: 'env' from os\.environ \(line 2877, credential/environment\) → subprocess\.run \(code execution\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: TT2

**Location:** `tests/test_contract.py:2904`  
**Confidence:** 65%  

**Message:** Tainted flow: 'env' from os\.environ \(line 2903, credential/environment\) → subprocess\.run \(code execution\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_contract.py:2940–2941`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: TT2

**Location:** `tests/test_contract.py:3148`  
**Confidence:** 65%  

**Message:** Tainted flow: 'self\.src' from os\.environ\.get \(line 141, credential/environment\) → shutil\.copy \(file write\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: TT2

**Location:** `tests/test_contract.py:3190`  
**Confidence:** 65%  

**Message:** Tainted flow: 'self\.src' from os\.environ\.get \(line 141, credential/environment\) → shutil\.copy \(file write\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: TT2

**Location:** `tests/test_contract.py:3243`  
**Confidence:** 65%  

**Message:** Tainted flow: 'self\.src' from os\.environ\.get \(line 141, credential/environment\) → shutil\.copy \(file write\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: TT2

**Location:** `tests/test_contract.py:4034`  
**Confidence:** 65%  

**Message:** Tainted flow: 'self\.src' from os\.environ\.get \(line 141, credential/environment\) → shutil\.copy \(file write\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: TT2

**Location:** `tests/test_contract.py:3252`  
**Confidence:** 65%  

**Message:** Tainted flow: 'self\.src' from os\.environ\.get \(line 141, credential/environment\) → shutil\.copy \(file write\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: TT2

**Location:** `tests/test_contract.py:3304`  
**Confidence:** 65%  

**Message:** Tainted flow: 'self\.src' from os\.environ\.get \(line 141, credential/environment\) → shutil\.copy \(file write\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: TT2

**Location:** `tests/test_contract.py:3334`  
**Confidence:** 65%  

**Message:** Tainted flow: 'self\.src' from os\.environ\.get \(line 141, credential/environment\) → shutil\.copy \(file write\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: TT2

**Location:** `tests/test_contract.py:3427`  
**Confidence:** 65%  

**Message:** Tainted flow: 'self\.src' from os\.environ\.get \(line 141, credential/environment\) → shutil\.copy \(file write\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: TT2

**Location:** `tests/test_contract.py:3346`  
**Confidence:** 65%  

**Message:** Tainted flow: 'self\.src' from os\.environ\.get \(line 141, credential/environment\) → shutil\.copy \(file write\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: TT2

**Location:** `tests/test_contract.py:3464`  
**Confidence:** 65%  

**Message:** Tainted flow: 'self\.src' from os\.environ\.get \(line 141, credential/environment\) → shutil\.copy \(file write\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: TT2

**Location:** `tests/test_contract.py:3510`  
**Confidence:** 65%  

**Message:** Tainted flow: 'self\.src' from os\.environ\.get \(line 141, credential/environment\) → shutil\.copy \(file write\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: TT2

**Location:** `tests/test_contract.py:3623`  
**Confidence:** 65%  

**Message:** Tainted flow: 'self\.src' from os\.environ\.get \(line 141, credential/environment\) → shutil\.copyfile \(file write\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: TT2

**Location:** `tests/test_contract.py:3792`  
**Confidence:** 65%  

**Message:** Tainted flow: 'self\.src' from os\.environ\.get \(line 141, credential/environment\) → shutil\.copyfile \(file write\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: TT2

**Location:** `tests/test_contract.py:4035`  
**Confidence:** 65%  

**Message:** Tainted flow: 'self\.camb' from os\.environ\.get \(line 148, credential/environment\) → shutil\.copy \(file write\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_contract.py:4074–4075`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_contract.py:4516`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: TT2

**Location:** `tests/test_contract.py:4516`  
**Confidence:** 65%  

**Message:** Tainted flow: 'req' from os\.environ\.get \(line 4515, credential/environment\) → subprocess\.run \(code execution\)

**Remediation:** Validate tainted variables before passing them to sinks\. Use allowlists, type checks, or sanitization functions on data from external sources\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_contract.py:4724–4725`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_contract.py:5222–5223`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST6

**Location:** `tests/test_contract.py:5700`  
**Confidence:** 65%  

**Message:** compile\(\) call detected

**Remediation:** Avoid compile\(\) with dynamic strings\. If code generation is needed, use templates or AST manipulation with strict validation\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_contract.py:5916–5917`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_cut_copy.py:41–42`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_cut_copy.py:53–54`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_editing.py:1386–1387`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_cut_copy.py:60–61`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_editing.py:765–766`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_cut_copy.py:71–72`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_cut_copy.py:329–330`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_cut_copy.py:581–582`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_cut_copy.py:761–763`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_cut_copy.py:765–766`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_cut_copy.py:779–781`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_cut_copy.py:867–868`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_cut_copy.py:890–891`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_cut_copy.py:933–934`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_cut_copy.py:1165–1167`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_cut_copy.py:1258–1259`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_cut_copy.py:1279–1280`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_delivery.py:216–218`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_delivery.py:602–604`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_editing.py:63–64`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_editing.py:499–501`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_picture.py:175–177`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_picture.py:2085–2087`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_picture.py:2108–2110`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_editing.py:821–822`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_editing.py:872–874`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_editing.py:904–906`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_editing.py:931–932`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_editing.py:1231`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_editing.py:1324–1326`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_editing.py:1374–1375`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_editing.py:1439–1440`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_editing.py:1441–1442`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_orchestration.py:712–714`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_orchestration.py:1266`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_orchestration.py:1290`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_orchestration.py:2351–2353`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AE4

**Location:** `tests/test_picture.py:1`  
**Confidence:** 80%  

**Message:** Suspicious Unicode normalization or mixed\-script content

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_picture.py:245`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_picture.py:1090–1091`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_picture.py:1227–1229`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_picture.py:1235–1236`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST3

**Location:** `tests/test_picture.py:1246`  
**Confidence:** 75%  

**Message:** Dynamic import via \_\_import\_\_\(\)

**Remediation:** Use standard import statements instead of \_\_import\_\_\(\)\. If dynamic loading is needed, use importlib with an allowlist of permitted modules\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_picture.py:2051–2054`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_picture.py:2134–2136`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_picture.py:2157–2159`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_picture.py:2262–2264`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_picture.py:2266–2268`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_picture.py:2294–2295`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_picture.py:2600`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_picture.py:2689`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_picture.py:2911`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_picture.py:2625–2627`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_picture.py:2738–2740`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_picture.py:2743–2744`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_picture.py:2813`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_picture.py:2914`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_picture.py:2958–2960`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_picture.py:2962–2963`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_picture.py:3026–3027`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_picture.py:3098–3100`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_picture.py:3119–3120`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_picture.py:4116–4117`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟡 MEDIUM: AST4

**Location:** `tests/test_picture.py:4181–4182`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess\.run\(\) with shell=False and an explicit argument list\. Validate all inputs and avoid passing user\-controlled data to commands\.

---

### 🟢 LOW: AST7

**Location:** `scripts/_common/__init__.py:157`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `scripts/_common/emit.py:79`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `scripts/_common/emit.py:80`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `scripts/_common/emit.py:332`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `scripts/_common/emit.py:333`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `scripts/_common/emit.py:119`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `scripts/_common/emit.py:119`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `scripts/_common/runner.py:249`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `scripts/audio.py:83`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `scripts/color.py:72`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `scripts/color.py:80`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `scripts/audio.py:226`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `scripts/audio.py:226`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `scripts/audio.py:233`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `scripts/caption.py:782`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `scripts/graphics.py:136`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `scripts/graphics.py:286`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `scripts/metadata.py:217`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `scripts/metadata.py:217`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `tests/_fixtures.py:271`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `tests/test_contract.py:4380`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `tests/test_contract.py:4863`  
**Confidence:** 50%  

**Message:** Dynamic attribute access via getattr\(\)

**Remediation:** Replace dynamic getattr\(\) with explicit attribute access or a dictionary lookup with an allowlist of permitted attributes\.

---

### 🟢 LOW: AST7

**Location:** `tests/test_contract.py:5053`  
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
| Coverage | 58\.9% |
| Fully inspected | 168 |
| Partially inspected | 117 |
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
| binary\_text\_projection | `assets/demo.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_content | `assets/icon.png` | Binary content is unsupported by this analyzer\. |
| binary\_content | `assets/logo.png` | Binary content is unsupported by this analyzer\. |
| binary\_content | `assets/social-preview.png` | Binary content is unsupported by this analyzer\. |
| binary\_content | `brand/app-icon-dark.png` | Binary content is unsupported by this analyzer\. |
| binary\_content | `brand/app-icon.png` | Binary content is unsupported by this analyzer\. |
| binary\_content | `demos/footage/ai_talk.mp4` | Binary content is unsupported by this analyzer\. |
| binary\_content | `demos/footage/ai_talk_en.mp4` | Binary content is unsupported by this analyzer\. |
| binary\_text\_projection | `docs/demos/audiogram.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/beats_snap.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/bgm_ducking.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/broll_cutaway.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/captions_ar.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/captions_emoji.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/captions_en.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/captions_fitsize.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/captions_ja.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/captions_ko.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/captions_multitrack.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/captions_phrase.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/captions_pop_karaoke.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/captions_zh.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/color_correct.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/color_lut.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/contact_sheet.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/crop_rect.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/cropdetect_crop.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/cut_accurate.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/cut_edit_list.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/cut_remove.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/deinterlace.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/delogo.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/denoise.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/downmix_51.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/export_reels.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/filler_en.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/filler_korean.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/fit_blur.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/freeze_hold.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/greenscreen.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/grid_2x2.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/hdr_tonemap.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/insert_still.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/join_fade.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/join_fadeblack.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/logo_overlay.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/loop_times.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/loudness.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/lower_third.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/lower_third_hindi.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/metadata_auto_chapters.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/metadata_chapters.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/motion_centre_crop.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/multicam_switch.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/multicam_switch_energy.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/overlay_place.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/pad_timeline.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/proxy.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/redact_blur.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/reframe_crop.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/reframe_pad.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/reframe_talk.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/render_pip.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/render_project.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/reverse.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/scenes_highlights.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/scenes_shots.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/sequence_frames.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/silence_removal.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/silence_speech_aware.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/speed_up.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/speedramp.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/sphere_flat.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/stabilize.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/straighten.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/sync_mic.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/template_tiktok.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/title_card.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_text\_projection | `docs/demos/waveform_render.gif` | Only bounded printable text was inspected; binary structure and behavior are outside scope\. |
| binary\_content | `site/brand/apple-touch-icon.png` | Binary content is unsupported by this analyzer\. |
| binary\_content | `site/brand/favicon.ico` | Binary content is unsupported by this analyzer\. |
| binary\_content | `site/brand/og.png` | Binary content is unsupported by this analyzer\. |
| binary\_content | `site/media/filler_en.jpg` | Binary content is unsupported by this analyzer\. |
| binary\_content | `site/media/filler_en.mp4` | Binary content is unsupported by this analyzer\. |
| binary\_content | `site/media/reframe_talk.jpg` | Binary content is unsupported by this analyzer\. |
| binary\_content | `site/media/reframe_talk.mp4` | Binary content is unsupported by this analyzer\. |

### Ledger Exceptions

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| runtime\_limit | `.claude-plugin/marketplace.json` | Inspection reached its configured runtime limit\. |
| static\_parse\_limit | `.claude/skills/build-artifacts/SKILL.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| runtime\_limit | `.claude/skills/destructive-operations/SKILL.md` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `.claude/skills/git-hygiene/SKILL.md` | Inspection reached its configured runtime limit\. |
| static\_parse\_limit | `.claude/skills/git-hygiene/SKILL.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| runtime\_limit | `.claude/skills/github-actions/SKILL.md` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `.claude/skills/mcp-server-design/SKILL.md` | Inspection reached its configured runtime limit\. |
| static\_parse\_limit | `.claude/skills/mcp-server-design/SKILL.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| runtime\_limit | `.claude/skills/reproducing-ci-locally/SKILL.md` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `.claude/skills/verifying-external-behavior/SKILL.md` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `.github/scripts/build_pages.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `.github/scripts/bump_contract_md.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `.github/scripts/bump_roadmap_md.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `.github/scripts/design_decisions_index.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `.github/scripts/resolve_version.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `.github/workflows/ci.yml` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `.github/workflows/dependabot-auto-merge.yml` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `.github/workflows/release.yml` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `CHANGELOG.md` | Inspection reached its configured runtime limit\. |
| obfuscated\_instruction\_text | `CHANGELOG.md` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |
| static\_parse\_limit | `CHANGELOG.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| runtime\_limit | `README.md` | Inspection reached its configured runtime limit\. |
| static\_parse\_limit | `README.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| runtime\_limit | `SKILL.md` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `SKILL.md` | Inspection reached its configured runtime limit\. |
| reference\_unresolved | `SKILL.md:30-30` | A local path\-like reference matched more than one bundled artifact and could not be resolved to a single target\. |
| reference\_unresolved | `SKILL.md:37-37` | A local path\-like reference matched more than one bundled artifact and could not be resolved to a single target\. |
| reference\_unresolved | `SKILL.md:62-62` | A local path\-like reference matched more than one bundled artifact and could not be resolved to a single target\. |
| reference\_missing | `SKILL.md:83-83` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| reference\_missing | `SKILL.md:90-90` | A local path\-like reference does not match any bundled artifact, such as a file the skill writes at runtime\. |
| runtime\_limit | `bin/install.js` | Inspection reached its configured runtime limit\. |
| static\_parse\_limit | `bin/install.js` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| runtime\_limit | `demos/CI.md` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `demos/build.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `demos/pages_videos.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/contract.md` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `docs/design-decisions.md` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `evals/contract/check.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `evals/grade_runs_24.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `evals/results/iteration-14-independent-grades.json` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `evals/results/iteration-16-independent-grades.json` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `evals/results/iteration-2-4-independent-grades.json` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `evals/results/iteration-2-4.json` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `evals/trigger/prompts.json` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `evals/write_fixtures.py` | Inspection reached its configured runtime limit\. |
| obfuscated\_instruction\_text | `examples/README.md` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |
| runtime\_limit | `package.json` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `references/gotchas.md` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `references/process-pitfalls.md` | Inspection reached its configured runtime limit\. |
| obfuscated\_instruction\_text | `references/requests.md` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |
| runtime\_limit | `references/scripts.md` | Inspection reached its configured runtime limit\. |
| static\_parse\_limit | `references/scripts.md` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| runtime\_limit | `scripts/_common/__init__.py` | Inspection reached its configured runtime limit\. |
| static\_parse\_limit | `scripts/_common/__init__.py` | A security\-relevant expression exceeded a bounded static parser's span limit\. |
| runtime\_limit | `scripts/_common/asr.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/_common/decision.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/_common/drawtext.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/_common/drawtext.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/_common/emit.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/_common/emit.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/_common/emoji.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/_common/emoji.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/_common/fonts.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/_common/fonts.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/_common/probe.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/_common/runner.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/_common/runner.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/_common/text.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/_common/timeline.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/_common/wrap.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/_contract.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/_contract.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/_platforms.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/audio.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/audio.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/background.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/batch.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/broll.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/caption.py` | Inspection reached its configured runtime limit\. |
| obfuscated\_instruction\_text | `scripts/caption.py` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |
| runtime\_limit | `scripts/caption.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/check.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/color.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/color.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/crop.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/cropdetect.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/cut.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/deinterlace.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/denoise.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/export.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/fit.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/freeze.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/graphics.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/graphics.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/grid.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/insert.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/join.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/join.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/look.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/loop.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/loudness.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/metadata.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/metadata.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/multicam.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/overlay.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/pad.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/probe.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/proxy.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/redact.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/render.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/render.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/report.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/reverse.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/reverse.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/scenes.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/sequence.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/silence.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/speedramp.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/sphere.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/stabilize.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/straighten.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/sync.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/verify.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/verify.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `scripts/waveform.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `site/brand/favicon.svg` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `site/brand/ffmpeg-skill-horizontal-on-dark.svg` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `site/brand/ffmpeg-skill-symbol-on-dark.svg` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `site/brand/velisa-horizontal-on-dark.svg` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `site/brand/velisa-horizontal.svg` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `site/index.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `site/index.html` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `templates/audiogram.json` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `templates/facebook.json` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `templates/linkedin.json` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `templates/podcast.json` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `templates/reels.json` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `templates/shorts.json` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `templates/tiktok.json` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `templates/x.json` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `templates/youtube-shorts.json` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `templates/youtube.json` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/_fixtures.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/_fixtures.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/bench_scenes.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/bench_scenes.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/bench_silence.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/bench_silence.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/bench_sync.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/bench_sync.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/bench_vt.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/bench_vt.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/corpus.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/corpus.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/fixtures/README.md` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/fixtures/caption_1_16_1_fitsize_off.ass` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/fixtures/ffmpeg_bsfs_6.1.txt` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/fixtures/ffmpeg_bsfs_8.1.2_macos.txt` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/fixtures/ffmpeg_bsfs_9.0.1_windows.txt` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/fixtures/ffmpeg_encoders_6.1.txt` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/fixtures/ffmpeg_encoders_6.1_no_aac.txt` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/fixtures/ffmpeg_encoders_8.1.2_macos.txt` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/fixtures/ffmpeg_encoders_9.0.1_windows.txt` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/fixtures/ffmpeg_filters_6.1.txt` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/fixtures/ffmpeg_filters_6.1.txt` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/fixtures/ffmpeg_filters_7.1_constructed.txt` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/fixtures/ffmpeg_filters_7.1_constructed.txt` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/fixtures/ffmpeg_filters_8.1.2_macos.txt` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/fixtures/ffmpeg_filters_8.1.2_macos.txt` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/fixtures/ffmpeg_filters_9.0.1_windows.txt` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/fixtures/ffmpeg_filters_9.0.1_windows.txt` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/fixtures/ffmpeg_filters_garbage.txt` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/fixtures/mcp_tools.json` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/release_check.sh` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/run_parallel.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/run_parallel.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/test_accel.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/test_accel.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/test_all.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/test_analysis.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/test_analysis.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/test_asr.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/test_asr.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/test_audio.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/test_audio.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/test_contract.py` | Inspection reached its configured runtime limit\. |
| obfuscated\_instruction\_text | `tests/test_contract.py` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |
| runtime\_limit | `tests/test_contract.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/test_cut_copy.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/test_cut_copy.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/test_delivery.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/test_delivery.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/test_editing.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/test_editing.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/test_orchestration.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/test_orchestration.py` | Inspection reached its configured runtime limit\. |
| runtime\_limit | `tests/test_picture.py` | Inspection reached its configured runtime limit\. |
| obfuscated\_instruction\_text | `tests/test_picture.py` | Obfuscated instruction text could not be fully evaluated by the deterministic layer\. |
| runtime\_limit | `tests/test_picture.py` | Inspection reached its configured runtime limit\. |

### Analyzer Statuses

| Reason / Status | Location | Details |
|-----------------|----------|---------|
| completed | `artifact_integrity` |  |
| completed | `behavioral_ast` |  |
| completed | `behavioral_taint_tracking` |  |
| completed | `bundled_execution_surface` |  |
| completed | `mcp_least_privilege` |  |
| completed | `mcp_rug_pull` |  |
| completed | `mcp_tool_poisoning` |  |
| degraded | `meta_analyzer` |  |
| completed | `reference_coverage` |  |
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
- Analyzer meta\_analyzer status: degraded\.

## Metadata

- **Executable Scripts:** Yes

*Generated by SkillSpector v2.12.0*

