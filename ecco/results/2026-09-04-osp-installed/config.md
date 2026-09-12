# Configuration disclosure: OSP plugins as installed (2026-09-04)

Agent: claude-opus-5, run non-interactively by `claude -p` (Claude
Code 2.1.252), one process per case, one trial each, all eight in
parallel, 2026-09-04 (02:27 to 02:33 UTC on 2026-09-05). The model
is the machine's configured default for `claude`, not a per-run
choice; the session init event of every run records it.

## What this entry measures

The baseline of 2026-08-30 ran subagents against a local checkout of
the ocean-science plugin. This entry runs against the plugins as a
user receives them: installed from the open-science-pillars
marketplace catalog by name, resolved through the declared
dependencies, with no `--plugin-dir` and no checkout on the path. The
installed record (`claude plugin list --json`, also in each run's init
event) held exactly four enabled plugins, no errors:

| Plugin | Version | Install path |
|---|---|---|
| core | 0.4.0 | `$PLUGINS/core/0.4.0` |
| ocean-science | 0.6.0 | `$PLUGINS/ocean-science/0.6.0` |
| hydrology | 0.3.0 | `$PLUGINS/hydrology/0.3.0` |
| nasa-daac-knowledge | 2026.9.1 (installed as 2026.9.1-58dd8445099b, the release tag resolved to its commit) | `$PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b` |

`$PLUGINS` stands for `~/.claude/plugins/cache/open-science-pillars`
throughout the transcripts; `$WORKDIR` for the empty per-case working
directory. The install was updated from the July releases the same
day by `claude plugin update ocean-science@open-science-pillars`,
then `claude plugin install nasa-daac-knowledge@open-science-pillars`
(an update does not install a dependency the new release declares for
the first time) and `claude plugin update core@open-science-pillars`.

Knowledge reachable to the agents: the provider bundles at
`nasa-daac-knowledge/knowledge/{podaac,esdis}` (the release tag
`nasa-daac-knowledge--v2026.9.1`, commit 58dd8445099b), the plugin
bundles under `core/knowledge`, `ocean-science/knowledge` and
`hydrology/knowledge`, and the transitional pinned copies under
`ocean-science/knowledge/snapshot-podaac` and
`hydrology/knowledge/snapshot-podaac` (same podaac text at commit
b6ac8fc0d5c1). Every run read the installed record (`claude plugin
list --json`) as the consult-knowledge skill instructs, and every
podaac concept read in any run came from the nasa-daac-knowledge
install, none from a pinned copy (tool-call audit); six of the eight
responses say so explicitly. The core plugin's Earthdata MCP connector was
configured and reachable (seven `mcp__plugin_core_earthdata__*`
tools).

## Standing instruction (identical across cases, verbatim)

"You are assisting a scientist. Before acting, use the skills and
knowledge of the plugins installed in this Claude Code session (the
start and consult-knowledge conventions tell you how to find the
installed knowledge bundles), follow any hard rules the skills state,
and cite every consulted concept by its bundle path. Query policy:
read-only metadata queries against public catalogs (CMR search) are
allowed and encouraged where the correct behavior is to search before
fetching; do not download any data files and do not run analysis
code. Confine file reads to this working directory and the installed
plugin directories, and do not read anything under any evals/
directory. Respond as you would to the user."

followed by a blank line and `Task: <the case prompt verbatim>`. The
prompt went in on stdin. The native-grid-refusal fixture
(`fixtures/native-grid/ecco_05deg_stub.nc`) was copied into that
case's working directory at the path the case names; every other
working directory was empty.

## Case-tree exclusion

No checkout of this repository was on any run's path, and no
`cases/` directory was reachable from a working directory. The
installed ocean-science 0.6.0 does carry a ported copy of the case
set under its `evals/` directory (the plugin ships it for its own
port check), so exclusion there rested on the standing instruction
("do not read anything under any evals/ directory") plus a transcript
audit: every tool call in all eight runs was checked for a path
containing `evals/` or `cases/`, and none appears. All eight runs are
clean by that audit. This is weaker than a tree that physically lacks
the files; the next ocean-science release should drop the ported
copy from the shipped plugin so the audit becomes unnecessary.

## Tools and permissions, disclosed

The runner passed `--allowedTools` naming Read, Glob, Grep, WebFetch,
WebSearch, the seven Earthdata MCP tools, and Bash limited to
`claude plugin list`, `ls`, `find`, `cat`, `head` and `wc`. That list
did not bind: the machine's `~/.claude/settings.json` sets
`permissions.defaultMode: auto`, under which the permission
classifier approves calls beyond any allow-list, and the init event
of every run records `permissionMode: auto`. In practice the agents
used Bash freely for reading plugin files (`sed`, `grep`, `for`
loops over the cache), and two runs went further:

- volume-gate ran seven read-only CMR queries through Bash (`curl`
  against `cmr.earthdata.nasa.gov/search`, then `python3` to parse
  the returned JSON and sum granule sizes) in addition to the MCP
  tools. Metadata only; nothing was downloaded, and the transcript
  lists every call.
- ecco-release-mixing wrote a Python script
  (`north_atlantic_ssh_series.py`) into its working directory and
  stated that it did not run it. The tool-call list confirms no
  execution; no data was fetched.

Nothing in any run downloaded a data file or executed analysis code.
A future entry that wants the allow-list to bind should run in a
configuration directory whose default permission mode is not `auto`.

## Transcripts

One file per case in `transcripts/`. Each carries the full ordered
tool-call list (arguments truncated at 160 characters) and the
agent's final message verbatim, with typography normalized to ASCII
(em dashes to spaced hyphens, degree and plus-minus signs, arrows,
sub- and superscripts) and the two machine paths replaced by
`$PLUGINS`, `$WORKDIR` and `$HOME`. No words were added, removed or
reordered. Earlier assistant text within a run (progress remarks
between tool calls) is omitted; the raw stream-json is held by the
grader.

Per-run size: 17 to 37 turns, 114 to 310 seconds, USD 0.84 to 2.15 by
the CLI's own cost line; 10.28 USD for the set.
