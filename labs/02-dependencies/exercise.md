# Lab 2: Directed software dependencies

## Goal and reading

Investigate reachability, cycles, and mutual reachability in a small package
ecosystem. Connect your computation to definitions and proof arguments, and
explain the limits of a dependency model.

Read Diestel Chapter 1 in full using [reading.md](reading.md). The directed-graph
experiment complements the chapter; it does not cover every topic in it.
Selected CLRS and van Steen material can support graph representations,
traversal, and directed connectivity. Choose supplementary sections by topic in
your own copies; exact exercise numbers have not been assigned.

## Model

Inspect the eight package names and five neutral scenarios in `lab.py`. Every
package exists in every scenario, including packages with no incident edges.

An edge `A -> B` means **package A directly depends on package B**. It does not
state that A is installed, currently running, or necessarily broken by a change
to B. Dependencies have no versions, optional flags, weights, or timing here.
Opposite edges are permitted; self-loops and duplicate ordered edges are not.

A directed path follows edge directions without repeating vertices. A vertex is
reachable from itself through a length-zero path. A directed cycle follows edge
directions and returns to its start, with no other repeated vertices. Two
vertices are mutually reachable if each is reachable from the other. A strongly
connected component is a maximal set of mutually reachable vertices.

Ignoring direction gives a different graph. Be explicit about which graph you
are discussing when using the words path, cycle, or component.

## Part 1: Predict before computing

Record your attempts in [notes.md](notes.md).

1. Draw all scenarios, including isolated packages. Explain the edge meaning in
   your own words using one pair from a scenario.
2. For each scenario, predict the vertices reachable from `api`, `shared`, and
   `sandbox`. Predict the strongly connected components and justify your groups.
3. Investigate how ignoring edge direction changes the questions and results.
   Keep directed cycles distinct from cycles in the undirected representation.
4. Choose a package change and predict which packages you would investigate for
   potential impact. Define whether your report includes the changed package.
5. Compare scenarios 1 and 4. State the relationship you observe and predict
   which conclusions it changes. Do not run code before recording predictions.

## Part 2: Definitions and proof attempts

1. Formulate directed reachability as a relation. Investigate reflexivity,
   symmetry, and transitivity; provide arguments or counterexamples as appropriate.
2. Investigate whether mutual reachability defines an equivalence relation and
   relate your reasoning to the proposed component output.
3. For one disputed grouping, state exactly what would establish or refute it.
   Separate the property you must prove from how you might compute it.
4. Explain what a directed dependency path establishes about the model and which
   additional assumptions would be needed to predict actual operational failure.

An incomplete argument with a precise obstacle is useful for focused review.
Do not seek an algorithm outline before attempting your own approach.

## Part 3: Implement

Implement the two tasks in `lab.py` with standard-library Python:

- `reachable_vertices(vertices, edges, start)` returns a set including start.
  An unknown start raises `ValueError`, even in an empty graph.
- `strongly_connected_components(vertices, edges)` returns a list of nonempty
  sets partitioning the supplied vertices. Component order is irrelevant. An
  empty graph returns an empty list.

Inputs satisfy the valid-graph contract in the docstrings. Functions must work
on their arguments rather than global scenario data and must not mutate inputs.
Choose an approach you can explain; no particular algorithm is prescribed. You
may reuse your own reachability implementation if you can justify that choice.

Before running the implementation, write down a proposed invariant and a
termination argument. Afterwards, review them against the actual code. Estimate
resource use in terms of vertex and edge counts, explaining your assumptions.
No performance benchmark is required for these small graphs.

Run your code on the scenarios and compare it with the original predictions.
Preserve the predictions when recording corrections. Investigate the selected
package change using your functions and any explicitly constructed graph inputs;
a separate impact-analysis function is not required.

## Part 4: Check behavior

After making independent predictions, run from the repository root:

```sh
python3 -B -m unittest discover -s labs/02-dependencies -p 'test_*.py' -v
```

Run this lab's tests separately from Lab 1's because each directory has its own
`lab.py` and `test_lab.py`. No packages or installation are required.

The scaffold deliberately raises `NotImplementedError`. Its tests initially
report errors; this does not mean the learner work has been completed. The test
file uses separate examples and partition checks rather than an answer table
for the main scenarios. Review its assertions after your prediction attempt.

Tests do not prove algorithm correctness, fully verify all possible inputs, or
evaluate written reasoning. Cyclic cases exercise termination in a normal test
run but are not a formal termination proof. A faulty implementation may hang;
interrupt it and review your argument. No real sleeps or timeout tests are used.
Discuss apparent conflicts with the contract before changing supplied tests.

## Part 5: Interpret and review

Write a short account of one potential impact report. Distinguish a guaranteed
graph property, a computation on supplied data, and an operational assumption.
Discuss at least two omitted features such as versions, optional dependencies,
runtime conditions, or incomplete dependency data. A missing edge is missing
information in a model; do not silently treat it as proof of independence.

## Completion checklist

- [ ] All scenario predictions, including isolated packages and edge direction.
- [ ] Attempts at the mathematical prompts, with reviewed gaps addressed.
- [ ] Both learner functions implemented and their behavioral checks passing.
- [ ] Invariant, termination, and resource-use arguments checked against the code.
- [ ] Potential impact analysis with explicit limits and assumptions.
- [ ] Chapter 1 section/proof checklist and selected exercises reviewed.

The files being prepared does not mark these tasks complete. Ask the agent for
a focused review of a prompt or code region; help proceeds gradually under
the project's tutoring instructions.

## Deferred work

Live package inspection, package installation, graph visualization packages,
production input validation, large-scale optimization, and OSTEP deadlock
experiments require later planning. This lab has no external service interactions.
