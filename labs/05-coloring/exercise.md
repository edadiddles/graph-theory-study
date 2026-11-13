# Lab 5: Examination conflicts and planar structure

## Goal and reading

Investigate the fewest examination time slots needed under shared-enrollment
constraints. Separately investigate what proposed drawings establish about
planarity. Read Diestel Chapters 4 and 5 in full using [reading.md](reading.md).
Use Epp selectively; consult Gamelin and Greene for topology questions as needed.

The scheduling graph is not assumed planar. Planarity and coloring theorems
require checking their own hypotheses; sharing a lab does not make the two
applications interchangeable.

## Model and definitions

In `lab.py`, the explicit inventory lists all examinations, including those with
no enrollment or conflicts. Each synthetic enrollment row represents one student.
An undirected edge joins two exams when at least one student takes both.
Repeated evidence still represents a single edge. Exams do not conflict with
themselves. No actual student data is used.

A proper vertex coloring assigns different colors to adjacent vertices. Its
number of colors is the number of distinct labels used. A minimum coloring
uses the smallest possible number; that number is the chromatic number. Colors
represent interchangeable slots, not ordered times or preferences.

The model omits rooms, capacity, exam duration, travel, availability, and limits
on how many examinations a student should take in one day. Feasibility under
this graph model does not establish a usable real timetable.

## Part 1: Predict before computation

Use [notes.md](notes.md) before implementation or reading the test answers.

1. Draw the conflict graph for each enrollment scenario. Keep every exam visible
   and explain the provenance of each proposed conflict edge.
2. Propose a proper coloring and predict the minimum number of slots. State
   evidence for lower and upper bounds; separate a feasible assignment from
   evidence of optimality.
3. Investigate ambiguity: which assignments can differ while having the same
   objective? Explain whether changing color names changes the schedule's quality.
4. Choose a local-choice coloring rule and a vertex order. Try it manually and
   examine whether changing the order changes its result. Do not claim a general
   guarantee from a few examples.
5. Identify a realistic constraint that cannot be inferred from pairwise shared
   enrollment alone. Explain what extra data and model decisions it would need.

## Part 2: Proof and bound attempts

1. Give a direct argument that your proposed schedule satisfies every modeled
   conflict. Explain why that argument alone need not establish optimality.
2. State and justify a lower bound for one scenario and investigate whether
   your constructed assignment meets it. State all assumptions explicitly.
3. Investigate the relationship between cliques and required colors. Give a
   proof or counterexample for each general claim you make.
4. Select a coloring result from the chapter, state it precisely, and assess its
   applicability to your model before using it.

## Part 3: Implement

Complete the two tasks in `lab.py` using standard-library Python:

- `build_conflict_edges(exams, enrollments)` returns exactly the supported conflict
  pairs, with each tuple in increasing lexical order. Keep the full vertex
  inventory separate; it cannot be reconstructed from edges alone.
- `minimum_coloring(vertices, edges)` returns a dictionary assigning an integer
  label to every vertex, minimizing the number of distinct labels. Empty input
  returns an empty dictionary; nonempty edgeless graphs still need assignments.

Any proper optimum is acceptable. No color names, visit order, or tie-breaking
rule is prescribed. Inputs satisfy the valid-data contracts in the docstrings.
Do not mutate them or consult global scenarios. Convert your conflict-edge set
to a tuple when calling the coloring function.

Choose your own approach and write correctness and termination arguments. Explain
why your approach minimizes color count rather than merely producing a proper
coloring. Exact search can become expensive; these instances are intentionally
tiny. Large workloads, benchmarks, and optimized solvers are deferred.

Run experiments only after predictions, preserve the originals, and record what
changed your mind. Do not silently revise the model to fit an implementation.

## Part 4: Manual planarity investigation

Use the separate `PLANARITY_CASES` in `lab.py`. Draw straight segments between
the proposed coordinates. Coordinates specify drawings to investigate, not
certified embeddings or the only permitted way to draw a graph.

1. Assess each proposed drawing using the book's definitions. Locate any issue
   precisely, including intersections that are not graph vertices.
2. Compare the two drawings of case 1. Distinguish properties of a drawing from
   properties of the underlying graph.
3. For each graph, attempt a planarity argument, a new embedding, or a relevant
   obstruction argument. Explain which theorem hypotheses you have checked.
4. For an embedding you have justified as plane, investigate faces and its dual
   under the text's conventions. Do not construct a plane dual from an uncertified
   crossing drawing. Check any counting claims against their assumptions.

No general planarity solver, drawing engine, or geometry library is supplied.
These arguments are reviewed manually, not certified by the coloring tests.

## Part 5: Behavioral checks

After an independent attempt, run from the repository root:

```sh
python3 -B -m unittest discover -s labs/05-coloring -p 'test_*.py' -v
```

Run each lab separately because module filenames are shared. The untouched
scaffold raises `NotImplementedError`; its initial errors are unfinished learner
tasks, not evidence of passing behavior.

Separate small examples check exact conflict edges and known optimum color counts.
Coloring tests check constraints and counts, not a particular labeling. Checks
on main scenarios assess edge provenance and schedule validity without supplying
a table of optimum counts. There is no reference coloring or planarity solver.

Passing tests does not prove correctness for all graphs or validate written
arguments. A faulty implementation may run indefinitely; interrupt it and review
termination. No real sleeps or production timeouts are required. Discuss apparent
contract conflicts before changing supplied tests.

## Part 6: Interpretation and completion

Write a brief scheduling report separating model construction, feasibility,
optimality evidence, and practical usefulness. Add a separate planarity account
that distinguishes drawing observations from mathematical conclusions.

- [ ] Conflict graphs and original schedule predictions recorded.
- [ ] Mathematical prompts and planarity investigations attempted and reviewed.
- [ ] Both learner tasks pass behavioral checks.
- [ ] Correctness, optimality, and termination arguments reviewed.
- [ ] Practical limitations and theorem hypotheses explained.
- [ ] Both full chapter checklists and selected exercises reviewed.

Preparing files does not complete learner work. The agent follows the project's
gradual-assistance policy for review and clarification.

## Deferred work

Room allocation, capacity, duration, availability, fairness objectives, actual
student records, general planarity algorithms, automatic geometry checks,
malformed-input validation, external solvers, and performance optimization
require later planning and approval.

## Technology extension

See [technology.md](technology.md) for the approved technology-study addition,
including task-specific library permissions and validation prompts. The core
exercise and tests above retain their existing scope. Technology setup and
runnable extension work remain a separate step; this addition does not complete
any learner work. Earlier deferred-work statements apply to the core exercise;
the extension describes the additional planned scope explicitly.
