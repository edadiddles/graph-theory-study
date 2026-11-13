# Lab 15: heat evolution and continuous-time walks

How does graph structure control evolution, and which analytical claims require
more than a plotted trajectory? Work after the earlier spectral labs and read
[all Chung Chapters 9-12](reading.md). The [Chung audit](consolidation.md) covers
all twelve chapters; preparing these files does not complete that reading.

## Working arrangement

Read the contracts in [lab.py](lab.py), make independent attempts in [notes.md](notes.md),
and request focused review under [AGENTS.md](../../AGENTS.md). Functions are
intentionally unfinished. Tests are separate: make predictions and a hand
calculation before opening [test_lab.py](test_lab.py). No solution implementation
or worked inequality argument is included.

Use the existing [NumPy requirement](../../requirements.txt). Create your own
virtual environment and install it when reaching the lab. Then, from this lab's
directory, run `python -m unittest -v`. Unfinished tasks are expected to raise
`NotImplementedError`; numerical checks have not been run during preparation.

## 1. Choose coordinates before computing

For each supplied graph, draw it, record weighted degrees, and distinguish:

- A combinatorial Laplacian acting on a column of physical state values.
- A symmetric normalized operator acting on normalized coordinates.
- A continuous-time transition acting on a row probability distribution.
- A homogeneous Dirichlet restriction with the complementary boundary held at zero.

Derive the physical evolution you intend to model, including vertex capacities
if applicable; specify when the combinatorial operator is appropriate. Specify
units and what total quantity, weighted quantity, or norm should be conserved
or dissipated. Do not assume ordinary coordinate sums are conserved for every
operator. Derive any coordinate conversion you use rather than treating distinct
state conventions as interchangeable.

Before implementing, choose a small graph you can solve by hand. Predict its
initial behavior, long-time behavior, and the effect of changing weights. Record
how a disconnected component or isolate changes the prediction. For the weak
link in scenario 3, predict a qualitative comparison with the graph obtained by
removing that link; compute no result yet.

## 2. Implement two contracts

Implement `heat_kernel` and `continuous_time_transition` in `lab.py`. Their
matrix exponentials are mathematical specifications, not entrywise operations.
Explain why your method computes each specified operator. Existing NumPy is
the only dependency; no SciPy or general matrix-exponential package is required.
Document and justify reuse of earlier learner code without importing neighboring
files through ambiguous `lab` module names.

Address the specified time, dimension, weight, empty-graph, and isolate cases.
Finite symmetric PSD input is a precondition for the heat task; general spectral
validation is deferred. Keep unexpected programming errors visible.

## 3. Investigate evolution and boundaries

Use the supplied times only as an initial exploration grid, not as convergence
certificates. Record predictions before each experiment.

1. Compare combinatorial and normalized heat evolution on scenario 1. Derive
   what each state represents and identify a conservation or dissipation law.
2. Compare ordinary discrete-time walks from Lab 13 with the continuous-time
   model, paying attention to periodicity, stationary states, and time units.
3. Investigate scenario 2's isolate and scenario 3's weak connection. Explain
   which initial masses and component structure determine limiting behavior.
4. Reuse your Lab 14 boundary work for the supplied ordered interiors. Compare
   zero-boundary evolution with induced-graph evolution. State the physical or
   probabilistic interpretation before calling any loss of mass a numerical error.
5. Check time composition, numerical residuals, and sensitivity to the time grid
   and graph weights. Explain whether global rescaling should affect each model.

Plotting is optional; tables and NumPy calculations suffice. No new plotting
library is assumed. Distinguish a short-time approximation, a finite observation,
a limiting claim, and a bound proved uniformly over specified states or times.

## 4. Analytical investigations

For each of Chapters 9-12, select a result or proof passage from your actual copy
and reconstruct its reasoning. Record exact identifiers and hypotheses. These
investigations supplement every-section reading; they do not replace it.

For a Harnack or Sobolev statement, specify its domain, operator, measure, norms,
constants, positivity assumptions, boundary conditions, and allowed times as
applicable. Translate the actual statement into your notation before attempting
a hand example or numerical illustration. Do not invent a graph inequality by
analogy with a continuum formula. Explain how a chosen heat-kernel or advanced
walk result connects to an earlier spectral or isoperimetric result.

A finite computation can find an inconsistency or illustrate a theorem; it
cannot establish the general theorem. Keep analytical proof review separate
from test outcomes and numerical tolerances.

## Checkpoint

Present your hand example, correctness arguments, actual test results, one
interpreted evolution comparison, and selected analytical arguments. Complete
the [consolidation audit](consolidation.md) with evidence for all Chung reading
and proof checkpoints. Record unresolved questions and assistance before review.

Optional later extensions: relate the weak-link experiment to earlier
entity-resolution graphs, or compare a graph diffusion model with a discretized
PDE. Preserve the distinction between similarity propagation and shared identity.
