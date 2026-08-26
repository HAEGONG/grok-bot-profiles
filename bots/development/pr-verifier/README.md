# PR Verifier

Put an independent evidence gate between agent-written code and the human merge decision.

Category: development

Create this as a separate Grok Bot. Never reuse the PR Producer Bot or its conversation for verification, and keep this bot out of the group chat where Spec Writer, Bug Reproducer, and PR Producer work.

## The setup prompt

Create a new Grok Bot and paste this URL as the first message:

https://raw.githubusercontent.com/HAEGONG/grok-bot-profiles/main/bots/development/pr-verifier/SETUP.md

The bot fetches [PROFILE.md](PROFILE.md) and sets Name, Title, and Description. Do not paste the profile by hand.

## Connect first

`GitHub`

Open **Settings → Plugins** and add it.

Use GitHub's API to inspect the pull request, source and test files, check results, and CI evidence. This bot must not clone the repository, run tests locally, or invoke a cloud coding agent. It leaves its verdict in the current chat only.

## Why it stays in its own conversation

Independence here is about evidence, not access. Bots share one computer, browser session, and file system per account, so separating bots is not a security boundary. What separation does protect is the basis for the verdict: in a shared group chat, the producer's intent, discarded options, and self-assessment become part of what this bot reads.

So this bot takes a pull request URL in its own conversation and judges GitHub-observable evidence only. A direct handover is fine when its entire content is the URL, which keeps that conversation independent. If a producer's summary or attachment rides along, it returns `HOLD` and asks for a clean URL-only handover in a fresh conversation. If you ask it to verify inside a production group chat, it returns `HOLD` and asks you to bring the URL to its own conversation instead. Evidence that exists only in chat also returns `HOLD`, with the missing artifact named, so PR Producer attaches it to GitHub first.

## Profile

[PROFILE.md](PROFILE.md)

Durable identity lives in [PROFILE.md](PROFILE.md). SETUP fetches it; do not paste the YAML frontmatter into the app.

## Related bots

- [Bug Reproducer](../bug-reproducer/)
- [Spec Writer](../spec-writer/)
- [PR Producer](../pr-producer/)

## First task

`Review the pull request URL I provide as an independent gate, in this conversation only. Evaluate tests, contracts, and regressions only, then return PASS, BLOCK, or HOLD with evidence. Do not change code or merge it.`
