# Lab 2 technology extension: graph containers and persistent dependencies

## Learning focus

Practice NetworkX representation and Neo4j property-graph modeling, Cypher, and
Python interchange using the existing synthetic package graph. No external
package registry or real dependency ingestion is needed.

## Independent work

Keep `reachable_vertices` and `strongly_connected_components` as the existing
standard-library learner tasks. Make the original predictions and arguments
without querying their answers through NetworkX or Neo4j.

## Supporting operations

Represent explicit packages and dependency edges in a directed NetworkX graph.
Inspect attributes and export/import a chosen format while retaining packages
with no edges. Design stable package IDs and a Neo4j schema before importing.
Basic storage, attribute queries, and Python driver mechanics are supporting
operations; they need not become new algorithm implementations.

## Comparison after review

After the independent implementations and corresponding reachability/SCC
reasoning are reviewed, compare NetworkX results on small cases. Then formulate
Cypher questions about dependency reachability and potential change impact.
State which direction each question follows and whether the start vertex is
included. Export the database graph back to Python for comparison. A query
returning paths is not by itself an SCC algorithm or an operational impact model.

## Validation and report

Check exact domain vertex IDs, isolates, directed edge sets, and selected
attributes across the round trip. In the later runnable extension, test a
repeated import for the intended absence of duplicates and an update for its
intended effect, using isolated study data. Compare reachability sets and SCC
partitions without relying on output order. Inspect a small cycle and a package
with no dependencies. Record the storage/query lessons separately from core
algorithm correctness and omitted domain details such as versions.

## Setup status and review record

Follow [shared technology guidance](../../TECHNOLOGIES.md) and
[the core exercise](exercise.md). The extension documentation is prepared;
versions, dependency/setup changes, extension code, and runtime checks remain
pending a separate approved step. Existing core dependency requirements still
apply. Record predictions, operations used, independent checks, actual outcomes,
assistance, limitations, and review in [notes.md](notes.md). This document
supplies no completed implementation, query answers, or proof.
