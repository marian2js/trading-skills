# Contributing

This repository is for portable trading and investing skills that improve judgment, risk clarity, planning, and review discipline.

Before adding or reshaping a skill, read [docs/repo-conventions.md](docs/repo-conventions.md) and [docs/new-skill-checklist.md](docs/new-skill-checklist.md).

For release hygiene and portability expectations, also read [docs/compatibility-and-install.md](docs/compatibility-and-install.md), [docs/versioning-and-releases.md](docs/versioning-and-releases.md), and [docs/release-checklist.md](docs/release-checklist.md).

## Contribution standards

Contributions should be:

- capability-first, not provider-first
- conservative in tone and claims
- understandable for non-technical users
- explicit about assumptions, freshness, and limitations
- portable across tools that support `SKILL.md`-style skills

Do not contribute:

- hype-driven "signal" skills with unverifiable claims
- broker execution workflows in v1
- public provider-specific skills unless there is a strong user-facing reason
- public skills whose main job is fetch/normalize plumbing instead of analysis
- giant abstractions that add complexity before the capability is useful

## Skill checklist

Every new public skill should include:

- `skills/<group>/<skill-name>/SKILL.md`
- minimal frontmatter with a name that matches the directory
- a specific description that explains what the skill does and when to use it
- realistic usage examples
- supporting references in `references/` when the method needs extra detail
- a lean folder shape without `fixtures/` or `sample-output.md`

If the skill is data-backed, it should also include:

- a user-data-first workflow
- a small `references/data-providers.md` file if optional provider support is needed
- concise provider docs under `references/providers/`
- clear behavior when the user already named a provider, and when they have not

## Writing guidelines

- Write for trust, not drama.
- Prefer plain language over financial theater.
- Do not imply certainty where only context exists.
- Avoid fake precision. Rounded ranges and caveats are often better than false exactness.
- Separate analysis from recommendation. The skill can support a decision without pretending to make it.

## Adding provider support to an existing skill

Do not create a new public skill for a provider unless the provider-specific capability is itself the product.

Instead:

1. Add the provider to `references/data-providers.md`.
2. Add or update a concise provider doc under `references/providers/`.
3. Update the skill text only if the user-facing analysis workflow changes.
4. Keep source disclosure in the final output.

Read [docs/provider-support.md](docs/provider-support.md) before adding provider guidance.

## Validation

Validation stays lightweight and repository-wide:

- skill structure
- frontmatter quality
- link integrity
- provider reference coverage
- markdown-first workflow behavior
- lean skill-directory enforcement

## Local setup quick start

```bash
make catalog
make validate
```

## Developer workflow

The repo keeps metadata intentionally light. In most cases the only frontmatter you should need is `name` and `description`.

## Shortest path to contribute a fix

1. Update the relevant file under `skills/`, `docs/`, or `scripts/`.
2. Run `make catalog` if skill names, descriptions, or example docs changed.
3. Run `make validate`.
4. Update [CHANGELOG.md](CHANGELOG.md) if the change is release-noteworthy.

Typical contributor flow:

1. Add or update a skill under `skills/<group>/<skill>/`.
2. Keep the skill folder lean and put longer examples in `docs/examples/` when they help users evaluate the capability.
3. Regenerate the small machine-readable catalog and README skill index with `make catalog`.
4. Run `make validate` before opening a PR.

## Maintainer workflow

Typical maintainer pass before merge or release:

1. Review the skill or doc change.
2. Confirm example docs still reflect the current behavior.
3. Run `make catalog`.
4. Run `make validate`.
5. Update [CHANGELOG.md](CHANGELOG.md) if needed.
6. Open or merge the PR once CI is green.

Run the full checks before opening a PR:

```bash
make catalog
make validate
```

If you only want the fast structural checks, use:

```bash
make validate
```

Avoid adding metadata or abstractions unless they clearly improve the current install experience, browsing experience, or validation quality.

## What not to add yet

Do not add:

- broker adapters
- order execution
- account management
- portfolio syncing
- provider-specific public skill clones of existing capabilities

## Suggested PR scope

Keep pull requests narrow:

- one new skill
- one provider-support addition
- one documentation improvement
- one validator improvement

This keeps review focused and preserves the clarity of the repository.
