---
name: economic-calendar
description: Summarize upcoming macro event risk from a normalized economic calendar so the user can see timing, importance, and coverage caveats without dealing with provider internals.
---

# Economic Calendar

Use this skill when you need a practical view of upcoming macro event risk that could affect risk-taking, holding periods, or trade timing.

The public capability is `economic-calendar`. Provider details are internal.

## What this skill does

- selects an internal provider adapter
- fetches upcoming economic events
- normalizes them into the canonical economic event schema
- analyzes event risk from the normalized schema with source, freshness, and caveats

The v1 implementation includes:

- a primary `fmp` adapter for live data
- an `example` adapter for demos, tests, and no-credential environments

See [references/interpretation-guide.md](references/interpretation-guide.md) for how to interpret the output and [scripts/fetch_calendar.py](scripts/fetch_calendar.py) for the adapter-backed script.

## Provider behavior

- If `FMP_API_KEY` is configured, the skill can use live data through the internal `fmp` adapter.
- If live credentials are missing, the skill should say so clearly and may fall back to the `example` adapter.
- The output must always disclose whether the data is live or example data.

## What it returns

Always include:

- source or provider used
- event window requested
- timestamp or last update information when available
- high-impact items first
- caveats about missing values, country coverage, or schedule uncertainty

## What this skill will not do

- predict the market direction after a release
- pretend example data is live data
- hide missing estimates, stale timestamps, or incomplete coverage

## Usage examples

- "Use `economic-calendar` to summarize the next 48 hours of macro risk for USD rates and index traders."
- "Use `economic-calendar` for next week, highlight high-impact US and euro area events, and tell me where data coverage looks thin."
