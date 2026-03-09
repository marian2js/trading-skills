# Post-Trade Debrief Framework

Use this framework to decide how far a trade review should go after a position is closed.

## Core question

The question is not only:

- "Did I make or lose money?"

The real questions are:

- What was the original plan?
- What actually happened?
- What is the clearest lesson?
- Is this lesson trade-specific or part of a larger pattern?

## Typical routing

Start with:

- `post-trade-review`

Add as needed:

- `journal-pattern-analyzer` when the same type of issue appears often enough to justify pattern review
- `risk-reward-sanity-check` when the original setup structure itself looks flawed
- `position-sizing` when the main issue was oversized risk

## Stop conditions

Stop when:

- the original plan cannot be reconstructed well enough for stronger claims
- the sample is too small for pattern analysis
- the clearest lesson is already specific and actionable at the single-trade level

## Wrapper discipline

The workflow should:

- start with reconstruction, not outcome
- separate single-trade learning from pattern learning
- return one clear process change
- avoid overstating what one trade proves

## Boundaries

This workflow does not reopen the trade.

It only decides what should be learned from it.
