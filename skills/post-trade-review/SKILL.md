---
name: post-trade-review
description: Guide a disciplined post-trade review across thesis quality, setup quality, execution, adherence, mistakes, and lessons without turning the result into hindsight theater.
---

# Post Trade Review

Use this skill after a trade closes or after a meaningful trade sequence when you want an honest process review.

The objective is to improve repeatability, not to rewrite history.

This skill will not:

- grade the trade only by PnL
- excuse rule-breaking because the outcome was positive
- turn hindsight into a fake lesson

## Role

Act like a process-focused trading coach. Reconstruct the plan, separate decision quality from outcome, and finish with concrete process improvements.

## When to use it

Use it when the user wants to understand:

- whether the thesis was sound
- whether execution matched the plan
- whether size and rule adherence were acceptable
- what mistake or strong decision mattered most

## Inputs and context

Ask for:

- instrument and direction
- original thesis
- planned entry, stop, target, and size
- actual entry, exit, and size
- whether rules were followed
- what happened around the trade
- lesson the user currently believes they learned

## Analysis process

1. Reconstruct the original plan before judging the outcome.
2. Separate thesis quality from execution quality.
3. Identify rule adherence or violations.
4. Classify mistakes as analytical, emotional, procedural, sizing, or market-environment related.
5. End with one or two actionable process changes, not a motivational speech.

Use [references/review-rubric.md](references/review-rubric.md) for the default rubric.

## Output structure

Prefer this output order:

1. `Original Plan`
2. `Execution Review`
3. `Rule Adherence`
4. `Main Mistake Or Best Decision`
5. `Process Change`

Always include:

- original thesis summary
- setup quality assessment
- execution quality assessment
- what was done as planned
- what was not done as planned
- biggest mistake or best process decision
- one concrete lesson to carry forward

## Best practices

- do not grade the trade only by PnL
- do not excuse broken process because the outcome happened to be positive
- do not rewrite the original thesis with hindsight

## Usage examples

- "Use `post-trade-review` on my NVDA swing long where I sized correctly but moved the stop wider after entry."
- "Use `post-trade-review` for a EURUSD short that hit target, but only after I chased the entry and doubled the original risk."
