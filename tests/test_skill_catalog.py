from __future__ import annotations

from tests.helpers import iter_skill_dirs, parse_frontmatter


def test_skill_catalog_has_expected_v1_skills(repo_root):
    expected = {
        "position-sizing",
        "risk-reward-sanity-check",
        "post-trade-review",
        "economic-calendar",
        "earnings-calendar",
        "market-regime-detector",
    }
    actual = {skill_dir.name for skill_dir in iter_skill_dirs(repo_root)}
    assert actual == expected, f"Expected skill catalog {sorted(expected)}, got {sorted(actual)}"


def test_skill_catalog_metadata_is_consistent(repo_root):
    seen_names = set()
    for skill_dir in iter_skill_dirs(repo_root):
        frontmatter = parse_frontmatter(skill_dir / "SKILL.md")
        assert frontmatter["name"] not in seen_names, f"Duplicate skill name found: {frontmatter['name']}"
        seen_names.add(frontmatter["name"])
