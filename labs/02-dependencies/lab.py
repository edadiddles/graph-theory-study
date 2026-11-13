"""Synthetic package dependencies and unfinished learner tasks for Lab 2.

An edge (left, right) means left directly depends on right. Importing this module
does not run experiments or print results.
"""

VERTICES = ("api", "worker", "store", "shared", "cli", "report", "monitor", "sandbox")

SCENARIOS = {
    "scenario_1": (
        ("api", "worker"),
        ("api", "store"),
        ("worker", "shared"),
        ("store", "shared"),
        ("cli", "api"),
        ("report", "store"),
    ),
    "scenario_2": (
        ("api", "worker"),
        ("worker", "store"),
        ("store", "api"),
        ("store", "shared"),
        ("cli", "api"),
        ("report", "store"),
    ),
    "scenario_3": (
        ("api", "worker"),
        ("worker", "api"),
        ("worker", "store"),
        ("store", "shared"),
        ("shared", "store"),
        ("cli", "api"),
        ("report", "shared"),
    ),
    "scenario_4": (
        ("worker", "api"),
        ("store", "api"),
        ("shared", "worker"),
        ("shared", "store"),
        ("api", "cli"),
        ("store", "report"),
    ),
    "scenario_5": (),
}


def reachable_vertices(
    vertices: tuple[str, ...], edges: tuple[tuple[str, str], ...], start: str
) -> set[str]:
    """Return every vertex reachable from start by following directed edges.

    Include start via a path of length zero. Raise ValueError if start is not in
    vertices, including when vertices is empty. An isolated start returns {start}.

    Vertices are unique strings. Each edge has two distinct endpoints in vertices;
    no ordered edge occurs twice. Opposite edges are permitted. Apart from an
    unknown start, invalid inputs are outside this initial contract.

    Do not mutate inputs, consult global scenario data, or use third-party
    packages. Graphs are small; correctness and termination take priority over
    optimization. Write your own implementation after making predictions.
    """
    raise NotImplementedError("Implement reachable_vertices for Lab 2.")


def strongly_connected_components(
    vertices: tuple[str, ...], edges: tuple[tuple[str, str], ...]
) -> list[set[str]]:
    """Return the maximal groups of mutually reachable vertices.

    Return a list of nonempty sets that partitions all supplied vertices. Include
    isolated vertices; component order is irrelevant. An empty graph returns [].

    The valid-graph assumptions match reachable_vertices. Do not mutate inputs
    or consult global scenario data. Standard-library Python only. No particular
    algorithm or performance bound is prescribed for these small examples.

    Decide whether reuse of your own reachability function helps your argument
    and implementation; this scaffold does not prescribe a decomposition.
    """
    raise NotImplementedError("Implement strongly_connected_components for Lab 2.")
