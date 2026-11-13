"""Deterministic checks; no stochastic pass/fail thresholds or reference solvers."""

import hashlib
import json
import random
import unittest
from unittest.mock import Mock

from lab import DATA_PATH, graph_summary, sample_gnp


class SamplerTests(unittest.TestCase):
    def test_probability_boundaries(self):
        for probability, expected in (
            (0.0, set()), (1.0, {("p", "q"), ("p", "r"), ("q", "r")}),
        ):
            with self.subTest(probability=probability):
                result = sample_gnp(("r", "p", "q"), probability, random.Random(7))
                self.assertEqual(result, expected)

    def test_empty_and_singleton_inventories(self):
        for vertices in ((), ("p",)):
            with self.subTest(vertices=vertices):
                self.assertEqual(sample_gnp(vertices, 0.5, random.Random(7)), set())

    def test_controlled_uniform_draws(self):
        rng = Mock(spec=random.Random)
        rng.random.side_effect = (0.2, 0.8, 0.2)
        result = sample_gnp(("p", "q", "r"), 0.5, rng)
        self.assertIsInstance(result, set)
        self.assertEqual(len(result), 2)
        self.assertTrue(result <= {("p", "q"), ("p", "r"), ("q", "r")})
        self.assertEqual(rng.random.call_count, 3)
        rng.seed.assert_not_called()

    def test_seed_reproducibility(self):
        vertices = ("p", "q", "r", "u", "v")
        first = sample_gnp(vertices, 0.4, random.Random(19))
        second = sample_gnp(vertices, 0.4, random.Random(19))
        self.assertEqual(first, second)

    def test_invalid_probability(self):
        for probability in (-0.1, 1.1, float('nan'), float('inf'), -float('inf')):
            with self.subTest(probability=probability):
                with self.assertRaises(ValueError):
                    sample_gnp(("p", "q"), probability, random.Random(7))

    def test_generated_edge_contract(self):
        vertices = ("z", "a", "m", "b")
        for seed in (11, 23):
            with self.subTest(seed=seed):
                result = sample_gnp(vertices, 0.6, random.Random(seed))
                self.assertIsInstance(result, set)
                for edge in result:
                    self.assertIsInstance(edge, tuple)
                    self.assertEqual(len(edge), 2)
                    left, right = edge
                    self.assertIn(left, vertices)
                    self.assertIn(right, vertices)
                    self.assertLess(left, right)

    def test_global_random_state_unchanged(self):
        before = random.getstate()
        sample_gnp(("p", "q", "r"), 0.5, random.Random(31))
        self.assertEqual(random.getstate(), before)


class GraphSummaryTests(unittest.TestCase):
    def test_known_structural_summaries(self):
        cases = (
            ("empty", (), (), (0, 0, 0)),
            ("isolates", ("p", "q", "r"), (), (0, 0, 1)),
            ("path", ("p", "q", "r", "u"),
             (("p", "q"), ("q", "r"), ("r", "u")), (3, 0, 4)),
            ("triangle_and_isolate", ("p", "q", "r", "u"),
             (("p", "q"), ("q", "r"), ("r", "p")), (3, 1, 3)),
            ("two_triangles", ("p", "q", "r", "u", "v", "w"),
             (("p", "q"), ("q", "r"), ("r", "p"),
              ("u", "v"), ("v", "w"), ("w", "u")), (6, 2, 3)),
            ("complete_four", ("p", "q", "r", "u"),
             (("p", "q"), ("p", "r"), ("p", "u"),
              ("q", "r"), ("q", "u"), ("r", "u")), (6, 4, 4)),
        )
        for name, vertices, edges, expected in cases:
            with self.subTest(case=name):
                result = graph_summary(vertices, edges)
                self.assertEqual(result, dict(zip(
                    ('edge_count', 'triangle_count', 'largest_component_size'), expected
                )))
                for value in result.values():
                    self.assertIsInstance(value, int)

    def test_relabeling_and_edge_order(self):
        result = graph_summary(
            ("z", "x", "w", "y"), (("y", "x"), ("z", "y"), ("x", "z"))
        )
        self.assertEqual(result, {'edge_count': 3, 'triangle_count': 1, 'largest_component_size': 3})


class InputPreservationTests(unittest.TestCase):
    def test_graph_inputs_unchanged(self):
        vertices, edges = ("p", "q", "r"), (("p", "q"),)
        for function, arguments in (
            (sample_gnp, (vertices, 0.5, random.Random(7))),
            (graph_summary, (vertices, edges)),
        ):
            with self.subTest(function=function.__name__):
                before = (vertices[:], edges[:])
                state = random.getstate()
                function(*arguments)
                self.assertEqual((vertices, edges), before)
                self.assertEqual(random.getstate(), state)


class DatasetTests(unittest.TestCase):
    def test_saved_dataset_integrity(self):
        raw = DATA_PATH.read_bytes()
        self.assertEqual(hashlib.sha256(raw).hexdigest(),
                         'ace09747bb2d0bb7a43d11e1c7cada95cedd7f3b34699142a5686b6e4407e7dd')
        data = json.loads(raw)
        self.assertEqual(data['source_release'], 'NetworkX 3.4.2')
        self.assertIs(data['directed'], False)
        self.assertIs(data['weighted'], False)
        self.assertEqual(data['vertices'], [str(i) for i in range(34)])
        self.assertEqual(len(data['edges']), 78)
        self.assertEqual(len({tuple(edge) for edge in data['edges']}), 78)
        for left, right in data['edges']:
            self.assertIn(left, data['vertices'])
            self.assertIn(right, data['vertices'])
            self.assertLess(left, right)


if __name__ == "__main__":
    unittest.main()
