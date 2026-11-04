# Level Up VFX CRM: how to use it

Site: https://levelup-vfx-crm-sigma.vercel.app (works on phone, tablet and computer).

## 1. First login and your password
1. Open the site and log in with your email and the password you were given.
2. The first time, the CRM asks you to choose a new password. It needs at least 8 characters, an upper case letter, a lower case letter and a number.
3. Click **Save password**. You land on the Home page.
4. Use the eye icon in any password box to show or hide what you typed.
5. Only one device can be logged in per account. If you log in somewhere else, the first device is signed out within seconds and shows "Signed in elsewhere".

## 2. Forgot your password
1. On the login page click **Forgot password?** (inside the password box).
2. Enter your email and click **Send code**.
3. Check your inbox for a 6-digit code. It works once and expires in 10 minutes.
4. Enter the code and a new password, then click **Verify code and save**.

The code only works for the email it was sent to. Note: sending codes needs the Gmail app password to be set up (see "What still needs the admin" below).

## 3. Set duty hours (admin)
1. Go to **Settings** (bottom of the left rail).
2. In the workday section set the shift start and end, the **clock-in window** and the **clock-out window** (times are Pakistan time, Asia/Karachi).
3. To give one person different hours, use **Per-employee hours**: pick the person, fill only the fields that differ, click **Save**. Blank fields use the workspace hours.

Outside these windows the Clock In / Clock Out buttons stay visible but greyed out with the reason underneath.

## 4. Add team members (admin)
1. Go to **Team** in the left rail.
2. Click **Add member**. Fill in **Name**, **Email**, **Role** (type any job title, for example "Video Editor" or "Outreach Specialist") and an **Initial password** (or click **Generate**).
3. Click **Add**. Give the person their email and initial password yourself. They must change it on first login.
4. To change someone's job title later, click it in the team list, type the new one and press Enter.
5. **Make admin / Remove admin** changes access level. The last admin can never be removed.
6. **Deactivate** removes access but keeps their history.

## 5. Create teams (admin)
1. Go to **Teams** in the left rail and click **New team**.
2. Type a name, then add members (you can pick several).
3. Rename a team by clicking its name. Delete it with the delete button (you will be asked to confirm).

## 6. Assign tasks (admin)
1. Go to **Home → Tasks** (or a team's page) and click **New task**.
2. Fill in title, description, deadline, priority and status.
3. Under **Assignees** pick one or more people. Under **Teams** pick one or more teams.
4. A task given to a team is seen by every member of that team, inside the **Teams** section, and by nobody else.
5. Open any task to see its **Comments**, **Activity** (who changed what) and **Contributors**.

## 7. Clock in and out
1. On **Home**, click **Clock In** at the start of your shift and confirm.
2. Click **Clock Out** at the end and confirm.
3. You can clock in once and out once per day, only inside the duty windows.
4. Forgot to clock out? Your next clock-in closes the old entry at that day's shift end and marks it for the admin to check.
5. The admin can correct any entry from the **Timesheet** page.

## 8. Reports
1. Employees: go to **Reports → Hourly** or **Daily**, fill in the report and click **Submit**. Once submitted it is locked.
2. Admin: open the report, add remarks, then **Approve** or **Request revision**. A revision unlocks it for the employee.
3. Employees can comment on their own daily reports.

## 9. Customise the CRM (admin)
**Settings → Branding & apps**: CRM name, logo, theme colour, default light/dark theme, and which apps show in the left rail (rename, change icon, reorder, hide).

## What employees can do
- Log in and change their own password.
- Clock in and out (once a day, inside the duty windows).
- Write and submit their own hourly and daily reports, and comment on their own daily reports.
- See only tasks assigned to them or to their team.
- Change the **status** of those tasks and add comments.

Everything else (tasks, projects, teams, members, job titles, duty hours, settings, documents, approvals) is admin only. The database itself enforces this, so it can't be bypassed from the browser.

## What still needs the admin (one-time)
1. **Gmail app password**, so reset codes can be emailed: open https://myaccount.google.com/apppasswords as Khizarvfx@gmail.com, create one named "Level Up VFX CRM", copy the 16 letters, then tell Claude "copied".
2. Nothing else is required to start using the CRM.
