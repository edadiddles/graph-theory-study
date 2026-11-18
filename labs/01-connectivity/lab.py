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
    components = []
    # iterate over edges to find and merge components
    for edge in edges:
        edge_a, edge_b = edge
        # initialize component sets to include only the verticies of each edge
        component_a, component_b = set({edge_a}), set({edge_b})
        idx_a, idx_b = -1, -1
        # iterate over component index
        # found components will be stored as a reference
        for idx in range(len(components)):
            # is the left vertex of the edge in a component
            if edge_a in components[idx]:
                idx_a = idx
                component_a = components[idx]
            # is the right vertex of the edge in a component
            if edge_b in components[idx]:
                idx_b = idx
                component_b = components[idx]
        # if the right vertex is in a component remove it from the comonent list
        if idx_b > -1 and idx_a != idx_b:
            components.pop(idx_b)

        # union both edge components
        component_a |= component_b

        # if the left vertex is not a known component add it
        if idx_a == -1:
            components.append(component_a)

    for vertex in vertices:
        if not any(vertex in component for component in components):
            components.append({vertex})
    return components
