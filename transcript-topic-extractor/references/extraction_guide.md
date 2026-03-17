# Extraction Schemas & Verification Guide

This guide provides best practices for defining extraction schemas and verifying the results to ensure high-fidelity data extraction from transcripts.

## 1. Defining Extraction Schemas

When using subagents to extract data, always provide a clear schema. Here are common patterns:

### Policy Commitments
- **Schema:** Description, Responsible Organization, Amount, Timeline, Exact Quote, Linguistic Reasoning.
- **Tip:** Focus on future-oriented action verbs (e.g., "will", "mandate", "directed").

### Stakeholder Mentions
- **Schema:** Stakeholder Name, Organization, Context/Topic, Sentiment (Positive/Neutral/Negative), Quote.
- **Tip:** Good for identifying influencers or lobbying groups mentioned in a speech.

### Argument/Thematic Extraction
- **Schema:** Theme, Key Argument, Supporting Evidence, Quote, Level of Certainty.
- **Tip:** Useful for long debates or legal transcripts.

## 2. The "Linguistic Reasoning" Principle

To ensure that the extraction is based on evidence rather than "hallucinations" or vague summaries, always ask for a "Reasoning" column that explains *why* a piece of text was identified as a hit.

- **BAD Reasoning:** "The government wants to fix water pipes because there's a crisis." (This is policy justification).
- **GOOD Reasoning:** "The phrase 'I have directed the Minister' identifies a formal executive instruction for future action." (This is linguistic evidence).

## 3. The Verification Workflow

1.  **Extraction Phase:** Extract data from small overlapping chunks (500 words/150-word overlap).
2.  **Consolidation Phase:** Merge results and deduplicate.
3.  **Audit Phase:** Pass the unique list back to a subagent with the *full transcript*. Ask the subagent to "re-read" the full text to verify every single detail, especially numeric data (amounts) and exact quotes.
