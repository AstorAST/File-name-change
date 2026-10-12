import os
import json
import shutil
from pathlib import Path

def load_config():
    with open("config.json", "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    config = load_config()
    target_dir = Path(config["target_dir"])
    

    if "copy_before" in config:
        for rule in config["copy_before"]:
            from_path = target_dir / rule["from"]
            if from_path.exists():
                for to_name in rule["to"]:
                    to_path = target_dir / to_name
                    shutil.copy2(from_path, to_path)
                    print(f"📋 {rule['from']} -> {to_name}")
            else:
                print(f"⚠️ 源文件不存在: {rule['from']}")
    

    rules = config["rules"]

    rule_map = {rule["from"]: rule["to"] for rule in rules}
    
    for file_path in target_dir.iterdir():
        if file_path.is_file():
            filename = file_path.name

            if filename in rule_map:
                new_name = rule_map[filename]
                new_path = file_path.with_name(new_name)
                file_path.rename(new_path)
                print(f"✅ {filename} -> {new_name}")
            else:

                pass

if __name__ == "__main__":
    main()