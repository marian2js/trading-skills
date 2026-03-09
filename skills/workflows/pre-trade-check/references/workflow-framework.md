# Pre-Trade Workflow Framework

Use this framework to decide which checks a trade idea actually needs before entry.

## Core principle

Do not run a giant checklist blindly.

Run the smallest set of checks that can answer:

- Is the idea worth acting on?
- If not, what is the blocking issue?

## Typical routing

If the user starts with many names:

- `watchlist-review`
- `catalyst-map`

If the user has an interesting but underdeveloped idea:

- `evidence-gap-check`
- `thesis-validation`

If event or regime risk matters:

- `earnings-preview` or `macro-event-analysis`
- `market-regime-analysis`

If the user is already building the trade:

- `risk-reward-sanity-check`
- `execution-plan-check`
- `portfolio-concentration`
- `position-sizing`

## Stop conditions

Stop the workflow when:

- the evidence is too incomplete
- the thesis is too vague
- the structure is incoherent
- the order logic is not executable
- the portfolio is already too concentrated

## Wrapper discipline

The wrapper should:

- be explicit about which checks ran
- stop at the real blocker
- avoid fake certainty
- produce one clear next action

## Boundaries

This workflow does not place trades.

It only decides whether the idea deserves the next step.
