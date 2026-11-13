"""Weighted graph fixtures and unfinished matrix learner tasks.

Requires the project's NumPy dependency. Importing performs no experiments.
"""

import numpy as np


SCENARIOS = {
    "scenario_1": {
        "vertices": ("a", "b"), "edges": (("a", "b"),),
        "weights": (2.0,), "vector": (1.0, -1.0),
    },
    "scenario_2": {
        "vertices": ("a", "b", "c"), "edges": (("a", "b"), ("b", "c")),
        "weights": (1.0, 2.0), "vector": (-1.0, 0.0, 1.0),
    },
    "scenario_3": {
        "vertices": ("a", "b", "c"),
        "edges": (("a", "b"), ("b", "c"), ("c", "a")),
        "weights": (1.0, 1.0, 1.0), "vector": (1.0, 0.0, -1.0),
    },
    "scenario_4": {
        "vertices": ("a", "b", "c", "d"),
        "edges": (("a", "b"), ("b", "c"), ("c", "d"), ("d", "a")),
        "weights": (1.0, 2.0, 1.0, 2.0), "vector": (1.0, 0.0, -1.0, 0.0),
    },
    "scenario_5": {
        "vertices": ("a", "b", "c"), "edges": (("a", "b"),),
        "weights": (2.0,), "vector": (1.0, -1.0, 0.0),
    },
}


def graph_matrices(
    vertices: tuple[str, ...], edges: tuple[tuple[str, str], ...], weights: tuple[float, ...]
) -> dict[str, np.ndarray]:
    """Return floating NumPy arrays keyed B, A, D, and L under these conventions.

    Vertex order determines rows of incidence B and rows/columns of A, D, and L.
    Edge order determines B's columns and matches the weight tuple. For edge
    (tail, head), B has -1 at tail and +1 at head. B is unweighted and has shape
    (n, m); edge direction is a representation choice for this undirected graph.

    A is weighted symmetric adjacency with zero diagonal. D is diagonal weighted
    degree. L is the combinatorial weighted Laplacian D - A, not a normalized
    Laplacian. A, D, and L each have shape (n, n). Keep isolated vertices explicit.
    For no edges, B has shape (n, 0). All matrices for an empty graph have shape
    (0, 0). Return exactly these four keys and real float64 arrays.

    Raise ValueError if weight count differs from edge count or any real weight
    is nonfinite or not strictly positive. Otherwise graph inputs are valid:
    unique string vertices, known distinct endpoints, no duplicate undirected
    edges, and small numerically well-scaled examples. Broader validation is deferred.

    Do not mutate inputs or consult global scenarios. Use NumPy as approved;
    implement the assembly yourself after recording hand predictions.
    """
    raise NotImplementedError("Implement graph_matrices for Lab 12.")


def quadratic_form(laplacian: np.ndarray, vector: np.ndarray) -> float:
    """Return the real scalar x-transpose L x for the supplied matrix and vector.

    Raise ValueError unless laplacian is two-dimensional and square and vector
    is one-dimensional with matching length. Inputs are finite real NumPy arrays;
    graph-matrix validity and broader malformed-type handling are outside this
    function's scope. Empty compatible arrays return 0.0.

    Do not mutate either array or consult global scenarios. Return a Python
    float. Interpret physical units and any energy factors separately; this
    function does not solve a circuit or select boundary conditions.
    """
    raise NotImplementedError("Implement quadratic_form for Lab 12.")
