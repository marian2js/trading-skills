# Market Regime Detector Walkthrough

Prompt:

> Use `market-regime-detector` from these observations: uptrend intact, breadth narrowing, volatility elevated, CPI tomorrow.

Expected outcome:

- regime classification: `trending-but-fragile`
- evidence tied directly to trend, breadth, volatility, and event backdrop
- an explicit caveat that heavy event risk weakens confidence in any regime label

This skill is data-optional. It can work from user observations without live credentials.
