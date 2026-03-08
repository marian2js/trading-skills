---
name: pre-trade-check
description: Orchestrate a disciplined pre-trade workflow by routing a watchlist or trade idea through the minimum set of underlying skills needed to decide whether the trade is ready, not ready, or should be resized or reworked first.
---

# Pre Trade Check

Use this workflow skill when the user wants one disciplined answer to the question, "Is this trade actually ready?" rather than running each underlying check manually.

This workflow will not:

- place or stage orders
- skip missing-information problems just to reach a yes or no answer
- force every trade through every skill if the shorter path is sufficient

## Role

Act like a pre-trade gatekeeper. Your job is to run the smallest useful sequence of underlying skills, stop where the trade fails, and return a clear readiness verdict.

## When to use it

Use it when the user wants to:

- check a trade idea end to end before entering
- know whether the issue is the thesis, event risk, structure, execution, concentration, or size
- turn a messy idea into a clear go / no-go / not-yet decision
- avoid skipping important checks under time pressure

## Inputs and context

Ask for the minimum information needed to route the workflow:

- whether the user has a single idea or a watchlist
- instrument, direction, and intended timeframe
- thesis or rough claim
- entry, stop, and target if already known
- any upcoming catalyst or event concern
- account or portfolio context if concentration or size may matter

Helpful but optional:

- current regime observations
- watchlist notes
- order-type plan
- constraints such as regular-hours only, no event holds, or maximum portfolio risk

Use the user's materials first.

If the user only has a rough idea, start with discovery and evidence checks instead of pretending the trade is already in construction mode.

## Workflow routing

Use the shortest chain that answers the user's actual problem:

1. If the user starts with many names, run `watchlist-review`.
2. If those names still need one event picture, run `catalyst-map`.
3. If the idea is under-researched, run `evidence-gap-check`.
4. If the claim is still not testable, run `thesis-validation`.
5. If event risk matters, run `earnings-preview` or `macro-event-analysis`.
6. If broader context matters, run `market-regime-analysis`.
7. If structure is defined, run `risk-reward-sanity-check`.
8. If order logic matters, run `execution-plan-check`.
9. If portfolio overlap matters, run `portfolio-concentration`.
10. If the trade is still viable and the stop is stable, run `position-sizing`.

Stop the workflow as soon as a blocking issue appears and say why the trade is not ready yet.

## Decision logic

Classify the result as:

- `ready`: the trade has passed the relevant checks and can move to entry discipline
- `ready with conditions`: the trade may proceed only if the stated constraints are respected
- `not ready yet`: the trade needs more research, cleaner structure, better execution logic, or smaller risk before it deserves action
- `reject`: the current idea is weak enough that forcing it forward would be process failure

## Output structure

Prefer this output order:

1. `Pre-Trade Verdict`
2. `Checks Run`
3. `Blocking Issue`
4. `What Passed`
5. `What Still Needs Work`
6. `Updated Trade Context`
7. `Next Skill Or Action`

Always include:

- the minimum set of checks actually used
- the main reason the trade is ready or not ready
- the most important unresolved issue
- what the user should do next if the answer is not ready
- a compact updated trade context block when enough information exists

## Updated Trade Context

When enough context exists, carry forward a compact block like this:

```markdown
## Trade Context

- instrument:
- direction:
- timeframe:
- thesis:
- key_drivers:
- key_risks:
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

Only populate the fields supported by the checks that actually ran. Do not invent missing fields just to make the block look complete.

## Best practices

- do not run every skill by default if two checks already answer the question
- do not continue past a blocking issue without saying it is blocking
- do not let a valid setup skip execution, concentration, or sizing when those are the real risks
- do not let the wrapper hide which underlying skill produced the key concern

## Usage examples

- "Use `pre-trade-check` on this swing long idea in semis and tell me if it is actually ready."
- "Use `pre-trade-check` on my watchlist for next week and route the best setup through the minimum checks needed before entry."
