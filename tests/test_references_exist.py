from __future__ import annotations

from tests.helpers import markdown_links


def test_local_markdown_references_exist(repo_root):
    markdown_files = sorted(repo_root.rglob("*.md"))
    assert markdown_files, "Expected markdown documentation files in the repository"
    for markdown_file in markdown_files:
        if any(part.startswith(".") and part not in {".github"} for part in markdown_file.parts):
            continue
        for target in markdown_links(markdown_file):
            if not target or "://" in target or target.startswith("#"):
                continue
            path = (markdown_file.parent / target).resolve()
            assert path.exists(), f"{markdown_file} references missing file: {target}"
            assert repo_root in path.parents or path == repo_root, f"{markdown_file} link escapes repo root: {target}"
