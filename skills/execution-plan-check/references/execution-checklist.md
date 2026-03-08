# Execution Checklist

Use this checklist to decide whether a trade idea can be implemented cleanly in the real market.

## Core execution questions

- What exact order type is being used?
- Why does that order type fit this instrument and this session?
- How wide is the spread likely to be?
- How much displayed liquidity is actually available near the current quote?
- Is there an event, opening auction, closing auction, or extended-hours condition that changes the risk?
- If the stop triggers, what behavior should the user realistically expect?

## Order-type guidance

- `Market order`: highest execution certainty, weakest price control. Most dangerous in thin, volatile, or fast-moving conditions.
- `Limit order`: stronger price control, but no execution guarantee. Often better when price discipline matters more than immediacy.
- `Stop order`: becomes a market order when triggered. Useful for risk control, but the fill can be worse than the stop price.
- `Stop-limit order`: adds price control after the stop triggers, but raises the risk of no fill during a fast move.

## Liquidity and spread

Low apparent spread does not always mean low execution risk.

Check:

- whether the instrument itself trades actively
- whether the underlying assets are liquid, especially for ETFs and options
- whether the user's size is large relative to typical volume or displayed size
- whether the session is regular hours or extended hours

## Timing risk

Execution quality often degrades around:

- the market open
- the close
- earnings releases
- macro releases such as CPI, payrolls, or central-bank decisions
- headline-sensitive sessions
- pre-market or after-hours trading

Extended-hours trading often means:

- less liquidity
- wider spreads
- higher volatility
- more partial fills or no fills

## Stop realism

Stops help define risk, but they do not guarantee the exit level.

Common problems:

- stop too close to normal noise
- stop expected to behave like a guaranteed price
- stop placed into a catalyst window where gap risk dominates
- stop-limit used where no fill would be worse than slippage

## Boundaries

This checklist is about execution realism.

It does not decide:

- whether the thesis is valid
- whether the reward-to-risk is attractive
- whether the portfolio is too concentrated
- how much capital should be allocated
