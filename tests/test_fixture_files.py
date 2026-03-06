from __future__ import annotations

import json


def test_all_fixture_json_files_parse(repo_root):
    fixtures = sorted(repo_root.glob("skills/*/fixtures/*.json"))
    assert fixtures, "Expected fixture JSON files under skills/*/fixtures/"
    for fixture in fixtures:
        try:
            json.loads(fixture.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise AssertionError(f"{fixture} is not valid JSON: {exc}") from exc
