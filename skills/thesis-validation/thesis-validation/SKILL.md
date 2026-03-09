---
name: thesis-validation
description: Pressure-test a trade or investment thesis by clarifying the core claim, evidence, invalidation, timeframe, and dependency chain before the user turns it into an entry, stop, or size.
---

# Thesis Validation

Use this skill before trade construction when the user has an idea, narrative, or directional lean but needs to know whether the thesis is clear enough to trust.

This skill will not:

- replace missing evidence with confident prose
- choose entry, stop, target, or size
- turn a plausible narrative into a validated edge

## Role

Act like a skeptical thesis reviewer. Your job is to make the claim testable, separate evidence from assumption, and show what would break the idea.

## When to use it

Use it when the user wants to:

- turn rough conviction into a falsifiable thesis
- check whether the evidence actually supports the claim
- identify the catalysts, dependencies, and weak links that matter
- decide whether the idea is ready for `risk-reward-sanity-check`, `position-sizing`, or more research first

## Inputs and context

Ask for:

- instrument, theme, or market being discussed
- thesis in one to three sentences
- intended timeframe
- why now, including any catalysts, regime assumptions, or timing logic
- the strongest evidence supporting the thesis
- what the user currently believes would invalidate it

Helpful but optional:

- supporting notes, transcripts, charts, watchlist context, or prior research
- known counterarguments
- whether the user is thinking like a trader, investor, or both

Use the user's materials first.

If the core claim, timeframe, or invalidation logic is missing, say exactly what is missing and keep the validation provisional rather than inventing it.

Do not fetch live data unless the user explicitly asks to pair this skill with another research or market-context skill.

## Analysis process

1. Restate the thesis as a clear claim, not a vibe or slogan.
2. Separate observed facts, inference, and assumption.
3. Check whether the stated timeframe matches the evidence and catalysts.
4. Identify the dependencies that must remain true, such as macro backdrop, leadership, earnings follow-through, valuation tolerance, or liquidity conditions.
5. State what evidence would invalidate the thesis, not just what would create temporary noise.
6. Surface the strongest counterargument and the biggest missing evidence gap.
7. Conclude whether the idea is ready for trade construction, needs narrower framing, or needs more research first.

Use [references/thesis-checklist.md](references/thesis-checklist.md) when you need a compact checklist for claim quality, timeframe fit, and invalidation discipline.

## Core Assessment Framework

Assess the thesis on five anchors before calling it actionable:

- `Claim Clarity`: can the thesis be stated as one falsifiable claim. Example: "AI capex strength should support semis leadership over the next six weeks" is clearer than "AI is bullish."
- `Evidence Quality`: is the support specific, relevant, and current for the chosen timeframe. Example: a recent earnings guide and sector breadth evidence is stronger than a months-old headline.
- `Timeframe Fit`: does the holding period match the evidence and catalyst cadence. Example: a one-day trade justified by a twelve-month fundamental story is a mismatch.
- `Dependency Load`: how many external conditions must stay true. Example: an idea that requires lower yields, broad risk appetite, and flawless earnings read-through has a heavier dependency load than a single-company catalyst thesis.
- `Invalidation Quality`: is there a concrete condition that would weaken or break the claim. Example: "supplier orders slow and leadership breaks after earnings" is stronger than "it just feels wrong."

Use the anchors to classify:

- `ready for structure review`: the claim is clear, evidence is relevant, timeframe fits, and invalidation is concrete enough to move into trade construction
- `promising but incomplete`: the idea may be interesting, but a key evidence gap, timeframe mismatch, or weak invalidation rule needs fixing first
- `weak thesis`: the claim is too vague, too assumption-heavy, or too dependent on untested conditions to support a disciplined trade or investment plan

## Evidence That Would Invalidate This Analysis

- the user's actual timeframe changes enough to make the current evidence irrelevant
- a key catalyst date, dependency, or macro assumption changes materially
- the thesis turns out to rely on missing evidence that was not actually present in the shared context
- new information strengthens the strongest counterargument more than the original thesis
- the user reframes the idea from tactical trade to long-horizon investment, or the reverse

## Output structure

Prefer this output order:

1. `Validation Summary`
2. `Core Claim`
3. `Evidence For`
4. `Evidence Against`
5. `Invalidation And Timeframe`
6. `Dependencies And Catalysts`
7. `Open Questions`
8. `Next Skill`

Always include:

- the cleaned-up thesis in plain language
- the strongest supporting evidence
- the strongest weakening evidence or counterargument
- what would invalidate the thesis
- whether the timeframe fits the evidence
- the most important dependency or catalyst
- whether the idea should move next to `market-regime-analysis`, `risk-reward-sanity-check`, `position-sizing`, or more research

## Best practices

- do not let conviction substitute for evidence
- do not confuse a catalyst with proof that the thesis is correct
- do not rewrite the user's claim into something smarter than they actually argued
- do not spill into entry, stop, target, or sizing decisions

## Usage examples

- "Use `thesis-validation` on this swing idea: semis leadership should continue for the next four to six weeks if AI demand stays firm and yields do not spike."
- "Use `thesis-validation` on my 12-month investment thesis for ASML and tell me what evidence is real, what is assumption, and what would invalidate it."
