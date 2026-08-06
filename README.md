# Multilingual LLM Evaluation Benchmark — EN↔TR

This repository contains a small evaluation benchmark for English↔Turkish translation quality assessment.

What’s included
- rubric.md — Scoring rubric (5-point scale) with fidelity/meaning-drift guidance.
- samples/ — 30 annotated sample files (JSON), one per sample. Fields: id, source, source_lang, reference, hypothesis, hypothesis_lang, score, notes.
- score.py — Simple scorer that loads samples/*.json and produces a CSV summary (samples_summary.csv) and basic stats.
- findings.md — Observations and recommendations from the 30-sample review.

How to run the scorer

Prerequisites: Python 3.8+.

Run locally:

```bash
python3 score.py
```

This will:
- Load all JSON files in samples/
- Print summary statistics (n, mean, median, stdev, distribution)
- Write samples_summary.csv to the repository root

Note: samples_summary.csv is already generated in the repo. Re-running the scorer will regenerate it from the contents of samples/.

Adding more samples
- Add a new JSON file to samples/ following the format used (sample_XXX.json). Then re-run score.py to update the CSV and stats.

Contact / author
- Pinar Methson (repo owner)
