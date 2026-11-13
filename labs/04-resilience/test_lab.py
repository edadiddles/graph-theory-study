"""Separate small graphs; make main-scenario predictions before reading.

Complete path lists in small examples certify disconnection without supplying
a reachability implementation or separator solver.
"""

import unittest

from lab import (
    SCENARIOS, SOURCE, TARGET, VERTICES,
    minimum_edge_separator, minimum_vertex_separator,
)


class VertexSeparatorTests(unittest.TestCase):
    def test_disconnected_terminals(self):
        self.assertEqual(
            minimum_vertex_separator(("p", "q", "r"), (("p", "q"),), "p", "r"),
            set(),
        )

    def test_path_with_multiple_minima(self):
        result = minimum_vertex_separator(
            ("p", "q", "r", "u"), (("p", "q"), ("q", "r"), ("r", "u")), "p", "u"
        )
        self.assertIsInstance(result, set)
        self.assertIn(result, ({"q"}, {"r"}))

    def test_alternative_routes(self):
        result = minimum_vertex_separator(
            ("p", "q", "r", "u"),
            (("p", "q"), ("q", "u"), ("p", "r"), ("r", "u")), "p", "u"
        )
        self.assertEqual(result, {"q", "r"})

    def test_shared_station(self):
        vertices = ("p", "q", "r", "v", "x", "y", "u")
        edges = (
            ("p", "q"), ("p", "r"), ("q", "v"), ("r", "v"),
            ("v", "x"), ("v", "y"), ("x", "u"), ("y", "u"),
        )
        self.assertEqual(minimum_vertex_separator(vertices, edges, "p", "u"), {"v"})

    def test_invalid_terminal_requests(self):
        cases = (
            (("p", "q", "r"), (("p", "q"),), "missing", "r"),
            (("p", "q", "r"), (("p", "q"),), "p", "missing"),
            (("p", "q", "r"), (("p", "q"),), "p", "p"),
            (("p", "q", "r"), (("p", "q"),), "p", "q"),
            ((), (), "p", "q"),
        )
        for vertices, edges, source, target in cases:
            with self.subTest(vertices=vertices, source=source, target=target):
                with self.assertRaises(ValueError):
                    minimum_vertex_separator(vertices, edges, source, target)

    def test_supplied_scenario_contract_and_input_preservation(self):
        for name, edges in SCENARIOS.items():
            with self.subTest(scenario=name):
                before = (VERTICES[:], edges[:])
                result = minimum_vertex_separator(VERTICES, edges, SOURCE, TARGET)
                self.assertIsInstance(result, set)
                self.assertTrue(result <= set(VERTICES) - {SOURCE, TARGET})
                self.assertEqual((VERTICES, edges), before)


class EdgeSeparatorTests(unittest.TestCase):
    def test_disconnected_terminals(self):
        self.assertEqual(
            minimum_edge_separator(("p", "q", "r"), (("p", "q"),), "p", "r"),
            set(),
        )

    def test_path_with_multiple_minima(self):
        edges = (("p", "q"), ("q", "r"), ("r", "u"))
        result = minimum_edge_separator(("p", "q", "r", "u"), edges, "p", "u")
        self.assertIsInstance(result, set)
        self.assertEqual(len(result), 1)
        self.assertTrue({frozenset(edge) for edge in result} <= {frozenset(edge) for edge in edges})

    def test_alternative_routes(self):
        edges = (("p", "q"), ("q", "u"), ("p", "r"), ("r", "u"))
        result = minimum_edge_separator(("p", "q", "r", "u"), edges, "p", "u")
        self.assertEqual(len(result), 2)
        removed = {frozenset(edge) for edge in result}
        self.assertEqual(len(removed), 2)
        self.assertTrue(removed <= {frozenset(edge) for edge in edges})
        paths = (("p", "q", "u"), ("p", "r", "u"))
        for path in paths:
            self.assertTrue(any(frozenset(pair) in removed for pair in zip(path, path[1:])))

    def test_shared_station_with_multiple_edge_routes(self):
        vertices = ("p", "q", "r", "v", "x", "y", "u")
        edges = (
            ("p", "q"), ("p", "r"), ("q", "v"), ("r", "v"),
            ("v", "x"), ("v", "y"), ("x", "u"), ("y", "u"),
        )
        result = minimum_edge_separator(vertices, edges, "p", "u")
        self.assertEqual(len(result), 2)
        removed = {frozenset(edge) for edge in result}
        self.assertEqual(len(removed), 2)
        self.assertTrue(removed <= {frozenset(edge) for edge in edges})
        paths = (
            ("p", "q", "v", "x", "u"), ("p", "q", "v", "y", "u"),
            ("p", "r", "v", "x", "u"), ("p", "r", "v", "y", "u"),
        )
        for path in paths:
            self.assertTrue(any(frozenset(pair) in removed for pair in zip(path, path[1:])))

    def test_adjacent_terminals(self):
        result = minimum_edge_separator(("p", "q"), (("p", "q"),), "p", "q")
        self.assertEqual(len(result), 1)
        self.assertEqual({frozenset(edge) for edge in result}, {frozenset(("p", "q"))})

    def test_invalid_terminal_requests(self):
        cases = (
            (("p", "q"), (("p", "q"),), "missing", "q"),
            (("p", "q"), (("p", "q"),), "p", "missing"),
            (("p", "q"), (("p", "q"),), "p", "p"),
            ((), (), "p", "q"),
        )
        for vertices, edges, source, target in cases:
            with self.subTest(vertices=vertices, source=source, target=target):
                with self.assertRaises(ValueError):
                    minimum_edge_separator(vertices, edges, source, target)

    def test_supplied_scenario_contract_and_input_preservation(self):
        for name, edges in SCENARIOS.items():
            with self.subTest(scenario=name):
                before = (VERTICES[:], edges[:])
                result = minimum_edge_separator(VERTICES, edges, SOURCE, TARGET)
                self.assertIsInstance(result, set)
                for edge in result:
                    self.assertIsInstance(edge, tuple)
                    self.assertEqual(len(edge), 2)
                normalized = {frozenset(edge) for edge in result}
                self.assertEqual(len(normalized), len(result))
                self.assertTrue(normalized <= {frozenset(edge) for edge in edges})
                self.assertEqual((VERTICES, edges), before)


if __name__ == "__main__":
    unittest.main()
