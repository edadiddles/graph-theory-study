"""Separate hand-checkable optima; make scenario predictions before reading."""

import unittest

from lab import SCENARIOS, SINK, SOURCE, VERTICES, maximum_flow, minimum_cut


# Optimum values belong to these separate tiny examples, not the main scenarios.
# There is no reference solver and no requirement to return a specific optimum.
CASES = (
    ("no_arcs", ("p", "q", "u"), {}, 0),
    ("single_arc", ("p", "u"), {("p", "u"): 5}, 5),
    ("bottleneck", ("p", "q", "u"), {("p", "q"): 7, ("q", "u"): 3}, 3),
    ("parallel_routes", ("p", "q", "r", "u"),
     {("p", "q"): 2, ("q", "u"): 2, ("p", "r"): 3, ("r", "u"): 3}, 5),
    ("opposite_arcs", ("p", "q", "r", "u"),
     {("p", "q"): 3, ("p", "r"): 2, ("q", "r"): 2, ("r", "q"): 1,
      ("q", "u"): 2, ("r", "u"): 3}, 5),
    ("zero_capacity", ("p", "q", "u"), {("p", "q"): 0, ("q", "u"): 4}, 0),
    ("terminal_incoming_outgoing", ("p", "q", "u"),
     {("p", "q"): 5, ("q", "u"): 3, ("u", "p"): 4}, 3),
)

INVALID_REQUESTS = (
    (("p", "u"), {}, "missing", "u"),
    (("p", "u"), {}, "p", "missing"),
    (("p", "u"), {}, "p", "p"),
    ((), {}, "p", "u"),
)


class MaximumFlowTests(unittest.TestCase):
    def test_feasibility_and_known_optimum_values(self):
        for name, vertices, capacities, optimum in CASES:
            with self.subTest(case=name):
                flow = maximum_flow(vertices, capacities, "p", "u")
                self.assertIsInstance(flow, dict)
                self.assertEqual(set(flow), set(capacities))
                for arc, amount in flow.items():
                    self.assertIsInstance(amount, int)
                    self.assertGreaterEqual(amount, 0)
                    self.assertLessEqual(amount, capacities[arc])
                for vertex in vertices:
                    outgoing = sum(amount for (left, _), amount in flow.items() if left == vertex)
                    incoming = sum(amount for (_, right), amount in flow.items() if right == vertex)
                    if vertex == "p":
                        self.assertEqual(outgoing - incoming, optimum)
                    elif vertex == "u":
                        self.assertEqual(incoming - outgoing, optimum)
                    else:
                        self.assertEqual(incoming, outgoing)

    def test_main_scenario_feasibility(self):
        for name, capacities in SCENARIOS.items():
            with self.subTest(scenario=name):
                flow = maximum_flow(VERTICES, capacities, SOURCE, SINK)
                self.assertIsInstance(flow, dict)
                self.assertEqual(set(flow), set(capacities))
                for arc, amount in flow.items():
                    self.assertIsInstance(amount, int)
                    self.assertGreaterEqual(amount, 0)
                    self.assertLessEqual(amount, capacities[arc])
                for vertex in set(VERTICES) - {SOURCE, SINK}:
                    incoming = sum(amount for (_, right), amount in flow.items() if right == vertex)
                    outgoing = sum(amount for (left, _), amount in flow.items() if left == vertex)
                    self.assertEqual(incoming, outgoing)

    def test_invalid_terminals(self):
        for vertices, capacities, source, sink in INVALID_REQUESTS:
            with self.subTest(vertices=vertices, source=source, sink=sink):
                with self.assertRaises(ValueError):
                    maximum_flow(vertices, capacities, source, sink)


class MinimumCutTests(unittest.TestCase):
    def test_known_optimum_capacities(self):
        for name, vertices, capacities, optimum in CASES:
            with self.subTest(case=name):
                side = minimum_cut(vertices, capacities, "p", "u")
                self.assertIsInstance(side, set)
                self.assertTrue(side <= set(vertices))
                self.assertIn("p", side)
                self.assertNotIn("u", side)
                capacity = sum(
                    amount for (left, right), amount in capacities.items()
                    if left in side and right not in side
                )
                self.assertEqual(capacity, optimum)

    def test_main_scenario_cut_contract(self):
        for name, capacities in SCENARIOS.items():
            with self.subTest(scenario=name):
                side = minimum_cut(VERTICES, capacities, SOURCE, SINK)
                self.assertIsInstance(side, set)
                self.assertTrue(side <= set(VERTICES))
                self.assertIn(SOURCE, side)
                self.assertNotIn(SINK, side)

    def test_invalid_terminals(self):
        for vertices, capacities, source, sink in INVALID_REQUESTS:
            with self.subTest(vertices=vertices, source=source, sink=sink):
                with self.assertRaises(ValueError):
                    minimum_cut(vertices, capacities, source, sink)


class InputPreservationTests(unittest.TestCase):
    def test_inputs_unchanged(self):
        for function in (maximum_flow, minimum_cut):
            with self.subTest(function=function.__name__):
                vertices = ("p", "q", "u")
                capacities = {("p", "q"): 2, ("q", "u"): 1}
                before = (vertices[:], capacities.copy())
                function(vertices, capacities, "p", "u")
                self.assertEqual((vertices, capacities), before)


if __name__ == "__main__":
    unittest.main()
