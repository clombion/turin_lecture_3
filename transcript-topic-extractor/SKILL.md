---
name: transcript-topic-extractor
description: High-fidelity structured data extraction (commitments, entities, themes) from long transcripts (speeches, meetings, debates). Use when documents exceed 2,000 words or require evidence-based verification against the original text.
---

# Transcript Topic Extractor

This skill provides a high-fidelity workflow for extracting structured data from long transcripts by combining overlapping chunking, parallel subagent processing, and full-text verification.

## Workflow

### 1. Segmentation (Overlapping Chunking)
Use `scripts/chunk_text.py` to divide the transcript into overlapping segments.
- **Goal:** Ensure information spanning boundaries is never lost.
- **Default:** 500-word chunks with 150-word overlap.

```bash
python scripts/chunk_text.py <input.md> step1_chunks.json --size 500 --overlap 150
```

### 2. Parallel Batch Extraction
Delegate extraction tasks to multiple `generalist` subagents in parallel.
- **Instructions:** Tell subagents to extract based on a specific schema (e.g., Commitments, Stakeholders).
- **Sub-task:** "Read `step1_chunks.json`, process chunks X-Y, and save results as `batch_N.json`."
- **Important:** Always ask for a 'Reasoning' column that focuses on linguistic evidence (e.g., "The phrase 'We are introducing' indicates a new policy").

### 3. Consolidation
Merge the batch results using `scripts/merge_results.py`.
- **Goal:** Combine all extracted data into one master list.

```bash
python scripts/merge_results.py "batch_*.json" step2_extracted_merged.json
```

### 4. Global Synthesis & Verification
Pass the merged list back to a `generalist` subagent along with the original transcript.
- **Task:** Deduplicate the list and verify every entry against the full original text to fill missing metadata (Amounts, Timelines, Quotes).
- **Goal:** Produce a final, unique, and verified JSON array.

### 5. Standardized Export
Convert the final JSON to CSV using `scripts/json_to_csv.py`.

```bash
python scripts/json_to_csv.py step3_final_verified.json final_output.csv --columns "Col1" "Col2" "Col3"
```

## Reference Guide
For advice on extraction schemas and verification techniques, consult `references/extraction_guide.md`.
