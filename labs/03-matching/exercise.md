# Lab 3: Matching records across databases

## Goal and reading

Investigate assignments when candidate record links compete for counterparts.
Distinguish a valid assignment, its objective value, and its agreement with
identity. Read Diestel Chapter 2 in full using [reading.md](reading.md); CLRS
provides supplementary matching algorithms when you are ready to consult them.

## Model and definitions

The two synthetic databases in `lab.py` each contain at most one record per
entity. Some entities may be absent from the other database. Names alone do not
determine identity. The known identity labels are evaluation data and must not
be consulted by the matching algorithm.

Vertices are records. Every candidate edge joins a left record to a right record;
its tuple order is `(left, right)`. The graph is bipartite and unweighted. An edge
indicates only a supplied candidate link, not established identity. No left or
right record may appear in more than one selected pair under this model.

A **matching** is a set of edges with no shared endpoint. Its **cardinality** is
the number of edges selected. A **maximal matching** admits no additional edge
without ceasing to be a matching. A **maximum matching** has largest cardinality
among all matchings of the graph. A matching **saturates** a vertex set when every
vertex of that set is incident to a selected edge. Consult the book for further
definitions and the hypotheses of its results.

The implementation objective is maximum cardinality. Weighted objectives and
identity correctness are separate questions. No tie-breaking rule is prescribed.

## Part 1: Predict before computing

Record original attempts in [notes.md](notes.md) before implementation or tests.

1. Draw the five candidate graphs, keeping all records visible, even without
   candidate edges. Explain why the graph is bipartite under this construction.
2. For each scenario, propose a matching and predict its maximum possible size.
   State what would establish that your predicted size cannot be improved.
3. Investigate which records can or must remain unmatched and whether different
   maximum matchings are possible. Do not assume a unique optimum.
4. Compare proposed assignments with known identity labels. Separate a missing
   candidate link from a candidate edge that the assignment does not select.
5. Make an independent local-choice assignment without revising earlier choices.
   State your selection rule and investigate whether it attains your predicted
   objective. Treat this as an experiment, not a general theorem.

## Part 2: Mathematical attempts

1. Investigate the relationship between maximal and maximum matchings. Justify
   each implication you claim or provide a counterexample.
2. State Hall's theorem precisely after reading the section. Identify which
   saturation question it addresses and investigate its hypotheses on your
   scenarios. Distinguish necessary evidence from a complete argument.
3. For a proposed optimum, supply an upper-bound argument and a matching that
   meets the claimed size, or explain the remaining gap in your reasoning.
4. Investigate whether maximum cardinality establishes correct entity links.
   Explain using your scenarios or a new example without changing the objective.
5. Describe a domain where the one-record-per-entity assumption fails. Explain
   which assignment constraint would then need reconsideration.

## Part 3: Implement

Implement `maximum_matching(left, right, edges)` in `lab.py`. Return a set of
candidate pairs, use each endpoint at most once, and maximize cardinality.
Any maximum matching is acceptable when the optimum is not unique. With no
candidate edges, return an empty set.

Inputs satisfy the valid-graph contract in the docstring. Use only the supplied
graph arguments and standard-library Python. Do not inspect identity labels,
scenario names, or global record tables. Do not mutate inputs. Choose your own
approach for these tiny graphs; no particular algorithm is prescribed.

Write a correctness and termination argument for the approach you choose. Relate
it to the objective rather than simply claiming that the output is a matching.
An incomplete argument with a specific obstacle is suitable for focused review.

Run your implementation on the scenarios. Compare with predictions, preserve
the originals, and explain discrepancies. Use the labels only afterwards to
interpret link correctness and remaining unmatched records.

## Part 4: Check behavior

After the independent attempt, run from the repository root:

```sh
python3 -B -m unittest discover -s labs/03-matching -p 'test_*.py' -v
```

Run this lab's tests separately: each lab has its own `lab.py` and `test_lab.py`.
The untouched scaffold raises `NotImplementedError`, so tests initially report
errors. This is unfinished learner work, not a passing implementation.

The tests use separate, hand-checkable graphs to check cardinality. They accept
different valid optima in the ambiguous example. Checks on the main scenarios
verify candidate membership and endpoint uniqueness without giving an optimum
answer table. There is no supplied reference solver.

Passing these examples is not a proof of correctness for every input and does
not validate the model or written work. Cyclic or repeated-choice behavior in
a faulty algorithm can fail to terminate; interrupt a stuck run and revisit
your argument. No real sleeps, benchmark suite, or production timeout is required.
Discuss conflicts with the contract before changing supplied tests.

## Part 5: Interpretation and review

Write a brief account separating a matching's validity, its cardinality, its
optimality evidence, and its identity accuracy. Explain why unmatched records
and ambiguous optima need interpretation rather than automatic error labels.

Describe the consequences of an incorrect selected pair and a missed true pair
for a hypothetical use case. No probabilistic scores or evaluation metric are
required yet. Identify what evidence a later statistical model would need.

## Completion checklist

- [ ] Graphs, predictions, proposed assignments, and ambiguity analysis recorded.
- [ ] All mathematical prompts attempted and reviewed, with gaps addressed.
- [ ] Learner implementation passes the behavioral checks.
- [ ] Correctness and termination arguments reviewed against the actual code.
- [ ] Interpretation separates objective value from identity correctness.
- [ ] Full Chapter 2 reading/proof checklist and selected exercises reviewed.

The agent provides focused clarification and gradual hints under `AGENTS.md`.
Preparing these files does not mark any learner task complete.

## Deferred work

Similarity scoring, weighted matching, blocking, duplicate entities within a
source, probabilistic decisions, real datasets, malformed-input validation,
production storage, and large-scale optimization require later approved work.
