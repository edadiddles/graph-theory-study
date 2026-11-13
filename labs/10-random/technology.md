# Lab 10 technology extension: ensembles and graph interchange

## Learning focus

Use NetworkX for later ensembles and additional graph families, keeping attention
on model adequacy and reproducibility rather than repeated plumbing code.

## Independent work

The independent-edge sampler, draw contract, graph summaries, probability
derivations, and original observed-network predictions remain learner work.
The saved unweighted karate-club snapshot remains the core data source.

## Supporting operations

Practice converting the saved vertex/edge inventory to NetworkX and a documented
interchange format. Preserve isolates and omitted-attribute decisions. Choose a
larger experiment's model, parameters, size, statistic list, and seed plan before
running it. Do not substitute a library dataset silently for the pinned snapshot.

## Comparison after review

After the sampler, summary implementation, and probability reasoning review,
use NetworkX generators and summary algorithms for later ensembles. A different
generator family needs an explicit modeling question and assumptions. You need
not reimplement each new generator when its construction is not the objective,
but must explain the distribution it is intended to sample.

## Validation and report

Check independent tiny summary cases and graph interchange invariants. Check
within-library seed reproducibility, but do not require different generators to
produce identical graphs for the same seed. Boundary probabilities and derived
expectations inform checks; finite samples do not prove independence or provide
an automatic statistical pass/fail rule. Record versions, seeds, sample counts,
and all planned comparisons. Distinguish a fitted statistic from evaluation and
retain the original snapshot's provenance and projection limitations.

## Setup status and review record

Follow [shared technology guidance](../../TECHNOLOGIES.md) and
[the core exercise](exercise.md). The extension documentation is prepared;
versions, dependency/setup changes, extension code, and runtime checks remain
pending a separate approved step. Existing core dependency requirements still
apply. Record predictions, operations used, independent checks, actual outcomes,
assistance, limitations, and review in [notes.md](notes.md). This document
supplies no completed implementation, query answers, or proof.
