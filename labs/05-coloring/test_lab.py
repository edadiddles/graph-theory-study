"""Separate examples; make independent scenario predictions before reading."""

import unittest

from lab import EXAMS, SCENARIOS, build_conflict_edges, minimum_coloring


class ConflictEdgesTests(unittest.TestCase):
    def test_empty_enrollment(self):
        for exams in ((), ("p", "q")):
            with self.subTest(exams=exams):
                self.assertEqual(build_conflict_edges(exams, ()), set())

    def test_shared_enrollment(self):
        result = build_conflict_edges(("p", "q", "r", "u"), (("r", "p", "q"),))
        self.assertEqual(result, {("p", "q"), ("p", "r"), ("q", "r")})

    def test_repeated_evidence_and_canonical_order(self):
        result = build_conflict_edges(
            ("p", "q", "r"), (("q", "p"), ("p", "q"), ("q", "p"), ("r",))
        )
        self.assertEqual(result, {("p", "q")})

    def test_no_unsupported_conflicts(self):
        result = build_conflict_edges(("p", "q", "r"), (("p",), (), ("q",)))
        self.assertEqual(result, set())

    def test_supplied_scenario_edge_contract(self):
        for name, rows in SCENARIOS.items():
            with self.subTest(scenario=name):
                result = build_conflict_edges(EXAMS, rows)
                self.assertIsInstance(result, set)
                for edge in result:
                    self.assertIsInstance(edge, tuple)
                    self.assertEqual(len(edge), 2)
                    left, right = edge
                    self.assertIn(left, EXAMS)
                    self.assertIn(right, EXAMS)
                    self.assertLess(left, right)
                    self.assertTrue(any(left in row and right in row for row in rows))


class MinimumColoringTests(unittest.TestCase):
    def test_hand_checkable_optimum_sizes(self):
        cases = (
            ("empty", (), (), 0),
            ("isolates", ("p", "q", "r"), (), 1),
            ("edge_and_isolate", ("p", "q", "r"), (("q", "p"),), 2),
            ("triangle_and_edge", ("p", "q", "r", "u", "v"),
             (("p", "q"), ("q", "r"), ("r", "p"), ("u", "v")), 3),
            ("odd_cycle", ("p", "q", "r", "u", "v"),
             (("p", "q"), ("q", "r"), ("r", "u"), ("u", "v"), ("v", "p")), 3),
            ("separate_edges", ("p", "q", "r", "u"), (("p", "q"), ("r", "u")), 2),
        )
        for name, vertices, edges, optimum in cases:
            with self.subTest(case=name):
                result = minimum_coloring(vertices, edges)
                self.assertIsInstance(result, dict)
                self.assertEqual(set(result), set(vertices))
                for color in result.values():
                    self.assertIsInstance(color, int)
                for left, right in edges:
                    self.assertNotEqual(result[left], result[right])
                self.assertEqual(len(set(result.values())), optimum)

    def test_supplied_scenario_schedule_validity(self):
        for name, rows in SCENARIOS.items():
            with self.subTest(scenario=name):
                edges = tuple(sorted(build_conflict_edges(EXAMS, rows)))
                result = minimum_coloring(EXAMS, edges)
                self.assertEqual(set(result), set(EXAMS))
                for row in rows:
                    self.assertEqual(len({result[exam] for exam in row}), len(row))


class InputPreservationTests(unittest.TestCase):
    def test_inputs_unchanged(self):
        exams = ("p", "q", "r")
        rows = (("p", "q"), ("r",))
        edges = (("p", "q"),)
        before = (exams[:], rows[:], edges[:])
        build_conflict_edges(exams, rows)
        minimum_coloring(exams, edges)
        self.assertEqual((exams, rows, edges), before)


if __name__ == "__main__":
    unittest.main()
