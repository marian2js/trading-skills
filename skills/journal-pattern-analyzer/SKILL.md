---
name: journal-pattern-analyzer
description: Analyze a trade journal or trade log to find repeated strengths, mistakes, environment-dependent patterns, and process changes that could improve future decisions without turning the review into hindsight theater.
---

# Journal Pattern Analyzer

Use this skill when the user has a set of trades, journal notes, or review entries and wants to know what patterns are repeating across them.

This skill will not:

- grade the user only by total PnL
- pretend a small sample proves a durable edge
- replace single-trade post-mortems when the problem is still one specific position

## Role

Act like a process analyst reviewing a journal, not a cheerleader reviewing outcomes. Your job is to identify repeatable strengths, repeatable mistakes, and where the user's process breaks down under specific conditions.

## When to use it

Use it when the user wants to:

- review a batch of trades instead of one trade
- identify recurring mistakes in entries, exits, sizing, timing, or catalyst handling
- see whether performance changes by setup, regime, instrument, or time horizon
- convert raw journal notes into one or two high-value process changes

## Inputs and context

Ask for:

- a trade log, journal entries, or a summarized set of closed trades
- the sample window: last 10 trades, last month, last quarter, earnings season, and so on
- what fields exist: setup type, thesis, entry, stop, target, size, result, notes, adherence, catalyst context
- whether the user wants to focus on behavioral patterns, setup quality, sizing quality, or environment fit

Helpful but optional:

- regime notes
- sector or instrument tags
- whether results are in dollars, percentages, or R multiples
- any pattern the user already suspects

Use the user's materials first.

If the sample is very small, say so clearly and keep the conclusions provisional.

For agents that support code execution, use [../_lib/calculations.py](../_lib/calculations.py) for trade-statistic summaries, expectancy, and win/loss distribution checks when the user provides structured results.

## Analysis process

1. Reconstruct the journal sample and what the user is trying to learn.
2. Group trades by setup, environment, mistake type, instrument, or catalyst context when the data supports it.
3. Separate outcome patterns from process patterns.
4. Identify recurring strengths and recurring mistakes.
5. Check whether the user's mistakes cluster around specific conditions such as open entries, event holds, oversizing, or late exits.
6. Distill the findings into one or two process changes that are specific enough to test.
7. End with what the user should keep doing, stop doing, and monitor next.

Use [references/pattern-framework.md](references/pattern-framework.md) when you need the default checklist for journal quality, sample interpretation, and repeatable mistake detection.

## Core Assessment Framework

Assess the journal on five anchors before drawing conclusions:

- `Sample Quality`: whether there are enough trades and enough detail to support pattern claims. Example: 20 tagged trades with notes is more informative than 4 trades with only PnL.
- `Process Consistency`: whether the user actually followed a recognizable process. Example: repeated pre-trade planning and post-trade notes make the patterns easier to trust.
- `Mistake Recurrence`: whether the same type of error appears multiple times. Example: widening stops after entry in several trades is a stronger signal than one isolated lapse.
- `Environment Fit`: whether results change across regimes, catalysts, timeframes, or instruments. Example: momentum setups may work in healthy trend conditions but degrade around heavy event risk.
- `Actionability`: whether the output can be turned into a specific rule, checklist item, or monitoring metric. Example: "do not enter breakouts in the first 15 minutes" is more actionable than "be more patient."

Use the anchors to classify:

- `useful pattern set`: the journal is detailed enough to support actionable conclusions
- `suggestive but thin`: there may be a pattern, but the sample or tagging quality is too weak for strong claims
- `not analyzable yet`: the notes are too sparse or the sample is too small to draw meaningful process conclusions

## Evidence That Would Invalidate This Analysis

- the sample is incomplete or selectively chosen
- key fields such as setup type, adherence, or notes were missing or mis-tagged
- the results mix different strategies or timeframes that should not have been analyzed together
- later entries show that the apparent pattern was only a short-lived cluster
- the user changes process materially, making the historical pattern less relevant

## Output structure

Prefer this output order:

1. `Pattern Summary`
2. `What Is Working`
3. `What Keeps Going Wrong`
4. `Where The Pattern Appears`
5. `Process Change To Test`
6. `What To Track Next`
7. `Next Skill`

Always include:

- whether the sample is strong enough for conclusions
- the clearest repeated strength
- the clearest repeated mistake
- where the pattern clusters: setup, timeframe, catalyst, instrument, or regime
- one or two process changes to test next
- whether the next step is `post-trade-review`, a revised rule in the journal, or no additional skill yet

## Best practices

- do not confuse outcome streaks with process quality
- do not draw strong conclusions from tiny samples
- do not hide repeated discipline failures behind a positive net PnL
- do not recommend more than one or two process changes at once

## Usage examples

- "Use `journal-pattern-analyzer` on my last 25 swing trades and tell me what mistake keeps repeating."
- "Use `journal-pattern-analyzer` on my trade journal from earnings season and show me whether event holds improved or hurt my process."
