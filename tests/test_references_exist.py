from __future__ import annotations

from tests.helpers import iter_skill_dirs, markdown_links


def test_local_markdown_references_exist(repo_root):
    for skill_dir in iter_skill_dirs(repo_root):
        skill_md = skill_dir / "SKILL.md"
        for target in markdown_links(skill_md):
            if not target or "://" in target or target.startswith("#"):
                continue
            path = (skill_md.parent / target).resolve()
            assert path.exists(), f"{skill_md} references missing file: {target}"
            assert repo_root in path.parents or path == repo_root, f"{skill_md} link escapes repo root: {target}"
