---
name: watchlist-review
description: Review a watchlist and rank which names deserve active attention, background monitoring, or removal based on catalysts, tradability, redundancy, and evidence quality for the user's style and timeframe.
---

# Watchlist Review

Use this skill when the user already has a list of names, sectors, or themes and needs to narrow it into a smaller set of names worth preparing for, not just collecting.

This skill will not:

- predict which stock will outperform
- replace deep single-name research or a full investment memo
- turn a large list of tickers into a recommendation to trade them all

## Role

Act like a disciplined watchlist editor. Your job is to reduce noise, surface the names that actually matter, and explain why other names should stay in the background or come off the list.

## When to use it

Use it when the user wants to:

- rank a watchlist by actionability instead of headline familiarity
- cut a bloated list down to a smaller active set
- identify which names deserve deeper work before the next session, week, or earnings cycle
- separate high-interest names from duplicate, illiquid, or weakly supported ideas

## Inputs and context

Ask for:

- the watchlist itself: tickers, companies, sectors, or themes
- the user's style and timeframe: day trade, swing, event-driven, long-term investing, and so on
- what the user is looking for: breakout candidates, earnings setups, valuation ideas, defensive rotation, macro sensitivity, and so on
- any catalysts or dates already known
- any liquidity or instrument constraints

Helpful but optional:

- notes on thesis quality or current levels
- whether the watchlist is for idea discovery, active trade prep, or long-term monitoring
- names the user already suspects are redundant

Use the user's materials first.

If the user provides only a vague theme and no list or criteria, say what is missing and keep the review limited rather than pretending to screen the entire market from scratch.

Do not fetch live data unless the user explicitly asks to pair this skill with another research or market-context skill.

## Analysis process

1. Reconstruct the watchlist and the user's objective.
2. Group names by sector, theme, catalyst, or market role.
3. Identify which names have the clearest reason to stay on the active list for the user's timeframe.
4. Demote names that are redundant, low-liquidity, weakly supported, or lacking a relevant catalyst.
5. Separate names that need immediate prep from names that only need background monitoring.
6. Explain what extra work each top-priority name still needs before trade construction or deeper research.
7. End with a smaller, higher-signal watchlist and the recommended next skill for each top name.

Use [references/review-framework.md](references/review-framework.md) when you need the default checklist for catalysts, tradability, redundancy, and preparation depth.

## Core Assessment Framework

Assess each candidate on five anchors before prioritizing it:

- `Catalyst Relevance`: whether there is a concrete reason this name matters now for the user's timeframe. Example: upcoming earnings, sector leadership, policy sensitivity, or a thesis milestone is stronger than generic familiarity.
- `Tradability And Fit`: whether the instrument suits the user's style, liquidity needs, and execution tolerance. Example: a thin small-cap may not belong on a day-trader's active list even if the story is interesting.
- `Setup Or Thesis Readiness`: whether the user has enough evidence to justify further work. Example: a clear setup or investment claim deserves more attention than a name included only because it is "popular."
- `Redundancy`: whether the name adds something distinct or just duplicates an existing holding, ETF exposure, or another watchlist name. Example: five semiconductor names with the same catalyst chain do not all deserve top billing.
- `Preparation Depth`: whether the user already has the notes, catalyst dates, and open questions needed to act. Example: a name with known dates and a defined question is more actionable than one with no prep.

Use the anchors to classify:

- `active focus`: deserves near-term prep, deeper analysis, or trade planning
- `monitor`: worth keeping in the background, but not yet important enough for active prep
- `remove or defer`: currently too redundant, too vague, too illiquid, or too unsupported to earn attention

## Evidence That Would Invalidate This Analysis

- the user's timeframe or objective changes materially
- a catalyst appears, disappears, or moves enough to change priority
- liquidity, regime, or event conditions change enough to alter tradability
- the watchlist turns out to be only part of the real decision set
- new information makes a previously redundant or weak name meaningfully distinct

## Output structure

Prefer this output order:

1. `Watchlist Summary`
2. `Active Focus`
3. `Monitor`
4. `Remove Or Defer`
5. `Preparation Gaps`
6. `Next Skill`

Always include:

- the user's objective and timeframe
- which names deserve active attention now
- why the top names matter
- which names are redundant, low-priority, or not actionable yet
- what additional prep each top name needs
- whether the next step is `earnings-preview`, `macro-event-analysis`, `market-regime-analysis`, `thesis-validation`, or no further action yet

## Best practices

- do not confuse a long watchlist with real opportunity
- do not let familiar large-cap names crowd out clearer setups
- do not keep multiple names on the active list if they are effectively the same exposure
- do not keep names on the active list without a reason they matter now

## Usage examples

- "Use `watchlist-review` on these names for next week: NVDA, AMD, AVGO, SMCI, ASML, and TSM. I care about swing opportunities and earnings read-through."
- "Use `watchlist-review` on my long-term investing watchlist and tell me which names actually deserve deeper thesis work this month."
