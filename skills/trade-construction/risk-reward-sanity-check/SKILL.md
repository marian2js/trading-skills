---
name: risk-reward-sanity-check
description: Use when the user wants to test whether a proposed entry, stop, and target structure is coherent, asymmetric enough, and vulnerable to obvious failure modes before the trade is placed.
---

# Risk Reward Sanity Check

Use this skill when a trade idea exists but you want to inspect whether the structure makes sense before committing capital.

This skill does not predict whether the trade will work. It checks whether the plan is internally coherent.

This skill will not:

- tell the user a positive ratio makes the trade good
- replace thesis quality with a single numeric multiple
- assume the stop or target is valid just because it is mathematically neat

## Role

Act like a skeptical pre-trade reviewer. Challenge the structure before money is at risk.

## When to use it

Use it when the user wants to know whether:

- the stop and target make sense together
- the proposed asymmetry is real or just cosmetic
- the thesis actually supports the target
- obvious structural issues are hiding behind attractive math

## Inputs and context

Ask for:

- direction
- entry
- stop
- one or more targets
- thesis in one or two sentences
- optional context such as time horizon, catalyst, or nearby event risk

## Analysis process

1. Calculate distance from entry to stop and from entry to target.
2. Express the raw risk-reward ratio.
3. Check for structural issues such as targets inside noise, stops placed at obvious liquidity pools, or targets with no thesis support.
4. Explain what would invalidate the structure even if the ratio looks attractive on paper.
5. Separate "good ratio" from "good trade." They are not the same thing.

See [references/failure-modes.md](references/failure-modes.md) for the default checklist.

For agents that support code execution, use [references/calculation-helpers.md](references/calculation-helpers.md) for the shared helper functions that cover reward-to-risk math, expectancy, and trade-statistic cross-checks.

## Output structure

Prefer this output order:

1. `Setup Summary`
2. `Risk Reward Math`
3. `Structural Review`
4. `Decision Risk`
5. `What Must Be True`

Always include:

- raw risk-reward math
- asymmetry assessment
- the main structural concern
- what would need to be true for the target to be plausible
- any mismatch between thesis, stop, and holding period

## Best practices

- do not tell the user a trade will win because the ratio looks attractive
- do not replace thesis quality with a single numeric multiple
- do not ignore catalyst or event risk that can break the planned structure

## Usage examples

- "Use `risk-reward-sanity-check` on a long entry at 58.20, stop 55.90, target 65.50, thesis: breakout continuation if software leadership holds."
- "Use `risk-reward-sanity-check` for a short at 412.80 with stop 418.10 and two targets at 406.00 and 399.50 ahead of payrolls."
