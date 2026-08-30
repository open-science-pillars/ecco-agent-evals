#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml"]
# ///
"""Score a results entry: per-case pass fraction with a Wilson 95% CI.

Reads results/<entry>/results.yaml:

  set: v0.1
  agent: <name/version>
  config: config.md
  cases:
    <case-id>: { trials: N, passes: k }

Prints one line per case plus the pooled line. Deterministic, no LLM.
Usage: score.py results/<entry>/results.yaml [--selftest]
"""
import argparse
import math
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("pyyaml required", file=sys.stderr)
    sys.exit(2)


def wilson(k: int, n: int, z: float = 1.96):
    if n == 0:
        return (0.0, 0.0, 0.0)
    p = k / n
    denom = 1 + z * z / n
    center = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    return p, max(0.0, center - half), min(1.0, center + half)


def score(path: Path) -> int:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    cases = data.get("cases", {})
    print(f"set {data.get('set', '?')}  agent {data.get('agent', '?')}  "
          f"cases {len(cases)}")
    tot_k = tot_n = 0
    for cid in sorted(cases):
        c = cases[cid]
        k, n = int(c["passes"]), int(c["trials"])
        p, lo, hi = wilson(k, n)
        tot_k += k
        tot_n += n
        print(f"{cid:<28} {k}/{n}  pass {p:.2f}  wilson95 [{lo:.2f}, {hi:.2f}]")
    p, lo, hi = wilson(tot_k, tot_n)
    print(f"{'POOLED':<28} {tot_k}/{tot_n}  pass {p:.2f}  "
          f"wilson95 [{lo:.2f}, {hi:.2f}]")
    return 0


def selftest() -> int:
    p, lo, hi = wilson(4, 5)
    ok = abs(p - 0.8) < 1e-9 and 0.35 < lo < 0.40 and 0.95 < hi < 0.99
    p2, lo2, hi2 = wilson(0, 5)
    ok = ok and p2 == 0.0 and lo2 == 0.0 and 0.40 < hi2 < 0.50
    print(f"wilson(4,5)=({p:.3f}, {lo:.3f}, {hi:.3f}); "
          f"wilson(0,5)=({p2:.3f}, {lo2:.3f}, {hi2:.3f})")
    print("selftest:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("results", type=Path, nargs="?")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    if not args.results:
        print("need a results.yaml path or --selftest", file=sys.stderr)
        return 2
    return score(args.results)


if __name__ == "__main__":
    sys.exit(main())
