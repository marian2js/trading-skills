# Portfolio Concentration Walkthrough

Prompt:

> Use `portfolio-concentration` on this book before I add more semis: NVDA 8%, SMH 10%, QQQ 12%, cash 20%, the rest broad ETFs.

Expected outcome:

- the skill identifies both direct and indirect concentration
- overlap across NVDA, SMH, and QQQ is made explicit
- the result says whether the new add should be smaller, deferred, or reviewed against a fuller snapshot before `position-sizing`

This is a static skill. It works from a user-provided portfolio snapshot without live credentials.
