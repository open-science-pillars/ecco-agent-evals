# Grading record: OSP bundle-off red demonstration (2026-08-30)

Grader: the OSP build session (claude-fable-5), hand-graded against
each case's notes; recorded for steward review. This entry exists to
show the set runs red as designed: same prompts, no knowledge bundle.

## Results: 0/2 pass, as designed

| Case | Grade | Failure line |
|---|---|---|
| mht-basin-scope | FAIL | ~1.0 PW quoted as THE 26.5N transport with no basin scope named (full-circle-consistent, not the Atlantic 0.666); near-agreement with RAPID constructed, the documented invent-agreement mode |
| swot-crossover-unapplied | FAIL | asserts the crossover calibration is pre-applied ("you do not apply corrections yourself") and computes statistics on the raw flag-gated field; silently wrong by meters per the governing concept |

Both responses are fluent, detailed, and plausible, which is the point:
the traps produce confident wrong answers, not errors.

## The contrast

The bundle-on entry (../2026-08-30-osp-bundle-on/) passes both cases
under the same prompts. Prior recorded evidence in the OSP design notes
(design-knowledge-coupling.md, July 2026): the knowledge-coupling POC
measured mht-basin-scope at 4/5 ON vs 1/5 OFF (+0.60), with
native-grid-refusal at ceiling in both arms (the hard-refusal floor)
and geothermal-omission at 5/5 in both arms (the physics is in model
training; that case's failability is a grader-discrimination property,
demonstrated in fixtures/grader-calibration/, not a bundle-ablation
property).

Voided attempts: two earlier OFF runs under a weaker instruction found
the workspace's knowledge bundle unbidden, consulted it, and passed;
voided as OFF evidence and disclosed in config.md.
