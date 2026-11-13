"""Finite behavioral checks, not proofs of properties of infinite graphs."""

import unittest

from lab import (
    FAMILIES, ROOTS, SCENARIOS,
    component_sizes_after_deletion, truncate_graph,
)


class TruncationTests(unittest.TestCase):
    def test_radius_zero(self):
        for family in FAMILIES:
            with self.subTest(family=family):
                vertices, edges = truncate_graph(family, 0)
                self.assertEqual(set(vertices), {ROOTS[family]})
                self.assertEqual(len(vertices), 1)
                self.assertEqual(edges, set())

    def test_small_known_neighborhoods(self):
        cases = (
            ("ray", 2, {"0", "1", "2"}, {("0", "1"), ("1", "2")}),
            ("double_ray", 1, {"-1", "0", "1"}, {("-1", "0"), ("0", "1")}),
            ("binary_tree", 1, {"", "0", "1"}, {("", "0"), ("", "1")}),
        )
        for family, radius, expected_vertices, expected_edges in cases:
            with self.subTest(family=family, radius=radius):
                vertices, edges = truncate_graph(family, radius)
                self.assertEqual(set(vertices), expected_vertices)
                self.assertEqual(len(vertices), len(expected_vertices))
                self.assertEqual(edges, expected_edges)

    def test_nested_induced_neighborhoods(self):
        for family in FAMILIES:
            for radius in range(4):
                with self.subTest(family=family, radius=radius):
                    inner_vertices, inner_edges = truncate_graph(family, radius)
                    outer_vertices, outer_edges = truncate_graph(family, radius + 1)
                    self.assertTrue(set(inner_vertices) <= set(outer_vertices))
                    self.assertTrue(inner_edges <= outer_edges)
                    restricted = {
                        (left, right) for left, right in outer_edges
                        if left in inner_vertices and right in inner_vertices
                    }
                    self.assertEqual(inner_edges, restricted)

    def test_output_contract_at_largest_experimental_radius(self):
        for family in FAMILIES:
            with self.subTest(family=family):
                vertices, edges = truncate_graph(family, 4)
                self.assertIsInstance(vertices, tuple)
                self.assertEqual(len(vertices), len(set(vertices)))
                self.assertIn(ROOTS[family], vertices)
                self.assertIsInstance(edges, set)
                for vertex in vertices:
                    self.assertIsInstance(vertex, str)
                for edge in edges:
                    self.assertIsInstance(edge, tuple)
                    self.assertEqual(len(edge), 2)
                    left, right = edge
                    self.assertIn(left, vertices)
                    self.assertIn(right, vertices)
                    self.assertLess(left, right)

    def test_unknown_family_and_negative_radius(self):
        for family, radius in (("unknown", 0), ("ray", -1), ("double_ray", -1), ("binary_tree", -1)):
            with self.subTest(family=family, radius=radius):
                with self.assertRaises(ValueError):
                    truncate_graph(family, radius)


class FiniteDeletionTests(unittest.TestCase):
    def test_known_finite_components(self):
        cases = (
            ("empty", (), (), (), ()),
            ("isolates", ("a", "b", "c"), (), ("b",), (1, 1)),
            ("middle_deletion", ("a", "b", "c", "d", "e"),
             (("a", "b"), ("b", "c"), ("c", "d"), ("d", "e")), ("c",), (2, 2)),
            ("cycle_deletion", ("a", "b", "c", "d"),
             (("a", "b"), ("b", "c"), ("c", "d"), ("d", "a")), ("b",), (3,)),
            ("all_deleted", ("a", "b", "c"), (("a", "b"), ("b", "c")), ("a", "b", "c"), ()),
            ("endpoint_deletion", ("a", "b", "c"), (("a", "b"), ("b", "c")), ("a",), (2,)),
            ("no_deletion", ("a", "b", "c"), (("a", "b"),), (), (1, 2)),
        )
        for name, vertices, edges, removed, expected in cases:
            with self.subTest(case=name):
                self.assertEqual(component_sizes_after_deletion(vertices, edges, removed), expected)

    def test_relabeling_and_edge_order(self):
        result = component_sizes_after_deletion(
            ("y", "w", "z", "x"), (("x", "z"), ("z", "w"), ("w", "y")), ("z",)
        )
        self.assertEqual(result, (1, 2))

    def test_scenario_size_invariants(self):
        for name, case in SCENARIOS.items():
            with self.subTest(scenario=name):
                vertices, edges = truncate_graph(case['family'], case['radius'])
                sizes = component_sizes_after_deletion(vertices, tuple(edges), case['removed'])
                self.assertIsInstance(sizes, tuple)
                self.assertEqual(sizes, tuple(sorted(sizes)))
                for size in sizes:
                    self.assertIsInstance(size, int)
                    self.assertGreater(size, 0)
                self.assertEqual(sum(sizes), len(set(vertices) - set(case['removed'])))


class InputPreservationTests(unittest.TestCase):
    def test_inputs_unchanged(self):
        vertices, edges, removed = ("a", "b", "c"), (("a", "b"),), ("c",)
        for function, arguments in (
            (truncate_graph, ("ray", 2)),
            (component_sizes_after_deletion, (vertices, edges, removed)),
        ):
            with self.subTest(function=function.__name__):
                before = (vertices[:], edges[:], removed[:])
                function(*arguments)
                self.assertEqual((vertices, edges, removed), before)


if __name__ == "__main__":
    unittest.main()
