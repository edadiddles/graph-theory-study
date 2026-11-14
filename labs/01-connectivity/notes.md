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
original working sections above. The plan and blueprint supply no solutions;
actual diagnostic work is preserved in the record below as it occurs.
M01 uses the whole existing
[connectivity exercise](exercise.md) under the adopted
[roadmap](../../ROADMAP.md) and [assessment policy](../../ASSESSMENT.md).

**Status:** initial prerequisite diagnostic reviewed; focused preparation P01
below is assigned. The learner supplied both book ISBNs, Trudeau chapter starts,
and exercise photographs. Eccles reading and one problem are selected; Trudeau
Exercises 5 and 11 are verified and assigned in P02 below.
Milestone objectives and the final quiz remain unassessed. M02 remains gated on
M01's completed review.
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
not a claim that every textbook exercise or page has been inspected. The current
verified selections are recorded below.

| Selection item | Status or evidence |
|---|---|
| Trudeau edition/ISBN and relevant page access | Learner supplied ISBN 9781684112319, all eight chapter starts, and local photographs of the Chapter 2 exercise pages |
| Eccles edition/ISBN | Learner supplied ISBN 9780521597180; matches Cambridge's paperback record |
| Diagnostic gaps and focused reading | D01-D04 reviewed; focused implication/proof-structure work begins with P01 |
| Verified textbook exercises and objective IDs | Eccles Problems I, Question 2 supports proof prerequisites; Trudeau 5 supports M01-E1/A1/J3 and 11 supports M01-J3 proof practice; see P01/P02 |
| Selection rationale and estimated added effort | P01: implication meaning, 0.5-1.0 active hour of prerequisite preparation; P02: path representations and proof practice, initially 0.5-1.0 active hour for the two problems within the milestone's mathematical-work budget, subject to recalibration |

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

#### M01-D01: quantifier order and general justification

Format: conversational prerequisite diagnostic, requested from current
understanding. This is not the final milestone quiz.

Prompt: decide whether these statements mean the same thing, classify each as
true or false, and justify the answers:

1. For every real x, there exists a real y such that y > x.
2. There exists a real y such that, for every real x, y > x.

Initial learner response:

> 1. true. i have relatively high confidence. 2. false. i have relatively high confidence though could see some construct like infinity which could be considered Real is argued to be greater than itself.

Assistance: confirmed the truth values and clarified that infinity is not a real
number; even in the extended reals, positive infinity is not strictly greater
than itself. Requested a justification of the first statement without supplying
a witness.

Learner's first-statement argument:

> suppose x in real numbers. let's construct y as a real number such that y = x + 0.01. then no matter the choice of x, y is a real number (addition of two real numbers) and y > x by construction.

Review: accepted the constructive argument, including real-valuedness and the
strict inequality for arbitrary x. Requested a justification of the second
statement using real numbers.

Learner's second-statement argument, before wording correction:

> suppose y is a real number. we want to find some value of y such that y > x regardless of x. this would mean y is the maximal value in the reals. however, (1) guarantees that there exists a real number k such that k > n for every real n. Thus the reals has no maximum and thus the statement is false.

Assistance: identified that the sentence about k, as written, asserted one k
above all real n. Asked the learner to restate the quantifiers in the order
justified by statement 1, without supplying the replacement sentence.

Learner correction:

> i said it backwards to try to prevent having to backspace. it should have been a restatement of (1) for every real n, there exists a real k such that k > n

Review outcome: accepted the corrected no-maximum argument. The learner
identified the reversal as a wording error. The constructive first argument and
corrected second argument support proceeding to the next prerequisite check.
Record the infinity clarification and quantifier feedback as assistance; no
milestone objective or final-quiz result is marked ready from this diagnostic.
Active time was not measured. Next check: sets and partitions.

#### M01-D02: sets and partitions

Format: conversational prerequisite diagnostic, not the final milestone quiz.

Initial prompt: state the partition conditions and decide whether
{{1, 2}, {2, 3}, {4}} partitions S = {1, 2, 3, 4}, explaining the reasoning.

Learner response:

> I forget the definition of partition.

Assistance: supplied the definition directly: nonempty subsets, union equal to
the underlying set, and pairwise disjointness; equivalently, each element belongs
to exactly one member. Did not apply the definition to the supplied example.

Learner's application:

> ok, with that clarification, it describes the necessary conditions. The provided set S does not qualify as a partition of S. the two subsets {1,2} and {2,3} intersect (2 is the intersection) which is a check for disqualification.

Review: accepted rejection of the collection due to overlap. Clarified the
notation: the intersection is the set {2}, with 2 its shared element.

Fresh check: decide whether P = {{a, c}, {b, d}} partitions T = {a, b, c, d},
justifying each condition.

Learner response:

