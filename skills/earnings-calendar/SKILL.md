---
name: earnings-calendar
description: Summarize upcoming earnings events with normalized fields and conservative relevance ranking so the user can prepare around catalysts without learning provider internals.
---

# Earnings Calendar

Use this skill when you need to know which upcoming earnings reports are most relevant to a symbol, sector, or watchlist.

The public capability is `earnings-calendar`. Provider adapters are internal.

## What this skill does

- fetches upcoming earnings events through an internal adapter
- normalizes them into the canonical earnings event schema
- ranks relevance with conservative, explainable heuristics after normalization
- discloses source, freshness, and coverage limitations

The v1 implementation includes:

- a primary `fmp` adapter for live data
- an `example` adapter for demos and tests

Use [scripts/fetch_earnings.py](scripts/fetch_earnings.py) for the adapter-backed script and [references/relevance-ranking.md](references/relevance-ranking.md) for the ranking heuristics.

## Provider behavior

- If `FMP_API_KEY` is configured, the skill can fetch live calendar data.
- If not, the skill should explain that live coverage is unavailable and may use the example adapter.
- The output must identify whether it is using live or example data.

## What it returns

Always include:

- source or provider used
- date window requested
- timestamp or last update information when available
- relevance rationale, not just a numeric score
- caveats around incomplete estimates, timing changes, or missing sector data

## What this skill will not do

- imply an earnings reaction is predictable
- treat example fixtures as live market coverage
- hide incomplete timing or estimate fields behind a neat ranking

## Usage examples

- "Use `earnings-calendar` to rank the most relevant reports in the next seven days for semiconductors and mega-cap tech."
- "Use `earnings-calendar` for AAPL, AMZN, and COST, then tell me which events matter most for index and sector read-through."
