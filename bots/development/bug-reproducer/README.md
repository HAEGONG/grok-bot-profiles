# Bug Reproducer

Turn a vague bug report into evidence an implementation agent can act on, without letting investigation silently become implementation.

Category: development

## The setup prompt

Create a new Grok Bot and paste this URL as the first message:

https://raw.githubusercontent.com/HAEGONG/grok-bot-profiles/main/bots/development/bug-reproducer/SETUP.md

The bot fetches [PROFILE.md](PROFILE.md) and sets Name, Title, and Description. Do not paste the profile by hand.

## Connect first

`GitHub`

Open **Settings → Plugins** and add it.

GitHub provides issue and source evidence through its API; this bot must not clone the repository. Product reproduction happens in the browser on the Bot's computer, never through a cloud coding agent. For a non-public surface, use an authorized browser session that you control; never paste credentials into the bot. If the surface or required logs are unavailable, the bot returns `BLOCKED` without guessing.

## Profile

[PROFILE.md](PROFILE.md)

Durable identity lives in [PROFILE.md](PROFILE.md). SETUP fetches it; do not paste the YAML frontmatter into the app.

## Related bots

- [PR Producer](../pr-producer/)
- [PR Verifier](../pr-verifier/)

## First task

`Ask me for the target repository and issue URL or number. If I provide only a repository, list its open issues labeled bug, sort them by explicit repository priority labels when present, and ask me to choose; never infer priority. Then attempt to reproduce the selected issue and leave the report in this chat without changing code or proposing a fix.`
