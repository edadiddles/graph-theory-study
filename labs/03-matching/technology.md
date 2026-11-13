# Lab 3 technology extension: persistent linkage evidence

## Learning focus

Revisit Neo4j to distinguish records, source identifiers, candidate-link evidence,
and accepted assignments. Use the existing synthetic records rather than
introducing sensitive data or a similarity-scoring pipeline.

## Independent work

The maximum-cardinality matching function, assignment predictions, and matching
arguments remain learner work. A database query or library matching call must
not supply those answers before the corresponding review.

## Supporting operations

Propose a property-graph representation of records and their source membership.
Specify how candidate links retain evidence and how an accepted assignment
would be represented separately. Practice importing, inspecting, filtering, and
updating candidate evidence. Export the bipartite candidate graph to NetworkX
with explicit side membership, including unmatched and isolated records.

Database identity, source record identity, and real-world identity are different
concepts. Decide how stable domain IDs preserve these distinctions. A structural
connection or stored assignment does not prove that two records describe one person.

## Comparison after review

After the matching implementation and reasoning review, use NetworkX to compare
maximum cardinality and assignment feasibility on small cases. When multiple
optima exist, compare validity and size rather than requiring identical pairs.
If persisting results, label them as outputs of the stated method rather than
converting candidate evidence silently into established identity.

## Validation and report

Check source-qualified record IDs, bipartite sides, isolates, and candidate-edge
sets across import/export. Verify that changing evidence does not accidentally
merge record nodes or create an accepted assignment. Plan a repeatable import
check and confirm that synthetic identity labels remain evaluation information,
not algorithm inputs. Report data-model assumptions and unresolved identity
questions separately from graph matching results.

## Setup status and review record

Follow [shared technology guidance](../../TECHNOLOGIES.md) and
[the core exercise](exercise.md). The extension documentation is prepared;
versions, dependency/setup changes, extension code, and runtime checks remain
pending a separate approved step. Existing core dependency requirements still
apply. Record predictions, operations used, independent checks, actual outcomes,
assistance, limitations, and review in [notes.md](notes.md). This document
supplies no completed implementation, query answers, or proof.
