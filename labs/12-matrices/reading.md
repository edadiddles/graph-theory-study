# Milestone 12: Linear algebra and physics bridge

This checklist selects supporting subjects rather than assigning another entire
book. Choose exact sections from your actual copies and record them in `notes.md`.
No unverified section numbers or exercise identifiers are assigned.

## Linear algebra: Anton and Rorres

- [ ] Subspaces, rank, nullspaces, and basis/dimension refreshed where needed.
- [ ] Inner products, orthogonality, and symmetric diagonalization reviewed.
- [ ] Quadratic forms and positive semidefiniteness reviewed.
- [ ] Spectral decomposition, multiplicity, and Rayleigh-quotient reasoning reviewed.
- [ ] Selected exercises attempted; gaps and assistance recorded.

Connect each topic with a graph example, but keep a mathematical argument
separate from a numerical illustration. Use Shankar or Griffiths quantum
mechanics only as alternative physical intuition if useful.

## Normal modes: Taylor, Chapter 11

- [ ] Relevant coupled-oscillator and normal-mode material reviewed.
- [ ] Unit-mass assumptions, boundary conditions, and frequency units stated.
- [ ] A hand-solvable example compared with the graph-matrix formulation.
- [ ] Selected exercise or derivation attempted and reviewed.

Do not introduce generalized mass matrices or full dynamical simulation solely
to reproduce a static spectral calculation in this first bridge.

## Circuits: Barnaal, with Anton and Rorres as support

- [ ] Relevant passive-network material located and reviewed.
- [ ] Resistance versus conductance and current conservation refreshed.
- [ ] Reference potential and balanced current assumptions made explicit.
- [ ] A hand-solvable circuit compared with the graph equations.
- [ ] Selected exercise or derivation attempted and reviewed.

Use Griffiths electrodynamics for context only when it addresses a specific
physical question. No additional electrodynamics course is a prerequisite.

## Numerical methods: Chapra and Canale

- [ ] Relevant linear-system and eigenvalue material consulted selectively.
- [ ] Conditioning, floating-point error, and residuals distinguished.
- [ ] Numerical tolerance choices explained for the actual small experiments.
- [ ] Singular systems and boundary-model issues kept visible.

Consult Dubin or Hassani as an alternative if a particular explanation fits
better. Python/NumPy is the computational environment; MATLAB or Mathematica
installation is not required.

## Finite-state Markov-chain preparation

- [ ] Probability distributions and stochastic-matrix conventions stated.
- [ ] A small transition example worked by hand with consistent row/column choices.
- [ ] Stationary distributions distinguished from convergence to stationarity.
- [ ] Questions about irreducibility, periodicity, and isolated states recorded.

Check your Anton-Rorres copy for its Markov-chain applications material before
assigning exact sections. Use Sethna selectively for random-walk intuition.
Record uncovered gaps for the Chung milestone rather than assuming a reference
contains every topic or that all chains have the same long-term behavior.

## Bridge review

- [ ] Matrix definitions, proof attempts, and coding tasks reviewed.
- [ ] Physics experiments, units, and numerical evidence reviewed.
- [ ] Reading sections and selected exercises actually consulted are recorded.
- [ ] Remaining prerequisites for the Chung sequence identified explicitly.

The NumPy pin is in [requirements.txt](../../requirements.txt). Its
[release notes](https://numpy.org/doc/2.5/release/2.5.0-notes.html) document supported
Python versions; installing it and creating a virtual environment are left to
the learner when reaching this lab.
