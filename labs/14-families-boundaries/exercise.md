# Lab 14: Graph families, symmetry, and boundary choices

## Goal and reading

Investigate how structural assumptions and boundary choices change spectral
conclusions. Read Chung Chapters 5-8 in full using [reading.md](reading.md).
Finite examples illustrate ideas; they do not certify quasi-randomness or
expansion of an unspecified graph family.

Use the existing [NumPy requirement](../../requirements.txt) and
[Lab 12 setup instructions](../12-matrices/exercise.md). No environment or package
is created during preparation. Readings, proofs, and learner progress remain
separate from the existence of these files.

## Part 1: Graph comparisons before computation

The unweighted `FAMILY_GRAPHS` in `lab.py` are neutral finite examples, not a
sequence with an established asymptotic property. Before computing, use
[notes.md](notes.md):

1. Draw every graph and predict degree patterns, cut behavior, and spectral
   similarities or differences. Identify comparisons controlling both size and degree.
2. Choose disjoint vertex sets and a stated density baseline. Predict the edge
   count between them and its signed difference from that baseline.
3. Explain which comparisons change graph size, degree, or density and why that
   matters for a claim about expansion or random-looking structure.
4. Investigate the supplied candidate permutations as maps from the common
   vertex order to the listed images. Test automorphism claims mathematically
   before interpreting spectra. Relabeling and being an automorphism are distinct.
5. Select an explicit construction from Chapter 6. Work a small instance by hand
   and record the assumptions and proof obligations for a family-level statement.

Implement `cut_discrepancy` using the contract in `lab.py`. It measures signed
raw discrepancy across two disjoint sets, not a maximum over sets or a normalized
family invariant. Empty sides are allowed. Overlap, unknown IDs, and invalid
density raise ValueError. Valid simple undirected graph inputs are assumed.

Use the existing NumPy dependency or the standard library. Do not mutate inputs
or consult global fixtures. No discrepancy optimizer, general automorphism
solver, or expander classifier is supplied.

After predictions, compare cuts and spectra using your own earlier code where
justified. Record operator conventions and normalize comparisons explicitly
when your question requires it. Do not label a finite graph family quasi-random
because a few measurements look close to a density baseline.

## Part 2: Boundaries before computation

The weighted `BOUNDARY_CASES` specify an ordered interior and its complementary
boundary. Draw each case and hand-derive two matrices on that same interior:

- The principal restriction of the full normalized Laplacian, retaining full
  weighted degrees: a homogeneous Dirichlet problem in normalized coordinates.
- The normalized Laplacian of the induced interior graph, recomputing degrees
  after deleting the complement: a different graph model.

For each, predict eigenvalue and eigenvector behavior and identify where the
outside connections enter. Do not automatically call the induced operator a
Neumann boundary operator. Compare it with any actual Neumann convention in
the book only after deriving that convention.

Implement `boundary_operators`. Return both float64 matrices under the keys
`dirichlet` and `induced`, in the given interior order. Empty interior gives
two empty square arrays. Full interior gives the same full normalized matrix
in both. Zero rows/columns at isolates use each model's relevant degrees.

Unknown or duplicate interior vertices and invalid weights raise ValueError.
Other valid-input assumptions are explicit in the docstring. Do not mutate
inputs or consult fixtures. Justify any reuse of your own normalized-operator
work; no implementation of that earlier task is copied into this scaffold.

## Part 3: Mathematical attempts

1. State a quasi-randomness or discrepancy result with its graph sequence,
   quantifiers, and normalization explicit. Identify the gap between it and
   one measured cut.
2. State an expansion claim and explain what must be uniform across a proposed
   family. Distinguish a spectral observation from the construction's proof.
3. For a candidate symmetry, justify the preserved graph structure and derive
   the relevant matrix relationship. Do not infer a full automorphism group
   from a repeated eigenvalue or matching spectra.
4. Derive what is retained and lost in each boundary model. State the coordinates
   and boundary values before interpreting a vector as a physical quantity.
5. Select a Chapter 8 comparison and check its hypotheses. Do not infer an
   unrestricted eigenvalue inequality from a few examples of two different models.

Explain correctness and termination of the two code tasks. Numerical checks
support the experiments but do not replace these arguments.

## Part 4: Experiments and interpretation

After predictions, compare cuts, symmetries, and spectra. For the boundary cases,
inspect residuals, numerical tolerance, and sensitivity to the selected interior.
Eigenvector sign changes and different bases at repeated eigenvalues are not
automatically different mathematical conclusions.

Write a report distinguishing finite statistics, proved structural relationships,
asymptotic claims, and boundary-model assumptions. Explain what information a
communication or physical network application would need beyond these graphs.
Record limitations when comparing graphs of different size or degree.

## Behavioral checks and completion

After an independent attempt and setup, from the repository root:

```sh
.venv/bin/python -B -m unittest discover -s labs/14-families-boundaries -p 'test_*.py' -v
```

Run labs separately because module names are shared. Without NumPy the module
cannot import; after setup, untouched learner functions raise NotImplementedError.
Numerical execution remains pending while NumPy is absent.

Separate hand-counted cuts and hand-derived matrices check the definitions.
Other checks address shape, ordering, relabeling, scaling, isolates, residuals,
and invalid inputs. No test certifies an asymptotic family property or an
automorphism-group classification. Tolerances concern small well-scaled examples.
Discuss apparent contract conflicts before changing supplied tests.

- [ ] Finite comparison and boundary predictions recorded before computing.
- [ ] Mathematical prompts and construction/symmetry investigations reviewed.
- [ ] Both learner tasks pass numerical checks after setup.
- [ ] Report distinguishes models, finite evidence, and general guarantees.
- [ ] Chapters 5-8 read in full, section inventory verified, supplied proofs and
  selected exercises reviewed using the reading checklist.

Scaffold preparation does not complete learning. The agent follows the project's
gradual-assistance policy for review and clarification.

## Deferred work

Large constructions, general automorphism algorithms, optimal discrepancy search,
automatic family certification, extra numerical packages, graph-limit software,
and production safeguards require later planning and approval.
