"""Separate hand-checkable operators and cuts; no partition solver is supplied.

Requires NumPy. Numerical tolerances concern the small well-scaled fixtures.
"""

import json
import unittest

import numpy as np
from numpy.testing import assert_allclose

from lab import KARATE_DATA_PATH, SCENARIOS, conductance, normalized_operators


class OperatorTests(unittest.TestCase):
    def test_weighted_path(self):
        operators = normalized_operators(("p", "q", "r"), (("p", "q"), ("q", "r")), (1.0, 2.0))
        expected_laplacian = np.array([
            [1, -1 / np.sqrt(3), 0],
            [-1 / np.sqrt(3), 1, -2 / np.sqrt(6)],
            [0, -2 / np.sqrt(6), 1],
        ])
        expected_walk = np.array([[0, 1, 0], [1 / 3, 0, 2 / 3], [0, 1, 0]])
        self.assertEqual(set(operators), {'L_norm', 'P', 'P_lazy'})
        for matrix in operators.values():
            self.assertIsInstance(matrix, np.ndarray)
            self.assertEqual(matrix.dtype, np.dtype('float64'))
        assert_allclose(operators['L_norm'], expected_laplacian, rtol=1e-10, atol=1e-12)
        assert_allclose(operators['P'], expected_walk, rtol=1e-10, atol=1e-12)
        assert_allclose(operators['P_lazy'], (np.eye(3) + expected_walk) / 2, atol=1e-12)

    def test_isolate_conventions(self):
        operators = normalized_operators(("p", "q", "r"), (("p", "q"),), (2.0,))
        assert_allclose(operators['L_norm'], [[1, -1, 0], [-1, 1, 0], [0, 0, 0]])
        assert_allclose(operators['P'], [[0, 1, 0], [1, 0, 0], [0, 0, 1]])
        assert_allclose(operators['P_lazy'], [[0.5, 0.5, 0], [0.5, 0.5, 0], [0, 0, 1]])

    def test_empty_and_edgeless_graphs(self):
        for vertices in ((), ("p", "q")):
            with self.subTest(vertices=vertices):
                operators = normalized_operators(vertices, (), ())
                for matrix in operators.values():
                    self.assertEqual(matrix.shape, (len(vertices), len(vertices)))
                assert_allclose(operators['L_norm'], np.zeros((len(vertices), len(vertices))))
                assert_allclose(operators['P'], np.eye(len(vertices)))
                assert_allclose(operators['P_lazy'], np.eye(len(vertices)))

    def test_representation_changes(self):
        vertices, edges, weights = ("p", "q", "r"), (("p", "q"), ("q", "r")), (1.0, 2.0)
        original = normalized_operators(vertices, edges, weights)
        permutation = [2, 0, 1]
        reordered = normalized_operators(tuple(vertices[i] for i in permutation), edges, weights)
        reversed_edges = tuple((right, left) for left, right in reversed(edges))
        reversed_operators = normalized_operators(vertices, reversed_edges, tuple(reversed(weights)))
        for name in ('L_norm', 'P', 'P_lazy'):
            assert_allclose(reordered[name], original[name][np.ix_(permutation, permutation)], atol=1e-12)
            assert_allclose(reversed_operators[name], original[name], atol=1e-12)

    def test_main_operator_and_walk_invariants(self):
        for name, case in SCENARIOS.items():
            with self.subTest(scenario=name):
                operators = normalized_operators(case['vertices'], case['edges'], case['weights'])
                laplacian = operators['L_norm']
                assert_allclose(laplacian, laplacian.T, atol=1e-12)
                values, vectors = np.linalg.eigh(laplacian)
                self.assertTrue(np.all(values >= -1e-12))
                self.assertTrue(np.all(values <= 2 + 1e-12))
                assert_allclose(laplacian @ vectors, vectors * values, rtol=1e-10, atol=1e-12)
                for key in ('P', 'P_lazy'):
                    transition = operators[key]
                    self.assertTrue(np.all(transition >= -1e-12))
                    assert_allclose(transition.sum(axis=1), 1.0, atol=1e-12)
                    distribution = np.array(case['initial'])
                    for _ in range(5):
                        distribution = distribution @ transition
                        self.assertTrue(np.all(distribution >= -1e-12))
                        self.assertAlmostEqual(float(distribution.sum()), 1.0)

    def test_hand_stationary_distribution(self):
        operators = normalized_operators(("p", "q", "r"), (("p", "q"), ("q", "r")), (1.0, 2.0))
        distribution = np.array([1.0, 3.0, 2.0]) / 6
        for name in ('P', 'P_lazy'):
            assert_allclose(distribution @ operators[name], distribution, rtol=1e-10, atol=1e-12)


