# Portfolio Risk Review Framework

Use this framework to decide whether portfolio-level risk is acceptable before adding or maintaining more exposure.

## Core question

The question is not only:

- "What is my biggest position?"

The real questions are:

- Where are my exposures clustered?
- Which catalysts matter to the portfolio as a whole?
- Which positions are fragile right now?
- Is the current book aligned with my objective and timeframe?

## Typical routing

Start with:

- `portfolio-concentration`

Add as needed:

- `catalyst-map` when several positions share event risk
- `market-regime-analysis` when broad tape conditions matter
- `macro-event-analysis` when the macro calendar can pressure the whole book
- `position-management` when one or more live positions are under pressure

If the user still wants a new trade after the review:

- `pre-trade-check`

## Stop conditions

Stop when:

- concentration is already too high
- several positions share the same catalyst cluster
- the macro or regime backdrop makes the current book too fragile
- the portfolio snapshot is too incomplete to review honestly

## Wrapper discipline

The workflow should:

- surface the biggest risk sources fast
- separate portfolio-level risk from single-name conviction
- avoid pretending the portfolio is diversified when the drivers are the same
- return one clear next portfolio action

## Boundaries

This workflow does not perform full financial planning.

It only reviews current portfolio risk and what should happen next.
