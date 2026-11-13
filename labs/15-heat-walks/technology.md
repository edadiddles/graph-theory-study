# Lab 15 technology extension: sparse evolution

## Learning focus

Use SciPy matrix-exponential action to evolve states on larger sparse operators
without requiring a full dense heat-kernel matrix.

## Independent work

The small `heat_kernel` and `continuous_time_transition` implementations, initial
hand example, coordinate conversions, and analytical investigations remain
learner work. A library exponential must not replace the core task or generate
its initial predicted answers.

## Supporting operations

Sparse graph storage and operator handling may be delegated under the earlier
representation checks. Derive which operator, state orientation, and boundary
model your proposed larger experiment needs before choosing a numerical API.
Keep physical time distinct from the dimensionless jump-attempt convention.

## Comparison after review

After the corresponding heat/transition implementations and reasoning review,
use SciPy's `expm_multiply` for later evolution experiments. It computes the
action of an exponential on a state or collection of states; it does not return
the full kernel by default. Do not implement its numerical internals. Explain
how its interface matches your chosen row or column convention, without treating
symmetric heat evolution as an ordinary probability transition on every graph.

## Validation and report

Compare the sparse action with an independently checked small dense-kernel
application. Check initial state, time composition, and relevant conservation,
dissipation, absorbing-isolate, and disconnected-block properties. Choose the
checks for the actual boundary model: ordinary mass preservation is not a
universal requirement. Record residuals/tolerances where meaningful, selected
times, runtime, and memory implications. No finite experiment proves convergence
or a Harnack/Sobolev inequality; review those arguments separately.

## Setup status and review record

Follow [shared technology guidance](../../TECHNOLOGIES.md) and
[the core exercise](exercise.md). The extension documentation is prepared;
versions, dependency/setup changes, extension code, and runtime checks remain
pending a separate approved step. Existing core dependency requirements still
apply. Record predictions, operations used, independent checks, actual outcomes,
assistance, limitations, and review in [notes.md](notes.md). This document
supplies no completed implementation, query answers, or proof.
