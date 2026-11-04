# Editor Tracker: implementation spec (final, 2026-11-04)

Per-task video checklist, copied from one admin-editable template. Employees tick items on their own or their team's tasks; the server stamps who/when; progress rolls up into `tasks.progress`, bars in the UI, a new "Editor Checklist" sheet tab. Free Supabase features only. Patterns follow `20261104000011` (guard triggers, `private.only_changed`, `is_privileged`) and `20261104000012` (`assigned_task_ids()` / `visible_task_ids()`, policies, audit, realtime).

## 1. Data model (migration `supabase/migrations/20261104000040_editor_tracker.sql`)

One template only (no template id). Positions are plain integers, ordered by `(position, id)`; no unique constraint on position (reorders rewrite positions in a batch).

| Table | Columns | Constraints / indexes |
|---|---|---|
| `checklist_template_stages` | `id uuid pk default gen_random_uuid()`, `name text not null`, `position int not null default 0`, `created_at`, `updated_at timestamptz not null default now()` | `check (char_length(btrim(name)) between 1 and 80)` |
| `checklist_template_items` | `id uuid pk`, `stage_id uuid not null references checklist_template_stages on delete cascade`, `label text not null`, `position int not null default 0`, `created_at`, `updated_at` | `check (char_length(btrim(label)) between 1 and 160)`; index `(stage_id, position)` |
| `task_checklist_stages` | `id uuid pk`, `task_id uuid not null references tasks on delete cascade`, `name text not null`, `position int not null default 0`, `created_at`, `updated_at` | same name check; index `(task_id, position)` |
| `task_checklist_items` | `id uuid pk`, `task_id uuid not null references tasks on delete cascade`, `stage_id uuid not null references task_checklist_stages on delete cascade`, `label text not null`, `position int not null default 0`, `checked boolean not null default false`, `checked_by uuid references profiles on delete set null`, `checked_at timestamptz`, `created_at`, `updated_at` | same label check; `check ((checked and checked_at is not null) or (not checked and checked_by is null and checked_at is null))`; indexes `(task_id)`, `(stage_id, position)`, `(checked_by)` |

`task_id` is denormalised onto items so every policy is one `task_id in (...)` test. Triggers on all four tables: `set_updated_at` (before update) and `private.write_audit()` (after insert/update/delete), same `do $$ foreach` pattern as `20261104000012`.

Grants: `revoke all ... from anon, authenticated;` then `grant select, insert, update, delete` on all four to `authenticated` (RLS decides), and `grant select` on `task_checklist_stages, task_checklist_items` to `service_role` (sheets-sync reads them; cf. `20261104000015`). RLS enabled on all four.

Seed (in the migration, `insert ... select` with positions 1..n): the 7 default stages and their items exactly as listed in the brief (Intake 3, Base cut 4, Hook and structure 3, Audio 5, Colour 3, Motion graphics and VFX 4, QC and delivery 7 = 29 items).

## 2. Attaching a checklist: `apply_checklist_template(p_task_id uuid) returns int`

`language plpgsql security definer set search_path = ''`. Steps: (1) `if not private.is_current_session() or not private.is_admin() then raise exception 'not allowed: only an admin can add a checklist' using errcode = '42501'`; (2) task must exist (`raise exception 'task not found'`); (3) `if exists (select 1 from public.task_checklist_stages where task_id = p_task_id) then raise exception 'task already has a checklist'`; (4) insert stages copying `name, position` from the template, keeping a `template_stage_id -> new_stage_id` map (CTE with `returning`), then insert items copying `label, position`; (5) return the item count. `revoke all on function ... from public, anon; grant execute to authenticated`. Removing a checklist = admin deletes the task's stages (cascade); no RPC. Template edits never touch `task_checklist_*` rows: copy semantics are guaranteed by the absence of any FK back to the template.

## 3. RLS and guard rules

All policies start with `(select private.is_current_session()) and ...`, like every policy in `20261104000012`.

| Table | select | insert / delete | update |
|---|---|---|---|
| `checklist_template_*` | any authenticated | admin only | admin only |
| `task_checklist_stages` | admin or `task_id in (select private.visible_task_ids())` | admin only | admin only |
| `task_checklist_items` | admin or `task_id in (select private.visible_task_ids())` | admin only | admin or `task_id in (select private.assigned_task_ids())` (using + with check) |

