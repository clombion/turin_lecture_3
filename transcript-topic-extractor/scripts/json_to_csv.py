import json
import csv
import argparse

def json_to_csv(input_file, output_file, columns):
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not data or not isinstance(data, list):
        print("Error: Input JSON must be a non-empty list of objects.")
        return

    # If columns not specified, use keys from the first object
    if not columns:
        columns = list(data[0].keys())

    with open(output_file, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        for row in data:
            # Map row keys to specified columns, handling missing keys
            mapped_row = {col: row.get(col, "") for col in columns}
            writer.writerow(mapped_row)

    print(f"Successfully wrote {len(data)} rows to {output_file}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a list of JSON objects to CSV.")
    parser.add_argument("input_file", help="Path to the input JSON file.")
    parser.add_argument("output_file", help="Path to the output CSV file.")
    parser.add_argument("--columns", nargs="+", help="Ordered list of column headers.")
    args = parser.parse_args()
    json_to_csv(args.input_file, args.output_file, args.columns)