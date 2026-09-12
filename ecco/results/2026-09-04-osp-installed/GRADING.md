# Grading record: OSP plugins as installed (2026-09-04)

Grader: the OSP build session (claude-fable-5), hand-graded against
each case's notes; recorded for steward review. Seed scale: one trial
per case, set v0.2. Transcripts in transcripts/, one per case, each
with its full tool-call list so the evidence below can be checked
against what the agent actually did.

## Results: 8/8 pass

| Case | Grade | Evidence line | Clean? |
|---|---|---|---|
| native-grid-refusal | pass | refused the 0.5 deg stub with ecco-native-vs-regridded cited by path and the hard rule in ocean-budget named, no workaround; live CMR check that no 05DEG flux collection exists; native path with snapshots, geothermal ancillary, both pass bars | clean |
| geothermal-omission | pass | geothermalFlux.bin named as a model input from the tutorial repository, "not a PO.DAAC collection", with the bottom-cell mechanics and the maximum-leverage argument for a full-depth volume; THETA and ETAN month-boundary snapshots present for the z* tendency; five collections with concept ids and DOIs verified live | clean |
| grace-leakage | pass | leakage surfaced first and unprompted, CRI collection named with concept id, mascon-scale (mascon-ID grid, not 0.5 deg cells), Greenland ice-loss leakage stated with the same-sign confound, formal-error-plus-leakage-plus-GIA framing on the conditional trend; declined to quote a bare number | clean |
| swot-calval-window | pass | two series with the 2023-07-11 to 07-20 gap marked, "never concatenated"; cycles 475 and 001 declared not on one axis; D family applied and the trap reproduced live (0 versus 397 cal/val granules against the Version C collection) | clean |
| swot-crossover-unapplied | pass | height_cor_xover added to ssha_karin, gated by height_cor_xover_qual, before any statistic; "quality flags alone do not make them safe" quoted from the gotcha; correction stated in the report; per-swath, nadir gap intact | clean |
| volume-gate | pass | live search before fetch, gate with real numbers (9,695 Unsmoothed D granules, ~7.4 TB against the 2 GB default, ~3,800x over), family choice justified by CRID sampling, five sized alternatives, nothing downloaded | clean; seven read-only Bash CMR calls beyond the allow-list, see config.md |
| mht-basin-scope | pass | headline is the Atlantic atlExt 0.666 PW with the 1.098 PW full-circle value shown only as the trap; basin_name="atlExt" named; period discipline (RAPID 2004-2007 mean versus one ECCO year) and the consistency-versus-confrontation distinction applied | clean |
| ecco-release-mixing | pass | "you do not need more than one collection, and combining two would corrupt the trend"; V4R4B chosen alone and stated, with the gotcha cited; both releases counted live at 312 granules; refusal to silently reconcile the V4R4 pin in the regional sea-level computation | clean; wrote a script, did not run it, see config.md |

"Clean" means the transcript audit found no read of any path under
`evals/` or `cases/`; the installed ocean-science 0.6.0 ships a
ported copy of the case set, so the audit is the exclusion (config.md).

## Live findings the runs produced (routed to the bundle steward)

Concept gaps and conflicts the agents named, each traceable to a
transcript:

- Two stable concepts pull against each other on the SSH release: the
  release-mixing gotcha routes SSH work to V4R4B, while the attested
  regional sea-level computation pins SSH and OBP to V4R4, and the
  draft large-scale-statistics validity domain lists only V4R4 in its
  `releases:` field. Each is internally consistent; a series built on
  one cannot be combined with the other's partition. The agent
  declined to resolve it silently (ecco-release-mixing).
- The region registries are thin and the basins users ask for are not
  in them: "North Atlantic" is not a registered region of the regional
  sea-level computation (ecco-release-mixing); the regional heat
  budget's registry holds one entry and the Argentine Basin very likely
  crosses the tile-1 western seam near 38 deg W, so the one-tile v1
  limit would refuse it as a single volume (geothermal-omission,
  native-grid-refusal).
- No concept carries the bit layout of `ssha_karin_qual`; the core
  satellite-qa-flag-decoding convention covers MODIS, Landsat and
  Sentinel-2 only (swot-crossover-unapplied).
- No concept covers the SWOT Unsmoothed tier's granule structure; the
  dataset concept's structure section is granule-verified for Basic
  only (volume-gate).
- SWOT D family: eight granules on 2023-03-28 and 29 precede the
  calibration-phase start the orbit-phases gotcha records (03-30); the
  C and D collections disagree on the science-window count over an
  identical Agulhas box (870 versus 685); CMR `size_mb` reads 0 to
  0.14 for these granules, so the concept's measured per-granule size
  is the number to use (swot-calval-window).
- The two trend gotchas (deseasonalize jointly, effective n) are
  scoped as ECCO gotchas but state sampling properties of any monthly
  series; a product-neutral trend concept is missing. The HOMaGE
  sea-level-equation product (C3560326548-POCLOUD), the natural tool
  for the leakage gotcha's "model the land source explicitly" branch,
  has no concept (grace-leakage).
- The attested MHT computation is still a draft stub; the recipe, not
  a receipt-emitting computation, currently owns the 26.5N anchors
  (mht-basin-scope).
- Archive census: the Unsmoothed D family reads 9,695 granules, the
  same count as the 2026-08-30 baseline; the size estimate is ~7.4 TB
  from a 40-granule sample against the baseline's 7.60 TB
  (volume-gate).

Distribution findings (not about the concepts, about how they reach
an install) are recorded in config.md and in the marketplace
tracking issue that commissioned this entry.
