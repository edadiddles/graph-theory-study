# Lab 16: independent modeling project

Choose an application and build a defensible argument from a question through
data, graph representation, mathematics, computation, and interpretation. This
project synthesizes the course; it does not require using every studied method.
The graph, methods, predictions, code, and conclusions remain your work.

## Working arrangement

Use the tutoring rules in [AGENTS.md](../../AGENTS.md). Ask for focused review
of your attempts; clarification does not authorize an agent to finish the model,
implementation, or proof. Record assistance in [notes.md](notes.md).

Begin with [project-brief.md](project-brief.md), then develop
[validation-plan.md](validation-plan.md) and [reading.md](reading.md).
These are blank planning templates. No application has been selected, no dataset
has been acquired, and no solution or application-specific tests are supplied.
Code and tests will be designed after the question and expected behavior are
agreed. New dependencies require approval; existing NumPy remains available
under the earlier agreement, with environment setup left to you.

## 1. Select the question

Choose an application you want to understand. Possibilities include entity
resolution, software dependencies, transport resilience, network communities,
or physical diffusion. These are starting subjects, not assigned questions or
method recommendations. You may propose a different application.

State one question that could be answered within a bounded project. Identify
the intended conclusion, what evidence could challenge it, and what remains
outside scope. Describe why a graph is useful and which modeling assumptions
need scrutiny. Propose a manageable data source or synthetic construction.

**Review checkpoint:** present the question, scope, proposed data, and initial
representation for discussion before designing application-specific code.

## 2. Define the model and evaluation

Specify vertices, edges, direction, weights, missing data, and any time or
boundary conventions that matter. Distinguish observations, constructed graph
properties, and claims about the application. Explain the intended meaning of
each output and choose methods whose assumptions you can justify.

Design a small case with independently derived expected results and a larger
empirical case that remains practical on your machine. Larger means larger than
the hand case, not a requirement for a large dataset. The empirical case may
use documented observed data or reproducibly generated synthetic observations;
state what its origin permits you to conclude.

Choose a baseline that addresses the question. Identify consequential modeling
choices to vary in a sensitivity investigation. Define success criteria before
seeing the final results. Where labels or reference outcomes are uncertain,
explain what evaluation is possible and what cannot be established.

**Review checkpoint:** present the completed brief, proposed validation scenarios
and expected outcomes, method rationale, and targeted reading. Agree on a small
implementation slice and its tests before creating application-specific code.

## 3. Implement and investigate

Start with the small case. Derive its expected behavior independently of the
implementation; preserve that reasoning and your predictions. Add focused tests
for the agreed outputs and relevant invariants. Validate this slice before
working on the larger empirical case.

Record data provenance, transformations, versions, seeds where applicable,
parameters, and run instructions. Choose modest resource limits appropriate to
your actual data. Record basic handling of missing or invalid inputs and
operational failures that matter in the chosen application. Keep unexpected
defects visible. Document limitations instead of assuming production scale or
adding safeguards for an unspecified deployment.

Run the planned baseline and sensitivity comparisons. Retain contradictory
observations and failed predictions. If the question, acceptance criteria, or
tests need revision, explain and review the change before proceeding; preserve
the original plan so changes are visible.

**Review checkpoint:** present actual test results, the small-case argument,
empirical evidence, deviations from predictions, and unresolved problems.

## 4. Defend the conclusions

Use the report prompts in [notes.md](notes.md). Trace the argument from the
application question to representation, hypotheses, method, evidence, and claim.
Include an appropriate mathematical justification: a proof, certificate, or
analytical bound, with exact hypotheses and scope. Explain what it establishes
and which remaining conclusions depend on empirical evidence or assumptions.

Present the baseline and sensitivity findings, numerical limitations where
relevant, and reproducible instructions. Distinguish algorithm correctness from
model adequacy. For entity resolution, distinguish candidate-match edges,
connectivity, and actual shared identity; for another domain, state the analogous
gap between graph properties and real conclusions.

## Completion checkpoint

- [ ] Question, graph definition, data provenance, and method rationale reviewed.
- [ ] Small-case expectations independently justified and actual tests recorded.
- [ ] Larger empirical case, baseline, and sensitivity investigation reviewed.
- [ ] Mathematical argument, assumptions, numerical issues, and limitations reviewed.
- [ ] Reproduction instructions and assistance record complete.
- [ ] [Diestel audit](../11-decompositions/consolidation.md) and
  [Chung audit](../15-heat-walks/consolidation.md) reviewed, including pending
  original-copy section inventories and remaining learning gaps.
- [ ] Final discussion completed, with unresolved questions explicitly recorded.

Scaffold creation and passing software tests alone do not complete this project
or either textbook's reading and proof requirements.
