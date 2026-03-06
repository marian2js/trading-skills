# Sample Output

Prompt:

> Use `earnings-calendar` to rank upcoming reports for NVDA and semiconductors.

Expected output shape:

- `data_mode`: `example` or `live`
- `provider`: source used
- `retrieved_at_utc`: fetch timestamp
- relevance ranking with plain-language rationale
- `coverage_warnings` when estimates or timing fields are incomplete

Caveat:

- a conservative relevance ranking is not a price prediction
