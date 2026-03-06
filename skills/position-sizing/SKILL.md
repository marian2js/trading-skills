---
name: position-sizing
description: Compute a conservative position size from account equity, risk budget, entry, stop, and trading friction so the user can inspect exposure before entering a trade.
---

# Position Sizing

Use this skill before entering a trade when you need a defensible position size instead of a gut-feel size.

It can be run manually or with [scripts/calculate_position_size.py](scripts/calculate_position_size.py) when a structured calculation is useful.

Focus on survival first:

- calculate max loss per trade from account size and risk budget
- convert that risk into units, shares, or contracts from entry and stop distance
- reduce size further if slippage, spreads, or gap risk are material

## Inputs

Ask for:

- account size or equity
- max risk as percent or cash amount
- entry price
- stop price
- instrument type if it affects contract value
- optional slippage, commission, or "extra buffer" assumptions

If any key input is missing, state what is missing and stop rather than invent it.

## Workflow

1. Compute the per-unit risk from entry to stop.
2. Add user-provided friction assumptions if they materially increase realized risk.
3. Compute the maximum position size that stays inside the risk budget.
4. Report the rounded-down size, estimated total risk, and any caveats.
5. Flag cases where the stop is too tight, too wide, or structurally unclear.

Use the worksheet in [assets/trade-plan-template.md](assets/trade-plan-template.md) when the user wants a reusable planning format. See [references/methodology.md](references/methodology.md) for sizing conventions and caveats.

## What it returns

Always include:

- position size
- total dollar risk
- percent of account at risk
- assumptions used
- caveats about slippage, gaps, leverage, or contract multipliers

Do not imply the size is "safe" just because it fits the arithmetic.

## What this skill will not do

- promise that a mathematically valid size is appropriate for the setup
- ignore contract multipliers or event risk when they materially change exposure
- replace the need for liquidation planning in fast or illiquid markets

## Usage examples

- "Use `position-sizing` for a $150,000 account risking 0.4% on a long entry at 84.20 with a stop at 81.90 and 0.10 slippage."
- "Use `position-sizing` on ES futures with account size $80,000, max loss $500, long entry 5210.25, and stop 5199.75."
