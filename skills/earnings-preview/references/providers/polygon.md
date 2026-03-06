# Polygon

Use this path only when the user already indicated `Polygon` or chose it from the supported provider list.

Polygon is useful here for recent reported fundamentals and prior-quarter anchors. It is not the best default source for exact upcoming earnings date or session confirmation.

## Best endpoint for recent reported financials

Call the official financials endpoint:

```bash
curl "https://api.polygon.io/vX/reference/financials?ticker=AAPL&timeframe=annual&limit=4&apiKey=<POLYGON_API_KEY>"
```

Use this when the user already knows the company and you need recent reported revenue, EPS-related fields, margin context, or balance-sheet anchors to frame the debate.

Pull only the fields you need:

- `ticker`
- `fiscal_period`
- `fiscal_year`
- `financials.income_statement`
- `financials.balance_sheet`
- `financials.cash_flow_statement`
- `filing_date`

## Optional market-reaction context

If the user also needs to know how the stock behaved around the last report, pair the fundamentals call with aggregate bars:

```bash
curl "https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2026-01-15/2026-02-15?adjusted=true&sort=asc&limit=500&apiKey=<POLYGON_API_KEY>"
```

## How to use the result

- use Polygon to anchor what the company last reported and where the debate may start
- do not pretend Polygon solved the forward schedule problem if the exact upcoming report date or session is still unclear
- if the user needs forward timing confirmation and Polygon does not provide it cleanly, say so and ask whether to supplement with `FMP` or `TradingEconomics`
- disclose that Polygon supplied the historical fundamental context

Official docs:

- [Polygon financials API](https://polygon.io/docs/rest/stocks/fundamentals/financials)
- [Polygon aggregate bars API](https://polygon.io/docs/rest/stocks/aggregates/custom-bars)
