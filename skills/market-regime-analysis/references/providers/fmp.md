# FMP

Use this path only when the user already indicated `FMP` or chose it from the supported provider list.

Use it to pull only the minimum price or event context needed for the regime read.

## Best endpoint for latest benchmark snapshot

Use the short quote endpoint for quick current context:

```bash
curl "https://financialmodelingprep.com/stable/quote-short?symbol=SPY&apikey=<FMP_API_KEY>"
```

This is useful when you only need the latest price, change, and volume snapshot.

## Best endpoint for recent trend

Use the light historical endpoint for a short lookback:

```bash
curl "https://financialmodelingprep.com/stable/historical-price-eod/light?symbol=SPY&from=2026-02-20&to=2026-03-06&apikey=<FMP_API_KEY>"
```

Repeat for other symbols only if needed, such as `QQQ`, `IWM`, or sector ETFs the user already cares about.

## Optional event-backdrop check

If the regime read also needs macro timing context, use:

```bash
curl "https://financialmodelingprep.com/stable/economic-calendar?from=2026-03-06&to=2026-03-13&country=US&apikey=<FMP_API_KEY>"
```

## How to use the result

- use quote data for the latest snapshot, not for forecasting
- use historical prices to judge trend quality and recent volatility
- use the calendar endpoint only if event risk is part of the missing context
- disclose that FMP supplied part of the market context

Official docs:

- [FMP quote short API](https://site.financialmodelingprep.com/developer/docs/stable/quote-short)
- [FMP historical price light API](https://site.financialmodelingprep.com/developer/docs/stable/historical-price-eod-light)
- [FMP economic calendar API](https://site.financialmodelingprep.com/developer/docs/stable/economics-calendar)
