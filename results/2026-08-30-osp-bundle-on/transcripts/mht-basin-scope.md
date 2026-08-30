# mht-basin-scope, trial 1, 2026-08-30, bundle-on (see ../config.md)

Grade: PASS. Clean run (no case-definition contamination).

## Agent response (verbatim)

**ECCO v4r4 Atlantic MHT at 26.5N, 2010 mean: 0.67 PW, about 0.66 PW
(roughly half) below the RAPID/MOCHA observed mean of
1.33 +/- 0.40 PW.**

That is your headline comparison. Details that bind it:

- **The number.** 0.666 PW is the bundle's validated 2010 anchor for
  the RAPID-comparable Atlantic section (`basin_name="atlExt"`),
  computed with `ecco_v4_py.calc_meridional_heat_trsp` from the monthly
  native-grid advective temperature fluxes plus geometry;
  steward-verified 2026-07-04 against live PO.DAAC granules, with the
  basin-sum identity checked (atlExt 0.666 + pacExt 0.430 + indExt
  0.002 = global circle 1.098 PW). I report the recipe's validated
  anchor rather than a fresh run, since this session downloads no data;
  a recomputation would follow that exact recipe.
- **Scope guard.** The global-circle value at 26.5N is 1.098 PW;
  quoting that against RAPID is a documented scope error. RAPID
  observes the Atlantic only, so only the atlExt number is comparable.
- **Why the gap is not a scandal.** The RAPID reference
  (1.33 +/- 0.40 PW, Johns et al. 2011) is a 2004-2007 mean, while 2010
  is the documented AMOC-minimum year, so this period mismatch biases
  the apparent offset high (RAPID's own 2010 was anomalously low). ECCO
  v4 Atlantic means also sit systematically low of RAPID's mean per the
  recipe, and a single-year mean carries a wider envelope than the
  multi-year 0.8 to 1.4 PW band. ECCO ships no formal error fields; the
  recipe's RAPID-comparison spread is the operative uncertainty
  framing. A period-matched comparison would use RAPID's own 2010
  series from the dataset DOI (10.17604/3nfq-va20).

## Consulted paths (as reported by the agent)

knowledge/recipes/ecco-mht-26n.md;
knowledge/gotchas/ecco-mht-basin-scope.md;
knowledge/datasets/rapid-mocha.md; knowledge/datasets/ecco-v4r4.md;
knowledge/fields/ecco-v4r4/temperature-flux-3d.md;
knowledge/gotchas/ecco-native-vs-regridded.md;
knowledge/computations/ecco-mht-26n.md;
skills/meridional-transport/SKILL.md; skills/transport-analysis/SKILL.md;
skills/compare-obs/SKILL.md.
