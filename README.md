# Grok Bot Profiles

> One outcome. One approval boundary. One bot.

A collection of ready-to-use profiles for Grok Bots. Each profile gives a bot a focused job, a concrete deliverable, and an explicit point where its authority ends.

General-purpose agents blur responsibility. These profiles keep research, implementation, and verification separate so a bot never approves its own work.

## Development workflow

The development collection is organized by outcome and approval boundary, not language or framework.

| Bot | Takes in | Produces | Must stop before |
| --- | --- | --- | --- |
| [Spec Writer](bots/development/spec-writer/) | A selected idea, request, or unclear issue | An implementation-ready specification for human approval | Approving the specification or implementing it |
| [Bug Reproducer](bots/development/bug-reproducer/) | A selected GitHub issue and product URL | A reproducibility verdict and evidence report | Editing code or invoking a coding agent |
| [PR Producer](bots/development/pr-producer/) | An approved issue, specification, or reproduction report | A focused branch and reviewable pull request through the built-in Cursor Cloud Agent | Reviewing, approving, or merging the pull request |
| [PR Verifier](bots/development/pr-verifier/) | A pull request, its brief, diff, tests, and GitHub checks | An evidence-backed `PASS`, `BLOCK`, or `HOLD` verdict | Implementing fixes or merging the pull request |

Use each role as a separate Grok Bot:

```text
Feature request → Spec Writer → Human spec approval ─┐
Bug report → Bug Reproducer → Evidence report ──────┤
                                                     ↓
                                              PR Producer
                                                     ↓
                                               PR Verifier
                                                     ↓
                                          Human merge decision
```

The PR Producer and PR Verifier must never be the same Bot or share the same conversation. The separation is the feature.

## Quick start

Grok Bot does not import files. The profile in git is the source; a new bot fetches it.

1. Create a new Grok Bot.
2. Copy the bot's raw `SETUP.md` URL below and paste it as the first message.

### Spec Writer

```text
https://raw.githubusercontent.com/HAEGONG/grok-bot-profiles/main/bots/development/spec-writer/SETUP.md
```

### Bug Reproducer

```text
https://raw.githubusercontent.com/HAEGONG/grok-bot-profiles/main/bots/development/bug-reproducer/SETUP.md
```

### PR Producer

```text
https://raw.githubusercontent.com/HAEGONG/grok-bot-profiles/main/bots/development/pr-producer/SETUP.md
```

### PR Verifier

```text
https://raw.githubusercontent.com/HAEGONG/grok-bot-profiles/main/bots/development/pr-verifier/SETUP.md
```

3. Connect GitHub when asked. Send the First task from that bot's README. Create PR Verifier as a **new** Bot, never from the PR Producer conversation.

Do not paste `PROFILE.md` into Description by hand. `SETUP.md` tells the bot to fetch the profile and set Name, Title, and Description.

New to Grok Bots? See the official [Get started](https://docs.x.ai/grok-bot/get-started) and [Create and manage Bots](https://docs.x.ai/grok-bot/bots) guides.

## What is in a profile?

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
- **Keep Description durable.** Put permanent role rules in `PROFILE.md`; put implementation-specific checklists in `SETUP.md` or the task conversation.
- **Make failure explicit.** Use outcomes such as `BLOCKED` or `HOLD` instead of guessing or silently expanding authority.
- **Require observable evidence.** Never invent logs, test results, check status, URLs, or repository state.
- **Stop at the boundary.** Opening a pull request, approving it, merging it, deploying it, and contacting people are different permissions.

One bot may combine several professional disciplines when they support the same outcome. Create a separate bot when the outcome, information sources, tools, schedule, or approval boundary changes.

## Create a profile

Give the following prompt to an AI coding agent working in this repository. Replace the bot idea with your own:

```text
Create a new Grok Bot profile in this repository.

Bot idea:
[Describe the bot, what it receives, the outcome it produces, and where its authority ends.]

Requirements:
- Read templates/bot/ and follow its three-file structure.
- Choose exactly one category from: productivity, marketing, sales, ops, personal, development.
- Create the profile at bots/<category>/<slug>/.
- Define one repeatable outcome and the sources the bot may read.
- Specify the exact deliverable and explicit failure states.
- State what the bot must not send, change, approve, purchase, publish, or otherwise do.
- Keep durable role rules in PROFILE.md and setup instructions in SETUP.md.
- Keep PROFILE.md, SETUP.md, and README.md consistent.
- Replace every placeholder and verify all local and raw GitHub links.
- Do not modify existing profiles.
```

Review the result before using it:

1. The bot has one outcome and one clear approval boundary.
2. Its information sources and required integrations are explicit.
3. Its deliverable and failure states are observable.
4. It cannot approve its own work or silently expand its authority.
5. `PROFILE.md`, `SETUP.md`, and `README.md` agree on the name, integrations, and First task.
6. No placeholders remain and all links resolve.

The source template is [`templates/bot/`](templates/bot/).

## Repository layout

```text
bots/
  development/
    spec-writer/
    bug-reproducer/
    pr-producer/
    pr-verifier/
templates/
  bot/
```

## Contributing

Profiles should be useful immediately after installation, narrow enough to trust, and explicit about authority. Pull requests for new profiles and improvements to existing ones are welcome.

If these profiles save you a setup cycle, star the repository and share the workflow that worked for you.
