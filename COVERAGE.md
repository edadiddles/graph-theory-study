# Reading coverage and existing lab crosswalk

## Scope and verification status

This map connects the adopted M-IDs in [ROADMAP.md](ROADMAP.md) to the existing
source labs. It preserves required reading scope without moving directories or
changing learner implementations, tests, data, or notes. Existing `Lab N` and
`Milestone N` headings inside those directories describe the original bundles.
The learner has approved adoption of this grouping with existing paths retained.
Local scopes are prepared when reached; any file migration requires later review.

Every assigned section includes definitions, examples, discussion, notes, and
all supplied proofs. For each section, the agent records actual proof identifiers,
attempts/reconstruction, assistance, gaps, and review evidence in the source
lab's notes under its new M-ID. Cited external proofs and open conjectures are
recorded accurately. Quiz sampling does not substitute for all-section/proof
review. All learning and proof completion is currently unassessed.

The 71 Diestel section labels and the first 20 Chung labels below are inherited
from the edition-specific reading records and their linked author contents.
They still need checking against the learner's copies. Their mapping is complete
relative to those records; this is not a claim to have individually inventoried
all theorem/proof identifiers. A fresh fetch of Diestel's contents was unavailable
during this revision, so no new edition verification is implied.

Chung Chapters 5-12 have chapter-level ownership below. Their original-copy
section inventories remain pending; section-level coverage cannot yet be
certified. No titles/counts are invented from the later revised edition. Before
starting those units, inventory every actual section/proof and assign it to one
primary owner, refining the conditional units when needed to fit the effort target.

## How to use legacy lab instructions

A source lab can span several new milestones. Prepare and review each new local
scope and quiz blueprint when reached. Under the adopted mapping,
whole-chapter reading and whole-lab completion instructions are distributed across
all listed owners, not silently imposed again on the first small unit. Behavioral
function contracts and existing tests retain their meaning. Some tests will
remain intentionally unready until a later function is implemented; select
applicable tests at local preparation without rewriting or weakening the suite.

Original wording about choosing exercises is implemented through agent selection
under [ASSESSMENT.md](ASSESSMENT.md). The learner supplies relevant exercise
pages only when needed for verified access; exercise selection remains the agent's
job. Update a source lab's final completion record only after every assigned unit,
required core task, and relevant reading/proof obligation has been reviewed.

## Existing lab crosswalk

| Existing source package | Primary learning owners | Core implementation ownership | Reading record |
|---|---|---|---|
| [01-connectivity](labs/01-connectivity/exercise.md) | M01 | connected_components: M01 | Trudeau refresher in exercise |
| [02-dependencies](labs/02-dependencies/exercise.md) | M02-M05 | reachable_vertices: M03; strongly_connected_components: M05 | [Checklist](labs/02-dependencies/reading.md) |
| [03-matching](labs/03-matching/exercise.md) | M06-M08 | maximum_matching: M06 | [Checklist](labs/03-matching/reading.md) |
| [04-resilience](labs/04-resilience/exercise.md) | M09-M11 | minimum_vertex_separator and minimum_edge_separator: M10 | [Checklist](labs/04-resilience/reading.md) |
| [05-coloring](labs/05-coloring/exercise.md) | M12-M17 | build_conflict_edges and minimum_coloring: M15; manual planarity: M12-M14 | [Checklist](labs/05-coloring/reading.md) |
| [06-flows](labs/06-flows/exercise.md) | M18-M20 | maximum_flow and minimum_cut: M18 | [Checklist](labs/06-flows/reading.md) |
| [07-extremal](labs/07-extremal/exercise.md) | M21-M26 | contains_triangle and maximum_triangle_free_graph: M21 | [Checklist](labs/07-extremal/reading.md) |
| [08-infinite](labs/08-infinite/exercise.md) | M27-M31 | truncate_graph and component_sizes_after_deletion: M27 | [Checklist](labs/08-infinite/reading.md) |
| [09-ramsey-hamilton](labs/09-ramsey-hamilton/exercise.md) | M32-M35 | monochromatic_triangle: M32; hamiltonian_cycle: M34 | [Checklist](labs/09-ramsey-hamilton/reading.md) |
| [10-random](labs/10-random/exercise.md) | M36-M39 | sample_gnp and graph_summary: M36 | [Checklist](labs/10-random/reading.md) |
| [11-decompositions](labs/11-decompositions/exercise.md) | M40-M45 | is_tree_decomposition and decomposition_width: M41 | [Checklist](labs/11-decompositions/reading.md) |
| [12-matrices](labs/12-matrices/exercise.md) | M46-M50 | graph_matrices and quadratic_form: M47; physics: M48-M49; Markov bridge: M50 | [Checklist](labs/12-matrices/reading.md) |
| [13-spectral-foundations](labs/13-spectral-foundations/exercise.md) | M51-M60 | normalized_operators: M52, with normalized-Laplacian reasoning in M51; conductance: M53 | [Checklist](labs/13-spectral-foundations/reading.md) |
| [14-families-boundaries](labs/14-families-boundaries/exercise.md) | M61-M68 | cut_discrepancy: M61; boundary_operators: M67 | [Checklist](labs/14-families-boundaries/reading.md) |
| [15-heat-walks](labs/15-heat-walks/exercise.md) | M69-M77 | heat_kernel: M71; continuous_time_transition: M72 | [Checklist](labs/15-heat-walks/reading.md) |
| [16-independent-project](labs/16-independent-project/exercise.md) | M78-M81 | Question/code/tests determined locally in M78-M81; no implementation supplied | [Checklist](labs/16-independent-project/reading.md) |

