# Configuration disclosure: OSP bundle-on baseline (2026-08-30)

Agent: claude-fable-5, run as Claude Code subagents (one per case, one
trial each), 2026-08-30.

Standing instruction (identical across cases): "before acting, discover
and consult the relevant material in the plugin at the local
ocean-science checkout (Glob/Grep/Read across knowledge/ and skills/),
follow any hard rules the skills state, and cite every consulted
concept by its bundle path. Do not download any data files and do not
run analysis code; respond as you would to the user." The volume-gate
case additionally permitted read-only CMR metadata queries, since
search-before-fetch is the tested behavior.

Knowledge state: ocean-science plugin checkout at 70ae6122de17
(snapshot of nasa-daac-knowledge at d1284f6ac951: the migrated podaac
bundle, the ten signed fields families, the attested computations, and
the draft tutorial companions); the core plugin checkout was also
present and was consulted by some runs, as in a real install.

Anomalies, disclosed:
- The agents' searchable tree included the plugin's evals/ directory,
  and three of eight runs discovered and read their own case definition
  mid-sweep (each disclosed it in-transcript; see GRADING.md). Behavior
  in all three traces to concepts and skills that predate the cases,
  and one case has an uncontaminated same-day twin pass, but this is
  exactly why RUNNER.md makes the case-tree exclusion mandatory for
  every future entry, this one included on any rerun.
- One run (ecco-release-mixing) made read-only CMR metadata queries
  beyond its plan-only instruction; disclosed, harmless, and the reason
  RUNNER.md states the query policy explicitly.
