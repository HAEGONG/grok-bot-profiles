# Grok Bot Profiles

Ready-to-use profiles for focused Grok Bots. Each bot owns one outcome and stops at a clear approval boundary.

## Development

The development collection is organized by responsibility, not language or framework:

- [Bug Reproducer](bots/development/bug-reproducer/) — reproduces a reported bug and returns evidence without changing code
- [PR Producer](bots/development/pr-producer/) — directs the built-in Cursor Cloud Agent to implement approved work and produce a pull request without merging it
- [PR Verifier](bots/development/pr-verifier/) — independently checks tests, contracts, and regressions, then passes, blocks, or holds the pull request

Use them as a pipeline:

```text
Bug Reproducer → PR Producer → PR Verifier → Human merge decision
```

## Install a bot

1. Open the bot's directory.
2. Follow its `README.md`.
3. Connect only the plugins listed for that bot.
4. Keep separate Grok Bots for reproduction, implementation, and review.

## Create another profile

Start with the files in [`templates/bot/`](templates/bot/). Keep every bot focused on one repeatable outcome and state what it must never do.

Grok Bots do not import profile JSON. A profile is text mapped to the app's **Name**, **Title**, **Description**, **Avatar**, and **Plugins** fields.

Official documentation: [Create and manage Bots](https://docs.x.ai/grok-bot/bots) · [Get started](https://docs.x.ai/grok-bot/get-started) · [Use cases](https://docs.x.ai/grok-bot/use-cases)

## App field mapping

| App field | Repository source |
| --- | --- |
| Name | `PROFILE.md` frontmatter `name` |
| Title | `PROFILE.md` frontmatter `title` |
| Description | `PROFILE.md` body, from `# NAME` through `First task`; exclude the YAML frontmatter |
| Avatar | Configure in the app |
| Plugins | frontmatter `integrations` → Settings → Plugins |

Keep only durable behavior in the Description. Put one-off instructions in the conversation.

## Add a bot

```bash
cp -R templates/bot bots/<category>/<slug>
```

Categories: `productivity` · `marketing` · `sales` · `ops` · `personal` · `development`

1. Fill in `NAME`, `ONE JOB`, `ONE_REPEATABLE_OUTCOME`, sources, deliverable, approval boundary, and `FIRST_TASK` in `PROFILE.md`.
2. Replace the matching placeholders in `SETUP.md` and `README.md`.
3. In the app, select **New → Create new agent**, then enter the Name, Title, and Description under **Edit Profile**.
4. Connect the plugins listed under `integrations` and send the First task.

One Grok Bot may combine multiple disciplines when they serve the same outcome. Split bots by outcome, tools and sources, working style, approval boundary, or schedule—not by language, framework, or arbitrary job title. Avoid general-purpose helper profiles.

## Repository layout

```
templates/bot/     Boilerplate to copy
bots/<category>/<slug>/
  PROFILE.md       Name, Title, integrations, and Description body
  SETUP.md         First setup message for a new Grok Bot
  README.md        Plugins, First task, and related bots
```
