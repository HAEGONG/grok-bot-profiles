# Connectors

| Plugin | Marketplace id | Why |
| --- | --- | --- |
| GitHub | `github` | PRs, issues, Actions, review |

Optional:

| Plugin | Marketplace id | Why |
| --- | --- | --- |
| Linear | `linear` | Ticket is the spec |
| Slack | `slack` | Only if review requests arrive in `{slack_channel}` |

Authorize in **Settings → Plugins**. Use `{github_repo}` in routines
until the user fills it in. Never store tokens here.
