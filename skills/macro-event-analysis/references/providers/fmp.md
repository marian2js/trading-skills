# FMP

Use this path only when the user already indicated `FMP` or chose it from the supported provider list.

Use the official economic calendar endpoint for the specific window you need:

```bash
curl "https://financialmodelingprep.com/stable/economic-calendar?from=2026-03-06&to=2026-03-13&country=US&apikey=<FMP_API_KEY>"
```

Pull only the fields you need for the analysis:

- `date`
- `country`
- `event`
- `impact`
- `previous`
- `estimate`
- `actual`
- `lastUpdated`

Filter to the user’s actual window and countries before writing the analysis.

After collecting the missing facts, return to the macro analysis. Disclose that `FMP` supplied the event schedule.

Official docs:

- [FMP economic calendar API](https://site.financialmodelingprep.com/developer/docs/stable/economics-calendar)
