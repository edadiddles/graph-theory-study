"""Separate numerical examples; make hand predictions before reading tests.

Requires NumPy. Tolerances apply to these small well-scaled fixtures, not all
possible problems. No reference graph-matrix assembly or physical solver is given.
"""

import unittest

import numpy as np
from numpy.testing import assert_allclose

from lab import SCENARIOS, graph_matrices, quadratic_form


class GraphMatrixTests(unittest.TestCase):
    def test_weighted_edge(self):
        matrices = graph_matrices(("p", "q"), (("p", "q"),), (2.0,))
        expected = {
            "B": [[-1.0], [1.0]], "A": [[0.0, 2.0], [2.0, 0.0]],
            "D": [[2.0, 0.0], [0.0, 2.0]], "L": [[2.0, -2.0], [-2.0, 2.0]],
        }
        self.assertEqual(set(matrices), set(expected))
        for name, values in expected.items():
            self.assertIsInstance(matrices[name], np.ndarray)
            self.assertEqual(matrices[name].dtype, np.dtype('float64'))
            assert_allclose(matrices[name], values, rtol=1e-10, atol=1e-12)

    def test_empty_graph_and_isolates(self):
        for vertices in ((), ("p", "q")):
            with self.subTest(vertices=vertices):
                matrices = graph_matrices(vertices, (), ())
                self.assertEqual(matrices['B'].shape, (len(vertices), 0))
                self.assertEqual(set(matrices), {'B', 'A', 'D', 'L'})
                for name in ('A', 'D', 'L'):
                    self.assertEqual(matrices[name].shape, (len(vertices), len(vertices)))
                    assert_allclose(matrices[name], np.zeros((len(vertices), len(vertices))))

    def test_weighted_path(self):
        matrices = graph_matrices(("p", "q", "r"), (("p", "q"), ("q", "r")), (1.0, 2.0))
        assert_allclose(matrices['B'], [[-1, 0], [1, -1], [0, 1]])
        assert_allclose(matrices['L'], [[1, -1, 0], [-1, 3, -2], [0, -2, 2]])

    def test_orientation_invariance(self):
        vertices, edges, weights = ("p", "q", "r"), (("p", "q"), ("q", "r")), (1.0, 2.0)
        original = graph_matrices(vertices, edges, weights)
        reversed_matrices = graph_matrices(vertices, tuple((right, left) for left, right in edges), weights)
        assert_allclose(reversed_matrices['B'], -original['B'])
        for name in ('A', 'D', 'L'):
            assert_allclose(reversed_matrices[name], original[name])
        vector = np.array([1.0, 0.0, -1.0])
        self.assertAlmostEqual(quadratic_form(original['L'], vector),
                               quadratic_form(reversed_matrices['L'], vector))

    def test_vertex_order_consistency(self):
        vertices, edges, weights = ("p", "q", "r"), (("p", "q"), ("q", "r")), (1.0, 2.0)
        permutation = [2, 0, 1]
        original = graph_matrices(vertices, edges, weights)
        reordered = graph_matrices(tuple(vertices[i] for i in permutation), edges, weights)
        assert_allclose(reordered['B'], original['B'][permutation, :])
        for name in ('A', 'D', 'L'):
            assert_allclose(reordered[name], original[name][np.ix_(permutation, permutation)])
        vector = np.array([1.0, 0.0, -1.0])
        self.assertAlmostEqual(quadratic_form(original['L'], vector),
                               quadratic_form(reordered['L'], vector[permutation]))

    def test_main_scenario_matrix_and_spectral_invariants(self):
        for name, case in SCENARIOS.items():
            with self.subTest(scenario=name):
                matrices = graph_matrices(case['vertices'], case['edges'], case['weights'])
                incidence, laplacian = matrices['B'], matrices['L']
                assert_allclose(laplacian, laplacian.T, atol=1e-12)
                assert_allclose(laplacian, matrices['D'] - matrices['A'], atol=1e-12)
                assert_allclose(laplacian, incidence @ np.diag(case['weights']) @ incidence.T, atol=1e-12)
                assert_allclose(laplacian @ np.ones(len(case['vertices'])), 0.0, atol=1e-12)
                values, vectors = np.linalg.eigh(laplacian)
                self.assertTrue(np.all(values >= -1e-12))
                assert_allclose(laplacian @ vectors, vectors * values, rtol=1e-10, atol=1e-12)
                assert_allclose(vectors.T @ vectors, np.eye(len(values)), rtol=1e-10, atol=1e-12)
                self.assertGreaterEqual(quadratic_form(laplacian, np.array(case['vector'])), -1e-12)

    def test_disconnected_nullspace(self):
        matrices = graph_matrices(("p", "q", "r"), (("p", "q"),), (2.0,))
        values = np.linalg.eigvalsh(matrices['L'])
        self.assertEqual(np.count_nonzero(np.abs(values) < 1e-12), 2)

    def test_invalid_weights(self):
        for weights in ((), (1.0, 2.0), (0.0,), (-1.0,), (float('nan'),), (float('inf'),)):
            with self.subTest(weights=weights):
                with self.assertRaises(ValueError):
                    graph_matrices(("p", "q"), (("p", "q"),), weights)


