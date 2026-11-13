# Lab 5 technology extension: scheduling heuristics and planarity checks

## Learning focus

Compare independently justified small schedules with library-generated schedules
and relate a planarity decision to its mathematical evidence.

## Independent work

Conflict construction, minimum coloring, the original schedule predictions,
and manual planarity investigations remain learner work. Library coloring and
planarity answers wait until the corresponding attempts and reasoning review.

## Supporting operations

Use NetworkX for graph representation and interchange. Retain all exams,
including isolated ones. A visual layout, if later plotting dependencies are
approved, supports inspection; it is not a planarity certificate.

## Comparison after review

After reviewing the coloring implementation and manual planarity work, use
NetworkX coloring heuristics on a modest larger conflict graph and its planarity
routines on separate reviewed examples. State the heuristic strategy and inspect
what evidence a selected planarity interface returns. Do not equate the number
of colors from a greedy heuristic with the chromatic number.

## Validation and report

Verify every conflict is respected and every exam is assigned. Compare small
color counts with independently established optima, allowing color renaming.
For larger cases, distinguish a feasible upper bound from any separately
justified lower bound. Preserve manually attempted planarity arguments and
explain how library evidence relates to them. Record sensitivity to heuristic
choices without selecting only a favorable result.

## Setup status and review record

Follow [shared technology guidance](../../TECHNOLOGIES.md) and
[the core exercise](exercise.md). The extension documentation is prepared;
versions, dependency/setup changes, extension code, and runtime checks remain
pending a separate approved step. Existing core dependency requirements still
apply. Record predictions, operations used, independent checks, actual outcomes,
assistance, limitations, and review in [notes.md](notes.md). This document
supplies no completed implementation, query answers, or proof.
