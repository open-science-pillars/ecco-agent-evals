# grace-leakage, trial 1, 2026-09-04, installed (see ../config.md)

Grade: PASS. Clean run (no case or evals file read; audit in config.md).

## Tool calls (20)
- `Skill` {"skill": "core:start"}
- `Bash` {"command": "claude plugin list --json 2>/dev/null | head -200", "description": "List installed plugins as JSON"}
- `Bash` {"command": "cat $PLUGINS/core/0.4.0/skills/consult-knowledge/SKILL.md 2>/dev/null", "description": "Read c...
- `Bash` {"command": "for p in $PLUGINS/core/0.4.0 $PLUGINS/hydrol...
- `Bash` {"command": "grep -ril \"mascon\\|GRACE\" $PLUGINS/*/*/knowledge 2>/dev/null | sort", "description": "Find ...
- `Bash` {"command": "B=$PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac; echo \"### DATASET\"; c...
- `Bash` {"command": "B=$PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac; ls -R $B | head -80; ec...
- `Bash` {"command": "B=$PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac; ls $B/gotchas $B/validi...
- `Bash` {"command": "cat $PLUGINS/ocean-science/0.6.0/skills/sea-level/SKILL.md 2>/dev/null; echo \"=====ANALYSIS==...
- `Bash` {"command": "B=$PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac; sed -n 1,200p $B/conven...
- `Bash` {"command": "ls -R $PLUGINS/core/0.4.0/knowledge | head -60; echo \"=== load-grace-tws ===\"; cat /Users/pr...
- `Bash` {"command": "ls -la $WORKDIR 2>/dev/null; echo \"--- any local config ---\"; find $HOME/...
- `Bash` {"command": "sed -n 1,120p $PLUGINS/core/0.4.0/knowledge/conventions/smell-test-ranges.md", "description": ...
- `ToolSearch` {"query": "select:mcp__plugin_core_earthdata__get_collections,mcp__plugin_core_earthdata__get_granules,mcp__plugin_core_earthdata__get_citations", "max_resul...
- `Bash` {"command": "B=$PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac; echo \"### connectors/e...
- `mcp__plugin_core_earthdata__get_collections` {"short_name": "TELLUS_GRAC-GRFO_MASCON_CRI_GRID_RL06.3_V4", "has_granules": true, "limit": 5}
- `mcp__plugin_core_earthdata__get_collections` {"keyword": "GRACE-FO mascon ocean", "has_granules": true, "limit": 10}
- `mcp__plugin_core_earthdata__get_granules` {"collection_concept_id": "C3195527175-POCLOUD", "temporal_start_date": "2019-01-01T00:00:00Z", "temporal_end_date": "2024-12-31T23:59:59Z", "spatial_wkt_geo...
- `Bash` {"command": "B=$PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac; echo \"### effective-n\...
- `Bash` {"command": "sed -n 1,90p $PLUGINS/core/0.4.0/skills/analysis-review/SKILL.md", "description": "Read analys...

## Agent response (verbatim final message, typography normalized to ASCII)

## What I did, and what I did not

I consulted the installed knowledge bundles and verified the product in CMR (read-only metadata). I did **not** download data or fit a trend - partly because this session is read-only on data, but mainly because the analysis as you framed it is the textbook wrong-result mode for this product, and a number from it would not mean what its coordinates claim. Details and the defensible alternatives below.

## Bundle consultation

Installed bundles searched (from `claude plugin list --json`): `core@0.4.0`, `ocean-science@0.6.0`, `hydrology@0.3.0`, and the provider bundle `nasa-daac-knowledge@2026.9.1-58dd8445099b`. Since the provider bundle is installed, I cite it rather than the pinned `snapshot-podaac/` copies carried by ocean-science and hydrology (same text, provider tier wins per `core/skills/consult-knowledge`). Three concepts bind this request; none is past its `stale_after` (2027-01-04, today is 2026-09-04).

**`knowledge/podaac/gotchas/grace-coastal-leakage.md`** - stable, severity high, human-reviewed (`human:PaulMRamirez`, 2026-07-04). This concept carries `eval_case: grace-leakage`, and it names your exact case:

> "Nearshore ocean mass series inherit land signal: apparent coastal sea level or ocean-mass trends **near Greenland**, Alaska, or major river basins can be dominated by leakage rather than ocean change. Nothing errors; the series just is not what its coordinates claim."

Its correct-approach clause: stay at mascon scale (not grid-cell scale), use the CRI product, **keep a buffer from strong land sources or model them explicitly**, and attach the formal uncertainty grids plus a leakage caveat for any mascon within one block of the coast. It closes with the scope: "Basin-scale open-ocean averages are robust; the trap is specifically the nearshore."

**`knowledge/podaac/datasets/grace-fo-mascons.md`** - stable, human-reviewed 2026-07-04. Two clauses change the plan. The 0.5 deg grid *represents* 3 deg mascons: "the native information scale is the mascon, not the grid cell." And: "a basin whose area approaches or falls below the mascon scale is resolution- and leakage-dominated, so state the resolution and leakage caveats before delivering its series." Its Uncertainty section also says the shipped per-mascon 1-sigma grids "do NOT include the two dominant systematic terms: coastal leakage and the GIA model choice; both exceed the formal errors regionally," and that mascon errors are spatially correlated, so a regional average does not beat noise down by sqrtN.

**`knowledge/podaac/gotchas/grace-gia-correction.md`** - stable, severity medium, human-reviewed 2026-07-04. A GIA model is already subtracted from this product. Any trend statement must name the applied model (read from product metadata at analysis time), never re-correct, and quote the GIA-model spread as a systematic term when comparing to literature. This bites trends specifically.

Also consulted: `knowledge/podaac/conventions/sea-level-budget-closure.md` (stable, human-verified 2026-09-04) for the bookkeeping any manometric trend must declare, and `knowledge/podaac/connectors/earthdata-mcp.md` (**draft**, so voiced as unverified) for the CMR discovery surface.

## Why the SE Greenland shelf box is not deliverable as an ocean mass trend

Three problems compound, and they all point the same direction:

1. **The region is smaller than the measurement.** The mascons are ~300 km equal-area spherical caps. The southeast Greenland shelf is order 100-200 km wide (general geography, not from a concept). Your target region does not span even one independent estimate. Whatever you average, you are reading mascons whose information is shared with the Greenland margin.

2. **The nearest land signal is the largest one on Earth for this period.** Greenland ice-sheet mass loss over 2019-2024 sits directly inside the mascons that touch the shelf. The CRI filter partitions straddling mascons, and the collection is the right one to use - but the concept is explicit that it "reduces leakage substantially but does not eliminate it."

3. **The leakage artifact and the real physics have the same sign.** Ice loss leaking into an adjacent ocean mascon depresses its apparent mass; the gravitational sea-level fingerprint of that same ice loss *also* depresses near-field ocean mass. So a shelf box will very likely return a negative manometric trend, and the box has no power to say how much is ocean and how much is bleed-through from the ice sheet next door. That confounding is my reasoning from the mechanism the concept describes, labeled as general method - no installed concept states it.

A number computed anyway would be a description of Greenland's ice loss wearing ocean coordinates. That is the failure the concept exists to prevent, so I am not producing one.

One trap to close off explicitly: the product ships optional gain (scale) factors for sub-mascon work, but the collection metadata scopes them to continental hydrology applications (Wiese, Landerer & Watkins 2016). They are not a license to resolve a shelf.

## What CMR confirms

The product identity in the dataset concept is live and current:

- `TELLUS_GRAC-GRFO_MASCON_CRI_GRID_RL06.3_V4`, version RL06.3Mv04, `C3195527175-POCLOUD`, DOI `10.5067/TEMSC-3JC634`, PO.DAAC/POCLOUD, ongoing from 2002-04-04.
- Granule check for 2019-01-01 -> 2024-12-31 over a shelf box (60-68 deg N, 44-30 deg W): **1 granule**, `GRCTellus.JPL.200204_202606.GLO.RL06.3M.MSCNv04CRI` - the full record 2002-04 to 2026-06 in a single global netCDF. Your 6-year window is a time slice of one file; there is no per-month granule filtering to do.
- The collection ships the land mask used for the CRI separation, the per-mascon uncertainty values, and the **gridded mascon-ID field** in the same directory. That mascon-ID grid is what makes the "stay at mascon scale" rule executable rather than aspirational - it tells you which 0.5 deg cells are the same estimate.
- The unfiltered twin `TELLUS_GRAC-GRFO_MASCON_GRID_RL06.3_V4` (`C3195502222-POCLOUD`) is also live; its own abstract flags it as expert-use-only for people applying their own land/ocean separation.

## What I'd recommend instead

**Option A - move the box off the shelf.** Take an Irminger Sea / Labrador Sea open-ocean domain that keeps at least one full mascon of buffer from the Greenland coast, per the concept's buffer clause. You lose "shelf waters," you gain a manometric trend that means what it says. This is the option that fits the concept's "basin-scale open-ocean averages are robust."

**Option B - model the land source explicitly rather than buffering it.** The concept permits this ("or models them explicitly"). CMR surfaced a product built for exactly this: `HOMAGE_GGFO_MSC_CRI_SALGRD_v01` (`C3560326548-POCLOUD`, DOI `10.5067/HMOGD-4JM01`) - monthly solutions of the sea level equation giving relative sea level, geoid height and radial deformation with the contributions separated by land source domain, Greenland among them. That gives you a modeled near-field Greenland fingerprint to remove or to compare against. Caveat, from its own abstract: it is derived from these same CRI mascons and "inherits all processing steps from those fields," so the leakage is inherited, not solved. **No installed concept covers HOMaGE** - I am reporting it from CMR metadata only, and it would need its own verification before you lean on it.

**Option C - reframe the question to what the shelf can support.** If the science interest is genuinely the shelf (freshwater delivery, boundary current), GRACE is the wrong instrument at that scale and the answer is a different observing system, not a better mask.

## If you want the shelf box computed anyway

It is your call, and I'll run it if you say so and lift the no-analysis constraint. These are the conditions that would have to travel with the result, and I would not report the number without them:

- Average at **mascon scale** using the shipped mascon-ID grid, not by averaging 0.5 deg cells; report how many independent mascons the box actually contains (I expect 1-3).
- Use the **CRI** collection; state the variant loaded and never re-apply the pre-applied GIA correction. **Name the GIA model** from the product metadata beside the trend.
- Handle GRACE-FO's month gaps inside 2019-2024 explicitly rather than bridging them silently.
- Fit the trend and the monthly climatology in **one joint least-squares fit**, not deseasonalize-then-fit. Over 6 complete years the sequential recipe biases the slope by a known factor (`knowledge/podaac/gotchas/ecco-trend-deseasonalize-jointly.md`, stable, human-reviewed 2026-09-04 - written against ECCO series, but the algebra is a property of monthly sampling, not of ECCO).
- Attach an **effective-sample-size-corrected CI**, never a textbook OLS error bar (`knowledge/podaac/gotchas/ecco-trend-without-effective-n.md`, stable, severity high, human-reviewed 2026-09-04; same scope note). Read fairly: that concept's calibration reports 92-95% coverage only for series of 120+ months, and materially worse below that. At 72 months, even the corrected interval undercovers - say so rather than presenting it as exact.
- Quote the per-mascon formal uncertainty, **and state that it excludes leakage and GIA-model error**, which the dataset concept says exceed it regionally. Do not shrink the regional error by sqrtN.
- Declare the bookkeeping the budget-closure convention requires before any comparison to altimetry or steric: GIA treatment, reference frame, atmospheric-pressure/inverse-barometer convention, effective smoothing, matching period.
- Label the headline as what it is: a mass trend over a sub-mascon coastal box, not separable from Greenland ice-sheet leakage.

## Provenance and gaps

Concepts consulted and cited: `knowledge/podaac/gotchas/grace-coastal-leakage.md`, `knowledge/podaac/datasets/grace-fo-mascons.md`, `knowledge/podaac/gotchas/grace-gia-correction.md`, `knowledge/podaac/conventions/sea-level-budget-closure.md`, `knowledge/podaac/connectors/earthdata-mcp.md` (draft), `knowledge/podaac/gotchas/ecco-trend-deseasonalize-jointly.md`, `knowledge/podaac/gotchas/ecco-trend-without-effective-n.md`, `core/knowledge/conventions/smell-test-ranges.md` (checked; it carries no anchor for a regional manometric trend). Skills followed: `core:start`, `core:consult-knowledge`, `ocean-science:sea-level`, `ocean-science:sea-level-analysis`, `hydrology:load-grace-tws` (its search-before-fetch step, which is why the CMR granule check ran), `core:analysis-review`.

Two gaps worth an ingest issue for the steward: (1) the two trend gotchas are scoped as ECCO dataset gotchas, but the joint-fit and effective-n rules are sampling properties that apply to any monthly series including GRACE - there is no product-neutral trend concept to cite; (2) no installed concept covers the HOMaGE GRD product, which is the natural tool for the "model the land source explicitly" branch of the leakage gotcha's own correct-approach clause.

Unrelated to this task, but flagged since the session reported it: the claude.ai Google Calendar and Mermaid Chart connectors are unauthorized and can't be authorized from this non-interactive session - you'd do that in your claude.ai connector settings.

Run: 22 turns, 221s, cost $1.37, is_error=False