Guard trigger `private.guard_task_checklist_item()` (before update, security definer, `search_path = ''`):
1. If `new.checked is distinct from old.checked`: server overwrites `new.checked_by := case when new.checked then auth.uid() end` and `new.checked_at := case when new.checked then now() end`. Client values of these two columns are always ignored, admin included.
2. If `new.checked = old.checked`: force `new.checked_by := old.checked_by; new.checked_at := old.checked_at` (nobody rewrites history without re-ticking).
3. If `not private.is_privileged()` and `not private.only_changed(to_jsonb(old), to_jsonb(new), array['checked','checked_by','checked_at','updated_at'])` then `raise exception 'not allowed: you can only tick or untick checklist items' using errcode = '42501'`. Also raise if `new.task_id <> old.task_id or new.stage_id <> old.stage_id` for anyone (items never move between tasks).

So the employee write scope grows by exactly one line in SECURITY-AUDIT: "task_checklist_items: tick/untick (`checked`) on tasks assigned to them or their team".

## 4. Progress

- View `public.task_checklist_stage_progress` (`security_invoker = true`, grant select to authenticated): `task_id, stage_id, position, name, total int, done int, percent int` = `round(100.0 * done / total)`, 0 when `total = 0`. One row per `task_checklist_stages` row. RLS of the base tables applies, so employees only see their tasks.
- Task percent = `round(100.0 * checked items / all items)` across the whole task (every item weighs 1; stages are not weighted). `tasks.progress` is kept equal to it by trigger `private.sync_task_progress()` (after insert, update of `checked`, delete on `task_checklist_items`; security definer): computes for `coalesce(new.task_id, old.task_id)`; if the task still has items, `perform set_config('levelup.system', 'on', true); update public.tasks set progress = pct where id = ...; perform set_config('levelup.system', coalesce(prev, ''), true)` (save/restore the previous flag value so the privilege does not leak to the rest of the transaction). If no items remain (checklist removed), `tasks.progress` is left as is. This is the only way an employee tick reaches `tasks.progress`: `guard_task` still forbids employees writing `progress` directly and that rule does not change.
- UI rule: when a task has a checklist, the progress slider in `TaskPanel` is disabled with caption "From checklist"; admin changes progress by ticking.

## 5. Realtime: yes, narrowly

`alter publication supabase_realtime add table public.task_checklist_items;` The client subscribes only while a video is open (`postgres_changes`, `filter: task_id=eq.<id>`), and unsubscribes on close. The tracker list needs no new channel: `tasks` is already live (`tasks-live` in DataContext) and `tasks.progress` is trigger-maintained; stage bars refetch the view when `loadTasks` runs.

## 6. Tests

**check-db (`scripts/check-db.mjs`, one block appended at the very end before the final `console.log`, by engineer B only, headed `// --- editor tracker (20261104000040) ---`).** Fixtures: `T1` assigned to `E1`, `T2` to `E2` already exist; the block creates team `TM1` with member `E2` and task `T3` linked to `TM1` via `task_teams`.
1. seed: 7 template stages, 29 template items.
2. employee cannot insert/update/delete template rows (3 `denied`).
3. admin can rename a template item; `apply_checklist_template(T1)` afterwards copies the renamed label; the copy on T2 made before the rename keeps the old label (copy semantics).
4. `apply_checklist_template` by E1 is denied; by admin on a missing task raises; a second call on T1 raises "already has a checklist".
5. E1 ticks an item of T1: `checked_by = E1`, `checked_at` within 5 s of `now()`; client-supplied `checked_by = A` is overwritten with E1.
6. E1 unticks: `checked_by` and `checked_at` are null.
7. E1 updating `label` or `position` on T1 is denied; E1 updating `checked_by` alone leaves it unchanged.
8. E2 ticking an item of T1 is denied (RLS: 0 rows); E2 cannot select T1's stages/items/view rows (count 0); E1 sees 29 items of T1.
9. team scope: E2 (member of TM1) ticks an item of T3 OK; E1 (non-member) sees 0 rows of T3 and is denied.
10. progress: after E1 ticks 3 of 29 on T1, `tasks.progress = 10` and view row for Intake = `done 3 total 3 percent 100`; untick one gives 7; E1 direct `update tasks set progress = 50` still denied; stale session (`e1Stale`) tick denied.
11. admin deletes T1's stages: items cascade, `tasks.progress` keeps its last value; `audit_log` has rows for `task_checklist_items` updates.
12. structure: RLS enabled on the 4 tables (the existing "RLS enabled on every public table" check covers it); `anon` cannot read the template.

