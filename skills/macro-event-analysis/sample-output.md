# Sample Output

Prompt:

> Use `macro-event-analysis` to summarize the next 48 hours of macro risk for USD rates and index futures.

Expected output shape:

- prioritized event slate
- why the top events matter
- transmission channels to watch
- `data_mode`: `example` or `live`
- `provider`: source used
- `retrieved_at_utc`: fetch timestamp
- `requested_window`: requested dates and optional country filter
- `coverage_warnings`: missing consensus or no-event warnings

Caveat:

- example/demo data should always be labeled as example data and never be confused with current macro coverage
