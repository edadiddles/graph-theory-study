# Lab 13 technology extension: sparse spectra and supporting paths

## Learning focus

Use NetworkX graph handling and SciPy selected eigenpairs to investigate larger
spectral examples without implementing numerical linear algebra internals.

## Independent work

Normalized operator assembly, conductance, initial partitions, coordinate
relationships, and the chapter's proof work remain learner tasks. Library
operator or conductance answers wait for the corresponding review.

## Supporting operations

Use a symmetric eigensolver for a justified operator, including SciPy's sparse
selected-eigenpair interface after setup. Explain which part of the spectrum
you request and why it addresses the question; implementation of the eigensolver
is not required. For a distance-bound investigation, library shortest paths are
permitted without first implementing Dijkstra, because shortest-path construction
is not this task. State weight meaning, admissible weights, direction, and the
difference between a route and a spectral distance bound. If shortest-path
implementation becomes a separate learning task, its solver answers are gated.

## Comparison after review

After the core operator/conductance implementation and reasoning review, use
library assembly and scoring to accelerate larger experiments. Do not introduce
a partition routine that performs a still-unattempted spectral investigation;
complete and review that investigation first. Preserve the saved karate graph's
unweighted projection if reusing it.

## Validation and report

Compare selected eigenvalues with dense small-case results, and check residuals
and orthogonality using appropriate tolerances. Account for repeated eigenvalues,
nullspace multiplicity, and sign/basis ambiguity. Verify explicit vertex ordering,
normalization, isolates, and probability conventions across conversions. Compare
cut scores rather than assuming one numerical eigenvector or partition is unique.
Explain what the experiments establish about cuts, walks, or distances and what
they do not establish about entity identity or globally optimal partitions.

## Setup status and review record

Follow [shared technology guidance](../../TECHNOLOGIES.md) and
[the core exercise](exercise.md). The extension documentation is prepared;
versions, dependency/setup changes, extension code, and runtime checks remain
pending a separate approved step. Existing core dependency requirements still
apply. Record predictions, operations used, independent checks, actual outcomes,
assistance, limitations, and review in [notes.md](notes.md). This document
supplies no completed implementation, query answers, or proof.
