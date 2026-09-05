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
carries no copy; its `README` and its bundle index point here, and a
plugin release is checked against the tagged case set it names. Each
case header carries two declarations:

- `concept_basis`: the signed concepts the case is graded against, by
  bundle path, pinned to a nasa-daac-knowledge commit;
- `targets`: the ocean-science skills the case exercises (a case that
  rests on the concepts alone declares `targets: []`).

Edit cases here, never anywhere else. A case whose underlying concept
changes status is re-versioned or retired with it, and a plugin skill
renamed or retired updates the `targets` that named it in the same
change. The case-level regression fixture for a plugin's own artifact
(a briefing's receipt values, for example) lives with that plugin
under its `verification/fixtures/`, because it guards the plugin's
output rather than a case here.

The case schema itself (fields, grader kinds, seed discipline) is
documented once, in the marketplace's
[eval authoring guide](https://github.com/open-science-pillars/marketplace/blob/main/docs/eval-authoring-guide.md);
this README does not restate it.

## Layout

- `CHARTER.md` - governance: neutral scope, versioned releases,
  transparent scoring, self-reported runs with published transcripts,
  and explicitly no editorial leaderboard.
- `cases/` - the case set (YAML: prompt, graders, trials, threshold,
  notes, concept basis, targets). The one home of the ocean cases; see
  above.
- `fixtures/` - grader reference fixtures (for example the tutorial's
  own checkpoint numbers) and case fixtures. `fixtures/native-grid/`
  holds the synthetic regridded stub the native-grid-refusal case
  exposes, with the deterministic generator that builds it.
- `scoring/score.py` - deterministic scoring with Wilson 95% CIs.
- `tools/run_checks.sh` - the gate: the scoring selftest and the
  fixture build check. Green before any PR.
- `RUNNER.md` - the protocol: configuration disclosure, the mandatory
  case-tree exclusion, query policy, trials, and the submission format.
- `results/` - submitted entries, one directory each, chronological.
  OSP's own runs are the first entries, from the hand-graded seed
  onward: we go first, publicly, including the runs where the agent
  was configured to fail.

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
