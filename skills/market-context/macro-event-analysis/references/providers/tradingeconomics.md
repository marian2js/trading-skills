# TradingEconomics

Use this path only when the user already indicated `TradingEconomics` or chose it from the supported provider list.

Use the smallest calendar request that fills the missing event facts.

## Best endpoint for a country-level upcoming slate

```bash
curl "https://api.tradingeconomics.com/calendar/country/united%20states?c=<TE_API_KEY>&f=json"
```

Use this when the user wants the next relevant releases for one country and you do not need a narrow indicator filter yet.

## Best endpoint for a specific indicator and date range

```bash
curl "https://api.tradingeconomics.com/calendar/country/united%20states/indicator/nonfarm%20payrolls/2026-03-01/2026-03-31?c=<TE_API_KEY>&f=json"
```

Use this when the user already identified the key release and you only need the dated event history or forward window for that indicator.

Pull only the fields you need:

- `Date`
- `Country`
- `Event`
- `Actual`
- `Previous`
- `Forecast`
- `Importance`
- `LastUpdate`
- `Source`

Keep the result analytical. Do not mirror the whole calendar back to the user unless they asked for that explicitly.

Official docs:

- [TradingEconomics economic calendar by country docs](https://docs.tradingeconomics.com/economic_calendar/country/)
- [TradingEconomics economic calendar point-in-time docs](https://docs.tradingeconomics.com/economic_calendar/point-in-time/)
