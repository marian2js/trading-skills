# Data Providers

Use this only if the user did not already provide enough market context.

Supported providers:

- `FMP`: recent price action, benchmark index context, and event calendar context
- `TradingEconomics`: market history for benchmark symbols and optional economic calendar checks

If the user already named one of these providers or already shared usable access details, use that provider path directly.

Otherwise ask: "Which provider do you want to use for the missing market context: FMP or TradingEconomics?"

Provider notes:

- [FMP](providers/fmp.md)
- [TradingEconomics](providers/tradingeconomics.md)
