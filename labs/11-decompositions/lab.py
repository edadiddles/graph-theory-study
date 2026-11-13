"""Small constraint-interaction graphs and unfinished decomposition tasks.

Vertices represent variables; edges represent pairwise interactions, not complete
constraint semantics. Importing performs no experiments.
"""

VERTICES = ("a", "b", "c", "d", "e")
EDGES = (("a", "b"), ("b", "c"), ("c", "d"), ("d", "e"))

SCENARIOS = {
    "scenario_1": {
        "bags": {"b0": frozenset(VERTICES)},
        "tree_edges": (),
    },
    "scenario_2": {
        "bags": {"b0": frozenset(("a", "b")), "b1": frozenset(("b", "c")),
                 "b2": frozenset(("c", "d")), "b3": frozenset(("d", "e"))},
        "tree_edges": (("b0", "b1"), ("b1", "b2"), ("b2", "b3")),
    },
    "scenario_3": {
        "bags": {"b0": frozenset(("a", "b")), "b1": frozenset(("b", "c")),
                 "b2": frozenset(("c", "d")), "b3": frozenset(("d", "e"))},
        "tree_edges": (("b0", "b1"), ("b1", "b2"), ("b2", "b3"), ("b3", "b0")),
    },
    "scenario_4": {
        "bags": {"b0": frozenset(("a", "b", "c")), "b1": frozenset(("c", "d")),
                 "b2": frozenset(("a", "d", "e"))},
        "tree_edges": (("b0", "b1"), ("b1", "b2")),
    },
    "scenario_5": {
        "bags": {"b0": frozenset(("a", "b")), "b1": frozenset(("b", "c")),
                 "b2": frozenset(("d", "e"))},
        "tree_edges": (("b0", "b1"), ("b1", "b2")),
    },
}


def is_tree_decomposition(
    vertices: tuple[str, ...], edges: tuple[tuple[str, str], ...],
    bags: dict[str, frozenset[str]], tree_edges: tuple[tuple[str, str], ...]
) -> bool:
    """Return whether a candidate is a tree decomposition of the supplied graph.

    The graph is valid and simple: unique string vertices, distinct known edge
    endpoints, and no duplicate undirected graph edges. Candidate containers have
    the stated shapes; general malformed-type handling is outside this contract.

    Bag IDs are dictionary keys, independent of graph vertex IDs. Bag contents
    must be graph vertices; every vertex is covered and every graph edge has
    both endpoints together in some bag. Bags may be empty. The bag graph must
    be a nonempty simple tree, with exactly the bag IDs as its vertex inventory.
    For each graph vertex, the bag nodes containing it must induce a connected
    subtree. Endpoint orientation in either graph is irrelevant.

    Return False for structural violations, including unknown references,
    missing coverage, self-loops or repeated undirected tree edges, a cyclic or
    disconnected bag graph, and an empty bag collection. The empty graph may
    have one empty bag and no tree edges, which is valid under this convention.

    Do not mutate inputs or consult global scenarios. Standard-library Python
    only; choose and justify your own checks rather than assuming optimality.
    """
    raise NotImplementedError("Implement is_tree_decomposition for Lab 11.")


def decomposition_width(bags: dict[str, frozenset[str]]) -> int:
    """Return largest bag size minus one for a nonempty bag collection.

    Raise ValueError for an empty collection. One empty bag has width -1. Bag
    names and insertion order are irrelevant. Input shapes are valid; do not
    mutate the mapping or consult globals. Standard-library Python only.

    This computes a bag collection's width, not whether it is a valid decomposition
    or whether its width is minimum for a graph. Establish validity separately.
    """
    raise NotImplementedError("Implement decomposition_width for Lab 11.")