## Diestel section ownership

All twelve chapters and 71 inherited main-text section labels are assigned
exactly once below. Chapter exercises and notes remain required at their
relevant chapter review, with selected exercises chosen adaptively. Review
Appendix A (infinite sets) and Appendix B (surfaces) as needed and record actual
portions consulted. Use the existing [Diestel audit](labs/11-decompositions/consolidation.md)
as the evidence record; its original lab references remain valid.

| Assigned section and inherited title | Primary learning owner | Source reading checklist |
|---|---|---|
| D 1.1: Graphs | M02 | [Reading](labs/02-dependencies/reading.md) |
| D 1.2: The degree of a vertex | M02 | [Reading](labs/02-dependencies/reading.md) |
| D 1.3: Paths and cycles | M02 | [Reading](labs/02-dependencies/reading.md) |
| D 1.4: Connectivity | M03 | [Reading](labs/02-dependencies/reading.md) |
| D 1.5: Trees and forests | M03 | [Reading](labs/02-dependencies/reading.md) |
| D 1.6: Bipartite graphs | M03 | [Reading](labs/02-dependencies/reading.md) |
| D 1.7: Contraction and minors | M04 | [Reading](labs/02-dependencies/reading.md) |
| D 1.8: Euler tours | M04 | [Reading](labs/02-dependencies/reading.md) |
| D 1.9: Some linear algebra | M05 | [Reading](labs/02-dependencies/reading.md) |
| D 1.10: Other notions of graphs | M05 | [Reading](labs/02-dependencies/reading.md) |
| D 2.1: Matching in bipartite graphs | M06 | [Reading](labs/03-matching/reading.md) |
| D 2.2: Matching in general graphs | M07 | [Reading](labs/03-matching/reading.md) |
| D 2.3: The Erdos-Posa theorem | M07 | [Reading](labs/03-matching/reading.md) |
| D 2.4: Tree packing and arboricity | M08 | [Reading](labs/03-matching/reading.md) |
| D 2.5: Path covers | M08 | [Reading](labs/03-matching/reading.md) |
| D 3.1: 2-Connected graphs and subgraphs | M09 | [Reading](labs/04-resilience/reading.md) |
| D 3.2: The structure of 3-connected graphs | M09 | [Reading](labs/04-resilience/reading.md) |
| D 3.3: Menger's theorem | M10 | [Reading](labs/04-resilience/reading.md) |
| D 3.4: A-paths and Mader's theorem | M11 | [Reading](labs/04-resilience/reading.md) |
| D 3.5: Linking pairs of vertices | M11 | [Reading](labs/04-resilience/reading.md) |
| D 4.1: Topological prerequisites | M12 | [Reading](labs/05-coloring/reading.md) |
| D 4.2: Plane graphs | M12 | [Reading](labs/05-coloring/reading.md) |
| D 4.3: Drawings | M12 | [Reading](labs/05-coloring/reading.md) |
| D 4.4: Planar graphs: Kuratowski's theorem | M13 | [Reading](labs/05-coloring/reading.md) |
| D 4.5: Algebraic planarity criteria | M13 | [Reading](labs/05-coloring/reading.md) |
| D 4.6: Plane duality | M14 | [Reading](labs/05-coloring/reading.md) |
| D 5.1: Colouring maps and planar graphs | M15 | [Reading](labs/05-coloring/reading.md) |
| D 5.2: Colouring vertices | M15 | [Reading](labs/05-coloring/reading.md) |
| D 5.3: Colouring edges | M16 | [Reading](labs/05-coloring/reading.md) |
| D 5.4: List colouring | M16 | [Reading](labs/05-coloring/reading.md) |
| D 5.5: Perfect graphs | M17 | [Reading](labs/05-coloring/reading.md) |
| D 5.6: Chi-bounded graph properties | M17 | [Reading](labs/05-coloring/reading.md) |
| D 6.1: Circulations | M18 | [Reading](labs/06-flows/reading.md) |
| D 6.2: Flows in networks | M18 | [Reading](labs/06-flows/reading.md) |
| D 6.3: Group-valued flows | M19 | [Reading](labs/06-flows/reading.md) |
| D 6.4: k-Flows for small k | M19 | [Reading](labs/06-flows/reading.md) |
| D 6.5: Flow-colouring duality | M20 | [Reading](labs/06-flows/reading.md) |
| D 6.6: Tutte's flow conjectures | M20 | [Reading](labs/06-flows/reading.md) |
| D 7.1: Subgraphs | M21 | [Reading](labs/07-extremal/reading.md) |
| D 7.2: Minors | M22 | [Reading](labs/07-extremal/reading.md) |
| D 7.3: Hadwiger's conjecture | M22 | [Reading](labs/07-extremal/reading.md) |
| D 7.4: Szemeredi's regularity lemma | M23 | [Reading](labs/07-extremal/reading.md) |
| D 7.5: Applying the regularity lemma | M24 | [Reading](labs/07-extremal/reading.md) |
| D 7.6: Two regularity tools | M25 | [Reading](labs/07-extremal/reading.md) |
| D 7.7: Szemeredi's theorem | M26 | [Reading](labs/07-extremal/reading.md) |
| D 8.1: Basic notions, facts and techniques | M27 | [Reading](labs/08-infinite/reading.md) |
| D 8.2: Paths, trees, and ends | M27 | [Reading](labs/08-infinite/reading.md) |
| D 8.3: Homogeneous and universal graphs | M28 | [Reading](labs/08-infinite/reading.md) |
| D 8.4: Connectivity and matching | M28 | [Reading](labs/08-infinite/reading.md) |
| D 8.5: Recursive structures | M29 | [Reading](labs/08-infinite/reading.md) |
| D 8.6: Graphs with ends: the complete picture | M29 | [Reading](labs/08-infinite/reading.md) |
| D 8.7: The topological cycle space | M30 | [Reading](labs/08-infinite/reading.md) |
| D 8.8: Infinite graphs as limits of finite ones | M31 | [Reading](labs/08-infinite/reading.md) |
| D 9.1: Ramsey's original theorems | M32 | [Reading](labs/09-ramsey-hamilton/reading.md) |
| D 9.2: Ramsey numbers | M32 | [Reading](labs/09-ramsey-hamilton/reading.md) |
| D 9.3: Induced Ramsey theorems | M33 | [Reading](labs/09-ramsey-hamilton/reading.md) |
| D 9.4: Ramsey properties and connectivity | M33 | [Reading](labs/09-ramsey-hamilton/reading.md) |
| D 10.1: Sufficient conditions | M34 | [Reading](labs/09-ramsey-hamilton/reading.md) |
| D 10.2: Hamilton cycles and degree sequences | M35 | [Reading](labs/09-ramsey-hamilton/reading.md) |
| D 10.3: Hamilton cycles in the square of a graph | M35 | [Reading](labs/09-ramsey-hamilton/reading.md) |
| D 11.1: The notion of a random graph | M36 | [Reading](labs/10-random/reading.md) |
| D 11.2: The probabilistic method | M37 | [Reading](labs/10-random/reading.md) |
| D 11.3: Properties of almost all graphs | M38 | [Reading](labs/10-random/reading.md) |
| D 11.4: Threshold functions and second moments | M39 | [Reading](labs/10-random/reading.md) |
| D 12.1: Well-quasi-ordering | M40 | [Reading](labs/11-decompositions/reading.md) |
| D 12.2: The graph minor theorem for trees | M40 | [Reading](labs/11-decompositions/reading.md) |
| D 12.3: Tree-decompositions | M41 | [Reading](labs/11-decompositions/reading.md) |
| D 12.4: Tree-width | M41 | [Reading](labs/11-decompositions/reading.md) |
| D 12.5: Tangles | M42 | [Reading](labs/11-decompositions/reading.md) |
| D 12.6: Tree-decompositions and forbidden minors | M43 | [Reading](labs/11-decompositions/reading.md) |
| D 12.7: The graph minor theorem | M44 | [Reading](labs/11-decompositions/reading.md) |

