# Bug Reproducer

Turn a vague bug report into evidence an implementation agent can act on, without letting investigation silently become implementation.

Category: development

## The setup prompt

Copy [SETUP.md](SETUP.md) and paste it as the first message to a new Grok Bot.

## Connect first

`GitHub`

Open **Settings → Plugins** and add it.

GitHub provides issue and repository evidence. Reproduction also requires a target URL that Grok can open. For a non-public surface, use an authorized browser session that you control; never paste credentials into the bot. If the surface or required logs are unavailable, the bot returns `BLOCKED` without guessing.

## Profile

[PROFILE.md](PROFILE.md)

Paste the PROFILE.md **body** (from `# Bug Reproducer` onward) into **Bot actions → Edit Profile → Description**. Set **Name** and **Title** from the frontmatter. Do not paste the YAML frontmatter into the app.

## Related bots

- [PR Producer](../pr-producer/)
- [PR Verifier](../pr-verifier/)

## First task

`Inspect the highest-priority open bug in the connected repository. Attempt to reproduce it and return the reproduction report only. Do not change code or propose a fix.`
