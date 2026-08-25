# Bug Reproducer

Turn a vague bug report into evidence an implementation agent can act on, without letting investigation silently become implementation.

Category: development

## The setup prompt

Copy [SETUP.md](SETUP.md) and paste it as the first message to a new Grok Bot.

## Connect first

`GitHub`

Open **Settings → Plugins** and add it.

GitHub provides issue and source evidence through its API; this bot must not clone the repository. Product reproduction happens in the browser on the Bot's computer, never through a cloud coding agent. For a non-public surface, use an authorized browser session that you control; never paste credentials into the bot. If the surface or required logs are unavailable, the bot returns `BLOCKED` without guessing.

## Profile

[PROFILE.md](PROFILE.md)

Paste the PROFILE.md **body** (from `# Bug Reproducer` onward) into **Bot actions → Edit Profile → Description**. Set **Name** and **Title** from the frontmatter. Do not paste the YAML frontmatter into the app.

## Related bots

- [PR Producer](../pr-producer/)
- [PR Verifier](../pr-verifier/)

## First task

`Ask me for the target repository and issue URL or number. If I provide only a repository, list its open issues labeled bug, sort them by explicit repository priority labels when present, and ask me to choose; never infer priority. Then attempt to reproduce the selected issue and leave the report in this chat without changing code or proposing a fix.`
