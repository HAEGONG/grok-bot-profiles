# Bug Reproducer

Turn a vague bug report into evidence an implementation agent can act on, without letting investigation silently become implementation.

Category: development

## The setup prompt

Create a new Grok Bot and paste this URL as the first message:

https://raw.githubusercontent.com/HAEGONG/grok-bot-profiles/main/bots/development/bug-reproducer/SETUP.md

The bot fetches [PROFILE.md](PROFILE.md) and sets Name, Title, and Description. Do not paste the profile by hand.

## Connect first

`GitHub`

Open **Settings → Plugins** and add it.

GitHub provides issue and source evidence through its API; this bot must not clone the repository. Product reproduction happens in the browser on the Bot's computer, never through a cloud coding agent. For a non-public surface, use an authorized browser session that you control; never paste credentials into the bot. If the surface or required logs are unavailable, the bot returns `BLOCKED` without guessing.

## Handing work to another bot

This bot returns its report in the conversation it was addressed in, including a shared production group chat. Leaving the report there needs no approval, but asking another bot to act on it does, even when the message names no bot in a group where participating bots may pick it up on their own. After you approve the content, the destination, and the next action being requested, it may hand the report to a PR Producer bot, or back to a Spec Writer bot when your handover says which specification or notice the report should update. If the report carries `None given`, name that target yourself. A handover is never approval to implement.

A label by itself never starts work. This bot begins only when you ask it directly, or when an explicit handover names it and asks for reproduction, so a Spec Writer notice sitting in the group does not wake it. Every report opens with the `Reproduction label` it was given, such as `repro-2-v1`, or `None given` when you asked directly. The same label travels from the notice through the approved handover to the report, so Spec Writer can match it to the right draft when several reproduction needs are open at once.

Reproduction reports usually rest on screenshots, and a bot-to-group handoff message carries text only. So a screenshot-dependent report goes through a direct bot-to-bot message. Keep in mind that PR Verifier judges GitHub-observable evidence only, so any screenshot that a verdict depends on has to be attached to the GitHub issue or pull request before verification.

## Profile

[PROFILE.md](PROFILE.md)

Durable identity lives in [PROFILE.md](PROFILE.md). SETUP fetches it; do not paste the YAML frontmatter into the app.

## Related bots

- [Spec Writer](../spec-writer/)
- [PR Producer](../pr-producer/)
- [PR Verifier](../pr-verifier/)

## First task

`Ask me for the target repository and issue URL or number. If I provide only a repository, list its open issues labeled bug, sort them by explicit repository priority labels when present, and ask me to choose; never infer priority. Then attempt to reproduce the selected issue and leave the report in this chat without changing code or proposing a fix.`
