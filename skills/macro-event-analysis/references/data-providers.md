# Data Providers

Use this only if the user did not already provide enough event information.

Supported providers:

- `FMP`: economic release calendar with timing and basic consensus fields
- `TradingEconomics`: macro event schedule and release context

If the user already named one of these providers or already shared usable access details, use that provider path directly.

Otherwise ask: "Which provider do you want to use for the missing macro event data: FMP or TradingEconomics?"

Provider notes:

- [FMP](providers/fmp.md)
- [TradingEconomics](providers/tradingeconomics.md)
