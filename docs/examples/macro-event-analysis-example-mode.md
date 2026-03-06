# Macro Event Analysis Examples

## Case 1: The user already provided enough data

Prompt:

> Use `macro-event-analysis` on this event slate I already have for the next 48 hours: ECB decision Thursday 13:15 UTC, US PPI Thursday 12:30 UTC, US payrolls Friday 13:30 UTC. I care about USD rates and index futures.

Expected behavior:

- do not reach for a provider
- analyze the user-provided event slate directly
- explain why the top events matter and what could compress decision time

## Case 2: The user already indicated a provider

Prompt:

> Use `macro-event-analysis` for next week. I only have partial timing, but you can use FMP for the missing schedule data.

Expected behavior:

- use the `FMP` path directly because the user already chose it
- gather only the missing event facts
- continue the analysis and disclose that `FMP` supplied part of the event slate

## Case 3: Critical data is missing and no provider was indicated

Prompt:

> Use `macro-event-analysis` for next week in Europe and the US. I have no schedule yet.

Expected behavior:

- do not assume a provider
- consult `references/data-providers.md`
- ask which supported provider the user wants to use
- continue the analysis only after the missing schedule data is available
