---
name: market-regime-analysis
description: Analyze current market context through trend, volatility, breadth, and event backdrop so the user can choose tactics that fit the environment without relying on black-box regime claims.
---

# Market Regime Analysis

Use this skill when you need a disciplined read on market context before selecting tactics, sizing, or holding period.

This skill will not:

- forecast market returns from a label
- assign fake confidence percentages to limited evidence
- replace instrument-specific trade planning or risk limits

## Role

Act like a market structure analyst. Your job is to classify the environment conservatively, explain the evidence, and highlight what would invalidate that view.

## When to use it

Use it when the user wants to:

- decide whether trend-following, mean reversion, or caution is the better default
- understand whether a market is healthy, fragile, defensive, or in transition
- adapt size and expectations to changing breadth or volatility
- pressure-test a market read before committing capital

## Inputs and context

Ask for observations about:

- trend
- volatility
- breadth or participation
- leadership quality or concentration
- liquidity and event backdrop
- relevant timeframe and market focus

If the user is vague, ask for the minimum evidence needed instead of forcing a fake label.

Use the user's materials first: market notes, watchlists, screenshots, chart observations, breadth notes, or any provider details already mentioned in the conversation.

## If critical data is missing

If the user already supplied enough evidence to classify the environment, do not fetch anything.

If trend, volatility, breadth, or event context is still too thin:

- check whether the user already named a supported provider or already shared usable access details
- if they already indicated `FMP`, `TradingEconomics`, or `Polygon`, use [references/providers/fmp.md](references/providers/fmp.md), [references/providers/tradingeconomics.md](references/providers/tradingeconomics.md), or [references/providers/polygon.md](references/providers/polygon.md) directly
- otherwise consult [references/data-providers.md](references/data-providers.md) and ask which supported provider they want to use
- once the missing context is gathered, continue the regime analysis and disclose the source used

## Analysis process

1. Assess trend, volatility, breadth, and event backdrop separately.
2. Look for agreement or conflict across those dimensions.
3. Classify the environment conservatively.
4. Explain which tactics fit the environment and which become fragile.
5. State what evidence would change the classification.

Use [references/regime-framework.md](references/regime-framework.md) if you need the default label set and interpretation guidance.

## Core Assessment Framework

Score the environment on four anchors before choosing a label:

- `Trend`: higher highs and higher lows on the user's timeframe, or repeated failure at support and resistance. Example: 20-day trend up but 5-day momentum flattening means the trend anchor is positive but weakening.
- `Volatility`: realized range and gap behavior relative to the recent norm. Example: daily ranges expanding from 1.1% to 2.0% means tactics should become more defensive even if price is still trending.
- `Breadth`: participation across sectors, index members, or the user's watchlist. Example: index up while only megacap tech participates counts as narrow breadth, not healthy breadth.
- `Event Backdrop`: whether macro releases, earnings clusters, or policy headlines can invalidate the read quickly. Example: CPI tomorrow and a central-bank speaker today should push the backdrop toward heavy even if tape action is calm.

Use these anchors to classify:

- `healthy trend`: trend positive, volatility contained or normal, breadth broad enough, event backdrop not immediately disruptive
- `fragile trend`: trend positive, but breadth narrow or volatility elevated
- `transition`: anchors conflict meaningfully and no single tactic deserves high conviction
- `defensive`: trend negative or unstable, volatility elevated, breadth weak, or event backdrop heavy enough to shrink decision time

## Evidence That Would Invalidate This Analysis

- the next session or two reverses the trend anchor with a decisive break of the key level the analysis relied on
- breadth expands or collapses enough to contradict the current participation read
- volatility contracts or explodes enough to make the current tactic set inappropriate
- a new macro or earnings event changes the backdrop from manageable to heavy, or the reverse
- the user's timeframe changes materially, because intraday and swing regime reads should not be treated as interchangeable

## Output structure

Prefer this output order:

1. `Regime Summary`
2. `Core Assessment Framework`
3. `Tactical Implications`
4. `Evidence That Would Invalidate This Analysis`
5. `Caveats`

Always include:

- regime classification in plain language
- key evidence used
- what weakens or invalidates the current read
- tactical implications for risk-taking, trade duration, and expectation-setting

Avoid fake certainty or theatrical confidence percentages.

## Best practices

- do not forecast returns from a single regime label
- do not turn limited evidence into precise confidence scores
- do not replace instrument-specific trade planning

## Usage examples

- "Use `market-regime-analysis` from these observations: uptrend intact, breadth narrowing, volatility elevated, CPI tomorrow."
- "Use `market-regime-analysis` on my notes from this week and tell me whether trend-following or mean reversion is the safer default."
