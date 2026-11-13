"""Unfinished heat-kernel and continuous-time-walk tasks. Requires NumPy.

Importing supplies fixtures and contracts, without running experiments.
"""

import numpy as np


SCENARIOS = {
    "scenario_1": {
        "vertices": ("a", "b", "c"),
        "edges": (("a", "b"), ("b", "c")), "weights": (1.0, 2.0),
        "initial": (1.0, 0.0, 0.0), "interior": ("b",),
    },
    "scenario_2": {
        "vertices": ("a", "b", "c", "d"),
        "edges": (("a", "b"), ("b", "c"), ("c", "a")),
        "weights": (1.0, 1.0, 1.0),
        "initial": (0.5, 0.0, 0.0, 0.5), "interior": ("a", "b"),
    },
    "scenario_3": {
        "vertices": ("a", "b", "c", "d", "e", "f"),
        "edges": (("a", "b"), ("b", "c"), ("c", "a"),
                  ("d", "e"), ("e", "f"), ("f", "d"), ("c", "d")),
        "weights": (1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.2),
        "initial": (1.0, 0.0, 0.0, 0.0, 0.0, 0.0),
        "interior": ("b", "c", "d", "e"),
    },
}

TIMES = (0.0, 0.1, 0.5, 2.0, 10.0)


def heat_kernel(operator: np.ndarray, time: float) -> np.ndarray:
    """Return exp(-time * operator), a new float64 array of the same shape.

    This is a MATRIX exponential, not an entrywise exponential. The input is a
    real finite symmetric positive-semidefinite graph operator (combinatorial,
    symmetric normalized, or homogeneous Dirichlet restriction). Its coordinate
    convention is chosen and documented by the caller. Evolution of a column
    state is H(t) @ state. Symmetry alone does not imply ordinary mass conservation.

    Raise ValueError for non-2D/nonsquare arrays or nonfinite/negative real time.
    Other operator properties above are preconditions; a general numerical PSD
    or symmetry validator is outside scope. Empty (0, 0) input gives (0, 0) output;
    time zero gives the identity, including on isolated vertices. Do not mutate
    inputs or consult fixtures. Use NumPy only. Target small well-scaled operators
    and moderate times; arbitrary precision and large sparse problems are deferred.
    """
    raise NotImplementedError("Implement heat_kernel for Lab 15.")


def continuous_time_transition(
    vertices: tuple[str, ...], edges: tuple[tuple[str, str], ...],
    weights: tuple[float, ...], time: float
) -> np.ndarray:
    """Return exp(time * (P - I)) as a new float64 (n, n) array in vertex order.

    P is the ordinary weighted random-walk transition: from a positive-degree
    vertex, choose a neighbor proportionally to edge weight. Isolates are
    absorbing (P_ii = 1). Probability distributions are ROW vectors, evolving by
    distribution @ T(t). Time is dimensionless at unit jump-attempt rate; it is
    not a physical diffusion time without a separate model. No laziness or edge
    weights as jump rates are introduced. T need not be symmetric.

    Graph inputs otherwise form a valid simple undirected graph: unique string
    IDs, known distinct endpoints, no duplicate undirected edges. Raise ValueError
    for weight-count mismatch, nonfinite/nonpositive real weights, or nonfinite/
    negative real time. Empty graph gives (0, 0); edgeless graph gives identity.
    Do not mutate inputs or consult fixtures. NumPy only; justify any reuse of
    earlier learner work and derive the relation to symmetric coordinates.
    """
    raise NotImplementedError("Implement continuous_time_transition for Lab 15.")
