# Economic Calendar In Example Mode

Prompt:

> Use `economic-calendar` to summarize the next 48 hours of macro event risk.

Example command:

```bash
python3 skills/economic-calendar/scripts/fetch_calendar.py --provider example --start-date 2026-03-12 --end-date 2026-03-13 --json
```

What to look for:

- `data_mode` is `example`
- `provider` is `example`
- `selection_reason` explains that example data was selected intentionally
- `coverage_warnings` is separate from the event list

This is demo data, not current market data.
