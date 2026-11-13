# Lab 10: Observed networks and random baselines

## Goal and reading

Investigate which properties of an observed network a simple random model can
explain, and what remains unsupported. Read all of Diestel Chapter 11 using
[reading.md](reading.md). Use van Steen for network context and Epp or Triola
for identified probability gaps.

## Observed data

Use the locally saved [karate-club network](data/karate_club.json). Read its
[provenance](data/PROVENANCE.md) before modeling. The file is an unweighted,
undirected projection with explicit vertex IDs; weights and club labels have
been omitted. No NetworkX dependency or runtime download is required.

For example, load the graph from the repository root with standard-library code:

```python
import json
from pathlib import Path

data = json.loads(Path("labs/10-random/data/karate_club.json").read_text())
vertices = tuple(data["vertices"])
edges = tuple(tuple(edge) for edge in data["edges"])
```

This is an observational graph, not a random sample of all possible social
networks. An edge is not an entity-identity assertion. Data collection and
projection choices limit interpretation independently of algorithm correctness.

## Part 1: Predict and specify the model

Use [notes.md](notes.md) before coding or reading test expectations.

1. State what vertices and edges represent and which upstream information was
   discarded. Identify uncertainty the saved representation cannot resolve.
2. Define the independent-edge G(n,p) model mathematically, including its fixed
   vertex inventory and independence assumptions. Compare them with the observed
   network; do not assume the model is realistic because it is easy to simulate.
3. Predict useful comparisons for edge count, triangle count, and largest
   component size. Record reasoning and uncertainty before examining summaries.
4. Decide how to choose p using the observed edge density. Define density and
   justify the parameter choice. Explain which statistic is used in fitting and
   which comparisons could provide additional evidence about adequacy.
5. Attempt expressions for expected edge and triangle counts and edge-count
   variance under the model. State how independence enters each derivation.

## Part 2: Implement

Complete the two tasks in `lab.py` using standard-library Python:

- `sample_gnp(vertices, probability, rng)` returns sampled undirected edges on
  the explicit inventory, using the supplied generator under the docstring's
  draw contract. Output pairs have lexical endpoint order; isolates remain in
  the original inventory. Nonfinite or out-of-range probabilities raise ValueError.
- `graph_summary(vertices, edges)` returns exactly `edge_count`, `triangle_count`,
  and `largest_component_size`. Count each unordered triangle once. An empty
  graph has all-zero counts; nonempty edgeless graphs still have components.

Do not consult observed data within either function, mutate graph inputs, use
global random state, or reseed the supplied generator. Advancing that generator
is an intended effect. Fresh generators with the same seed and identical ordered
inputs must reproduce results. No particular summary algorithm is prescribed;
explain any reuse of your own earlier functions.

Write correctness and termination arguments, including why the sampler matches
the specified probabilistic model. Tests with a few controlled draws do not prove
the distribution or independence property for all inputs.

## Part 3: Run a reproducible ensemble

Plan the seed list, number of samples, statistics, and comparisons before looking
at outcomes. Start with a small ensemble, such as 30 independently initialized
standard-library `random.Random(seed)` generators with recorded distinct seeds.
Pseudorandom experiments are computational approximations, not independent
observational evidence. Do not search for a seed that produces a desired result.

1. Compute the observed summaries with your own implementation.
2. Sample graphs with the same inventory and your chosen p. Summarize each one.
3. Compare ensemble variation with the observed values and your theoretical
   predictions. Report sample count and seeds, not just a selected graph.
4. Examine why agreement on a fitting statistic alone is insufficient to assess
   the full model. Account for fitting and randomness in any stronger inference.
5. Identify which assumptions or retained features a different baseline might
   change. State the modeling question before proposing a more complex generator.

No formal hypothesis test, significance cutoff, or inferential confidence claim
is required in this iteration. A finite ensemble is exploratory, not a proof
of a threshold or an asymptotic property.

## Part 4: Behavioral checks

After an independent attempt, run from the repository root:

```sh
python3 -B -m unittest discover -s labs/10-random -p 'test_*.py' -v
```

Run labs separately because module names are shared. Untouched learner functions
raise `NotImplementedError`. The independent dataset-integrity test can pass
before those tasks are completed; that does not make the lab complete.

Unit tests use deterministic boundary cases, controlled draws, reproducibility,
state checks, and separate known graphs. No statistical pass/fail threshold or
real-time wait is used. The dataset test validates the saved snapshot and schema,
not its real-world validity or the learner's observed summary answers.

Tests do not prove general correctness, sampler independence, or model adequacy.
Interrupt nonterminating learner code and revisit its argument. Discuss apparent
contract conflicts before changing supplied tests.

## Part 5: Report and completion

Write a report distinguishing observed data, modeling assumptions, fitted
parameters, theoretical expectations, finite-sample observations, and conclusions.
Explain remaining uncertainty and avoid interpreting a structural similarity
or discrepancy as evidence of shared entity identity or a causal mechanism.

- [ ] Data provenance, model definition, predictions, and fitting choice recorded.
- [ ] Probability derivations attempted and reviewed, with gaps addressed.
- [ ] Both learner functions pass deterministic behavior tests.
- [ ] Code arguments and random-state handling reviewed.
- [ ] Ensemble plan, seeds, outputs, variation, and limitations recorded.
- [ ] Model-adequacy account separates fitting from evaluation.
- [ ] Entire Chapter 11 checklist and selected exercises reviewed.

Preparing files does not complete learner work. The agent provides focused
clarification and gradual assistance under `AGENTS.md`.

## Deferred work

Formal hypothesis testing, fitted-model uncertainty analysis, sophisticated null
models, large datasets, directed or weighted models, plotting libraries, automated
downloads, production input handling, and performance optimization require later
planning and approval.
