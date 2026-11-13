# Lab 6 technology extension: capacity experiments

## Learning focus

Use NetworkX to accelerate later capacity and bottleneck experiments once the
small maximum-flow/minimum-cut reasoning has been reviewed.

## Independent work

Both core learner functions, feasible-flow arguments, cut predictions, and the
optimality justification remain independent work. A library flow routine must
not fill in those functions or provide unattempted answers.

## Supporting operations

Represent the directed capacity network and explicit vertex inventory in
NetworkX. Choose a modest extension of the synthetic distribution network and
state which capacities will vary before computation. Keep capacity distinct
from cost, travel time, or reliability.

## Comparison after review

After the core implementation and reasoning review, compare NetworkX flow and
cut results on small cases, then run the planned capacity changes. Confirm
capacity-attribute names and treatment of opposite directed arcs. Preserve the
lab's finite capacity assumptions instead of accepting an unintended library
default. Different optimum flows or cuts may be valid.

## Validation and report

Check capacity bounds, conservation at intermediate vertices, source/sink value,
and equality with the capacity of an appropriate cut. Compare optimum values
rather than exact flow dictionaries, accounting for omitted zero entries.
Confirm representation round trips preserve capacities and direction. Report
which conclusions follow from the model and which operational constraints it
omits; include resource use for the chosen workload.

## Setup status and review record

Follow [shared technology guidance](../../TECHNOLOGIES.md) and
[the core exercise](exercise.md). The extension documentation is prepared;
versions, dependency/setup changes, extension code, and runtime checks remain
pending a separate approved step. Existing core dependency requirements still
apply. Record predictions, operations used, independent checks, actual outcomes,
assistance, limitations, and review in [notes.md](notes.md). This document
supplies no completed implementation, query answers, or proof.