**pgTAP: new file `supabase/tests/database/editor_tracker.test.sql`** (own `plan(n)`, own fixtures, `begin ... rollback`; `rls.test.sql` untouched). Same cases 1-11 translated to `ok / is / throws_ok / lives_ok` with `set local role authenticated` and `request.jwt.claims` like `rls.test.sql`. Run: `supabase test db` against the hosted project, result rolled back.

## 7. UI (route `/editor-tracker`, React + Tailwind + `motion/react`, lucide icons)

Files (all new unless marked):
- `src/lib/checklist.ts`: types `ChecklistStage { id, taskId, name, position, items: ChecklistItem[] }`, `ChecklistItem { id, taskId, stageId, label, position, checked, checkedBy, checkedAt }`, `StageProgress { taskId, stageId, name, position, total, done, percent }`; `loadChecklist(taskId)`, `loadStageProgress()` (view, all visible tasks, one query), `tickItem(id, checked)` (`update ... set checked` only), `applyTemplate(taskId)` (rpc), `remaining(stages)` (unchecked items in order), `nextItem(stages)`. Pure helpers get a `src/lib/checklist.test.ts` (vitest: percent maths, remaining order).
- `src/types/index.ts` (edit): re-export the three types above.
- `src/components/editor/EditorTrackerView.tsx`: page. Header "Editor Tracker"; status filter chips (statuses from `useData`, plus "All"; default = everything not Completed); grid of `VideoCard`s for tasks the user can work on (`canWork` logic copied from `TasksWorkspace`: admin sees all tasks that have a checklist, employee sees assigned/team). Empty state: "No videos with a checklist yet" (admin: "Open a task and add the editor checklist").
- `src/components/editor/VideoCard.tsx`: title, project, due label (`dueLabel` from `taskBits`), task `ProgressBar`, one thin bar per stage (7 stacked segments, stage name on hover/long-press), "N left · next: <label>"; tap opens `/editor-tracker/:taskId` (same route element, panel/sheet over the list; phone: full-screen sheet).
- `src/components/editor/VideoChecklist.tsx`: the staged checklist. Props `{ taskId, canTick, compact? }`. Loads via `loadChecklist`, subscribes to realtime for that task, optimistic toggle with rollback + toast on error. Stage header = name + `done/total` + animated bar; items = full-width rows, min height 56 px, 28 px round check control, label, and under it "Done by Name · 4 NOV 2026, 10:13 AM" (`formatDateTime` from `src/utils/dateFormat.ts`, names from `useData().users`). Toggle "What's left" hides checked items and empty stages. Motion: check control `whileTap={{ scale: 0.9 }}`, checkmark path draw-in and row fade with `SPRING_SOFT`, bar width animates with `SPRING`; all gated by `useLowMotion()` (reduced-motion users get instant changes). `touch-action: manipulation`, no hover-only affordances, no images.
- `src/components/editor/ChecklistTemplateEditor.tsx`: admin-only section mounted from `src/components/settings/SettingsView.tsx` (one import + one block, next to `SheetsSyncSettings`; route stays `/settings`): list stages and items, inline rename, add, delete (confirm), move up/down (batch position rewrite). Note under the title: "Changes apply to checklists added from now on; existing videos keep their copy."
- `src/components/tasks/TaskPanel.tsx` (edit): new "Editor checklist" block under progress. No checklist: admin sees button "Add editor checklist" (calls `applyTemplate`, then loads); employee sees nothing. With checklist: `<VideoChecklist compact canTick={isAdmin || ctx.canStatus(task)} />`; progress slider `disabled` with caption "From checklist"; admin gets "Remove checklist" (deletes stages, confirm dialog).
- Navigation (edits): `src/components/shell/nav.ts` add `editorTracker: { to: '/editor-tracker', label: 'Editor Tracker', icon: ListChecks }`; `SecondarySidebar.tsx` home list: insert after `NAV.myTasks`; `src/App.tsx` add `<Route path="/editor-tracker" element={<EditorTrackerView />} />` and `/editor-tracker/:taskId`, both inside `Shell` (not `AdminOnly`); add to `LEGACY_TAB_ROUTES` only if the command palette reads from NAV (it does: nothing more to do).

Low-data: list = 1 task query (already cached) + 1 view query; open video = 1 query + 1 filtered channel; no polling, no images, lazy-load the editor chunk (`React.lazy`).

## 8. Sheet mirror (`supabase/functions/sheets-sync`)

