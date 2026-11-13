# Lab 1: Connectivity and entity identity

## Goal

Refresh graph fundamentals and investigate what graph connectivity establishes
about candidate matches between records. This lab uses synthetic data; no real
personal information or similarity scoring is involved.

You will make predictions, attempt mathematical arguments, implement component
discovery, and interpret results. The supplied code contains an unfinished task.
Working tests alone do not complete the lab.

## Reading and vocabulary

Refresh the relevant material in Trudeau. Exact pages depend on your edition.
Use Eccles if relations or proof writing need attention; Epp is an alternative.
No Diestel or Chung reading is required yet.

- A **simple undirected graph** has vertices and unordered pairs of distinct
  vertices as edges. This lab uses no parallel edges or edge weights.
- A **path** connects vertices through successive adjacent vertices without
  repeating vertices. A single vertex is permitted as a path of length zero.
- A **connected component** is a maximal connected set of vertices.
- A **cycle** is a closed sequence of adjacent vertices with no vertex repetition
  except its start/end, and at least three edges in a simple graph.
- A **tree** is a connected graph without cycles; a forest has no cycles.
- A **bridge** is an edge whose deletion increases the number of components.
- A **cut vertex** is a vertex whose deletion, together with its incident edges,
  increases the number of components.

These are definitions, not instructions for a particular algorithm.

## Model and supplied data

Open `lab.py` to inspect the six records, their known synthetic identities, and
five candidate-edge scenarios. A vertex represents a record, not a person. An
edge means only that the pair has been supplied as a candidate match.

The known identities are evaluation labels. Do not use them in your component
algorithm. All six vertices exist in every scenario, including vertices with no
incident edges. Treat the graph as unweighted and undirected.

The scenario names are neutral. Discover their behavior rather than assuming
each represents a particular type of error.

## Part 1: Define and predict

Work in `notes.md` before implementing or running tests.

1. Explain the distinction between a record, a candidate match, and an entity.
2. Draw each scenario with all six vertices. Predict its components, bridges,
   and cut vertices. Record your reasoning and uncertainty.
3. Compare each predicted grouping with the supplied identity labels. Describe
   any disagreements in words; no scoring metric is required.
4. Select an edge and a vertex from each scenario. Predict the components after
   their deletion. Vertex deletion also removes its incident edges.
5. Which scenarios are forests? Which contain cycles? Justify your choices.

## Part 2: Reason before coding

Attempt each prompt without asking for a complete solution. An incomplete
argument with a clearly identified obstacle is useful material for review.

1. Define a relation on the vertex set by saying that two vertices are related
   when a path connects them. Investigate whether this is an equivalence relation.
2. State precisely the grouping claim that component discovery makes. What
   additional claim would be needed to interpret the components as entities?
3. Construct a numerical example with three records and a similarity threshold
   in which the resulting candidate-match relation is not transitive. Define
   your similarity values and threshold rule explicitly.
4. Investigate whether structural importance establishes that a match is wrong.
   Address both bridges and edges that are not bridges using examples or proofs.

## Part 3: Implement and experiment

Implement only `connected_components` in `lab.py`. Use the Python standard
library. Its docstring specifies inputs, outputs, and the initial scope.

Run it on the supplied scenarios. Compare the results with your written
predictions before revising any predictions. Record both the original prediction
and what changed your mind.

Experiment with the deletions you selected. You may construct modified input
tuples and call your function again; this lab does not require separate bridge
or cut-vertex algorithms. Keep the known identity labels out of the computation.

## Part 4: Check your work

The separate test file uses small examples and structural invariants, not an
answer table for the five scenarios. Read it after making predictions if you
want to preserve the independent attempt.

From the repository root, run:

```sh
python3 -m unittest discover -s labs/01-connectivity -p 'test_*.py' -v
```

The untouched scaffold raises `NotImplementedError`, so its behavior tests will
initially report errors. That is an unfinished learner task, not a passing lab.
No packages or installation are required.

The tests assume valid inputs. They do not exhaustively prove your algorithm
correct or assess your written reasoning. Do not change tests merely to make
your implementation pass; investigate the contract and discuss any conflict.

## Part 5: Interpret and review

Write a short account separating:

- A mathematical statement about the graph.
- A computational observation from your implementation.
- An assumption about whether records represent the same person.

Explain the grouping errors you found and the limitations of the model. Identify
one question that similarity scores or real data would introduce but this lab
does not answer.

## Completion checklist

- [ ] Drawings and predictions for all five scenarios, including isolated vertices.
- [ ] Reasoning about cycles, bridges, cut vertices, and selected deletions.
- [ ] Attempts at all four mathematical prompts, reviewed with gaps addressed.
- [ ] Component implementation using only graph inputs.
- [ ] Behavioral checks pass; predictions and discrepancies have been discussed.
- [ ] Interpretation distinguishes connectivity from entity identity.

Ask the agent for a focused review when ready. State which prompt or code region
you want help with; the project tutoring rules require gradual assistance.

## Deferred work

Similarity scoring, blocking, probabilistic matching, real datasets, visualization
libraries, and performance optimization belong to later approved work. Invalid
vertices, malformed edges, self-loops, duplicate inputs, and adversarial data are
outside this first function's input contract.

## M01 entry point

Use the [M01 learning card](notes.md#m01-learning-card-agent-prepared) to begin
with the prerequisite diagnostic, finalize agent-selected textbook work, and
follow the session plan and mixed-assessment blueprint. The core exercise above
remains independent learner work. Advancement follows objective-specific readiness
under [ASSESSMENT.md](../../ASSESSMENT.md).
