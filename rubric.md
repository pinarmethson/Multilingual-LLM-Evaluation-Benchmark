# 5-point Scoring Rubric for EN↔TR Evaluation

This rubric defines a 1–5 score for judging model translation outputs between English and Turkish.

Scoring scale (1 to 5):

1 — Unacceptable
- Meaning mostly lost; output is unintelligible or unrelated to the source.
- Major mistranslations, hallucinations, or empty output.
- Grammar and fluency are so poor that comprehension fails.

2 — Poor
- Partial meaning preserved but important information is incorrect or missing.
- Frequent grammatical errors or unnatural phrasing that obstruct understanding.
- Localization and cultural references typically wrong.

3 — Acceptable
- Core meaning preserved, but with noticeable errors (fluency/grammar/word choice).
- Minor omissions or mistranslations that do not change the main message.
- Readable and usable with light editing.

4 — Good
- Very minor errors only (one or two awkward phrases, minor grammar issues).
- Nuances and tone mostly preserved; terminology appropriate.
- Natural and fluent for the target language.

5 — Excellent
- Accurate, fluent, and natural; preserves nuance, tone, and register.
- No meaningful errors; correct vocabulary and idiomatic phrasing.


## Rubric dimensions (example)
Below is an explicit example dimension focusing on fidelity / meaning drift. Use this as a reference when judging whether the hypothesis has preserved the source meaning.

| Score | Definition |
|---|---|
| 5 | Fully faithful, no drift |
| 3 | Minor drift, meaning largely preserved |
| 1 | Significant hallucination or fabricated content |

Notes on applying the fidelity dimension
- Fidelity is critical: if the hypothesis introduces facts not present in the source (hallucination) or reverses key facts (e.g., loss of negation), prefer the lower score.
- When multiple dimensions conflict (fluency vs fidelity), prioritize fidelity: a fluent but hallucinated output should be scored lower than a less fluent but faithful one.
- Record short notes explaining the main error types (wording, omission, tense, mistranslation, cultural mismatch, hallucination) and flag hallucinations explicitly.

Annotation notes
- Prefer literal fidelity for named entities, numbers, and instructions; favor natural phrasing elsewhere.
- When in doubt between two close scores, prefer the lower one (be conservative).
- Record short notes explaining the main error types (wording, omission, tense, mistranslation, cultural mismatch, hallucination).

Examples
- Source: "The battery lasts up to 10 hours." — Hypothesis: "Pil 10 saate kadar dayanır." — Score: 5
- Source: "She drove to the bank." — Hypothesis: "O bankaya sürmek." — Score: 2 (ambiguous / mistranslated verb usage)
