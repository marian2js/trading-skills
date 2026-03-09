# Data Providers

Use this only if the user did not already provide enough event information.

Supported providers:

- `FMP`: economic release calendar with timing and basic consensus fields through `/stable/economic-calendar`
- `TradingEconomics`: macro event schedule and release context through `/calendar/...`

If the user already named one of these providers or already shared usable access details, use that provider path directly.

Otherwise ask: "Which provider do you want to use for the missing macro event data: FMP or TradingEconomics?"

Fallback strategy:

- start with `FMP` when the user needs a quick event slate by date window and country
- use `TradingEconomics` when the user needs indicator-specific history, country filtering, or source-heavy calendar context
- if one provider lacks forecast, prior, or timing detail for a critical event, say so and ask whether to supplement with the other supported provider

Provider notes:

- [FMP](providers/fmp.md)
- [TradingEconomics](providers/tradingeconomics.md)
