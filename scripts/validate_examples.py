import os
import yaml
import json
from jsonschema import validate, ValidationError

SCHEMAS_DIR = "schemas"
EXAMPLES_DIR = "examples"

def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def validate_example(example_path, schema_path):
    example = load_yaml(example_path)
    schema = load_json(schema_path)
    validate(instance=example, schema=schema)

def main():
    for root, _, files in os.walk(EXAMPLES_DIR):
        for file in files:
            if file.endswith(".yaml") or file.endswith(".yml"):
                example_path = os.path.join(root, file)
                schema_name = file.replace(".example.yaml", ".schema.json")
                schema_path = os.path.join(SCHEMAS_DIR, schema_name)

                print(f"Validating {example_path} against {schema_path}")
                validate_example(example_path, schema_path)

if __name__ == "__main__":
    main()


