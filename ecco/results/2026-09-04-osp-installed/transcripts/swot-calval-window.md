# swot-calval-window, trial 1, 2026-09-04, installed (see ../config.md)

Grade: PASS. Clean run (no case or evals file read; audit in config.md).

## Tool calls (20)
- `Skill` {"skill": "core:start"}
- `Bash` {"command": "claude plugin list --json 2>/dev/null | head -200", "description": "List installed plugins as JSON"}
- `Bash` {"command": "ls -la $PLUGINS/ 2>/dev/null; echo \"---CWD---\"; ls -la $HOME/.claude/jobs/7612e702...
- `Skill` {"skill": "core:consult-knowledge"}
- `Bash` {"command": "for p in $PLUGINS/core/0.4.0 $PLUGINS/ocean-...
- `Bash` {"command": "grep -ril \"swot\" $PLUGINS/*/*/knowledge 2>/dev/null | sort", "description": "Find SWOT-relat...
- `Bash` {"command": "cd $PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac; echo \"########## data...
- `Bash` {"command": "cd $PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac; echo \"########## gotc...
- `Skill` {"skill": "ocean-science:load-swot"}
- `Bash` {"command": "ls $PLUGINS/ocean-science/0.6.0/knowledge/; echo \"---\"; sed -n '1,80p' $HOME/.clau...
- `Bash` {"command": "cat $PLUGINS/ocean-science/0.6.0/skills/swot/SKILL.md 2>/dev/null | head -120; echo \"=== loca...
- `ToolSearch` {"query": "select:mcp__plugin_core_earthdata__get_granules,mcp__plugin_core_earthdata__get_collections", "max_results": 3}
- `mcp__plugin_core_earthdata__get_granules` {"collection_concept_id": "C3233942270-POCLOUD", "temporal_start_date": "2023-03-30T00:00:00Z", "temporal_end_date": "2023-07-10T23:59:59Z", "spatial_wkt_geo...
- `mcp__plugin_core_earthdata__get_granules` {"collection_concept_id": "C2799465428-POCLOUD", "temporal_start_date": "2023-03-30T00:00:00Z", "temporal_end_date": "2023-07-10T23:59:59Z", "spatial_wkt_geo...
- `mcp__plugin_core_earthdata__get_granules` {"collection_concept_id": "C3233942270-POCLOUD", "temporal_start_date": "2023-07-21T00:00:00Z", "temporal_end_date": "2024-03-31T23:59:59Z", "spatial_wkt_geo...
- `mcp__plugin_core_earthdata__get_granules` {"collection_concept_id": "C3233942270-POCLOUD", "temporal_start_date": "2023-03-01T00:00:00Z", "temporal_end_date": "2023-03-29T23:59:59Z", "spatial_wkt_geo...
- `mcp__plugin_core_earthdata__get_granules` {"collection_concept_id": "C3233942270-POCLOUD", "temporal_start_date": "2023-07-11T00:00:00Z", "temporal_end_date": "2023-07-20T23:59:59Z", "spatial_wkt_geo...
- `mcp__plugin_core_earthdata__get_granules` {"collection_concept_id": "C2799465428-POCLOUD", "temporal_start_date": "2023-07-21T00:00:00Z", "temporal_end_date": "2024-03-31T23:59:59Z", "spatial_wkt_geo...
- `mcp__plugin_core_earthdata__get_granules` {"collection_concept_id": "C3233942270-POCLOUD", "temporal_start_date": "2023-03-01T00:00:00Z", "temporal_end_date": "2024-03-31T23:59:59Z", "spatial_wkt_geo...
- `Bash` {"command": "cd $PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac; ls recipes validity-do...

## Agent response (verbatim final message, typography normalized to ASCII)

## Orientation

Installed OSP plugins (from `claude plugin list --json`): **core 0.4.0**, **ocean-science 0.6.0**, **hydrology 0.3.0**, **nasa-daac-knowledge 2026.9.1-58dd8445099b** - all enabled, no `errors`. The Earthdata MCP connector is configured and reachable (I ran live CMR searches through it). No `ocean-science.local.md` in this working directory, so **no volume-gate threshold is configured**.

Because the provider bundle `nasa-daac-knowledge` is installed, I cite its PO.DAAC concepts rather than the pinned copies under `ocean-science/0.6.0/knowledge/snapshot-podaac/` (same text at commit `b6ac8fc0d5c1`, per `snapshot.yaml`).

## The request hits a known trap before anything else

`knowledge/podaac/gotchas/swot-calval-orbit-phases.md` (**stable**, human-reviewed - `verified: human:PaulMRamirez, 2026-09-04`; `stale_after` 2027-01-04, so current) fires on any range touching 2023, and your window straddles the transition:

- SWOT flew a **1-day repeat cal/val orbit** (calibration phase 2023-03-30 -> 2023-07-10, cycles in the 400-500s), then the **21-day science orbit from 2023-07-21**, cycles restarting at 001.
- Wrong-result mode 1: a single time series spanning July 2023 **mixes incompatible sampling regimes and aliases the orbit change into apparent variability**.
- Wrong-result mode 2: a cal/val-era query against a Version C collection returns empty and reads as "no data" - the data is in the D family.

So "March 2023 through March 2024" is not one record. It is two, with a gap.

## What CMR actually holds for the Agulhas box

Region taken as 10 deg E-40 deg E, 45 deg S-30 deg S (Agulhas Current, retroflection and ring corridor). Tier: **Basic** (skill default; the dataset concept notes `height_cor_xover` and its qual flag are already present in Basic, so Basic suffices for the correction below). Read-only granule searches, no downloads:

| Window | `SWOT_L2_LR_SSH_BASIC_D` (C3233942270) | `SWOT_L2_LR_SSH_BASIC_2.0` (C2799465428) |
|---|---|---|
| 2023-03-01 -> 03-29 | **8** (all on 03-28/29, cycles 473-474) | - |
| 2023-03-30 -> 07-10 (cal/val) | **397** | **0** |
| 2023-07-11 -> 07-20 | **0** | - |
| 2023-07-21 -> 2024-03-31 (science) | **685** (cycle 001 pass 137, 2023-07-26 -> cycle 013 pass 111, 2024-03-31) | **870** |
| Full 2023-03-01 -> 2024-03-31 | **1090** | - |

The version-family trap reproduces exactly as the concept describes: **0 vs 397 granules** for the same box and cal/val window. Three further facts the numbers settle:

- **Your window really starts 2023-03-28**, not 2023-03-01 - nothing in this box before then, consistent with the D family beginning at cycle 473 (`knowledge/podaac/datasets/swot-karin.md`, family holdings probe of 2026-09-04). The 8 granules on 03-28/29 sit *before* the declared calibration-phase start of 03-30; I'd label them commissioning and either exclude them or carry them flagged separately.
- **The 11-day gap 2023-07-11 -> 07-20 is empty** - the orbit-change maneuver, matching the concept's phase boundaries.
- **Both CRIDs `PGD0_01` and `PGD0_02` appear in the returned granule names**, so the within-collection baseline drift the dataset concept warns about is live in this exact subset; the `crid` attributes of whatever is actually loaded are the only record of it.

One observation **no installed concept covers**: for the science window the C family returns 870 hits and D returns 685 over the identical box and dates. Likely differing granule footprint metadata or reprocessing scope, but it is unverified - I would not treat either count as "the number of passes" without checking footprints. Staying entirely in D is the right call anyway for family consistency across the cal/val segment.

## Loading

I did **not** download anything - this session is read-only on data files. Independently, the hard volume gate in `load-swot` would fire here: no threshold is configured locally, and 1090 Basic granules at the ~9.4 MB/granule the dataset concept records from its Gulf Stream probe is **~10 GB**. (CMR's `size_mb` field came back as 0-0.14 for these granules; that is not the file size - use the concept's measured figure, not the metadata field.) The smaller alternatives I'd offer: one segment at a time, a tighter box (e.g. the retroflection at 15-25 deg E), or a cycle subset.

When you do load: subset to the box **before** any aggregation - CMR matches whole pole-to-pole passes, and a matched pass can carry zero in-box pixels. Expect ~39% valid `ssha_karin` after flag and land gating in open ocean; that is normal, not a defect.

## The time series I would build - two, not one

**Segment A - cal/val, 1-day repeat (2023-03-30 -> 2023-07-10, ~103 days, 397 passes).**
Roughly 4 passes per day cross the box, on a *fixed, sparse* track set (passes 014, 016, 027, 001 recur in the returned names). This is a **daily time series at a few fixed swath locations**, not a regional field. What it supports: high-frequency SSH variability, the passage of Agulhas rings and meanders across those specific tracks, sub-mesoscale structure in the Unsmoothed tier, and confrontation with in-situ (Argo, tide gauges) on daily timescales. What it cannot give: a map of the region on any given day.

**Segment B - science, 21-day repeat (2023-07-26 -> 2024-03-31, cycles 001-013, 685 passes).**
Full 2-D coverage of the box each cycle (~55 passes/cycle), each location revisited ~1-2 times per 21 days. This is a **~12-point series at 21-day spacing**: per-cycle SSHA maps and a per-cycle box statistic (mean, variance, eddy kinetic energy proxy). What it supports: mesoscale eddy census, ring-shedding events, SSH variance structure across the retroflection. Temporal resolution is 21 days, so anything faster is aliased.

**The two are plotted adjacent with the gap and the regime change marked, never concatenated into one curve.** Cycle numbers must be read per phase - 475 and 001 are not on the same axis.

Before any statistic in either segment: **add `height_cor_xover`, gated by `height_cor_xover_qual`, to `ssha_karin`** (`knowledge/podaac/gotchas/swot-crossover-unapplied.md`, **stable**, human-reviewed, severity high). The correction is not pre-applied; the uncorrected field carries a spurious cross-track ramp of order +/-2.9 m against genuine mesoscale structure with std 0.17 m on the same scene. Flag gating alone does not make a regional mean safe - this is precisely the failure that would sink an Agulhas box-average series. And per the loading contract: per-swath summaries, nadir gap left intact, never interpolated across.

## What I would not claim from this

- **No seasonal cycle and no trend across the full 13 months.** The sampling regime changes mid-record; 13 months is short against Agulhas mesoscale variance regardless.
- **Uncertainty on any box-average is not `ssh_karin_uncert`.** That field is per-sample *random* noise (1-sigma) and excludes the correlated swath-scale systematics - roll, phase, timing, wet-troposphere residuals - that dominate at long cross-track wavelengths and do **not** average down over a regional mean (`datasets/swot-karin.md`, Uncertainty section). If a headline number is wanted, the systematic term has to be carried explicitly, and the Expert tier's full correction stack is the way to get at it.

## Provenance

Concepts consulted and cited, all **stable** and human-verified 2026-09-04, none past `stale_after`:
- `knowledge/podaac/datasets/swot-karin.md` - tiers, ShortNames/concept ids, family holdings, granule size, uncertainty, whole-pass search caveat, baseline drift
- `knowledge/podaac/gotchas/swot-calval-orbit-phases.md` - the phase split and version-family trap
- `knowledge/podaac/gotchas/swot-crossover-unapplied.md` - `height_cor_xover`

Skills followed: `core:start`, `core:consult-knowledge`, `ocean-science:load-swot`, `ocean-science:swot`.

**Gaps for the steward:** no installed concept covers (a) constructing a SWOT KaRIn regional SSH time series across the phase boundary - the gotcha says split, but no recipe defines the per-segment statistic; (b) the Agulhas region specifically; (c) the C-vs-D granule-count difference over an identical region and window observed above.

Two connectors in this session need authorization before use - **claude.ai Google Calendar** and **claude.ai Mermaid Chart** - via your claude.ai connector settings; neither is needed for this work.

Run: 24 turns, 186s, cost $1.12, is_error=False
