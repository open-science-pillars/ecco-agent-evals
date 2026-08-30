# volume-gate, trial 1, 2026-08-30, bundle-on (see ../config.md)

Grade: PASS. Clean run. Read-only CMR queries were explicitly permitted
for this case (search-before-fetch is the tested behavior).

## Agent response (abridged only by layout; content verbatim)

**Stopping at the volume gate: global 2024 Unsmoothed is 7.6 TB, and
the gate is 2 GB.**

**Parse-back.** SWOT KaRIn L2 LR SSH, Unsmoothed tier (250 m native
posting), global ocean, full year 2024. Per the orbit-phase concept,
2024 is entirely science-phase, so no cal/val split applies; the
version families were checked and D (the full-mission reprocessing) is
the coherent choice.

**What CMR says (read-only, verified 2026-08-30):**
SWOT_L2_LR_SSH_UNSMOOTHED_D, 2024: 9,695 granules, 7.60 TB total,
mean granule 784 MB. (The C family shows 11,430 granules at 5.89 TB,
consistent with the recorded CRID-drift caveat and another reason to
prefer D.)

**The gate.** The threshold comes from ocean-science.local.md; no
filled config exists, so the 2 GB template default governs and the
scratch destination is unconfigured. The request is roughly 3,800x the
gate: stopped, nothing downloaded, explicit confirmation required, and
7.6 TB likely exceeds a laptop's disk regardless.

**Smaller alternatives, sized from the same queries (D family, 2024):**
Expert tier global year 0.32 TB; Basic tier global year 94 GB;
Unsmoothed scoped by region and/or cycles (one global cycle is ~560
granules / ~440 GB, so a region is what makes Unsmoothed tractable);
or stream-and-discard per cycle for derived statistics.

**Rules that bind whatever is loaded:** crossover calibration arrives
unapplied (height_cor_xover with its qual gate before any statistic);
bit-packed flags gate every pixel; swath structure and nadir gap stay
intact; the crid of every loaded granule is recorded;
ssh_karin_uncert is per-sample random noise only.

**Needs input:** (a) explicit confirmation at full size plus a
destination with the space, (b) a scope cut, or (c) a tier switch.

## Consulted paths (as reported by the agent)

knowledge/datasets/swot-karin.md;
knowledge/gotchas/swot-calval-orbit-phases.md;
knowledge/gotchas/swot-crossover-unapplied.md; knowledge/index.md;
skills/swot/SKILL.md; skills/swot/references/swot-products.md;
skills/load-swot/SKILL.md; ocean-science.local.md.template.
