# Earnings Calendar In Live Mode

Prompt:

> Use `earnings-calendar` to rank upcoming reports for NVDA and ADBE with live data only.

Example command:

```bash
export FMP_API_KEY=your_key_here
python3 skills/earnings-calendar/scripts/fetch_earnings.py --provider auto --live-only --symbols NVDA,ADBE --json
```

What to look for:

- `data_mode` is `live`
- `provider` is `fmp`
- `fallback_reason` is `null`
- `requested_window` echoes the date window and watchlist inputs

If live data is unavailable, `--live-only` should fail instead of switching to example data.
