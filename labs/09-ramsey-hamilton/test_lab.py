"""Separate small existence examples and witness validators, without solvers."""

import unittest

from lab import (
    RAMSEY_SCENARIOS, RAMSEY_VERTICES, ROUTE_SCENARIOS, ROUTE_VERTICES,
    hamiltonian_cycle, monochromatic_triangle,
)


TRIANGLE_CASES = (
    ("empty", (), {}, False),
    ("two", ("a", "b"), {("a", "b"): "blue"}, False),
    ("mixed", ("a", "b", "c"),
     {("a", "b"): "red", ("a", "c"): "red", ("b", "c"): "blue"}, False),
    ("red", ("a", "b", "c"),
     {("a", "b"): "red", ("a", "c"): "red", ("b", "c"): "red"}, True),
    ("blue", ("a", "b", "c"),
     {("a", "b"): "blue", ("a", "c"): "blue", ("b", "c"): "blue"}, True),
    ("four_without", ("a", "b", "c", "d"),
     {("a", "b"): "red", ("a", "c"): "blue", ("a", "d"): "red",
      ("b", "c"): "red", ("b", "d"): "blue", ("c", "d"): "red"}, False),
    ("four_with", ("a", "b", "c", "d"),
     {("a", "b"): "red", ("a", "c"): "red", ("a", "d"): "blue",
      ("b", "c"): "red", ("b", "d"): "blue", ("c", "d"): "blue"}, True),
)

ROUTE_CASES = (
    ("empty", (), (), False),
    ("singleton", ("p",), (), False),
    ("two", ("p", "q"), (("p", "q"),), False),
    ("triangle", ("p", "q", "r"), (("p", "q"), ("q", "r"), ("r", "p")), True),
    ("cycle", ("p", "q", "r", "u"),
     (("p", "q"), ("q", "r"), ("r", "u"), ("u", "p")), True),
    ("path", ("p", "q", "r", "u"), (("p", "q"), ("q", "r"), ("r", "u")), False),
    ("cycle_and_isolate", ("p", "q", "r", "u", "v"),
     (("p", "q"), ("q", "r"), ("r", "u"), ("u", "p")), False),
    ("complete_four", ("p", "q", "r", "u"),
     (("p", "q"), ("p", "r"), ("p", "u"), ("q", "r"), ("q", "u"), ("r", "u")), True),
    ("connected_with_bridge", ("p", "q", "r", "u", "v", "w"),
     (("p", "q"), ("q", "r"), ("r", "p"), ("r", "u"),
      ("u", "v"), ("v", "w"), ("w", "u")), False),
)


class MonochromaticTriangleTests(unittest.TestCase):
    def test_known_existence_and_witnesses(self):
        for name, vertices, colors, exists in TRIANGLE_CASES:
            with self.subTest(case=name):
                witness = monochromatic_triangle(vertices, colors)
                if not exists:
                    self.assertIsNone(witness)
                else:
                    self.assertIsInstance(witness, tuple)
                    self.assertEqual(len(witness), 3)
                    self.assertEqual(len(set(witness)), 3)
                    self.assertTrue(set(witness) <= set(vertices))
                    labels = {colors[tuple(sorted(pair))] for pair in zip(witness, witness[1:] + witness[:1])}
                    self.assertEqual(len(labels), 1)

    def test_relabeling_color_swap_and_input_order(self):
        names = {"a": "z", "b": "x", "c": "w", "d": "y"}
        swap = {"red": "blue", "blue": "red"}
        for name, vertices, colors, exists in TRIANGLE_CASES[-2:]:
            with self.subTest(case=name):
                renamed = {
                    tuple(sorted((names[left], names[right]))): swap[color]
                    for (left, right), color in reversed(tuple(colors.items()))
                }
                witness = monochromatic_triangle(tuple(names[vertex] for vertex in reversed(vertices)), renamed)
                self.assertEqual(witness is not None, exists)
                if witness is not None:
                    self.assertIsInstance(witness, tuple)
                    self.assertEqual(len(witness), 3)
                    self.assertEqual(len(set(witness)), 3)
                    self.assertEqual(len({renamed[tuple(sorted(pair))] for pair in zip(witness, witness[1:] + witness[:1])}), 1)

    def test_main_scenario_witnesses(self):
        for name, colors in RAMSEY_SCENARIOS.items():
            with self.subTest(scenario=name):
                witness = monochromatic_triangle(RAMSEY_VERTICES, colors)
                if witness is not None:
                    self.assertIsInstance(witness, tuple)
                    self.assertEqual(len(witness), 3)
                    self.assertEqual(len(set(witness)), 3)
                    self.assertTrue(set(witness) <= set(RAMSEY_VERTICES))
                    self.assertEqual(len({colors[tuple(sorted(pair))] for pair in zip(witness, witness[1:] + witness[:1])}), 1)


class HamiltonCycleTests(unittest.TestCase):
    def test_known_existence_and_witnesses(self):
        for name, vertices, edges, exists in ROUTE_CASES:
            with self.subTest(case=name):
                witness = hamiltonian_cycle(vertices, edges)
                if not exists:
                    self.assertIsNone(witness)
                else:
                    self.assertIsInstance(witness, tuple)
                    self.assertEqual(len(witness), len(vertices))
                    self.assertEqual(set(witness), set(vertices))
                    available = {frozenset(edge) for edge in edges}
                    for pair in zip(witness, witness[1:] + witness[:1]):
                        self.assertIn(frozenset(pair), available)

    def test_relabeling_and_edge_order(self):
        vertices = ("y", "z", "w", "x")
        edges = (("x", "w"), ("w", "z"), ("z", "y"), ("y", "x"))
        witness = hamiltonian_cycle(vertices, tuple((right, left) for left, right in reversed(edges)))
        self.assertIsInstance(witness, tuple)
        self.assertEqual(len(witness), len(vertices))
        self.assertEqual(set(witness), set(vertices))
        for pair in zip(witness, witness[1:] + witness[:1]):
            self.assertIn(frozenset(pair), {frozenset(edge) for edge in edges})

    def test_main_scenario_witnesses(self):
        for name, edges in ROUTE_SCENARIOS.items():
            with self.subTest(scenario=name):
                witness = hamiltonian_cycle(ROUTE_VERTICES, edges)
                if witness is not None:
                    self.assertIsInstance(witness, tuple)
                    self.assertEqual(len(witness), len(ROUTE_VERTICES))
                    self.assertEqual(set(witness), set(ROUTE_VERTICES))
                    for pair in zip(witness, witness[1:] + witness[:1]):
                        self.assertIn(frozenset(pair), {frozenset(edge) for edge in edges})


class InputPreservationTests(unittest.TestCase):
    def test_inputs_unchanged(self):
        vertices = ("a", "b", "c")
        colors = {("a", "b"): "red", ("a", "c"): "red", ("b", "c"): "blue"}
        edges = (("a", "b"), ("b", "c"), ("c", "a"))
        for function, arguments in (
            (monochromatic_triangle, (vertices, colors)),
            (hamiltonian_cycle, (vertices, edges)),
        ):
            with self.subTest(function=function.__name__):
                before = (vertices[:], colors.copy(), edges[:])
                function(*arguments)
                self.assertEqual((vertices, colors, edges), before)


if __name__ == "__main__":
    unittest.main()
