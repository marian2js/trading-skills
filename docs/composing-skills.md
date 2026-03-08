# Composing Skills

These skills are designed to work well alone, but they become more useful when an agent carries forward a small amount of structured trade context from one skill to the next.

Use two layers deliberately:

- atomic skills: reusable capabilities such as `thesis-validation`, `execution-plan-check`, or `position-sizing`
- workflow skills: wrappers such as `pre-trade-check` that route the user through the smallest useful chain

## Recommended chaining order

Use the shortest chain that answers the user's actual problem.

Recommended default order:

1. `pre-trade-check` if the user wants one readiness verdict instead of manual routing
2. `watchlist-review` if the user starts with several names and needs triage first
3. `catalyst-map` if the user needs one ranked event map across several names or exposures
4. `evidence-gap-check` if the idea is promising but the missing information is not yet prioritized
5. `macro-event-analysis` or `earnings-preview` if event risk is part of the setup
6. `market-regime-analysis` to classify the broader environment
7. `thesis-validation` to test whether the claim is clear enough to act on
8. `risk-reward-sanity-check` to pressure-test the specific trade structure
9. `execution-plan-check` to confirm the order logic and stop behavior are operationally realistic
10. `portfolio-concentration` to confirm the portfolio can absorb the idea without hidden overlap
11. `position-sizing` once the structure, execution, concentration, and stop are clear
12. `position-management` while the trade is open
13. `post-trade-review` after the trade closes
14. `journal-pattern-analyzer` when enough completed trades exist to review a real sample

Practical rule:

- move from broad context to narrow decision
- cut the list before doing deep work on every name
- do not size first if event risk, thesis quality, or structure is still unclear
- do not size first if the order plan is not operationally realistic
- do not size first if the portfolio fit is still unclear
- once the trade is live, switch from construction questions to management questions
- do not review outcome before reconstructing the original plan

## Trade Context schema

When multiple skills need to share state, prefer a small markdown block like this:

```markdown
## Trade Context

- instrument: NVDA
- watchlist_focus: semis leadership names
- direction: long
- timeframe: swing
- thesis: AI demand stays strong and gross margins remain resilient
- invalidation: capex commentary softens and semis leadership breaks
- entry_idea: buy pullback near 118.50
- execution_notes: regular-hours only, limit order near support
- stop_idea: 112.90
- targets: 124.00, 129.50
- event_risk: NVDA earnings next Wednesday after the close
- regime_view: healthy trend, but narrow breadth
- portfolio_context: already own QQQ and SMH
- sizing_constraints: risk 0.50% of a $125,000 account
- open_questions:
  - Is the report worth holding through?
  - Does semis breadth still support the setup?
```

Keep it small. Only carry forward fields that the next skill actually needs.

## Workflow 1: Event-heavy swing trade

1. Run `watchlist-review` on the peer set to decide which names deserve active prep.
2. Run `catalyst-map` to rank the company, macro, and policy events that matter across the peer set.
3. Run `evidence-gap-check` if the user still has an interesting idea but incomplete preparation.
4. Run `earnings-preview` on the company and peer group.
5. Carry forward the event date, key debate, and read-through risk into `market-regime-analysis`.
6. Use `thesis-validation` to pressure-test the claim, timeframe, and invalidation logic.
7. Use `risk-reward-sanity-check` once the user commits to an entry, stop, and target.
8. Run `execution-plan-check` before sizing if the entry depends on breakouts, thin liquidity, or catalyst timing.
9. Run `portfolio-concentration` before sizing if the user already has related exposure.
10. Finish with `position-sizing` after the stop is stable.

Good handoff fields:

- event timing
- catalyst ranking
- blocking research gaps
- key debate
- main invalidation trigger
- thesis statement
- watchlist priority
- entry, stop, targets
- order logic
- existing related exposure
- account risk budget

## Workflow 2: Macro week portfolio defense

1. Run `macro-event-analysis` for the next 48 hours to two weeks.
2. Feed the event clustering and transmission channels into `market-regime-analysis`.
3. Use `thesis-validation` to test whether the tactical claim still holds under that backdrop.
4. If the user still wants to put on a tactical trade, run `risk-reward-sanity-check`.
5. Use `execution-plan-check` if the trade depends on open, close, or release-window execution.
6. Use `portfolio-concentration` if the trade overlaps existing sector, factor, or macro exposure.
7. Use `position-sizing` only after the event window and stop placement are explicit.

Good handoff fields:

- prioritized event slate
- transmission channels
- heavy or quiet backdrop
- thesis statement
- order timing
- related existing exposure
- timeframe for the intended trade

## Workflow 0: Too many names, not enough attention

1. Run `watchlist-review` on the current list.
2. Run `catalyst-map` on the reduced set if the user still needs one cross-name event map.
3. Use `evidence-gap-check` when a name is interesting but still under-researched.
4. Keep only the active-focus names.
5. Route those names into `earnings-preview`, `macro-event-analysis`, `market-regime-analysis`, or `thesis-validation` depending on what matters most.

Good handoff fields:

- active names
- why they matter now
- catalyst map
- missing evidence
- names to defer
- next recommended skill per active name

## Workflow -1: One-command readiness check

1. Run `pre-trade-check`.
2. Let it choose the minimum useful chain.
3. Stop at the first real blocker or continue until the trade is ready.

Good handoff fields:

- checks run
- blocking issue
- updated trade context
- next recommended skill or action

## Workflow 3: Closed trade learning loop

1. Carry the original plan into `post-trade-review`.
2. If the review identifies poor structure, run `risk-reward-sanity-check` on the original setup.
3. If the review identifies oversizing, use `position-sizing` to show what the size should have been.
4. If a batch of reviews now exists, run `journal-pattern-analyzer` across them.

Good handoff fields:

- original thesis
- planned and actual entry, stop, target, size
- rule violation summary
- one process change to test next time

## Workflow 5: Batch learning loop

1. Gather a journal sample or batch of closed trades.
2. Run `journal-pattern-analyzer` to find repeatable strengths and mistakes.
3. Feed the strongest mistake pattern back into future pre-trade and live-trade rules.

Good handoff fields:

- repeated mistake type
- repeated strength
- environment or setup cluster
- one or two process changes to test next

## Workflow 4: Open position under pressure

1. Carry the original plan and current status into `position-management`.
2. If a catalyst is near, supplement with `earnings-preview` or `macro-event-analysis`.
3. If the trade later closes, route the result into `post-trade-review`.

Good handoff fields:

- original thesis
- current price or PnL status
- current stop or trailing logic
- upcoming catalyst
- hold, trim, tighten risk, or exit decision
