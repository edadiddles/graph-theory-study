"""Synthetic inputs and a learner task for the connectivity lab.

Importing this module performs no experiments and prints no results.
"""

RECORDS = {
    "A": {"name": "Alex Morgan", "true_entity": "person-1"},
    "B": {"name": "A. Morgan", "true_entity": "person-1"},
    "C": {"name": "Alex M.", "true_entity": "person-1"},
    "D": {"name": "Alex Morgan", "true_entity": "person-2"},
    "E": {"name": "A. J. Morgan", "true_entity": "person-2"},
    "F": {"name": "Sam Lee", "true_entity": "person-3"},
}

VERTICES = tuple(RECORDS)

SCENARIOS = {
    "scenario_1": (("A", "B"), ("B", "C"), ("D", "E")),
    "scenario_2": (("A", "B"), ("B", "C"), ("C", "D"), ("D", "E")),
    "scenario_3": (("A", "B"), ("D", "E")),
    "scenario_4": (("A", "B"), ("B", "C"), ("A", "C"), ("D", "E")),
    "scenario_5": (
        ("A", "B"),
        ("B", "C"),
        ("C", "D"),
        ("D", "E"),
        ("A", "E"),
    ),
}


def connected_components(
    vertices: tuple[str, ...], edges: tuple[tuple[str, str], ...]
) -> list[set[str]]:
    """Return the components of a simple undirected graph.

    Inputs are valid: vertex IDs are unique strings; each edge has two distinct
    endpoints from vertices; no undirected edge occurs twice. Inputs may be empty.

    Include every vertex, including isolated vertices, in exactly one nonempty
    component. Return an empty list for an empty vertex set. Component order is
    irrelevant. Do not mutate inputs or consult RECORDS or its identity labels.

    Initial scope: small graphs and standard-library Python. Input validation,
    production safeguards, and performance optimization are deferred.
    """
    # Learner task: implement after recording predictions and proof attempts.
    raise NotImplementedError("Implement connected_components for Lab 1.")
