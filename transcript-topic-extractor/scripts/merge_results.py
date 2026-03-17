import json
import argparse
import glob

def merge_json_files(pattern, output_file):
    all_data = []
    files = glob.glob(pattern)
    for filename in files:
        with open(filename, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                if isinstance(data, list):
                    all_data.extend(data)
                else:
                    all_data.append(data)
            except json.JSONDecodeError:
                print(f"Warning: Skipping {filename} - Invalid JSON.")

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(all_data, f, indent=2)
    
    print(f"Merged {len(files)} files into {output_file}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge multiple JSON files into one.")
    parser.add_argument("pattern", help="Glob pattern for input files (e.g., 'batch_*.json').")
    parser.add_argument("output_file", help="Path to save the merged JSON file.")
    args = parser.parse_args()
    merge_json_files(args.pattern, args.output_file)