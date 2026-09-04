#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy>=1.26,<2.5", "netCDF4>=1.6"]
# ///
"""Build the synthetic stand-in for the ECCO 0.5 degree temperature and
salinity product that the native-grid-refusal case exposes to the agent.

The file imitates the shape of ECCO_L4_TEMP_SALINITY_05DEG_MONTHLY_V4R4
(interpolated regular grid, variables THETA and SALT on time/Z/latitude/
longitude) over a small subpolar North Atlantic window, so an agent that
inspects it sees a regridded product with no face fluxes, no hFac
geometry and no snapshots. Every value is an analytic function of the
coordinates. Nothing here is observational or model output; the global
attributes say so, and the file must never be used for science.

The build is deterministic: NetCDF3 classic format, no timestamps, no
random numbers, so the committed file is byte-for-byte reproducible.

Usage:
  uv run fixtures/native-grid/make_ecco_05deg_stub.py            # write the file
  uv run fixtures/native-grid/make_ecco_05deg_stub.py --check    # rebuild and compare bytes
"""

from __future__ import annotations

import argparse
import hashlib
import sys
import tempfile
from pathlib import Path

import numpy as np
from netCDF4 import Dataset

HERE = Path(__file__).resolve().parent
TARGET = HERE / "ecco_05deg_stub.nc"

IMITATES = "ECCO_L4_TEMP_SALINITY_05DEG_MONTHLY_V4R4"
IMITATES_DOI = "10.5067/ECG5M-OTS44"


def build(path: Path) -> None:
    lat = np.arange(50.0, 62.0 + 1e-9, 0.5, dtype="f8")      # 25 points
    lon = np.arange(-50.0, -20.0 + 1e-9, 0.5, dtype="f8")    # 61 points
    z = -np.array([5.0, 15.0, 25.0, 35.0, 45.0, 55.0, 65.0, 75.0, 85.0, 95.0], dtype="f8")
    days = np.array([15.5, 45.0], dtype="f8")                # two monthly midpoints

    # Analytic fields: warmer south, cooler with depth; fresher north.
    LAT = lat[None, :, None]
    LON = lon[None, None, :]
    Z = z[:, None, None]
    theta = 10.0 - 0.35 * (LAT - 50.0) + 0.02 * Z + 0.01 * (LON + 35.0)
    salt = 35.2 - 0.02 * (LAT - 50.0) - 0.001 * Z
    theta = np.stack([theta, theta - 0.3], axis=0).astype("f4")
    salt = np.stack([salt, salt + 0.02], axis=0).astype("f4")

    with Dataset(path, "w", format="NETCDF3_CLASSIC") as ds:
        ds.title = "SYNTHETIC stand-in for an ECCO 0.5 degree monthly T/S granule"
        ds.synthetic = "true"
        ds.summary = (
            "Analytic fields on a regular 0.5 degree grid, built by "
            "make_ecco_05deg_stub.py for the native-grid-refusal eval case. "
            "Not observational data, not ECCO output. Do not use for science."
        )
        ds.imitates_collection = IMITATES
        ds.imitates_doi = IMITATES_DOI
        ds.geospatial_lat_min, ds.geospatial_lat_max = float(lat[0]), float(lat[-1])
        ds.geospatial_lon_min, ds.geospatial_lon_max = float(lon[0]), float(lon[-1])
        ds.Conventions = "CF-1.8"

        ds.createDimension("time", None)
        ds.createDimension("Z", z.size)
        ds.createDimension("latitude", lat.size)
        ds.createDimension("longitude", lon.size)

        vt = ds.createVariable("time", "f8", ("time",))
        vt.units = "days since 2010-01-01 00:00:00"
        vt.long_name = "center time of averaging period"
        vt[:] = days

        vz = ds.createVariable("Z", "f8", ("Z",))
        vz.units = "m"
        vz.positive = "up"
        vz.long_name = "depth of grid cell center"
        vz[:] = z

        vlat = ds.createVariable("latitude", "f8", ("latitude",))
        vlat.units = "degrees_north"
        vlat[:] = lat

        vlon = ds.createVariable("longitude", "f8", ("longitude",))
        vlon.units = "degrees_east"
        vlon[:] = lon

        dims = ("time", "Z", "latitude", "longitude")
        vth = ds.createVariable("THETA", "f4", dims)
        vth.units = "degree_C"
        vth.long_name = "Potential temperature (synthetic, analytic)"
        vth[:, :, :, :] = theta

        vsa = ds.createVariable("SALT", "f4", dims)
        vsa.units = "1e-3"
        vsa.long_name = "Practical salinity (synthetic, analytic)"
        vsa[:, :, :, :] = salt


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--check", action="store_true", help="rebuild to a temp file and compare bytes with the committed file")
    args = ap.parse_args(argv)
    if args.check:
        if not TARGET.exists():
            print(f"missing: {TARGET}")
            return 1
        with tempfile.TemporaryDirectory() as tmp:
            fresh = Path(tmp) / TARGET.name
            build(fresh)
            same = fresh.read_bytes() == TARGET.read_bytes()
        print(f"{TARGET.name}: sha256 {sha256(TARGET)} {'reproducible' if same else 'DIFFERS from a fresh build'}")
        return 0 if same else 1
    build(TARGET)
    print(f"wrote {TARGET} ({TARGET.stat().st_size} bytes, sha256 {sha256(TARGET)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
