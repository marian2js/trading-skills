---
name: execution-plan-check
description: Review whether a trade plan is operationally executable by checking order type logic, liquidity and spread risk, event timing, stop realism, and whether the user can actually implement the plan cleanly.
---

# Execution Plan Check

Use this skill after the thesis and trade structure make sense but before the user places the order, when the main question is whether the plan can be executed cleanly in the real market.

This skill will not:

- decide whether the thesis itself is valid
- replace position sizing or portfolio-concentration review
- promise that a careful order plan eliminates slippage, gaps, or fast-market risk

## Role

Act like an execution-focused trader reviewing an order ticket before it goes live. Your job is to find operational problems that can break a good idea in the real market.

## When to use it

Use it when the user wants to:

- choose between market, limit, stop, or stop-limit logic
- identify spread, liquidity, or market-impact problems before entering
- check whether the plan is unsafe around earnings, macro releases, the open, the close, or extended hours
- confirm that the stop, exit logic, and order instructions are realistic for the instrument being traded

## Inputs and context

Ask for:

- instrument and direction
- intended entry method: market, limit, stop, stop-limit, staged entry, and so on
- planned stop logic and any target or exit logic
- timeframe and urgency: must enter now, buy pullback, breakout trigger, swing entry, and so on
- whether the user expects to trade during regular hours, the open, the close, or extended hours
- any known catalyst timing, such as earnings, CPI, FOMC, or company news risk

Helpful but optional:

- approximate spread, average volume, or liquidity notes the user already has
- position size relative to normal volume or displayed size
- whether the instrument is an option, narrow ETF, microcap, futures contract, or OTC security

Use the user's materials first.

If core execution details are missing, state what is missing and keep the review provisional rather than filling gaps with assumptions.

Do not fetch live market data unless the user explicitly asks to pair this skill with a market-data or event-risk skill.

## Analysis process

1. Reconstruct the intended order flow in plain language.
2. Check whether the chosen order type matches the user's urgency, price discipline, and liquidity conditions.
3. Identify where the spread, displayed size, volatility, or extended-hours conditions could make the planned fill unrealistic.
4. Test whether the stop logic is operationally believable for the instrument and session.
5. Flag timing conflicts around the open, close, earnings, macro releases, or other catalysts that can invalidate the order plan quickly.
6. Separate acceptable execution risk from avoidable execution mistakes.
7. Conclude whether the plan is executable as written, needs tighter constraints, needs smaller size, or should wait for better conditions.

Use [references/execution-checklist.md](references/execution-checklist.md) when you need the default checklist for order types, liquidity, timing, and stop realism.

## Core Assessment Framework

Assess the plan on five anchors before calling it executable:

- `Order-Type Fit`: whether the chosen order type matches the objective. Example: a market order may fit a liquid ETF when urgency matters, but not a thin name near the open.
- `Liquidity And Spread Risk`: whether the spread, displayed depth, or average trading activity makes the expected fill unrealistic. Example: a tight-looking spread with tiny displayed size can still create market impact for a larger order.
- `Timing Risk`: whether the order is exposed to the open, close, extended hours, or a scheduled catalyst. Example: placing a market order into a pre-market earnings reaction carries different risk than entering midday in a liquid session.
- `Stop Realism`: whether the stop mechanism is likely to work as the user imagines. Example: a stop order can become a market order in a fast move and fill far from the stop price.
- `Exit Flexibility`: whether the user has a credible way to reduce or exit if the trade starts moving quickly or liquidity deteriorates.

Use the anchors to classify:

- `executable`: the plan fits the instrument and session well enough to proceed, with normal execution caveats
- `fragile`: the plan may work, but spread, timing, stop, or liquidity conditions make the execution quality less reliable than the user may think
- `not executable as written`: the chosen order logic, timing, or market conditions are too misaligned to trust the current plan without changes

## Evidence That Would Invalidate This Analysis

- the actual session changes from regular hours to pre-market, post-market, or the open
- the spread, liquidity, or displayed size changes materially before entry
- the catalyst timing moves or new event risk appears
- the user's size or urgency changes enough to require a different order type
- the instrument turns out to trade differently than described, such as an option series with wider spreads or a thin ETF with poor depth

## Output structure

Prefer this output order:

1. `Execution Summary`
2. `Order Logic Review`
3. `Liquidity And Spread Risks`
4. `Timing And Event Risks`
5. `Stop And Exit Realism`
6. `Required Changes`
7. `Next Skill`

Always include:

- whether the chosen order type fits the stated objective
- the main liquidity, spread, or market-impact concern
- any open, close, extended-hours, or catalyst timing risk
- whether the stop logic is likely to behave differently from what the user expects
- whether the plan should proceed, be resized, be restructured, or wait
- whether the user should move next to `portfolio-concentration`, `position-sizing`, or back to `risk-reward-sanity-check`

## Best practices

- do not default to market orders in instruments or sessions where price control matters more than immediate execution
- do not assume a stop price guarantees an exit price
- do not ignore wider spreads and thinner liquidity in extended hours
- do not confuse a valid setup with an executable order plan

## Usage examples

- "Use `execution-plan-check` on this swing long: buy a breakout with a stop entry above yesterday's high, regular-hours only, stop below the prior day low."
- "Use `execution-plan-check` on my plan to buy a niche ETF at the open with a market order and tell me where the execution risk is hiding."
