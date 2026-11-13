# Lab 16 technology extension: justify the toolchain

## Learning focus

Select technologies that support the project question and compare representations
or execution approaches only where the comparison has a clear purpose.

## Independent work

The question, model, predictions, mathematical argument, evaluation design, and
interpretation remain learner work. Any specifically agreed algorithm-learning
task retains its independent implementation requirement.

## Supporting operations

Use NetworkX for graph handling and suitable established algorithms, SciPy for
sparse numerical work, and Neo4j where persistence, relationship evidence, or
queries support the question. Previously studied algorithms may be delegated;
there is no requirement to rewrite every method used by the project. Explain
assumptions, exact versus heuristic behavior, and why each operation applies.

## Optional comparisons after review

Consider python-igraph only for a concrete alternative representation or measured
workload question. It is not a required extra library. Consider Neo4j Graph Data
Science only after the stored property graph and analysis projection have been
defined and reviewed. State relationship filters, direction, weights, aggregation,
and node inventory for that projection. Do not assume the projected graph is
identical to the database or that a community algorithm establishes identity.

For any solver that answers a core learning task, complete and review the
independent task first. An unfamiliar supporting algorithm needs an explanation
of its assumptions and outputs, not necessarily a new implementation exercise.
Extra dependencies and runnable setup need their own approved scope.

## Validation and report

Extend the project's validation plan with relevant conversion invariants,
independent small cases, and a reproducible workload if comparing engines.
Check IDs, isolates, direction, weights, attribute loss, and matrix ordering.
Compare validity and objectives rather than arbitrary nonunique outputs. Report
versions, data/parameters, runtime and memory measurements with their scope,
and any differences in model semantics. Include database import/export or
projection checks only if those tools are actually selected. Keep tool familiarity,
algorithm correctness, and evidence for the application conclusion separate.

## Setup status and review record

Follow [shared technology guidance](../../TECHNOLOGIES.md) and
[the core exercise](exercise.md). The extension documentation is prepared;
versions, dependency/setup changes, extension code, and runtime checks remain
pending a separate approved step. Existing core dependency requirements still
apply. Record predictions, operations used, independent checks, actual outcomes,
assistance, limitations, and review in [notes.md](notes.md). This document
supplies no completed implementation, query answers, or proof.
