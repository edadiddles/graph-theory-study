"""Neutral finite examples and unfinished witness-search tasks.

Importing performs no experiments. No Ramsey threshold or search solver is given.
"""

RAMSEY_VERTICES = ("j", "k", "m", "n")
RAMSEY_SCENARIOS = {
    "scenario_1": {
        ("j", "k"): "red", ("j", "m"): "red", ("j", "n"): "red",
        ("k", "m"): "red", ("k", "n"): "red", ("m", "n"): "red",
    },
    "scenario_2": {
        ("j", "k"): "red", ("j", "m"): "red", ("j", "n"): "red",
        ("k", "m"): "blue", ("k", "n"): "blue", ("m", "n"): "blue",
    },
    "scenario_3": {
        ("j", "k"): "red", ("j", "m"): "blue", ("j", "n"): "red",
        ("k", "m"): "red", ("k", "n"): "blue", ("m", "n"): "red",
    },
    "scenario_4": {
        ("j", "k"): "red", ("j", "m"): "blue", ("j", "n"): "blue",
        ("k", "m"): "red", ("k", "n"): "blue", ("m", "n"): "red",
    },
    "scenario_5": {
        ("j", "k"): "red", ("j", "m"): "red", ("j", "n"): "blue",
        ("k", "m"): "red", ("k", "n"): "blue", ("m", "n"): "blue",
    },
}

ROUTE_VERTICES = ("depot", "a", "b", "c", "d", "e")
ROUTE_SCENARIOS = {
    "scenario_1": (
        ("depot", "a"), ("a", "b"), ("b", "c"),
        ("c", "d"), ("d", "e"), ("e", "depot"),
    ),
    "scenario_2": (
        ("depot", "a"), ("a", "b"), ("b", "c"), ("c", "d"), ("d", "e"),
    ),
    "scenario_3": (
        ("depot", "a"), ("a", "b"), ("b", "depot"),
        ("b", "c"), ("c", "d"), ("d", "e"), ("e", "c"),
    ),
    "scenario_4": (
        ("depot", "c"), ("depot", "d"), ("depot", "e"),
        ("a", "c"), ("a", "d"), ("a", "e"),
        ("b", "c"), ("b", "d"), ("b", "e"),
    ),
    "scenario_5": (
        ("depot", "a"), ("depot", "b"), ("depot", "c"),
        ("depot", "d"), ("depot", "e"),
    ),
}


def monochromatic_triangle(
    vertices: tuple[str, ...], edge_colors: dict[tuple[str, str], str]
) -> tuple[str, str, str] | None:
    """Return any monochromatic triangle witness, or None if none exists.

    Inputs are a complete simple undirected graph with unique string vertex IDs.
    Each unordered pair has exactly one key in edge_colors, in increasing lexical
    endpoint order. Each color is either "red" or "blue". Malformed inputs are
    outside this initial contract.

    A witness is a tuple of three distinct supplied vertices whose three pairwise
    edges all have the same color. Any vertex order or valid witness is accepted.
    Fewer than three vertices return None. This examines a supplied coloring; it
    does not decide a universal Ramsey statement or compute a Ramsey number.

    Standard-library Python only. Do not mutate inputs or consult global scenarios.
    Choose your own approach and justify any claim that a search is complete.
    """
    raise NotImplementedError("Implement monochromatic_triangle for Lab 9.")


def hamiltonian_cycle(
    vertices: tuple[str, ...], edges: tuple[tuple[str, str], ...]
) -> tuple[str, ...] | None:
    """Return any Hamilton cycle witness, or None if none exists.

    Return each supplied vertex exactly once as a tuple; do not repeat the first
    vertex at the end. Successive entries and the implied closing pair must be
    edges. Any start, traversal direction, or valid cycle is accepted. Simple
    cycles have at least three vertices, so smaller inventories return None.

    Inputs form a valid simple undirected graph: unique string vertices, known
    distinct endpoints, and no duplicate undirected edges. Endpoint orientation
    is irrelevant. Invalid inputs are deferred. No costs or shortest-tour objective
    are present. Inputs are small; no particular algorithm is prescribed.

    Standard-library Python only. Do not mutate inputs or consult global scenarios.
    Distinguish a valid witness from a justified absence claim.
    """
    raise NotImplementedError("Implement hamiltonian_cycle for Lab 9.")
