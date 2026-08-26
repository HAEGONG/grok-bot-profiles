# Grok Bot Profiles

[English](README.md) | [한국어](README.ko.md)

> One outcome. One approval boundary. One bot.

Ready-to-use profiles for Grok Bots. Each profile gives a bot one focused job, a concrete deliverable, and an explicit point where its authority ends.

General-purpose agents blur responsibility. This collection keeps specification, investigation, implementation, and verification separate so a bot never approves its own work.

## Quick start

Grok Bot does not import local files. To install a profile:

1. Create a new Grok Bot.
2. Copy the profile's **Setup prompt** URL from the table below.
3. Paste the URL as the bot's first message.
4. Connect GitHub when the bot asks for it.
5. Send the **First task** from the profile's README.

`SETUP.md` fetches the profile and configures the bot's Name, Title, and Description. Do not paste `PROFILE.md` into Description by hand.

| Profile | Use it when you need to | Setup prompt |
| --- | --- | --- |
| [Spec Writer](bots/development/spec-writer/) | Turn a selected idea, request, or unclear issue into an implementation-ready specification | [Copy raw URL](https://raw.githubusercontent.com/HAEGONG/grok-bot-profiles/main/bots/development/spec-writer/SETUP.md) |
| [Bug Reproducer](bots/development/bug-reproducer/) | Turn a selected bug report into a reproducibility verdict and evidence report | [Copy raw URL](https://raw.githubusercontent.com/HAEGONG/grok-bot-profiles/main/bots/development/bug-reproducer/SETUP.md) |
| [PR Producer](bots/development/pr-producer/) | Turn approved work into a focused branch and reviewable pull request | [Copy raw URL](https://raw.githubusercontent.com/HAEGONG/grok-bot-profiles/main/bots/development/pr-producer/SETUP.md) |
| [PR Verifier](bots/development/pr-verifier/) | Independently evaluate a pull request and return `PASS`, `BLOCK`, or `HOLD` | [Copy raw URL](https://raw.githubusercontent.com/HAEGONG/grok-bot-profiles/main/bots/development/pr-verifier/SETUP.md) |

### Create your own bot

Want a profile for a different job? See [CREATE_YOUR_OWN_BOT.md](CREATE_YOUR_OWN_BOT.md) for the profile template, AI-assisted creation prompt, and review checklist.

New to Grok Bots? See the official [Get started](https://docs.x.ai/grok-bot/get-started) and [Create and manage Bots](https://docs.x.ai/grok-bot/bots) guides.

## Development workflow

Use each role as a separate Grok Bot:

```text
Feature request → Spec Writer → Human spec approval ─┐
Bug report → Bug Reproducer → Evidence report ───────┤
                                                     ↓
                                              PR Producer
                                                     ↓
                                               PR Verifier
                                                     ↓
                                          Human merge decision
```

| Bot | Must stop before |
| --- | --- |
| Spec Writer | Approving the specification or implementing it |
| Bug Reproducer | Editing code or invoking a coding agent |
| PR Producer | Reviewing, approving, or merging the pull request |
| PR Verifier | Implementing fixes or merging the pull request |

The PR Producer and PR Verifier must never be the same bot or share the same conversation. Their separation is the approval boundary, not an implementation detail.

## How profiles work

Every bot directory contains three files:

| File | Purpose |
| --- | --- |
| `PROFILE.md` | Durable identity, job, output contract, working rules, and approval boundary |
| `SETUP.md` | One-time setup message and task-specific operating checklist |
| `README.md` | Installation instructions, required integrations, related bots, and first task |

The YAML frontmatter in `PROFILE.md` maps to the Grok Bot interface:

| App field | Profile source |
| --- | --- |
| Name | `name` |
| Title | `title` |
| Description | Markdown body below the frontmatter |
| Plugins | `integrations` |
| Avatar | Configure directly in the app |

## Design principles

- **Split by outcome, not stack.** Frontend and backend work can belong to one bot when they serve the same user outcome.
- **Separate production from verification.** A bot must not review or approve work it produced.
- **Keep Description durable.** Put permanent role rules in `PROFILE.md`; put setup and task-specific instructions elsewhere.
- **Make failure explicit.** Use named outcomes such as `BLOCKED` or `HOLD` instead of guessing or silently expanding authority.
- **Require observable evidence.** Never invent logs, test results, check status, URLs, or repository state.
- **Stop at the boundary.** Opening, approving, merging, and deploying a pull request are different permissions.

Create a separate bot when the outcome, information sources, tools, schedule, or approval boundary changes.

## Repository layout

```text
bots/
  development/
    bug-reproducer/
    pr-producer/
    pr-verifier/
    spec-writer/
templates/
  bot/
```

## Contributing

Pull requests for new profiles and improvements to existing ones are welcome. Profiles should be immediately useful, narrow enough to trust, and explicit about authority.

If these profiles save you a setup cycle, star the repository and share the workflow that worked for you.

## License

Except where otherwise noted, this repository is licensed under the [Creative Commons Attribution 4.0 International License](LICENSE). When sharing or adapting this work, credit HAEGONG, link to this repository and the license, and indicate whether you made changes.
