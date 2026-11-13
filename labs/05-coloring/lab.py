"""Synthetic exam enrollments, manual drawing cases, and unfinished tasks.

Importing runs no experiments. Enrollment rows represent anonymous synthetic
students; no actual student information is used.
"""

EXAMS = ("algebra", "mechanics", "optics", "programming", "statistics", "writing")

SCENARIOS = {
    "scenario_1": (("algebra",), ("mechanics",), ("writing",)),
    "scenario_2": (
        ("algebra", "mechanics"), ("mechanics", "optics"),
        ("optics", "programming"), ("programming", "statistics"), ("writing",),
    ),
    "scenario_3": (
        ("algebra", "mechanics", "optics"), ("programming", "statistics"),
        ("algebra", "mechanics"), ("writing",),
    ),
    "scenario_4": (
        ("algebra", "mechanics"), ("mechanics", "optics"),
        ("optics", "programming"), ("programming", "statistics"),
        ("statistics", "algebra"), ("writing",),
    ),
    "scenario_5": (
        ("algebra", "mechanics", "optics", "programming", "statistics", "writing"),
    ),
}

# Coordinates describe proposed straight-line drawings for manual investigation,
# not certified plane embeddings. Case names intentionally give no conclusions.
PLANARITY_CASES = {
    "case_1": {
        "vertices": ("p", "q", "r", "u"),
        "edges": (("p", "q"), ("q", "r"), ("r", "u"), ("u", "p")),
        "drawings": (
            {"p": (0, 0), "q": (2, 0), "r": (2, 2), "u": (0, 2)},
            {"p": (0, 0), "q": (2, 2), "r": (0, 2), "u": (2, 0)},
        ),
    },
    "case_2": {
        "vertices": ("p", "q", "r", "x", "y", "z"),
        "edges": (
            ("p", "x"), ("p", "y"), ("p", "z"),
            ("q", "x"), ("q", "y"), ("q", "z"),
            ("r", "x"), ("r", "y"), ("r", "z"),
        ),
        "drawings": (
            {"p": (0, 4), "q": (0, 1), "r": (0, 0),
             "x": (4, 5), "y": (4, 2), "z": (4, -1)},
        ),
    },
    "case_3": {
        "vertices": ("p", "q", "r", "u", "v"),
        "edges": (
            ("p", "q"), ("p", "r"), ("p", "u"), ("p", "v"),
            ("q", "r"), ("q", "u"), ("q", "v"),
            ("r", "u"), ("r", "v"), ("u", "v"),
        ),
        "drawings": (
            {"p": (0, 3), "q": (3, 1), "r": (2, -2),
             "u": (-2, -2), "v": (-3, 1)},
        ),
    },
}


def build_conflict_edges(
    exams: tuple[str, ...], enrollments: tuple[tuple[str, ...], ...]
) -> set[tuple[str, str]]:
    """Return exactly the pairs of exams sharing at least one enrolled student.

    Each enrollment row lists one student's exams. Exams are unique strings;
    each row contains only known exams, without repeats. Rows may be empty or
    repeated across students. Other malformed inputs are outside this contract.

    Represent an undirected edge as a two-item tuple in increasing lexical order.
    Do not include self-loops or duplicate edges. Exams without conflicts remain
    in the separate exams inventory; no vertices are inferred from edges alone.

    Do not mutate inputs or consult globals. Use standard-library Python and
    implement only after making your own predictions. Empty inputs return set().
    """
    raise NotImplementedError("Implement build_conflict_edges for Lab 5.")


def minimum_coloring(
    vertices: tuple[str, ...], edges: tuple[tuple[str, str], ...]
) -> dict[str, int]:
    """Return a proper vertex coloring with the fewest distinct colors.

    Map every supplied vertex, including isolates, to an integer color label.
    Adjacent vertices must receive different colors. Any minimum coloring and
    any integer label names are acceptable. Empty vertices return {}.

    Inputs form a valid simple undirected graph: unique string IDs, known distinct
    endpoints, and no duplicate undirected edges. Endpoint order is irrelevant.
    Invalid inputs are deferred. Do not mutate inputs or consult global scenarios.

    Standard-library Python only. Graphs are tiny; no particular algorithm is
    prescribed. Prove optimality for your approach, not merely proper coloring.
    """
    raise NotImplementedError("Implement minimum_coloring for Lab 5.")
