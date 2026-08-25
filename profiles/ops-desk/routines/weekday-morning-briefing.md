# Weekday morning briefing

- **Name:** Weekday morning briefing
- **Slug:** `weekday-morning-briefing`
- **Schedule:** Every weekday at 8:30 in the user's local time
- **Intent:** Start-of-day brief; never send

## Prompt

Every weekday at 8:30 in the user's local time, run an ops brief. Read
Google Calendar for the day. If Gmail or Slack `{slack_channel}` is
connected, note only items that change the day (time-sensitive, needs
a decision). Post in this conversation. No-data: say which source
failed. Do not send, decline, or buy.
