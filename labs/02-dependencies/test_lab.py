"""Separate examples for checking behavior; make exercise predictions first."""

import unittest

from lab import SCENARIOS, VERTICES, reachable_vertices, strongly_connected_components


class ReachabilityTests(unittest.TestCase):
    def test_isolated_start(self):
        self.assertEqual(reachable_vertices(("p", "q"), (), "p"), {"p"})

    def test_edge_direction(self):
        vertices = ("p", "q")
        edges = (("p", "q"),)
        self.assertEqual(reachable_vertices(vertices, edges, "p"), {"p", "q"})
        self.assertEqual(reachable_vertices(vertices, edges, "q"), {"q"})

    def test_branches_and_shared_dependency(self):
        vertices = ("p", "q", "r", "s", "t")
        edges = (("p", "q"), ("p", "r"), ("q", "s"), ("r", "s"))
        result = reachable_vertices(vertices, edges, "p")
        self.assertIsInstance(result, set)
        self.assertEqual(result, {"p", "q", "r", "s"})

    def test_cycle_with_outgoing_edge_and_disconnected_vertex(self):
        result = reachable_vertices(
            ("p", "q", "r", "s"), (("p", "q"), ("q", "p"), ("q", "r")), "p"
        )
        self.assertEqual(result, {"p", "q", "r"})

    def test_unknown_start(self):
        for vertices in ((), ("p",)):
            with self.subTest(vertices=vertices):
                with self.assertRaises(ValueError):
                    reachable_vertices(vertices, (), "missing")

    def test_inputs_unchanged(self):
        vertices = ("p", "q")
        edges = (("p", "q"),)
        before = (vertices[:], edges[:])
        reachable_vertices(vertices, edges, "p")
        self.assertEqual((vertices, edges), before)


class StrongComponentsTests(unittest.TestCase):
    def test_empty_graph(self):
        self.assertEqual(strongly_connected_components((), ()), [])

    def test_isolated_vertices(self):
        result = strongly_connected_components(("p", "q"), ())
        self.assertCountEqual(result, [{"p"}, {"q"}])

    def test_one_way_path(self):
        result = strongly_connected_components(
            ("p", "q", "r"), (("p", "q"), ("q", "r"))
        )
        self.assertCountEqual(result, [{"p"}, {"q"}, {"r"}])

    def test_cycles_with_one_way_connection_and_isolated_vertex(self):
        vertices = ("p", "q", "r", "s", "t")
        edges = (("p", "q"), ("q", "p"), ("q", "r"), ("r", "s"), ("s", "r"))
        result = strongly_connected_components(vertices, edges)
        self.assertCountEqual(result, [{"p", "q"}, {"r", "s"}, {"t"}])

    def test_partition_invariants_for_supplied_scenarios(self):
        for name, edges in SCENARIOS.items():
            with self.subTest(scenario=name):
                result = strongly_connected_components(VERTICES, edges)
                self.assertIsInstance(result, list)
                for component in result:
                    self.assertIsInstance(component, set)
                    self.assertTrue(component)
                flattened = [vertex for component in result for vertex in component]
                self.assertCountEqual(flattened, VERTICES)

    def test_inputs_unchanged(self):
        vertices = ("p", "q")
        edges = (("p", "q"), ("q", "p"))
        before = (vertices[:], edges[:])
        strongly_connected_components(vertices, edges)
        self.assertEqual((vertices, edges), before)


if __name__ == "__main__":
    unittest.main()
