# geothermal-omission, trial 1, 2026-08-30, bundle-on (see ../config.md)

Grade: PASS. Clean run (no case-definition contamination).

## Agent response (abridged only by layout; content verbatim)

**Parse-back**: property = heat; domain = Argentine Basin, western
South Atlantic, nominally 35S to 50S, 70W to 20W (exact native-grid
mask shown before computing); depth = full water column, all 50 levels;
period = unspecified, single calendar year proposed first (12 monthly
means bracketed by 13 month-boundary snapshots).

**The one non-negotiable rule first**: native llc90 only; no `05DEG`
collection appears anywhere in this plan (the interpolated product does
not conserve, and the 3D flux ingredients do not exist there;
`knowledge/gotchas/ecco-native-vs-regridded.md`).

**Collections to download (exact ShortNames, all V4R4):**
1. ECCO_L4_GEOMETRY_LLC0090GRID_V4R4 (static, ~8.6 MB; fetched via
   earthaccess, not ecco_access, per the recorded static-collection
   quirk; merged into every dataset).
2. ECCO_L4_OCEAN_3D_TEMPERATURE_FLUX_LLC0090GRID_MONTHLY_V4R4 (ADVx_TH,
   ADVy_TH, ADVr_TH; DFxE_TH, DFyE_TH, DFrE_TH, DFrI_TH).
3. ECCO_L4_HEAT_FLUX_LLC0090GRID_MONTHLY_V4R4 (TFLUX, oceQsw).
4. ECCO_L4_TEMP_SALINITY_LLC0090GRID_SNAPSHOT_V4R4 (THETA bookends;
   monthly means never used as bookends).
5. ECCO_L4_SSH_LLC0090GRID_SNAPSHOT_V4R4 (ETAN for the z* factor;
   release note: the whole budget is V4R4 throughout, stated so no
   release mixing occurs).

**Plus one mandatory non-PO.DAAC ancillary**: `geothermalFlux.bin` from
the ECCO v4 Python Tutorial repository's misc/ directory. No PO.DAAC
collection carries the geothermal forcing; a full-depth budget
assembled from the archive alone omits it silently and bottom cells
fail closure by order 10 to 100 mW m-2 equivalent; for a full-depth
Argentine Basin budget this term is not optional
(`knowledge/gotchas/ecco-geothermal-flux.md`). Read with
`read_llc_to_tiles`, masked to the bottom wet cell.

**Terms** (formulation authority
`skills/ecco/references/budget-formulation.md`; constants rhoconst
1029, c_p 3994; volume element rA x drF x hFacC, never applied again to
MASS/flux variables): (1) tendency from sTHETA = THETA_snap x
(1 + ETAN_snap/Depth) differenced across bookends; (2) advective
convergence with tile-aware operators, ADVr zero-padded and dry-masked;
(3) diffusive convergence with DFrE + DFrI (implicit never omitted);
(4) forcing with two-band shortwave penetration (R 0.62, zeta 0.6/20 m,
200 m cutoff) plus GEOFLX at the bottom wet cell; (5) residual against
the attested pass bar (`knowledge/computations/ecco-heat-budget.md`:
max 1e-10, p999 1e-11 degC/s, absolute and pointwise), diagnosed via
the traps table, never averaged away.

**Region and closure semantics**: mask from XC/YC, never (j, i);
pointwise closure asserted per cell; a domain-integrated statement for
this open basin requires the lateral boundary transports as their own
term, reported broken out.

**Safeguards**: load-ecco workflow with exact ShortNames and the 2 GB
volume gate; budget-auditor reviews the result even if green;
uncertainty framing per the dataset concept (no formal error fields;
the closure tolerance is the identity's own uncertainty statement).

**Decision requested**: the time period (2010 proposed first).

## Consulted paths (as reported by the agent)

23 plugin paths spanning skills (ecco, ocean-budget, budget-closure,
load-ecco, three references), knowledge (dataset, recipe, computation,
four gotchas incl. two checked and ruled not applicable), and seven
fields-layer concepts.
