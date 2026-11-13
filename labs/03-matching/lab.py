"""Synthetic cross-database candidates and an unfinished matching task.

Each edge is oriented (left record, right record). Identities are evaluation
labels, not inputs to the algorithm. Importing the module runs no experiments.
"""

LEFT_RECORDS = {
    "L1": {"name": "Alex Morgan", "true_entity": "person-1"},
    "L2": {"name": "Alex J. Morgan", "true_entity": "person-2"},
    "L3": {"name": "Sam Lee", "true_entity": "person-3"},
    "L4": {"name": "Riley Chen", "true_entity": "person-4"},
}

RIGHT_RECORDS = {
    "R1": {"name": "A. Morgan", "true_entity": "person-1"},
    "R2": {"name": "Alex Morgan", "true_entity": "person-2"},
    "R3": {"name": "S. Lee", "true_entity": "person-3"},
    "R4": {"name": "Riley Chen", "true_entity": "person-5"},
}

LEFT = tuple(LEFT_RECORDS)
RIGHT = tuple(RIGHT_RECORDS)

SCENARIOS = {
    "scenario_1": (("L1", "R1"), ("L2", "R2"), ("L3", "R3")),
    "scenario_2": (("L1", "R1"), ("L1", "R2"), ("L2", "R1"), ("L3", "R3")),
    "scenario_3": (("L1", "R1"), ("L2", "R1"), ("L3", "R3"), ("L4", "R4")),
    "scenario_4": (
        ("L1", "R1"),
        ("L1", "R2"),
        ("L2", "R1"),
        ("L2", "R2"),
        ("L3", "R3"),
    ),
    "scenario_5": (),
}


def maximum_matching(
    left: tuple[str, ...], right: tuple[str, ...], edges: tuple[tuple[str, str], ...]
) -> set[tuple[str, str]]:
    """Return any maximum-cardinality matching using the supplied candidate edges.

    A matching is a set of candidate pairs in which no left or right record is
    used more than once. Maximize the number of selected pairs, not a similarity
    score or agreement with known identities. Any maximum matching is acceptable.

    Left and right IDs are unique within their respective tuples and disjoint
    across them. Each edge contains an ID from left followed by an ID from right.
    There are no duplicate candidate pairs. Inputs may be empty; invalid inputs
    are outside the initial contract. With no candidate edges, return set().

    Do not mutate inputs or consult LEFT_RECORDS, RIGHT_RECORDS, SCENARIOS, or
    identity labels. Use standard-library Python. Graphs are tiny; choose an
    approach you can justify without a prescribed algorithm or performance bound.
    """
    raise NotImplementedError("Implement maximum_matching for Lab 3.")
