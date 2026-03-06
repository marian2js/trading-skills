# Macro Event Analysis In Example Mode

Prompt:

> Use `macro-event-analysis` to summarize the next 48 hours of macro event risk for USD rates and index futures.

Optional verification command:

```bash
python3 skills/macro-event-analysis/scripts/fetch_calendar.py --provider example --start-date 2026-03-12 --end-date 2026-03-13 --json
```

What to look for:

- `data_mode` is `example`
- `provider` is `example`
- `selection_reason` explains that example data was selected intentionally
- the analysis highlights which events matter and why
- `coverage_warnings` is separate from the event slate

This is demo data, not current market data.
