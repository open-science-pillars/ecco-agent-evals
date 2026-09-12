# Running the set: the protocol

How to produce a submittable results entry. The charter governs; this
document is the mechanics.

## The agent configuration

Run every case against one fixed agent configuration and disclose it
fully in your entry's `config.md`: the model and version, the tools
available, any knowledge sources attached (plugins, bundles, retrieval),
and the standing instructions. Results are only meaningful relative to
the disclosed configuration.

**Case-tree exclusion (mandatory).** The agent's searchable file tree
and retrieval sources MUST NOT include this repository's `<product>/cases/`
directory or any copy of the case definitions. In OSP's own seed
baseline, agents given a broad local tree discovered their case files
mid-run (disclosed in those transcripts); the layout rule exists so that
cannot happen. Fixtures under `<product>/fixtures/` MAY be exposed when a case
names them.

**Query policy.** Unless a case says otherwise: read-only metadata
queries against public catalogs (CMR search) are allowed and encouraged
where the correct behavior is search-before-fetch; downloading data
files and executing analysis code are not part of a case run unless the
case's prompt explicitly requires it. Nothing in any case requires
credentials beyond a standard Earthdata login.

## Trials and grading

- Seed runs: 1 trial per case, hand-graded against the case's `notes`
  (the rubric of record until programmatic graders land), grader named.
- Standard runs: `trials` per case (20 recommended), threshold per
  `pass_threshold`, scored with `scoring/score.py` (Wilson 95% CIs).
- A case must be graded on the transcript alone; the grader never
  repairs or reinterprets the agent's answer.

## The entry you submit

One directory under the product's `results/` (`ecco/results/` for the ECCO set), by PR with DCO sign-off:

```
ecco/results/<date>-<yourname>-<agent>/
  config.md        the full configuration disclosure
  results.yaml     set, agent, cases: {id: {trials, passes}}
  GRADING.md       grader, per-case evidence lines, anomalies disclosed
  transcripts/     one file per case per trial (CC BY 4.0)
```

State the tagged set you ran (results are only comparable within one
tag). The project verifies reproducibility on sampled cases and
publishes what is submitted, in chronological order, without editorial
ranking. Disagreements about a case resolve against its cited concepts
(`concept_basis` in each case header); if the concept is wrong, that
finding goes to the bundle steward as the more important result.
