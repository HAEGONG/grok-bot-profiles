# Grok Bot profiles

A collection of shareable [Grok Bot](https://x.ai/news/introducing-grok-bot)
personas you can install as always-on teammates.

[Grok Bot](https://x.ai/bot) is Cursor / xAI’s desktop teammate: a named Bot
with a description, memory, routines, skills, and connectors. Each Bot works
on its own cloud computer — browser, filesystem, and terminal — signs into
the tools you already use, coordinates with other Bots in DMs and group
chats, and keeps going after you close the laptop.

There is no official import command in the app today. Install is: create a
Bot, paste the description, send `ADOPT.md` as the first message, then
optionally add the routines, skills, and connectors listed in `recipe.json`.

This repository is **private** today. When it is public, this is the
community pack.

## Install in three steps

1. **Create a Bot.** In Grok Bot, create a new teammate. Set **name**,
   **title**, **avatar shape**, and **avatar color** from
   `profiles/<slug>/profile.json`.
2. **Paste the description.** Use the `description` field from
   `profile.json` (the same role summary appears at the top of `SOUL.md`).
3. **Send `ADOPT.md` as the first message.** That file is written as
   instructions *to* the Bot: identity, memory seeds, suggested routines.
   Connect the plugins in `connectors.md` when the Bot asks — never paste
   secrets into chat.

`recipe.json` is the canonical pack (`botTemplateSchema`) for share/import
tooling. Until a share link exists, treat it as the source of truth and
`ADOPT.md` as the human paste.

## Profile catalog

| Folder | Name | Title | Best for |
| --- | --- | --- | --- |
| [`starter`](profiles/starter/) | Starter | Patient Guide | First Bot; learning Grok Bot without overwhelm |
| [`senna`](profiles/senna/) | Senna | Top Orchestrator | Front door; routes work to specialist Bots |
| [`code`](profiles/code/) | Code | Implementation Lead | Bugs, PRs, reviews; hands implementation to Cursor cloud agents |
| [`research`](profiles/research/) | Research | Investigator | Evidence-based research with citations |
| [`communication`](profiles/communication/) | Communication | Comms Desk | Email, Slack, meetings — drafts only, never auto-send |
| [`knowledge`](profiles/knowledge/) | Knowledge | Librarian | Docs, wikis, Notion/Drive, portable notes |
| [`business`](profiles/business/) | Business | Strategist | Product and strategy briefs; no fake metrics |
| [`creative`](profiles/creative/) | Creative | Design Lead | UI, visuals, image generation with rationale |
| [`ops-desk`](profiles/ops-desk/) | Donna | Ops Desk | Executive assistant; weekday briefing and calendar |

A suggested fleet: **Senna** as the front door, plus **Code**, **Research**,
**Communication**, and **Donna** as specialists. Add the others when the
work shows up.

## Pack layout

Each folder under `profiles/` is one Bot:

| File | Role |
| --- | --- |
| `profile.json` | Shareable identity (`name`, `description`, `title`, `avatarShape`, `avatarColor`) |
| `recipe.json` | Canonical pack: profile, memory, skills, routines, plugins |
| `SOUL.md` | Full persona and operating instructions |
| `ADOPT.md` | Paste-ready first message, written **to** the Bot |
| `connectors.md` | Human notes for plugins listed in `recipe.plugins` |
| `routines/` | Optional markdown mirrors of suggested routines |
| `skills/` | Optional short skills that are useful on Grok Bot |

Field rules: [FORMAT.md](FORMAT.md). How to add a pack:
[CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE).
