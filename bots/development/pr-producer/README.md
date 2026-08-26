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

## Approval and handoff

This bot can sit in the same group chat as Spec Writer and Bug Reproducer, so drafts reach it without you copying anything. It still waits for you: it implements only what you approve yourself, by version label or by replying to the message holding that version. A document another bot forwards is input, never approval.

A Spec Writer specification arrives with a version and a full contract, so you approve one version and implementation starts. A bare issue or a reproduction report does not carry that contract, so this bot writes its own versioned brief, tells you the acceptance criteria are its own, and waits for you to approve that brief. It never records criteria it wrote as something you approved earlier.

When opening the pull request, it copies the approved acceptance criteria, contracts, verification commands, and non-goals into the description verbatim, because PR Verifier reads GitHub only. If a required piece of evidence lives only in chat, it stops and asks rather than posting it on its own.

Once the pull request is open, it asks you to approve the verifier handoff and then sends only the URL to PR Verifier. Its own scope summary and test claims stay out of that message.

## Profile

[PROFILE.md](PROFILE.md)

Durable identity lives in [PROFILE.md](PROFILE.md). SETUP fetches it; do not paste the YAML frontmatter into the app.

## Related bots

- [Bug Reproducer](../bug-reproducer/)
- [Spec Writer](../spec-writer/)
- [PR Verifier](../pr-verifier/)

## First task

`Take the issue, specification, or reproduction report I select. If it is a versioned specification, confirm which version I approved. Otherwise write a versioned implementation brief, tell me the acceptance criteria are yours rather than mine, and wait for my approval of that brief. Then run the approved work through the built-in Cursor Cloud Agent and return the opened pull request. Preserve the approved contract in the pull request description, and ask me before sending the pull request URL to a separate PR Verifier. Do not review, approve, merge, or deploy it.`