## Chung Chapters 1-4 section ownership

The 20 inherited section labels remain subject to comparison with the assigned
1997 copy. Every section and supplied proof is required, including material not
implemented by the lab. Verify identifiers before selecting work.

| Assigned section and inherited title | Primary learning owner | Source reading checklist |
|---|---|---|
| C 1.1: Introduction | M51 | [Reading](labs/13-spectral-foundations/reading.md) |
| C 1.2: The Laplacian and eigenvalues | M51 | [Reading](labs/13-spectral-foundations/reading.md) |
| C 1.3: Basic facts about the spectrum of a graph | M51 | [Reading](labs/13-spectral-foundations/reading.md) |
| C 1.4: Eigenvalues of weighted graphs | M52 | [Reading](labs/13-spectral-foundations/reading.md) |
| C 1.5: Eigenvalues and random walks | M52 | [Reading](labs/13-spectral-foundations/reading.md) |
| C 2.1: History | M53 | [Reading](labs/13-spectral-foundations/reading.md) |
| C 2.2: The Cheeger constant of a graph | M53 | [Reading](labs/13-spectral-foundations/reading.md) |
| C 2.3: The edge expansion of a graph | M53 | [Reading](labs/13-spectral-foundations/reading.md) |
| C 2.4: The vertex expansion of a graph | M54 | [Reading](labs/13-spectral-foundations/reading.md) |
| C 2.5: A characterization of the Cheeger constant | M54 | [Reading](labs/13-spectral-foundations/reading.md) |
| C 2.6: Isoperimetric inequalities for cartesian products | M55 | [Reading](labs/13-spectral-foundations/reading.md) |
| C 3.1: The diameter of a graph | M56 | [Reading](labs/13-spectral-foundations/reading.md) |
| C 3.2: Eigenvalues and distances between two subsets | M56 | [Reading](labs/13-spectral-foundations/reading.md) |
| C 3.3: Eigenvalues and distances among many subsets | M57 | [Reading](labs/13-spectral-foundations/reading.md) |
| C 3.4: Eigenvalue upper bounds for manifolds | M57 | [Reading](labs/13-spectral-foundations/reading.md) |
| C 4.1: Paths and sets of paths | M58 | [Reading](labs/13-spectral-foundations/reading.md) |
| C 4.2: Flows and Cheeger constants | M58 | [Reading](labs/13-spectral-foundations/reading.md) |
| C 4.3: Eigenvalues and routes with small congestion | M59 | [Reading](labs/13-spectral-foundations/reading.md) |
| C 4.4: Routing in graphs | M59 | [Reading](labs/13-spectral-foundations/reading.md) |
| C 4.5: Comparison theorems | M60 | [Reading](labs/13-spectral-foundations/reading.md) |

