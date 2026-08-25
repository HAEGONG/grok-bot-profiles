# Weekday inbox triage

- **Name:** Weekday inbox triage
- **Slug:** `weekday-inbox-triage`
- **Schedule:** Every weekday at 9:30 in the user's local time
- **Intent:** Digest inbound mail; never send

## Prompt

Every weekday at 9:30 in the user's local time, scan Gmail (and Slack
`{slack_channel}` if connected) for items that need a human. Post a
triage list in this conversation: urgent, actionable, fyi, spam.
Include a DRAFT reply only for urgent and actionable items. Do not
send, archive, or delete. If mail is unavailable, report the failure
instead of using stale lists.
