# Port notes: cold-cli (Go) and trickle (TS)

Read 2026-11-03, read-only, via raw.githubusercontent.com at pinned SHAs. Nothing cloned, built or run, so every "bug" below is **static reading, not verified by execution**. Line refs are `file:line` at the SHA.

| Repo | License | SHA read |
|---|---|---|
| andersmyrmel/cold-cli | MIT | `1dabc627c2b9971d50f4c835d439a2e837d068cc` |
| suneet07/trickle | MIT | `f04207d63522864cdc7802324d676bf2e71859ff` |

---
## 1. cold-cli

### 1.1 Tick engine (`internal/tick.go`)
Cron every 10 min (ARCHITECTURE.md:141). `Tick()` order, tick.go:47-403:
1. `completeFinishedCampaignsAt` (60). 2. Reply+unsub poll per provider (91-112). 3. Bounce poll (115-132). 4. `SetLastPollAt(now)` (148). 5. `preloadDailyCounts` (157). 6. `RebalancePendingSchedules` (173). 7. `loadDueSends` = `status='pending' AND send_at<=now AND campaign.status='active' ORDER BY send_at` (572-596). 8. Send loop (197-393).
- Per-send loop: `refreshPendingSend` re-reads row (198, 626-660) -> daily-limit check `dailyCounts[acct] >= DailyLimit` (219) -> `isInSendWindow` (230, 709-760) -> render -> external `checkBeforeSend` fail-closed (494, pre_send_check.go:27) -> provider send, 30s timeout (gws.go:95) -> mark sent (331) -> insert `events` row (338) -> backfill step-1 thread/message id onto later steps (370-379) -> rebalance account (381) -> in-memory count++ (385) -> `sleep 90+rand.Intn(51)` s (390).
- Defaults: min/max gap 90/140 s (config.go:27-28); account daily_limit 50 (main.go:2843).
- Lock: `AcquireTickLock` at main.go:1834-1844 (skipped for `--dry-run`). SQLite: `flock(LOCK_EX|LOCK_NB)` store.go:236. Postgres: `pg_try_advisory_lock(0x636f6c645f746963)` store.go:21,256. Second tick prints "tick already running", exit 0.

### 1.2 send_at pre-compute and jitter (`internal/scheduler.go`)
- `ComputeSchedule` 131-216. Account = `AccountIDs[leadIdx % n]` (169, round-robin, sticky per lead). Variant = `leadIdx % (1+len(variants))` (176-179).
- Step 1: `gap = Min + rand.Intn(Max-Min)` drawn **once per lead**; `sendAt = start + leadIdx*gap` seconds; then `clampToWindow` (185-199). So offset is `leadIdx x one random gap`, not a cumulative sum of random gaps.
- Step N: `nextScheduledTime(prev, delayDays)` = `clampToWindow(prev + delayDays days)` (194, 786-788).
- `clampToWindow` 763-784: before window -> window start; at/after end -> next day start; skip non-send days.
- `RebalancePendingSchedules` 265-418 (deterministic, no new randomness): per account, merge all campaigns' pending rows in time order (sort 367-386); `earliest = max(candidate.at, lastAssigned + max(MinGap, lastMinGap))` (390-399); `allocateDailyLimitedSendAt` pushes to next sendable day while `usage[UTCdate] >= limit` (701-708). Usage = `COUNT` of `events type IN ('sent','manual_reply')` grouped by **UTC date** (547-578, 741-743).
- Net effect: real jitter comes only from the tick's 90-140 s sleep (tick.go:390). Rebalanced rows sit at exactly `MinGap` spacing, front-loaded from window open.
- In-flight leads re-anchor follow-ups from actual `sent_at` (ARCHITECTURE.md:262). Step-1 rows stranded >30 days past anchor are pulled back (scheduler.go:668-676).

