# Graph theory study roadmap

## Agreed approach

Study Trudeau, then Diestel, then Chung through reading, proofs, Python modeling,
and interpretation. Cover every section and proof in Diestel and Chung, with
selected exercises rather than every exercise. Review appendices as needed and
record them in the reading checklist. Do not treat a chapter as complete merely
because its associated lab works.

Use independent attempts with agent checkpoints under [AGENTS.md](AGENTS.md).
Clarification does not authorize solutions. Approve each milestone's lab scope
and validation plan before creating it. The overall roadmap and the lab scopes
for Milestones 1-5 are approved. Later lab ideas below are provisional.

Primary goals define the milestone. Ancillary goals support it and should be
studied when a gap appears. Keep supplementary reading selective. Use varied
applications, with entity resolution as a recurring thread.

## Core books

- Richard J. Trudeau, *Introduction to Graph Theory*: refresher; edition not yet
  recorded.
- Reinhard Diestel, *Graph Theory*, sixth edition (2025), ISBN 9783662701065.
- Fan R. K. Chung, *Spectral Graph Theory* (1997), ISBN 9780821803158.

Diestel and Chung were awaiting arrival when this roadmap was approved. Check
exact exercise references against the learner's copies before assigning them.

## Milestones

### 1. Refresh graph foundations

- **Reading:** selected Trudeau; Eccles for proof methods, Epp as an alternative.
- **Primary:** paths, cycles, components, trees, bridges, cut vertices; translate
  between descriptions, drawings, and Python representations.
- **Ancillary:** relations, quantifiers, equivalence relations, counterexamples;
  predictions before computation; distinguish proofs from empirical evidence.
- **Lab:** [entity-resolution connectivity](labs/01-connectivity/exercise.md),
  using supplied candidate edges and synthetic identities to investigate
  grouping errors and structural changes.
- **Checkpoint:** justify computed results and explain what connectivity does
  and does not establish about identity.
- **Status:** lab scope approved; scaffold created; learner work not started.

### 2. Foundations, proofs, and algorithms

- **Reading:** Diestel Chapter 1, *The Basics*, in full; selected CLRS and van Steen.
- **Primary:** precise definitions, short proofs, graph representations,
  traversal, reachability; introduce directed connectivity as supplementary work.
- **Ancillary:** induction, invariants, correctness, and algorithm analysis.
- **Lab:** [directed software dependencies](labs/02-dependencies/exercise.md),
  cycles, and potential change impact, with a separate
  [full Chapter 1 reading checklist](labs/02-dependencies/reading.md).
  The OSTEP resource-dependency case remains a later optional extension.
- **Checkpoint:** state hypotheses accurately, reconstruct a short proof, and
  explain the limits of a dependency model.
- **Status:** lab scope approved; scaffold created; learner completion not assessed.

### 3. Matching, covering, and packing

- **Reading:** Diestel Chapter 2 in full; CLRS for selected algorithms.
- **Primary:** bipartite and general matching, covering and packing, tree packing,
  arboricity, and path covers.
- **Ancillary:** feasibility versus optimization; one-to-one matching assumptions.
- **Lab:** [cross-database record linkage](labs/03-matching/exercise.md),
  supplemented by a [full Chapter 2 checklist](labs/03-matching/reading.md) and
  mathematical investigations for topics not represented by that application.
- **Checkpoint:** justify assignment constraints and distinguish the chapter's
  different matching, covering, and packing questions.
- **Status:** lab scope approved; scaffold created; learner completion not assessed.

### 4. Connectivity and resilience

- **Reading:** Diestel Chapter 3 in full; van Steen; TCP/IP for domain context.
- **Primary:** connectivity structure, separating sets, disjoint paths, Menger's
  theorem, and the chapter's further linking results.
- **Ancillary:** bounds and certificates; structural versus operational resilience.
- **Lab:** [station and connection failures](labs/04-resilience/exercise.md),
  supplemented by a [full Chapter 3 checklist](labs/04-resilience/reading.md).
  Learner tasks implement pairwise minimum separators; disjoint-path evidence
  is manual.
- **Checkpoint:** justify resilience claims and identify failures the model omits.
- **Status:** lab scope approved; scaffold created; learner completion not assessed.

### 5. Planarity and coloring

- **Reading:** Diestel Chapters 4 and 5 in full; Epp as needed; Gamelin and Greene
  only for topology questions that arise.
- **Primary:** plane and planar graphs, planarity criteria, duality, vertex and
  edge coloring, and the later coloring topics in the chapter.
- **Ancillary:** drawings versus graphs; feasible versus optimal schedules.
- **Lab:** [exam-conflict scheduling and manual planarity investigations](labs/05-coloring/exercise.md),
  supplemented by a [full Chapters 4-5 checklist](labs/05-coloring/reading.md).
  Conflict construction and minimum coloring are learner tasks; planarity is
  assessed through separate drawings and mathematical arguments.
- **Checkpoint:** explain the representation assumptions and justify bounds.
- **Status:** lab scope approved; scaffold created; learner completion not assessed.

### 6. Flows

- **Reading:** Diestel Chapter 6 in full; CLRS for network-flow algorithms.
- **Primary:** circulations, network flows, group-valued flows, flow-coloring
  duality, and the remaining results and conjectures presented in the chapter.
- **Ancillary:** distinguish capacity, cost, latency, and reliability.
- **Lab:** constrained distribution or service capacity; separate proof exercises
  for material beyond the application.
- **Checkpoint:** distinguish computed optima, proved results, and conjectures.

### 7. Extremal graph theory

- **Reading:** Diestel Chapter 7 in full.
- **Primary:** extremal subgraph and minor questions, regularity tools, and their
  applications as developed in the chapter.
