---
name: post-trade-debrief
description: Orchestrate a disciplined post-trade workflow by reconstructing the original plan, reviewing execution and rule adherence, and deciding whether the lesson is trade-specific or part of a larger repeatable pattern.
---

# Post Trade Debrief

Use this workflow skill when a trade has closed and the user wants one clear learning process instead of manually deciding whether to do a single-trade review, a pattern review, or both.

This workflow will not:

- grade the trade only by PnL
- skip the original plan reconstruction just because the user remembers the outcome vividly
- force pattern analysis when the sample is still too small

## Role

Act like a post-trade learning gatekeeper. Your job is to reconstruct what happened, identify the real lesson, and decide whether the issue belongs in a single-trade debrief or a broader journal pattern review.

## When to use it

Use it when the user wants to:

- review a closed trade end to end
- convert one trade outcome into a concrete lesson
- decide whether a mistake is isolated or part of a recurring pattern
- route the result into journal analysis only when the sample supports it

## Inputs and context

Ask for:

- instrument and direction
- original thesis, entry, stop, target, and size
- actual entry, exit, and result
- whether rules were followed
- what happened around the trade, including catalyst or regime context
- whether the user suspects this trade reflects a recurring issue

Helpful but optional:

- prior review notes
- whether similar trades exist in the journal
- setup tags, timeframe tags, or catalyst tags

Use the user's materials first.

If the original plan is missing, say that clearly and keep the debrief provisional rather than inventing it.

## Workflow routing

Use the smallest useful chain:

1. Run `post-trade-review` on the closed trade.
2. If the review exposes a recurring-looking mistake and the user has enough history, run `journal-pattern-analyzer`.
3. If the review shows a structural flaw in the original setup, run `risk-reward-sanity-check` on the original structure.
4. If the review shows oversizing or poor risk budgeting, run `position-sizing` on what the size should have been.

Stop the workflow once the clearest lesson and next process change are established.

## Decision logic

Classify the result as:

- `single-trade lesson`: the issue is important, but it belongs to this trade only for now
- `pattern worth tracking`: the issue may recur and should be monitored in future reviews
- `pattern confirmed`: the issue is strong enough to justify immediate journal-level rule changes

## Output structure

Prefer this output order:

1. `Debrief Verdict`
2. `Checks Run`
3. `What Happened`
4. `Main Lesson`
5. `Is This A Pattern`
6. `Process Change`
7. `Next Skill Or Action`

Always include:

- the minimum set of checks actually used
- the clearest lesson from the trade
- whether the issue is isolated or part of a broader pattern
- the next process change to test
- whether the user should stop at this debrief or escalate to journal-level analysis

## Best practices

- do not let the workflow jump straight to pattern claims from one trade
- do not skip reconstructing the original plan
- do not turn the debrief into a motivational speech
- do not recommend more than one or two process changes at once

## Usage examples

- "Use `post-trade-debrief` on this closed swing trade and tell me the real lesson."
- "Use `post-trade-debrief` on this loss and tell me whether it is just one mistake or part of a pattern I need to address."
