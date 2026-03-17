import json

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
    with open("sona-2026-transcript.md", "r") as f:
        transcript = f.read()

    chunks = chunk_text(transcript, chunk_size=500, overlap=150)
    
    with open("step1_chunks.json", "w") as f:
        json.dump(chunks, f, indent=2)
    
    print(f"Successfully generated {len(chunks)} chunks.")