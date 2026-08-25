# PR Verifier

Put an independent evidence gate between agent-written code and the human merge decision.

Category: development

Create this as a separate Grok Bot. Never reuse the PR Producer Bot or its conversation for verification.

## The setup prompt

Create a new Grok Bot and paste this URL as the first message:

https://raw.githubusercontent.com/HAEGONG/grok-bot-profiles/main/bots/development/pr-verifier/SETUP.md

The bot fetches [PROFILE.md](PROFILE.md) and sets Name, Title, and Description. Do not paste the profile by hand.

## Connect first

`GitHub`

Open **Settings → Plugins** and add it.

Use GitHub's API to inspect the pull request, source and test files, check results, and CI evidence. This bot must not clone the repository, run tests locally, or invoke a cloud coding agent. It leaves its verdict in the current chat only.

## Profile

[PROFILE.md](PROFILE.md)

Durable identity lives in [PROFILE.md](PROFILE.md). SETUP fetches it; do not paste the YAML frontmatter into the app.

## Related bots

- [Bug Reproducer](../bug-reproducer/)
- [PR Producer](../pr-producer/)

## First task

`Review the pull request I provide as an independent gate. Evaluate tests, contracts, and regressions only, then return PASS, BLOCK, or HOLD with evidence. Do not change code or merge it.`
