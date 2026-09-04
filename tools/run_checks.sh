#!/usr/bin/env bash
# Gate for ecco-agent-evals. Green before any PR.
#
#   tools/run_checks.sh                     # selftests and the fixture build check
#   PLUGIN_EVALS=path tools/run_checks.sh   # also check a plugin's port against cases/
#
# When PLUGIN_EVALS is unset and a sibling ../ocean-science/evals exists,
# the port check runs against it. A port that is behind the authority
# fails the gate on purpose: refresh the port (see README.md).
set -u
cd "$(dirname "$0")/.."

status=0
run() {
  echo "== $*"
  "$@" || status=1
  echo
}

run uv run scoring/score.py --selftest
run uv run tools/port_check.py --selftest
run uv run fixtures/native-grid/make_ecco_05deg_stub.py --check

plugin="${PLUGIN_EVALS:-}"
if [ -z "$plugin" ] && [ -d ../ocean-science/evals ]; then
  plugin=../ocean-science/evals
fi
if [ -n "$plugin" ]; then
  run uv run tools/port_check.py "$plugin"
else
  echo "== port check skipped: no PLUGIN_EVALS and no ../ocean-science/evals"
fi

if [ "$status" -eq 0 ]; then echo "run_checks: GREEN"; else echo "run_checks: RED"; fi
exit "$status"
