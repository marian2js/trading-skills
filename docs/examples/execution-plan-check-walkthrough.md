# Execution Plan Check Walkthrough

Prompt:

> Use `execution-plan-check` on my plan to buy a niche ETF at the open with a market order and a stop below yesterday's low.

Expected outcome:

- the skill distinguishes setup quality from execution quality
- spread, open-auction, and liquidity risks are made explicit
- the output says whether the order logic should change before the user moves on to final sizing

This is a static skill. It works from the user's order plan and market context without live credentials.
