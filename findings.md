# Findings — 30-sample EN↔TR evaluation

## Summary
- Samples: 30 (mix of EN→TR and TR→EN)
- Score distribution:
  - 5: 5
  - 4: 10
  - 3: 8
  - 2: 5
  - 1: 2
- Mean score: 3.37
- Median score: 3.5

## Method
- Annotation rubric: 1–5 (see rubric.md)
- Sample selection: 30 examples chosen to cover short/long sentences, named entities, numerals, negation, modality, and cultural references across EN↔TR directions.
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
   - Rare (2/30) but high-impact when present — typically full addition of facts not in the source.
6. Register and formality
   - Pronoun choice (sen vs siz) and formality-level inconsistencies appear in some outputs.

## Representative examples
- Good (score 5): sample_001 — accurate numeric preservation and natural phrasing.
- Moderate (score 3): sample_012 — minor tense mismatch but core meaning preserved.
- Poor (score 2): sample_025 — omission of negation changing the meaning.
- Unacceptable (score 1): sample_030 — hallucinated content unrelated to source.

## Recommendations
- Add targeted fine-tuning on Turkish morphological constructs and suffixation patterns.
- Post-processing checks for numbers, dates, and named entities to ensure preservation and formatting.
- Use prompt engineering or constrained decoding to reduce hallucinations on factual content.

## Appendix
Full per-sample table is recorded in the samples/ directory as individual JSON files (sample_001.json ... sample_030.json).
