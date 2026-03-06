---
name: risk-reward-sanity-check
version: 0.1.0
description: Evaluate whether a proposed entry, stop, and target structure is coherent, asymmetric enough, and vulnerable to common failure modes before the trade is placed.
dependency_class: static
tags: risk-management, trade-structure, pre-trade
---

# Risk Reward Sanity Check

Use this skill when a trade idea exists but you want to inspect whether the structure makes sense before committing capital.

This skill does not predict whether the trade will work. It checks whether the plan is internally coherent.

## Inputs

Ask for:

- direction
- entry
- stop
- one or more targets
- thesis in one or two sentences
- optional context such as time horizon, catalyst, or nearby event risk

## Workflow

1. Calculate distance from entry to stop and from entry to target.
2. Express the raw risk-reward ratio.
3. Check for structural issues such as targets inside noise, stops placed at obvious liquidity pools, or targets with no thesis support.
4. Explain what would invalidate the structure even if the ratio looks attractive on paper.
5. Separate "good ratio" from "good trade." They are not the same thing.

See [references/failure-modes.md](references/failure-modes.md) for the default checklist.

## Output requirements

Always include:

- raw risk-reward math
- the main structural concern
- what would need to be true for the target to be plausible
- any mismatch between thesis, stop, and holding period

## Usage examples

- "Use `risk-reward-sanity-check` on a long entry at 58.20, stop 55.90, target 65.50, thesis: breakout continuation if software leadership holds."
- "Use `risk-reward-sanity-check` for a short at 412.80 with stop 418.10 and two targets at 406.00 and 399.50 ahead of payrolls."
