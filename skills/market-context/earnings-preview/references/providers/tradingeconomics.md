# TradingEconomics

Use this path only when the user already indicated `TradingEconomics` or chose it from the supported provider list.

Use the smallest request that fills the missing earnings facts.

## Best endpoint for a date window

Call the official earnings and revenues endpoint:

```bash
curl "https://api.tradingeconomics.com/earnings-revenues?c=<TE_API_KEY>&d1=2026-03-09&d2=2026-03-20&f=json"
```

Use this when the user gave a time window and you need the report date, session, or forecast fields for more than one company.

Pull only the fields you need for the preview:

- `Date`
- `Symbol`
- `Name`
- `Forecast`
- `RevenueForecast`
- `Previous`
- `RevenuePrevious`
- `MarketRelease`
- `Importance`
- `LastUpdate`

## Best endpoint for a single company

If the user only cares about one company and you already know the provider symbol, use:

```bash
curl "https://api.tradingeconomics.com/earnings-revenues/symbol/aapl:us?c=<TE_API_KEY>&d1=2025-01-01&d2=2026-12-31&f=json"
```

TradingEconomics symbols are provider-specific, such as `aapl:us`.

## How to use the result

- confirm the report date and `MarketRelease` timing
- use `Forecast` and `RevenueForecast` only as context, not as a prediction signal
- if the provider lacks a field the analysis needs, say so clearly and continue with the available information
- disclose that TradingEconomics supplied the missing schedule or estimate data

Official docs:

- [TradingEconomics earnings and revenues docs](https://docs.tradingeconomics.com/financials/earnings_revenues/)
