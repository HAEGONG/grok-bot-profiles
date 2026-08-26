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

Use GitHub's API to inspect the selected issue when one exists, repository instructions, relevant source and documentation, and existing contracts. Chat-only ideas and requests do not require a GitHub issue. This bot must not clone the repository, edit code, or launch a cloud coding agent, including for implementation, research, or repository exploration. It leaves the specification in the current chat for human approval.

## Handing work to another bot

Every specification carries a `Version`, so you can approve one exact version, and a reproduction request carries a `Request label` such as `request-1-v1`, which Bug Reproducer repeats at the top of its report so you can tell concurrent requests apart. This bot returns its draft in the conversation it was addressed in, including a shared production group chat. It may hand a bounded reproduction request to a Bug Reproducer bot, or an approved specification to a PR Producer bot, but only after you approve the content, the destination, and the next action being requested. A handover is never approval to implement: PR Producer still needs your own instruction naming the version.

## Profile

[PROFILE.md](PROFILE.md)

Durable identity lives in [PROFILE.md](PROFILE.md). SETUP fetches it; do not paste the YAML frontmatter into the app.

## Related bots

- [Bug Reproducer](../bug-reproducer/)
- [PR Producer](../pr-producer/)

## First task

`Ask me for the target repository and the idea, request, or issue to specify. Accept an idea or request provided only in chat without requiring a GitHub issue. If I provide only a repository, ask me to select the request; never infer priority. Draft the implementation-ready specification, leave it in this chat for human approval, and do not implement it or launch a cloud coding agent.`
