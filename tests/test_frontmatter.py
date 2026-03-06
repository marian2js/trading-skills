from __future__ import annotations

from tests.helpers import (
    FRONTMATTER_ALLOWED,
    FRONTMATTER_REQUIRED,
    GENERIC_DESCRIPTION_FRAGMENTS,
    iter_skill_dirs,
    parse_frontmatter,
)


def test_frontmatter_exists_and_has_required_fields(repo_root):
    for skill_dir in iter_skill_dirs(repo_root):
        frontmatter = parse_frontmatter(skill_dir / "SKILL.md")
        missing = FRONTMATTER_REQUIRED - set(frontmatter)
        assert not missing, f"{skill_dir.name} is missing frontmatter fields: {sorted(missing)}"
        unexpected = set(frontmatter) - FRONTMATTER_ALLOWED
        assert not unexpected, (
            f"{skill_dir.name} should keep frontmatter minimal; unexpected fields: {sorted(unexpected)}"
        )


def test_frontmatter_name_matches_directory(repo_root):
    for skill_dir in iter_skill_dirs(repo_root):
        frontmatter = parse_frontmatter(skill_dir / "SKILL.md")
        assert (
            frontmatter["name"] == skill_dir.name
        ), f"{skill_dir / 'SKILL.md'} should use name '{skill_dir.name}', got '{frontmatter['name']}'"


def test_descriptions_are_specific(repo_root):
    for skill_dir in iter_skill_dirs(repo_root):
        frontmatter = parse_frontmatter(skill_dir / "SKILL.md")
        description = frontmatter["description"].strip()
        assert len(description) >= 40, f"{skill_dir.name} description is too short to be useful"
        lowered = description.lower()
        assert not any(
            fragment in lowered for fragment in GENERIC_DESCRIPTION_FRAGMENTS
        ), f"{skill_dir.name} description looks generic: {description!r}"
