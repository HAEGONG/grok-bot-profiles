# PR Producer

Convert approved engineering work into a focused branch and pull request through the built-in Cursor Cloud Agent, then stop before review or merge.

Category: development

## The setup prompt

Copy [SETUP.md](SETUP.md) and paste it as the first message to a new Grok Bot.

## Connect first

`GitHub`

Open **Settings → Plugins** and add it. Cursor Cloud Agent is built into Grok and does not require a plugin.

## Profile

[PROFILE.md](PROFILE.md)

Paste the PROFILE.md **body** (from `# PR Producer` onward) into **Bot actions → Edit Profile → Description**. Set **Name** and **Title** from the frontmatter. Do not paste the YAML frontmatter into the app.

## Related bots

- [Bug Reproducer](../bug-reproducer/)
- [PR Verifier](../pr-verifier/)

## First task

`Take the approved issue or reproduction report I provide, prepare a bounded implementation brief, run it through the built-in Cursor Cloud Agent, and return the opened pull request. Do not review, approve, merge, or deploy it.`
