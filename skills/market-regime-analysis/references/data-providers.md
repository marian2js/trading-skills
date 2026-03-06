# Data Providers

Use this only if the user did not already provide enough market context.

Supported providers:

- `FMP`: recent price action, benchmark index context, and event calendar context through quotes, light historical prices, and the economic calendar
- `TradingEconomics`: market history for benchmark symbols and optional economic calendar checks through `/markets/historical` and `/calendar/country/...`
- `Polygon`: strong default for recent price history and benchmark comparison when the user already uses Polygon market data

If the user already named one of these providers or already shared usable access details, use that provider path directly.

Otherwise ask: "Which provider do you want to use for the missing market context: FMP, TradingEconomics, or Polygon?"

Fallback strategy:

- start with `FMP` when you need one provider for price context plus a quick macro-event check
- use `TradingEconomics` when cross-checking market history with macro calendar pressure
- use `Polygon` when the user already uses Polygon and the missing context is recent price action or benchmark comparison
- if event-backdrop context is still missing after a `Polygon` query, say so and ask whether to supplement with `FMP` or `TradingEconomics`

Provider notes:

- [FMP](providers/fmp.md)
- [TradingEconomics](providers/tradingeconomics.md)
- [Polygon](providers/polygon.md)
