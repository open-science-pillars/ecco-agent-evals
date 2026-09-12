# swot-crossover-unapplied, trial 1, 2026-08-30, bundle-on (see ../config.md)

Grade: PASS. Clean run.

## Agent response (abridged only by layout; content verbatim)

**The critical correction first.** In the KaRIn L2 LR SSH products the
crossover calibration arrives UNAPPLIED in `ssha_karin`. Flag-gated
statistics on the raw field carry a spurious linear cross-track ramp of
order meters (observed: raw span about +/-2.9 m versus 0.17 m std after
correction, on a PGD0 cycle-011 granule). Quality flags alone do not
make the mean and std safe. The correct field is
`ssha_karin + height_cor_xover`, with `height_cor_xover` itself gated
by `height_cor_xover_qual`. Your headline numbers must come from that
corrected field, and the write-up must state the correction was
applied.

**The computation, in order:** (1) identify the granule (tier, version
family, cycle, pass, and the `crid` attribute, recorded because
baselines drift within a collection); (2) trim to the region before any
aggregation (a matched pass can carry zero in-box pixels; the in-region
good-pixel count is reported); (3) fill-value audit before anything;
(4) decode `ssha_karin_qual` bitwise from the granule's own
`flag_masks`/`flag_meanings` (no concept pins a SWOT bit layout), keep
fully-good pixels, apply the categorical gates that fit the region,
report the masked fraction (39 percent valid on an open-ocean pass is
normal); (5) apply the crossover correction with its qual mask;
(6) mean and std per swath and combined, nadir gap intact, never
interpolated; (7) uncertainty statement: `ssh_karin_uncert` is
per-sample random noise only, excluded from being quoted as the total
budget; spatially blocked bootstrap for sampling uncertainty with the
residual correlated systematics stated as outside that interval.

**Two things not done under any instruction:** averaging unflagged or
packed-flag pixels, and filling the nadir gap.

## Consulted paths (as reported by the agent)

skills/swot/SKILL.md; skills/swot/references/swot-products.md;
skills/load-swot/SKILL.md; knowledge/index.md;
knowledge/datasets/swot-karin.md;
knowledge/gotchas/swot-crossover-unapplied.md;
knowledge/gotchas/swot-calval-orbit-phases.md;
core skills quality-control and uncertainty-quantification;
core knowledge/conventions/satellite-qa-flag-decoding.md.
