# Seed grades: OSP hand-graded baseline (2026-07-04)

The earliest record of these cases: one manual run per case on Claude
Code, N=1, rubric-graded by hand by the OSP steward, before the
automated runner and its N-trial confidence intervals existed. It was
kept beside the ocean-science plugin's copy of the cases while that
copy lived; the copy is retired and the record moves here, into the
entry sequence it began. It predates `results.yaml`, the scoring
script, and the configuration-disclosure format the later entries
follow, so it carries none of them; the grades and their evidence
lines are reproduced as recorded, with the file pointers rewritten to
their present locations.

Model: claude-fable-5 for all runs. Transcripts referenced live in
marketplace/docs/prompts/behavior/.

| Case | Date | Model | Grade | Evidence line |
|---|---|---|---|---|
| native-grid-refusal | 2026-07-04 | claude-fable-5 | pass | refused with the gotcha cited by title and date; both mechanisms explained; native path offered with collections and volumes (behavior/regridded-budget-refusal.md, verbatim prompt) |
| geothermal-omission | 2026-07-04 | claude-fable-5 | pass | plan included geothermal as a non-PO.DAAC static ancillary, snapshot bookends, native-grid rule, and the recipe's absolute tolerance, all cited |
| swot-calval-window | 2026-07-04 | claude-fable-5 | pass | range split at the July 2023 transition with per-phase cycle numbering; D-family constraint applied (behavior/swot-calval-window.md, verbatim prompt) |
| grace-leakage | 2026-07-04 | claude-fable-5 | pass | leakage surfaced unprompted with the fingerprint-vs-artifact split declared unknowable from the product; CRI named; mascon-scale honored; GIA not re-applied; open-ocean control region used diagnostically |
| volume-gate | 2026-07-04 | claude-fable-5 | pass | 7.25 TB request stopped with real numbers, four alternatives, nothing downloaded (behavior/swot-volume-gate.md, verbatim prompt) |

## Seed findings

Five of five pass. The gotcha-avoidance cases fire on knowledge-bundle
content (concepts cited by name in the transcripts), which is the
behavior the bundle-on versus bundle-off ablation quantifies (the two
2026-08-30 entries beside this one). The three cases added after this
date (ecco-release-mixing, mht-basin-scope, swot-crossover-unapplied)
have no seed grade; their first grades are in those entries.
