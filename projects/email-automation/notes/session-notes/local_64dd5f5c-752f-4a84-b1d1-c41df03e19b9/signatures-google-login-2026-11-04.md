# Gmail signatures + Supabase Google login (checked 2026-11-04)

## 1. Scopes for sendAs
- sendAs.get and sendAs.list: any of gmail.settings.basic, https://mail.google.com/, gmail.modify, gmail.readonly.
  Sources: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.settings.sendAs/get and .../sendAs/list
  Quote: "Requires one of the following OAuth scopes:" (list as above)
- sendAs.update and sendAs.patch: ONLY gmail.settings.basic or gmail.settings.sharing.
  Sources: .../sendAs/update and .../sendAs/patch (same quote). gmail.modify is NOT listed, so it does NOT cover updating a signature.
- Google's own sample uses GmailScopes.GMAIL_SETTINGS_BASIC (https://developers.google.com/workspace/gmail/api/guides/alias_and_signature_settings).
- Only the primary address can be updated with a normal user token. Quote (update page): "Addresses other than the primary address for the account can only be updated by service account clients" (domain-wide delegation).

## 2. Classification
- https://developers.google.com/workspace/gmail/api/auth/scopes lists gmail.settings.basic, gmail.settings.sharing and gmail.modify all under "Restricted scopes" (not sensitive). Fetched twice, same result.
- Restricted needs restricted-scope OAuth verification (page: "provide wide access to Google user data").
- 100-user cap: https://support.google.com/cloud/answer/7454865 -> "100 new users in total, after the app presents the unverified app screen." Stated for unverified apps in general, so the same cap applies to settings.basic and modify. Separate "Testing status" test-user cap: not verified here.

## 3. Signature format
- HTML. Quote (sendAs resource): "An optional HTML signature that is included in messages composed with this alias in the Gmail web UI."
- Same page: "This signature is added to new emails only."
- Sanitization (update page): "If a signature is provided, Gmail will sanitize the HTML before saving it with the alias."
- Which tags and inline styles survive: NOT documented officially. Not verified. Only reliable check: patch, then get, and diff. Third-party claims (unverified): <style> blocks are stripped, inline styles kept.
- Max length: 10,000 characters per Gmail help (https://support.google.com/mail/answer/8395: "You can put up to 10,000 characters in your signature."). API docs state no limit; API limit not verified.
- Primary address: yes. Guide quote: "represents the primary email address of the account." Guide samples set the signature on the primary address. isPrimary doc: "Every Gmail account has exactly one primary address".

## 4. Editor fonts / sizes / colors
- Official docs name no fonts, sizes or colors (support.google.com/mail/answer/8395 checked: not documented).
- Font names in the editor (third-party, not official): Sans Serif, Serif, Fixed Width, Wide, Narrow, Comic Sans MS, Garamond, Georgia, Tahoma, Trebuchet MS, Verdana.
- CSS per font: NOT verified from an official source. A Stylus gist (https://gist.github.com/thundernixon/bd84eca959565db33390797807566f7d) shows old Gmail used font face="trebuchet ms, sans-serif", "arial black, sans-serif", "arial narrow, sans-serif". Likely stacks, from memory, UNVERIFIED: Serif "times new roman",serif; Fixed Width monospace; Wide "arial black",sans-serif; Narrow "arial narrow",sans-serif; Comic Sans "comic sans ms",sans-serif; Garamond garamond,"times new roman",serif; Georgia georgia,serif; Tahoma tahoma,sans-serif; Trebuchet "trebuchet ms",sans-serif; Verdana verdana,sans-serif. Sans Serif = default (no font-family).
- Sizes Small/Normal/Large/Huge to CSS: not verified (memory: small / default / large / x-large). Confirm by inspecting a draft in DevTools.
- Color palette hex values: not documented officially; not verified. Best route: DevTools on the signature editor.

## 5. Shows in new compose?
- Web: yes per docs: "included in messages composed with this alias in the Gmail web UI" and "added to new emails only".
- Mobile: separate setting. Quote (https://support.google.com/mail/answer/8395, Android tab): "Set up a signature that shows up only for emails you send from the Gmail app." Fallback quote: "If you don't create a signature in the Gmail app, new messages use the signature you created on your computer." iPhone text was not visible to me: iOS fallback not verified. Real device behaviour with an API-set signature: not tested.

## 6. Signup off + Google
- Docs (https://supabase.com/docs/guides/auth/general-configuration): "Users will be able to sign up. If this config is disabled, only existing users can sign in." Does not mention OAuth explicitly.
- Source (supabase/auth internal/api/external.go, CreateAccount branch): if config.DisableSignup then error "Signups not allowed for this instance" (422 signup_disabled); no account created.
- Real report: https://github.com/supabase/auth/issues/1677 : Google flow redirects with "error_code=422&error_description=Signups+not+allowed+for+this+instance".

## 7. Auto-linking
- https://supabase.com/docs/guides/auth/auth-identity-linking : "Supabase Auth automatically links identities with the same email address to a single user."
- Caution: "It would also be an insecure practice to automatically link an identity to a user with an unverified email address". Code reads Google email_verified (provider/google.go IsEmailVerified). So confirm the invited user's email (email_confirm true); case of an unconfirmed password user: not tested.

## 8. Redirect URI and scopes
- https://supabase.com/docs/guides/auth/social-login/auth-google : "Under Authorized redirect URIs add your Supabase project's callback URL." Shown on the Dashboard Google provider page. Local: http://127.0.0.1:54321/auth/v1/callback. Hosted format https://<project-ref>.supabase.co/auth/v1/callback is Supabase convention; the doc text did not print it, confirm on the Dashboard.
- Default scopes: docs ".../auth/userinfo.email (added by default)", ".../auth/userinfo.profile (added by default)", "openid (add manually)" in the Google consent screen config. Code (provider/google.go) requests "email", "profile".
- Second redirect URI on same client: yes. Google (https://developers.google.com/identity/protocols/oauth2/web-server): "The value must exactly match one of the authorized redirect URIs for the OAuth 2.0 client". Adding Gmail restricted scopes triggers verification; Supabase doc: "If you add more scopes, especially those on the sensitive or restricted list your application might be subject to verification".

## 9. session_id
- https://supabase.com/docs/guides/auth/sessions : "Every access token contains a `session_id` claim, a UUID, uniquely identifying the session of the user."
- Google sign-in makes a normal Supabase session, so same claim: inferred from "every access token"; not separately tested.
- Built-in single-session setting: "You can also enforce only one active session per user per device or browser." Needs Pro plan or higher (same page). A custom rule on session_id is not plan-gated.
