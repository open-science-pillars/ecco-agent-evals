# SYNTHETIC grader-calibration exhibit. This is NOT an agent transcript:
# it is a constructed failing response demonstrating that the case's
# grading notes discriminate. Every case ships with its pass shown by a
# real run and its fail shown here or by a real bundle-off run.

Response under test: "I'll build one continuous monthly time series
from March 2023 through March 2024 by averaging all available passes in
the box each month from SWOT_L2_LR_SSH_BASIC_2.0."

Grader verdict: FAIL. No split at the July 2023 transition, cycle
numbering unaddressed, and the Version C collection cannot even supply
the cal/val months (it returns zero granules there); the notes fail a
continuous cross-transition series without comment.
