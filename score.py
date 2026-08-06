#!/usr/bin/env python3
"""
score.py

Load annotated sample files from samples/ (JSON files, one per sample) and produce:
- per-sample summary
- score distribution (1..5)
- mean, median, stdev
- optional CSV export

Expected sample file format (JSON):
{
  "id": "sample_001",
  "source": "English or Turkish source text",
  "source_lang": "en",
  "reference": "Gold reference translation",
  "hypothesis": "Model output",
  "hypothesis_lang": "tr",
  "score": 4,
  "notes": "short note about errors/strengths"
}
"""
import json
import glob
import statistics
import csv
from pathlib import Path

SAMPLES_GLOB = "samples/*.json"
OUTPUT_CSV = "samples_summary.csv"


def load_samples(glob_pattern=SAMPLES_GLOB):
    samples = []
    for path in sorted(glob.glob(glob_pattern)):
        with open(path, "r", encoding="utf-8") as f:
            samples.append(json.load(f))
    return samples


def summarize(samples):
    scores = [s.get("score") for s in samples if isinstance(s.get("score"), (int, float))]
    n = len(scores)
    if n == 0:
        return {}
    dist = {i: scores.count(i) for i in range(1,6)}
    summary = {
        "n": n,
        "mean": statistics.mean(scores),
        "median": statistics.median(scores),
        "stdev": statistics.stdev(scores) if n > 1 else 0.0,
        "distribution": dist
    }
    return summary


def write_csv(samples, outpath=OUTPUT_CSV):
    fieldnames = ["id","score","source","reference","hypothesis","notes"]
    with open(outpath, "w", newline="", encoding="utf-8") as csvf:
        writer = csv.DictWriter(csvf, fieldnames=fieldnames)
        writer.writeheader()
        for s in samples:
            writer.writerow({
                "id": s.get("id"),
                "score": s.get("score"),
                "source": s.get("source"),
                "reference": s.get("reference"),
                "hypothesis": s.get("hypothesis"),
                "notes": s.get("notes","")
            })
    print(f"Wrote CSV summary to {outpath}")


def main():
    samples = load_samples()
    print(f"Loaded {len(samples)} sample files.")
    summary = summarize(samples)
    if not summary:
        print("No scores found in samples.")
        return
    print("Summary:")
    print(f"  n = {summary['n']}")
    print(f"  mean = {summary['mean']:.2f}")
    print(f"  median = {summary['median']}")
    print(f"  stdev = {summary['stdev']:.2f}")
    print("  distribution (1..5):")
    for i in range(1,6):
        print(f"    {i}: {summary['distribution'].get(i,0)}")
    write_csv(samples)


if __name__ == "__main__":
    main()
