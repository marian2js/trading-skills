# Earnings Preview In Live Mode

Prompt:

> Use `earnings-preview` for NVDA and ADBE with live data only. I care about the key debates and the names with the biggest read-through risk.

Optional verification command:

```bash
export FMP_API_KEY=your_key_here
python3 skills/earnings-preview/scripts/fetch_earnings.py --provider auto --live-only --symbols NVDA,ADBE --json
```

What to look for:

- `data_mode` is `live`
- `provider` is `fmp`
- `fallback_reason` is `null`
- the output prioritizes the reports that actually matter to the watchlist
- source, freshness, and coverage caveats stay explicit

If live data is unavailable, `--live-only` should fail instead of switching to example data.