## Chung Chapters 5-12: pending original-copy inventory

Each chapter has two provisional learning units. Their combined obligation is
**every actual section, example, note, and supplied proof in that chapter**.
The split is not a claim about chapter length or an exhaustive topic list.
Before assigning either part, enter every original-copy section and proof into
its reading record and allocate the work explicitly. Add/refine units if needed;
do not discard topics to keep two slots or the common time estimate.

| Chapter from the author's outline | Proposed owners together | Source inventory | Remaining preparation |
|---|---|---|---|
| 5. Eigenvalues and quasi-randomness | M61-M62 | [Lab 14](labs/14-families-boundaries/reading.md) | All original-copy sections/proofs; split pending |
| 6. Expanders and explicit constructions | M63-M64 | [Lab 14](labs/14-families-boundaries/reading.md) | All original-copy sections/proofs; split pending |
| 7. Eigenvalues of symmetrical graphs | M65-M66 | [Lab 14](labs/14-families-boundaries/reading.md) | All original-copy sections/proofs; split pending |
| 8. Eigenvalues of subgraphs with boundary conditions | M67-M68 | [Lab 14](labs/14-families-boundaries/reading.md) | All original-copy sections/proofs; split pending |
| 9. Harnack inequalities | M69-M70 | [Lab 15](labs/15-heat-walks/reading.md) | All original-copy sections/proofs; split pending |
| 10. Heat kernels | M71-M72 | [Lab 15](labs/15-heat-walks/reading.md) | All original-copy sections/proofs; split pending |
| 11. Sobolev inequalities | M73-M74 | [Lab 15](labs/15-heat-walks/reading.md) | All original-copy sections/proofs; split pending |
| 12. Advanced techniques on random walks | M75-M76 | [Lab 15](labs/15-heat-walks/reading.md) | All original-copy sections/proofs; split pending |

