# Lab 11: Tree decompositions, graph minors, and consolidation

## Goal and reading

Investigate how overlapping local groups represent a graph, and what a proposed
decomposition establishes. Read all of Diestel Chapter 12 using [reading.md](reading.md).
Use [consolidation.md](consolidation.md) to audit the full Diestel study separately
from lab preparation. No learning-completion status is inferred from file creation.

## Model and conventions

The small graph in `lab.py` represents variables with pairwise interactions.
It records which variables interact, not the values, logical content, or
solvability of constraints. A bag is a set of graph vertices. Bag IDs name nodes
of a second graph; their connections are distinct from the interaction edges.

A tree decomposition requires:

- Every graph vertex occurs in at least one bag, and bags contain only graph vertices.
- Every graph edge has both endpoints together in at least one bag.
- The graph connecting bag nodes is a nonempty simple tree.
- For each graph vertex, the bag nodes containing it induce a connected subtree.

Empty bags are permitted. The empty graph can be represented by one empty bag.
An empty bag collection is not accepted in this lab. The width of a nonempty
bag collection is its largest bag size minus one, so one empty bag has width -1.
Tree-width concerns minimizing over valid decompositions; computing the width
of one candidate does not establish that minimum.

These definitions state what must be checked, not how to implement the checks.

## Part 1: Predict before computing

Record original attempts in [notes.md](notes.md) before implementation or tests.

1. Draw the interaction graph and every candidate bag graph. Keep graph vertex
   IDs, bag IDs, and bag contents distinct.
2. Predict each candidate's validity. Check every condition separately and
   identify a precise witness when claiming a violation.
3. Predict each nonempty bag collection's width. Explain why an invalid candidate's
   numerical width need not provide a justified graph-parameter bound.
4. Attempt an improvement to a valid candidate. State the evidence for any width
   bound you claim, and distinguish an improvement from proved optimality.
5. Explain what constraint information the interaction graph leaves out, and what
   additional work would be needed to use a decomposition in an application solver.

## Part 2: Mathematical attempts

1. Unpack the quantifiers in the decomposition definition. For an example of
   your own, investigate whether edge and vertex coverage alone suffice.
2. Give a correctness argument for accepting a candidate and a separate argument
   for rejecting one. State which mathematical conditions your code establishes.
3. Investigate what a valid width claim establishes about tree-width. Explain
   what further evidence would be needed to prove optimality.
4. Work a small sequence of graph deletions or contractions manually. Record
   the exact objects and claim before applying a result about minors.
5. Select a structural statement from the chapter, state its hypotheses, and
   distinguish a finite illustration from the supplied general proof.

## Part 3: Implement

Complete the two learner tasks in `lab.py` with standard-library Python:

- `is_tree_decomposition(vertices, edges, bags, tree_edges)` returns a Boolean
  for a candidate of the documented container shapes. Structural invalidity,
  including unknown references, returns False rather than being accepted silently.
- `decomposition_width(bags)` returns the defined numerical width, raising
  ValueError for an empty collection. It does not certify graph validity or
  minimum tree-width.

The underlying graph inputs are valid simple undirected graphs. Candidate bags
have string IDs and frozenset contents. Tree-edge pairs have string endpoints;
unknown IDs, loops, duplicate undirected edges, disconnection, and cycles are
candidate violations to detect. General malformed-type handling is deferred.

Do not mutate inputs or consult global scenarios. Choose your own approach and
explain any reuse of earlier learner code. Do not hide unexpected programming
defects behind False results. No optimal-decomposition, minor-detection, or
constraint-satisfaction solver is supplied or required.

Write correctness and termination arguments, compute after predictions, preserve
originals, and investigate discrepancies. Keep validity and width conclusions
separate in both code use and written interpretation.

## Part 4: Behavioral checks

After an independent attempt, run from the repository root:

```sh
python3 -B -m unittest discover -s labs/11-decompositions -p 'test_*.py' -v
```

Run labs separately because module names are shared. Untouched functions raise
NotImplementedError; initial errors indicate unfinished learner work.

Separate small candidates isolate coverage, bag-tree, reference, and connected-
occurrence conditions. Width checks do not depend on the validity function.
Main-scenario checks verify output type and input preservation without supplying
an answer table. There is no reference validator or decomposition solver.

Tests do not prove general correctness, minimum tree-width, or a minor theorem.
Review main decisions and bounds manually. Interrupt nonterminating code and
revisit its argument; no real sleeps or production timeout are required. Discuss
apparent contract conflicts before changing supplied tests.

## Part 5: Consolidate and complete

Write an account separating representation, validity evidence, numerical width,
graph-parameter bounds, and application implications. Audit Diestel using the
separate consolidation record without marking earlier work complete unreviewed.

- [ ] Candidate drawings, validity predictions, violations, and widths recorded.
- [ ] Mathematical prompts and manual minor investigations reviewed.
- [ ] Both learner functions pass behavioral checks.
- [ ] Correctness, termination, and width-bound reasoning reviewed.
- [ ] Full Chapter 12 checklist and selected exercises reviewed.
- [ ] Chapters 1-12 proof/exercise records and relevant appendix work audited.
- [ ] Open questions reviewed and remaining work explicitly recorded.

Preparing these files is separate from meeting the study checkpoints. The agent
follows the project's gradual-assistance policy for clarification and review.

## Deferred work

Automatic minimum tree-width, general minor detection, algorithmic tangle
construction, application solvers, production input handling, and large-scale
optimization require later planning and approval.
