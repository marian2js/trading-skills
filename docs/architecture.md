# Architecture

## Core idea

This repository is designed around user-facing analytical capabilities, not raw integrations.

That means:

- `macro-event-analysis` is a public skill
- `earnings-preview` is a public skill
- optional provider support such as `FMP` is secondary to those skills

This is the default because users think in terms of a job to be done, not in terms of vendor topology.

The same principle applies to scope boundaries: broker execution is not part of v1. Decision support comes first, while brokerage workflows remain explicitly out of scope.

Public skills should feel like analyst workflows. Raw fetch and plumbing concerns belong behind the skill boundary, not in the public skill text.

## Skill != Provider

A skill is a repeatable decision-support capability. It may use:

- no external data at all
- one external source
- several sources normalized into a common representation
- user-provided observations or files

A provider is only one possible dependency.

Treating "skill" and "provider integration" as the same concept causes predictable product problems:

- the install surface becomes cluttered with vendor names
- users must understand internal implementation choices
- swapping providers becomes a packaging problem instead of an internal change
- the capability becomes harder to trust because the design reflects engineering internals more than the user workflow

## Capability-first vs provider-first

Capability-first design produces cleaner public UX:

- one public skill per user job
- stable naming over time
- room to evolve internals without breaking the public mental model

Provider-first design tends to create unnecessary fragmentation:

- `fmp-earnings-preview`
- `fred-macro-event-analysis`
- `alpaca-market-regime-analysis`

Those names may describe implementation, but they are usually poor product defaults.

Provider-specific public skills should be rare and justified by user-facing differences, not engineering convenience.

## Optional provider support

Data-aware skills should follow a simple pattern:

1. Use the user's materials first
2. Only if critical data is missing, consult the skill's provider references
3. If the conversation already indicates a supported provider, use that provider path directly
4. Otherwise ask the user which supported provider they want to use
5. Continue the analysis and disclose the source used

This keeps the repo analysis-first while still leaving room for optional external data support when it is truly needed.

## v1 approach

The repository is intentionally pragmatic in v1:

- public skills stay focused on the analytical job
- provider support stays small and markdown-based
- user-provided context is preferred over external fetching
- `SKILL.md` frontmatter should stay lightweight unless extra fields are clearly paying for themselves now

This keeps the repo useful without turning it into a provider SDK or mini integration framework.
