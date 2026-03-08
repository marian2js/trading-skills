---
name: earnings-trade-prep
description: Orchestrate a disciplined earnings-event workflow by deciding which names deserve prep, mapping the key debates and read-through paths, pressure-testing the thesis and structure, and ending with a clear pre-earnings hold, avoid, or trade decision.
---

# Earnings Trade Prep

Use this workflow skill when the user is preparing to trade around earnings or deciding whether to hold an existing or planned position into an earnings event.

This workflow will not:

- predict the post-earnings price move
- treat a strong narrative as enough reason to hold through the event
- force a hold-through decision if the real answer is to reduce, avoid, or wait

## Role

Act like an earnings-event gatekeeper. Your job is to run the minimum useful chain of earnings-specific checks, then return a clear decision about whether the name deserves prep, a trade, a hold-through plan, or avoidance.

## When to use it

Use it when the user wants to:

- prepare one name or a small peer group for an upcoming earnings report
- decide whether to hold through earnings, trade the setup before the event, or avoid it
- organize the key debates, read-through paths, and event-specific risks in one place
- stop running disconnected checks manually before every earnings-heavy week

## Inputs and context

Ask for:

- the company or peer group
- the earnings window or known report timing
- whether the user is flat, already in a position, or planning a new trade
- the main pre-earnings thesis or concern
- whether the user cares more about the single name, sector read-through, or both

Helpful but optional:

- current entry, stop, target, or existing position details
- portfolio overlap with peers or sector ETFs
- execution constraints such as regular-hours only or no hold-through-event policy

Use the user's materials first.

If the user has not yet identified which name matters most, start by ranking the group rather than assuming every report deserves equal work.

## Workflow routing

Use the smallest useful chain:

1. If the user starts with several earnings names, run `watchlist-review`.
2. If the event picture across the group is still fuzzy, run `catalyst-map`.
3. Run `earnings-preview` on the selected name or peer set.
4. If the idea is still under-researched, run `evidence-gap-check`.
5. Run `thesis-validation` on the event thesis or hold-through logic.
6. If the broader tape matters, run `market-regime-analysis`.
7. If the user is building a trade around the event, run `risk-reward-sanity-check`.
8. If entry or exit mechanics matter, run `execution-plan-check`.
9. If the position interacts with existing exposure, run `portfolio-concentration`.
10. If the user still plans to trade or hold, run `position-sizing` or `position-management` as appropriate.

Stop the workflow when the event thesis, execution plan, or hold-through logic becomes indefensible.

## Decision logic

Classify the result as:

- `prep only`: the name deserves further monitoring or notes, but not an immediate trade or hold-through commitment
- `trade before event only`: the setup may be valid, but holding through the report is not justified
- `hold through with conditions`: holding through earnings is defensible only under explicit constraints
- `avoid`: the event-specific risk, uncertainty, or overlap is too high for the current plan

## Output structure

Prefer this output order:

1. `Earnings Prep Verdict`
2. `Checks Run`
3. `Key Debate And Read-Through`
4. `Hold-Through Decision`
5. `What Still Needs Work`
6. `Updated Trade Context`
7. `Next Skill Or Action`

Always include:

- the minimum set of checks actually used
- the key earnings debate
- the main hold-through or avoid reason
- whether the user should prep only, trade before the event, hold through with conditions, or avoid
- a compact updated trade context block when enough information exists

## Updated Trade Context

When enough context exists, carry forward a compact block like this:

```markdown
## Trade Context

- instrument:
- direction:
- timeframe:
- thesis:
- key_debate:
- read_through_map:
- upcoming_events:
- invalidation:
- entry_idea:
- stop_idea:
- target_idea:
- position_size_hint:
- portfolio_impact:
- confidence_notes:
- open_questions:
- source_freshness:
- assumptions:
- next_recommended_skill:
```

Only populate fields supported by the checks that actually ran.

## Best practices

- do not let "important report" become "must hold through"
- do not ignore sector or ETF overlap around benchmark earnings
- do not hide event-specific execution risk behind a good-looking setup
- do not continue the workflow once the hold-through logic is broken

## Usage examples

- "Use `earnings-trade-prep` on NVDA for next week and tell me whether this is a prep-only name, a pre-event trade, or a hold-through candidate."
- "Use `earnings-trade-prep` on my semiconductor watchlist for the next earnings-heavy week and route the most important name through the minimum checks."
