# Lab 12 technology extension: graph-to-matrix conversion

## Learning focus

Connect NetworkX representations with dense NumPy and sparse SciPy operators,
then use these tools for modest larger physical-network examples.

## Independent work

The initial incidence, adjacency, degree, and Laplacian assembly, quadratic form,
hand calculations, and physical-model arguments remain learner work. Library
matrix constructors must not replace the core assembly task.

## Supporting operations

Learn sparse-array storage and its distinction between stored entries and
mathematical nonzeros. Numerical linear solvers and eigensolvers may support
normal-mode/circuit work: implementing their internals is not this lab's
objective. Keep singularity, reference potentials, physical units, residuals,
and the chosen operator visible. Additional SciPy use awaits the setup step.

## Comparison after review

After reviewing independent matrix assembly and reasoning, use NetworkX matrix
conversion with an explicit vertex list and weight attribute. Compare a small
case with the learner's matrices before moving to larger sparse examples.
Compare incidence conventions explicitly; opposite edge orientations need not
produce identical incidence matrices. Later construction can be delegated once
the resulting operator and physical assumptions are justified.

## Validation and report

Check IDs, isolates, matrix ordering, weights, and shapes across conversion.
Compare dense and sparse small-case operators under agreed conventions. Record
symmetry, relevant quadratic forms, solver residuals, and boundary/reference
choices. Explain which outputs have physical meaning and which require another
model assumption. Avoid full dense conversion solely to inspect a larger sparse
operator; record actual memory/runtime constraints rather than assuming scale.

## Setup status and review record

Follow [shared technology guidance](../../TECHNOLOGIES.md) and
[the core exercise](exercise.md). The extension documentation is prepared;
versions, dependency/setup changes, extension code, and runtime checks remain
pending a separate approved step. Existing core dependency requirements still
apply. Record predictions, operations used, independent checks, actual outcomes,
assistance, limitations, and review in [notes.md](notes.md). This document
supplies no completed implementation, query answers, or proof.