The [Chung audit](labs/15-heat-walks/consolidation.md) remains the final learning
record. M77 reviews all twelve chapters; it does not fill missing inventories
by inference. Appendix material is consulted as needed, with scope recorded.

## Technology crosswalk

These are planned extensions with preserved disclosure gates and pending runnable
setup. Budget a selected extension explicitly or prepare it as its own reviewed
unit. They are not eleven additional invisible requirements in every math estimate.

| Source extension | Related learning units | Intended role |
|---|---|---|
| [Lab 2](labs/02-dependencies/technology.md) | M03-M05 and a separately scoped database unit | NetworkX representation; Neo4j import/query/export after relevant reasoning review |
| [Lab 3](labs/03-matching/technology.md) | M06-M08 and database continuation | Candidate evidence, records, and assignments kept distinct |
| [Lab 4](labs/04-resilience/technology.md) | M09-M11 | Comparisons after core separator review |
| [Lab 5](labs/05-coloring/technology.md) | M12-M17 | Planarity/coloring comparisons after the corresponding work |
| [Lab 6](labs/06-flows/technology.md) | M18-M20 | Capacity experiments after core flow/cut review |
| [Lab 10](labs/10-random/technology.md) | M36-M39 | Later ensembles/interchange after core sampler and probability review |
| [Lab 12](labs/12-matrices/technology.md) | M47-M49 | Matrix conversion after independent assembly; sparse support |
| [Lab 13](labs/13-spectral-foundations/technology.md) | M51-M60 | Selected eigenpairs and supporting paths without bypassing core objectives |
| [Lab 14](labs/14-families-boundaries/technology.md) | M61-M68 | Generated instances after the relevant independent construction |
| [Lab 15](labs/15-heat-walks/technology.md) | M71-M72 and later numerical comparison | Sparse exponential action after the core heat/walk tasks |
| [Lab 16](labs/16-independent-project/technology.md) | M78-M81 | Question-driven tools; optional igraph/GDS |

## Coverage review checklist

- [x] Learner approved adoption of the revised sequence and provisional effort target.
- [ ] All 71 Diestel and 20 inherited Chung labels checked against assigned copies.
- [ ] Chung Chapters 5-12 original-copy inventories completed and sections allocated.
- [ ] Every assigned supplied proof has an identifier and reviewed evidence record.
- [ ] Every source learner function and original investigation assigned/reviewed.
- [ ] Selected exercises have verified statements and declared purposes.
- [ ] All required objective readiness, appendix work, and remaining gaps reviewed.

Preparation of this map checks assignment coverage, not learner completion or
mathematical correctness of an unattempted proof. Existing runtime limitations
for numerical labs and planned technology setup remain visible in their sources.
