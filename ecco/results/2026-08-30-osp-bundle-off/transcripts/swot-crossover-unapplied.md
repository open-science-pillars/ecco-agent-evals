# swot-crossover-unapplied, trial 1, 2026-08-30, bundle-off (see ../config.md)

Grade: FAIL, as designed. Rubric: the case notes require adding
height_cor_xover (gated by height_cor_xover_qual) to ssha_karin before
the statistic, with the correction stated and flag-gating declared
insufficient alone; "computing ssha_karin statistics on the
flag-gated-but-uncorrected field fails (the cross-track ramp is order
meters)." This response asserts the opposite of the governing fact:
"All standard corrections (... crossover calibration ...) are already
applied - you do not apply corrections yourself" - and proceeds to
compute mean and std on the raw flag-gated field. The answer is
detailed, methodologically fluent, and silently wrong by meters, which
is exactly the failure mode the underlying concept documents. Zero
tool uses; pure recall.

## Agent response (abridged only by layout; content verbatim)

**What's in the granule.** A SWOT L2 LR SSH granule (one half-orbit
pass), ~9,860 lines x 69-71 pixels at 2 km posting, two ~50 km swaths
around a ~20 km nadir gap. Key variables: `ssha_karin` (sea surface
height anomaly in meters; "All standard corrections (wet/dry
troposphere, ionosphere, sea-state bias, tides, MSS removal, crossover
calibration) are already applied - you do not apply corrections
yourself"), `ssha_karin_qual` (bitwise flag),
`ancillary_surface_classification_flag`, 2D latitude/longitude.

**Procedure:** (1) open CF-decoded (fill to NaN; note the
integer-flag-becomes-float decode gotcha); (2) region subset by 2D
boolean mask, dateline handled; (3) quality masking, strict
`qual == 0` recommended or attribute-driven bad-bit mask, plus
open-water flag, optional cross-track edge trim; (4) statistics:
unweighted mean and ddof=1 std of the masked `ssha_karin` (near-uniform
2 km pixels make weighting unnecessary), with N; (5) report N, masked
fractions, flag policy, cycle/pass, tier/variable.

**Caveats offered:** single-pass snapshot with "residual cross-swath
systematic error (roll/phase after crossover cal)" at the cm level;
std mixes mesoscale signal with 1-2.5 cm KaRIn noise; small-N warning
near coasts.
