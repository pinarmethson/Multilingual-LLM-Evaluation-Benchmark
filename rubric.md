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
Below are explicit rubric dimensions you can apply when annotating. Use the fidelity/meaning-drift dimension as a required check; other dimensions (fluency, terminology, register) are optional signals to include in notes.

### Fidelity (meaning-drift)
This dimension captures whether the hypothesis preserves the source meaning and avoids adding information not present in the source.

| Score | Fidelity (meaning drift) |
|---|---|
| 5 | Fully faithful, no drift — hypothesis contains only content entailed by the source; preserves facts, negation, numbers, named entities, and core relations. |
| 4 | Minor drift — small rephrasings, clarifications, or word‑choice differences that do not change facts or the main message. |
| 3 | Moderate drift — limited omission/addition or subtle change in emphasis that slightly alters nuance but leaves the main proposition intact. |
| 2 | Major drift — important information is omitted, reversed, or changed so that the reader could be misled about a key fact or intent. |
| 1 | Significant hallucination or fabrication — hypothesis introduces facts not in the source, adds sensitive or high‑impact content, or otherwise grossly misrepresents the source (e.g., losing negation that flips meaning). |

Notes on applying the fidelity dimension
- Fidelity is critical: if the hypothesis introduces facts not present in the source (hallucination) or reverses key facts (e.g., loss of negation), prefer the lower score.
- When multiple dimensions conflict (fluency vs fidelity), prioritize fidelity: a fluent but hallucinated output should be scored lower than a less fluent but faithful one.
- Use a checklist while scoring: numbers/dates, negation/modality, named entities, core relations (who-did-what-to-whom), and factual claims.
- Immediately flag hallucinations in the notes with explicit examples of what was added.

### Fluency
(Optional signal) Assess naturalness, grammaticality, and idiomatic phrasing. Low fluency lowers the overall impression but does not override fidelity.

### Terminology and register
(Optional signal) Evaluate whether specialized terms and formality level are appropriate for the target language and context.

Annotation notes
- Prefer literal fidelity for named entities, numbers, and instructions; favor natural phrasing elsewhere.
- When in doubt between two close scores, prefer the lower one (be conservative).
- Record short notes explaining the main error types (wording, omission, tense, mistranslation, cultural mismatch, hallucination).
- Optional: include per-sample fields `fidelity_score`, `fluency_score`, and `register_score` in addition to the overall `score` if you want multi-dimensional annotations.

Examples
- Score 5: preserves numeric fact and nuance — Source: "The battery lasts up to 10 hours." Hypothesis: "Pil 10 saate kadar dayanır."  
- Score 3: slight nuance change but main point preserved — e.g., subtle tense/aspect mismatch or added hedging.  
- Score 1: hallucination — Hypothesis introduces a new sensitive fact not in source (e.g., a credit-card number).
