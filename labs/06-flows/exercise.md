# Lab 6: Distribution capacity and bottlenecks

## Goal and reading

Investigate how much material can pass through a directed distribution network
and what establishes its limiting capacity. Distinguish feasibility, optimality,
and usefulness of the model.

Read Diestel Chapter 6 in full using [reading.md](reading.md). Use CLRS for a
selected algorithmic treatment after an independent attempt. The distribution
application does not replace the chapter's broader flow material.

## Model and conventions

In `lab.py`, vertices are facilities and directed arcs are transport connections.
Capacities are nonnegative integer batches per hour. A zero-capacity connection
is supplied explicitly. Opposite arcs have separate capacities. The model has
one commodity, no loss or accumulation at intermediate facilities, and no travel
time, cost, reliability, demand deadline, or changing capacity.

A feasible flow assigns a nonnegative integer amount to every supplied arc,
not exceeding its capacity. Intermediate facilities conserve material: their
total inflow equals their total outflow. Source inflow and sink outflow are
permitted; flow value means net source outflow. Feasible circulation may occur
without contributing to delivered throughput. All comparisons use original
capacities and explicit arc directions.

A cut partitions vertices into a source side and its complement, with source
and sink on different sides. Its capacity counts only original arcs directed
from the source side to the other side. A minimum cut has least capacity, not
necessarily fewest arcs. Isolated facilities remain in the vertex inventory.

These conventions describe the programming interface. Compare them explicitly
with any different flow representation in the book before applying a theorem.

## Part 1: Predict before computing

Record attempts in [notes.md](notes.md) before implementation or test inspection.

1. Draw every scenario with arc directions and capacity units, including isolated
   facilities and zero-capacity arcs.
2. Propose a feasible flow, its net value, and your prediction of maximum value.
   Check every arc bound and intermediate conservation claim manually.
3. Propose a source-side cut and compute its capacity under the stated direction
   convention. Investigate alternative cuts and uncertainty in your prediction.
4. Choose a capacity change and predict whether it changes possible throughput.
   Separate a hypothesis from evidence of optimality.
5. Investigate the distinction between a directed connection existing, positive
   throughput being possible, and a useful service being available in practice.

## Part 2: Mathematical attempts

1. State the relevant maximum-flow/minimum-cut result with its hypotheses. Relate
   your proposed flow and cut to the exact conditions, including direction.
2. For a proposed optimum, supply both feasibility evidence and an argument that
   no larger value is possible. Explain the role of each piece of evidence.
3. Examine how source incoming and sink outgoing arcs affect the meaning of
   throughput. Check your net-value reasoning on a small example.
4. Investigate a relationship with an earlier matching or resilience question.
   Define the construction, capacities, and claim before asserting equivalence.
5. Explain why a transport capacity result is not automatically an electrical
   current solution, a cheapest route, or a probability of successful delivery.

## Part 3: Implement

Complete both functions in `lab.py` with standard-library Python:

- `maximum_flow` returns a dictionary with exactly one entry for every supplied
  arc, including zero amounts. Values are integer nonnegative flows, constrained
  by the original capacities and conservation, with maximum net source outflow.
- `minimum_cut` returns any optimal source-side vertex set. It includes source,
  excludes sink, and contains no unknown vertices.

Raise `ValueError` for unknown or identical terminals. Otherwise assume valid
graph inputs as documented. Do not modify the capacities dictionary, mutate
inputs, or consult global scenarios. No algorithm, tie-breaking rule, or exact
optimal representative is prescribed. Choose an approach you can justify for
the tiny instances. No reference solver is supplied.

Write correctness and termination arguments. Compute the value and capacity of
your outputs, compare with original predictions, and investigate discrepancies.
Agreement between two routines is useful evidence but can also reflect a shared
mistake; retain independent mathematical checks.

## Part 4: Behavioral checks

After making your own predictions, run from the repository root:

```sh
python3 -B -m unittest discover -s labs/06-flows -p 'test_*.py' -v
```

Run each lab separately because module filenames are shared. The untouched
scaffold raises `NotImplementedError`, so initial errors indicate unfinished
learner work. No external package or installation is needed.

The tests check feasibility and known optimum values on separate small examples.
Cut tests compare original outgoing capacities with independently specified
optimum values. They do not obtain expected answers from the flow routine.
Main-scenario checks verify contracts without supplying an optimum table.

Passing tests does not prove general correctness or assess the written work.
A faulty implementation may fail to terminate; interrupt it and revisit your
argument. No real sleeps, performance benchmark, or production timeout is required.
Discuss apparent contract conflicts before changing supplied tests.

## Part 5: Interpretation and review

Write a short capacity report stating the commodity, units, terminal pair,
steady-state assumptions, feasible output, and optimality evidence. Discuss a
proposed intervention and the additional evidence needed to recommend it.

Explain the limitations introduced by ignoring costs, transit time, storage,
multiple commodities, failures, and changing demand. Do not infer practical
reliability or acceptable service solely from a throughput maximum.

## Completion checklist

- [ ] Drawings, flow predictions, cuts, and capacity-change predictions recorded.
- [ ] Mathematical prompts attempted and reviewed, with gaps addressed.
- [ ] Both learner functions pass independent behavioral checks.
- [ ] Correctness, conservation, optimality, and termination arguments reviewed.
- [ ] Capacity report explains units and the model's operational limits.
- [ ] Entire Chapter 6 checklist and selected exercises reviewed.

Scaffold preparation does not complete learner work. The agent follows the
project's gradual-assistance policy for clarification and review.

## Deferred work

Costs, multiple commodities, floating-point or time-dependent capacities,
production input validation, real services, optimized solvers, and large-scale
performance work require later planning and approval.

## Technology extension

See [technology.md](technology.md) for the approved technology-study addition,
including task-specific library permissions and validation prompts. The core
exercise and tests above retain their existing scope. Technology setup and
runnable extension work remain a separate step; this addition does not complete
any learner work. Earlier deferred-work statements apply to the core exercise;
the extension describes the additional planned scope explicitly.
