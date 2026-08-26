#!/usr/bin/env bash
#
# Verifies that every relative Markdown link in this repository resolves to a
# file that exists, and that no placeholder text remains outside templates/.
#
# Only local paths are checked. Raw URLs are skipped on purpose: a link to the
# default branch returns 404 until the change is merged, so a network check
# would fail for every legitimate new profile.

set -euo pipefail

repo_root=$(git rev-parse --show-toplevel)
cd "$repo_root"

failures=0

while IFS= read -r file; do
  dir=$(dirname "$file")
  while IFS= read -r target; do
    # Strip an optional link title and any anchor before resolving the path.
    path=${target%% *}
    path=${path%%#*}
    [ -n "$path" ] || continue
    case "$path" in
      http://*|https://*|mailto:*) continue ;;
    esac
    if [ ! -e "$dir/$path" ]; then
      printf 'broken link: %s -> %s\n' "$file" "$path"
      failures=$((failures + 1))
    fi
  done < <(grep -o ']([^)]*)' "$file" | sed 's/^](//; s/)$//')
done < <(git ls-files '*.md')

# Placeholders belong only in templates/, which new profiles copy and fill in.
while IFS= read -r file; do
  if grep -nE 'ORIGIN_OWNER|ORIGIN_REPOSITORY|DEFAULT_BRANCH|FIRST_TASK|ONE_DELIVERABLE|STOP_BEFORE' "$file"; then
    printf 'unreplaced placeholder: %s\n' "$file"
    failures=$((failures + 1))
  fi
done < <(git ls-files '*.md' | grep -v '^templates/')

if [ "$failures" -gt 0 ]; then
  printf '\n%d problem(s) found.\n' "$failures"
  exit 1
fi

printf 'All relative links resolve and no placeholders remain.\n'
