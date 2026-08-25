# PR Producer

Convert approved engineering work into a focused branch and pull request through the built-in Cursor Cloud Agent, then stop before review or merge.

Category: development

## The setup prompt

Create a new Grok Bot and paste this URL as the first message:

https://raw.githubusercontent.com/HAEGONG/grok-bot-profiles/main/bots/development/pr-producer/SETUP.md

The bot fetches [PROFILE.md](PROFILE.md) and sets Name, Title, and Description. Do not paste the profile by hand.

## Connect first

`GitHub`

Open **Settings → Plugins** and add it. Cursor Cloud Agent is built into Grok and does not require a plugin.

## Profile

[PROFILE.md](PROFILE.md)

Durable identity lives in [PROFILE.md](PROFILE.md). SETUP fetches it; do not paste the YAML frontmatter into the app.

## Related bots

- [Bug Reproducer](../bug-reproducer/)
- [PR Verifier](../pr-verifier/)

## First task

`Take the approved issue or reproduction report I provide, prepare a bounded implementation brief, run it through the built-in Cursor Cloud Agent, and return the opened pull request. Do not review, approve, merge, or deploy it.`