> yes, P does partition T because the union of the subsets of P is {a,c,b,d} (preserving the order) which contains all elements of T. order doesn't matter and was used to provide some insight that I understood the subset division and what the union operation does.

Assistance: accepted the coverage and order reasoning; requested that the
remaining two conditions also be checked, without supplying those checks.

Learner's completion:

> P contains two members A={a,c} and B={b,d}. each member is non-empty since A contains a and c while B contains b and d. They are pairwise disjoint because a is not in B, c is not in B, b is not in A, and d is not in A

Review outcome: accepted the completed justification of all three conditions.
The definition needed refreshing; the learner then correctly recognized an
overlap and applied the conditions to a fresh example. Record the definition,
notation clarification, and completeness reminder as assistance. Current evidence
does not indicate a need for more partition practice before the next prerequisite
check. Milestone objectives and the final quiz remain unassessed. Active time
was not measured. Next checks: definitions/assumptions/conclusions and graph
vocabulary.

#### M01-D03: definitions, assumptions, conclusions, and proof structure

Format: conversational prerequisite diagnostic. The summaries below describe
the exchange; quoted excerpts preserve the learner's wording. This is not an
independent end-of-milestone assessment.

Initial prompt: explain how a definition, an assumption, and a conclusion differ
in a mathematical argument, in the learner's own words.

The learner described definitions as grounding the idea, assumptions as statements
used as true, and conclusions as argument outcomes. They supplied the familiar
irrationality-of-sqrt(2) proof as an example of assuming rationality and reaching
a contradiction. Their initial account also included:

> assumptions are used as argument technique that allows the argument to progress with the caveat that the assumption must be true for th argument and the subsequent conclusion to be valid.

Assistance: pointed out the tension between that sentence and the learner's own
contradiction example; asked for a revision. The learner distinguished an unproved
supporting claim from a temporary contradiction assumption, while also asserting:

> In the case of a constructive proof (i think this is being used correctly) assumptions that are false would cause any arguments relying on those assumptions to be false.

Assistance: introduced the unrelated conditional x = 2 implies x squared = 4,
evaluated at x = -2, to examine whether a false premise forces a false conclusion.
The learner questioned the change of context but explicitly corrected the claim:

> to your point, a false assumption is not sufficient to make the derived conclusion false.

Clarification: acknowledged that the example's framing could have been clearer;
explained evaluation of the conditional under the supplied value and separated
valid inference from truth of the premises. The learner also emphasized that
intervening reasoning must be checked independently.

Follow-up prompt: suppose P is assumed and an attempted proof gets stuck at an
unjustified intermediate step; does that establish that P is false, and why?

The learner requested clarification of both "cannot justify an intermediate
step" and the role of P. These were ambiguities in the diagnostic wording,
not evidence of learner error. Clarified that a proposed transition A implies B
had no currently supplied justification, and that the intended goal was to prove
not-P by contradiction while temporarily assuming P.

Learner's final response included:

> ok, the inability to justify a step doesn't mean the step is invalid. in this case, an inability to justify the statement if A then B means that your proof in incomplete.

The learner connected the issue to a missing supporting parity lemma in their
sqrt(2) example and observed that a disproved supporting claim would require
repairing or modifying the argument. Their description of finishing the proof
also said:

> a complete proof would be the justification of A then B and the assertion of it's meaning 'thus p cannot be true'.

Review: accepted the distinction between an incomplete attempted proof and a
disproof. The remaining refinement is that a justified transition alone does
not reject P: a contradiction must actually follow from the assumptions through
valid reasoning. Keep proof structure as a focused refresher topic, with a fresh
small check before relying on it in the main lab. Do not infer independent proof
mastery from this assisted discussion or treat the learner's proof summary as a
fully supplied proof. No textbook section or exercise number has been invented.
Milestone objectives and the final quiz remain unassessed. Active time was not
measured. Next diagnostic area: graph vocabulary.

#### M01-D04: connected graphs, trees, and rooted structure

Format: conversational prerequisite diagnostic. Initial prompt: explain how a
connected graph and a tree differ, with a small example.

Learner's initial response:

> a tree is structurally hierarchical where a graph is not. By that I mean, there is a clear parent child relationship on a tree where a graph doesn't have this requirement. If we take a tree that has A->B->C, if we had a connection like C->A, then it is no longer a tree but it is a graph. One thing to note is that a tree is a graph but a graph is not necessarily a tree.

Assistance: accepted that trees are graphs and that the added connection in the
example creates a cycle. Distinguished a rooted tree's hierarchy from the simple
undirected definition used in the lab: connected and acyclic. Explained that
connectedness requires a path between every pair and that choosing a root adds
the parent/child interpretation.

Fresh check: vertices {u, v, w, z} with only edges {u, v} and {w, z}; decide
whether it is a tree and check both conditions.

