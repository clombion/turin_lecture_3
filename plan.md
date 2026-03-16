# Implementation Plan: Extracting Commitments from SoNA 2026 Transcript

## Objective
Extract all commitments made in the 2026 State of the Nation Address transcript and format them into a CSV file with specific columns: Concise Description, Who/Organization, Amount, Timeline, Exact Quotes, and Reasoning. Finally, commit all generated files and push them to the repository.

## Strategy: Staged Execution with Intermediate Files and Parallel Subagents
To ensure accuracy and prevent data loss across chunks, the process will be broken down into distinct steps. Each step will read from the output file of the previous step and write its results to a new intermediate file. This allows for the use of multiple subagents working in parallel.

### Step 0: Save Plan
*   **Action:** Save a copy of this implementation plan to a file named `plan.md` in the root of the workspace repository.

### Step 1: Overlapping Document Chunking
*   **Action:** Read the `sona-2026-transcript.md` file.
*   **Process:** Programmatically split the transcript into overlapping chunks (e.g., ~500 words with a 150-word overlap) to ensure commitments spanning paragraph breaks are not lost.
*   **Output:** Save the resulting chunks to an intermediate file: `step1_chunks.json`.

### Step 2: Parallel Extraction of Themes and Commitments
*   **Action:** Read `step1_chunks.json`.
*   **Process:** Divide the chunks into batches. Delegate each batch to a separate **`generalist` subagent** running concurrently.
*   **Subagent Task:** For each chunk, the subagent will identify:
    *   **Themes:** General topics discussed.
    *   **Commitments:** Preliminary extraction of promises or actionable plans.
    *   **Draft Metadata:** Initial extraction of Who/Organization, Amount, Timeline, Exact Quotes, and Reasoning.
*   **Output:** Collect the results from all subagents and combine them into a single intermediate file: `step2_extracted_commitments.json`.

### Step 3: Consolidation and Full-Transcript Verification
*   **Action:** Read `step2_extracted_commitments.json` and the original `sona-2026-transcript.md`.
*   **Process:** Delegate the raw list of commitments to a **`generalist` subagent** for final review.
*   **Subagent Task:**
    1.  **Deduplicate & Merge:** Combine overlapping or duplicate commitments into a master list of *unique* commitments.
    2.  **Verify & Fill Gaps:** Cross-reference the unique commitments against the full original transcript to ensure all details (Who, Amount, Timeline, Exact Quotes) are complete and accurate.
*   **Output:** Save the verified, unique commitments to an intermediate file: `step3_verified_commitments.json`.

### Step 4: CSV Formatting and Final Output
*   **Action:** Read `step3_verified_commitments.json`.
*   **Process:** Map the JSON data exactly to the requested CSV columns:
    1.  `Concise Description`
    2.  `Who/Organization`
    3.  `Amount`
    4.  `Timeline`
    5.  `Exact Quotes`
    6.  `Reasoning`
*   **Output:** Generate the CSV content and save it to the final file: `sona-2026-commitments.csv`.

### Step 5: Commit and Push
*   **Action:** Use git commands to stage the new files (`plan.md`, `step1_chunks.json`, `step2_extracted_commitments.json`, `step3_verified_commitments.json`, `sona-2026-commitments.csv`).
*   **Process:** Create a commit with a descriptive message (e.g., "feat: extract and structure commitments from SoNA 2026 transcript").
*   **Output:** Push the commit to the remote repository.

## Verification & Testing
*   Ensure intermediate JSON files are correctly formatted and contain the expected data at each step.
*   Verify the final CSV file contains the correct headers and that data is properly aligned in columns.
*   Perform a spot check comparing a few rows in the CSV against the original transcript to confirm accuracy.
*   Verify the git push was successful.