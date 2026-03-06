# Live Data Setup

The current data-backed skills are:

- `macro-event-analysis`
- `earnings-preview`

Both skills can run in two modes:

- `example`: uses checked-in fixture data for demos and tests
- `live`: uses the internal FMP adapter when `FMP_API_KEY` is configured

## Configure live data

Set your API key in the environment before running the skill scripts:

```bash
export FMP_API_KEY=your_key_here
```

## How fallback works

Default behavior uses `--provider auto`:

- if live data is configured and available, the script uses `fmp`
- otherwise it falls back to the example adapter

If you do not want fallback behavior, use `--live-only`. In that mode the script exits with an error instead of switching to example data.

## How to verify live vs example mode

The JSON envelope and text output explicitly include:

- `data_mode`
- `provider`
- `selection_reason`
- `fallback_reason`
- `requested_window`
- `retrieved_at_utc`
- `coverage_warnings`

If `data_mode` is `example`, you are not looking at current live data.

## What to expect without credentials

- `macro-event-analysis` and `earnings-preview` still remain demoable through example fixtures
- `--provider fmp` fails with an actionable error if `FMP_API_KEY` is missing
- `--live-only` fails instead of falling back

Example:

```bash
python3 skills/macro-event-analysis/scripts/fetch_calendar.py --provider auto --json
python3 skills/earnings-preview/scripts/fetch_earnings.py --provider auto --json
python3 skills/macro-event-analysis/scripts/fetch_calendar.py --provider auto --live-only --json
```
