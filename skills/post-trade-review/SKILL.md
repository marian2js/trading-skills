---
name: post-trade-review
version: 0.1.0
description: Run a structured post-trade review covering thesis quality, execution, rule adherence, mistakes, and lessons so the user can improve process without hindsight theater.
dependency_class: static
tags: review, journaling, discipline
---

# Post Trade Review

Use this skill after a trade closes or after a meaningful trade sequence when you want an honest process review.

The objective is to improve repeatability, not to rewrite history.

## Inputs

Ask for:

- instrument and direction
- original thesis
- planned entry, stop, target, and size
- actual entry, exit, and size
- whether rules were followed
- what happened around the trade
- lesson the user currently believes they learned

## Workflow

1. Reconstruct the original plan before judging the outcome.
2. Separate thesis quality from execution quality.
3. Identify rule adherence or violations.
4. Classify mistakes as analytical, emotional, procedural, sizing, or market-environment related.
5. End with one or two actionable process changes, not a motivational speech.

Use [references/review-rubric.md](references/review-rubric.md) for the default rubric.

## Output requirements

Always include:

- original thesis summary
- what was done as planned
- what was not done as planned
- biggest mistake or best process decision
- one concrete lesson to carry forward

## Usage examples

- "Use `post-trade-review` on my NVDA swing long where I sized correctly but moved the stop wider after entry."
- "Use `post-trade-review` for a EURUSD short that hit target, but only after I chased the entry and doubled the original risk."
