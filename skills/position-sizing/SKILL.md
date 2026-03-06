---
name: position-sizing
description: Compute a conservative position size from account equity, risk budget, entry, stop, and trading friction so the user can inspect exposure before entering a trade.
---

# Position Sizing

Use this skill before entering a trade when you need a defensible size instead of a gut-feel size.

This skill will not:

- tell the user whether the trade thesis is good
- override liquidity, gap, or event-risk judgment with a formula
- turn an aggressive stop or oversized conviction into a safe trade

## Role

Act like a conservative risk manager. Survival comes before conviction.

## When to use it

Use it when the user has a trade idea and needs to know:

- how many shares, units, or contracts fit the risk budget
- how slippage, fees, or contract multipliers change the math
- whether the planned stop makes the size impractical
- whether the trade is arithmetically small enough before asking whether it is strategically worth taking

## Inputs and context

Ask for:

- account size or equity
- max risk as percent or cash amount
- entry price
- stop price
- instrument type if it affects contract value
- optional slippage, commission, or "extra buffer" assumptions

If any key input is missing, state what is missing and stop rather than invent it.

## Analysis process

1. Compute the per-unit risk from entry to stop.
2. Add user-provided friction assumptions if they materially increase realized risk.
3. Compute the maximum position size that stays inside the risk budget.
4. Report the rounded-down size, estimated total risk, and any caveats.
5. Flag cases where the stop is too tight, too wide, or structurally unclear.

Use [references/methodology.md](references/methodology.md) for sizing conventions and caveats. Use [assets/trade-plan-template.md](assets/trade-plan-template.md) when the user wants a reusable planning format.

For agents that support code execution, use [../_lib/calculations.py](../_lib/calculations.py) for fixed-fractional sizing, volatility-adjusted sizing, Kelly fraction context, and futures contract math.

## Output structure

Prefer this output order:

1. `Inputs Used`
2. `Sizing Method`
3. `Sizing Math`
4. `Position Recommendation`
5. `Risk Caveats`

Always include:

- position size
- total dollar risk
- percent of account at risk
- assumptions used
- caveats about slippage, gaps, leverage, or contract multipliers

Do not imply the size is "safe" just because it fits the arithmetic.

## Best practices

- do not promise that a mathematically valid size is strategically appropriate
- do not ignore contract multipliers or event risk when they materially change exposure
- do not replace the need for liquidation planning in fast or illiquid markets

## Usage examples

- "Use `position-sizing` for a $150,000 account risking 0.4% on a long entry at 84.20 with a stop at 81.90 and 0.10 slippage."
- "Use `position-sizing` on ES futures with account size $80,000, max loss $500, long entry 5210.25, and stop 5199.75."
