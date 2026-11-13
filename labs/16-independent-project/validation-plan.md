# Independent project validation plan

Complete and review this before application-specific implementation. Derive
expectations from the agreed question and requirements. The table below is
blank; no application-specific acceptance criteria or tests have been decided.

## Observable requirements and acceptance scenarios

Give each requirement a stable identifier. Map every specific requirement to
an appropriate test or review, with its expected outcome and evidence. A single
check can protect multiple requirements when the relationship is explicit.

| Requirement ID and behavior | Scenario or input | Independently justified expectation | Test or review level | Evidence location |
|---|---|---|---|---|
| | | | | |

## Small-case expectations before computation

Record the hand argument, assumptions, expected outputs or acceptable witnesses,
and why they provide an independent check. For nonunique valid outputs, specify
the required properties instead of an arbitrary preferred answer.

## Mathematical justification and invariants

Identify the proposed proof, certificate, or bound; state hypotheses, what its
review will establish, and which claims remain empirical. Select structural or
numerical invariants relevant to this model rather than testing every property
of an underlying library.

## Larger-case evaluation and baseline

Specify data origin, evaluation quantities, the baseline's purpose, expected
comparison or decision criterion, and what a contradictory result would mean.
If labels are uncertain or unavailable, state the resulting evaluation limits.

## Sensitivity investigation

Choose consequential graph or data assumptions, specify the variations, and
record predictions before running them. Explain which conclusion each
comparison tests. Keep performance claims within measured workloads.

## Boundary and failure scenarios

Select relevant cases for the chosen model: empty or missing inputs, disconnected
structure, invalid weights, uncertain labels, unavailable data, or other actual
boundary conditions. Specify expected behavior and distinguish operational
failures from programming defects. Mark irrelevant cases with a reason.

## Numerical verification, if applicable

Justify tolerances, residuals, state conventions, and any conservation or
dissipation checks. Separate floating-point evidence from analytical claims.
Record why this section does not apply if the project is purely discrete.

## Reproduction and environment

Record data provenance and transformations, versions, seeds where relevant,
parameters, commands, expected output artifacts, and practical resource limits.
List needed fixtures and dependencies; obtain approval for new dependencies.

## Planned checks and actual outcomes

Keep plans separate from execution evidence. Leave outcomes blank until run.

| Check and protected requirement IDs | Planned command or review | Actual outcome | Evidence and limitations |
|---|---|---|---|
| | | | |

## Gaps and deferred scenarios

State what is unverified, why it is deferred, and how that limits conclusions.

## Plan review and revisions

Record approval and reasons for changes. Investigate failures against agreed
requirements; do not change expected outcomes simply to make code pass. Review
changes to tests, assumptions, or acceptance criteria explicitly before editing.