### 1.3 Double-send avoidance
There is **no claim/lease state and no DB uniqueness on sends**. Protection is layered:
1. One global tick lock (above).
2. State machine `pending -> sent|failed|skipped|cancelled`; loop re-reads each row and skips if not `pending` or campaign not `active` (tick.go:198-208, 626-660). Reply/bounce/unsub flip pending rows to `skipped` (reply.go:304, 439).
3. Pre-send external contact check (tick.go:494).
4. DDL `scheduled_sends` (db.go:89-103) has **no UNIQUE(campaign_id, lead_id, step_number)**. Only UNIQUE keys in the schema: accounts.email, campaigns.name, leads.email, `manual_reply_attempts.idempotency_key` (db.go:21,44,70,149; that table is the only true idempotency key, for manual replies).
5. Leads are deduped globally by `leads.email UNIQUE`; CSV re-import updates fields instead of ignoring.

### 1.4 Reply matching (`internal/reply.go`)
- Gmail query: `to:<acct> -from:<acct> after:<unix>` (105), not limited to INBOX. IMAP: `ListMessages(account, since, false)` (121).
- Cursor per account+provider `reply_poll_at:<provider>:<id>` (35-41), advanced only on success (138-145), rewound by `replyPollOverlap = 2h` (130,156). Dedup by `events.message_id IN reply|unsubscribe|bounce|auto_reply` (176-182).
- Strategy 1: `In-Reply-To` -> `events.message_id` where type `sent|manual_reply` (188-202). Strategy 2 fallback: `thread_id` equality (206-221).
- IDs: gws stores RFC `Message-ID` fetched via `GetMessage` after send, falls back to the Gmail API id (tick.go:511-521). IMAP: `normalizeMessageID` keeps `<...>` (imap.go:793-805); thread id = first `<id>` in `References`, else `In-Reply-To` (imap.go:691-694, 807-824). SMTP step-1 thread id = its own Message-ID (smtp.go:84-88).
- Classification order, first wins: **bounce > auto-reply > unsubscribe > reply** (reply.go:377-389). Unmatched inbound mail is ignored (223-225).
- Reply effects: `campaign_leads.status='replied'`, pending sends `skipped` (297-308); `stop_on_domain_reply` pauses same-domain leads (310-339).
- Unsubscribe phrases (12), run on quote-stripped body (reply.go:67-80, reply_body.go:16-40): unsubscribe, stop emailing, stop sending, remove me, opt out, opt-out, take me off, don't contact, do not contact, don't email, do not email, stop contacting. Effect: `BlacklistLead` globally (reply.go:263-271).

### 1.5 Bounce detection strategies
**Is-a-bounce** (`isBounceMessage` reply.go:579-621), any of:
1. `X-Failed-Recipients` header non-empty (580).
2. DSN MIME: `message/delivery-status`, or `multipart/report; report-type=delivery-status`, or any part with that MIME (683-697).
3. From contains `mailer-daemon` or `postmaster` (588-591).
4. 19 phrases in subject/snippet/text/html (594-614): delivery status notification, delivery failed/failure, delivery has failed, undelivered mail (+returned to sender), undeliverable, address not found, mail delivery failed, message not delivered, message wasn't delivered, message could not be delivered, returned mail, `550 5.1.1`, nosuchuser, no such user, user unknown, recipient address rejected, mailbox unavailable.

**Which lead** (`resolveBounceToLead` 763-797): (1) `thread_id` of a sent event; (2) `X-Failed-Recipients` == lead email; (3) first email-looking token in snippet+body+subject, excluding `mailer-daemon`/`postmaster` locals (800-830), must exist in `leads`.

**Two redundant paths**: reply-poll path (only if In-Reply-To/thread matched; 235-240) and a dedicated bounce poll: Gmail `(from:mailer-daemon OR from:postmaster) after:<last_poll>` with `includeSpamTrash=true` (534-542); IMAP bounce poll also includes spam/trash (545-551).
**Effects** (`recordBounceForLead` 416-463): idempotent (skip if `leads.global_status=='bounced'`, 421-425); lead globally bounced, all its pending sends `skipped` across campaigns (429-442); event deduped by message id (444).
**Prevention**: pre-import SMTP RCPT probe + MX + catch-all probe with random mailbox (email_validation.go:232-291, catch-all 263-265).

