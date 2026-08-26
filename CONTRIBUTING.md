# Contributing

Thanks for considering a contribution. This collection stays useful only while every profile keeps one outcome, one approval boundary, and one clearly defined job, so most of the review effort goes toward those three properties.

## What belongs here

A profile belongs in this repository when it is immediately useful after installation, narrow enough that a person can predict what the bot will do, and explicit about where the bot's authority ends. A profile that covers several unrelated outcomes should be split into separate bots instead.

A profile does not belong here when it depends on credentials, private infrastructure, or an internal service that other people cannot reach.

## Adding a profile

1. Read [CREATE_YOUR_OWN_BOT.md](CREATE_YOUR_OWN_BOT.md). It contains the generation prompt and the review checklist that reviewers apply to your pull request.
2. Copy the three-file structure from [`templates/bot/`](templates/bot/) into `bots/<category>/<slug>/`. Choose exactly one category from productivity, marketing, sales, ops, personal, or development.
3. Keep durable role rules in `PROFILE.md`, one-time setup instructions in `SETUP.md`, and installation guidance in `README.md`.
4. Add the profile to the discovery table in every root README, including [README.ko.md](README.ko.md), and write each translated entry in that README's language.
5. Work through the checklist in [CREATE_YOUR_OWN_BOT.md](CREATE_YOUR_OWN_BOT.md) before opening the pull request. The pull request template repeats it.

Do not modify [`templates/bot/`](templates/bot/) or files inside an existing profile directory in the same pull request that adds a new profile. Separate changes are easier to review and to revert.

## Changing an existing profile

State which promise of the profile is currently wrong, and quote the behavior you observed. A change that narrows a boundary or makes a failure outcome observable is usually straightforward. A change that widens what a bot may do needs to explain why the wider authority is safe, because that is the property this collection exists to protect.

## Verifying your change

There is no build step. Before opening a pull request, confirm by hand that:

- `PROFILE.md`, `SETUP.md`, and `README.md` agree on the bot's name, its integrations, and its First task.
- Every relative link resolves to a file that exists.
- Raw URLs use the owner and repository of the origin remote and the repository's default branch. A default-branch 404 is expected until the change is merged, so verify the local path instead.
- No placeholder text, tokens, credentials, or secrets remain in any file.

## Reporting a problem

Open an issue with the [profile problem template](.github/ISSUE_TEMPLATE/profile-problem.md) when a bot acted outside its stated boundary or returned the wrong deliverable. Quote what you sent and what the bot did; a summary usually loses the detail that explains the behavior.

To suggest a profile without writing one, use the [new profile template](.github/ISSUE_TEMPLATE/new-profile.md).

## License

By contributing, you agree that your contribution is licensed under the [Creative Commons Attribution 4.0 International License](LICENSE), the same license that covers this repository.
