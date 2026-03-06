# New Skill Checklist

Use this checklist before opening a pull request for a new skill or a major skill rewrite.

## Naming and scope

- The skill name is capability-first and concise.
- The skill does not expose a provider name unless there is a strong user-facing reason.
- The skill does not introduce broker dependency or execution behavior for v1.

## Skill quality

- `SKILL.md` frontmatter is complete and matches the directory name.
- The description explains what the skill does and when to use it.
- The skill clearly states helpful inputs.
- The skill clearly states what it returns.
- The skill clearly states what it will not do.
- The examples feel realistic rather than toy-like.

## Trust and risk clarity

- The skill avoids hype, guarantees, and fake precision.
- Risk, caveats, and uncertainty are explicit.
- Data-backed output discloses provider, freshness, and coverage limitations.
- Analysis support is kept separate from execution claims.

## Fixtures and tests

- `fixtures/` contains realistic sample data or examples.
- Static skills include example input/output pairs when practical.
- Data-backed skills include raw and normalized fixture examples.
- Root `tests/` were added or updated to cover the new behavior.

## Data-backed skills only

- The skill defines or reuses a canonical schema.
- At least one concrete provider adapter exists.
- An example or mock adapter or fixture path exists for demoability.
- Provider selection and fallback behavior are documented.
