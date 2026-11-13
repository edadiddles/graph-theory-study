# Technology practice in the graph theory study

Use libraries to support modeling and to avoid coding work outside a task's
learning objective. Keep independent reasoning where it is the objective.
There is no blanket requirement to implement every algorithm before using it.
For example, using a shortest-path implementation to investigate a spectral
distance bound is appropriate when shortest-path construction is not the task.
You must still explain what distance means and why the algorithm applies.

Lab numbers in this document identify the original source packages. The revised
[roadmap](ROADMAP.md) and [coverage crosswalk](COVERAGE.md) define adopted smaller
learning units without renaming those directories. Follow
[ASSESSMENT.md](ASSESSMENT.md) for objective-specific readiness: a technology
extension does not bypass a core assessment. Budget assigned technology work
explicitly; a distinct technology objective can have its own reviewed unit
instead of increasing a mathematics unit beyond its estimated effort range.

The technology-extension documentation is approved. Exact dependency versions,
environment changes, runnable extension scaffolds, and Neo4j setup remain a
separate step. No new packages, servers, data downloads, or runtime services
have been added. The existing NumPy requirement and learner-managed setup stand.

## Permissions by task

Each linked extension separates three kinds of work:

- **Independent work:** the current lab's required implementation, derivation,
  proof, or prediction. Existing contracts and core tests remain authoritative.
- **Supporting operations:** representation, interchange, numerical routines,
  or already-understood algorithms outside the current objective. These may be
  delegated once their assumptions and interpretation are explained; no prior
  implementation is required solely to unlock their use.
- **Comparison after review:** a library solver that answers a core task, or a
  library example/source listing that discloses its key step. Use it only after
  the independent attempt, completed task, and corresponding reasoning review.
  Document differences without treating library output as the sole authority.

These stages regulate disclosure, not just imports. Do not provide an answer
table, reference implementation, or solver-generated proof before its checkpoint.
Unrelated API mechanics can be explained directly under [AGENTS.md](AGENTS.md).

## Technology sequence

| Technology | Intended role | First planned use |
|---|---|---|
| NetworkX | Graph containers, interchange, generators, and supporting/comparison algorithms | [Lab 2](labs/02-dependencies/technology.md) |
| Neo4j and official Python driver | Persistent property-graph modeling, Cypher, updates, and Python interchange | [Lab 2](labs/02-dependencies/technology.md), revisited in [Lab 3](labs/03-matching/technology.md) |
| SciPy | Sparse arrays, selected eigenpairs, and exponential action | [Lab 12](labs/12-matrices/technology.md) onward |
| python-igraph | Optional alternative for a justified workload comparison | [Lab 16](labs/16-independent-project/technology.md) |
| Neo4j Graph Data Science | Optional algorithms on explicitly defined projections | [Lab 16](labs/16-independent-project/technology.md) |

NetworkX supplies [graph file interchange](https://networkx.org/documentation/stable/reference/readwrite/index.html)
and [SciPy sparse conversion](https://networkx.org/documentation/stable/reference/generated/networkx.convert_matrix.to_scipy_sparse_array.html).
SciPy supplies [selected symmetric eigenpairs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.eigsh.html)
and [matrix-exponential action](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.expm_multiply.html).
Neo4j's [official Python driver](https://neo4j.com/docs/python-manual/current/)
supports database interaction; its [GDS workflow](https://neo4j.com/docs/getting-started/gds/)
adds in-memory graph projections and algorithms. [python-igraph](https://python.igraph.org/en/stable/)
offers another graph representation and NetworkX interchange. Check versions
and compatible features when preparing the later dependency/setup step.

## Checks at representation boundaries

Before a larger experiment, state the mathematical graph and document how
each technology represents it. Select checks that protect the actual model:

| Boundary | Expected invariant or explicitly documented change |
|---|---|
| Tuples to a graph container | Explicit vertex IDs and isolates survive; direction and edge multiplicity agree |
| File or database round trip | Semantic vertices, relationships, and selected attributes survive; no reliance on incidental row order |
| Property graph to analysis graph | Relationship types, direction, filters, parallel-edge aggregation, and weights are specified |
| Graph to matrix | An explicit vertex order maps rows/columns back to IDs; weight meaning, normalization, and isolate convention agree |
| Dense to sparse | Small examples represent the same operator, including zero entries and boundary restrictions |
| Algorithm comparison | Validity, objective values, or appropriate invariants agree; nonunique witnesses need not be identical |
| Random generation | Model properties and within-implementation reproducibility are checked; equal seeds across libraries need not yield equal graphs |

Independent hand cases and mathematical arguments come first. Cross-library
agreement can miss shared assumptions or errors. A heuristic result is not an
optimality certificate. Numerical tolerances, residuals, and model adequacy
require separate justification.

## Neo4j scope and safeguards for the later setup step

Start with the existing synthetic dependency and linkage data in an isolated
study database. Plan stable domain IDs, uniqueness where required, explicit
relationship direction, repeatable imports, and preservation of unrelated data.
Keep credentials outside tracked files and use parameterized data values.
Define how unavailable service and rejected writes are reported. Agree on
version, local deployment, connection configuration, and cleanup before setup;
no cloud account, paid service, or GDS installation is assumed.

Database modeling is itself a learning objective. Directed stored relationships
do not automatically define the undirected analysis graph. Candidate links,
accepted assignments, and identity claims must remain distinct. GDS projections
require their own explicit model and validation; they are not synonymous with
the stored database or a guarantee of unlimited scale.

## Experiment and completion record

Use the relevant lab's existing notes to record: objective, library operations
used, permission stage, versions, data transformations, predictions, independent
checks, actual results, resource use, limitations, assistance, and review.
No extra progress file is required. Extension preparation and core completion
are separate; full Diestel/Chung reading and proof checkpoints remain unchanged.

Start with modest graphs whose runtime and memory are practical. Measure before
introducing another engine; using a library alone is not a scaling strategy.
Infrastructure tuning, broad benchmarking, GPU/distributed processing, and extra
libraries need a concrete question and their own approved scope.
