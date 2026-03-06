# Earnings Preview Examples

## Case 1: The user already provided enough data

Prompt:

> Use `earnings-preview` for NVDA next week. I already know the date is Wednesday after the close. My focus is AI demand, gross margin, and read-through to semis.

Expected behavior:

- do not reach for a provider
- work from the user's date and debate framing
- build the preview around the key questions and read-through paths

## Case 2: The user already indicated a provider

Prompt:

> Use `earnings-preview` for ADBE and CRM next week. I do not have the exact timing, but you can use TradingEconomics for the missing schedule data.

Expected behavior:

- use the `TradingEconomics` path directly because the user already chose it
- gather only the missing timing facts
- continue the preview and disclose that `TradingEconomics` supplied the schedule confirmation

## Case 3: Critical data is missing and no provider was indicated

Prompt:

> Use `earnings-preview` for my software watchlist next week. I have not pulled the schedule yet.

Expected behavior:

- do not assume a provider
- consult `references/data-providers.md`
- ask which supported provider the user wants to use
- continue the preview only after the missing schedule context is available