Learner response:

> no, it would need an edge {u,w}, {u,z}, {v,w}, or {v,z}. Only one of these edges would make it a tree, otherwise two would provide a cycle

Review: accepted the rejection of the original disconnected acyclic graph.
Read "only one" as adding exactly one edge, consistent with the rest of the
response: any single listed cross-edge creates a tree, while adding any two
distinct listed cross-edges creates a cycle. This shows application of the
connected/acyclic conditions after the definition clarification. Do not infer
independent recall of all graph vocabulary from this one example. Active time
was not measured; milestone objectives and final quiz remain unassessed.

#### Initial diagnostic summary and focused preparation

This summarizes observed prerequisite evidence, not milestone completion or a
numerical grade. The record includes assistance and diagnostic wording issues.

| Area | Observed evidence | Next preparation |
|---|---|---|
| Quantifiers | Constructive witness and corrected no-maximum argument; infinity clarification and quantifier feedback recorded | Revisit wording as needed during proof work; no additional drill indicated now |
| Sets and partitions | Definition needed refresh; then identified overlap and checked all conditions on a fresh example | Keep the definition available for reading; no additional set drill indicated now |
| Proof structure | Corrected false-premise claim and distinguished an incomplete proof from disproof after discussion | Focused review of assumptions, valid inference, supporting lemmas, and an actual derived contradiction; fresh small check before main proof tasks |
| Graph vocabulary | Rooted hierarchy needed distinction from an undirected tree; then correctly analyzed the fresh case and connecting edges | Targeted Trudeau refresh of paths, connectivity, trees/forests, cycles, and the lab's separating-vertex/edge conventions |

Next study step: prepare the short proof-structure refresher and finalize the
agent-selected reading/exercises using verified source statements. The initial
inventory check found no edition identifiers; the learner subsequently supplied
both ISBNs, the Trudeau contents, and exercise photographs, recorded below.
Verified exercise selections are in P01/P02. No extra book purchase or dependency
installation is indicated by this initial diagnostic. Existing core lab prompts
remain assigned; their graph predictions and proofs have not been supplied.

#### M01-P01: focused implication refresher and selected exercise

Status: assigned, not attempted or assessed in this record. This is preparation
informed by D03, not the final milestone quiz. The learner supplied:

- Trudeau, Introduction to Graph Theory: ISBN 9781684112319.
- Eccles, An Introduction to Mathematical Reasoning: ISBN 9780521597180.

Book identifiers are recorded here; the separate library inventory has not been
edited. Do not transfer pagination or exercise numbering from a different Trudeau
ISBN. Chapter starts and the selected exercise statements from that copy are
verified from learner-supplied material below.

Assigned next work:

1. Read Eccles Chapter 2, **Implications**, printed pages 10-20. Focus on the
   meaning of an implication, the roles of hypothesis/conclusion, and the
   distinction between the truth of component statements and the implication.
   Consult Chapter 1's connective notation only if it is needed for this reading.
2. Attempt **Problems I, Question 2** in the Part I problem set (printed pages
   53-58). Follow the problem's truth-table instruction and compare the three
   statements it specifies. This is one selected problem, not the full problem
   set. Use the statement in the learner's book; no worked table or answer is
   supplied in these notes.
3. Preserve the original table/reasoning and note any specific obstacle for
   review. Use the existing gradual-help policy. A fresh small prerequisite
   check follows review; completing this exercise does not mark M01 ready.

Selection rationale: the diagnostic identified uncertainty about premise truth,
conditional statements, and valid inference. The selected problem practices that
distinction with explicit logical statements rather than changing the numerical
context of another example. It supports later relation and implementation
arguments without supplying the graph lab's proof or algorithm.

Provisional effort: 0.5-1.0 active hour for reading and the selected problem,
with flexible stopping points after reading or an initial table attempt. This is
targeted prerequisite work additional to the initial core estimate, not a time
limit. Actual time and outcomes remain unrecorded until work occurs.

Verification provenance: Cambridge's paperback record identifies the supplied
Eccles ISBN. Its chapter listings give Chapter 2 as pages 10-20, and its publicly
indexed Problems I extract (pages 53-58) provides the Question 2 statement used
for selection. This uses publisher-provided material rather than an unofficial
book or solutions upload. Publisher pages:

