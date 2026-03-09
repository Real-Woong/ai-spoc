import json
from glob import glob

files = sorted(glob("batches/batch*.json"))
all_data = []
seen = set()

if not files:
    raise SystemExit("No batch files found in ./batches")

for fp in files:
    with open(fp, "r", encoding="utf-8") as f:
        arr = json.load(f)

    if not isinstance(arr, list):
        raise ValueError(f"{fp} is not a JSON array")

    for item in arr:
        _id = item.get("id")
        if not _id:
            raise ValueError(f"Missing id in {fp}")

        if _id in seen:
            raise ValueError(f"Duplicate id found: {_id}")
        seen.add(_id)
        all_data.append(item)

with open("merged.json", "w", encoding="utf-8") as f:
    json.dump(all_data, f, ensure_ascii=False, indent=2)

print("Merged items:", len(all_data))