# Lab 12: Graph matrices, springs, and resistor networks

## Goal and reading

Connect graph structure to systems of equations, normal modes, and physical
interpretation. Work from hand predictions to numerical experiments while
keeping mathematical proof, numerical evidence, and physical assumptions distinct.

Use [reading.md](reading.md) for selected topics in your existing books. This is
a prerequisite bridge, not an additional whole-book assignment. No new Diestel
or Chung chapter is assigned. Keep the Diestel consolidation record separate
from preparing this lab's files.

## Setup when you reach this lab

NumPy is the first external dependency and is listed in the root
[requirements.txt](../../requirements.txt). No virtual environment or installation
has been created as part of preparing this lab. NumPy 2.5.0 supports Python
3.12-3.14 according to its [release notes](https://numpy.org/doc/2.5/release/2.5.0-notes.html).

When ready, from the repository root:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -B -m unittest discover -s labs/12-matrices -p 'test_*.py' -v
```

Use a Python version compatible with the pin. Earlier standard-library labs
remain usable without this dependency. Run labs separately because their module
names are shared. Without NumPy this lab cannot import; after installation,
the untouched learner functions still raise NotImplementedError. Neither state
means that the numerical behavior checks have passed.

## Matrix and model conventions

Vertices are ordered explicitly; that order determines matrix rows and columns.
Edges are undirected, but their supplied endpoint order chooses an orientation
for the incidence matrix. Its columns follow edge order, with -1 at the tail
and +1 at the head. Weights follow the same edge order and are strictly positive.

The four output matrices are unweighted incidence B, weighted adjacency A,
weighted degree D, and combinatorial weighted Laplacian L. Their precise shapes
and definitions are in `lab.py`. This L is not a normalized Laplacian. Keep
isolated vertices and empty shapes explicit. General invalid graph inputs are
deferred; invalid weights and vector dimensions have specified errors.

For mechanical experiments, vertices are unit masses and edges are ideal linear
springs. Weights represent spring constants. For electrical experiments, the
same graph shape represents resistors, but weights represent conductances.
Record units separately; a weight is not simultaneously a spring constant and
an electrical conductance. The supplied `vector` is a numerical test vector;
choose and state its physical interpretation in each experiment.

## Part 1: Predict before computing

Use [notes.md](notes.md) before implementation or test inspection.

1. Draw each scenario and hand-assemble its four matrices under the chosen
   conventions. Record any uncertainty and distinguish weighted degree from
   number of neighbors.
2. Predict the action of L on constant vectors and investigate its nullspace.
   Relate claims to connectivity, including the disconnected example.
3. Predict the effect of reversing an incidence orientation, permuting vertices,
   and changing a weight. Keep representation changes separate from model changes.
4. For the supplied vectors, predict the sign and value of the quadratic form.
   Attempt an expression in terms of graph edges and justify it mathematically.
5. Predict qualitative motions or potentials for a physical example, including
   the role of free translation or reference potential.

## Part 2: Mathematical attempts

1. Derive relationships among the four matrices, incidence orientation, and
   weights. State the roles of dimensions and vertex/edge ordering explicitly.
2. Attempt proofs of symmetry, semidefiniteness, and the nullspace claims you
   make. Numerical eigenvalues alone are not proof.
3. State a Rayleigh-quotient claim under its precise conditions and investigate
   it on a hand-solvable example. Distinguish a value on one vector from an extremum.
4. Derive the relevant spring and circuit equations from physical assumptions.
   Identify which quadratic expressions represent energy or power, including
   the factors and units required by each interpretation.
5. Explain why an ungrounded resistor problem can lack a unique potential and
   what a legitimate boundary condition changes. Distinguish this from an
   inconsistent injection vector or an unexpected programming defect.

## Part 3: Implement assembly and the quadratic form

Complete `graph_matrices` and `quadratic_form` in `lab.py` using NumPy. The first
returns exactly the four arrays defined by its contract; the second evaluates
the scalar quadratic form without solving a physical problem.

Check the specified weight and dimension failures with ValueError. Do not mutate
inputs, consult global scenarios, or hide unexpected errors. Choose an assembly
approach you can justify. NumPy supplies numerical linear algebra for your later
experiments; no general eigensolver or circuit solver is a learner coding task.

Explain correctness and termination. Run after predictions, preserve the original
matrices and calculations, and investigate discrepancies before revising them.

## Part 4: Normal-mode experiments

Use the first four connected scenarios for initial physical experiments. Use
scenario 5 to investigate matrix properties and the limitations of transferring
connected-network conclusions; a general disconnected circuit solver is deferred.

For unit masses and ideal springs, derive the eigenvalue problem before calling
NumPy's [eigh](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigh.html).
Interpret mode shapes and frequencies with units and boundary assumptions visible.
Compare a hand-solvable case with numerical eigenvalues. Check residuals and
orthogonality without requiring eigenvectors to have a fixed sign. Repeated
eigenvalues can admit different bases; do not mistake a basis difference for a
different physical conclusion.

Record numerical tolerances and explain why they suit the small examples.
Do not silently replace small negative roundoff values or mask unexplained
residuals before investigating them.

## Part 5: Resistor-network experiments

Choose a connected scenario, a balanced current-injection vector, and an explicit
reference potential. Derive the resulting equations and identify the unknowns
before using NumPy's [solve](https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html).
Keep boundary treatment as learner work rather than copying a complete solution.

Check the original-node equations and conservation after recovering potentials.
Interpret potential differences, currents, and power. Compare against a hand
calculation, then investigate changing a conductance or the reference potential.

Do not hide singular-system errors with a zero vector or silently choose a
least-squares replacement. The model and boundary conditions must justify the
system being solved. Time dependence, generalized mass matrices, and disconnected
DC solves are outside the initial experiments.

## Behavioral checks and completion

After the hand attempt and environment setup, run the command above. Separate
known examples check matrices and scalar values. Other checks address ordering,
orientation, shapes, nullspaces, residuals, invalid inputs, and preservation.
Physical checks use a separate two-node example rather than solving the main
scenarios. There is no reference graph-assembly implementation.

The numerical tolerances in tests apply to their small well-scaled fixtures,
not arbitrary networks. Tests do not prove spectral results or physical validity.
Discuss apparent contract conflicts before changing supplied tests.

- [ ] Hand predictions, matrix conventions, and physical assumptions recorded.
- [ ] Mathematical prompts attempted and reviewed, with gaps addressed.
- [ ] Both learner functions pass numerical behavior checks after setup.
- [ ] Normal-mode and grounded-circuit experiments checked against hand reasoning.
- [ ] Units, residuals, tolerances, and model limitations explained.
- [ ] Targeted reading and Markov-chain preparation reviewed.

Preparing these files does not complete learner work. The agent follows the
project's gradual-assistance policy for review and clarification.

## Deferred work

Normalized Laplacians enter the Chung sequence. Sparse solvers, generalized mass
matrices, time integration, arbitrary disconnected boundary problems, plotting
packages, and production numerical safeguards require later planning and approval.

## Technology extension

See [technology.md](technology.md) for the approved technology-study addition,
including task-specific library permissions and validation prompts. The core
exercise and tests above retain their existing scope. Technology setup and
runnable extension work remain a separate step; this addition does not complete
any learner work. Earlier deferred-work statements apply to the core exercise;
the extension describes the additional planned scope explicitly.
