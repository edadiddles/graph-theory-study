"""Behavior checks; attempt the exercise predictions before reading these."""

import unittest

from lab import SCENARIOS, VERTICES, connected_components


class ConnectedComponentsTests(unittest.TestCase):
    def test_empty_graph(self):
        self.assertEqual(connected_components((), ()), [])

    def test_isolated_vertices(self):
        result = connected_components(("p", "q"), ())
        self.assertEqual(len(result), 2)
        self.assertCountEqual(result, [{"p"}, {"q"}])

    def test_undirected_paths_and_separate_groups(self):
        vertices = ("p", "q", "r", "s", "t", "u")
        edges = (("q", "p"), ("q", "r"), ("t", "s"))
        result = connected_components(vertices, edges)
        self.assertEqual(len(result), 3)
        self.assertCountEqual(result, [{"p", "q", "r"}, {"s", "t"}, {"u"}])

    def test_cycle(self):
        result = connected_components(
            ("p", "q", "r"), (("p", "q"), ("q", "r"), ("r", "p"))
        )
        self.assertEqual(result, [{"p", "q", "r"}])

    def test_partition_and_edge_invariants_for_supplied_scenarios(self):
        for name, edges in SCENARIOS.items():
            with self.subTest(scenario=name):
                result = connected_components(VERTICES, edges)
                self.assertIsInstance(result, list)
                for component in result:
                    self.assertIsInstance(component, set)
                    self.assertTrue(component)
                flattened = [vertex for component in result for vertex in component]
                self.assertCountEqual(flattened, VERTICES)
                for left, right in edges:
                    self.assertTrue(
                        any(left in component and right in component for component in result)
                    )


if __name__ == "__main__":
    unittest.main()
