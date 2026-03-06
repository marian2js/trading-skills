# Data Providers

Use this only if the user did not already provide enough market context.

Supported providers:

- `FMP`: recent price action, benchmark index context, and event calendar context
- `Yahoo Finance`: recent price action for major indexes, ETFs, and leaders

If the user already named one of these providers or already shared usable access details, use that provider path directly.

Otherwise ask: "Which provider do you want to use for the missing market context: FMP or Yahoo Finance?"

Provider notes:

- [FMP](providers/fmp.md)
- [Yahoo Finance](providers/yahoo-finance.md)