- **Ancillary:** counting, asymptotic reasoning, and constructive examples.
- **Lab:** small extremal constructions and computational investigations, with
  explicit separation between finite experiments and general proofs.
- **Checkpoint:** explain the hypotheses and scope of the chapter's results.

### 8. Infinite graphs

- **Reading:** Diestel Chapter 8 in full; appendix on infinite sets as needed.
- **Primary:** infinite graph techniques, paths and ends, connectivity and
  matching, recursive structures, cycle spaces, and limits.
- **Ancillary:** finite versus infinite arguments and limits of computation.
- **Lab:** finite approximations paired with proof investigations; no claim that
  a finite experiment settles an infinite statement.
- **Checkpoint:** identify where arguments require finiteness or an infinite method.

### 9. Ramsey theory and Hamilton cycles

- **Reading:** Diestel Chapters 9 and 10 in full.
- **Primary:** Ramsey results and bounds; Hamilton-cycle existence criteria.
- **Ancillary:** necessary versus sufficient conditions and computational search.
- **Lab:** small Ramsey investigations and route-cycle examples.
- **Checkpoint:** distinguish existence, construction, and optimization.

### 10. Random graphs

- **Reading:** Diestel Chapter 11 in full; van Steen; Epp and Triola as needed.
- **Primary:** random graph models, probabilistic methods, typical properties,
  thresholds, and second-moment reasoning.
- **Ancillary:** conditional probability, expectation, variance, independence,
  simulation, and reproducibility.
- **Lab:** observed networks versus explicitly chosen generated baselines.
- **Checkpoint:** explain what a baseline preserves and what conclusions it permits.

### 11. Graph minors and Diestel consolidation

- **Reading:** Diestel Chapter 12 in full; remaining relevant appendix material;
  audit the section checklist for Chapters 1-12.
- **Primary:** well-quasi-ordering, tree decompositions, tree-width, tangles, and
  the graph minor theorem as developed in the book.
- **Ancillary:** structural representations and algorithmic implications.
- **Lab:** decomposition investigations plus a synthesis of earlier models.
- **Checkpoint:** complete all Diestel section/proof checkpoints and selected
  exercises before beginning the Chung sequence. Acknowledge any proofs the
  book cites rather than supplies; do not invent a requirement to reconstruct
  external proofs.

### 12. Linear algebra and physics bridge

- **Reading:** Anton and Rorres; Taylor Chapter 11; selected Chapra and Canale;
  Barnaal for circuit context.
- **Primary:** incidence, adjacency, and Laplacian matrices; nullspaces, quadratic
  forms, orthogonality, spectral decomposition, and Rayleigh quotients.
- **Ancillary:** normal modes, boundary conditions, conditioning, numerical error;
  probability and finite-state Markov-chain preparation.
- **Lab:** spring and resistor networks, starting with hand-solvable examples.
- **Checkpoint:** connect structure, physical equations, and numerical results.

### 13. Spectral foundations and applications

- **Reading:** Chung Chapters 1-4 in full; Spielman and Sethna selectively.
- **Primary:** graph Laplacians, isoperimetric problems, diameters, paths, flows,
  and routing through spectral methods.
- **Ancillary:** normalization conventions, Markov chains, and numerical eigensolvers.
- **Lab:** spectral partitioning and random-walk experiments; revisit the
  distinction between communities and entities.
- **Checkpoint:** state assumptions and interpret spectral results in the model.

### 14. Quasi-randomness, expanders, symmetry, and boundaries

- **Reading:** Chung Chapters 5-8 in full.
- **Primary:** quasi-randomness, expander constructions, symmetrical graphs,
  and eigenvalues with boundary conditions.
- **Ancillary:** algebra and probability refreshers as needed; structural versus
  spectral comparisons.
- **Lab:** compare graph families and boundary choices; choose the exact
  experiment after the prerequisite review.
- **Checkpoint:** connect proved spectral properties to observed behavior.

### 15. Spectral analysis and advanced random walks

- **Reading:** Chung Chapters 9-12 in full; Strauss, Sethna, and analysis references
  selectively; audit all Chung section/proof checkpoints.
- **Primary:** Harnack inequalities, heat kernels, Sobolev inequalities, and
  advanced techniques for random walks.
- **Ancillary:** required analysis, diffusion, and continuous/discrete comparisons.
- **Lab:** diffusion and boundary experiments paired with analytical exercises.
- **Checkpoint:** complete all Chung section/proof checkpoints and selected
  exercises, identifying where numerical evidence requires analytical support.

### 16. Independent modeling project

- **Reading:** references selected for the question; Kleppmann for data modeling
  where relevant. Rios is an optional systems implementation reference.
- **Primary:** formulate a question, justify a model, implement methods, validate
  results, and defend conclusions.
- **Ancillary:** evaluation design, uncertain labels, sensitivity, reproducibility.
- **Lab:** an independently selected application with a small exact case and a
  larger empirical case. Entity resolution remains an option.
- **Checkpoint:** present a defensible modeling argument and remaining limitations.

## Reading and completion records

Create section-level checklists when each milestone is prepared, using the
actual edition. Record section reading, proof attempts/reconstruction, selected
exercises, open questions, and review status separately. Read the full text,
including examples, notes, and discussions of conjectures; not every statement
is a theorem with a proof. Resolve or explicitly review open questions before
marking a milestone complete. Track learner completion separately from lab-file
creation and passing software checks.

## References for chapter mapping

- [Diestel sixth-edition contents](https://diestel-graph-theory.com/Contents.pdf)
- [Chung's book contents](https://fanchung.ucsd.edu/research/outline.html)
- [Van Steen's applied companion](https://www.distributed-systems.net/index.php/books/gtcn/)

The personal book inventory is separate: `/home/eruzek/git/library/books.csv`.
