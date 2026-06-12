#!/usr/bin/env python3
"""
Validate Earth Brain OS example YAML files against JSON Schemas.

This validator supports local $ref resolution for schemas under ./schemas,
including v0.2 Modular Event Architecture layer schemas.
"""

from **future** import annotations

import json
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, RefResolver
from jsonschema.exceptions import ValidationError

ROOT_DIR = Path(**file**).resolve().parents[1]
SCHEMAS_DIR = ROOT_DIR / "schemas"
EXAMPLES_DIR = ROOT_DIR / "examples"

VALIDATION_TARGETS = [
{
"name": "Earth Brain Event v0.2 Modular Example",
"schema": SCHEMAS_DIR / "earth-brain-event.schema.json",
"example": EXAMPLES_DIR / "earth-brain-event.example.yaml",
}
]

def load_json(path: Path) -> dict[str, Any]:
with path.open("r", encoding="utf-8") as f:
return json.load(f)

def load_yaml(path: Path) -> Any:
with path.open("r", encoding="utf-8") as f:
return yaml.safe_load(f)

def build_schema_store() -> dict[str, dict[str, Any]]:
"""
Register all local schemas so relative and absolute $ref values resolve
without network access.

```
This is important because earth-brain-event.schema.json references:
  - layers/ai-agent-layer.schema.json
  - layers/optical-nervous-layer.schema.json
  - layers/knowledge-cortex-layer.schema.json
  - layers/trace-attribution-layer.schema.json
  - layers/royalty-circulation-layer.schema.json
  - layers/kazene-regulation-layer.schema.json
  - layers/defense-immune-layer.schema.json
  - layers/human-governance-layer.schema.json
"""
store: dict[str, dict[str, Any]] = {}

for schema_path in SCHEMAS_DIR.rglob("*.json"):
    schema = load_json(schema_path)

    file_uri = schema_path.resolve().as_uri()
    store[file_uri] = schema

    schema_id = schema.get("$id")
    if isinstance(schema_id, str):
        store[schema_id] = schema

return store
```

def format_validation_error(error: ValidationError) -> str:
path = "/".join(str(part) for part in error.absolute_path)
schema_path = "/".join(str(part) for part in error.absolute_schema_path)

```
location = path if path else "<root>"
schema_location = schema_path if schema_path else "<schema root>"

return (
    f"Validation error at: {location}\n"
    f"Schema path: {schema_location}\n"
    f"Message: {error.message}"
)
```

def validate_example(name: str, schema_path: Path, example_path: Path, store: dict[str, dict[str, Any]]) -> bool:
if not schema_path.exists():
print(f"[FAIL] {name}")
print(f"  Missing schema: {schema_path.relative_to(ROOT_DIR)}")
return False

```
if not example_path.exists():
    print(f"[FAIL] {name}")
    print(f"  Missing example: {example_path.relative_to(ROOT_DIR)}")
    return False

schema = load_json(schema_path)
example = load_yaml(example_path)

base_uri = schema.get("$id")
if not isinstance(base_uri, str):
    base_uri = schema_path.resolve().as_uri()

resolver = RefResolver(
    base_uri=base_uri,
    referrer=schema,
    store=store,
)

validator = Draft202012Validator(
    schema=schema,
    resolver=resolver,
)

errors = sorted(validator.iter_errors(example), key=lambda e: list(e.absolute_path))

if errors:
    print(f"[FAIL] {name}")
    print(f"  Schema : {schema_path.relative_to(ROOT_DIR)}")
    print(f"  Example: {example_path.relative_to(ROOT_DIR)}")
    print()
    for error in errors:
        print(format_validation_error(error))
        print()
    return False

print(f"[PASS] {name}")
print(f"  Schema : {schema_path.relative_to(ROOT_DIR)}")
print(f"  Example: {example_path.relative_to(ROOT_DIR)}")
return True
```

def main() -> int:
store = build_schema_store()

```
all_passed = True

for target in VALIDATION_TARGETS:
    passed = validate_example(
        name=target["name"],
        schema_path=target["schema"],
        example_path=target["example"],
        store=store,
    )
    all_passed = all_passed and passed

if not all_passed:
    print()
    print("Validation failed.")
    return 1

print()
print("All examples passed validation.")
return 0
```

if **name** == "**main**":
sys.exit(main())
