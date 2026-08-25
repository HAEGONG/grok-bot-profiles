# PR Producer

Convert approved engineering work into a focused branch and pull request through Cursor Cloud Agents, then stop before review or merge.

Category: development

## The setup prompt

Copy [SETUP.md](SETUP.md) and paste it as the first message to a new Grok Bot.

## Connect first

`Cursor, GitHub`

Open **Settings → Plugins** and add each one.

## Profile

[PROFILE.md](PROFILE.md)

Paste the PROFILE.md **body** (from `# PR Producer` onward) into **Bot actions → Edit Profile → Description**. Set **Name** and **Title** from the frontmatter. Do not paste the YAML frontmatter into the app.

## Related bots

- [Bug Reproducer](../bug-reproducer/)
- [PR Verifier](../pr-verifier/)

## First task

`Take the approved issue or reproduction report I provide, prepare a bounded implementation brief, run it through Cursor Cloud Agents, and return the opened pull request. Do not review, approve, merge, or deploy it.`