New `TabSpec` appended to `SPECS` in `mapper.ts`:
`{ name: 'Editor Checklist', idHeader: 'Item ID', textHeaders: ['Done At'], headers: ['Item ID', 'Task ID', 'Task Title', 'Assignee', 'Stage', 'Stage Order', 'Item', 'Item Order', 'Done', 'Done By', 'Done At'] }`.
Row per `task_checklist_items` row, sorted by id (`byId`): `Task Title` = task title, `Assignee` = same joined names as Tasks_Deadlines, `Stage` = stage name, `Stage Order`/`Item Order` = positions (numbers), `Done` = `yes`/`no`, `Done By` = profile name or blank, `Done At` = `formatDateTime(checked_at)` -> `4 NOV 2026, 10:13 AM` (Asia/Karachi) or blank.
`SyncData` gains `checklistStages: Row[]; checklistItems: Row[]`; `index.ts` `runSync` loads them with `all(admin, 'task_checklist_stages')` and `all(admin, 'task_checklist_items')`.
Tasks_Deadlines `Progress Percent`: unchanged code (`t.progress`), which the trigger in section 4 keeps equal to the checklist percent whenever the task has one. Document this in a one-line comment next to the column.
Tests: extend `src/lib/sheetsMapper.test.ts` with: tab present with exact headers; one row per item; `Done At` format; blank when unchecked; task without a checklist produces no rows.

## 9. Work split (5 engineers, disjoint files, all can start now)

| Eng | Files (only these) | Done when |
|---|---|---|
| **B** DB | NEW `supabase/migrations/20261104000040_editor_tracker.sql`; NEW `supabase/tests/database/editor_tracker.test.sql`; `scripts/check-db.mjs` (one appended block, nothing else edited) | `npm run check:db` ALL PASSED incl. the 12 groups in section 6; pgTAP file runs green on hosted (`supabase test db`), output pasted in PR; `supabase db push` applied; `select count(*) from checklist_template_items` = 29 on hosted |
| **C** UI | NEW `src/components/editor/*`, NEW `src/lib/checklist.ts` + `checklist.test.ts`; EDIT `src/types/index.ts`, `src/App.tsx`, `src/components/shell/nav.ts`, `src/components/shell/SecondarySidebar.tsx`, `src/components/tasks/TaskPanel.tsx`, `src/components/settings/SettingsView.tsx` | `npm run build` + `npm test` green; admin adds checklist from TaskPanel, edits template in Settings; employee ticks on phone viewport (375 px) with 56 px rows; "What's left" toggle; slider disabled when checklist exists; no console errors; screenshots in `proof/editor-tracker/` (phone + desktop, light + dark) |
| **D** Sheets | `supabase/functions/sheets-sync/mapper.ts`, `supabase/functions/sheets-sync/index.ts`, `src/lib/sheetsMapper.test.ts` | `npm test` green; `supabase functions deploy sheets-sync`; a sync creates tab "Editor Checklist" with the 11 headers and `Done At` as `4 NOV 2026, 10:13 AM`; Tasks_Deadlines `Progress Percent` matches the checklist for a task with one; screenshot of both tabs |
| **E** QA | NEW `scripts/qa-editor-tracker.cjs` (Playwright, pattern of `qa-logged-in.cjs`, uses `.env.test` accounts) | Script PASSes: admin applies template to a task assigned to employee A; A ticks 2 items on phone viewport and sees "Done by ... PKT" stamp; progress bar on `/my-tasks` panel shows the same %; employee B (not assigned) gets no card for that task and a direct `/editor-tracker/:id` shows "not available"; B's direct `update` via supabase-js in-page returns 0 rows; admin removes checklist. Screens saved to `proof/qa/editor-tracker/` |
| **F** Docs | `USER-GUIDE.md` (new section "10. Editor checklist"), `SECURITY-AUDIT.md` (new table row + RPC row for `apply_checklist_template`), `FEATURES.md` (entry), `app/CLAUDE.md` status line, `PROGRESS.md` row | Docs describe exactly what shipped (verified against B's migration and C's screens); no em-dashes; committed |

Order of truth: B's migration column names are final as written in section 1; C and D code against them without waiting. Integration check after merge: run `npm run check:db`, `npm test`, E's script, then one sheet sync.

## 10. Out of scope (decided)

Multiple templates, per-stage weights, item notes/attachments, reordering items inside an existing task's checklist by employees, a `task_events` kind for ticks (items carry who/when already), email/push on completion.
