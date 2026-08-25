# Weekday PR scan

- **Name:** Weekday PR scan
- **Slug:** `weekday-pr-scan`
- **Schedule:** Every weekday at 10:00 in the user's local time
- **Intent:** Digest open PRs; do not act on them

## Prompt

Every weekday at 10:00 in the user's local time, list open pull requests
on `{github_repo}`. For each: author, title, CI status if visible, age,
whether it looks blocked on review.

Post a short digest in this conversation. Do not approve, merge, comment
on GitHub, or dispatch a cloud agent unless the user asked. If GitHub is
disconnected, say so.