- [Eccles book record and contents](https://www.cambridge.org/highereducation/books/an-introduction-to-mathematical-reasoning/884E620008388D6452ED9707CBEA0BF0/modular-arithmetic/A07CF0317D88FFDF711CDE44BA90ADCF)
- [Chapter 2 publisher listing](https://www.cambridge.org/core/browse-subjects/mathematics/logic-categories-and-sets/listing?pageNum=294)
- [Problems I publisher extract/listing](https://www.cambridge.org/core/browse-subjects/mathematics/logic-categories-and-sets/listing?pageNum=296)

Access limitation: the publisher's scanned excerpt could not be rendered through
the available screenshot tool, and some direct pages were unavailable. The
assignment relies on the visible indexed publisher chapter/problem statements,
not an inferred exercise number or a claim to have inspected the full chapter.
If the physical copy differs, resolve the discrepancy before attempting it.

#### Trudeau contents supplied by the learner

Source: typed transcription from the learner's copy, ISBN 9781684112319.
Capitalization is normalized below; titles and page starts are preserved.

| Chapter | Title | Starting page |
|---|---|---|
| 1 | Pure Mathematics | 1 |
| 2 | Graphs | 12 |
| 3 | Planar Graphs | 64 |
| 4 | Euler's Formula | 97 |
| 5 | Platonic Graphs | 117 |
| 6 | Coloring | 127 |
| 7 | The Genus of a Graph | 141 |
| 8 | Euler Walks and Hamilton Walks | 172 |

Chapter 2 is the first relevant refresher block. Its page interval is 12-63,
inferred from the supplied start of Chapter 3, not inspection of every page.
The contents alone do not establish the location of every vocabulary item or
the wording of exercises. Keep the core lab's conventions explicit and avoid
claiming a precise Trudeau location for a term until the text is checked.

Exercise access was subsequently resolved by the learner-supplied local images
listed in P02. Typed statements and vertex/edge descriptions remain suitable
alternatives for future selections. The assigned problems were selected from
the actual photographed statements, not the contents alone.

#### M01-P02: selected Trudeau graph and proof exercises

Status: assigned; no attempts, results, or readiness outcomes recorded. The
learner supplied four local photographs, all inspected directly:

| Source image | Visible material used to verify selection |
|---|---|
| image3.jpeg | Chapter 2 Exercises 1-20; right-hand page visibly numbered 57, with Exercise 5 on the facing left page |
| image2.jpeg | Pages 58-59, later exercises and figures |
| image1.jpeg | Pages 60-61, figures and later exercise text |
| image0.jpeg | Pages 62-63, final figures/exercise continuation and suggested reading |

Original source directory: `/mnt/c/Users/EdwardRuzek/Downloads/`. The images are
learner-provided views of the copy identified by ISBN 9781684112319. They were
read in place; no image files or worked solutions have been added to the study
repository. Exercise 5's page 56 is inferred from its position facing the
visibly numbered page 57. The selected exercise numbers and statements are clear.

Review the Chapter 2 exposition relevant to graph definitions, path graphs, and
degree notation in the learner's copy. Keep the lab's undirected-graph conventions
explicit. The supplied exercise pages do not establish where every tree,
connectivity, bridge, or cut-vertex definition occurs in the preceding text;
no exact page reference for those terms is being invented.

Selected independent work, using the full wording in the book:

| Reference | Required work | Purpose and objective support |
|---|---|---|
| Chapter 2, Exercise 5, p. 56 (facing p. 57) | Follow the given vertex/edge definition of P_v, draw its first five graphs, then find and prove a general formula for its edge count | Connect formal graph input, drawings, and a justified general claim; supports M01-E1/A1 and the reasoning discipline in M01-J3 |
| Chapter 2, Exercise 11, p. 57 | Prove the stated degree-sum identity in terms of the graph's edge count | Practice a general graph argument with explicit assumptions and justified steps; supports M01-J3 proof discipline |

Exercise 5 refers to the book's Theorem 2 as an analogy. The theorem's text is
not in these photographs; consult it in the physical book as needed. The exercise
statement itself, including its path-graph definition and requested output, was
verified. No formula, drawing, proof strategy, or worked answer is supplied here.
Exercise 11 uses degree as a supporting definition from the reading; it does
not introduce an unannounced extra topic into M01's final quiz blueprint.

Sequence: finish P01's Eccles reading/problem and focused review first, then
attempt Trudeau 5, followed by 11. Preserve original work and request focused
review of an obstacle or completed argument. Current selection is limited to
these two Trudeau problems; the other photographed exercises are not assigned
for M01. Core lab prompts and reading obligations remain as stated.

Initial effort estimate for the two Trudeau problems: 0.5-1.0 active hour,
uncalibrated, with a natural stopping point after Exercise 5's drawings or proof
attempt. Account for this in the milestone's mathematical-work budget and
revisit the total after actual attempts; do not silently assume the additional
problems plus all original prompts fit the earlier estimate. Focused reading or
remediation beyond that estimate is recorded separately. None of this is timed
or used as a grading threshold.

Review checks: definition/drawing consistency and the scope of the general
argument in Exercise 5; the stated assumptions and validity of the proof in
Exercise 11. Assessment records remain blank until actual attempts are supplied.
Exercise completion alone does not establish all M01 objectives or permit M02.
