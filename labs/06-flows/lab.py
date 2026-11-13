"""Synthetic distribution networks and unfinished learner tasks.

Capacities are integer batches per hour on distinct directed connections.
Importing runs no experiments and prints no results.
"""

VERTICES = ("source", "a", "b", "c", "sink", "unused")
SOURCE = "source"
SINK = "sink"

SCENARIOS = {
    "scenario_1": {
        ("source", "a"): 4, ("a", "sink"): 3,
        ("source", "b"): 2, ("b", "sink"): 2,
        ("a", "c"): 1, ("c", "sink"): 1,
    },
    "scenario_2": {
        ("source", "a"): 7, ("source", "b"): 5,
        ("a", "c"): 3, ("b", "c"): 4, ("c", "sink"): 4,
    },
    "scenario_3": {
        ("source", "a"): 3, ("source", "b"): 2,
        ("a", "b"): 2, ("b", "a"): 1,
        ("a", "sink"): 2, ("b", "sink"): 3,
        ("sink", "c"): 1, ("c", "source"): 1,
    },
    "scenario_4": {("source", "a"): 4, ("b", "sink"): 6},
    "scenario_5": {
        ("source", "a"): 0, ("a", "sink"): 5,
        ("source", "b"): 3, ("b", "sink"): 0,
    },
}


def maximum_flow(
    vertices: tuple[str, ...], capacities: dict[tuple[str, str], int], source: str, sink: str
) -> dict[tuple[str, str], int]:
    """Return any maximum feasible integer flow, including every supplied arc.

    Return a dictionary with exactly the same keys as capacities, including arcs
    with zero flow or capacity. Values are nonnegative integers at most capacity.
    At each vertex other than source and sink, total inflow equals total outflow.

    Flow value is source outflow minus source inflow. Source incoming arcs and
    sink outgoing arcs are allowed. Opposite arcs are distinct, with independent
    nonnegative flow values. Feasible circulations may be present in an optimum;
    no particular optimal representative is required. No route gives value zero.

    Raise ValueError for unknown or identical terminals, including empty vertices.
    Otherwise inputs are valid: unique string vertices, known distinct endpoints,
    and finite nonnegative integer capacities on a simple directed graph.

    Do not mutate inputs or consult global scenarios. Use standard-library Python
    on these tiny graphs. Choose an approach you can justify; no algorithm or
    performance bound is prescribed. Broader input validation is deferred.
    """
    raise NotImplementedError("Implement maximum_flow for Lab 6.")


def minimum_cut(
    vertices: tuple[str, ...], capacities: dict[tuple[str, str], int], source: str, sink: str
) -> set[str]:
    """Return the source-side vertex set of any minimum directed cut.

    Include source, exclude sink, and include only supplied vertices. Cut capacity
    is the sum of original capacities on arcs directed from this set to its
    complement. Reverse crossing arcs do not contribute to that sum. Zero-capacity
    cuts are allowed, and isolated vertices need not have a prescribed side.

    Raise ValueError for unknown or identical terminals. Valid-input assumptions
    match maximum_flow. Do not mutate inputs or consult global scenarios.
    Standard-library Python only; no algorithm or tie-breaking rule is prescribed.
    """
    raise NotImplementedError("Implement minimum_cut for Lab 6.")
