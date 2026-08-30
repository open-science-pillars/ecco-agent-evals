# Configuration disclosure: OSP bundle-off red demonstration (2026-08-30)

Agent: claude-fable-5, run as Claude Code subagents, 2026-08-30. The
deliberate failure arm: the same case prompts verbatim, with NO
knowledge bundle and no local reference material.

Standing instruction: "For this task you have NO file access: do not
read any local files or directories, do not search the filesystem, and
do not use any local reference material. Do not download any data and
do not run analysis code. Answer purely from your own general
expertise."

Scope: two cases (mht-basin-scope, swot-crossover-unapplied), chosen as
the pair with recorded discriminating power (the July 2026
knowledge-coupling POC measured mht-basin-scope at +0.60 ON-OFF delta;
the crossover trap is a product-specific fact no general model reliably
carries). The remaining cases' failability is evidenced by the recorded
bundle-OFF ablation history cited in the OSP design notes and gets
re-demonstrated per case as the set moves to standard N.

Voided attempts, disclosed: two earlier OFF runs under a weaker
instruction (files not explicitly denied) discovered the workspace's
knowledge bundle on their own initiative, consulted it, and passed;
they are voided as OFF-arm evidence (the configuration failed, not the
cases) and are themselves a live demonstration that the bundle augments
behavior when discoverable. The sealed no-file-access instruction above
is the corrected configuration.
