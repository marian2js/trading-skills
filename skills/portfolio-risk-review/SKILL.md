---
name: portfolio-risk-review
description: Orchestrate a whole-book risk review by checking concentration, correlated exposure, catalyst clustering, market-context sensitivity, and live-position fragility before the user adds, holds, or reduces portfolio risk.
---

# Portfolio Risk Review

Use this workflow skill when the user wants a portfolio-level answer to the question, "Where is my real risk right now?" rather than a single-position analysis.

This workflow will not:

- build a long-term strategic financial plan
- replace tax, legal, or retirement-planning advice
- assume a portfolio is safe just because no single holding looks extreme in isolation

## Role

Act like a portfolio risk reviewer. Your job is to identify where the book is actually exposed, which risks are clustered, and what needs attention before the user adds, holds, or reduces risk.

## When to use it

Use it when the user wants to:

- review portfolio risk before adding a new position
- understand where concentration or overlap is hiding
- assess whether upcoming catalysts create too much clustered exposure
- know whether the current book needs trimming, hedging, smaller adds, or closer monitoring

## Inputs and context

Ask for:

- the portfolio or account snapshot, including approximate weights or position sizes
- whether the snapshot is the full portfolio, one account, or only the active risk sleeve
- any planned new add or reduction
- upcoming catalysts the user already knows about
- whether the focus is tactical trading capital, swing capital, or longer-term investing capital

Helpful but optional:

- sector, theme, or factor tags
- current regime view or macro concern
- which positions are already under pressure or near key catalysts
- any known liquidity or execution constraints

Use the user's materials first.

If the snapshot is partial, say so clearly and keep the result provisional.

## Workflow routing

Use the smallest useful chain:

1. Run `portfolio-concentration` to identify direct and indirect concentration.
2. If catalyst clustering matters, run `catalyst-map`.
3. If broad market context matters, run `market-regime-analysis`.
4. If a major macro calendar is relevant to the portfolio, run `macro-event-analysis`.
5. If one or more open positions are under pressure, run `position-management` on the critical positions.
6. If the user is considering a new add, run `pre-trade-check` or the specific construction skills only after the portfolio-level risk picture is clear.

Stop the workflow when the book is already too concentrated or too catalyst-heavy for the user's stated objective.

## Decision logic

Classify the result as:

- `portfolio risk acceptable`: the book appears aligned with the user's objective and no immediate portfolio-level change is necessary
- `portfolio risk elevated`: the book is still manageable, but concentration, overlap, or catalyst clustering needs active monitoring or smaller adds
- `portfolio risk too high`: the book is too dependent on a limited set of exposures, events, or fragile positions to justify adding risk without changes

## Output structure

Prefer this output order:

1. `Portfolio Risk Verdict`
2. `Checks Run`
3. `Main Risk Sources`
4. `Catalyst And Regime Pressure`
5. `What To Reduce, Watch, Or Avoid Adding`
6. `Updated Portfolio Context`
7. `Next Skill Or Action`

Always include:

- whether the snapshot was full or partial
- the main risk sources in the current book
- where exposures overlap or cluster
- whether upcoming catalysts or macro conditions increase portfolio fragility
- whether the right action is hold, trim, avoid adding, or review specific positions more closely
- a compact updated portfolio context block when enough information exists

## Updated Portfolio Context

When enough context exists, carry forward a compact block like this:

```markdown
## Portfolio Context

- objective:
- snapshot_scope:
- top_exposures:
- overlap_clusters:
- key_catalysts:
- regime_pressure:
- fragile_positions:
- planned_add:
- portfolio_constraints:
- risk_summary:
- open_questions:
- assumptions:
- next_recommended_skill:
```

Only populate the fields supported by the checks that actually ran.

## Best practices

- do not treat issuer count as diversification by itself
- do not ignore shared catalyst risk across several names
- do not review a partial snapshot as if it were the whole book
- do not continue into a new trade workflow before the portfolio-level blocker is explicit

## Usage examples

- "Use `portfolio-risk-review` on my current book before I add more semis."
- "Use `portfolio-risk-review` on this account for the next two weeks and tell me where the real risk is concentrated."