### 1.6 Auto-reply detection (`isAutoReplyMessage` reply.go:623-681)
- `message/disposition-notification` / report-type (699-713).
- `Auto-Submitted` first token non-empty and != `no` (629-632); exception only for Zendesk newest-comment.
- Any non-empty `X-Autoreply`, `X-Autorespond`, `X-Auto-Reply`, `X-Auto-Response` (634-644).
- `Precedence` == `bulk|auto_reply|auto-reply` (646-649).
- 20 phrases on subject+quote-stripped body (652-673): auto reply, auto-reply, automatic reply, automated reply, automatic response, out of office, out of the office, away from the office, ticket submitted, ticket has been submitted, your ticket has been submitted, we'll/we will pick up your ticket, we have/we've/we received your request, your request has been received, read receipt, return receipt, disposition notification.
- Recorded as `auto_reply` event, does **not** stop the sequence (391-414).

### 1.7 Follow-up threading
- Headers (send.go:66-73): `In-Reply-To: <step-1 Message-ID>`, `References:` = same single id (not a growing chain). PrepareFollowUp send.go:247-269; wired tick.go:280-283.
- Subject: step's own rendered subject, prefixed `Re: ` unless already `re:`; if empty, `Re: <step-1 subject>` (send.go:252-268).
- gws: also passes Gmail `threadId` (gws.go:127-135). SMTP: sends Date + generated `<unixnano.hex@senderdomain>` Message-ID (send.go:272-286; smtp.go:61-69).
- Body is always `text/html` wrapped in `<div>`, `<br>` for newlines, no text/plain part (send.go:83-85, 220-234). List-Unsubscribe is opt-in (send.go:76-80; ARCH decision 22).

---
## 2. trickle

### 2.1 Ramp and daily cap (`packages/core/src/cap.ts`)
```
headroom   = max(0, totalCap - warmupVolumeManual)            // cap.ts:59   (40, 15 -> 25)
capCold    = min(capColdBase, headroom) * healthMult * ramp   // cap.ts:60-62 (base 25)
cap        = floor(capCold)                                   // cap.ts:63
remaining  = max(0, cap - floor(sentToday + queuedToday))     // cap.ts:48-55
dailyBudget= min(globalCeiling=100, sum(computeCap(a)))       // cap.ts:105-112
```
- `ramp(ageDays)`: <=7 -> 0.3; <=14 -> 0.5; <=21 -> 0.75; else 1.0 (cap.ts:31-36). `ageDays = floor((now-createdAt)/86400000)`; `warmedUp` -> 999 (lib.ts:10-14).
- `healthMult(h)`: >=90 -> 1.0; >=70 -> 0.6; >=50 -> 0.3; else 0 (cap.ts:23-28).
- Defaults: base 25, warmupVolumeManual 15, warmupTarget 200 (schema.prisma:70,73,79); totalCap 40, global 100 (env.ts:81-82; cap.ts:10-13).
- Example: new inbox, health 100 -> floor(25*1*0.3) = 7; health 75 -> floor(25*0.6*0.3) = 4.
- Planner runs 00:05 UTC and on campaign start; health 00:20 UTC (index.ts:179,191), so the planner uses **yesterday's** score.
- Built-in warm-up (`apps/worker/src/jobs/warmup.ts`): cron `0 9,13,17 * * *` UTC (index.ts:204). Per run `perRun = max(1, min(warmupVolumeManual, peers, remaining, 5))` (52) -> <=15/day/inbox; random peer among your own warm-up inboxes; 5 subjects + 4 bodies + `[wu]` subject tag (15-28); receiver rescue = `messages.modify` add IMPORTANT, remove SPAM/UNREAD (82-89). At `warmupSentTotal >= warmupTarget` sets `warmedUp=true` (110), which skips the ramp. Flat, not progressive.

