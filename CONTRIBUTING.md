# Contributing

Thanks for helping this become a public Grok Bot pack. Profiles here should
feel like colleagues you would actually install, not prompt dumps.

## Add a profile

1. Read [FORMAT.md](FORMAT.md). `recipe.json` is canonical.
2. Copy an existing folder under `profiles/` as a starting point.
3. Use a new kebab-case slug. Put the Bot’s display name in `profile.json`,
   not in the folder name, unless they match.
4. Fill every required file:

   - `profile.json` — only `name`, `description`, `title`, `avatarShape`,
     `avatarColor`
   - `recipe.json` — `profile` must match `profile.json`; memory, skills,
     routines, plugins as needed
   - `SOUL.md` — Grok Bot persona (80–200 lines)
   - `ADOPT.md` — first message written **to** the Bot
   - `connectors.md` — plugins for this role; no secrets

5. Keep `recipe.profile` identical to `profile.json`.
6. Memory items: generic persona facts only, `kind` `profile` or `log`,
   max 32 items, max 500 characters each.
7. Routines: weekday daytime in the user’s local time; placeholders like
   `{slack_channel}` and `{github_repo}` instead of real IDs.
8. Plugins: known Cursor marketplace ids only (`github`, `slack`, `gmail`,
   `google-calendar`, `google-drive`, `notion-workspace`, `linear`). Omit
   if unknown.
9. Run `python3 scripts/validate-profiles.py`.

## License

New original writing in this repo is MIT. See [LICENSE](LICENSE).

## Do not submit

- Offensive security, pentest, exploit, or “red team” packs
- Kids profiles or sexual/romantic content involving minors
- Secrets, tokens, private paths, Discord channel IDs
- `namedBy`, `serverId`, `harness`, `settings.json`, `store.db`, memory
  logs, `runs.json`

## Writing bar

- Persona first, machinery second.
- Tell the Bot what it **is** and how it **decides**.
- Rank recommendations. Cite sources. Never invent metrics.
- Approval gates for send / publish / pay / delete / production change.

## Pull requests

Use a short title that names the Bot or the doc change. Keep the PR to one
profile unless the change is shared documentation.
