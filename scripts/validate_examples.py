#!/usr/bin/env python3
"""
Validate YAML example files against JSON Schemas.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Dict, List, Tuple

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT_DIR = Path(__file__).resolve().parents[1]
SCHEMAS_DIR = ROOT_DIR / "schemas"
EXAMPLES_DIR = ROOT_DIR / "examples"

EXPLICIT_EXAMPLE_SCHEMA_MAP: Dict[str, str] = {
    "earth-brain-os-flow.example.yaml": "earth-brain-event.schema.json",
}

def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)

def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    if data is None:
        return {}

    if not isinstance(data, dict):
        raise ValueError(f"Example must be a YAML object: {path}")

    return data

def schema_name_from_example(example_path: Path) -> str:
    name = example_path.name

    if name in EXPLICIT_EXAMPLE_SCHEMA_MAP:
        return EXPLICIT_EXAMPLE_SCHEMA_MAP[name]

    if name.endswith(".example.yaml"):
        base_name = name.removesuffix(".example.yaml")
        return f"{base_name}.schema.json"

    if name.endswith(".example.yml"):
        base_name = name.removesuffix(".example.yml")
        return f"{base_name}.schema.json"

    raise ValueError(f"Unsupported example filename format: {example_path}")

def collect_validation_targets() -> List[Tuple[Path, Path]]:
    if not EXAMPLES_DIR.exists():
        raise FileNotFoundError(f"Examples directory not found: {EXAMPLES_DIR}")

    if not SCHEMAS_DIR.exists():
        raise FileNotFoundError(f"Schemas directory not found: {SCHEMAS_DIR}")

    targets: List[Tuple[Path, Path]] = []

    example_paths = sorted(
        list(EXAMPLES_DIR.glob("*.example.yaml"))
        + list(EXAMPLES_DIR.glob("*.example.yml"))
    )

    for example_path in example_paths:
        schema_name = schema_name_from_example(example_path)
        schema_path = SCHEMAS_DIR / schema_name

        if not schema_path.exists():
            raise FileNotFoundError(
                f"Schema not found for example: {example_path.relative_to(ROOT_DIR)} "
                f"-> expected {schema_path.relative_to(ROOT_DIR)}"
            )

        targets.append((example_path, schema_path))

    return targets

def validate_example(example_path: Path, schema_path: Path) -> List[str]:
    errors: List[str] = []

    try:
        schema = load_json(schema_path)
        example = load_yaml(example_path)

        validator = Draft202012Validator(
            schema,
            format_checker=FormatChecker(),
        )

        validation_errors = sorted(
            validator.iter_errors(example),
            key=lambda error: list(error.path),
        )

        for error in validation_errors:
            location = "/".join(str(part) for part in error.absolute_path)
            if not location:
                location = "<root>"

            errors.append(
                f"{example_path.relative_to(ROOT_DIR)} "
                f"against {schema_path.relative_to(ROOT_DIR)} "
                f"at {location}: {error.message}"
            )

    except Exception as exc:
        errors.append(
            f"{example_path.relative_to(ROOT_DIR)} "
            f"against {schema_path.relative_to(ROOT_DIR)}: {exc}"
        )

    return errors

def main() -> int:
    try:
        targets = collect_validation_targets()
    except Exception as exc:
        print(f"Validation setup failed: {exc}", file=sys.stderr)
        return 1

    if not targets:
        print("No example files found.")
        return 0

    all_errors: List[str] = []

    for example_path, schema_path in targets:
        errors = validate_example(example_path, schema_path)
        all_errors.extend(errors)

        if errors:
            print(f"FAIL: {example_path.relative_to(ROOT_DIR)}")
        else:
            print(
                "PASS: "
                f"{example_path.relative_to(ROOT_DIR)} "
                f"-> {schema_path.relative_to(ROOT_DIR)}"
            )

    if all_errors:
        print("\nValidation errors:", file=sys.stderr)
        for error in all_errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"\nAll examples validated successfully. Total: {len(targets)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
