#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6.0"]
# ///
"""Check that a plugin's ported eval cases match the authority cases here.

cases/ in this repository is the authority for the ocean eval cases.
A plugin (for example ocean-science/evals) carries a port of each case
that is allowed to differ from the authority only by its header. This
tool compares every plugin case against its authority counterpart with
the header removed and reports MATCH, MISMATCH or MISSING per case.

The header, precisely:

  authority side (cases/*.yaml)
    - leading comment lines before the first key
    - the `concept_basis` key (the signed concepts the case is graded
      against, with the nasa-daac-knowledge commit they are pinned to)

  plugin side (<plugin>/evals/*.yaml)
    - leading comment lines before the first key
    - the `targets` key (the plugin skills and concepts the case
      exercises)

Everything else (id, type, prompt, fixtures, graders, trials,
pass_threshold, notes and any other key) must agree. Comparison is on
the parsed YAML, not the bytes: the two repositories fold long strings
differently, so every string is compared with runs of whitespace
collapsed to one space and the ends trimmed. Fixture entries are
compared by basename, because each side names fixtures relative to its
own repository; a basename match with a different directory is reported
as a note, not a mismatch.

Counterparts are found by `id` first, then by filename.

Fixture paths are also resolved: an authority case naming a fixture that
does not exist under this repository fails the check (FIXTURE line); a
plugin case naming a fixture that does not exist under the plugin
repository (the parent of its evals dir) is reported as a WARN line
without failing, since fixing it belongs to the plugin.

Usage:
  uv run tools/port_check.py <plugin-evals-dir> [--cases DIR]
  uv run tools/port_check.py --selftest

Exit status is 0 when every plugin case matches and no authority case is
missing from the plugin; 1 otherwise.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import tempfile
from pathlib import Path

import yaml

AUTHORITY_HEADER_KEYS = ("concept_basis",)
PLUGIN_HEADER_KEYS = ("targets",)
CASES_DIR = Path(__file__).resolve().parent.parent / "cases"

_WS = re.compile(r"\s+")


def _norm(value):
    """Normalise a parsed YAML value for comparison.

    Strings collapse whitespace; containers normalise recursively;
    scalars pass through.
    """
    if isinstance(value, str):
        return _WS.sub(" ", value).strip()
    if isinstance(value, list):
        return [_norm(v) for v in value]
    if isinstance(value, dict):
        return {k: _norm(v) for k, v in value.items()}
    return value


def load_case(path: Path) -> dict:
    with path.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    if not isinstance(data, dict):
        raise ValueError(f"{path}: top level is not a mapping")
    return data


def strip_header(case: dict, header_keys) -> dict:
    """Drop the header keys. Leading comments never reach the parser."""
    return {k: v for k, v in case.items() if k not in header_keys}


def load_dir(directory: Path, header_keys) -> dict[str, tuple[Path, dict]]:
    """Map case id to (path, body) for every YAML file in a directory."""
    out: dict[str, tuple[Path, dict]] = {}
    for path in sorted(directory.glob("*.yaml")):
        case = load_case(path)
        body = strip_header(case, header_keys)
        case_id = str(case.get("id") or path.stem)
        out[case_id] = (path, body)
    return out


def _fixture_names(value) -> list[str]:
    if not isinstance(value, list):
        return []
    return [os.path.basename(str(v)) for v in value]


def missing_fixtures(body: dict, root: Path) -> list[str]:
    """Fixture entries in a case body that do not exist under root."""
    fixtures = body.get("fixtures") or []
    if not isinstance(fixtures, list):
        return []
    return [str(f) for f in fixtures if not (root / str(f)).exists()]


def _describe(a, p, width: int = 60) -> str:
    """Render a value difference; long strings show where they diverge."""
    if isinstance(a, str) and isinstance(p, str) and max(len(a), len(p)) > width:
        i = 0
        while i < min(len(a), len(p)) and a[i] == p[i]:
            i += 1
        start = max(0, i - 20)
        return (
            f"differ at char {i}: authority {a[start:i + width]!r}"
            f" vs plugin {p[start:i + width]!r}"
        )
    return f"authority {a!r} vs plugin {p!r}"


def compare(auth: dict, port: dict) -> tuple[list[str], list[str]]:
    """Return (differences, notes) between two header-stripped bodies."""
    diffs: list[str] = []
    notes: list[str] = []
    a = _norm(auth)
    p = _norm(port)
    keys = sorted(set(a) | set(p))
    for key in keys:
        if key not in a:
            diffs.append(f"{key}: present in plugin only")
            continue
        if key not in p:
            diffs.append(f"{key}: present in authority only")
            continue
        if key == "fixtures":
            an, pn = _fixture_names(a[key]), _fixture_names(p[key])
            if an != pn:
                diffs.append(f"fixtures: authority {a[key]!r} vs plugin {p[key]!r}")
            elif a[key] != p[key]:
                notes.append(
                    f"fixtures: same files, different paths "
                    f"(authority {a[key]!r}, plugin {p[key]!r})"
                )
            continue
        if a[key] != p[key]:
            diffs.append(f"{key}: {_describe(a[key], p[key])}")
    return diffs, notes


def run(cases_dir: Path, plugin_dir: Path) -> int:
    if not cases_dir.is_dir():
        print(f"error: cases dir not found: {cases_dir}", file=sys.stderr)
        return 2
    if not plugin_dir.is_dir():
        print(f"error: plugin evals dir not found: {plugin_dir}", file=sys.stderr)
        return 2

    authority = load_dir(cases_dir, AUTHORITY_HEADER_KEYS)
    plugin = load_dir(plugin_dir, PLUGIN_HEADER_KEYS)

    # Counterpart by id first, then by filename stem.
    plugin_by_stem = {path.stem: cid for cid, (path, _) in plugin.items()}

    auth_root = cases_dir.resolve().parent
    plugin_root = plugin_dir.resolve().parent

    failures = 0
    matched: set[str] = set()
    for case_id in sorted(authority):
        a_path, a_body = authority[case_id]
        lost = missing_fixtures(a_body, auth_root)
        if lost:
            failures += 1
            print(f"FIXTURE   {case_id}: authority names fixtures that do not exist under {auth_root}: {lost}")
            continue
        match_id = case_id if case_id in plugin else plugin_by_stem.get(a_path.stem)
        if match_id is None:
            failures += 1
            print(f"MISSING   {case_id}: no counterpart in {plugin_dir}")
            continue
        p_path, p_body = plugin[match_id]
        diffs, notes = compare(a_body, p_body)
        if diffs:
            failures += 1
            print(f"MISMATCH  {case_id}: {p_path.name}")
            for d in diffs:
                print(f"    {d}")
        else:
            print(f"MATCH     {case_id}: {p_path.name}")
        for n in notes:
            print(f"    note: {n}")
        for f in missing_fixtures(p_body, plugin_root):
            print(f"    WARN: plugin fixture does not exist under {plugin_root}: {f}")
        matched.add(match_id)

    for case_id in sorted(set(plugin) - matched):
        print(f"EXTRA     {case_id}: in plugin, not in authority (not an error)")

    total = len(authority)
    print(f"{total - failures}/{total} authority cases matched; {failures} failing")
    return 1 if failures else 0


# --- selftest ---------------------------------------------------------------

_AUTH_CASE = """\
# Ported from somewhere; header comment.
# Second header comment line.
id: sample-case
type: rejection
concept_basis:  # nasa-daac-knowledge @ 0123456789ab
  - knowledge/podaac/gotchas/sample.md