class QuadraticFormTests(unittest.TestCase):
    def test_hand_calculated_values(self):
        cases = (
            (np.zeros((0, 0)), np.zeros(0), 0.0),
            (np.array([[2.0, -2.0], [-2.0, 2.0]]), np.array([1.0, -1.0]), 8.0),
            (np.array([[2.0, -2.0], [-2.0, 2.0]]), np.array([3.0, 3.0]), 0.0),
        )
        for matrix, vector, expected in cases:
            with self.subTest(vector=vector):
                result = quadratic_form(matrix, vector)
                self.assertIs(type(result), float)
                self.assertAlmostEqual(result, expected)

    def test_invalid_dimensions(self):
        for matrix, vector in (
            (np.zeros((2, 3)), np.zeros(2)), (np.zeros((2, 2)), np.zeros(3)),
            (np.zeros((2, 2)), np.zeros((2, 1))), (np.zeros(2), np.zeros(2)),
            (np.zeros((0, 0)), np.zeros((0, 1))),
        ):
            with self.subTest(matrix_shape=matrix.shape, vector_shape=vector.shape):
                with self.assertRaises(ValueError):
                    quadratic_form(matrix, vector)


class PhysicalExampleTests(unittest.TestCase):
    def test_two_node_modes(self):
        laplacian = graph_matrices(("p", "q"), (("p", "q"),), (2.0,))['L']
        values, vectors = np.linalg.eigh(laplacian)
        assert_allclose(values, [0.0, 4.0], atol=1e-12)
        assert_allclose(laplacian @ vectors, vectors * values, rtol=1e-10, atol=1e-12)

    def test_two_node_grounded_circuit(self):
        laplacian = graph_matrices(("p", "q"), (("p", "q"),), (2.0,))['L']
        current = np.array([1.0, -1.0])
        free_potential = np.linalg.solve(laplacian[:1, :1], current[:1])
        potential = np.array([free_potential[0], 0.0])
        assert_allclose(potential, [0.5, 0.0], atol=1e-12)
        assert_allclose(laplacian @ potential, current, rtol=1e-10, atol=1e-12)

    def test_ungrounded_singularity_visible(self):
        laplacian = graph_matrices(("p", "q"), (("p", "q"),), (2.0,))['L']
        with self.assertRaises(np.linalg.LinAlgError):
            np.linalg.solve(laplacian, np.array([1.0, -1.0]))


class InputPreservationTests(unittest.TestCase):
    def test_graph_inputs_unchanged(self):
        vertices, edges, weights = ("p", "q"), (("p", "q"),), (2.0,)
        before = (vertices[:], edges[:], weights[:])
        graph_matrices(vertices, edges, weights)
        self.assertEqual((vertices, edges, weights), before)

    def test_array_inputs_unchanged(self):
        matrix = np.array([[2.0, -2.0], [-2.0, 2.0]])
        vector = np.array([1.0, -1.0])
        matrix_before, vector_before = matrix.copy(), vector.copy()
        quadratic_form(matrix, vector)
        np.testing.assert_array_equal(matrix, matrix_before)
        np.testing.assert_array_equal(vector, vector_before)


if __name__ == "__main__":
    unittest.main()
