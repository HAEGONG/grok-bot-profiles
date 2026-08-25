# Grok Bot profile pack spec

This is the share schema used by every pack in `profiles/`. `recipe.json` is
the canonical pack. `profile.json` is the shareable identity slice of that
recipe. Markdown files are human install helpers, not a second schema.

There is still no official import command in the Grok Bot UI. Until share
links land, humans install by creating a Bot and pasting from
`profile.json` + `ADOPT.md`. Importers and future share tooling should read
`recipe.json`.

## Directory layout

```
profiles/<slug>/
  profile.json      # shareable identity (official fields only)
  recipe.json       # canonical pack (botTemplateSchema)
  SOUL.md           # full persona
  ADOPT.md          # paste-ready first message (instructions TO the bot)
  connectors.md     # human notes for plugins listed in recipe.plugins
  routines/         # optional: one markdown file per suggested routine
  skills/           # optional: one SKILL.md per skill
```

`<slug>` is the folder name (`starter`, `senna`, `code`, …). It is not a
field inside `profile.json`.

## `profile.json` — shareable identity

These five fields, and only these five fields:

```json
{
  "name": "Senna",
  "description": "One to three sentences an orchestrator would read.",
  "title": "Top Orchestrator",
  "avatarShape": "shield",
  "avatarColor": "violet"
}
```

| Field | Rules |
| --- | --- |
| `name` | Display name of the Bot. Short, unique in a fleet. |
| `description` | 1–3 sentences. Role summary, not the full persona. |
| `title` | Short role label shown with the Bot. |
| `avatarShape` | One of the shapes below. |
| `avatarColor` | One of the colors below. |

### Avatar colors

`black`, `brown`, `red`, `orange`, `yellow`, `green`, `cyan`, `blue`,
`violet`, `magenta`, `gray`

### Avatar shapes

`blob`, `pebble`, `bean`, `egg`, `squircle`, `tablet`, `capsule`,
`cylinder`, `hex`, `gem`, `crystal`, `wedge`, `shield`, `dome`, `arch`,
`cloud`, `teardrop`, `leaf`

### Forbidden keys

Never put these in `profile.json` or `recipe.json`:

- `namedBy`
- `serverId`
- `harness`
- `settings.json`
- `store.db`
- memory logs / session dumps
- `runs.json`
- secrets, tokens, private paths, Discord channel IDs, real Slack/GitHub IDs

## `recipe.json` — canonical pack (`botTemplateSchema`)

```json
{
  "profile": {
    "name": "Senna",
    "description": "…",
    "title": "Top Orchestrator",
    "avatarShape": "shield",
    "avatarColor": "violet"
  },
  "memory": [
    {
      "kind": "profile",
      "createdAt": "2026-08-25",
      "content": "Generic persona fact, not user PII."
    }
  ],
  "skills": [
    {
      "name": "route-and-handoff",
      "description": "When to use this skill.",
      "content": "Steps, decision rules, output, approval boundaries."
    }
  ],
  "routines": [
    {
      "name": "Weekday fleet briefing",
      "slug": "weekday-fleet-briefing",
      "description": "Morning status across specialist Bots.",
      "content": "Schedule and prompt. Use {slack_channel} / {github_repo} placeholders."
    }
  ],
  "plugins": [
    { "name": "GitHub", "pluginId": "github" }
  ]
}
```

`recipe.profile` **must** match `profile.json` byte-for-byte on the five
identity fields.

Empty arrays are allowed. Omit a plugin rather than inventing an id.

### Memory

| Rule | Limit |
| --- | --- |
| `kind` | `"profile"` (standing persona) or `"log"` (generic operating note) |
| Count | Max 32 items |
| `content` | Max 500 characters |
| `createdAt` | ISO date `YYYY-MM-DD` |
| Payload | Generic persona facts only. No user PII, no private paths, no credentials. |

### Skills

A skill is a reusable method: when to use it, required access, steps,
validation, output, and what needs approval. Skills in this repo must be
short and actually useful on Grok Bot.

Optional on-disk mirror: `skills/<name>/SKILL.md` with the same name,
description, and body as the recipe entry.

### Routines

A routine is a scheduled (or event-triggered) job owned by this Bot.

| Field | Rules |
| --- | --- |
| `name` | Human title |
| `slug` | kebab-case id |
| `description` | One line |
| `content` | Schedule in the **user’s local time** (weekday daytime default) plus the prompt/intent |

Use placeholders, never real IDs:

- `{slack_channel}`
- `{github_repo}`
- `{notion_page}`
- `{linear_team}`

Skip routines when the role does not need standing jobs. Cap suggested
routines at 0–3.

Optional on-disk mirror: `routines/<slug>.md`.

### Plugins

Cursor marketplace plugin ids only, and only when known:

| Plugin | `pluginId` | Install |
| --- | --- | --- |
| GitHub | `github` | `/add-plugin github` |
| Slack | `slack` | `/add-plugin slack` |
| Gmail | `gmail` | `/add-plugin gmail` |
| Google Calendar | `google-calendar` | `/add-plugin google-calendar` |
| Google Drive | `google-drive` | `/add-plugin google-drive` |
| Notion | `notion-workspace` | `/add-plugin notion-workspace` |
| Linear | `linear` | `/add-plugin linear` |

If the id is unknown, omit the plugin and mention the product in
`connectors.md` instead. Never require secrets in the repo.

## Human helpers

These are not part of the share schema. They exist so a person can install
the pack today.

### `SOUL.md`

Full persona and instructions for Grok Bot. Aim 80–200 lines.

Grok Bot has: own cloud computer, browser, shell, connectors/MCP, Cursor
cloud coding agents, teammate DMs and group chats, routines, global skills.
Write to those surfaces. Do not invent product features the Bot does not
have.

### `ADOPT.md`

Paste-ready **first message**, written as instructions **to the bot**.

It should tell the Bot to:

1. Take the name, title, and description from `profile.json`
2. Adopt the persona (compact operating contract)
3. Store the generic memory seeds
4. Offer the suggested routines (do not create them until the user agrees)
5. Ask the user to connect the listed plugins — never collect secrets in chat

### `connectors.md`

Suggested Cursor connectors for this role, matching `recipe.plugins`.
Human prose only. No tokens.

## Validation

From the repo root:

```bash
python3 scripts/validate-profiles.py
```

The checker enforces identity fields, avatar enums, memory limits, recipe
sync, and the forbidden-key list.