prompt: >
  Compute the thing from the wrong product.
fixtures: [fixtures/sample/stub.nc]
graders:
  - programmatic: refuses
  - rubric: refusal-quality.md
trials: 5
pass_threshold: 0.8
notes: >
  Pass requires refusal with the gotcha cited
  and a native path offered.
"""

_PORT_MATCH = """\
id: sample-case
type: rejection
targets: [some-skill, gotchas/sample]
prompt: >
  Compute the thing from the
  wrong product.
fixtures: [verification/fixtures/stub.nc]
graders:
  - programmatic: refuses
  - rubric: refusal-quality.md
trials: 5
pass_threshold: 0.8
notes: >
  Pass requires refusal with the gotcha cited and a native path offered.
"""

_PORT_MISMATCH = _PORT_MATCH.replace("trials: 5", "trials: 20").replace(
    "a native path offered.", "a native path offered. Extra sentence."
)


def _write(directory: Path, name: str, text: str) -> None:
    (directory / name).write_text(text, encoding="utf-8")


def selftest() -> int:
    ok = True
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        cases = root / "cases"
        cases.mkdir()
        _write(cases, "sample-case.yaml", _AUTH_CASE)
        (root / "fixtures" / "sample").mkdir(parents=True)
        _write(root / "fixtures" / "sample", "stub.nc", "")

        # 1. match: header differs, prompt folded differently, fixture path differs
        good = root / "good"
        good.mkdir()
        _write(good, "sample-case.yaml", _PORT_MATCH)
        rc = run(cases, good)
        print(f"selftest match:    exit {rc} (expect 0)")
        ok &= rc == 0

        # 2. mismatch: trials and notes differ
        bad = root / "bad"
        bad.mkdir()
        _write(bad, "sample-case.yaml", _PORT_MISMATCH)
        rc = run(cases, bad)
        print(f"selftest mismatch: exit {rc} (expect 1)")
        ok &= rc == 1

        # 3. missing: plugin dir has no counterpart
        empty = root / "empty"
        empty.mkdir()
        _write(empty, "other-case.yaml", _PORT_MATCH.replace("sample-case", "other-case"))
        rc = run(cases, empty)
        print(f"selftest missing:  exit {rc} (expect 1)")
        ok &= rc == 1

        # 4. counterpart found by filename when ids differ
        by_name = root / "by_name"
        by_name.mkdir()
        _write(by_name, "sample-case.yaml", _PORT_MATCH.replace("id: sample-case", "id: renamed"))
        rc = run(cases, by_name)
        print(f"selftest by-name:  exit {rc} (expect 1, id differs)")
        ok &= rc == 1

        # 5. authority fixture missing on disk
        (root / "fixtures" / "sample" / "stub.nc").unlink()
        rc = run(cases, good)
        print(f"selftest fixture:  exit {rc} (expect 1, authority fixture absent)")
        ok &= rc == 1

    print("selftest", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("plugin_dir", nargs="?", help="plugin evals directory to check")
    ap.add_argument("--cases", default=str(CASES_DIR), help="authority cases dir (default: cases/ here)")
    ap.add_argument("--selftest", action="store_true", help="exercise match, mismatch and missing")
    args = ap.parse_args(argv)
    if args.selftest:
        return selftest()
    if not args.plugin_dir:
        ap.error("plugin_dir is required unless --selftest")
    return run(Path(args.cases), Path(args.plugin_dir))


if __name__ == "__main__":
    sys.exit(main())
