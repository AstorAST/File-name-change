import os
import json
import re
from pathlib import Path

def load_config():
    with open("config.json", "r", encoding="utf-8") as f:
        return json.load(f)

def apply_rules(filename, rules):
    new_name = filename
    for rule in rules:
        new_name = new_name.replace(rule["from"], rule["to"])
    return new_name

def main():
    config = load_config()
    target_dir = Path(config["target_dir"])
    rules = config["rules"]

    for file_path in target_dir.iterdir():
        if file_path.is_file():
            new_name = apply_rules(file_path.name, rules)
            if new_name != file_path.name:
                new_path = file_path.with_name(new_name)
                file_path.rename(new_path)
                print(f"✅ {file_path.name} -> {new_name}")

if __name__ == "__main__":
    main()