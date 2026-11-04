# Upstream (third-party project)

Harvey is an open-source project by someone else. `app\` is a full clone, including its own `.git` history. Its files are NOT edited here.

| Item | Value |
|---|---|
| Upstream remote (origin) | https://github.com/ethanplusai/harvey |
| Commit copied | 6b6a23a789090e165802baef4104ee4618a3e169 (Merge pull request #160, 2026-11-01) |
| Package version | harvey 0.3.0 (pyproject.toml) |
| Licence | MIT (app\LICENSE) |
| Copied from | D:\All Automations Records\Harvey\ on 2026-11-05 (original untouched) |
| Local changes | none (working tree clean at copy time; `.venv`, `harvey.egg-info`, caches not copied) |

Update to a newer upstream (optional, needs Git):
```
git -C app pull origin main
```
Then delete `app\.venv` and run `install\INSTALL.cmd` again.
