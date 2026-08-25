# Connectors

Senna routes; specialists do most connector-heavy work. For status and
dispatch, connect:

| Plugin | Marketplace id | Why |
| --- | --- | --- |
| GitHub | `github` | Open PRs, issues, Actions for the fleet briefing |
| Slack | `slack` | Mentions and channel pulse (`{slack_channel}`) |

Optional if this Bot is also the human’s front door for mail/calendar:

| Plugin | Marketplace id |
| --- | --- |
| Gmail | `gmail` |
| Google Calendar | `google-calendar` |
| Linear | `linear` |

Authorize in **Settings → Plugins**. Never store tokens in the repo.
Use `{github_repo}` and `{slack_channel}` in routines until the user
fills them in.
