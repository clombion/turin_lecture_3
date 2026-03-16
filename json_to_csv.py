import json
import csv
import sys

input_file = "step3_verified_commitments.json"
output_file = "sona-2026-commitments.csv"

columns = [
    "Concise Description",
    "Who/Organization",
    "Amount",
    "Timeline",
    "Exact Quotes",
    "Reasoning"
]

try:
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    print(f"Error: {input_file} not found.")
    sys.exit(1)
except json.JSONDecodeError:
    print(f"Error: {input_file} is not valid JSON.")
    sys.exit(1)

with open(output_file, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=columns)
    writer.writeheader()
    for row in data:
        # Map the row keys to the requested columns, handling case variations or missing keys
        mapped_row = {}
        for col in columns:
            # We check for exact match or lowercase match just in case
            val = row.get(col, row.get(col.lower(), row.get(col.replace("/", " / "), "")))
            mapped_row[col] = val if val is not None else ""
        writer.writerow(mapped_row)

print(f"Successfully wrote {len(data)} commitments to {output_file}.")
