# Data Providers

Use this only if the user did not already provide enough schedule or estimate context.

Supported providers:

- `FMP`: best default for forward earnings dates, report timing, and estimate fields through `/stable/earnings-calendar`
- `TradingEconomics`: useful for earnings dates, release session, forecast fields, and revenue context through `/earnings-revenues`
- `Polygon`: useful when the user already works in Polygon and needs recent reported financials, but not the best default for forward earnings schedule confirmation

If the user already named one of these providers or already shared usable access details, use that provider path directly.

Otherwise ask: "Which provider do you want to use for the missing earnings context: FMP, TradingEconomics, or Polygon?"

Fallback strategy:

- start with `FMP` when the missing piece is the upcoming earnings date, session, or consensus-style estimate fields
- use `TradingEconomics` when the user already works there or when revenue forecast context matters
- use `Polygon` when the user already uses Polygon for fundamentals and the missing piece is prior reported context rather than the upcoming schedule
- if the user insists on `Polygon` but the exact upcoming date or session still cannot be confirmed, say that clearly and ask whether to supplement with `FMP` or `TradingEconomics`

Provider notes:

- [FMP](providers/fmp.md)
- [TradingEconomics](providers/tradingeconomics.md)
- [Polygon](providers/polygon.md)
