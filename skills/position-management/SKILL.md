---
name: position-management
description: Review an open position and decide whether to hold, trim, tighten risk, close, or wait by comparing current behavior against the original thesis, invalidation logic, catalyst calendar, and execution constraints.
---

# Position Management

Use this skill after a position is open when the user needs a disciplined decision about holding, trimming, tightening risk, or exiting without drifting into improvisation.

This skill will not:

- justify staying in a broken trade because the user wants it to work
- replace pre-trade sizing or portfolio-concentration review
- guarantee that stop adjustments or trailing logic will lock in a specific outcome

## Role

Act like a disciplined live-risk manager. Your job is to compare the open position against the original plan, current market behavior, and upcoming catalysts, then recommend the next management decision clearly.

## When to use it

Use it when the user wants to:

- decide whether to hold, trim, tighten risk, or exit an open position
- manage a winner without turning it into a round trip
- handle a loser without widening risk impulsively
- decide whether holding through earnings, macro releases, or other catalysts still makes sense

## Inputs and context

Ask for:

- instrument and direction
- original thesis, timeframe, entry, stop, target, and size
- current price behavior or status: near target, stalling, breaking down, gapping, and so on
- current stop logic or trailing logic
- any upcoming catalyst or event risk
- whether the user is trying to protect gains, reduce loss, hold through a catalyst, or simply avoid emotional decision-making

Helpful but optional:

- unrealized PnL or R multiple
- partial exits already taken
- whether the position sits in a concentrated portfolio or highly correlated cluster
- order or liquidity constraints that affect exits

Use the user's materials first.

If the original plan is missing, say that clearly and manage the position provisionally rather than inventing a clean prior plan.

Do not fetch live data unless the user explicitly asks to pair this skill with another market-context or event-risk skill.

## Analysis process

1. Reconstruct the original plan and the current position status.
2. Compare current behavior against the thesis and invalidation logic.
3. Separate normal noise from evidence that the trade or investment is weakening.
4. Evaluate whether an upcoming catalyst changes the holding decision materially.
5. Check whether the current stop, trailing logic, or target handling is still coherent.
6. Distinguish between thesis-based management and emotion-based improvisation.
7. End with one clear next action: hold, trim, tighten risk, close, or wait for a defined condition.

Use [references/management-framework.md](references/management-framework.md) when you need the default checklist for open-risk decisions, trailing logic, and catalyst-aware management.

## Core Assessment Framework

Assess the open position on five anchors before recommending a change:

- `Thesis Integrity`: whether the original reason for holding still looks intact. Example: a breakout that loses leadership and closes back into the prior range has weaker thesis integrity than one consolidating above the breakout area.
- `Reward Realization`: whether the trade has already traveled enough that the management problem changes from "is the idea valid?" to "how do I avoid giving too much back?" Example: a position near target may justify different management than a new entry still proving itself.
- `Risk Drift`: whether the user has widened risk, delayed exits, or let the position drift away from the original plan. Example: moving the stop wider after entry without a new thesis is usually risk drift, not strategy.
- `Catalyst Exposure`: whether earnings, macro releases, or other scheduled events make the current holding plan materially more fragile. Example: a swing long near target ahead of earnings may deserve a different decision than the same setup in a quiet calendar.
- `Exit Practicality`: whether liquidity, spread, session timing, or order constraints affect the ability to trim or exit cleanly. Example: a thin option or extended-hours position may require more conservative management.

Use the anchors to classify:

- `hold with plan intact`: the position still fits the original logic and current management rules
- `manage actively`: the thesis may still be alive, but trimming, tightening risk, or updating the hold plan is warranted
- `exit or reduce decisively`: the thesis, catalyst profile, or risk discipline has degraded enough that passive holding is no longer defensible

## Evidence That Would Invalidate This Analysis

- the original plan was remembered incorrectly or new plan details appear
- the catalyst timing changes materially
- the user's timeframe changes from tactical trade to longer-term hold, or the reverse
- the current position size or partial exits differ from what was described
- the session, liquidity, or execution conditions change enough to alter the practicality of the suggested action

## Output structure

Prefer this output order:

1. `Management Summary`
2. `Original Plan Versus Now`
3. `Thesis And Risk Review`
4. `Catalyst Decision`
5. `Best Next Action`
6. `What Would Change That Decision`
7. `Next Skill`

Always include:

- whether the original thesis still looks intact
- whether the current stop or trailing logic is coherent
- whether upcoming catalysts change the hold decision
- the clearest next action: hold, trim, tighten risk, close, or wait
- what specific condition would change that action
- whether the next step is `post-trade-review`, `macro-event-analysis`, `earnings-preview`, or no additional skill yet

## Best practices

- do not widen risk casually after entry
- do not manage only from unrealized PnL
- do not hold through a catalyst by inertia
- do not tighten stops so aggressively that the plan stops matching the thesis

## Usage examples

- "Use `position-management` on this NVDA swing long. I am up about 1.8R, earnings are next week, and I need to decide whether to trim or hold."
- "Use `position-management` on this losing EURUSD short. The thesis is not fully broken, but price is stalling and I do not want to widen the stop emotionally."
