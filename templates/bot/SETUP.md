Create this Grok Bot. Name = NAME. Title = ONE JOB. Fetch https://raw.githubusercontent.com/ORIGIN_OWNER/ORIGIN_REPOSITORY/DEFAULT_BRANCH/bots/CATEGORY/SLUG/PROFILE.md and set Description to the markdown body after the YAML frontmatter (from `# NAME` through First task). Do not put the frontmatter in Description. Connect the plugins listed below under Settings → Plugins. Then send the First task from the README. Follow the permissions and stop-before boundary in PROFILE.md; do not infer additional permission. Return results in the conversation you were addressed in, and hand work to another Bot only when PROFILE.md names that destination and the user approves the content, destination, and requested next action. The First task must stay inside the same boundary.

Connect first:
- PLUGIN
