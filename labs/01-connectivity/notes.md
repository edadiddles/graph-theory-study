# Lab 1 working notes

Keep original predictions when recording later corrections. Incomplete attempts
and specific questions are welcome. This file intentionally contains no answers.

## Model in my own words

What do records, candidate edges, and entity labels represent?

## Predictions before computation

For each scenario, include a drawing, components, bridges, cut vertices, cycles
or forest status, and reasoning. Compare the proposed groups with known labels.
Select an edge and vertex deletion and predict their effects.

### Scenario 1

### Scenario 2

### Scenario 3

### Scenario 4

### Scenario 5

## Mathematical attempts

### Path relation

### Grouping claim and identity assumption

### Similarity-threshold example

### Structural importance and match correctness

## Implementation observations

What did I implement? Which contract requirements did I check?

## Predictions versus results

What agreed, what differed, and why? Preserve the original prediction above.

## Model interpretation

Separate mathematical statements, computational observations, and identity
assumptions. Describe limitations and a question deferred to later labs.

## Questions for focused review

Identify a prompt or code region, what I tried, and the specific obstacle.

## Review record

Record feedback and remaining questions without marking unfinished work complete.

## M01 learning card: agent-prepared

This section is an agent-prepared study plan, separate from the learner's
original working sections above. It contains no predictions, implementations,
proofs, quiz answers, or completed learner results. M01 uses the whole existing
[connectivity exercise](exercise.md) under the adopted
[roadmap](../../ROADMAP.md) and [assessment policy](../../ASSESSMENT.md).

**Status:** prepared for the prerequisite diagnostic; no responses or readiness
outcomes recorded. Textbook exercise references remain pending diagnostic and
edition/statement verification. M02 remains gated on M01's completed review.
No additional technology or package setup is needed for M01.

### Required objectives

| Objective | Depth | Learning evidence to develop |
|---|---|---|
| M01-E1 | Explain | Use paths, components, cycles, trees/forests, bridges, and cut vertices precisely, including isolated vertices and deletion conventions |
| M01-E2 | Explain | Distinguish record vertices, supplied candidate edges, known synthetic identity labels, graph claims, and additional application assumptions |
| M01-A1 | Apply | Draw and predict all five source scenarios, compare groupings with labels, and predict the selected edge/vertex deletions before computation |
| M01-J1 | Justify | Investigate the path-defined relation and justify the properties claimed in the original mathematical prompt |
| M01-A2 | Apply and justify | Construct and justify the requested numerical similarity-threshold example under an explicit rule |
| M01-J2 | Justify | Address the original structural-importance prompt with arguments or examples that support the stated scope of the claim |
| M01-A3 | Apply | Independently implement connected_components for its full documented contract using only graph inputs and standard-library Python |
| M01-J3 | Justify | Explain why the implementation returns the claimed components and handles the specified boundaries; separate its computational observations from identity conclusions |

These objectives cover the existing lab's predictions, all four mathematical
prompts, implementation, and interpretation. The diagnostic and final quiz
assess different things: prerequisites first, milestone learning after study.

### Initial effort estimate

| Planned work | Active hours |
|---|---|
| Prerequisite diagnostic and focused preparation plan | 0.25-0.5 |
| Targeted Trudeau refresher | 0.5-0.75 |
| Scenario drawings, predictions, and deletions | 0.75-1.0 |
| Mathematical attempts and selected exercises | 0.75-1.0 |
| Implementation, behavioral checks, and interpretation | 0.75-1.25 |
| Mixed quiz and objective-specific review | 1.0-1.5 |
| Total initial estimate | 4.0-6.0 |

This is an uncalibrated estimate, not a limit. Prior familiarity may shorten
practice; substantial prerequisite remediation or reassessment is estimated
separately. Revisit the budget after the diagnostic and exercise selection.
If the actual scope is too large, review a meaningful split rather than rushing
proofs or silently removing original requirements.

### Prerequisite diagnostic plan

Conduct short conversational checks, with no model answers supplied. Diagnose:

- Quantifier meaning/order and how a general claim differs from examples.
- Sets, membership, relations, and partition language used by the lab contract.
- The difference between a definition, an assumption, and a justified conclusion.
- Basic graph vocabulary, checking what needs refresh without grading new work
  as if it had already been studied.

Use reasoning from each response to choose the next relevant check. Clarify
notation directly when that is the obstacle. Use unrelated examples where a
check or explanation could disclose a core lab argument. Record assistance and
any focus areas after responses arrive; leave outcomes blank before then.

### Reading and agent-selected exercises

Refresh Trudeau by topic: paths, connectivity, trees/forests, cycles, and the
relevant separating-vertex/edge notions where covered. Exact pages and section
names must be verified against the learner's copy. The exercise's vocabulary
sets the lab conventions without asserting a page reference for every term.
No Diestel or Chung reading is required for M01.

