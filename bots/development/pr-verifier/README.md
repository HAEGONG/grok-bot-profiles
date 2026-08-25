# PR Verifier

Put an independent evidence gate between agent-written code and the human merge decision.

Category: development

Create this as a separate Grok Bot. Never reuse the PR Producer Bot or its conversation for verification.

## The setup prompt

Copy [SETUP.md](SETUP.md) and paste it as the first message to a new Grok Bot.

## Connect first

`GitHub`

Open **Settings → Plugins** and add it.

## Profile

[PROFILE.md](PROFILE.md)

Paste the PROFILE.md **body** (from `# PR Verifier` onward) into **Bot actions → Edit Profile → Description**. Set **Name** and **Title** from the frontmatter. Do not paste the YAML frontmatter into the app.

## Related bots

- [Bug Reproducer](../bug-reproducer/)
- [PR Producer](../pr-producer/)

## First task

`Review the pull request I provide as an independent gate. Evaluate tests, contracts, and regressions only, then return PASS, BLOCK, or HOLD with evidence. Do not change code or merge it.`
