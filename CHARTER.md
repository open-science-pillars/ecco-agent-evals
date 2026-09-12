# Agent Evals: Charter (v1 draft)

**One benchmark repository (2026-09-12).** This repository is the
organization's one home for agent evaluation cases. Each product's set
lives under its own directory (`ecco/` first) and every set is governed
by this charter; a new product joins here rather than in a repository
of its own. The scope below is written for the ECCO set and applies to
each later set with its product's name in place of ECCO's.

**Scope.** This project publishes evaluation cases that test whether an
AI agent uses ECCO ocean state estimate products correctly: avoiding
documented misuse, selecting appropriate collections, and reproducing
validated quantities within recorded tolerances. It evaluates behavior
against signed knowledge; it does not evaluate scientific novelty, and
it does not rank products or vendors.

**Ground truth.** Every case cites the steward-signed concept or attested
computation it derives from, by path and commit. A case with no signed
basis does not ship. When the underlying concept changes status, its
cases are re-versioned or retired in the same release.

**Releases.** Cases, fixtures, and scoring code are versioned together
and released as tagged sets; results are only comparable within a tagged
set and must state it. Changes land by PR with DCO sign-off; case
additions require one maintainer review, scoring changes two.

**Results.** Runs are self-reported by PR: the tagged set, the agent and
configuration, full transcripts, and the scoring output. The project
publishes what is submitted and verifies reproducibility on sampled
cases; it does not editorialize rankings, and README tables list
submissions in chronological order only.

**Neutrality.** Maintainership is open on merit; no case may encode a
vendor-specific interface as the correct answer; access patterns are
expressed against public NASA endpoints and open libraries. Disputes
about a case's correctness are resolved against the cited concept, and
if the concept is wrong, that finding goes to the bundle steward as the
more important result.

**License and name.** Code and cases under Apache 2.0; transcripts under
CC BY 4.0. The project name is descriptive and unaffiliated; ECCO and
NASA marks belong to their owners and endorsement is neither claimed nor
implied unless a formal stewardship handoff makes it explicit.
