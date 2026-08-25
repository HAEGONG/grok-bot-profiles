---
name: pr-review-pack
description: Use when reviewing a pull request on GitHub or when a cloud agent opens a PR.
---

# PR review pack

Inputs: `{github_repo}` and the PR URL or number.

1. Read the PR description and diff.
2. Check tests exist for the change; note gaps.
3. Flag correctness, security, and contract breaks — not style nits
   unless they hide bugs.
4. Try to reproduce claimed behavior when practical (clone, test
   command, or cloud agent).
5. Return: summary, verdict (approve / request changes / comment),
   blocking issues, non-blocking notes.

Never merge without the user. Never rubber-stamp an untested diff.
