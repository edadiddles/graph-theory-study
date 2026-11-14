# Graph theory study roadmap

## Revision status and scope

The redesign principles are approved: learning-sized milestones, a provisional
4-6 active-hour target, prerequisite diagnostics, agent-selected exercises, and
mixed assessments with focused review before advancement. The learner has
approved adoption of the revised 81-unit sequence. Existing lab directories
remain the source packages; the new M-IDs describe learning progress. Exact
exercise choices, quiz questions, and local scopes are finalized when reaching
each milestone. All learner completion remains unassessed.

M01 has a [prepared learning card](labs/01-connectivity/notes.md#m01-learning-card-agent-prepared),
with its initial prerequisite diagnostic reviewed. Focused preparation and
one Eccles exercise are assigned in the notes; Trudeau Exercises 5 and 11 are
verified from the learner's photographs and assigned there as well. Later units are mapped
but not locally prepared. The later Chung boundaries remain conditional on
original-copy inventories and effort calibration.

Study Trudeau, then Diestel, then Chung. Cover every main-text section, example,
note, and supplied proof in both principal books, with selected exercises and
appendix work as needed. The revised grouping changes packaging, not coverage.
Record cited results and conjectures accurately; external proofs are not silently
added as obligations. See [COVERAGE.md](COVERAGE.md) for the section and lab map.

Core books: Trudeau, *Introduction to Graph Theory*, ISBN 9781684112319
(chapter starts and selected exercise references supplied/verified from the learner's copy);
Diestel, *Graph Theory*, sixth edition (2025), ISBN 9783662701065; Chung,
*Spectral Graph Theory* (1997), ISBN 9780821803158. Check exact references against
the learner's copies; the earlier record of awaited delivery is not a current
claim about possession.

## Sizing, sessions, and progress

Each learning unit initially targets **4-6 active study hours**, including its
diagnostic, planned reading/proof work, selected exercises, focused experiment,
and mixed quiz. These are uncalibrated planning estimates, not measured durations,
deadlines, or grading rules. Each unit's initial estimate is 4-6 hours; advanced
proof units and the unverified later Chung allocation have lower confidence.
Review estimates after the first few completed units and when new evidence appears.

At milestone preparation, replace the common estimate with a local breakdown:
prerequisite check, reading/proofs, exercises, lab/application, and assessment.
Include planned technology work if it is assigned; price optional extensions and
remediation separately. Split an overloaded unit at a meaningful concept/proof
boundary with review. Keep every section and proof assigned. A long proof may
span sessions or refined milestones; it must not be rushed to meet an estimate.

At 81 units, simply multiplying the common range gives 324-486 active hours.
That is an illustration of the adopted scope, not a completion forecast: later
section inventories, actual pace, prerequisite work, and revised boundaries can
change it substantially. No calendar schedule is assumed.

Prepare short tasks with natural stopping points. End a session with where I
stopped, the next action, and an unresolved question in the existing lab notes,
using the revised M-ID. After an interruption, use a short prerequisite/retrieval
check to target refresh work. Progress is based on evidence, not a daily streak.

## Study and assessment cycle

Follow [ASSESSMENT.md](ASSESSMENT.md): diagnose prerequisites; address identified
gaps; study and attempt selected exercises; complete the focused lab work; take
closed-book reasoning followed by a separate open-book application; review and
reassess unmet objectives before the next milestone. Agents select exercises
at the milestone using the learner's pathway and verified edition/text access.
Questions and answers are not pre-generated into required startup material.

**E** means explain precisely, **A** means apply to an unfamiliar small example,
and **J** means justify or prove at the stated depth. The evidence column declares
required objectives; exact statements, selected proof identifiers, and assessment
coverage are recorded before study. Every assigned section and supplied proof
still requires review, including material beyond the representative quiz tasks.
Ancillary subjects support those objectives and are studied when gaps appear.

The next milestone waits until all required objectives have demonstrated readiness
at their declared depth. High aggregate marks cannot conceal an unmet objective.
Assisted practice is recorded separately from independent reassessment. Use the
existing gradual-help rules in [AGENTS.md](AGENTS.md).

## Existing labs and technology practice

The sixteen existing directories remain source lab packages, with their approved
core contracts, tests, data, and notes preserved. A package may serve several new
milestones. Its old number and `Milestone N` headings identify the original
bundle, not the new M-ID. Completing one new unit does not complete its entire
source lab. Use the [lab crosswalk](COVERAGE.md#existing-lab-crosswalk) before
following legacy whole-chapter or whole-lab completion instructions.

The learning sequence is adopted with existing paths retained. Changes to these
boundaries or a later file migration need review; existing tests still define
the learner functions' behavior. At local preparation, identify which tests apply
to that unit; later unfinished functions do not imply the current reasoning failed.
Code, dependencies, and database setup remain outside this documentation step.

Follow [TECHNOLOGIES.md](TECHNOLOGIES.md) and each source lab's `technology.md`.
Use libraries for supporting operations; preserve independent work where it is
the objective. Planned technology extensions can be separate 4-6 hour units when
their learning objectives would overload the associated mathematics. They are
not all silently included in every estimate. NetworkX representation/interchange,
a Neo4j dependency-to-linkage workflow, and SciPy sparse experiments are the
initial progression; optional igraph/GDS remains question-driven. Versions,
runnable setup/scaffolds, and runtime validation remain a separate approved step.

Use owned supplementary books first, with targeted lectures and legitimate online
resources from [SUPPLEMENTS.md](SUPPLEMENTS.md). Physical books are preferred;
new purchases are recommendations only. Exact supplementary sections and lecture
segments are selected from verified material for an identified learning purpose.

## Adopted milestone sequence

Reading notation: **D** = the assigned Diestel edition; **C** = the assigned
Chung edition. All listed section ranges include the full text and supplied
proofs. Every row has the initial 4-6 hour estimate described above. Numbering
can be refined through review as actual effort and section inventories clarify
learning dependencies and coverage.

## Foundations and graph language

Diagnose quantifiers, relations, proof structure, induction, and graph vocabulary. Use Eccles or Epp selectively. Directed dependency work supplements Diestel; the full Chapter 1 reading remains assigned across M02-M05.

| Milestone | Reading scope | Required learning evidence | Focus and ancillary support |
|---|---|---|---|
| M01: Refresh graph reasoning | Trudeau refresher | E: paths, components, trees, and identity assumptions; A: component discovery and deletion predictions; J: connectivity relation and model limitations. | [Source lab](labs/01-connectivity/exercise.md). Relations, quantifiers, proof structure. |
| M02: Graph language, degrees, and paths | D 1.1-1.3 | E: graph objects and degree/path conventions; A: translate examples between drawings and representations; J: selected counting and path arguments. | [Source lab](labs/02-dependencies/exercise.md). Notation, counting, counterexamples. |
| M03: Connectivity, trees, and bipartite structure | D 1.4-1.6 | E: connectivity, tree, and bipartite definitions; A: implement reachability and examine examples; J: selected equivalences and traversal reasoning. | [Source lab](labs/02-dependencies/exercise.md). Induction, invariants; reuse Lab 1. |
| M04: Minors and Euler tours | D 1.7-1.8 | E: graph operations and tour conventions; A: construct small minors and tours; J: selected existence criteria and their hypotheses. | [Source lab](labs/02-dependencies/exercise.md). Finite constructions; distinguish paths and tours. |
| M05: Graph algebra and directed dependencies | D 1.9-1.10 | E: chapter algebra and alternative graph notions; A: implement SCCs and interpret dependency impact; J: partition/correctness arguments and selected algebra results. | [Source lab](labs/02-dependencies/exercise.md). Targeted linear algebra; explicit direction. |

## Matching and connectivity

Check earlier connectivity and proof reasoning. Diagnose counting, terminal conventions, and optimization/certificate distinctions. Use CLRS only for the selected supporting purpose and respect disclosure gates.

| Milestone | Reading scope | Required learning evidence | Focus and ancillary support |
|---|---|---|---|
| M06: Bipartite matching and record linkage | D 2.1 | E: assignment and covering constraints; A: implement maximum matching on tiny cases; J: optimality and the section's matching/covering argument. | [Source lab](labs/03-matching/exercise.md). Relations, ambiguity, one-record-per-source assumption. |
| M07: General matching and covering/packing | D 2.2-2.3 | E: general matching and covering/packing statements; A: investigate separate small examples; J: selected supplied arguments with exact hypotheses. | [Source lab](labs/03-matching/exercise.md). Feasibility versus optimum; chapter topics beyond linkage. |
| M08: Tree packing, arboricity, and path covers | D 2.4-2.5 | E: distinguish the three objectives; A: construct examples or certificates; J: selected bounds and their scope. | [Source lab](labs/03-matching/exercise.md). Counting and decomposition; retain linkage interpretation. |
| M09: Two- and three-connected structure | D 3.1-3.2 | E: connectivity structure and separators; A: analyze small station graphs; J: selected structural claims. | [Source lab](labs/04-resilience/exercise.md). Local versus global connectivity. |
| M10: Menger and pairwise resilience | D 3.3 | E: terminal and path conventions; A: implement minimum separators; J: minimum claims with independent path/separation evidence. | [Source lab](labs/04-resilience/exercise.md). Certificates; structural versus operational failure. |
| M11: Further linking results | D 3.4-3.5 | E: A-path and linking hypotheses; A: investigate small instances; J: selected Mader/linking proof passages. | [Source lab](labs/04-resilience/exercise.md). Quantifiers and path constraints. |

## Planarity, coloring, and flows

Check graph operations, drawings, and graph algebra before planarity; review groups only where algebraic flows require them. Planarity and coloring are separate learning units, connected again by planar coloring and flow duality.

| Milestone | Reading scope | Required learning evidence | Focus and ancillary support |
|---|---|---|---|
| M12: Plane embeddings and drawings | D 4.1-4.3 | E: plane versus planar graph and drawing conventions; A: analyze faces/drawings; J: selected counting statements and drawing claims. | [Source lab](labs/05-coloring/exercise.md). Targeted topology; no coloring implementation yet. |
| M13: Planarity criteria | D 4.4-4.5 | E: obstruction and algebraic criteria; A: attempt small certificates; J: selected planarity arguments. | [Source lab](labs/05-coloring/exercise.md). Subdivisions/minors and graph algebra. |
| M14: Plane duality | D 4.6 | E: dual construction and embedding dependence; A: construct duals; J: selected primal/dual relationships. | [Source lab](labs/05-coloring/exercise.md). Prepare later map coloring and flow duality. |
| M15: Map and vertex coloring | D 5.1-5.2 | E: proper coloring and planar hypotheses; A: build conflicts and implement minimum coloring; J: lower/upper bounds and optimality. | [Source lab](labs/05-coloring/exercise.md). Scheduling assumptions; keep planar/nonplanar cases distinct. |
| M16: Edge and list coloring | D 5.3-5.4 | E: edge/list constraints; A: formulate distinct assignment problems; J: selected coloring arguments. | [Source lab](labs/05-coloring/exercise.md). Feasible choices and constraint modeling. |
| M17: Perfect graphs and chi-boundedness | D 5.5-5.6 | E: graph versus graph-class quantifiers; A: investigate examples; J: selected results with their exact scope. | [Source lab](labs/05-coloring/exercise.md). Induced subgraphs; no general classification solver. |
| M18: Circulations and capacity flows | D 6.1-6.2 | E: conservation and capacity conventions; A: implement flow and cut tasks; J: correctness and optimality evidence. | [Source lab](labs/06-flows/exercise.md). Units, terminal conventions, certificates. |
| M19: Group-valued and small-k flows | D 6.3-6.4 | E: algebraic flow definitions; A: work small examples; J: selected supplied results. | [Source lab](labs/06-flows/exercise.md). Targeted group refresher; distinguish ordered capacities. |
| M20: Flow-coloring duality and conjectures | D 6.5-6.6 | E: duality hypotheses and conjecture status; A: compare an embedding/flow example; J: supplied arguments and interpretation limits. | [Source lab](labs/06-flows/exercise.md). Revisit M14-M16; no obligation to solve conjectures. |

## Extremal graph theory

Diagnose counting, asymptotic notation, and quantifier order. Advanced regularity arguments have high effort uncertainty; refine boundaries before assigning them rather than compressing proofs into a nominal time budget.

| Milestone | Reading scope | Required learning evidence | Focus and ancillary support |
|---|---|---|---|
| M21: Extremal subgraphs | D 7.1 | E: forbidden-subgraph objective; A: implement triangle detection and tiny extremal construction; J: optimality/completeness and selected bounds. | [Source lab](labs/07-extremal/exercise.md). Counting and finite-versus-general claims. |
| M22: Extremal minors and Hadwiger | D 7.2-7.3 | E: subgraph/minor distinctions and statement status; A: inspect minor examples; J: selected supplied arguments. | [Source lab](labs/07-extremal/exercise.md). Revisit contraction and coloring. |
| M23: The regularity lemma | D 7.4 | E: definitions and quantifier order; A: examine a small schematic example; J: reconstruct selected proof structure. | [Source lab](labs/07-extremal/exercise.md). Asymptotics; high effort uncertainty. |
| M24: Applying regularity | D 7.5 | E: hypotheses in an application; A: trace an example of their use; J: selected application argument. | [Source lab](labs/07-extremal/exercise.md). Counting, parameter dependencies. |
| M25: Further regularity tools | D 7.6 | E: distinguish the two tools; A: unpack their conditions; J: selected supplied arguments. | [Source lab](labs/07-extremal/exercise.md). Parameter order; high effort uncertainty. |
| M26: Szemeredi's theorem | D 7.7 | E: the statement and graph translation; A: investigate the correspondence; J: trace the supplied argument. | [Source lab](labs/07-extremal/exercise.md). Connections beyond graph objects; high effort uncertainty. |

## Infinite graphs, Ramsey theory, and Hamilton cycles

Diagnose infinite-set prerequisites before M27 and use Appendix A selectively. Check distinctions between a witness, exhaustive search, an existence theorem, and an asymptotic claim. Topology is targeted support, not a second full course.

| Milestone | Reading scope | Required learning evidence | Focus and ancillary support |
|---|---|---|---|
| M27: Infinite graphs, paths, and ends | D 8.1-8.2 | E: infinite definitions and finite windows; A: implement truncation/deletion tasks; J: selected finite/infinite distinctions. | [Source lab](labs/08-infinite/exercise.md). Appendix A as needed; no infinite claim from finite tests. |
| M28: Universal graphs and infinite linking | D 8.3-8.4 | E: universality/connectivity/matching hypotheses; A: examine examples; J: selected infinite arguments. | [Source lab](labs/08-infinite/exercise.md). Set principles and quantifiers. |
| M29: Recursive structures and ends | D 8.5-8.6 | E: recursive and end structure; A: trace a construction; J: selected proof mechanisms. | [Source lab](labs/08-infinite/exercise.md). Review finite/infinite proof assumptions. |
| M30: The topological cycle space | D 8.7 | E: objects and topology used; A: interpret a small representation; J: selected supplied arguments. | [Source lab](labs/08-infinite/exercise.md). Topology only as needed; high effort uncertainty. |
| M31: Infinite graphs as limits | D 8.8 | E: the text's limit notions; A: compare finite-window evidence; J: a supplied limit argument. | [Source lab](labs/08-infinite/exercise.md). Convergence quantifiers and limitations of computation. |
| M32: Ramsey existence and numbers | D 9.1-9.2 | E: quantifiers and bound conventions; A: implement monochromatic-triangle witnesses; J: existence/bound arguments. | [Source lab](labs/09-ramsey-hamilton/exercise.md). Counting and search completeness. |
| M33: Induced Ramsey results and connectivity | D 9.3-9.4 | E: embedding and connectivity assumptions; A: investigate small cases; J: selected supplied arguments. | [Source lab](labs/09-ramsey-hamilton/exercise.md). Induced versus ordinary subgraphs. |
| M34: Hamilton-cycle conditions | D 10.1 | E: necessary/sufficient distinctions; A: implement a cycle witness task; J: witness validity and selected criteria. | [Source lab](labs/09-ramsey-hamilton/exercise.md). Existence, construction, and optimization. |
| M35: Degree sequences and graph squares | D 10.2-10.3 | E: the two additional settings; A: examine examples; J: selected supplied Hamilton arguments. | [Source lab](labs/09-ramsey-hamilton/exercise.md). Graph transformations and theorem hypotheses. |

## Random graphs

Run the probability diagnostic before M36: conditional probability, independence, expectation/variance, elementary bounds, and asymptotic language. Add focused preparation from SUPPLEMENTS.md when needed; verify second-moment prerequisites before M39.

| Milestone | Reading scope | Required learning evidence | Focus and ancillary support |
|---|---|---|---|
| M36: Random graph models and moments | D 11.1 | E: probability space and independent-edge assumptions; A: implement G(n,p) sampling and summaries; J: model/distribution and moment arguments. | [Source lab](labs/10-random/exercise.md). Probability diagnostic before starting; targeted preparation if needed. |
| M37: The probabilistic method | D 11.2 | E: random construction versus existence proof; A: work a selected existence example; J: the probability argument establishing existence. | [Source lab](labs/10-random/exercise.md). Probability bounds; simulation is different evidence. |
| M38: Typical random-graph properties | D 11.3 | E: almost-all/asymptotic quantifiers; A: plan and run a small ensemble; J: compare a supplied theorem with finite evidence. | [Source lab](labs/10-random/exercise.md). Fitting versus evaluation; reproducibility. |
| M39: Thresholds and second moments | D 11.4 | E: threshold and moment conventions; A: interpret a controlled comparison; J: a selected second-moment argument. | [Source lab](labs/10-random/exercise.md). Variance/covariance and asymptotics; high effort uncertainty. |

## Graph minors and Diestel consolidation

Check order relations, induction, and separation conventions. Read every remaining Diestel section and supplied proof. M45 closes the complete Diestel audit before the Chung sequence; it does not impose reconstruction of proofs only cited externally.

| Milestone | Reading scope | Required learning evidence | Focus and ancillary support |
|---|---|---|---|
| M40: Well-quasi-ordering and trees | D 12.1-12.2 | E: order and tree-minor statements; A: trace small examples; J: selected supplied arguments. | [Source lab](labs/11-decompositions/exercise.md). Quantifiers, induction, and order relations. |
| M41: Tree decompositions and width | D 12.3-12.4 | E: all decomposition conditions; A: implement validity and width tasks; J: correctness and justified width bounds. | [Source lab](labs/11-decompositions/exercise.md). Local representation versus global property. |
| M42: Tangles | D 12.5 | E: the text's separation/tangle conventions; A: analyze a small instance; J: selected supplied proof structure. | [Source lab](labs/11-decompositions/exercise.md). High effort uncertainty; split further if needed. |
| M43: Decompositions and forbidden minors | D 12.6 | E: the structural connection; A: trace a relevant example; J: selected supplied argument. | [Source lab](labs/11-decompositions/exercise.md). Keep implications and hypotheses explicit. |
| M44: The graph minor theorem | D 12.7 | E: theorem scope and cited results; A: connect earlier constructions; J: supplied arguments, distinguishing external proofs. | [Source lab](labs/11-decompositions/exercise.md). High effort uncertainty; no invented external obligations. |
| M45: Diestel synthesis and review | Diestel full-course audit | E: connect major concepts; A: transfer earlier ideas to an unfamiliar case; J: defend selected arguments and resolve recorded gaps. | [Source lab](labs/11-decompositions/exercise.md). All D sections/proofs and selected exercises reviewed before Chung study. |

## Linear algebra, physics, and Markov bridge

Run the linear-algebra and Markov diagnostics. These units integrate existing knowledge with graph models; demonstrated prior understanding can reduce required practice. Use physical intuition from owned texts and distinguish equations, state conventions, and numerical error.

| Milestone | Reading scope | Required learning evidence | Focus and ancillary support |
|---|---|---|---|
| M46: Symmetric linear algebra bridge | Owned linear algebra; targeted diagnostics | E: subspaces, PSD, and spectral conventions; A: small hand spectral analysis; J: selected Rayleigh/variational arguments. | [Source lab](labs/12-matrices/exercise.md). Anton-Rorres; focused supplementary preparation. |
| M47: Graph matrices and energy | Lab 12 matrix conventions | E: incidence, adjacency, degree, and Laplacian; A: implement matrix assembly and quadratic form; J: graph/matrix relationships. | [Source lab](labs/12-matrices/exercise.md). Ordering, weights, orientation, and isolates. |
| M48: Normal modes | Taylor Ch 11, selected portions | E: physical state and units; A: analyze a hand-checkable oscillator graph; J: equation/operator interpretation. | [Source lab](labs/12-matrices/exercise.md). Symmetric eigensolver use; residuals. |
| M49: Resistor networks | Barnaal, selected portions | E: conductance/current/reference assumptions; A: solve a hand-checkable network; J: conservation and boundary interpretation. | [Source lab](labs/12-matrices/exercise.md). Conditioning and linear-system residuals. |
| M50: Finite-state Markov chains | Owned references; optional targeted Levin-Peres | E: stationarity, reversibility, irreducibility, and periodicity; A: hand transition examples; J: selected stationary/convergence reasoning. | [Source lab](labs/12-matrices/exercise.md). Probability diagnostic and row/column conventions. |

## Chung foundations, inequalities, distances, and routing

Require the Diestel review and relevant bridge readiness. Diagnose variational reasoning, weighted inner products, and finite-state walks before use. Core numerical implementation and proof work remain separate; supporting numerical/path algorithms can be delegated as documented.

| Milestone | Reading scope | Required learning evidence | Focus and ancillary support |
|---|---|---|---|
| M51: Laplacians and spectral facts | C 1.1-1.3 | E: spectrum and normalization conventions; A: assemble/review normalized Laplacians; J: selected spectral facts. | [Source lab](labs/13-spectral-foundations/exercise.md). PSD, variational reasoning, isolates. |
| M52: Weighted graphs and random walks | C 1.4-1.5 | E: weighted setting and transition conventions; A: complete ordinary/lazy operator work; J: relations and stationarity arguments. | [Source lab](labs/13-spectral-foundations/exercise.md). Compare book loops/weights with narrower lab inputs. |
| M53: Cheeger constants and edge expansion | C 2.1-2.3 | E: relevant cut/volume definitions; A: implement conductance and examine candidate cuts; J: a selected spectral/isoperimetric argument. | [Source lab](labs/13-spectral-foundations/exercise.md). Normalization, bounds versus minimization. |
| M54: Vertex expansion and characterization | C 2.4-2.5 | E: distinguish expansion notions; A: compare examples; J: selected characterization arguments. | [Source lab](labs/13-spectral-foundations/exercise.md). Hypotheses and weighted measures. |
| M55: Cartesian-product inequalities | C 2.6 | E: product definitions and constants; A: investigate a small product; J: selected supplied argument. | [Source lab](labs/13-spectral-foundations/exercise.md). Tensor/product intuition as needed. |
| M56: Diameters and distances between sets | C 3.1-3.2 | E: distance and spectral-bound conventions; A: compare graph distances and bounds; J: selected distance argument. | [Source lab](labs/13-spectral-foundations/exercise.md). Supporting shortest-path routines permitted under technology guidance. |
| M57: Many subsets and the manifold comparison | C 3.3-3.4 | E: compared objects/hypotheses; A: interpret examples; J: selected supplied arguments and scope. | [Source lab](labs/13-spectral-foundations/exercise.md). Targeted geometry/analysis; graph numerics do not prove manifold claims. |
| M58: Paths, flows, and Cheeger constants | C 4.1-4.2 | E: path/flow setting; A: compare earlier network models; J: selected spectral flow argument. | [Source lab](labs/13-spectral-foundations/exercise.md). Revisit M10/M18/M53. |
| M59: Congestion and routing | C 4.3-4.4 | E: route demand and congestion; A: investigate a tiny routing model; J: distinguish a bound from a constructed route. | [Source lab](labs/13-spectral-foundations/exercise.md). Operational assumptions and supporting algorithms. |
| M60: Spectral comparison theorems | C 4.5 | E: compared quantities and implication direction; A: test hypotheses on an example; J: reconstruct a selected comparison argument. | [Source lab](labs/13-spectral-foundations/exercise.md). Earlier paths, flow, and expansion results. |

## Later Chung chapters: provisional learning boundaries

Before finalizing any of these units, inventory every section in the assigned 1997 copy and allocate all sections/proofs between its two proposed units. Refine or add units to preserve the 4-6 hour target. No section numbers or complete workload estimate for these chapters are claimed here.

| Milestone | Reading scope | Required learning evidence | Focus and ancillary support |
|---|---|---|---|
| M61: Quasi-randomness and finite statistics | C Ch 5, first part: boundaries pending | E: actual definitions and quantifiers; A: implement signed cut discrepancy; J: relate the statistic to an actual chapter statement. | [Source lab](labs/14-families-boundaries/exercise.md). Original-copy inventory required; probability and density assumptions. |
| M62: Quasi-randomness: remaining arguments | C Ch 5, remaining sections/proofs | E: remaining chapter concepts; A: compare a selected family example; J: selected general relationships. | [Source lab](labs/14-families-boundaries/exercise.md). Pending section allocation; cover every remaining topic. |
| M63: Expander constructions | C Ch 6, first part: boundaries pending | E: actual construction and family parameters; A: work a small instance; J: trace its guarantee. | [Source lab](labs/14-families-boundaries/exercise.md). Targeted algebra/probability; no generator answer before independent work. |
| M64: Expanders: applications and remaining topics | C Ch 6, remaining sections/proofs | E: remaining chapter concepts; A: investigate an appropriate application; J: separate proved guarantees from finite evidence. | [Source lab](labs/14-families-boundaries/exercise.md). Pending section allocation; uniform family claims. |
| M65: Symmetry and spectra | C Ch 7, first part: boundaries pending | E: actual symmetry notions; A: verify proposed maps on examples; J: a spectral relationship. | [Source lab](labs/14-families-boundaries/exercise.md). Permutations and targeted algebra. |
| M66: Symmetry: remaining arguments | C Ch 7, remaining sections/proofs | E: remaining chapter concepts; A: extend a symmetry investigation; J: selected supplied arguments. | [Source lab](labs/14-families-boundaries/exercise.md). Pending section allocation; matching spectra are not an automorphism proof. |
| M67: Boundary operators | C Ch 8, first part: boundaries pending | E: operator, coordinates, and boundary values; A: implement paired boundary operators; J: their differing interpretations. | [Source lab](labs/14-families-boundaries/exercise.md). Original versus induced degrees; inherited zero-degree convention. |
| M68: Boundary theory: remaining models and results | C Ch 8, remaining sections/proofs | E: the book's other boundary settings; A: compare with the lab's narrower models; J: selected supplied arguments. | [Source lab](labs/14-families-boundaries/exercise.md). Pending section allocation; induced normalization is not automatically Neumann. |
| M69: Harnack statements and hypotheses | C Ch 9, first part: boundaries pending | E: actual inequality and its hypotheses; A: translate notation and examine an admissible example; J: explain roles of assumptions. | [Source lab](labs/15-heat-walks/exercise.md). Targeted analysis; original-copy inventory required. |
| M70: Harnack arguments and remaining topics | C Ch 9, remaining sections/proofs | E: remaining chapter concepts; A: connect a statement to an earlier spectral setting; J: selected supplied arguments. | [Source lab](labs/15-heat-walks/exercise.md). Pending section allocation; finite tests are illustrations. |
| M71: Finite heat kernels | C Ch 10, first part: boundaries pending | E: kernel and state conventions; A: implement symmetric heat evolution; J: hand example and implementation argument. | [Source lab](labs/15-heat-walks/exercise.md). Matrix exponential, coordinates, and boundaries. |
| M72: Heat, walks, and remaining kernel results | C Ch 10, remaining sections/proofs | E: actual remaining kernel/walk statements; A: implement continuous-time transitions; J: evolution and selected analytical arguments. | [Source lab](labs/15-heat-walks/exercise.md). Pending section allocation; mass preservation is model-dependent. |
| M73: Sobolev statements and norms | C Ch 11, first part: boundaries pending | E: actual norms, measures, and function class; A: translate and investigate a statement; J: assumptions and selected proof steps. | [Source lab](labs/15-heat-walks/exercise.md). Targeted analysis; no continuum formula substituted silently. |
| M74: Sobolev arguments and remaining topics | C Ch 11, remaining sections/proofs | E: remaining chapter concepts; A: connect to earlier isoperimetry; J: selected supplied arguments. | [Source lab](labs/15-heat-walks/exercise.md). Pending section allocation; all proofs remain required. |
| M75: Advanced walk techniques | C Ch 12, first part: boundaries pending | E: an actual chapter technique and assumptions; A: analyze its use on an appropriate example; J: its supplied argument. | [Source lab](labs/15-heat-walks/exercise.md). Stationarity, convergence, and state conventions. |
| M76: Advanced walks: remaining results | C Ch 12, remaining sections/proofs | E: remaining chapter concepts; A: compare analytical claims with finite observations; J: selected supplied arguments. | [Source lab](labs/15-heat-walks/exercise.md). Pending section allocation; numerical evidence versus guarantees. |

## Synthesis and independent project

The Chung audit checks all chapters, supplied proofs, selected exercises, and unresolved questions. Project preparation may occur earlier, but final completion requires both book audits and all required assessments. Scope project implementation to the agreed question.

| Milestone | Reading scope | Required learning evidence | Focus and ancillary support |
|---|---|---|---|
| M77: Chung synthesis and review | Chung full-course audit | E: connect operators, cuts, and evolution; A: transfer to an unfamiliar model; J: defend arguments and review all recorded gaps. | [Source lab](labs/15-heat-walks/exercise.md). Every C section/proof, selected exercise record, and inventory checked. |
| M78: Project question and graph model | Question-specific references | E: application and model assumptions; A: complete a bounded project brief; J: method and evaluation rationale. | [Source lab](labs/16-independent-project/exercise.md). Data provenance, uncertain labels, practical scope. |
| M79: Project small case and justification | Verified results needed by the project | E: required method assumptions; A: independently derive expected results and implement the agreed slice; J: proof/certificate/bound. | [Source lab](labs/16-independent-project/exercise.md). Focused tests, reproducibility, error visibility. |
| M80: Project empirical investigation | Question-specific supplementary work | E: baseline and sensitivity purpose; A: run the planned larger case; J: conclusions within observed evidence. | [Source lab](labs/16-independent-project/exercise.md). Resource use, versions, and numerical limitations. |
| M81: Project defense and study completion | Both full-course audits | E: complete modeling argument; A: present reproducible evidence; J: defend conclusions and limitations. | [Source lab](labs/16-independent-project/exercise.md). Reading/proof/quiz records and unresolved questions reviewed. |

## Completion and next preparation

Begin M01 with the prerequisite diagnostic described in its learning card. Use
the results and verified textbook access to finish exercise selection and any
focused preparation. The card supplies objectives, a quiz blueprint, and session
stopping points. Questions for an actual assessment are generated only when the
learner is ready. Advancement to M02 requires M01's readiness evidence.

Full study completion requires reviewed records for all Diestel and Chung
sections/supplied proofs, selected exercises, needed appendices, required milestone
assessments, and the final modeling argument. Keep code checks, lab preparation,
technology practice, and learning readiness distinct. Later Chung inventories
and local proof/exercise identifiers remain explicit preparation gaps.

Source mappings: [Diestel contents](https://diestel-graph-theory.com/Contents.pdf),
[Chung chapter outline](https://fanchung.ucsd.edu/research/outline.html), and the
linked edition-specific reading records. The personal book inventory remains
separate at `/home/eruzek/git/library/books.csv`.
