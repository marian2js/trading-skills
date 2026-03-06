# Sample Output

Prompt:

> Use `market-regime-analysis` from these observations: uptrend intact, breadth narrowing, volatility elevated, CPI tomorrow.

Expected output shape:

- regime: `trending-but-fragile`
- evidence: trend, volatility, breadth, and event backdrop
- caveat: heavy event risk reduces confidence in any regime label

Limitation:

- the skill classifies context; it does not forecast returns
