# Credential setup: click paths (checked 2026-11-03)

Read-only research. Nothing changed in any console.
- **Done:** Supabase, Google Cloud OAuth, service-account/Sheets paths researched from official pages (raw markdown or raw HTML text, quotes checked by grep).
- **Not done:** no project, client or key created.
- **Not verified:** listed in section 4. Those items are marked "not verified" below.

---

## 1. Supabase

### 1a. Create a project (Free plan)
Doc: https://supabase.com/docs/guides/getting-started/quickstarts/nextjs
1. Open the dashboard new-project page (https://supabase.com/dashboard/new/_). Quote: "Create a new Supabase project from the Dashboard of any organization you belong to."
2. Fill the form. Quote (Multigres docs page, "Multigres", URL not confirmed): "Finish the remaining fields such as database password, region, and compute size, if shown."
   - Field labels "Name", "Database password", "Region" as exact UI text: not verified.
3. Click **Create new project**. Quote: "Click **Create new project**." (same Multigres page; this is the only official source for the button label, so the standard form label is not verified).
4. Plan: choose Free. Plan selector label: not verified.
   - Free plan limit. Quote: "Limit of 2 active projects." Sources checked 3x: https://supabase.com/pricing (2026-11-03), https://supabase.com/docs/guides/platform/billing-on-supabase ("You are granted two free projects."), and the Supabase full docs index.
5. Save the database password. Reset path, quote (Laravel quickstart, "Use Supabase with Laravel", URL not confirmed): "If you don't have your database password, you can reset it in your Database Settings." Database Settings URL: https://supabase.com/dashboard/project/_/database/settings

### 1b. Session pooler connection string (port 5432)
Doc: https://supabase.com/docs/guides/database/connecting-to-postgres
1. Open your project in the dashboard.
2. Click **Connect** at the top of the page. Quote: "Click **Connect** at the top of the page."
3. In the Connect dialog choose **Session pooler**. Quote: "Get this string from the Supabase Dashboard by clicking Connect and choosing Session pooler."
   - Direct link: https://supabase.com/dashboard/project/_?showConnect=true&method=session
4. Copy the URI and replace the password placeholder. Quote: "Copy the string and replace `[YOUR-PASSWORD]` with your database password."
5. Check the port. Quote: "Port 5432 reaches Postgres for a direct connection and the shared pooler for session mode."

### 1c. Turn off public sign-ups
Doc: https://supabase.com/docs/guides/auth/general-configuration
1. Dashboard left menu: **Authentication**, then **Sign In / Providers**. Quote: "Sign In / Providers to configure authentication providers and sign-in methods for your users."
   - Direct link: https://supabase.com/dashboard/project/_/auth/providers
2. Turn OFF the toggle **Allow new users to sign up**. Quote: "If this config is disabled, only existing users can sign in."
3. Exact on-page position of the toggle: not verified.
4. Do not confuse with **Confirm Email**, which the same page describes as a separate provider-level option.

### 1d. Create a user by hand
Doc: https://supabase.com/docs/guides/auth/users (section "Inviting users")
1. Go to **Authentication > Users** in the Dashboard. Quote: "Go to **Authentication > Users** in the Dashboard."
2. Click **Add user** and select **Send invitation**. Quote: "Click **Add user** and select **Send invitation**."
3. Enter the email and click **Invite user**. Quote: "Enter the user's email address and click **Invite user**."
- The invited user finishes setup from the email link, "for example, by setting a password."
- Creating a user with a password chosen in the dashboard: not verified (no official step found).

### 1e. SQL Editor (run a .sql file)
Doc: https://supabase.com/docs/guides/database/functions
1. Open the **SQL Editor** section. Quote: "Go to the **SQL Editor** section."
   - Direct link: https://supabase.com/dashboard/project/_/sql
   - Sidebar icon position: not verified.
2. Click **New Query**. Quote: "Click **New Query**."
3. Open the .sql file in a text editor, copy all text, paste it into the query box, then click **Run**. Quote: "Click **Run**. You can also press `cmd+enter` or `ctrl+enter`."
- No file-upload option for .sql found in the docs. Paste the contents.

---

## 2. Google Cloud (OAuth for Gmail)

### 2a. Create a project
Doc: https://developers.google.com/workspace/guides/create-project
1. Menu > IAM & Admin > Create a Project. Quote: "In the Google Cloud console, go to Menu menu > IAM & Admin > Create a Project."
2. Type a name in the Project Name field. Quote: "In the Project Name field, enter a descriptive name for your project."
3. Location: click **Browse**, then **Select**. Quote: "In the Location field, click Browse to display potential locations for your project. Then, click Select."
4. Click **Create**. Quote: "Click Create."

### 2b. Enable Gmail API and Google Sheets API
Doc: https://developers.google.com/workspace/guides/enable-apis
1. Menu > APIs & Services > Library > Google Workspace. Quote: "In the Google Cloud console, go to Menu menu > APIs & Services > Library > Google Workspace."
2. Click the API (Gmail API, then Sheets API). Quote: "Click the API that you want to turn on."
3. Click **Enable**. Quote: "Click Enable."

### 2c. OAuth consent screen (Google Auth Platform), External, publish
Docs: https://developers.google.com/workspace/guides/configure-oauth-consent ; https://support.google.com/cloud/answer/15549945?hl=en ; https://support.google.com/cloud/answer/15549049
1. Open Google Auth Platform: Menu > Google Auth platform. Quote (create-credentials page): "go to Menu menu > Google Auth platform > Clients."
2. Sections per the help-center nav: Branding ("Manage OAuth App Branding"), Audience ("Manage App Audience"), Data Access ("Manage App Data Access"). Exact sidebar labels: not verified.
3. Audience: choose External. Quote: "Under Audience, select the user type for your app."
   - Internal (Workspace org only) removes the 100-user cap: "All users within your organization can access. Verification is not required." (overview page, https://developers.google.com/identity/protocols/oauth2/production-readiness/overview)
4. While testing, add yourself: Audience > Test users > Add users > Save. Quote: "Under Test users, click Add users."
5. Publish: click **Publish app**. Quote: "A project's publishing status is considered In production after selecting the Publish app button." The button sits on the Audience page. Quote: "Manage your app publishing status in the Audience page of the Google Auth Platform."

### 2d. OAuth client ID, type Desktop app
Doc: https://developers.google.com/workspace/guides/create-credentials
1. Menu > Google Auth platform > Clients.
2. Click **Create Client**. Quote: "Click Create Client."
3. **Application type** > **Desktop app**. Quote: "Click Application type > Desktop app."
4. Type a name in the **Name** field. Quote: "In the Name field, type a name for the credential."
5. Click **Create**. Quote: "Click Create."
6. Copy client ID and client secret, or download JSON: not verified (the page does not describe this for Desktop app clients).

### 2e. gmail.modify, warning screen, user caps
- **gmail.modify is a restricted scope.** Doc: https://developers.google.com/workspace/gmail/api/auth/scopes . The row sits under the "Restricted scopes" table. Quote: "These scopes provide wide access to Google user data and require restricted scope OAuth App Verification."
- Storing restricted data on servers adds an audit. Quote: "If you store restricted scope data on servers (or transmit), then you must go through a security assessment."
- **Warning users see.** Doc: https://developers.google.com/identity/protocols/oauth2/production-readiness/brand-verification . Quote (screenshot alt text): "Warning message that Google hasn't verified an app that's undergoing testing." On-screen title text: not verified.
- Published app with restricted scopes, not verified: "unverified app warnings (Danger UI) will be displayed to users, and a hard cap of 100 total users applies." (overview page, linked above)
- **Testing status cap:** "limited to up to 100 test users listed in the OAuth consent screen." (https://support.google.com/cloud/answer/15549945?hl=en)
- Test-user tokens expire: "Authorizations by a test user will expire seven days from the time of consent." (same page)
- Rate-limit row for unverified-app screen: "Apps that present the unverified app screen to users | 100 new users in total." (same page)
- Verification removes the warning and cap. Quote (overview): "Required for public apps that request sensitive and restricted scopes."
- Net effect: a published app that asks for gmail.modify shows the unverified warning and stops at 100 total users until Google verifies it.

---

## 3. Service account for Sheets

### 3a. Create the service account
Doc: https://docs.cloud.google.com/iam/docs/service-accounts-create
1. Open the Create service account page. Quote: "In the Google Cloud console, go to the Create service account page."
2. Enter a name. Quote: "Enter a service account name to display in the Google Cloud console."
3. Skip roles and click **Done**. Quote: "If you don't want to set access controls now, click Done to finish creating the service account."
- Whether Sheets needs any project IAM role: not verified. The documented grant is sharing the sheet (3c).

### 3b. Create a JSON key
Doc: https://docs.cloud.google.com/iam/docs/keys-create-delete (redirects from cloud.google.com)
1. Open the Service accounts page and click the service account email.
2. Click the **Keys** tab. Quote: "Click the Keys tab."
3. Click the **Add key** drop-down, then **Create new key**. Quote: "Click the Add key drop-down menu, then select Create new key."
4. Select **JSON** as the Key type and click **Create**. Quote: "Select JSON as the Key type and click Create."
5. The file downloads once. Quote: "After you download the key file, you cannot download it again."
6. Store the file outside the repo and reference it from `.env` (gitignored). Quote: "Always store your service account keys in a secure location."

### 3c. Share each Sheet with the service account
Doc: https://developers.google.com/workspace/guides/create-credentials
1. Open the spreadsheet and click **Share**. Quote: "Open the Sheets document or Drive folder you want to access. Click Share."
2. Add the service account email and choose access. Quote: "Add the service account's email address and assign the appropriate access level (such as Editor or Viewer)."
3. Deselect **Notify people**, then click **Share**.
- Read-only scope name (spreadsheets.readonly) on an official page: not verified.

### 3d. Can the org policy block key creation?
Docs: https://docs.cloud.google.com/resource-manager/docs/manage-baseline-constraints ; https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts
- Yes. Constraint "Disable service account key creation" = `constraints/iam.managed.disableServiceAccountKeyCreation`. Quote: "Prevent users from creating persistent keys for service accounts."
- Default: "Google Cloud security baseline constraints are enforced for all organizations created on or after May 3, 2024." Quote also: "Some organizations created between February 2024 and April 2024 might also have these default policy enforcements set."
- Effect: "When this constraint is set, user-managed credentials cannot be created for service accounts in projects affected by the constraint."
- Caution: the restricting-service-accounts page has a separate sentence, "If your organization was created on or after May 3, 2024, this constraint is enforced by default." It sits under the automatic IAM grants constraint, not key creation. Do not mix them up.
- If blocked: key creation fails. Exact error text: not verified. Exemption tag and the console path to change the policy: not verified on fetched official pages.

---

## 4. Not verified (summary)
1. Supabase: exact create-project field labels ("Name", plan selector) and the standard "Create new project" button.
2. Supabase: on-page position of the "Allow new users to sign up" toggle.
3. Supabase: creating a user with a password in the dashboard (only invite flow documented).
4. Supabase: SQL Editor sidebar icon; .sql file upload (none documented).
5. Google: Desktop app client secret / JSON download.
6. Google: sidebar labels Branding / Audience / Data Access (help-center names only).
7. Google: exact on-screen title of the unverified-app warning.
8. Google: project-level exemption from the key-creation constraint and the console path to change org policy.
9. Google: read-only Sheets scope name on an official page.
