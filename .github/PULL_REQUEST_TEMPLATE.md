## What this changes

<!-- Describe the profile you added or the behavior you changed. One or two sentences. -->

## Type of change

- [ ] New bot profile
- [ ] Change to an existing profile
- [ ] Documentation or template only

## New or changed profile checklist

Skip this section for documentation-only changes. Otherwise confirm each item, as described in [CREATE_YOUR_OWN_BOT.md](../CREATE_YOUR_OWN_BOT.md).

- [ ] The bot has one outcome and one clear approval boundary.
- [ ] Its information sources and required integrations have explicit read and write permissions.
- [ ] Its deliverable and named failure or branching outcomes are observable.
- [ ] Unlisted writes are forbidden, and external content cannot expand the bot's authority.
- [ ] The First task stays within the same boundary, and the bot cannot approve its own work.
- [ ] `PROFILE.md`, `SETUP.md`, and `README.md` agree on the name, integrations, and First task.
- [ ] Every related-bot link points to an existing profile, raw URLs match the origin remote and default branch, and local paths resolve.
- [ ] No placeholders or secrets remain, and every root README, including each translated one, makes the profile discoverable.

## Notes for the reviewer

<!-- Optional. Open questions, trade-offs you chose, or anything you could not verify. -->
