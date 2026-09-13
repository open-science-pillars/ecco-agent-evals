# agent-evals

The organization's one benchmark repository: versioned, neutral
evaluation cases that test whether an AI agent uses NASA Earth science
data correctly, each product's set under its own directory and every
set governed by one [charter](CHARTER.md). The ECCO set, under
`ecco/`, is the first (renamed from ecco-agent-evals on 2026-09-12;
the old name redirects).

## The ECCO set

Can your agent do ECCO right? A neutral, versioned benchmark of
realistic ocean-data tasks that test whether an AI agent avoids the
documented ECCO traps and produces numbers inside recorded tolerances:
interpolated-grid budgets, missing snapshot bookends, the dropped
geothermal term, mixed releases, unapplied SWOT crossover calibration,
basin-scope errors against RAPID, ungated terabyte downloads, and a
regional budget certified by an identity that holds for any array.

Every case cites the steward-signed knowledge concept it derives from,
by path and commit (`concept_basis` in each case header), so the
benchmark inherits its provenance from the
[OSP knowledge bundle](https://github.com/open-science-pillars/nasa-daac-knowledge)
(`knowledge/podaac/` in that repository) rather than inventing its own
truth. Cases whose underlying concept changes status are re-versioned
or retired with it.

## ecco/cases/ is the authority

The ocean eval cases have one home: `ecco/cases/` in this repository. The
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
change. `ecco/cases/candidates/` holds a case drafted before its concept is
signed (a dead-end or field-state proposed at load_bearing high enters
its bundle at medium until the case that measures it exists); a
candidate is not in the case set, is not graded, is cited by no
results entry, and moves up to `ecco/cases/` in the change that records the
concept's signature and its `eval_case`. The case-level regression fixture for a plugin's own artifact
(a briefing's receipt values, for example) lives with that plugin
under its `verification/fixtures/`, because it guards the plugin's
output rather than a case here.

The case schema itself (fields, grader kinds, seed discipline) is
documented once, in the marketplace's
[testing guide](https://github.com/open-science-pillars/marketplace/blob/main/docs/testing.md);
this README does not restate it.

## Layout

- `CHARTER.md` - governance: neutral scope, versioned releases,
  transparent scoring, self-reported runs with published transcripts,
  and explicitly no editorial leaderboard.
- `ecco/cases/` - the ECCO case set (YAML: prompt, graders, trials, threshold,
  notes, concept basis, targets). The one home of the ocean cases; see
  above.
- `ecco/fixtures/` - grader reference fixtures (for example the tutorial's
  own checkpoint numbers) and case fixtures. `ecco/fixtures/native-grid/`
  holds the synthetic regridded stub the native-grid-refusal case
  exposes, with the deterministic generator that builds it.
- `scoring/score.py` - deterministic scoring with Wilson 95% CIs, shared by every product's set.
- `tools/run_checks.sh` - the gate: the scoring selftest and the
  fixture build check. Green before any PR.
- `RUNNER.md` - the protocol: configuration disclosure, the mandatory
  case-tree exclusion, query policy, trials, and the submission format.
- `ecco/results/` - submitted entries for the ECCO set, one directory each, chronological.
  OSP's own runs are the first entries, from the hand-graded seed
  onward: we go first, publicly, including the runs where the agent
  was configured to fail.

## Run it

1. Read `RUNNER.md`, fix your agent configuration, and exclude
   `ecco/cases/` from anything the agent can search.
2. Run each case's `prompt` verbatim; grade against `notes` (seed) or
   the programmatic graders and rubric judge of the
   [evals](https://github.com/open-science-pillars/evals) runner; score with
   `uv run scoring/score.py ecco/results/<your-entry>/results.yaml`.
3. Submit your entry by PR (DCO sign-off; transcripts CC BY 4.0).

The organization's own runs use the runner in the
[evals repository](https://github.com/open-science-pillars/evals) with
the manifest `manifests/ocean-science.yaml`; a submitter may use any
agent, and the protocol in `RUNNER.md` is what makes the entries
comparable.

Results are comparable only within a tagged set; state the tag.

## License

Code and cases Apache-2.0; transcripts CC BY 4.0. The project name is
descriptive and unaffiliated; ECCO and NASA marks belong to their
owners, and endorsement is neither claimed nor implied.
