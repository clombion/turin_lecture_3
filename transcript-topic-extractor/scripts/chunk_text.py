import json
import argparse

def chunk_text(text, chunk_size=500, overlap=150):
    words = text.split()
    chunks = []
    i = 0
    chunk_id = 1
    while i < len(words):
        chunk_words = words[i:i + chunk_size]
        chunk_text = ' '.join(chunk_words)
        chunks.append({"chunk_id": chunk_id, "text": chunk_text})
        chunk_id += 1
        i += chunk_size - overlap
    return chunks

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split text into overlapping chunks.")
    parser.add_argument("input_file", help="Path to the input file.")
    parser.add_argument("output_file", help="Path to save the JSON chunks.")
    parser.add_argument("--size", type=int, default=500, help="Chunk size in words.")
    parser.add_argument("--overlap", type=int, default=150, help="Overlap size in words.")
    args = parser.parse_args()

    with open(args.input_file, "r", encoding="utf-8") as f:
        text = f.read()

    chunks = chunk_text(text, chunk_size=args.size, overlap=args.overlap)
    
    with open(args.output_file, "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2)
    
    print(f"Generated {len(chunks)} chunks in {args.output_file}.")