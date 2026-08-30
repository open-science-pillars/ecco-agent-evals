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
rather than inventing its own truth. Cases whose underlying concept
changes status are re-versioned or retired with it.

## Layout

- `CHARTER.md` - governance: neutral scope, versioned releases,
  transparent scoring, self-reported runs with published transcripts,
  and explicitly no editorial leaderboard.
- `cases/` - the case set (YAML: prompt, graders, trials, threshold,
  notes, concept basis).
- `fixtures/` - grader reference fixtures (for example the tutorial's
  own checkpoint numbers).
- `scoring/score.py` - deterministic scoring with Wilson 95% CIs.
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
