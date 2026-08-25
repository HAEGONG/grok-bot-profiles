# Connectors

Starter does not require any connector. The Bot should work from chat,
web search, and its cloud computer.

Add plugins later only when a task actually needs them:

| Need | Plugin | Marketplace id |
| --- | --- | --- |
| Email | Gmail | `gmail` |
| Repos / PRs | GitHub | `github` |
| Chat | Slack | `slack` |
| Notes | Notion | `notion-workspace` |
| Files | Google Drive | `google-drive` |
| Schedule | Google Calendar | `google-calendar` |

Install from Grok Bot **Settings → Plugins** (or `/add-plugin <id>` in
Cursor). Authorize in the browser. Never put secrets in this repo or in
chat.
