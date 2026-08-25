# Weekday fleet briefing

- **Name:** Weekday fleet briefing
- **Slug:** `weekday-fleet-briefing`
- **Schedule:** Every weekday at 9:00 in the user's local time
- **Intent:** Recap the fleet without inventing status

## Prompt

Every weekday at 9:00 in the user's local time, gather status from
specialist Grok Bots and from `{github_repo}` / `{slack_channel}` if
those plugins are connected.

Post in this conversation:

1. Yesterday completed
2. Still open
3. Blocked on the user
4. Suggested next dispatch

Do not ping specialists for work they already closed. If a source is
unavailable, say so — do not invent status. Never send mail or Slack on
the user's behalf.
