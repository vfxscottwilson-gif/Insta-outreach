# 03 How to change things

| I want to... | Do this |
|---|---|
| Change a setting (time zone, sync interval, app name, accent) | Edit the key in `secrets\.env`, run `install\INSTALL.cmd` (copies it), restart the app. Keys listed in `docs\START_HERE.md` section 7 |
| Add/remove a lead sheet | In the app: Sources & sync. Or `secrets\sources.yaml` (template `app\dashboard\sources.example.yaml`) |
| Change niche categories | `secrets\categories.yaml` (template `categories.example.yaml`) |
| Add an employee / reset a password | Admin portal -> Users. Owner reset: `install\create-admin.cmd` |
| Run the tests | In `app\dashboard`: `.venv\Scripts\python.exe -m pytest tests -q -p no:cacheprovider` |
| Back up | `backups\backup.ps1` |
| Change the code | Edit under `app\dashboard\dash\`; commit in the `app` git repo. Do not edit while another chat is building there |
| Rotate the password key | `manage.py rotate-password-key` (then update `DASH_PASSWORD_KEY` in `secrets\.env` from `app\dashboard\.env`) |

Do not edit the sheets' `My Notes` column; write-back is limited to agreed columns.
