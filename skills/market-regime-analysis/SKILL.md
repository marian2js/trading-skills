---
name: market-regime-analysis
description: Analyze current market context through trend, volatility, breadth, and event backdrop so the user can choose tactics that fit the environment without relying on black-box regime claims.
---

# Market Regime Analysis

Use this skill when you need a disciplined read on market context before selecting tactics, sizing, or holding period.

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
- if they already indicated `FMP` or `Yahoo Finance`, use [references/providers/fmp.md](references/providers/fmp.md) or [references/providers/yahoo-finance.md](references/providers/yahoo-finance.md) directly
- otherwise consult [references/data-providers.md](references/data-providers.md) and ask which supported provider they want to use
- once the missing context is gathered, continue the regime analysis and disclose the source used

## Analysis process

1. Assess trend, volatility, breadth, and event backdrop separately.
2. Look for agreement or conflict across those dimensions.
3. Classify the environment conservatively.
4. Explain which tactics fit the environment and which become fragile.
5. State what evidence would change the classification.

Use [references/regime-framework.md](references/regime-framework.md) if you need the default label set and interpretation guidance.

## Output structure

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
