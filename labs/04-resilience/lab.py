"""Synthetic station networks and unfinished separator tasks.

Edges are undirected bidirectional connections. Importing runs no experiments.
All scenarios use terminals s and t; spare is an explicitly isolated station.
"""

VERTICES = ("s", "a", "b", "c", "d", "e", "t", "spare")
SOURCE = "s"
TARGET = "t"

SCENARIOS = {
    "scenario_1": (("s", "a"), ("a", "b"), ("b", "t")),
    "scenario_2": (("s", "a"), ("a", "t"), ("s", "b"), ("b", "t")),
    "scenario_3": (
        ("s", "a"), ("s", "b"), ("a", "c"), ("b", "c"),
        ("c", "d"), ("c", "e"), ("d", "t"), ("e", "t"),
    ),
    "scenario_4": (("s", "a"), ("a", "b"), ("c", "d"), ("d", "t")),
    "scenario_5": (
        ("s", "a"), ("a", "t"), ("s", "b"), ("b", "t"),
        ("s", "c"), ("c", "t"),
    ),
}


def minimum_vertex_separator(
    vertices: tuple[str, ...], edges: tuple[tuple[str, str], ...], source: str, target: str
) -> set[str]:
    """Return any smallest vertex set whose deletion disconnects source and target.

    Exclude the terminals from the result. Deleting a vertex also deletes its
    incident edges. Initially disconnected terminals have separator set().

    Raise ValueError for unknown, identical, or adjacent terminals. The last
    restriction belongs to this function, not minimum_edge_separator.

    Graph inputs are valid: vertices are unique strings, edges have distinct
    known endpoints, and there are no duplicate undirected edges. Inputs may be
    empty, in which case terminals are unknown and the request raises ValueError.

    Return a set, do not mutate inputs or consult global scenarios, and use only
    standard-library Python. Choose an approach suitable for these tiny graphs.
    No algorithm or performance bound is prescribed. Broader validation is deferred.
    """
    raise NotImplementedError("Implement minimum_vertex_separator for Lab 4.")


def minimum_edge_separator(
    vertices: tuple[str, ...], edges: tuple[tuple[str, str], ...], source: str, target: str
) -> set[tuple[str, str]]:
    """Return any smallest edge set whose deletion disconnects source and target.

    Each returned pair represents an edge from the input graph. Either endpoint
    order is acceptable because edges are undirected. Never return both orders
    of the same edge. Initially disconnected terminals have separator set().

    Raise ValueError for unknown or identical terminals. Adjacent distinct
    terminals are permitted. Valid-graph assumptions match the vertex task.

    Do not mutate inputs or consult global scenarios. Standard-library Python
    only, with no prescribed algorithm or performance bound for these tiny graphs.
    """
    raise NotImplementedError("Implement minimum_edge_separator for Lab 4.")
