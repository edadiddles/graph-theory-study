"""Small graphs, construction orders, and unfinished extremal tasks.

Importing performs no experiments. Neutral scenario names supply no conclusions.
"""

VERTICES = ("p", "q", "r", "u", "v")

SCENARIOS = {
    "scenario_1": (("p", "q"), ("q", "r"), ("r", "u"), ("u", "v")),
    "scenario_2": (("p", "q"), ("q", "r"), ("r", "p"), ("r", "u"), ("u", "v")),
    "scenario_3": (
        ("p", "r"), ("p", "u"), ("p", "v"),
        ("q", "r"), ("q", "u"), ("q", "v"),
    ),
    "scenario_4": (("p", "q"), ("q", "r"), ("r", "u"), ("u", "v"), ("v", "p")),
    "scenario_5": (
        ("p", "q"), ("p", "r"), ("p", "u"),
        ("q", "r"), ("q", "u"), ("r", "u"),
    ),
}

VERTEX_SETS = ((), ("p",), ("p", "q"), ("p", "q", "r"),
               ("p", "q", "r", "u"), VERTICES)


def contains_triangle(vertices: tuple[str, ...], edges: tuple[tuple[str, str], ...]) -> bool:
    """Return whether the simple undirected graph contains a triangle subgraph.

    A triangle has three distinct vertices joined pairwise by edges. Extra edges
    elsewhere do not invalidate a triangle. Return a bool, including for empty
    graphs and graphs with isolated vertices.

    Inputs are valid: unique string vertex IDs, distinct known edge endpoints,
    and no duplicate undirected edges. Endpoint order is irrelevant. Do not mutate
    inputs or consult global scenarios. Use standard-library Python; choose your
    own approach. Broader validation is deferred.
    """
    raise NotImplementedError("Implement contains_triangle for Lab 7.")


def maximum_triangle_free_graph(vertices: tuple[str, ...]) -> set[tuple[str, str]]:
    """Return the edges of any maximum-size triangle-free graph on vertices.

    Inputs are unique string IDs, with at most five vertices in this iteration.
    Return a set of undirected edge tuples, each in increasing lexical order,
    with known distinct endpoints and no duplicates. The full vertex inventory
    remains the supplied vertices, even when some have no incident edge.

    Every possible simple edge is eligible; no input candidate graph restricts
    the construction. Maximize edge count subject to triangle avoidance. Any
    optimal construction is accepted. Empty or singleton inventories return set().

    Do not mutate inputs or consult globals. Standard-library Python only, with
    no prescribed algorithm. If reusing your triangle detector, justify that
    dependency and validate the detector separately. Larger orders and malformed
    inputs are outside this initial contract.
    """
    raise NotImplementedError("Implement maximum_triangle_free_graph for Lab 7.")
