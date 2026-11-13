"""Separate hand-checkable candidates, without a decomposition solver."""

import unittest

from lab import EDGES, SCENARIOS, VERTICES, decomposition_width, is_tree_decomposition


CASES = (
    ("empty_graph", (), (), {"A": frozenset()}, (), True),
    ("one_vertex", ("p",), (), {"A": frozenset(("p",))}, (), True),
    ("path", ("p", "q", "r", "u"), (("p", "q"), ("q", "r"), ("r", "u")),
     {"A": frozenset(("p", "q")), "B": frozenset(("q", "r")), "C": frozenset(("r", "u"))},
     (("A", "B"), ("B", "C")), True),
    ("single_full_bag", ("p", "q", "r"), (("p", "q"), ("q", "r"), ("r", "p")),
     {"A": frozenset(("p", "q", "r"))}, (), True),
    ("missing_vertex", ("p", "q", "r"), (("p", "q"),),
     {"A": frozenset(("p", "q"))}, (), False),
    ("uncovered_edge", ("p", "q", "r"), (("p", "q"), ("q", "r")),
     {"A": frozenset(("p", "q")), "B": frozenset(("r",))}, (("A", "B"),), False),
    ("disconnected_occurrences", ("p", "q", "r"), (("p", "q"), ("q", "r")),
     {"A": frozenset(("p", "q")), "B": frozenset(("q", "r")), "C": frozenset(("p", "r"))},
     (("A", "B"), ("B", "C")), False),
    ("disconnected_bag_graph", ("p", "q"), (),
     {"A": frozenset(("p",)), "B": frozenset(("q",))}, (), False),
    ("cyclic_bag_graph", ("p", "q", "r"), (),
     {"A": frozenset(("p",)), "B": frozenset(("q",)), "C": frozenset(("r",))},
     (("A", "B"), ("B", "C"), ("C", "A")), False),
    ("unknown_graph_vertex", ("p",), (), {"A": frozenset(("p", "unknown"))}, (), False),
    ("unknown_bag", ("p",), (), {"A": frozenset(("p",))}, (("A", "missing"),), False),
    ("bag_self_loop", ("p",), (), {"A": frozenset(("p",))}, (("A", "A"),), False),
    ("repeated_tree_edge", ("p", "q"), (),
     {"A": frozenset(("p",)), "B": frozenset(("q",))}, (("A", "B"), ("B", "A")), False),
    ("empty_collection", (), (), {}, (), False),
    ("empty_leaf_bag", ("p",), (),
     {"A": frozenset(("p",)), "B": frozenset()}, (("A", "B"),), True),
)


class DecompositionTests(unittest.TestCase):
    def test_known_candidates(self):
        for name, vertices, edges, bags, tree_edges, expected in CASES:
            with self.subTest(case=name):
                self.assertIs(is_tree_decomposition(vertices, edges, bags, tree_edges), expected)

    def test_relabeling_and_bag_order(self):
        for index in (2, 6):
            name, vertices, edges, bags, tree_edges, expected = CASES[index]
            with self.subTest(case=name):
                names = {vertex: 'vertex_' + vertex for vertex in vertices}
                bag_names = {bag: 'bag_' + bag for bag in bags}
                renamed_bags = {
                    bag_names[bag]: frozenset(names[vertex] for vertex in members)
                    for bag, members in reversed(tuple(bags.items()))
                }
                renamed_edges = tuple((names[right], names[left]) for left, right in reversed(edges))
                renamed_tree = tuple((bag_names[right], bag_names[left]) for left, right in reversed(tree_edges))
                self.assertIs(is_tree_decomposition(
                    tuple(names[vertex] for vertex in reversed(vertices)), renamed_edges,
                    renamed_bags, renamed_tree,
                ), expected)

    def test_main_scenario_output_and_input_preservation(self):
        for name, case in SCENARIOS.items():
            with self.subTest(scenario=name):
                before = (VERTICES[:], EDGES[:], case['bags'].copy(), case['tree_edges'][:])
                result = is_tree_decomposition(VERTICES, EDGES, case['bags'], case['tree_edges'])
                self.assertIsInstance(result, bool)
                self.assertEqual((VERTICES, EDGES, case['bags'], case['tree_edges']), before)


class WidthTests(unittest.TestCase):
    def test_known_widths(self):
        cases = (
            ({"A": frozenset()}, -1),
            ({"A": frozenset(("p",))}, 0),
            ({"A": frozenset(("p", "q")), "B": frozenset(("q", "r"))}, 1),
            ({"A": frozenset(("p", "q", "r")), "B": frozenset(("p",))}, 2),
            ({"A": frozenset(), "B": frozenset(("p", "q"))}, 1),
        )
        for bags, expected in cases:
            with self.subTest(bags=bags):
                width = decomposition_width(bags)
                self.assertIsInstance(width, int)
                self.assertEqual(width, expected)

    def test_empty_collection(self):
        with self.assertRaises(ValueError):
            decomposition_width({})

    def test_names_and_order_irrelevant(self):
        self.assertEqual(decomposition_width({
            "last": frozenset(("z",)), "first": frozenset(("x", "y")),
        }), 1)


class InputPreservationTests(unittest.TestCase):
    def test_inputs_unchanged(self):
        vertices, edges = ("p", "q"), (("p", "q"),)
        bags, tree_edges = {"A": frozenset(("p", "q"))}, ()
        for function, arguments in (
            (is_tree_decomposition, (vertices, edges, bags, tree_edges)),
            (decomposition_width, (bags,)),
        ):
            with self.subTest(function=function.__name__):
                before = (vertices[:], edges[:], bags.copy(), tree_edges[:])
                function(*arguments)
                self.assertEqual((vertices, edges, bags, tree_edges), before)


if __name__ == "__main__":
    unittest.main()
