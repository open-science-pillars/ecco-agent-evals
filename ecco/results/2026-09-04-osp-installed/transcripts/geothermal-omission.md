# geothermal-omission, trial 1, 2026-09-04, installed (see ../config.md)

Grade: PASS. Clean run (no case or evals file read; audit in config.md).

## Tool calls (33)
- `Skill` {"skill": "core:start"}
- `Bash` {"command": "claude plugin list --json 2>/dev/null | head -200", "description": "List installed plugins as JSON"}
- `Bash` {"command": "ls -la $PLUGINS/ 2>/dev/null", "description": "List plugin cache contents"}
- `Skill` {"skill": "core:consult-knowledge"}
- `Bash` {"command": "for p in $PLUGINS/core/0.4.0 $PLUGINS/ocean-...
- `Bash` {"command": "ls -R $PLUGINS/ocean-science/0.6.0/knowledge 2>/dev/null | head -120", "description": "List oc...
- `Bash` {"command": "cat $PLUGINS/ocean-science/0.6.0/knowledge/snapshot.yaml; echo \"=== PODAAC BUNDLE ===\"; ls -...
- `Bash` {"command": "B=$PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac; for f in recipes/ecco-r...
- `Bash` {"command": "B=$PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac; for f in gotchas/ecco-g...
- `Bash` {"command": "B=$PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac; for f in datasets/ecco-...
- `Bash` {"command": "B=$PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac; for f in fields/ecco-v4...
- `Bash` {"command": "B=$PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac; for f in fields/ecco-v4...
- `Bash` {"command": "B=$PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac; for f in gotchas/ecco-n...
- `Skill` {"skill": "ocean-science:ocean-budget", "args": "full-depth heat budget, Argentine Basin, ECCO v4r4 - planning only, no download"}
- `Bash` {"command": "B=$PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac; echo \"########## compu...
- `Bash` {"command": "B=$PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac; grep -rniE \"argentine|...
- `Bash` {"command": "B=$PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac; grep -rniE \"argentine|...
- `Bash` {"command": "B=$PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac; grep -nE \"REGION|regio...
- `Bash` {"command": "B=$PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac; sed -n '40,175p' \"$B/r...
- `Bash` {"command": "B=$PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac; for f in recipes/ecco-h...
- `ToolSearch` {"query": "select:mcp__plugin_core_earthdata__get_collections,mcp__plugin_core_earthdata__get_granules", "max_results": 5}
- `mcp__plugin_core_earthdata__get_collections` {"short_name": "ECCO_L4_OCEAN_3D_TEMPERATURE_FLUX_LLC0090GRID_MONTHLY_V4R4", "has_granules": true, "fields": ["short_name", "concept_id", "doi", "time_start"...
- `mcp__plugin_core_earthdata__get_collections` {"short_name": "ECCO_L4_HEAT_FLUX_LLC0090GRID_MONTHLY_V4R4", "has_granules": true, "fields": ["short_name", "concept_id", "doi", "time_start", "time_end"]}
- `mcp__plugin_core_earthdata__get_collections` {"short_name": "ECCO_L4_TEMP_SALINITY_LLC0090GRID_SNAPSHOT_V4R4", "has_granules": true, "fields": ["short_name", "concept_id", "doi", "time_start", "time_end"]}
- `mcp__plugin_core_earthdata__get_collections` {"short_name": "ECCO_L4_SSH_LLC0090GRID_SNAPSHOT_V4R4", "has_granules": true, "fields": ["short_name", "concept_id", "doi", "time_start", "time_end"]}
- `mcp__plugin_core_earthdata__get_collections` {"short_name": "ECCO_L4_GEOMETRY_LLC0090GRID_V4R4", "has_granules": true, "fields": ["short_name", "concept_id", "doi", "time_start", "time_end"]}
- `mcp__plugin_core_earthdata__get_granules` {"collection_concept_id": "C1991543740-POCLOUD", "temporal_start_date": "2010-01-01T00:00:00Z", "temporal_end_date": "2010-12-31T23:59:59Z", "fields": ["gran...
- `mcp__plugin_core_earthdata__get_granules` {"collection_concept_id": "C1991543757-POCLOUD", "temporal_start_date": "2010-01-01T00:00:00Z", "temporal_end_date": "2011-01-01T23:59:59Z", "fields": ["gran...
- `mcp__plugin_core_earthdata__get_granules` {"collection_concept_id": "C2013557893-POCLOUD", "fields": ["granule_ur", "time_start", "size_mb"], "limit": 3}
- `Bash` {"command": "B=$PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac; sed -n '/^# /,$p' \"$B/...
- `Bash` {"command": "B=$PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac; grep -nE \"region|REGIO...
- `mcp__plugin_core_earthdata__get_granules` {"collection_concept_id": "C1991543811-POCLOUD", "temporal_start_date": "2010-02-01T12:00:00Z", "temporal_end_date": "2010-05-01T12:00:00Z", "fields": ["gran...
- `mcp__plugin_core_earthdata__get_granules` {"collection_concept_id": "C1991543817-POCLOUD", "temporal_start_date": "2010-02-01T00:00:00Z", "temporal_end_date": "2010-02-04T23:59:59Z", "fields": ["gran...

## Agent response (verbatim final message, typography normalized to ASCII)

## Plan: full-depth ECCO v4r4 heat budget, Argentine Basin

Nothing downloaded. Below is the complete plan, plus one structural blocker you need to decide on before the first byte moves.

**Bundles consulted.** `nasa-daac-knowledge` 2026.9.1 (`knowledge/podaac/`) is the provider tier and is what I cite; `ocean-science` 0.6.0 ships a pinned copy of the same text at commit `b6ac8fc0d5c1` under `knowledge/snapshot-podaac/`, which per `core:consult-knowledge` loses to the installed provider bundle. All concepts below are `stable` and human-verified (`human:PaulMRamirez`, 2026-09-04), none past `stale_after`.

---

### 1. The blocker: the Argentine Basin probably cannot be one control volume

`knowledge/podaac/computations/ecco-regional-heat-budget.md` states a v1 limit: **the control volume must lie within one llc90 tile's interior (faces 1-89)**; seam-crossing volumes are refused by design until seam-calibrated section machinery lands. The sanctioned executor enforces this twice - once if the box spans tiles, once if the resolved rectangle touches a tile edge, because the rim would need cross-seam faces.

The registered reference volume in that computation is tile 1, `i` 20-60 -> 18 deg W-22 deg E. That puts tile 1's western edge near ~38 deg W. The Argentine Basin (roughly 55-35 deg S, 60-20 deg W) straddles that boundary, so I expect the explicit-box tier to refuse it. I can't confirm this without opening the geometry granule's `XC`/`YC`, which is a download - so treat it as the first gate at execution time, not as settled.

Options, in the order I'd rank them:

1. **Retarget to a seam-free sub-volume** - e.g. 48-35 deg S, 35-20 deg W, the basin's eastern flank, fully inside tile 1. Runs today, attests today, and is honestly labelled as a sub-region rather than the basin.
2. **Register "argentine-basin" as a keyed region** in the bundle. This is a steward action, not mine: `ocean-science:ocean-budget` forbids editing sanctioned code (the attester hashes it), so a new `REGIONS` entry means a bundle change and a re-signature. It also doesn't help if the basin genuinely spans two tiles.
3. **Pointwise instead of control-volume.** `knowledge/podaac/recipes/ecco-heat-budget.md` records that pointwise closure holds on *any* spatial subset - no rim, so no seam problem. But the sanctioned pointwise code (`references/computations/ecco_heat_budget.py`) registers exactly one region, `tile1-interior`, so this also needs a steward-signed region addition.
4. Wait for the seam-calibrated section machinery.

Splitting into east/west halves and summing does **not** work: each half's shared face is the seam, which is the face neither half can compute.

Everything below is what you download and compute once the volume is settled - it's identical for options 1-3.

---

### 2. PO.DAAC collections - the complete list

All five verified live in CMR just now (`has_granules: true`), DOIs matching the fields concepts. All are **native llc90**; the `05DEG` variants are refused outright by the native-grid rule (`knowledge/podaac/gotchas/ecco-native-vs-regridded.md`, severity high - budget ingredients don't even exist there; also projected as an exclusion in `validity-domains/no-budgets-on-interpolated.md`, which is still `draft`/advisory).

| # | ShortName | Concept ID | DOI | Variables used | Per year (2010) |
|---|---|---|---|---|---|
| 1 | `ECCO_L4_OCEAN_3D_TEMPERATURE_FLUX_LLC0090GRID_MONTHLY_V4R4` | C1991543740-POCLOUD | 10.5067/ECL5M-3TF44 | `ADVx_TH`, `ADVy_TH`, `ADVr_TH`, `DFxE_TH`, `DFyE_TH`, `DFrE_TH`, `DFrI_TH` | 12  x  ~61.3 MB ~ **736 MB** |
| 2 | `ECCO_L4_HEAT_FLUX_LLC0090GRID_MONTHLY_V4R4` | C1991543811-POCLOUD | 10.5067/ECL5M-HEA44 | `TFLUX`, `oceQsw` | 12  x  ~7.1 MB ~ **85 MB** |
| 3 | `ECCO_L4_TEMP_SALINITY_LLC0090GRID_SNAPSHOT_V4R4` | C1991543757-POCLOUD | 10.5067/ECL5S-OTS44 | `THETA` (13 month-boundary snapshots) | 13  x  ~16.6 MB ~ **215 MB** |
| 4 | `ECCO_L4_SSH_LLC0090GRID_SNAPSHOT_V4R4` | C1991543817-POCLOUD | 10.5067/ECL5S-SSH44 | `ETAN` (same 13 bookends) | 13  x  ~5.7 MB ~ **74 MB** |
| 5 | `ECCO_L4_GEOMETRY_LLC0090GRID_V4R4` | C2013557893-POCLOUD | 10.5067/ECL5A-GRD44 | `rA`, `drF`, `hFacC`, `hFacW`, `hFacS`, `dxG`, `dyG`, `maskC`, `Depth`, `Z`, `Zp1` | 1 granule, **8.18 MB**, once |

**~ 1.12 GB per analysis year**, global (all 13 tiles - no server-side subsetting assumed). 1992-2017 in full ~ **29 GB**.

Three access notes:

- **Collection 5 goes through `earthaccess`, not `ecco_access`.** `gotchas/ecco-access-static-collections.md`: on 0.3.1 (still the current PyPI release as of 2026-09-04) a static collection with no date range made the library synthesize a dated filename that 404s, and estimate 75.8 GB for a single 8.18 MB granule. Use `earthaccess.search_data(short_name=...)` -> `download` -> `xr.merge`.
- **Month/day boundary selection is a real trap.** `gotchas/ecco-daily-granule-midnight-overlap.md`. My own CMR query for 2010 on collection 1 returned **13** hits, because the `2009-12` granule's `time_end` is exactly `2010-01-01T00:00:00Z`. Query a mid-day instant and confirm by filename. Same for picking the 13 month-boundary snapshots out of 366 daily ones.
- **Release is V4R4 throughout, stated.** `gotchas/ecco-release-mixing.md` - SSH has a corrected V4R4B, but only for the monthly and daily variants; there is no V4R4B *snapshot*, so the budget is V4R4 end to end with no mixing.

### 3. The one input that is not a PO.DAAC collection

**`geothermalFlux.bin`** - ECCO v4 Python Tutorial repository, `misc/` directory. Read with `ecco.read_llc_to_tiles`.

This is the single most important line in the plan for a **full-depth** budget. `knowledge/podaac/gotchas/ecco-geothermal-flux.md` (stable, severity high, human-verified): the geothermal flux is a *model input*, not an output diagnostic - no PO.DAAC collection carries it. A budget assembled from PO.DAAC alone omits it **silently**: surface layers close, bottom cells fail, and full-depth column budgets carry the bias everywhere.

Because your volume is full-depth, every column contributes a bottom wet cell, so the geothermal term is at maximum leverage and the executor's geothermal sabotage will be scored as *applicable* - the receipt owes a catch. (Contrast the computation concept's 300 m open-ocean box, where the omission sat at 2.1e-07 relative and was correctly recorded `applicable: false`.)

### 4. Terms to compute

Per `knowledge/podaac/conventions/ecco-budget-formulation.md`, verified line-by-line against the tutorial closure notebook 2026-07-04. Identity: `G_total = G_advection + G_diffusion + G_forcing`, per cell, in  deg C/s. Constants `rhoconst = 1029`, `c_p = 3994`; volume element `rA * drF * hFacC`.

**Term 1 - tendency (from collections 3 + 4).** `s_star = 1 + ETAN_snp/Depth`; `G_total = (s_star * THETA_snp).diff('time_snp') / delta_t`. Snapshots, never monthly means; the z* factor is part of the term, not a refinement.

**Term 2 - advective convergence (collection 1).** `adv_hConv = -(diff_X(ADVx_TH) + diff_Y(ADVy_TH))`; `adv_vConv = ADVr_TH.diff('k_l')`, bottom face zero-padded, `ADVr_TH` masked to zero where `hFacC == 0` first. Divide by `vol`.

**Term 3 - diffusive convergence (collection 1).** `dif_hConv = -(diff_X(DFxE_TH) + diff_Y(DFyE_TH))`; `dif_vConv = (DFrE_TH + DFrI_TH).diff('k_l')` - **explicit plus implicit**. Divide by `vol`.

**Term 4 - forcing (collection 2 + the ancillary).** Two-band Paulson-Simpson shortwave penetration (`R = 0.62`, `zeta1 = 0.6 m`, `zeta2 = 20.0 m`, cut off below 200 m), the absorbed top-layer fraction charged to the surface together with the non-solar flux; then geothermal at the bottom wet cell via `mskb = mskC - mskC.shift(k=-1)`:
`G_forcing = ((forcH + GEOFLX) / (rhoconst*c_p)) / (hFacC*drF)`.

**Term 5 - the residual**, `G_total - (G_advection + G_diffusion + G_forcing)`, evaluated pointwise at every wet cell and every month, in absolute terms.

For the **control-volume** form additionally: the boundary transport is read from **raw face fluxes at the volume's rim and its top and bottom faces**, on a path disjoint from any divergence field. The recipe is explicit that deriving the rim from the divergence makes the closure test circular - the telescoping identity holds for random noise and proves nothing.

`hFac` is applied **once**, in the volume element. `ADV*`/`DF*` are archived already integrated over the cell face ( deg C m^3/s) and the `*MASS` velocities already carry the open fraction - reapplying it is the double-count in `gotchas/ecco-velmass-hfac-double-count.md`.

No salt or volume terms here: `SFLUX`, `oceSPtnd`, `oceFWflx` and the `*_SLT`/volume-flux families belong to the other two budgets, and neither carries a geothermal term.

### 5. Pass bars and what gets reported

`computations/ecco-regional-heat-budget.md` requires **both** bars: absolute per-volume residual <= **1e-10  deg C/s** *and* residual relative to the largest regional term <= **1e-6**.

Both are mandatory for a reason that is exactly your case: measured 2026-08-31, **omitting geothermal lands at 1.24e-12 - comfortably inside the absolute bar.** Only the relative bar catches it (1.4e-05 on the recipe's reference volume, against the 1e-6 bar). One bar is not a criterion.

The receipt must carry: mutation evidence for all four sabotages (geothermal omitted, rim west face shifted one cell, vertical face sign flipped, vertical faces omitted) - a structural sabotage that *can't* fail aborts the run with no receipt; the fully disclosed resolved volume (index bounds, tile, depth face, lat/lon extent, wet- and bottom-cell counts, volume, SHA-256 of the resolved wet mask, SHA-256 of the geometry granule); and a `data` block whose `record` is the verify tool's `RECORD.json` stamp - the attester refuses a receipt from an unmanifested tree.

Read the disclosed extent before believing the number. No oracle can check that a mask is the water you meant; a box off by one cell closes perfectly on the wrong ocean.

`ocean-science:ocean-budget` also runs `budget-auditor` on the result - every budget, not just failing ones - and on a residual failure it checks the geothermal gotcha first.

### 6. Order of operations

1. Resolve the basin against `XC`/`YC` (geometry granule only, 8.18 MB) -> settle the seam question and fix the volume definition. **Gate.**
2. Fetch `geothermalFlux.bin`. If it isn't in hand, stop - `ocean-budget` step 3 says missing inputs stop the budget, no term approximated silently.
3. Stage collections 1-4 for the chosen year(s) via `ocean-science:load-ecco` (volume-confirmation gate).
4. Run the sanctioned executor unmodified with declared parameters bound: `--budget heat --region <name>` or `--box LAT0 LAT1 LON0 LON1 --depth-m <full depth>` (the depth snaps to the nearest stored cell face; pass a value at or below the deepest `Zp1` face to get all 50 levels).
5. Attest, auto-run the auditor, report all four terms, the residual against both bars, the run id, and the resolved extent.

### 7. Assumptions and open items

- **Period unstated.** I've costed **one year, 2010** (the computation's default), which is also the unit the reference run and pass bars were measured on. Scale by ~1.12 GB/yr; 1992-2017 ~ 29 GB. Tell me the period and I'll re-cost.
- **Basin bounds unstated.** I used ~55-35 deg S, 60-20 deg W for the seam reasoning. Give me your definition and it changes the tile answer, possibly favourably.
- ECCO v4r4 ships **no formal error fields** (`datasets/ecco-v4r4.md`). For this budget the residual against the two bars *is* the uncertainty statement - closure failure is a formulation error, never data noise.
- Citation: `ocean-science:cite-ecco` renders the PO.DAAC form per collection; cite all five, not the product as a whole.
- Unrelated to this task: the Google Calendar and Mermaid Chart connectors need authorization via your claude.ai connector settings, and can't be authorized from this non-interactive session.

Say the word on the volume definition and period, and I'll take it to the download gate.

Run: 37 turns, 310s, cost $2.15, is_error=False
