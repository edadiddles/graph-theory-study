"""Family specifications, finite experiments, and unfinished learner tasks.

No infinite graph is materialized. Importing runs no experiments.
"""

FAMILIES = ("ray", "double_ray", "binary_tree")
RADII = (0, 1, 2, 3, 4)
ROOTS = {"ray": "0", "double_ray": "0", "binary_tree": ""}

SCENARIOS = {
    "scenario_1": {"family": "ray", "radius": 4, "removed": ("1",)},
    "scenario_2": {"family": "double_ray", "radius": 4, "removed": ("0",)},
    "scenario_3": {"family": "binary_tree", "radius": 4, "removed": ("",)},
    "scenario_4": {"family": "binary_tree", "radius": 4, "removed": ("0", "1")},
    "scenario_5": {"family": "ray", "radius": 0, "removed": ("0",)},
}


def truncate_graph(family: str, radius: int) -> tuple[tuple[str, ...], set[tuple[str, str]]]:
    """Return the finite induced ball around the specified infinite graph's root.

    Family definitions and labels:
    - ray: nonnegative integers, adjacent when they differ by one; root 0.
    - double_ray: all integers, adjacent when they differ by one; root 0.
    - binary_tree: finite binary words, adjacent when one appends one bit to the
      other; root is the empty word.

    Path vertices use their integer's decimal string; binary-tree vertices use
    their binary word, including "". Include exactly vertices at graph distance
    at most radius and every family edge between included vertices.

    Return a tuple of unique vertex IDs (any order) and a set of edge tuples,
    each in increasing lexical order. The root exists even at radius zero.
    Radius zero is not an empty graph.

    Raise ValueError for an unknown family or negative integer radius. Initial
    experiments use integer radii zero through four; larger radii and malformed
    noninteger inputs are outside this iteration. Standard-library Python only;
    no prescribed algorithm. Do not mutate supplied data or consult SCENARIOS.
    """
    raise NotImplementedError("Implement truncate_graph for Lab 8.")


def component_sizes_after_deletion(
    vertices: tuple[str, ...], edges: tuple[tuple[str, str], ...], removed: tuple[str, ...]
) -> tuple[int, ...]:
    """Return component sizes of the finite graph after deleting removed vertices.

    Delete incident edges as well. Return positive integer sizes sorted in
    nondecreasing order; include isolated surviving vertices as components.
    An empty graph or deletion of every vertex returns (). Empty deletion is valid.

    Inputs are valid: unique string vertices, known distinct edge endpoints, no
    duplicate undirected edges, and unique removed IDs drawn from vertices.
    Endpoint order is irrelevant. Unknown removed vertices and other malformed
    graph inputs are outside this initial contract.

    Do not mutate inputs or consult global scenarios. Use standard-library Python
    and justify any reuse of your own earlier graph functions. This function
    reports finite component sizes, not infinite components or graph ends.
    """
    raise NotImplementedError("Implement component_sizes_after_deletion for Lab 8.")
