# swot-calval-window, trial 1, 2026-08-30, bundle-on (see ../config.md)

Grade: PASS. Clean run. Note: the agent made read-only CMR metadata
queries (allowed under the search-before-fetch policy) and live-fired
the version-family trap on purpose.

## Agent response (abridged only by layout; content verbatim)

**Parse (show-back).** Region: Agulhas Current and retroflection
(10E-40E, 45S-30S proposed). Time: 2023-03-01 through 2024-03-31.
Tier: Basic. Version family: D, for the reasons below.

**What the bundle changes before anything is fetched:**
1. The window spans the July 2023 orbit transition, so this is two
   datasets, not one: a 1-day repeat cal/val orbit until July 2023,
   then the 21-day science orbit, with different coverage, sampling,
   and cycle numbering (cal/val cycles in the 400-500s; science
   restarts at 001). One series across the transition would alias the
   orbit change into apparent ocean variability. The plan splits at
   the transition.
2. Cal/val data exists only in the Version D collections, confirmed
   live: BASIC_2.0 (Version C) returned 0 granules for Mar-Jul 2023
   over the box; BASIC_D returned 405. CMR also now marks the C Basic
   collection SUPERSEDED with D ACTIVE, so D serves the whole record.
3. Any SSH statistic adds the crossover calibration first
   (ssha_karin + height_cor_xover, gated by height_cor_xover_qual),
   stated in the summary.
4. CRIDs (PGD0_01, PGD0_02 observed) get recorded at load time.
5. Subset to the box before aggregating (whole-pass matches can carry
   zero in-box pixels).

**Search results (metadata only):** cal/val 405 granules from
2023-03-28 (cycle 473, daily repeats of 3-4 fixed passes); science 685
granules from 2023-07-26 (cycle 001); the mid-July orbit-transfer gap
is real and stays. Volume estimated at ~10 GB from the concept's
verified ~9.4 MB/granule (CMR size metadata unreliable here).

**Volume gate: STOPPED** at the 2 GB template default; four sized
alternatives offered (science-only ~6.4 GB; tighter retroflection box;
fewer cycles; Basic already lightest).

**The time series: two series, never concatenated.** Cal/val: daily
along-track statistics at fixed tracks (flag-decoded, trimmed,
crossover-corrected, per swath, nadir gap intact), high-frequency
variability at those tracks, not regional coverage. Science: cycle-level
regional statistics each 21 days (~12 points), the mesoscale field in
2D. Phases comparable only qualitatively; no statistic spans the July
boundary; uncertainty per the dataset concept (ssh_karin_uncert is
random noise only); ~60 percent masked fractions normal.

## Consulted paths (as reported by the agent)

knowledge/index.md; knowledge/datasets/swot-karin.md;
knowledge/gotchas/swot-calval-orbit-phases.md;
knowledge/gotchas/swot-crossover-unapplied.md; skills/swot/SKILL.md;
skills/load-swot/SKILL.md; skills/swot/references/swot-products.md;
ocean-science.local.md.template.
