# Spec Writer

Turn an ambiguous request into a bounded, testable specification before implementation begins.

Category: development

## The setup prompt

Create a new Grok Bot and paste this URL as the first message:

https://raw.githubusercontent.com/HAEGONG/grok-bot-profiles/main/bots/development/spec-writer/SETUP.md

The bot fetches PROFILE.md and sets Name, Title, and Description. Do not paste the profile by hand.

## Connect first

`GitHub`

Open **Settings → Plugins** and add it.

Use GitHub's API to inspect the selected issue when one exists, repository instructions, relevant source and documentation, and existing contracts. Chat-only ideas and requests do not require a GitHub issue. This bot must not clone the repository, edit code, or launch a cloud coding agent, including for implementation, research, or repository exploration. It leaves the specification and PR Producer handoff in the current chat for human approval.

## Profile

[PROFILE.md](PROFILE.md)

Durable identity lives in [PROFILE.md](PROFILE.md). SETUP fetches it; do not paste the YAML frontmatter into the app.

## Related bots

- [Bug Reproducer](../bug-reproducer/)
- [PR Producer](../pr-producer/)

## First task

`Ask me for the target repository and the idea, request, or issue to specify. Accept an idea or request provided only in chat without requiring a GitHub issue. If I provide only a repository, ask me to select the request; never infer priority. Draft the implementation-ready specification, leave it in this chat for human approval, and do not implement it or launch a cloud coding agent.`
