---
name: market-regime-detector
version: 0.1.0
description: Classify market context conservatively from trend, volatility, breadth, and event backdrop so the user can adapt tactics without relying on black-box regime claims.
dependency_class: data-optional
category: market-data
status: beta
requires_configuration: false
asset_coverage: equities, futures, fx
tags: market-context, regime, risk-management
---

# Market Regime Detector

Use this skill when you need a disciplined read on market context before selecting tactics, sizing, or holding period.

This is a context classifier, not a prediction engine.

## Inputs

This skill can work in two modes:

- manual observations supplied by the user
- optional structured inputs via [scripts/assess_regime.py](scripts/assess_regime.py)

Useful inputs include:

- price trend state
- volatility state
- breadth or participation state
- liquidity or macro event backdrop
- whether leadership is concentrated or broad

See [references/regime-framework.md](references/regime-framework.md) for the scoring logic.

## Workflow

1. Assess trend, volatility, breadth, and event backdrop separately.
2. Look for agreement or conflict between those signals.
3. Classify the environment conservatively.
4. Explain which trading styles are supported and which are fragile in that regime.
5. State what evidence would change the classification.

## What it returns

Always include:

- regime classification
- key evidence used
- what weakens confidence in the classification
- tactical implications for risk-taking

Avoid fake certainty or theatrical confidence percentages.

## What this skill will not do

- forecast returns from a single regime label
- turn limited evidence into precise confidence scores
- replace instrument-specific trade planning

## Usage examples

- "Use `market-regime-detector` from these observations: uptrend intact, breadth narrowing, volatility elevated, CPI tomorrow."
- "Use `market-regime-detector` on my notes from this week and tell me whether trend-following or mean reversion is the safer default."
