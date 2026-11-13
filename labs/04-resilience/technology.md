# Lab 4 technology extension: resilience comparisons

## Learning focus

Use NetworkX after the small separator exercise to investigate a somewhat
larger synthetic network and compare structural failure scenarios.

## Independent work

Minimum vertex/edge separators, the original predictions, and the disjoint-path
reasoning remain independent work under the existing contracts.

## Supporting operations

Prepare a graph container, preserve station IDs and isolates, and create copies
for proposed failure scenarios. Choose a modest network and record the pairwise
resilience question and hypotheses before obtaining answers. Graph construction
and interchange can be delegated without implementing a new container.

## Comparison after review

Once the separator tasks and corresponding arguments are reviewed, use suitable
NetworkX connectivity/cut routines for comparisons and larger experiments.
Check their conventions for adjacent terminals, initially disconnected pairs,
and allowed removal of endpoints against the lab contracts before comparison.
A different convention requires a documented comparison restriction, not a
change to the core tests. Supporting traversal routines may then accelerate
repeated failure analysis without reimplementing them.

## Validation and report

Validate each returned separator by the relevant deletion and connectivity
property. On independent tiny cases, compare minimum cardinalities; different
valid optimum sets may be acceptable. Check that failed-station deletion removes
incident edges while unaffected isolates survive. Explain whether each claim
concerns one pair or the whole graph and distinguish structural disconnection
from actual transport service disruption. Record workload and practical limits.

## Setup status and review record

Follow [shared technology guidance](../../TECHNOLOGIES.md) and
[the core exercise](exercise.md). The extension documentation is prepared;
versions, dependency/setup changes, extension code, and runtime checks remain
pending a separate approved step. Existing core dependency requirements still
apply. Record predictions, operations used, independent checks, actual outcomes,
assistance, limitations, and review in [notes.md](notes.md). This document
supplies no completed implementation, query answers, or proof.
