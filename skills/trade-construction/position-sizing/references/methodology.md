# Position Sizing Methodology

## Base formula

The conservative core formula is:

`position size = allowed trade risk / per-unit realized risk`

Where:

- allowed trade risk is either a cash number or a percentage of equity converted to cash
- per-unit realized risk is not just entry minus stop if trading friction is meaningful

## Friction matters

When it is realistic, add:

- expected slippage on entry and exit
- spread cost for illiquid instruments
- commission if it is large relative to the stop distance
- a gap-risk buffer when the stop may not fill at the intended level

## Practical cautions

- Tight stops can create oversized positions that are fragile in real execution.
- Wide stops can produce tiny positions that may not justify the trade.
- Futures and options require multiplier awareness. Do not reuse equity math blindly.
- A mathematically valid size can still be inappropriate if event risk is elevated.
