# ecco-agent-evals

Can your agent do ECCO right? A neutral, versioned benchmark of
realistic ocean-data tasks that test whether an AI agent avoids the
documented ECCO traps and produces numbers inside recorded tolerances:
interpolated-grid budgets, missing snapshot bookends, the dropped
geothermal term, mixed releases, unapplied SWOT crossover calibration,
basin-scope errors against RAPID, and ungated terabyte downloads.

Every case cites the steward-signed knowledge concept it derives from,
by path and commit (`concept_basis` in each case header), so the
benchmark inherits its provenance from the
[OSP knowledge bundle](https://github.com/open-science-pillars/nasa-daac-knowledge)
(`knowledge/podaac/` in that repository) rather than inventing its own
truth. Cases whose underlying concept changes status are re-versioned
or retired with it.

## cases/ is the authority

The ocean eval cases have one home: `cases/` in this repository. The
[ocean-science plugin](https://github.com/open-science-pillars/ocean-science)
carries a port of each case in its `evals/` directory so the plugin can
run them in place, and that port is allowed to differ from the
authority only by its file header:

- here, the header is the leading comment lines plus `concept_basis`
  (the signed concepts the case is graded against, pinned to a
  nasa-daac-knowledge commit);
- in the plugin, the header is the leading comment lines plus `targets`
  (the plugin skills and concepts the case exercises).

Everything else (`id`, `type`, `prompt`, `fixtures`, `graders`,
`trials`, `pass_threshold`, `notes`) must agree. `tools/port_check.py`
enforces this. It compares the parsed YAML, not the bytes, because the
two repositories fold long strings differently: strings are compared
with whitespace collapsed, and fixtures are compared by file name
because each side names them relative to its own repository (a same
name, different path pair is reported as a note, not a mismatch). It
also checks that every fixture an authority case names exists here,
and warns when a plugin case names one that does not exist there.

    uv run tools/port_check.py ../ocean-science/evals   # exit 1 on MISMATCH or MISSING
    uv run tools/port_check.py --selftest               # match, mismatch, missing, fixture

**Refreshing the port.** Edit cases here, never in the plugin. Then,
in the plugin, for each changed case copy the authority file over
`evals/<id>.yaml`, drop the comment header and the `concept_basis`
block, and restore that case's `targets` line; run `port_check.py`
against the plugin's `evals/` until every case reports MATCH. A case
added here is MISSING in the plugin until it is ported; a case removed
here shows as EXTRA in the plugin (not an error, retire it there too).

The case schema itself (fields, grader kinds, seed discipline) is
documented once, in the marketplace's
[eval authoring guide](https://github.com/open-science-pillars/marketplace/blob/main/docs/eval-authoring-guide.md);
this README does not restate it.

## Layout

- `CHARTER.md` - governance: neutral scope, versioned releases,
  transparent scoring, self-reported runs with published transcripts,
  and explicitly no editorial leaderboard.
- `cases/` - the case set (YAML: prompt, graders, trials, threshold,
  notes, concept basis). The authority; see above.
- `fixtures/` - grader reference fixtures (for example the tutorial's
  own checkpoint numbers) and case fixtures. `fixtures/native-grid/`
  holds the synthetic regridded stub the native-grid-refusal case
  exposes, with the deterministic generator that builds it.
- `scoring/score.py` - deterministic scoring with Wilson 95% CIs.
- `tools/port_check.py` - the port check described above.
- `tools/run_checks.sh` - the gate: both selftests, the fixture build
  check, and the port check against `../ocean-science/evals` when that
  sibling exists (or `PLUGIN_EVALS=<dir>` to point it elsewhere).
  Green before any PR.
- `RUNNER.md` - the protocol: configuration disclosure, the mandatory
  case-tree exclusion, query policy, trials, and the submission format.
- `results/` - submitted entries, one directory each, chronological.
  OSP's own baseline is the first entry: we go first, publicly,
  including the runs where the agent was configured to fail.

## Run it

1. Read `RUNNER.md`, fix your agent configuration, and exclude
   `cases/` from anything the agent can search.
2. Run each case's `prompt` verbatim; grade against `notes` (seed) or
   the programmatic graders (as they land); score with
   `uv run scoring/score.py results/<your-entry>/results.yaml`.
3. Submit your entry by PR (DCO sign-off; transcripts CC BY 4.0).

Results are comparable only within a tagged set; state the tag.

## License

Code and cases Apache-2.0; transcripts CC BY 4.0. The project name is
descriptive and unaffiliated; ECCO and NASA marks belong to their
owners, and endorsement is neither claimed nor implied.
