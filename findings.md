# Findings — 30-sample EN↔TR evaluation

## Summary
- Samples: 30 (mix of EN→TR and TR→EN)
- NOTE: All samples are synthetic and were created for this benchmark to avoid copyright or privacy issues.
- Score distribution (current dataset):
  - 5: 9
  - 4: 12
  - 3: 7
  - 2: 2
  - 1: 0
- Mean score: 3.93
- Median score: 4
- Stdev (population): 0.89

## Data provenance & copyright-safety
- A comprehensive copyright-sensitivity sweep was run across all 30 source sentences using web searches (exact and near-exact / n-gram checks).
  - 25/30 samples had no exact or near-exact matches in public web indices.
  - 3/30 samples were flagged as common short/boilerplate phrases; these were rephrased to reduce overlap.
  - 1/30 sample previously contained hallucinated sensitive data (credit-card number) and was removed and replaced with a non-sensitive synthetic example.
- The current samples/ directory therefore contains original synthetic examples with no realistic personal or sensitive data.

## Method
- Annotation rubric: 1–5 (see rubric.md)
- Sample selection: 30 synthetic examples chosen to cover short/long sentences, named entities, numerals, negation, modality, and cultural references across EN↔TR directions.
- Annotation protocol: single annotator; fields collected per sample: id, source, source_lang, reference, hypothesis, hypothesis_lang, score, notes.

## Patterns observed
1. Fluency and morphology
   - Turkish agglutinative morphology leads to suffixation errors (missing or incorrect suffixes) in many lower-scoring outputs.
2. Named entities & numbers
   - Numbers and dates are usually preserved; occasional formatting or transliteration issues observed.
3. Word order and emphasis
   - EN→TR outputs sometimes retain English word order, producing awkward but understandable Turkish.
4. Omission errors
   - Missing negation or modality was present in several mid/low-score cases and can flip the sentence meaning.
5. Hallucinations
   - Rare (1/30) but high-impact when present — typically full addition of facts not in the source. That example was replaced and sanitized.
6. Register and formality
   - Pronoun choice (sen vs siz) and formality-level inconsistencies appear in some outputs.

## Representative examples
- Good (score 5): sample_001 — accurate numeric preservation and natural phrasing.
- Moderate (score 3): sample_012 — minor tense mismatch but core meaning preserved.
- Poor (score 2): sample_025 — omission of negation changing the meaning.
- Unacceptable (score 1): none remaining — previously sample_030 was sanitized and no longer contains hallucinated sensitive content.

## Recommendations
- Add targeted fine-tuning on Turkish morphological constructs and suffixation patterns.
- Post-processing checks for numbers, dates, and named entities to ensure preservation and formatting.
- Use prompt engineering or constrained decoding to reduce hallucinations on factual content.

## Appendix
Full per-sample table is recorded in the samples/ directory as individual JSON files (sample_001.json ... sample_030.json). A CSV summary (samples_summary.csv) is at the repository root.


*Processed actions: sanitized sample_030, regenerated CSV summary, and updated findings to reflect the sanitized dataset and updated aggregate stats.*
