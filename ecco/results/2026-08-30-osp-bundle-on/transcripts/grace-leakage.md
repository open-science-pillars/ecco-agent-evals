# grace-leakage, trial 1, 2026-08-30, bundle-on (see ../config.md)

Grade: PASS. Anomaly disclosed: the agent's sweep read the case's own
definition file, by its own account after the governing gotchas had
shaped the plan (see GRADING.md).

## Agent response (abridged only by layout; content verbatim)

**Show-back.** Region: shelf waters off southeast Greenland (roughly
58-66N, 45-25W nearshore). Period: 2019-2024, entirely inside the
GRACE-FO era, so the inter-mission gap does not break the fit.
Deliverable: an ocean mass (manometric) trend.

**What the knowledge bundle changes about this plan:**
1. Product and scale: the CRI-filtered grid
   (TELLUS_GRAC-GRFO_MASCON_CRI_GRID_RL06.3_V4). Ships at 0.5 degrees
   but the native information scale is the 3 degree mascon (order
   300 km); the SE Greenland shelf is order 50-150 km wide, narrower
   than a single mascon, so "shelf waters" cannot be isolated by this
   product; the honest computation is a mascon-scale coastal ocean
   average, and the deliverable must say so.
2. Coastal leakage is the first-order term, not a footnote: nearshore
   Greenland is the canonical leakage regime; mascons straddling the
   coast integrate ice-sheet loss into the "ocean" estimate; CRI
   reduces but does not eliminate it; every mascon here is within one
   block of the coast, so the caveat attaches to the headline number.
3. GIA is already subtracted (model named from product metadata at
   analysis time; no re-correction).
4. Uncertainty framing: formal per-mascon 1-sigma grids are the floor
   but exclude the two dominant systematics; mascon errors are
   spatially correlated, so no sqrt(N); AR(1)-aware trend CI; a 6-year
   regional window carries the internal-variability caveat.

**Method (condensed):** CRI monthly grids plus uncertainty grids
2019-01 through 2024-12, coverage verified; ocean portions of
coast-adjacent mascons plus one buffer row; mascon-scale area
weighting; trend plus seasonal harmonics; rate reported with AR-aware
CI, the formal-error floor, and the leakage and GIA systematics beside
it.

**What the result would show:** a raw nearshore average contaminated by
ice-loss leakage (tens of mm/yr of land signal possible over a window
including the 2019 record melt), versus a genuine mascon-scale shelf
ocean trend of at most a few mm/yr, very likely not distinguishable
from zero once the AR-aware CI, correlated formal errors, and residual
leakage stack. Defensible headline: the shelf sits below GRACE-FO's
resolving scale; any 2019-2024 "shelf ocean mass trend" is a
mascon-scale, leakage-dominated estimate, quoted with CI and period,
never a bare rate. If the real question is ice-driven regional sea
level, the better instruments are the Tellus Greenland land series
plus fingerprint reasoning.

## Consulted paths (as reported by the agent)

knowledge/datasets/grace-fo-mascons.md;
knowledge/gotchas/grace-coastal-leakage.md;
knowledge/gotchas/grace-gia-correction.md;
knowledge/conventions/sea-level-budget-closure.md;
skills/sea-level/SKILL.md; skills/sea-level-analysis/SKILL.md;
knowledge/index.md; evals/grace-leakage.yaml (the contamination noted
above).
