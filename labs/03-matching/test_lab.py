"""Separate small examples; make the exercise predictions before reading."""

import unittest

from lab import LEFT, RIGHT, SCENARIOS, maximum_matching


class MaximumMatchingTests(unittest.TestCase):
    def test_empty_partitions(self):
        for left, right in (((), ()), (("p",), ()), ((), ("x",))):
            with self.subTest(left=left, right=right):
                self.assertEqual(maximum_matching(left, right, ()), set())

    def test_no_candidate_edges(self):
        self.assertEqual(maximum_matching(("p", "q"), ("x", "y"), ()), set())

    def test_single_candidate_and_isolated_records(self):
        result = maximum_matching(("p", "q"), ("x", "y"), (("p", "x"),))
        self.assertEqual(result, {("p", "x")})

    def test_global_cardinality(self):
        edges = (("p", "x"), ("p", "y"), ("q", "x"))
        result = maximum_matching(("p", "q"), ("x", "y"), edges)
        self.assertEqual(result, {("p", "y"), ("q", "x")})

    def test_multiple_optima(self):
        edges = (("p", "x"), ("p", "y"), ("q", "x"), ("q", "y"))
        result = maximum_matching(("p", "q"), ("x", "y"), edges)
        self.assertIsInstance(result, set)
        self.assertEqual(len(result), 2)
        self.assertTrue(result <= set(edges))
        self.assertEqual(len({left for left, _ in result}), 2)
        self.assertEqual(len({right for _, right in result}), 2)

    def test_some_records_must_remain_unmatched(self):
        edges = (("p", "x"), ("q", "x"))
        result = maximum_matching(("p", "q", "r"), ("x", "y"), edges)
        self.assertEqual(len(result), 1)
        self.assertTrue(result <= set(edges))

    def test_candidate_and_uniqueness_invariants_for_supplied_scenarios(self):
        for name, edges in SCENARIOS.items():
            with self.subTest(scenario=name):
                result = maximum_matching(LEFT, RIGHT, edges)
                self.assertIsInstance(result, set)
                self.assertTrue(result <= set(edges))
                self.assertEqual(len({left for left, _ in result}), len(result))
                self.assertEqual(len({right for _, right in result}), len(result))

    def test_inputs_unchanged(self):
        left, right = ("p", "q"), ("x", "y")
        edges = (("p", "x"), ("p", "y"), ("q", "x"))
        before = (left[:], right[:], edges[:])
        maximum_matching(left, right, edges)
        self.assertEqual((left, right, edges), before)


if __name__ == "__main__":
    unittest.main()
