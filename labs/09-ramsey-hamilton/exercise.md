# Lab 9: Unavoidable patterns and visiting every location

## Goal and reading

Study two different existence questions: monochromatic patterns in edge-colored
complete graphs, and routes visiting each vertex exactly once before returning
to their start. Read Diestel Chapters 9 and 10 in full using [reading.md](reading.md).
The experiments complement the chapters, including material not represented by
the two coding tasks.

## Part A: A supplied coloring versus every coloring

The first datasets in `lab.py` give complete simple graphs. Every unordered edge
has exactly one of the labels `red` and `blue`. These are arbitrary categories,
not the proper edge-coloring constraint from an earlier lab. Endpoints in color
dictionary keys are in increasing lexical order.

A monochromatic triangle has three distinct vertices with all three pairwise
edges the same color. The learner function examines one supplied coloring.
A universal assertion over colorings is a different question. No Ramsey-number
threshold or complete search over all colorings is supplied.

Before computing, use [notes.md](notes.md):

1. Draw each supplied coloring and predict whether it has the requested pattern.
   Record a witness or an absence argument, with uncertainty left visible.
2. State a Ramsey question with explicit quantifiers and graph conventions.
   Distinguish an example at one order from a universal statement at that order.
3. Attempt a bound argument or counterexample of your own. Explain exactly which
   claim your evidence supports. Do not infer a universal threshold from the
   finite list of supplied colorings.
4. Describe what a complete computational investigation would have to examine,
   and justify that scope before attempting an optional small enumeration.
5. Investigate relabeling vertices or swapping the two color names. State which
   conclusion should remain invariant and justify it.

Implement `monochromatic_triangle(vertices, edge_colors)`, returning any tuple
of three distinct vertices forming a witness, or `None` when none exists. Inputs
are valid complete colorings. Fewer than three vertices return `None`. Do not
mutate inputs or consult global scenarios. Use standard-library Python and
choose an approach you can explain. Justify a negative decision as well as a
positive witness; a failed incomplete search is not absence evidence.

## Part B: Visiting every location

The route examples use simple, undirected, unweighted networks. Vertices are
locations; edges are permitted bidirectional direct moves. Every location must
be visited once on a closed route. `depot` is an ordinary vertex, not a required
starting position. Costs, times, capacities, and preferences are omitted.

A Hamilton cycle contains every vertex exactly once, with an edge returning
from the last to the first. A simple cycle requires at least three vertices.
This differs from traversing every edge or finding a cheapest tour.

Before computing:

1. Draw every route scenario and predict whether a Hamilton cycle exists.
   Record a proposed cycle or a mathematical obstacle, with supporting reasoning.
2. Compare this question with Euler tours, ordinary cycles, and shortest routes.
   State what must be covered in each problem you discuss.
3. Select a relevant sufficient condition from Chapter 10, state its hypotheses,
   and assess its applicability. Investigate what can be concluded when its
   hypotheses fail without assuming a converse.
4. For a negative prediction, attempt a proof or a justified complete-search
   argument. State what an unsuccessful local construction leaves unresolved.

Implement `hamiltonian_cycle(vertices, edges)`. A witness lists every vertex once
as a tuple; the closing edge is implied, so do not repeat the first vertex at
the end. Any start, orientation, or valid cycle is accepted. Return `None` when
no cycle exists, including inventories with fewer than three vertices. Inputs
are valid simple graphs. Do not mutate inputs or consult global scenarios.

Use standard-library Python and your own justified approach. No shortest-tour
objective or particular search algorithm is prescribed. Explain correctness
and termination for both witness discovery and absence decisions.

## Behavioral checks and experiments

After independent predictions, run from the repository root:

```sh
python3 -B -m unittest discover -s labs/09-ramsey-hamilton -p 'test_*.py' -v
```

Run labs separately because their module filenames are shared. Untouched
functions raise `NotImplementedError`, so initial errors indicate unfinished
learner work. No packages or external services are required.

Separate hand-checkable examples have known positive and negative decisions.
Witness checks validate membership, distinctness, and required edges/colors,
not a particular answer ordering. Main-scenario checks validate returned
witnesses; they do not independently certify every `None` result. Review main
absence claims mathematically and manually inspect outputs.

There is no reference search solver. Tests do not prove search completeness,
general correctness, or any universal Ramsey theorem. A faulty implementation
may fail to terminate; interrupt it and revisit the argument. No benchmark or
real-time timeout requirement is introduced. Discuss apparent contract conflicts
before changing supplied tests.

Compare computations with preserved predictions and explain discrepancies.
Keep a supplied coloring, a bound argument, a cycle witness, and a universal
claim separate in your final account.

## Completion checklist

- [ ] Both sets of drawings and original predictions recorded.
- [ ] Quantified Ramsey question and independent bound attempts reviewed.
- [ ] Hamilton-cycle hypotheses and negative-case arguments reviewed.
- [ ] Both learner tasks pass behavioral checks.
- [ ] Witnesses and main absence decisions inspected independently.
- [ ] Correctness, termination, and any completeness claims reviewed.
- [ ] Full Chapters 9-10 checklist and selected exercises reviewed.

Preparing files does not complete learner work. The agent supplies focused
clarification and gradual hints under the project tutoring policy.

## Deferred work

General Ramsey-number computation, extensive coloring enumeration, large search
spaces, shortest tours, weighted routing, external solvers, and malformed-input
validation require later planning and approval.
