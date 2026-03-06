# Composing Skills

These skills are designed to work well alone, but they become more useful when an agent carries forward a small amount of structured trade context from one skill to the next.

## Recommended chaining order

Use the shortest chain that answers the user's actual problem.

Recommended default order:

1. `macro-event-analysis` or `earnings-preview` if event risk is part of the setup
2. `market-regime-analysis` to classify the broader environment
3. `risk-reward-sanity-check` to pressure-test the specific trade structure
4. `position-sizing` once the structure and stop are clear
5. `post-trade-review` after the trade closes

Practical rule:

- move from broad context to narrow decision
- do not size first if event risk or structure is still unclear
- do not review outcome before reconstructing the original plan

## Trade Context schema

When multiple skills need to share state, prefer a small markdown block like this:

```markdown
## Trade Context

- instrument: NVDA
- direction: long
- timeframe: swing
- thesis: AI demand stays strong and gross margins remain resilient
- entry_idea: buy pullback near 118.50
- stop_idea: 112.90
- targets: 124.00, 129.50
- event_risk: NVDA earnings next Wednesday after the close
- regime_view: healthy trend, but narrow breadth
- sizing_constraints: risk 0.50% of a $125,000 account
- open_questions:
  - Is the report worth holding through?
  - Does semis breadth still support the setup?
```

Keep it small. Only carry forward fields that the next skill actually needs.

## Workflow 1: Event-heavy swing trade

1. Run `earnings-preview` on the company and peer group.
2. Carry forward the event date, key debate, and read-through risk into `market-regime-analysis`.
3. Use `risk-reward-sanity-check` once the user commits to an entry, stop, and target.
4. Finish with `position-sizing` after the stop is stable.

Good handoff fields:

- event timing
- key debate
- main invalidation trigger
- entry, stop, targets
- account risk budget

## Workflow 2: Macro week portfolio defense

1. Run `macro-event-analysis` for the next 48 hours to two weeks.
2. Feed the event clustering and transmission channels into `market-regime-analysis`.
3. If the user still wants to put on a tactical trade, run `risk-reward-sanity-check`.
4. Use `position-sizing` only after the event window and stop placement are explicit.

Good handoff fields:

- prioritized event slate
- transmission channels
- heavy or quiet backdrop
- timeframe for the intended trade

## Workflow 3: Closed trade learning loop

1. Carry the original plan into `post-trade-review`.
2. If the review identifies poor structure, run `risk-reward-sanity-check` on the original setup.
3. If the review identifies oversizing, use `position-sizing` to show what the size should have been.

Good handoff fields:

- original thesis
- planned and actual entry, stop, target, size
- rule violation summary
- one process change to test next time