class ConductanceTests(unittest.TestCase):
    def test_hand_calculated_partitions(self):
        cases = (
            ("path", ("p", "q", "r", "u"),
             (("p", "q"), ("q", "r"), ("r", "u")), (1.0, 1.0, 1.0), frozenset(("p", "q")), 1 / 3),
            ("weighted_path", ("p", "q", "r", "u"),
             (("p", "q"), ("q", "r"), ("r", "u")), (1.0, 2.0, 3.0), frozenset(("p", "q")), 0.5),
            ("disconnected", ("p", "q", "r", "u"),
             (("p", "q"), ("r", "u")), (2.0, 3.0), frozenset(("p", "q")), 0.0),
            ("isolate_on_positive_side", ("p", "q", "r"),
             (("p", "q"),), (2.0,), frozenset(("p", "r")), 1.0),
        )
        for name, vertices, edges, weights, subset, expected in cases:
            with self.subTest(case=name):
                result = conductance(vertices, edges, weights, subset)
                self.assertIs(type(result), float)
                self.assertAlmostEqual(result, expected)

    def test_scaling_and_complement(self):
        for name, case in SCENARIOS.items():
            with self.subTest(scenario=name):
                vertices, edges, weights = case['vertices'], case['edges'], case['weights']
                subset = frozenset(('a',))
                complement = frozenset(vertices) - subset
                scaled = tuple(7 * weight for weight in weights)
                value = conductance(vertices, edges, weights, subset)
                self.assertAlmostEqual(value, conductance(vertices, edges, weights, complement))
                self.assertAlmostEqual(value, conductance(vertices, edges, scaled, subset))
                original = normalized_operators(vertices, edges, weights)
                changed = normalized_operators(vertices, edges, scaled)
                for key in ('L_norm', 'P', 'P_lazy'):
                    assert_allclose(original[key], changed[key], rtol=1e-10, atol=1e-12)

    def test_invalid_partitions(self):
        vertices, edges, weights = ("p", "q", "r"), (("p", "q"),), (2.0,)
        for subset in (frozenset(), frozenset(vertices), frozenset(('unknown',)),
                       frozenset(('r',)), frozenset(('p', 'q'))):
            with self.subTest(subset=subset):
                with self.assertRaises(ValueError):
                    conductance(vertices, edges, weights, subset)
        with self.assertRaises(ValueError):
            conductance((), (), (), frozenset())


class BoundaryTests(unittest.TestCase):
    def test_invalid_weights(self):
        vertices, edges = ("p", "q"), (("p", "q"),)
        for weights in ((), (1.0, 2.0), (0.0,), (-1.0,), (float('nan'),), (float('inf'),)):
            for function, arguments in (
                (normalized_operators, (vertices, edges, weights)),
                (conductance, (vertices, edges, weights, frozenset(('p',)))),
            ):
                with self.subTest(weights=weights, function=function.__name__):
                    with self.assertRaises(ValueError):
                        function(*arguments)


class InputPreservationTests(unittest.TestCase):
    def test_inputs_unchanged(self):
        vertices, edges, weights = ("p", "q", "r"), (("p", "q"), ("q", "r")), (1.0, 2.0)
        subset = frozenset(('p',))
        for function, arguments in (
            (normalized_operators, (vertices, edges, weights)),
            (conductance, (vertices, edges, weights, subset)),
        ):
            with self.subTest(function=function.__name__):
                before = (vertices[:], edges[:], weights[:], subset)
                function(*arguments)
                self.assertEqual((vertices, edges, weights, subset), before)


class ObservedGraphTests(unittest.TestCase):
    def test_saved_graph_operator_contract(self):
        data = json.loads(KARATE_DATA_PATH.read_text())
        vertices = tuple(data['vertices'])
        edges = tuple(tuple(edge) for edge in data['edges'])
        operators = normalized_operators(vertices, edges, (1.0,) * len(edges))
        for matrix in operators.values():
            self.assertEqual(matrix.shape, (len(vertices), len(vertices)))
            self.assertTrue(np.isfinite(matrix).all())
        assert_allclose(operators['P'].sum(axis=1), 1.0, atol=1e-12)
        assert_allclose(operators['L_norm'], operators['L_norm'].T, atol=1e-12)


if __name__ == "__main__":
    unittest.main()
