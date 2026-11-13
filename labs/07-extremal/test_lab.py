"""Separate tiny examples and counts; attempt predictions before reading.

No general extremal formula, reference detector, or construction solver is given.
"""

import unittest

from lab import SCENARIOS, VERTICES, contains_triangle, maximum_triangle_free_graph


TRIANGLE_CASES = (
    ("empty", (), (), False),
    ("isolates", ("a", "b", "c"), (), False),
    ("single_edge", ("a", "b"), (("b", "a"),), False),
    ("path", ("a", "b", "c"), (("a", "b"), ("b", "c")), False),
    ("triangle", ("a", "b", "c"), (("a", "b"), ("b", "c"), ("c", "a")), True),
    ("four_cycle", ("a", "b", "c", "d"),
     (("a", "b"), ("b", "c"), ("c", "d"), ("d", "a")), False),
    ("triangle_and_tail", ("a", "b", "c", "d"),
     (("a", "b"), ("b", "c"), ("c", "a"), ("c", "d")), True),
    ("separate_triangle", ("a", "b", "c", "d", "e"),
     (("a", "b"), ("c", "d"), ("d", "e"), ("e", "c")), True),
)


class TriangleTests(unittest.TestCase):
    def test_known_graphs(self):
        for name, vertices, edges, expected in TRIANGLE_CASES:
            with self.subTest(case=name):
                self.assertIs(contains_triangle(vertices, edges), expected)

    def test_relabeling_and_edge_order(self):
        cases = (
            ((("a", "b"), ("b", "c")), False),
            ((("a", "b"), ("b", "c"), ("c", "a")), True),
        )
        names = {"a": "z", "b": "x", "c": "y"}
        for edges, expected in cases:
            with self.subTest(edges=edges):
                renamed = tuple((names[right], names[left]) for left, right in reversed(edges))
                self.assertIs(contains_triangle(("y", "z", "x"), renamed), expected)

    def test_main_scenario_output_type(self):
        for name, edges in SCENARIOS.items():
            with self.subTest(scenario=name):
                self.assertIsInstance(contains_triangle(VERTICES, edges), bool)


class ExtremalConstructionTests(unittest.TestCase):
    def test_small_hand_checkable_orders(self):
        # Individual finite cases, not a supplied general formula or construction.
        cases = (((), 0), (("a",), 0), (("a", "b"), 1),
                 (("a", "b", "c"), 2), (("a", "b", "c", "d"), 4),
                 (("a", "b", "c", "d", "e"), 6))
        for vertices, optimum in cases:
            with self.subTest(order=len(vertices)):
                result = maximum_triangle_free_graph(vertices)
                self.assertIsInstance(result, set)
                self.assertEqual(len(result), optimum)
                for edge in result:
                    self.assertIsInstance(edge, tuple)
                    self.assertEqual(len(edge), 2)
                    left, right = edge
                    self.assertIn(left, vertices)
                    self.assertIn(right, vertices)
                    self.assertLess(left, right)
                self.assertIs(contains_triangle(vertices, tuple(result)), False)

    def test_relabeling_and_vertex_order(self):
        for vertices in (("z", "b", "y", "a", "x"), ("r5", "r4", "r3", "r2", "r1")):
            with self.subTest(vertices=vertices):
                result = maximum_triangle_free_graph(vertices)
                self.assertEqual(len(result), 6)
                for left, right in result:
                    self.assertIn(left, vertices)
                    self.assertIn(right, vertices)
                    self.assertLess(left, right)
                self.assertIs(contains_triangle(vertices, tuple(result)), False)


class InputPreservationTests(unittest.TestCase):
    def test_inputs_unchanged(self):
        vertices = ("a", "b", "c")
        edges = (("a", "b"), ("b", "c"))
        for function, arguments in (
            (contains_triangle, (vertices, edges)),
            (maximum_triangle_free_graph, (vertices,)),
        ):
            with self.subTest(function=function.__name__):
                before = (vertices[:], edges[:])
                function(*arguments)
                self.assertEqual((vertices, edges), before)


if __name__ == "__main__":
    unittest.main()
