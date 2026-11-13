# Lab 8: Infinite graphs through finite windows

## Goal and reading

Investigate what finite neighborhoods reveal about infinite graphs, and where
independent mathematical arguments are necessary. Read all of Diestel Chapter 8
using [reading.md](reading.md), consulting the infinite-sets appendix and Pinter
for specific gaps. Finite tests do not certify ends, infinite paths, or limits.

## Mathematical family definitions

Work with three simple undirected infinite graphs:

- `ray`: vertices are nonnegative integers; consecutive integers are adjacent.
  Root at 0. Encode vertices as decimal strings, such as `"0"` and `"2"`.
- `double_ray`: vertices are all integers; consecutive integers are adjacent.
  Root at 0. Encode integers as decimal strings, including `"-1"`.
- `binary_tree`: vertices are all finite binary words; one word is adjacent to
  another if appending one bit to one produces the other. The empty word is the
  root. Encode words literally, so the root is `""`.

A finite ball includes every vertex at graph distance at most its radius from
the root and every family edge between included vertices. These definitions
specify the objects; they do not supply their graph-theoretic conclusions.

The graph is infinite even though each experiment materializes a finite induced
ball. The represented empty word is a vertex, not an empty graph. Removing a
finite set from a ball is a finite experiment distinct from removing it from
the entire infinite graph.

## Part 1: Predict before computing

Use [notes.md](notes.md) before implementation or test inspection.

1. Restate each family's vertex set, adjacency rule, and root mathematically.
   Explain why the label encoding does not define graph distance.
2. Draw the balls of radii zero, one, and two. Predict their vertices and edges.
3. For the neutral scenarios in `lab.py`, predict components after deletion and
   their finite sizes. Include isolated surviving vertices.
4. Choose a fixed finite deletion set and investigate increasing radii in which
   all removed vertices are present. Predict what changes and what stays fixed.
5. Compare vertices at a ball's boundary with their counterparts in the infinite
   graph. Identify conclusions that might be artifacts of the truncation.

## Part 2: Mathematical attempts

1. State a claim about one underlying infinite graph and write its quantifiers
   explicitly. Identify what your finite computations would and would not prove.
2. Investigate rays and double rays using the text's definitions. Supply a
   mathematical argument for the existence or nonexistence claims you make.
3. State the definition of an end from the chapter and investigate it for these
   families. Keep finite component counts distinct from a count of ends.
4. Select an earlier finite-graph argument and identify exactly where finiteness
   enters. Investigate its applicability to an infinite graph without assuming
   that a familiar proof transfers unchanged.
5. Attempt an example or argument illustrating why knowing a finite neighborhood
   alone need not settle a global infinite-graph question. State the information
   being held fixed and the claim being tested.

## Part 3: Implement finite experiments

Complete the two tasks in `lab.py` with standard-library Python:

- `truncate_graph(family, radius)` returns the finite ball's vertex tuple and
  edge set. Vertex order is arbitrary; each undirected edge tuple has endpoints
  in increasing lexical order. Radius zero includes the root.
- `component_sizes_after_deletion(vertices, edges, removed)` deletes the named
  vertices and their incident edges, returning positive component sizes sorted
  in nondecreasing order. With no remaining vertices, return `()`.

Unknown families and negative integer radii raise `ValueError`. Initial radii
are zero through four; other validity assumptions are in the docstrings. Do not
mutate inputs or consult global scenarios. Convert the returned edge set to a
tuple when passing it to the finite deletion function.

Choose an approach you can justify. Explain any reuse of your own earlier graph
code. Write a correctness and termination argument for the finite routines, and
state what they do not claim about the infinite objects.

Run the experiments after predictions, preserve originals, and explain any
discrepancies. A fixed finite number of successful cases is not an infinite proof.

## Part 4: Behavioral checks

From the repository root, after an independent attempt:

```sh
python3 -B -m unittest discover -s labs/08-infinite -p 'test_*.py' -v
```

Run labs separately because module names are shared. Untouched learner functions
raise `NotImplementedError`, so initial errors indicate unfinished work.

Tests check small exact neighborhoods, nesting, induced restrictions, finite
deletions, and output invariants. The nested tests compare learner outputs with
each other and cannot alone establish family correctness. Independently inspect
your radius-four graphs against the family definitions. The separate finite
deletion examples exercise that function without depending on truncation code.

No test determines the infinite graph's ends, proves an infinite path exists,
or establishes a graph limit. Those are written mathematical review tasks.
Tests do not prove general algorithm correctness. Interrupt nonterminating
learner code and review its argument; no real sleep or timeout test is required.
Discuss apparent contract conflicts before changing supplied tests.

## Part 5: Interpretation and completion

Write a report distinguishing the mathematical family, finite representation,
observed finite property, conjecture, and independently justified infinite claim.
Describe radius and deletion choices, boundary effects, and remaining uncertainty.
Do not label a computed finite component as infinite.

- [ ] Family definitions, drawings, deletion predictions, and boundary questions recorded.
- [ ] Mathematical prompts attempted and reviewed, with gaps addressed.
- [ ] Both finite routines pass their behavioral checks.
- [ ] Radius-four outputs independently checked against the family definitions.
- [ ] Correctness and termination arguments reviewed for the finite routines.
- [ ] Infinite claims reviewed separately from computational evidence.
- [ ] Full Chapter 8 checklist and selected exercises reviewed.

Scaffold preparation does not complete learner work. The agent supplies focused
clarification and gradual hints under the project's tutoring instructions.

## Deferred work

General infinite-graph representations, automatic end classification, universal
graph construction, topological cycle-space software, automatic graph-limit
analysis, larger computations, and malformed-input handling require later approval.
