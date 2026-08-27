# Research Scout

Turn a keyword into a research brief in which every claim carries the source it came from, so you can judge the evidence instead of trusting a summary.

Category: productivity

## The setup prompt

Create a new Grok Bot and paste this URL as the first message:

https://raw.githubusercontent.com/HAEGONG/grok-bot-profiles/main/bots/productivity/research-scout/SETUP.md

The bot fetches [PROFILE.md](PROFILE.md) and sets Name, Title, and Description. Do not paste the profile by hand.

## Connect first

Nothing. This bot needs no plugins.

This profile lists no connectors, so the bot works through the browser on the Bot's computer and opens every source in a new private browsing session. If a built-in web search tool turns out to be available in your Bot, it uses that to find candidates and still opens each source in the private browser before citing it. The profile does not assume the tool exists, so the brief stays valid either way, and `Searches run` tells you which path it actually used.

Reddit and X get separate rules, because they fail in different ways. Reading public subreddits, threads, and comments signed out is in scope, and the bot treats a 403 from an HTTP fetch or a Reddit API as a quirk of that access path rather than proof that Reddit is unreachable: it retries the same URL in the private browser first, and falls back to `old.reddit.com` when the new interface gets in the way. Signed-out X search, by contrast, currently redirects to login or onboarding with no posts visible, so the bot reads an individual X URL only when it loads without a login wall, marks that URL unreachable when it hits login or a CAPTCHA, and does not claim X as a working source path unless a page actually rendered while signed out during that run.

Reading stays signed-out on purpose. A signed-in session would let the bot reach content you cannot see through the brief's own source URLs, and it would put a write-capable account one click away from a read-only role.

Signed-out reading takes explicit handling here, because every bot on your account shares one computer, one browser, and its stored logins. A session that another bot signed in would otherwise carry over silently. So this bot opens each source in a new private browsing session, and it never signs out of a shared session or clears its cookies, since that would change another bot's state. When it cannot confirm a signed-out read for one source, it names that site as unreachable and keeps researching through the paths that remain, instead of reading as whoever is logged in.

If a source needs an account, a paid subscription, or community membership, the bot records it under `Gaps` as unreachable instead of working around the restriction.

## What you get back

A brief with `Question`, `Answer so far`, `Findings`, `Agreement and disagreement`, `Source quality`, `Gaps`, and `Searches run`. Findings are numbered `F-1`, `F-2`, and so on, each with its source URL and date, and each marked as either the originating source or a repetition of another one. A page that shows no date gets `Date not shown` rather than an inferred one.

`Searches run` exists so you can see the coverage behind the answer. A brief built from three queries and a brief built from twenty read the same otherwise.

Three named outcomes replace a confident-sounding answer when one is not warranted. `NEEDS_SCOPE` comes back when the keyword has two readings that would produce different briefs, so the bot asks the distinguishing question rather than silently picking one. `THIN_EVIDENCE` comes back when nothing independently corroborates the core claim; five articles that all repeat one original count as one source, not five. `BLOCKED` comes back only when no allowed path can cover your scope at all, so a single unavailable platform lands in `Gaps` and the research continues.

The first two exist because the failure this role invites is a fluent brief assembled from general knowledge with sources attached decoratively.

## What it will not do

It reports, and stops there. It does not post or reply anywhere, contact anyone it found, sign up or spend, or make the decision the research is meant to inform. Every write action on every platform is out of scope.

It also returns its brief only in the conversation you addressed it in. This profile names no destination bot, so it will not hand the brief to another bot, including through a general request in a group chat where a participating bot might pick it up. Copy what you need into the next bot's conversation yourself.

## Profile

[PROFILE.md](PROFILE.md)

Durable identity lives in [PROFILE.md](PROFILE.md). SETUP fetches it; do not paste the YAML frontmatter into the app.

## First task

`Ask me for the keyword or question to research, and ask which scope applies, covering the time window, the region or language, and whether to prioritize X, Reddit, or the open web. If I give a keyword without a scope, state the default scope you will apply and start; if the keyword itself has two readings that would change the answer, return NEEDS_SCOPE instead of choosing one. Then leave the research brief in this chat without posting, replying, or contacting anyone.`
