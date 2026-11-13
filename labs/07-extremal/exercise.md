# Lab 7: Extremal constructions and forbidden patterns

## Goal and reading

Investigate how many edges a graph can have while avoiding a specified structure.
Start with triangle avoidance on at most five vertices. Distinguish exhibiting
a construction, computing an optimum at a finite order, and proving a theorem
for arbitrary order.

Read Diestel Chapter 7 in full using [reading.md](reading.md). This experiment
supports the chapter but does not replace its minor and regularity material.
Try the small construction questions before reading a result that settles them;
afterwards, connect your reasoning with the text and record any assistance.

## Model and conventions

Graphs are simple, undirected, and unweighted. Vertices are explicit string IDs;
isolated vertices remain part of the graph. A triangle consists of three distinct
vertices joined pairwise. Extra edges elsewhere do not prevent its occurrence.

The construction task supplies only a vertex inventory. Any simple edge between
its vertices is eligible. The objective is largest edge count subject to no
triangle subgraph. This is not a request to remove as few edges as possible from
a supplied scenario. Any optimal graph is acceptable; a unique answer is not
assumed. Output edges use increasing lexical endpoint order.

This lab is a mathematical experiment rather than a claim that triangles are
undesirable in every real network. A practical forbidden-pattern constraint
would need its own domain justification.

## Part 1: Predict and construct before computing

Use [notes.md](notes.md) before implementation or test inspection.

1. Draw each neutral scenario with all five vertices and predict triangle
   presence. Supply evidence for each prediction, including absence claims.
2. For each inventory in `VERTEX_SETS`, propose a triangle-free construction.
   Record its edge count and whether you believe it is optimal.
3. Try to improve each construction. State a bound and explain the evidence
   supporting it without assuming that an unsuccessful attempt proves a maximum.
4. Investigate whether changing names or input order should affect edge counts.
   Distinguish a graph's structure from its labeled representation.
5. State exactly what a finite exhaustive search would have to examine to certify
   an optimum at one order. Estimate its scope before implementing any search.

## Part 2: Mathematical attempts

1. State the extremal question with explicit quantifiers. Identify what a single
   example proves and what it leaves open.
2. Attempt an upper-bound argument and a construction attaining a bound for one
   chosen order. Keep the two obligations separate.
3. Investigate the difference between a construction to which no edge can be
   added and a construction with maximum edge count. Prove your claims or give
   counterexamples; do not rely on terminology alone.
4. Explain how forbidding a subgraph, an induced subgraph, or a minor changes a
   question. Use your own examples and avoid asserting equivalence without proof.
5. After independent attempts, compare with an applicable Chapter 7 result.
   State its hypotheses and separate any general proof from computational support.

## Part 3: Implement and experiment

Complete the two learner functions in `lab.py` with standard-library Python:

- `contains_triangle` returns a Boolean for valid small graph inputs, independent
  of endpoint orientation and vertex names.
- `maximum_triangle_free_graph` returns the edges of any maximum triangle-free
  graph on the supplied inventory, of size at most five in this iteration.

The full vertex set remains the argument, including isolates. Do not infer it
from returned edges, mutate inputs, or consult global scenarios. The docstrings
define valid inputs and output representation. Larger orders and malformed
inputs are outside this initial contract. No algorithm is prescribed.

Explain your approach, termination, and correctness. If the construction depends
on your detector, identify that dependency and how a detector error could affect
the result. A claimed exhaustive search needs a completeness argument, not just
an output. A construction based on a theorem needs its hypotheses checked.

Run the scenarios and construction cases only after predictions. Preserve the
original attempts and record discrepancies. Do not infer a general extremal law
solely because the first few counts agree with a proposed pattern.

## Part 4: Behavioral checks

After an independent attempt, run from the repository root:

```sh
python3 -B -m unittest discover -s labs/07-extremal -p 'test_*.py' -v
```

Run labs separately because their module filenames are shared. Untouched learner
functions raise `NotImplementedError`; initial errors are not passing behavior.

Separate examples test triangle detection. Construction tests check small known
counts, legal edge representation, and the learner detector's result. They accept
any optimum and contain no general formula or reference solver. Inspect the
returned constructions manually as well: a shared detector mistake can affect
both routines. Tests and small examples do not replace mathematical review.

There is no performance benchmark or real-time timeout requirement. Interrupt
an implementation that fails to terminate and revisit its argument. Discuss any
apparent contract conflict before changing supplied tests.

## Part 5: Interpretation and completion

Write a short report separating construction evidence, finite optimality evidence,
and a general theorem. Describe the exact orders examined, assumptions, limitations,
and remaining questions. Explain what extra work a broader forbidden-pattern
question would need.

- [ ] Scenario predictions and construction attempts recorded before computing.
- [ ] Bounds, quantifiers, and mathematical prompts attempted and reviewed.
- [ ] Both learner functions pass the behavioral checks.
- [ ] Returned graphs manually inspected for triangle avoidance and legality.
- [ ] Correctness, termination, and optimality arguments reviewed.
- [ ] Full Chapter 7 checklist and selected exercises reviewed.

Scaffold preparation is separate from learning completion. The agent provides
focused clarification and gradual hints under `AGENTS.md`.

## Deferred work

General forbidden-pattern solvers, induced-subgraph or minor detection, larger
searches, automated isomorphism reduction, computational regularity algorithms,
external libraries, and production safeguards require later planning and approval.
