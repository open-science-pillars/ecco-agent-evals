#!/usr/bin/env bash
# Gate for ecco-agent-evals. Green before any PR.
#
#   tools/run_checks.sh   # the scoring selftest and the fixture build check
set -u
cd "$(dirname "$0")/.."

status=0
run() {
  echo "== $*"
  "$@" || status=1
  echo
}

run uv run scoring/score.py --selftest
run uv run fixtures/native-grid/make_ecco_05deg_stub.py --check

if [ "$status" -eq 0 ]; then echo "run_checks: GREEN"; else echo "run_checks: RED"; fi
exit "$status"
