# Apps standard (for Claude sessions)

1. Every app lives in `F:\Github Repos\projects\<app-name>\`, fully self-contained and movable by copying the folder.
2. Layout: README.md, SETUP-GUIDE.md, GUIDE\ (chapters 00-05), install\, app\, database\, docs\, notes\, proof\, reference\, archive\, backups\, secrets\. Start from `_TEMPLATE\`. Details: `projects\README.md`.
3. README.md = start here + folder map. SETUP-GUIDE.md = the 10-section roadmap for a non-expert (Windows 10, numbered steps) and links to the detailed chapters in `GUIDE\`.
4. `install\INSTALL.cmd` (double-click) calls `install.ps1`; it must support `-Check` and restore frontend, backend, database, Supabase functions, hosting and sheet access.
5. `app\` holds source and has its own git. Never edit or install in `app\` while another session builds there.
6. `database\` has a README and a restore method; `backups\backup.ps1` makes the dated folder zip + DB export (outputs gitignored); refresh before big changes.
7. `secrets\` is the ONE secrets folder (never `private\`), gitignored by the hub (`projects/*/secrets/`); it holds `.env`, key files, account lists. `SECRETS-CHECKLIST.md` lists each secret NAME, where it is used and how to get it.
8. NEVER print or copy secret VALUES into any guide, chat, log or commit.
9. Never delete anything; move old or unused files to `archive\`.
10. Keep docs\ current (roadmap, brief, features, audit, prices); keep proof\ for screenshots and test output.
11. Update the project CLAUDE.md "Status / next step" and `projects\README.md` whenever an app is added or changes state.
12. The app standard also applies: email+password login, one active session, code-based password reset, full admin portal.
