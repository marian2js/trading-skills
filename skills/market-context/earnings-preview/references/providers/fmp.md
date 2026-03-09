# FMP

Use this path only when the user already indicated `FMP` or chose it from the supported provider list.

Use the smallest request that fills the missing earnings facts.

## Best endpoint for a date window

Call the official earnings calendar endpoint:

```bash
curl "https://financialmodelingprep.com/stable/earnings-calendar?from=2026-03-09&to=2026-03-20&apikey=<FMP_API_KEY>"
```

Use this when the user gave a date window and you need report timing or estimate context for one or more names.

Pull only the fields you need for the preview:

- `date`
- `symbol`
- `name`
- `time`
- `epsEstimated`
- `revenueEstimated`
- `epsActual`
- `revenueActual`
- `lastUpdated`

## Best endpoint for a single company

If the user only cares about one company and you already know the symbol, use:

```bash
curl "https://financialmodelingprep.com/stable/earnings?symbol=AAPL&apikey=<FMP_API_KEY>"
```

This is useful when the user wants one-name context rather than a calendar sweep.

## How to use the result

- confirm the report date and timing first
- use estimate fields only to frame the debate, not to imply direction
- if `time`, EPS estimates, or revenue estimates are missing, say that explicitly
- disclose that FMP supplied the missing schedule or estimate data

Official docs:

- [FMP earnings calendar API](https://site.financialmodelingprep.com/developer/docs/stable/earnings-calendar)
- [FMP earnings report API](https://site.financialmodelingprep.com/developer/docs/earnings-historical-earnings)