### 2.2 Health score 0-100 (`cap.ts:114-135`, inputs `health-check.ts:14-44`)
```
health = 100
       - 30 * clamp(bounceRate7d  / 0.05)
       - 25 * clamp(gmailErrRate7d / 0.10)
       - 15 * (dnsblListed ? 1 : 0)
       - 10 * (spfDkimDmarcFail ? 1 : 0)
       + 10 * clamp(replyRate7d   / 0.05)
health = round(clamp(health, 0, 100))      // clamp(x,0,1) default, util.ts:1-3
```
- Rates = sums over `SendLog` rows with `date >= startOfDay(utcNow-7d)` divided by `max(1, sum(coldSent))` (health-check.ts:14-25, 38-44). Warm-up sends are not in the denominator.
- Max penalty 80, so floor is 20; reply bonus up to +10. Bounce alone can never quarantine (min 70); quarantine needs e.g. bounce>=5% + gmailErr>=10%, or bounce>=5% + DNSBL + SPF/DMARC.
- `spfDkimDmarcFail = !(spf && dmarc)` only; DKIM is **not** checked (dns-checks.ts:24-26). DNSBL = A record of `mail.<domain>` queried on zen.spamhaus.org and dnsbl.sorbs.net, any A answer = listed (dns-checks.ts:38-49; health-check.ts:32-33).

### 2.3 Circuit breakers
| Trip | Action | Cooldown / reset | Ref |
|---|---|---|---|
| health < 50 | `status='quarantined'`, alert once on crossing | back to `active` when daily check sees health >= 70; no timer | health-check.ts:50-53, 60-63 |
| 50 <= health < 70 | alert only when previous >= 70; cap x0.3 via multiplier | a quarantined inbox stays quarantined in this band | health-check.ts:54-59 |
| >=2 bounces today (UTC `SendLog.bounces`) | `pausedUntil = now+48h` (re-set on every further bounce) | time-based expiry, no manual reset path | poll-replies.ts:152-168 |
| Gmail 429/403 on send | throw -> BullMQ 5 attempts, exponential from 60 s | after 5, job fails; hourly reconcile resets `queued` rows to `planned` | send-email.ts:203-205; queue.ts:26-31; reconcile.ts:13-34 |
| Other Gmail error | message `failed`, alert, `gmailErr++` | none | send-email.ts:195-207 |
| Campaign reply rate < 1% (sent >= 400) | informational alert only, max 1/week/campaign | n/a | index.ts:127-129,137 |
- Enforcement points: planner skips non-active or paused inboxes (daily-planner.ts:46-52); sender re-checks status, `pausedUntil`, campaign state, suppression, lead status before every send and re-plans the message instead of sending (send-email.ts:47-83).
- Daily worker cadence: poll-replies every 10 min (index.ts:185); `concurrency: 3` on sends (index.ts:34).
- Reply/auto-reply logic is thread-id based only, Gmail headers `Auto-Submitted`, `Precedence` + subject regex (poll-replies.ts:45-51, 54-59). Bounce = From regex `mailer-daemon|postmaster` or subject regex (38-40).

---
## 3. Bugs / weak points I noticed (static reading, unexecuted)

### cold-cli
1. **At-least-once sends.** Provider send (tick.go:309) happens before the `UPDATE ... 'sent'` (331); a failed update is only logged (333-335), row stays `pending`, next tick resends. No `sending` claim state, no unique key.
2. **Ambiguous failure -> duplicate on retry.** 30 s gws timeout (gws.go:95) after Gmail accepted marks the row `failed` (tick.go:325); `campaign retry` blindly resets all `failed` to `pending` (campaign.go:1813-1845).
3. **Stale `now`.** `now` is fixed at tick start (tick.go:50-53) but each send sleeps 90-140 s; window and due checks (205, 230) and stored `sent_at` (331) use that old time. A long backlog can send after the window closes.
4. **Probable SQLite daily-count miss.** `preloadDailyCounts` compares `timestamp >= '2026-..T..Z'` (tick.go:544) against default `CURRENT_TIMESTAMP` text `'YYYY-MM-DD HH:MM:SS'` (db.go:114; insert at tick.go:338 sets no timestamp). Byte 0x20 < 'T', so same-day rows compare lower and are not counted. The test uses RFC3339 timestamps (tick_test.go:1198-1202), so it would not catch it. Rebalance parses both formats (scheduler.go:566, campaign.go:1573) and mitigates. Day boundary also differs: tick uses the configured tz (tick.go:537), rebalance uses UTC date (scheduler.go:741-743).
5. **No hard/soft distinction, no account breaker.** A "Delivery Status Notification (Delay)" or any 4.x.x temp failure permanently bounces the lead globally (reply.go:429-442). No bounce-rate auto-pause exists (grep of internal/ found only manual `account pause`).
6. **Bounce parsing gaps.** `extractBouncedEmail` returns only the first email-like token (reply.go:804-808); if that is the sender account, the bounce is missed. From containing `postmaster` classifies a human mail as a bounce (589). `SetLastPollAt` runs even when the bounce poll errored (tick.go:118-120,148); the reply path's 2 h overlap partially covers it.
7. **Header-name case.** gws parsing switches on exact `"In-Reply-To"` (gws.go:281) and `extractRFCMessageID` reads `Headers["Message-ID"]` (tick.go:267); a `Message-Id` variant silently falls back to the Gmail api id and breaks In-Reply-To matching (thread fallback still works).
8. **Threading caveat.** Follow-up subject = `Re: <that step's own subject>` (send.go:263-268). If a sequence gives step 2 a different subject, Gmail will not thread even with `threadId` (Gmail requires matching Subject; per Gmail docs, not run). `References` is a single id, not a chain.
9. **HTML-only mail**, no text/plain alternative (send.go:83-85).
10. **Linux/macOS only lock**: `syscall.Flock` unconditional in store.go:236, no build tag in the file header; likely does not compile on Windows. Relevant for a Windows host.
11. Step-1 offset `leadIdx*gap` is non-monotonic (lead 11 at gap 60 beats lead 10 at gap 120) and large lists overflow the first window (scheduler.go:188-192); rebalance flattens it anyway.

