# Lab 4: Station and connection failures

## Goal and reading

Investigate which failures disconnect two chosen locations and what establishes
the minimum number required. Distinguish station failures from connection
failures and local connectivity from the connectivity of an entire network.

Read Diestel Chapter 3 in full using [reading.md](reading.md). Van Steen provides
network context. TCP/IP can support an alternative communication interpretation,
but the supplied experiment uses synthetic transport stations.

## Model and conventions

In `lab.py`, every vertex is a station and every undirected edge is an available
bidirectional connection. All listed stations exist in every scenario. There
are no weights, capacities, travel times, parallel connections, self-loops, or
failure probabilities. An isolated station remains part of the graph.

The terminal pair is `s`, `t`. A vertex separator is a set of other stations
whose deletion, together with their incident connections, leaves no terminal
path. An edge separator removes connections while retaining all stations.
Minimum means smallest cardinality, not merely that no further deletion appears
necessary. More than one minimum separator may exist.

The vertex task excludes adjacent terminal pairs and never permits deleting
the terminals. The edge task permits adjacent distinct terminals. Both tasks
return an empty set when the terminals are already disconnected. These are
pairwise questions, not definitions of global graph connectivity.

## Part 1: Predict before computation

Use [notes.md](notes.md) before implementing or reading the tests.

1. Draw each scenario, including stations without incident edges. Record whether
   the terminals are connected and compare that question with whole-graph connectivity.
2. Select station failures and connection failures. Predict the remaining
   terminal paths and explain what each deletion means operationally.
3. Propose a smallest separator of each type for every scenario. State your
   predicted sizes, possible alternatives, and evidence that smaller sets fail.
4. Construct path evidence for each prediction. Specify whether paths are
   internally vertex-disjoint or edge-disjoint and check the distinction carefully.
5. Investigate which conclusions would change if a station failure disabled
   several connections simultaneously. Do not assume independent failures.

## Part 2: Mathematical attempts

1. State the relevant forms of Menger's theorem with their precise hypotheses.
   Relate them to your path evidence and separator claims without conflating
   the vertex and edge formulations.
2. For one proposed separator, give both a disconnection argument and evidence
   of minimum cardinality. Explain why those are separate obligations.
3. Investigate whether a set that cannot lose any of its members while remaining
   a separator must have smallest cardinality. Supply a proof or counterexample.
4. Explain the adjacent-terminal restriction in the vertex task under the stated
   endpoint-deletion rule. Do not silently extend that restriction to edge failures.
5. Examine whether a local terminal-pair result establishes global connectivity.
   State any additional argument your conclusion would require.

## Part 3: Implement

Implement the two unfinished functions in `lab.py` using standard-library Python.
No particular algorithm is prescribed for these tiny graphs.

- `minimum_vertex_separator` returns a set of station IDs excluding terminals.
- `minimum_edge_separator` returns a set of endpoint tuples representing input
  edges. Either endpoint order is accepted. Do not include both orders of an edge.

Return any minimum separator, not a prescribed representative. Raise `ValueError`
for unknown or identical terminals in either function, and for adjacent terminals
in the vertex function. Graph inputs otherwise satisfy the docstrings' validity
assumptions. Do not mutate inputs or consult global scenarios.

Choose an approach you can justify. If using your own earlier graph functions,
explain the reuse without editing their completed work unasked. No reference
reachability routine or separator solver is supplied. Flow-based implementations
and an automated disjoint-path solver are deferred to later planning.

Write correctness and termination arguments, then compare actual results with
the preserved predictions. Revisit disagreements rather than replacing the
original reasoning silently.

## Part 4: Behavioral checks

After your independent attempt, run from the repository root:

```sh
python3 -B -m unittest discover -s labs/04-resilience -p 'test_*.py' -v
```

Run each lab separately because their module filenames are shared. Importing
this lab runs no experiments. The untouched functions raise `NotImplementedError`,
so the initial tests report unfinished-task errors, not passing behavior.

Separate small examples check cardinality and valid choices. Some tests list
all simple terminal paths of a tiny example and check that returned edge failures
intersect every such path. This verifies disconnection for those examples without
providing a general graph solver. Main-scenario checks verify the output contract
rather than give a table of optimum sizes.

Tests do not prove general correctness or evaluate your written work. A faulty
learner implementation may not terminate; interrupt it and review your argument.
No benchmark, real sleep, or production timeout is required. Discuss apparent
conflicts with the contract before changing supplied tests.

## Part 5: Interpret and review

Write a short resilience report separating:

- A mathematical claim about the supplied terminal pair.
- A computed result and the evidence for its optimality.
- An operational claim about a real transport system.

Discuss missing capacities, travel times, accessibility, service schedules, or
common-cause failures. Explain why a connection count does not establish a
failure probability or guarantee an acceptable substitute route.

## Completion checklist

- [ ] Scenario drawings, failure predictions, and separator-size claims recorded.
- [ ] Manual path evidence and mathematical prompts attempted and reviewed.
- [ ] Both learner functions pass their behavioral checks.
- [ ] Correctness, termination, and minimum-cardinality arguments reviewed.
- [ ] Report distinguishes local/global structure and operational reliability.
- [ ] Full Chapter 3 checklist and selected exercises reviewed.

Preparing these files does not mark learner work complete. The agent supplies
focused clarification and gradual assistance under the project tutoring rules.

## Deferred work

Real maps, routing services, capacities, costs, flow-based algorithms, automated
path packing, weighted or directed resilience, probabilistic reliability,
malformed-graph validation, and large-scale optimization require later approval.

## Technology extension

See [technology.md](technology.md) for the approved technology-study addition,
including task-specific library permissions and validation prompts. The core
exercise and tests above retain their existing scope. Technology setup and
runnable extension work remain a separate step; this addition does not complete
any learner work. Earlier deferred-work statements apply to the core exercise;
the extension describes the additional planned scope explicitly.
