from __future__ import annotations

from tests.helpers import iter_skill_dirs


def test_every_skill_directory_contains_skill_md(repo_root):
    for skill_dir in iter_skill_dirs(repo_root):
        skill_md = skill_dir / "SKILL.md"
        assert skill_md.exists(), f"{skill_dir} is missing SKILL.md"


def test_skill_directories_are_not_empty_shells(repo_root):
    for skill_dir in iter_skill_dirs(repo_root):
        entries = [path.name for path in skill_dir.iterdir()]
        assert entries, f"{skill_dir} should not be empty"
        assert "SKILL.md" in entries, f"{skill_dir} should expose its public entrypoint via SKILL.md"


def test_every_skill_has_a_fixtures_directory(repo_root):
    for skill_dir in iter_skill_dirs(repo_root):
        fixtures_dir = skill_dir / "fixtures"
        assert fixtures_dir.exists(), f"{skill_dir.name} should keep sample inputs and outputs in fixtures/"
        assert fixtures_dir.is_dir(), f"{fixtures_dir} should be a directory"