If the diagnostic identifies proof/relations gaps, select a focused Eccles or
Epp passage; consult [supplementary resources](../../SUPPLEMENTS.md) only for a
specific unmet need. Do not assign another full foundations course by default.

The original lab prompts are assigned independent work. After the diagnostic,
the agent selects any additional textbook exercises needed for objective coverage
and verifies statements and identifiers before assignment. Keep the set small
and purposeful; selection remains the agent's job. These choices are pending,
not a claim that a numbered Trudeau problem has already been verified.

| Selection item | Status or evidence |
|---|---|
| Trudeau edition/ISBN and relevant page access | Pending verification |
| Diagnostic gaps and focused reading | Awaiting responses |
| Verified textbook exercises and objective IDs | Pending diagnostic and access |
| Selection rationale and estimated added effort | Pending selection |

### Short-session stopping points

Work in the existing learner sections above, preserving originals and corrections.
The following are resumable task boundaries, not mandatory session lengths:

1. Finish a diagnostic check and record a focused next action.
2. Finish one relevant reading segment and record vocabulary questions.
3. Draw and predict one scenario, including the selected deletions, then pause.
4. Attempt one mathematical prompt and state any unresolved obstacle.
5. Implement or review one part of the function contract after predictions.
6. Compare one experiment with its preserved prediction and interpret it.
7. Complete a declared assessment batch or focused review task.

At each pause record where I stopped, next action, and an unresolved question.
After a break, use a short check of the prerequisites needed to resume.

### Implementation and behavioral checks

Keep the existing connected_components task and test suite unchanged. The
function must include every vertex in the documented partition, handle empty
and edgeless inputs, respect undirected edges, avoid mutation, and ignore the
record table/identity labels. Other malformed-input handling remains deferred
under the core contract. No reference algorithm or solver is supplied here.

After independent predictions and an implementation attempt, use the command in
[the exercise](exercise.md) to run its tests. Empty/isolate, path, cycle, and
source-scenario invariant checks support implementation review. Input preservation,
independence from labels, and general correctness also need inspection/reasoning;
the current tests are not presented as exhaustive proof. Record actual outcomes
only after execution. Any proposed test change follows the approval workflow.

### Mixed assessment blueprint

The table specifies evidence categories, not actual questions or expected answers.
Generate fresh questions when the learner is ready. A task may assess several
objectives; there is no requirement for eight separate quizzes.

| Objective | Closed-book reasoning coverage | Separate open-book application coverage |
|---|---|---|
| M01-E1 | Explain the relevant concepts and conventions in the learner's own words | Use appropriate vocabulary in a new small graph |
| M01-E2 | Explain the roles of observations, labels, and assumptions | Interpret outputs in a distinct record-model example |
| M01-A1 | Explain a prediction or deletion claim with its assumptions | Analyze an unfamiliar graph and compare predictions with computation |
| M01-J1 | Supply the required relation reasoning at the agreed scope | Apply the reasoning consistently when interpreting a new case |
| M01-A2 | Explain the rule and justification of the learner's construction | Transfer the distinction to a fresh admissible example if needed |
| M01-J2 | Justify the stated structural-versus-identity claim | Critique a new modeling conclusion at the stated scope |
| M01-A3 | Explain the implemented contract and its boundaries | Use and inspect the learner's implementation on fresh inputs |
| M01-J3 | Defend the implementation argument and distinguish evidence types | Explain discrepancies or limitations without treating tests as proof |

Closed-book work permits clarification of wording but no notes, code, references,
or substantive assistance. Open-book work permits the learner's notes, owned
references, and own implementation with standard-library support. Component
solvers and answer-producing agent help cannot replace the independently assessed
work. Follow gradual assistance if a task becomes practice rather than assessment.

Every required objective must be ready at its declared depth, with original
lab obligations reviewed, before advancing. Record focused review or pending
evidence per objective; a percentage cannot compensate for a missing objective.
After a substantive gap, use targeted practice and a fresh comparable independent
task. Keep minor slips, conceptual gaps, and uncertain grading distinct.

### Diagnostic, quiz, and readiness record

Leave results unfilled until the work occurs. Record actual prompts/responses,
permitted aids, assistance, evidence, review tasks, and reassessment here. Preserve
the learner's original attempts in the working sections above.

| Objective | Readiness | Response/evidence reference | Review or reassessment |
|---|---|---|---|
| M01-E1 | Not assessed | | |
| M01-E2 | Not assessed | | |
| M01-A1 | Not assessed | | |
| M01-J1 | Not assessed | | |
| M01-A2 | Not assessed | | |
| M01-J2 | Not assessed | | |
| M01-A3 | Not assessed | | |
| M01-J3 | Not assessed | | |
