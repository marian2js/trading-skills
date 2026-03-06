from __future__ import annotations

from tests.helpers import json_code_blocks


def test_schema_doc_json_examples_parse(repo_root):
    schema_doc = repo_root / "docs" / "canonical-schemas.md"
    examples = json_code_blocks(schema_doc)
    assert examples, "docs/canonical-schemas.md should include at least one JSON example"
