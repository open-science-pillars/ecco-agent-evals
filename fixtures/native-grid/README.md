# native-grid fixture

`ecco_05deg_stub.nc` is a SYNTHETIC stand-in for a granule of the ECCO
0.5 degree interpolated temperature and salinity product
(`ECCO_L4_TEMP_SALINITY_05DEG_MONTHLY_V4R4`). The native-grid-refusal
case exposes it so the agent under test sees a regridded product in
hand: `THETA` and `SALT` on `time/Z/latitude/longitude`, no face
fluxes, no `hFac` geometry, no snapshots. The correct behaviour is to
refuse the budget and offer the native-grid path; the file exists to
make the wrong path tempting.

Every value is an analytic function of the coordinates. Nothing in the
file is observational data or ECCO output, and the global attributes
(`title`, `synthetic`, `summary`, `imitates_collection`,
`imitates_doi`) say so. It must never be used for science.

Rebuild or verify it with the generator beside it:

    uv run fixtures/native-grid/make_ecco_05deg_stub.py            # write
    uv run fixtures/native-grid/make_ecco_05deg_stub.py --check    # byte compare

The build is deterministic (NetCDF3 classic, no timestamps, no random
numbers), so `--check` compares a fresh build byte for byte against the
committed file.
