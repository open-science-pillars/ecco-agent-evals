# mht-basin-scope, trial 1, 2026-09-04, installed (see ../config.md)

Grade: PASS. Clean run (no case or evals file read; audit in config.md).

## Tool calls (15)
- `Skill` {"skill": "core:start"}
- `Bash` {"command": "claude plugin list --json 2>/dev/null | head -200", "description": "List installed plugins"}
- `Bash` {"command": "cat \"$PLUGINS/core/0.4.0/skills/consult-knowledge/SKILL.md\" 2>/dev/null", "description": "Re...
- `Bash` {"command": "for p in $PLUGINS/core/0.4.0 $PLUGINS/ocean-...
- `Bash` {"command": "cat \"$PLUGINS/ocean-science/0.6.0/skills/meridional-transport/SKILL.md\" 2>/dev/null", "descr...
- `Bash` {"command": "OS=$PLUGINS/ocean-science/0.6.0/knowledge; ls -R \"$OS\" | head -100", "description": "List oc...
- `Bash` {"command": "grep -ril -e \"RAPID\" -e \"26.5\" -e \"meridional\" -e \"heat transport\" -e \"MHT\" $HOME/.claude/plugins/cache/open-science-pillars...
- `Bash` {"command": "K=$PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac; for f in gotchas/ecco-m...
- `Bash` {"command": "K=$PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac; for f in computations/e...
- `Bash` {"command": "cat \"$PLUGINS/ocean-science/0.6.0/skills/transport-analysis/SKILL.md\"", "description": "Read...
- `Bash` {"command": "K=$PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac; echo \"===== temperatur...
- `ToolSearch` {"query": "select:mcp__plugin_core_earthdata__get_collections,mcp__plugin_core_earthdata__get_granules", "max_results": 2}
- `mcp__plugin_core_earthdata__get_collections` {"short_name": "ECCO_L4_OCEAN_3D_TEMPERATURE_FLUX_LLC0090GRID_MONTHLY_V4R4", "has_granules": true, "fields": ["concept_id", "short_name", "doi", "time_start"...
- `mcp__plugin_core_earthdata__get_granules` {"collection_concept_id": "C1991543740-POCLOUD", "temporal_start_date": "2010-01-01T00:00:00Z", "temporal_end_date": "2010-12-31T23:59:59Z", "limit": 12, "fi...
- `Bash` {"command": "P=$PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac; S=$HOME/.clau...

## Agent response (verbatim final message, typography normalized to ASCII)

## The headline

**ECCO v4r4 Atlantic MHT at 26.5 deg N for 2010: 0.666 PW - about 0.66 PW below RAPID/MOCHA's published mean of 1.33 PW.**

One caveat that has to travel with that number: **I did not compute it this session.** Your query policy rules out downloading data files and running analysis code, so I verified the inputs and read the value from the bundle's validated record rather than re-deriving it. Details below.

## The scope trap, which is the thing that would have burned you

`knowledge/podaac/gotchas/ecco-mht-basin-scope.md` (stable, severity high, human-verified by PaulMRamirez 2026-09-04, fresh until 2027-01-04): `calc_meridional_heat_trsp(ds, lat_vals=26.5)` **with no `basin_name` integrates the full latitude circle** - Atlantic + Pacific + Indian. RAPID observes the Atlantic only, which needs `basin_name="atlExt"`.

For ECCO 2010 the two numbers are:

| Scope | 2010 mean |
|---|---|
| Atlantic (`atlExt`) - RAPID-comparable | **0.666 PW** |
| Full latitude circle (no mask) | 1.098 PW = 0.666 + 0.430 (Pac) + 0.002 (Ind) |

Quoting 1.098 PW against RAPID's ~1.3 PW would look like near-agreement while actually comparing a global-circle quantity to an Atlantic-only observation - it invents agreement in one direction and hides the real Atlantic offset in the other. The full-circle value is only good as a method check: it must equal the basin sum, and it does exactly.

## What the comparison is, and isn't

Both numbers come from `knowledge/podaac/recipes/ecco-mht-26n.md` (stable, human-verified 2026-09-04), from its recorded 2026-07-04 reproducing run against live PO.DAAC monthly granules. The RAPID side is 1.33 +/- 0.40 PW from Johns et al. 2011 (doi:10.1175/2010JCLI3997.1).

Three qualifications, all load-bearing:

- **The periods differ.** RAPID's 1.33 +/- 0.40 PW is a 2004-2007 mean; 0.666 PW is a single ECCO year. The array does cover 2010, but the bundle carries no period-matched RAPID value, so this is not an overlap-matched comparison.
- **2010 is low on purpose.** It sits below the recipe's 0.8-1.4 PW multi-year band because it is the documented 2009/2010 AMOC-minimum year, and single-year means carry a wider envelope. Atlantic monthly values in 2010 span +0.09 to +1.14 PW. The recipe also notes ECCO v4 Atlantic means generally sit low of the observed mean, so a negative offset is expected, not anomalous.
- **This is a quoted spread, not a confrontation.** Per `knowledge/podaac/conventions/consistency-versus-confrontation.md` (stable, human-verified 2026-09-02), the MHT recipe cites the array without colocating against it or measuring a score - explicitly "a third and weaker kind of statement." So 0.66 PW is a difference between two published numbers, not a validated bias with an interval. The bundle's only real confrontation at 26.5 deg N is the overturning one (`computations/ecco-rapid-amoc-confrontation.md`), not heat transport. For scale: `datasets/rapid-mocha.md` puts array MHT uncertainty near +/-0.2 PW on 10-day values and says sub-0.1 PW model distinctions are beyond the method's resolution - 0.66 PW is well clear of that floor, but I'd stop short of calling it a measured disagreement.

## Inputs, verified live

`ECCO_L4_OCEAN_3D_TEMPERATURE_FLUX_LLC0090GRID_MONTHLY_V4R4` -> `C1991543740-POCLOUD`, DOI 10.5067/ECL5M-3TF44, matching `fields/ecco-v4r4/temperature-flux-3d.md`. All twelve 2010 monthly granules present (~61 MB each, ~740 MB for the year, plus the static geometry granule). Native llc90 only - no interpolated variant exists, and `gotchas/ecco-native-vs-regridded.md` forbids transports on regridded fields anyway.

## If you want it computed for real

Lift the no-code constraint and the path is: `load-ecco` for the flux collection + geometry, then `ecco_v4_py.calc_meridional_heat_trsp(..., lat_vals=26.5, basin_name="atlExt")` - the advective flux diagnostics (`ADVx_TH`/`ADVy_TH`) are preferred because they already carry bolus and sub-monthly covariance, which a monthly v x theta reconstruction loses. Worth knowing: the attested computation `computations/ecco-mht-26n.md` is still **draft** - a stub awaiting extraction from the `transport_analysis` golden - so the recipe, not a receipt-emitting computation, currently owns these anchors. Once that lands, its attester is specified to refuse a global-circle value presented against RAPID, making the scope trap above a mechanical check rather than a human one.

Also, one housekeeping note unrelated to this task: the claude.ai Google Calendar and Mermaid Chart connectors need authorization before their tools work, and this session can't run the OAuth flow - you'd do that from your claude.ai connector settings.

Run: 17 turns, 114s, cost $0.99, is_error=False
