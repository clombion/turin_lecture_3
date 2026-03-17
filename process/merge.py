import json
import os

all_commitments = []

for i in range(1, 4):
    filename = f"batch_{i}_results.json"
    if os.path.exists(filename):
        with open(filename, "r") as f:
            try:
                data = json.load(f)
                if isinstance(data, list):
                    all_commitments.extend(data)
                else:
                    print(f"Warning: {filename} does not contain a list.")
            except json.JSONDecodeError:
                print(f"Error: {filename} is not valid JSON.")

with open("step2_extracted_commitments.json", "w") as f:
    json.dump(all_commitments, f, indent=2)

print(f"Combined {len(all_commitments)} total commitments into step2_extracted_commitments.json")