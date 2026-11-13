"""Local dataset location and unfinished random-graph learner tasks.

Importing neither loads data nor generates graphs. NetworkX is not a dependency.
"""

from pathlib import Path
from random import Random


DATA_PATH = Path(__file__).parent / "data" / "karate_club.json"


def sample_gnp(
    vertices: tuple[str, ...], probability: float, rng: Random
) -> set[tuple[str, str]]:
    """Sample a simple undirected independent-edge graph on the given inventory.

    Include each unordered pair independently with the supplied probability.
    Return a set of edge tuples in increasing lexical endpoint order. Do not
    infer the vertex inventory from edges: isolates remain in vertices.

    Use only the supplied rng for randomness. For 0 < probability < 1, use one
    rng.random() uniform draw per unordered pair, retaining it when below the
    probability. Pair iteration order is your choice but must be deterministic
    for identical ordered inputs. At probability zero/one the edge set is
    empty/complete; advancing rng in those boundary cases is not required.

    Raise ValueError for nonfinite probabilities or values outside [0, 1].
    Other inputs are valid: unique string vertex IDs and a compatible generator.
    Empty or singleton inventories produce no edges. Do not mutate vertices,
    use global random state, reseed rng, or consult the observed dataset. The
    supplied generator may advance; fresh equal seeds reproduce equal inputs.

    Standard-library Python only; larger model families and broader validation
    are deferred. Explain why the model's independence assumptions fit your code.
    """
    raise NotImplementedError("Implement sample_gnp for Lab 10.")


def graph_summary(
    vertices: tuple[str, ...], edges: tuple[tuple[str, str], ...]
) -> dict[str, int]:
    """Return edge_count, triangle_count, and largest_component_size.

    Count each unordered triangle once, regardless of vertex/edge order. Include
    isolates when determining components. For an empty inventory all counts
    are zero; a nonempty edgeless graph has largest component size one.

    Inputs are a valid simple undirected graph: unique string vertex IDs, known
    distinct endpoints, and no duplicate undirected edges. Endpoint orientation
    is irrelevant. Return exactly the three named keys with integer counts.

    Do not mutate inputs or consult the dataset or global random state. Use
    standard-library Python and justify any reuse of your own earlier functions.
    These are structural statistics, not evidence of identity or causality.
    """
    raise NotImplementedError("Implement graph_summary for Lab 10.")
