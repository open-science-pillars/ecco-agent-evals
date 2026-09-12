# swot-crossover-unapplied, trial 1, 2026-09-04, installed (see ../config.md)

Grade: PASS. Clean run (no case or evals file read; audit in config.md).

## Tool calls (17)
- `Skill` {"skill": "core:start"}
- `Bash` {"command": "claude plugin list --json 2>/dev/null | head -200", "description": "List installed plugins"}
- `Bash` {"command": "ls -la $WORKDIR/ 2>/dev/null", "description": "List working directory"}
- `Skill` {"skill": "core:consult-knowledge"}
- `Bash` {"command": "cat $WORKDIR/started; echo \"---\"; find $HOME/.claude/jobs/7612...
- `Bash` {"command": "for p in $PLUGINS/core/0.4.0 $PLUGINS/ocean-...
- `Bash` {"command": "grep -ril \"swot\" $PLUGINS/*/*/knowledge/ 2>/dev/null | sort", "description": "Find SWOT-rela...
- `Bash` {"command": "cd $PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac; echo \"########## data...
- `Bash` {"command": "cd $PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac; echo \"########## gotc...
- `Bash` {"command": "cd $PLUGINS/ocean-science/0.6.0; echo \"### snapshot.yaml\"; cat knowledge/snapshot.yaml 2>/de...
- `Bash` {"command": "cat \"$PLUGINS/ocean-science/0.6.0/skills/load-swot/SKILL.md\" 2>/dev/null || find /Users/pram...
- `Bash` {"command": "sed -n '1,200p' \"$PLUGINS/ocean-science/0.6.0/skills/swot/SKILL.md\"", "description": "Read o...
- `Bash` {"command": "sed -n '1,200p' \"$PLUGINS/core/0.4.0/skills/quality-control/SKILL.md\"", "description": "Read...
- `Bash` {"command": "cd $PLUGINS/nasa-daac-knowledge/2026.9.1-58dd8445099b/knowledge/podaac; ls fields/ conventions...
- `Bash` {"command": "cd $PLUGINS/core/0.4.0/knowledge; ls; echo \"--- conventions ---\"; ls conventions/ 2>/dev/nul...
- `Bash` {"command": "cd $PLUGINS/core/0.4.0/knowledge/conventions; echo \"########## satellite-qa-flag-decoding.md\...
- `Bash` {"command": "cd $PLUGINS/core/0.4.0/knowledge/conventions; echo \"########## smell-test-ranges.md\"; cat sm...

## Agent response (verbatim final message, typography normalized to ASCII)

## Before anything: two blockers, then the method

**I can't compute the numbers yet.** The working directory `$WORKDIR/` contains one file (`started`) - no granule. And you haven't given me the region. Point me at the file and the bounding box and I'll run it.

**More importantly: the analysis as you described it would give you a confidently wrong answer.** Flag gating alone is not enough for SWOT KaRIn SSHA. Here's why.

## What the knowledge bundles say

I searched the enabled plugins from the installer record (`claude plugin list --json`): core 0.4.0, ocean-science 0.6.0, hydrology 0.3.0, and the provider bundle nasa-daac-knowledge 2026.9.1. ocean-science carries a pinned copy of the PO.DAAC concepts under `knowledge/snapshot-podaac/`; since the provider plugin is installed, I cite the canonical text.

### The headline: crossover calibration arrives UNAPPLIED

`knowledge/podaac/gotchas/swot-crossover-unapplied.md` (severity **high**, status **stable**, human-verified by `human:PaulMRamirez` at 2026-09-04, `stale_after` 2027-01-04 - current).

The crossover calibration is **not** pre-applied to `ssha_karin` / `ssh_karin`. The granule metadata itself instructs adding `height_cor_xover`, and the Product Description (JPL D-56407 Rev C, section 4.1.8) says the correction "is not applied in forming `ssh_karin`, `ssh_karin_2`, `ssha_karin`, or `ssha_karin_2`" and "should be added ... by the user."

The concept's observed wrong-result mode is exactly your plan: **flag-gated statistics on the raw `ssha_karin` showed a spurious linear cross-track ramp spanning about +/-2.9 m** (a roll/phase systematic). The same scene with the correction applied showed physically sensible mesoscale structure, **std 0.17 m**. Observed 2026-07-05 on a PGD0 Expert-tier granule, cycle 011 pass 424.

In the concept's own words: *"quality flags alone do not make them safe."* A mean and standard deviation off the uncorrected field is a plausible-looking number that is silently wrong - the std in particular is dominated by the instrument ramp, not the ocean.

**So the correction is a required step, not an option:** add `height_cor_xover` to `ssha_karin`, gated by `height_cor_xover_qual` (0 good, 1 suspect, 2 bad - from the PDD via the gotcha's footnote), and state in the result that it was applied. `height_cor_xover` is present in the Basic tier too, per `knowledge/podaac/datasets/swot-karin.md` - you don't need Expert for this.

### Also binding on your request

- **Subset before you aggregate.** `datasets/swot-karin.md` (stable, human-verified 2026-09-04): CMR spatial search matches whole pole-to-pole passes, and a matched pass can carry zero in-box pixels. Trim to your region first, then compute. Observed on pass 011/424.
- **Check the date.** `gotchas/swot-calval-orbit-phases.md` (severity high, stable, human-verified 2026-09-04): if the granule is from 2023, the 1-day cal/val orbit (through 2023-07-10) and the 21-day science orbit (from 2023-07-21) are not one record, and cal/val-era data exists only in the `*_D` family. One granule is one phase, so this is a labelling question here rather than a mixing hazard - but it decides how you describe the sampling.
- **Uncertainty caveat.** Same dataset concept, Uncertainty section: `ssh_karin_uncert` is per-sample **random** noise (1sigma) only. It excludes the correlated swath-scale systematics (roll, phase, timing, wet-troposphere residuals) that dominate at long cross-track wavelengths. Quoting it as the error on a regional mean understates the uncertainty.
- **Masked fraction is expected to be large.** A loaded open-ocean pass had **39% valid** `ssha_karin` after flag and land gating. That order of loss is normal, not a defect - so don't treat a big masked fraction as a sign something went wrong.
- **Swath structure stays intact.** From the `ocean-science:swot` skill's hard refusals: never interpolate across the nadir gap, and treat the two swaths as having independent error profiles. I'll report per-swath as well as pooled.

## The procedure I'll run

Per `ocean-science:load-swot` and `core:quality-control` (six checks, fill-value audit **before** bounds):

1. Open the granule; record the global `crid` attribute - the dataset concept notes baselines drift within a collection, and the granule's own `crid` is the only record of which one you have.
2. Confirm `_FillValue` applied on every variable used; scan for undeclared sentinels per `knowledge/conventions/common-fill-values.md` (core, stable).
3. Subset to your bounding box on `latitude`/`longitude`, keeping `(num_lines, num_pixels, num_sides)` intact.
4. Decode `ssha_karin_qual` **bitwise** from the variable's own `flag_meanings`/`flag_masks` attributes - never threshold the packed integer. Report which bits were masked and what fraction that removed.
5. Gate `height_cor_xover_qual` (keep 0; report how many pixels 1/2 costs you) and add `height_cor_xover` to `ssha_karin`.
6. Compute mean and std over surviving pixels, per swath and pooled, with the valid-pixel count.
7. Sanity check: if the corrected std lands near 0.1-0.2 m you're in the neighbourhood of the concept's corrected reference (0.17 m); a std of order meters means the correction didn't take.

I'd also plot cross-track ssha before and after the correction - the ramp is visible by eye, and it's the cheapest confirmation that step 5 actually did something.

## What I need from you

1. **Path to the granule** (and confirm it's inside this working directory - I'm scoped to it).
2. **Region bounds** - lat/lon box, or a named region I can turn into one.
3. **Tier**, if you know it (Basic vs Expert changes what else is available, though not the crossover step).

## One gap worth naming

No installed concept carries the bit layout for `ssha_karin_qual`. The core QA convention `knowledge/conventions/satellite-qa-flag-decoding.md` (stable) covers MODIS, Landsat C2, and Sentinel-2 only. I'll read the layout from the granule's own `flag_meanings`/`flag_masks` attributes and state exactly which bits I masked, rather than assume a layout. That's ingest material for the steward - a SWOT KaRIn flag-layout concept would close it.

---

*Housekeeping, unrelated to this task: the claude.ai Google Calendar and Mermaid Chart connectors need authorization before their tools work - via your claude.ai connector settings. This session can't run the OAuth flow.*

Run: 20 turns, 118s, cost $0.84, is_error=False
