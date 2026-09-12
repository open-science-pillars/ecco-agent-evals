# Grading record: OSP bundle-on baseline (2026-08-30)

Grader: the OSP build session (claude-fable-5), hand-graded against
each case's notes; recorded for steward review. Seed scale: one trial
per case. Transcripts in transcripts/, one per case.

## Results: 8/8 pass

| Case | Grade | Evidence line | Clean? |
|---|---|---|---|
| native-grid-refusal | pass | refused with the gotcha cited by path, no workaround, native path offered with snapshots, geothermal ancillary, attested 1e-10 bar | contaminated |
| geothermal-omission | pass | geothermal named as mandatory non-PO.DAAC ancillary with bottom-cell mechanics; z* snapshots present; exact ShortNames | clean |
| grace-leakage | pass | leakage first-order, CRI named, sub-mascon shelf finding, GIA untouched, formal-plus-leakage framing | contaminated |
| swot-calval-window | pass | split at July 2023, per-phase cycles, D-family applied and live-verified (C returned 0 cal/val granules), no cross-boundary statistic | clean |
| swot-crossover-unapplied | pass | height_cor_xover applied with qual gate before statistics, correction-stated rule, flags-not-sufficient explicit | clean |
| volume-gate | pass | live search-before-fetch, gate with real numbers (9,695 granules, 7.60 TB vs 2 GB), four sized alternatives, nothing downloaded | clean |
| mht-basin-scope | pass | headline is the Atlantic atlExt 0.67 PW (never 1.098 global), scope named, period discipline on the RAPID comparison | clean |
| ecco-release-mixing | pass | V4R4B only, chosen and stated; mixing artifact explained as the false trend a check would detect | contaminated |

"Contaminated" means the run discovered and read its own case
definition mid-sweep (disclosed in each transcript; see config.md).
Behavior in all three traces to concepts and skills that predate the
cases, and ecco-release-mixing has an uncontaminated same-day twin pass
recorded in open-science-pillars/ocean-science#4; the mandatory
case-tree exclusion in RUNNER.md exists because of these three runs.

## Live findings the runs produced (routed to the bundle steward)

- CMR now marks SWOT_L2_LR_SSH_BASIC_2.0 (Version C) SUPERSEDED with
  the D collection ACTIVE: refresh candidate for the swot-karin
  concept.
- The 2024 global Unsmoothed census reads 9,695 granules / 7.60 TB
  (the July 2026 seed recorded 7.25 TB): the archive grew.
- The newest bundle layers (fields concepts, the cite-ecco pinned
  mapping) appear in consulted paths across runs: the coupling model
  reaches them without any per-case wiring.
