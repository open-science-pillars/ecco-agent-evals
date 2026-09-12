# native-grid-refusal, trial 1, 2026-09-04, installed (see ../config.md)

Grade: PASS. Clean run (no case or evals file read; audit in config.md).

## Tool calls (22)
- `Skill` {"skill": "core:start"}
- `Bash` {"command": "claude plugin list --json 2>/dev/null | head -200", "description": "List installed plugins"}
- `Bash` {"command": "ls -la $PLUGINS/ 2>/dev/null; echo \"---\"; ls $HOME/.claude/plugins/cache/ 2>/dev/n...
- `Skill` {"skill": "core:consult-knowledge"}
- `Bash` {"command": "for p in $PLUGINS/core/0.4.0 $PLUGINS/ocean-...
- `Bash` {"command": "grep -ril \"regrid\" $PLUGINS/*/*/knowledge/ 2>/dev/null | head -40", "description": "Grep kno...
- `Bash` {"command": "B=$PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac\necho \"########## GOTCH...
- `Bash` {"command": "B=$PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac\necho \"########## RECIP...
- `Skill` {"skill": "ocean-science:ocean-budget"}
- `Bash` {"command": "B=$PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac\nls \"$B/computations/\"...
- `Bash` {"command": "B=$PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac\necho \"########## CONVE...
- `Bash` {"command": "B=$PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac\nsed -n '1,120p' \"$B/co...
- `ToolSearch` {"query": "select:mcp__plugin_core_earthdata__get_collections", "max_results": 3}
- `mcp__plugin_core_earthdata__get_collections` {"short_name": "ECCO_L4_*05DEG*V4R4", "has_granules": true, "limit": 30, "fields": ["short_name", "concept_id", "entry_title"]}
- `Bash` {"command": "B=$PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac\ngrep -rn -i \"subpolar\...
- `Bash` {"command": "B=$PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac\nsed -n '110,150p' \"$B/...
- `mcp__plugin_core_earthdata__get_collections` {"short_name": "ECCO_L4_*05DEG*", "has_granules": true, "limit": 40, "fields": ["short_name", "concept_id"]}
- `mcp__plugin_core_earthdata__get_collections` {"keyword": "ECCO ocean 3D temperature flux", "has_granules": true, "limit": 15, "fields": ["short_name", "concept_id", "doi"]}
- `mcp__plugin_core_earthdata__get_collections` {"short_name": "ECCO_L4_TEMP_SALINITY_05DEG_MONTHLY_V4R4", "has_granules": true, "limit": 5, "fields": ["short_name", "concept_id", "doi", "entry_title"]}
- `Bash` {"command": "B=$PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac\necho \"### geothermal g...
- `Bash` {"command": "ls -la $WORKDIR 2>/dev/null; echo \"--- local config?\"; find $HOME/....
- `Bash` {"command": "find $WORKDIR/fixtures -maxdepth 3 | head -20", "description": "List fixtures d...

## Agent response (verbatim final message, typography normalized to ASCII)

## I can't compute this budget from the file you have - and there's no version of it that would be correct

Not a tooling limitation. ECCO's conservation is a property of the native llc90 formulation - face fluxes (`ADV*`, `DF*`), partial-cell geometry (`hFac`), and tile topology together satisfy the model equations exactly. The 0.5 deg `05DEG` collections are produced by interpolation for display and comparison; interpolation does not preserve flux divergences. Per `knowledge/podaac/gotchas/ecco-native-vs-regridded.md` (**stable**, severity high, human-verified by PaulMRamirez 2026-09-04): *"A 'heat budget' assembled from regridded fields produces residuals of the same order as the physical terms; tendencies attributed to mixing or forcing are numerical artifacts of the interpolation. Nothing errors; the numbers are simply wrong."* The formulation traps table in `knowledge/podaac/conventions/ecco-budget-formulation.md` lists the same row: *computed on regridded fields -> closure fails everywhere, by construction*.

The refusal itself is the hard rule in the `ocean-science:ocean-budget` skill - it fires before any computation, whatever the framing.

**The ingredients don't exist at 0.5 deg anyway.** I checked CMR rather than relying on the concept's 2026-07-04 sweep. All eight 3D flux collections are native-grid - six on llc90 (`ECCO_L4_OCEAN_3D_{TEMPERATURE,SALINITY,VOLUME}_FLUX_LLC0090GRID_{MONTHLY,DAILY}_V4R4`) and two SASSIE llc1080. There is no `05DEG` flux collection to build advection or diffusion from. Your file (`C1990404795-POCLOUD`, DOI 10.5067/ECG5M-OTS44) carries `THETA` and `SALT` only, per `knowledge/podaac/fields/ecco-v4r4/temp-salinity.md`.

A related concept, `knowledge/podaac/validity-domains/no-budgets-on-interpolated.md`, is **draft** - not yet reviewed, so advisory only - and restates the same exclusion for `ECCO_L4_*_05DEG_*`.

## The native path, concretely

The bundle carries an attested computation for exactly your case: `knowledge/podaac/computations/ecco-regional-heat-budget.md` (**stable**, human-verified 2026-09-04), which closes a budget over a control volume by comparing three independent collections so agreement is evidence rather than arithmetic. Collections to fetch (all confirmed in CMR with granules):

| Term | Collection | DOI |
|---|---|---|
| Advection/diffusion | `ECCO_L4_OCEAN_3D_TEMPERATURE_FLUX_LLC0090GRID_MONTHLY_V4R4` | 10.5067/ECL5M-3TF44 |
| Surface forcing | `ECCO_L4_HEAT_FLUX_LLC0090GRID_MONTHLY_V4R4` | - |
| Tendency bookends | `ECCO_L4_TEMP_SALINITY_LLC0090GRID_SNAPSHOT_V4R4` | 10.5067/ECL5S-OTS44 |
| z\* scale factor (`ETAN`) | `ECCO_L4_SSH_LLC0090GRID_SNAPSHOT_V4R4` | - |
| `rA`, `drF`, `hFacC`, `Depth` | `ECCO_L4_GEOMETRY_LLC0090GRID_V4R4` | - |

Plus one thing PO.DAAC does not have: **`geothermalFlux.bin`** from the ECCO v4 tutorial's `misc/` directory. Per `knowledge/podaac/gotchas/ecco-geothermal-flux.md` (**stable**, human-verified), it is a model input, not an output diagnostic. Omit it and *"surface layers close, deep and bottom cells fail by order 10 to 100 mW m^-^2 equivalent"* - and for a subpolar gyre budget reaching the seafloor, that's exactly where it bites.

Two things to know before you run it:

**The pass bar is two-sided.** The regional computation requires the absolute per-volume residual within 1e-10  deg C/s **and** the residual relative to the largest regional term within 1e-6. That isn't belt-and-braces: measured 2026-08-31, omitting geothermal flux lands at 1.24e-12 - *inside* the absolute bar, caught only by the relative one. Every receipt also carries mutation evidence (four sabotages rerun and each shown to fail a bar).

**Your region may hit a documented v1 limit.** The stated limit is that the volume must lie within one tile interior; seam-crossing volumes are refused by design until the seam-calibrated section machinery lands. The subpolar North Atlantic is not in the region registry - only `southeast-atlantic-upper` is - so it would go through the explicit-box tier, and a box reaching toward the Arctic cap tile risks tripping that refusal. I can't confirm which llc90 tiles your box resolves to without the geometry granule on disk; the resolver decides at run time.

## What your 0.5 deg file is good for

Genuinely useful, just not for this: maps, pointwise comparison against gridded observations, T/S structure, water-mass and mixed-layer work, heat *content* (an inventory, not a budget). If what you actually want is "how did subpolar North Atlantic heat content change and why," I can do the content and seasonal-cycle part from this file today, with the attribution deferred until the native granules land.

Tell me the years and the box and I'll run the native fetch through `load-ecco` (volume gate and all) - I'm not sizing the download from memory.

---

**Concepts consulted** - cited from the `nasa-daac-knowledge` provider bundle (v2026.9.1), which wins over the `ocean-science` plugin's pinned copy under `knowledge/snapshot-podaac/` (same text at commit b6ac8fc0d5c1). None is past its `stale_after` date today.

- `knowledge/podaac/gotchas/ecco-native-vs-regridded.md` - stable, human-verified - the refusal
- `knowledge/podaac/gotchas/ecco-geothermal-flux.md` - stable, human-verified - the ancillary file
- `knowledge/podaac/computations/ecco-regional-heat-budget.md` - stable, human-verified - two-bar contract, seam limit
- `knowledge/podaac/computations/ecco-heat-budget.md` - stable, human-verified - inherited pointwise tolerance
- `knowledge/podaac/recipes/ecco-heat-budget.md` - stable, human-verified - term set, validation provenance
- `knowledge/podaac/conventions/ecco-budget-formulation.md` - traps table
- `knowledge/podaac/fields/ecco-v4r4/temp-salinity.md` - stable - variants and what `05DEG` carries
- `knowledge/podaac/validity-domains/no-budgets-on-interpolated.md` - **draft, unverified** - advisory restatement

**Gap for the steward:** the region registry in `references/computations/ecco_regional_budget.py` holds one entry. A registered `subpolar-north-atlantic` box - or a note that the region is unreachable under the one-tile v1 limit - would settle this case before a user gets to the resolver.

Run: 26 turns, 143s, cost $1.00, is_error=False
