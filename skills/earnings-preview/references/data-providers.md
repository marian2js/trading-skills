# Data Providers

Use this only if the user did not already provide enough schedule or estimate context.

Supported providers:

- `FMP`: earnings dates, timing, EPS estimates, revenue estimates
- `TradingEconomics`: earnings dates, release session, forecasts, previous values, and revenue context

If the user already named one of these providers or already shared usable access details, use that provider path directly.

Otherwise ask: "Which provider do you want to use for the missing earnings schedule data: FMP or TradingEconomics?"

Provider notes:

- [FMP](providers/fmp.md)
- [TradingEconomics](providers/tradingeconomics.md)