### trickle
1. **Bounce counter is not idempotent.** Poll lists `newer_than:1d in:inbox` every 10 min (poll-replies.ts:20-24; index.ts:185) and `handleBounce` has no per-message dedupe, so `bumpSendLog('bounces')` (150) runs every poll while the NDR sits in the inbox. The 2nd poll reaches `bounces>=2` (158) -> 48 h pause, re-extended on each later poll; bounce rate then saturates the -30 penalty. Only applies if the NDR threads with the outbound message (54-59); otherwise bounces are never detected (no X-Failed-Recipients or body-parse fallback).
2. Bounce/auto-reply regexes are broad: `postmaster` in From, no hard/soft split, "Delay" DSNs suppress the lead (poll-replies.ts:38-40, 143-147).
3. `maxResults: 50`, no pagination, `in:inbox` only (20-24): >50 messages in 24 h or archived/spam replies are missed.
4. Opt-out regex includes `stop`, `no longer`, `not interested` (103-106): false suppressions (e.g. "I no longer work there", "stop by").
5. **Send not idempotent**: Gmail send (send-email.ts:180) before DB update (184); a crash or BullMQ stalled-job redelivery resends. Every retried 403 (not only quota) bumps `gmailErr` (197, 203), inflating the error-rate term; 5xx is treated as permanent (206).
6. Health: DNSBL checks `mail.<domain>`, not the real sending IP (Google's), so it is meaningless for Gmail/Workspace; DKIM never checked; Spamhaus returns sentinel `127.255.255.x` answers to public resolvers, and any A answer counts as "listed" (dns-checks.ts:43-45). Spamhaus behaviour and SORBS status are from memory, **not verified**.
7. health-check.ts: alert text says "x0.6" for the <70 band but multiplier there is 0.3 (59); comment promises "3 consecutive good days" (56) but the branch is empty; hysteresis is only `>=70`; an inbox with no sends scores 100 (`denom=max(1,0)`), and a quarantined inbox recovers mainly because bad days age out of the 7-8 day window.
8. Ramp off-by-one: `ageDays <= 7` covers days 0-7 (8 days at 0.3) vs docs "days 1-7" (cap.ts:32; README ramp table).
9. Warm-up: `newTotal = sent + perRun` counts failed sends (warmup.ts:104), so an inbox can be marked `warmedUp` without sending; rescue query lacks `includeSpamTrash` (75-79) and Gmail `messages.list` excludes SPAM by default, so spam rescue likely never finds anything (Gmail API default, not run); closed pool of own inboxes with 5 subjects and a `[wu]` tag is easy to fingerprint; "ramp with progress" comment (50) is not implemented.
10. Reply matching is thread-id only (poll-replies.ts:54-59); no In-Reply-To/References fallback.
