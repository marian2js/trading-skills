# Polygon

Use this path only when the user already indicated `Polygon` or chose it from the supported provider list.

Polygon is strongest here for recent price action and benchmark comparison. It does not replace macro calendar context.

## Best endpoint for recent benchmark history

Call the official aggregate bars endpoint:

```bash
curl "https://api.polygon.io/v2/aggs/ticker/SPY/range/1/day/2026-02-20/2026-03-06?adjusted=true&sort=asc&limit=500&apiKey=<POLYGON_API_KEY>"
```

Repeat for `QQQ`, `IWM`, or sector ETFs only if the breadth or leadership question actually requires them.

Pull only the fields you need:

- `ticker`
- `results[].t`
- `results[].o`
- `results[].h`
- `results[].l`
- `results[].c`
- `results[].v`

## How to use the result

- use the bar series to judge trend persistence, recent range expansion, and relative benchmark strength
- do not imply Polygon answered the macro-event question if the backdrop still depends on calendar risk
- if event timing still matters after the price check, ask whether to supplement with `FMP` or `TradingEconomics`
- disclose that Polygon supplied the market-price context

Official docs:

- [Polygon aggregate bars API](https://polygon.io/docs/rest/stocks/aggregates/custom-bars)
