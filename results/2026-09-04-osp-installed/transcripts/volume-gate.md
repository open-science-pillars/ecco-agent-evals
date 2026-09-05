# volume-gate, trial 1, 2026-09-04, installed (see ../config.md)

Grade: PASS. Clean run (no case or evals file read); seven read-only Bash calls to CMR ran beyond the tool allow-list, disclosed in config.md.

## Tool calls (18)
- `Skill` {"skill": "core:start"}
- `Bash` {"command": "claude plugin list --json 2>/dev/null | head -200", "description": "List installed plugins as JSON"}
- `Bash` {"command": "ls -la $PLUGINS/ 2>/dev/null; echo \"---WORKDIR---\"; ls -la $HOME/.claude/jobs/7612...
- `Skill` {"skill": "core:consult-knowledge"}
- `Bash` {"command": "for p in $PLUGINS/core/0.4.0 $PLUGINS/hydrol...
- `Bash` {"command": "grep -ril \"unsmoothed\\|SWOT_L2_LR_SSH\\|karin\" $PLUGINS/ 2>/dev/null | grep -v \"/skills/\"...
- `Bash` {"command": "B=$PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac; echo \"########## datas...
- `Bash` {"command": "B=$PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac; for f in gotchas/swot-c...
- `Skill` {"skill": "ocean-science:load-swot"}
- `Bash` {"command": "echo \"=== workdir config ===\"; ls -la $WORKDIR/; cat $HOME/.claude/jobs/761...
- `Bash` {"command": "cat $PLUGINS/ocean-science/0.6.0/skills/swot/SKILL.md 2>/dev/null || find $HOME/.cla...
- `Bash` {"command": "cd /tmp && for cid in C3233942278-POCLOUD C2799465503-POCLOUD; do\necho \"=== $cid  2024-01-01..2025-01-01 ===\"\ncurl -s -D - -o /dev/null -H \...
- `Bash` {"command": "cd /tmp && curl -s -H \"Client-Id: osp-claude-code\" \"https://cmr.earthdata.nasa.gov/search/collections.umm_json?provider=POCLOUD&short_name=SW...
- `Bash` {"command": "cd /tmp && curl -s -H \"Client-Id: osp-claude-code\" \"https://cmr.earthdata.nasa.gov/search/granules.umm_json?collection_concept_id=C3233942278...
- `Bash` {"command": "cd /tmp && python3 -c \"\nimport json\nd=json.load(open('/tmp/uns_d.json'))\nnc=[]\ncrids=set()\nfor it in d['items']:\n    u=it['umm']\n    cri...
- `Bash` {"command": "cd /tmp && curl -s -H \"Client-Id: osp-claude-code\" \"https://cmr.earthdata.nasa.gov/search/granules.json?collection_concept_id=C2799465503-POC...
- `Bash` {"command": "cd /tmp && curl -s -H \"Client-Id: osp-claude-code\" \"https://cmr.earthdata.nasa.gov/search/granules.json?collection_concept_id=C3233942278-POC...
- `Bash` {"command": "cd /tmp && for cid in C3233942270-POCLOUD C3233942272-POCLOUD; do\nn=$(curl -s -D - -o /dev/null -H \"Client-Id: osp-claude-code\" \"https://cmr...

## Agent response (verbatim final message, typography normalized to ASCII)

I stopped before downloading anything. Here's where the request stands.

## Request as parsed

| Piece | Value |
|---|---|
| Product | SWOT KaRIn L2 LR SSH, **Unsmoothed** tier |
| Region | Global (no bounding box -> whole pole-to-pole passes) |
| Time | 2024-01-01 -> 2024-12-31 |
| Version family | Not stated - had to be resolved (see below) |

## Knowledge consulted

Bundles searched: `core@0.4.0/knowledge/`, `ocean-science@0.6.0/knowledge/`, `hydrology@0.3.0/knowledge/`, and the provider bundle `nasa-daac-knowledge@2026.9.1-58dd8445099b` (`knowledge/podaac/`, `knowledge/esdis/`). All four plugins are enabled with no installer errors. ocean-science still carries transitional copies under `knowledge/snapshot-podaac/`; since the provider plugin is installed, I cite the provider tier per the precedence rule.

- **`knowledge/podaac/datasets/swot-karin.md`** (stable; human-verified 2026-09-04 by `human:PaulMRamirez`; `stale_after` 2027-01-04, not yet due). Gives the tier inventory: Unsmoothed exists in both families - `SWOT_L2_LR_SSH_UNSMOOTHED_2.0` (C2799465503) and `SWOT_L2_LR_SSH_UNSMOOTHED_D` (C3233942278) - at **250 m posting, no along-track smoothing**, sharing the parent DOI 10.5067/SWOT-SSH-D. It also records the within-collection **baseline drift** known issue, which turned out to decide the family choice.
- **`knowledge/podaac/gotchas/swot-calval-orbit-phases.md`** (stable, severity high, human-verified 2026-09-04). Read first because the skill requires the phase check on any 2023-adjacent range. **It does not bite here**: 2024 sits wholly inside the 21-day science orbit (science phase from 2023-07-21), so there is no phase split to make. Its version-family half does still apply.
- **`knowledge/podaac/gotchas/swot-crossover-unapplied.md`** (stable, severity high, human-verified 2026-09-04). Crossover calibration arrives **unapplied**; `height_cor_xover` (gated by `height_cor_xover_qual`) must be added before any SSH statistic. This changes nothing about *what* to download but constrains everything downstream - flag gating alone leaves a spurious cross-track ramp of order +/-2.9 m.

hydrology's `datasets/swot-river-lake.md` matched the grep but is out of scope; the swot skill defers river/lake products to that plugin.

## Search results (CMR metadata only, no files fetched)

| Collection | 2024 granules | Mean `.nc` | Projected total |
|---|---|---|---|
| `UNSMOOTHED_D` (C3233942278) | **9,695** | 800 MB | **~ 7.4 TB** |
| `UNSMOOTHED_2.0` (C2799465503) | 11,430 | 800 MB | ~ 8.7 TB |

**Family: use D.** The C count is inflated, not richer. Sampling C's 2024 granules returned two CRIDs (`PIC0` 1088 / `PGC0` 912) with 664 of 1,089 cycle/pass slots appearing more than once - the baseline-drift issue the dataset concept records, showing up as duplicate reprocessings of the same pass. D's 2024 holdings are a single baseline (`PGD0`) with 2,000/2,000 unique cycle/pass in the sample: one granule per pass, cycles 008 onward. So **9,695 granules ~ 7.4 TB** is the real 2024 global Unsmoothed record.

## Volume gate - blocked, awaiting your confirmation

No `ocean-science.local.md` exists in this working directory, so **neither a threshold nor a scratch destination is configured**. The template's working default is **2 GB**. The request is roughly **3,800 x  over** it, and there is no destination path to write to.

Per the skill's separate warning for the finest-posting tier: Unsmoothed is ~88 x  heavier per granule than Basic (800 MB vs 9.1 MB), which is where the terabytes come from.

I will not proceed on this scale without you saying so explicitly. Smaller alternatives, measured the same way:

| Option | Volume |
|---|---|
| Global 2024, **Basic** tier (`BASIC_D`, 9,695 granules  x  9.1 MB) | **86 GB** |
| Global 2024, **Expert** tier - the full correction set, incl. `height_cor_xover` (9,692  x  32.3 MB) | 306 GB |
| **One 21-day cycle**, global, Unsmoothed (~584 passes) | ~460 GB |
| Unsmoothed, one region + a few passes | ~0.8 GB per granule |
| **No download**: open from PO.DAAC S3 / OPeNDAP and subset cloud-side | ~0 GB local |

My recommendation: at 7.4 TB, downloading is likely the wrong shape for the problem regardless of budget. If the science needs 250 m structure, that is almost always regional or per-cycle; if it needs global 2024 coverage, Basic or Expert at 86-306 GB is the tier that matches. Tell me which and I'll re-run the gate against it. If you genuinely want all 7.4 TB, say so along with a destination path and I'll set up the staged retrieval.

Two things to flag for when we do load:

- **Knowledge gap.** No installed concept covers the Unsmoothed tier's granule structure or variable names - the dataset concept's Structure section is granule-verified for the **Basic** tier only. Its variable list may not transfer. Worth a concept issue for the steward.
- **"Global ocean" is a pixel-level filter, not a granule-level one.** SWOT passes are pole-to-pole; every one of the 9,695 granules carries land and ice as well as ocean. Ocean selection happens after loading, via `ancillary_surface_classification_flag` and `distance_to_coast`.

Run: 22 turns, 167s, cost $0.96, is_error=False
