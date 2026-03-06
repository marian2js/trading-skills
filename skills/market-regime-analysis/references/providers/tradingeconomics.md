# TradingEconomics

Use this path only when the user already indicated `TradingEconomics` or chose it from the supported provider list.

Use it to pull only the minimum price or event context needed for the regime read.

## Best endpoint for recent market trend

Call the official markets historical endpoint with a short benchmark basket:

```bash
curl "https://api.tradingeconomics.com/markets/historical/spy:us,qqq:us,iwm:us?c=<TE_API_KEY>&d1=2026-02-20&d2=2026-03-06&f=json"
```

Use this when you need a quick read on trend, relative strength, or narrowing breadth across major US equity benchmarks.

Pull only the fields you need:

- `Symbol`
- `Date`
- `Open`
- `High`
- `Low`
- `Close`

## Optional event-backdrop check

If the regime read also needs macro timing context, use the economic calendar by country endpoint:

```bash
curl "https://api.tradingeconomics.com/calendar/country/united%20states?c=<TE_API_KEY>&f=json"
```

Use only the relevant upcoming events. Do not dump the entire calendar into the output.

## How to use the result

- use the market history to judge trend persistence, volatility, and leadership concentration
- use the calendar only to confirm whether event risk is quiet, normal, or heavy
- if breadth, liquidity, or cross-asset context is still incomplete, say so directly
- disclose that TradingEconomics supplied part of the market context

Official docs:

- [TradingEconomics markets historical docs](https://docs.tradingeconomics.com/markets/historical/)
- [TradingEconomics economic calendar by country docs](https://docs.tradingeconomics.com/economic_calendar/country/)
