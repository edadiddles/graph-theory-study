"""Behavioral checks, separate from predictions. Requires learner implementation.

No reference eigensolver/exponential implementation is supplied. Expected values
below are small hand cases; tolerances concern small well-scaled operators.
"""

import unittest

import numpy as np
from numpy.testing import assert_allclose

from lab import SCENARIOS, continuous_time_transition, heat_kernel


class HeatTests(unittest.TestCase):
    def test_zero_time_and_empty_shape(self):
        for operator in (np.empty((0, 0)), np.zeros((3, 3)),
                         np.array([[2, -2], [-2, 2]], dtype=float)):
            with self.subTest(shape=operator.shape):
                result = heat_kernel(operator, 0.0)
                self.assertIsInstance(result, np.ndarray)
                self.assertEqual(result.dtype, np.dtype('float64'))
                self.assertEqual(result.shape, operator.shape)
                assert_allclose(result, np.eye(len(operator)), atol=1e-12)
                self.assertFalse(np.shares_memory(result, operator))
        self.assertEqual(heat_kernel(np.empty((0, 0)), 2.0).shape, (0, 0))

    def test_hand_two_vertex_heat(self):
        operator = np.array([[2, -2], [-2, 2]], dtype=float)
        for time in (0.1, 0.5, 2.0):
            with self.subTest(time=time):
                decay = np.exp(-4 * time)
                expected = np.array([[1 + decay, 1 - decay],
                                     [1 - decay, 1 + decay]]) / 2
                result = heat_kernel(operator, time)
                assert_allclose(result, expected, rtol=1e-10, atol=1e-12)
                self.assertEqual(result.dtype, np.dtype('float64'))

    def test_symmetric_normalized_coordinates(self):
        # The unit-weight path has degrees (1, 2, 1). Ordinary row sums
        # are deliberately not a required invariant of its symmetric kernel.
        operator = np.array([[1, -1 / np.sqrt(2), 0],
                             [-1 / np.sqrt(2), 1, -1 / np.sqrt(2)],
                             [0, -1 / np.sqrt(2), 1]])
        result = heat_kernel(operator, 0.7)
        assert_allclose(result, result.T, atol=1e-12)
        stationary_coordinates = np.array([1, np.sqrt(2), 1])
        assert_allclose(result @ stationary_coordinates, stationary_coordinates, atol=1e-12)
        mode = np.array([1, 0, -1])
        assert_allclose(result @ mode, np.exp(-0.7) * mode, atol=1e-12)
        self.assertGreater(np.max(np.abs(result.sum(axis=1) - 1)), 1e-3)

    def test_composition_contraction_and_component_blocks(self):
        operator = np.array([[1, -1, 0, 0], [-1, 1, 0, 0],
                             [0, 0, 3, -3], [0, 0, -3, 3]], dtype=float)
        first, second = heat_kernel(operator, 0.2), heat_kernel(operator, 0.4)
        assert_allclose(first @ second, heat_kernel(operator, 0.6), atol=1e-12)
        assert_allclose(first[:2, 2:], 0, atol=1e-12)
        assert_allclose(first[2:, :2], 0, atol=1e-12)
        values = np.linalg.eigvalsh(first)
        self.assertTrue(np.all(values >= -1e-12))
        self.assertTrue(np.all(values <= 1 + 1e-12))
        assert_allclose(first, first.T, atol=1e-12)

    def test_zero_boundary_and_induced_models(self):
        # Middle vertex of a three-vertex normalized path: principal
        # restriction versus normalized induced singleton.
        time = 0.7
        assert_allclose(heat_kernel(np.array([[1.0]]), time), [[np.exp(-time)]], atol=1e-12)
        assert_allclose(heat_kernel(np.array([[0.0]]), time), [[1.0]], atol=1e-12)
        operator = np.diag([0.0, 2.0, 0.0])
        assert_allclose(heat_kernel(operator, time), np.diag([1.0, np.exp(-2 * time), 1.0]), atol=1e-12)

    def test_invalid_dimensions_and_times(self):
        for operator in (np.array(1.0), np.ones(3), np.ones((2, 3)), np.ones((2, 2, 2))):
            with self.subTest(shape=operator.shape):
                with self.assertRaises(ValueError):
                    heat_kernel(operator, 1.0)
        for time in (-1.0, float('inf'), float('-inf'), float('nan')):
            with self.subTest(time=time):
                with self.assertRaises(ValueError):
                    heat_kernel(np.eye(2), time)


class TransitionTests(unittest.TestCase):
    def test_hand_edge_and_output_contract(self):
        for time in (0.0, 0.1, 0.5, 2.0):
            with self.subTest(time=time):
                decay = np.exp(-2 * time)
                expected = np.array([[1 + decay, 1 - decay],
                                     [1 - decay, 1 + decay]]) / 2
                result = continuous_time_transition(('p', 'q'), (('p', 'q'),), (7.0,), time)
                self.assertIsInstance(result, np.ndarray)
                self.assertEqual(result.dtype, np.dtype('float64'))
                self.assertEqual(result.shape, (2, 2))
                assert_allclose(result, expected, atol=1e-12)

    def test_probability_and_composition(self):
        for name, case in SCENARIOS.items():
            with self.subTest(scenario=name):
                args = case['vertices'], case['edges'], case['weights']
                first = continuous_time_transition(*args, 0.2)
                second = continuous_time_transition(*args, 0.5)
                result = continuous_time_transition(*args, 0.7)
                self.assertEqual(result.shape, (len(case['vertices']),) * 2)
                assert_allclose(first @ second, result, atol=1e-12)
                assert_allclose(result.sum(axis=1), 1, atol=1e-12)
                self.assertTrue(np.all(result >= -1e-12))
                distribution = np.array(case['initial']) @ result
                self.assertTrue(np.all(distribution >= -1e-12))
                self.assertAlmostEqual(float(distribution.sum()), 1.0)
                assert_allclose(continuous_time_transition(*args, 0.0), np.eye(len(case['vertices'])), atol=1e-12)

    def test_irregular_walk_generator_and_stationarity(self):
        args = ('p', 'q', 'r'), (('p', 'q'), ('q', 'r')), (1.0, 2.0)
        result = continuous_time_transition(*args, 0.7)
        stationary = np.array([1.0, 3.0, 2.0]) / 6
        assert_allclose(stationary @ result, stationary, atol=1e-12)
        flux = stationary[:, None] * result
        assert_allclose(flux, flux.T, atol=1e-12)
        self.assertGreater(np.max(np.abs(result - result.T)), 1e-3)
        step = 1e-5
        generator = np.array([[-1, 1, 0], [1 / 3, -1, 2 / 3], [0, 1, -1]])
        difference = (continuous_time_transition(*args, step) - np.eye(3)) / step
        assert_allclose(difference, generator, rtol=0, atol=2e-5)

    def test_isolates_empty_and_disconnected(self):
        self.assertEqual(continuous_time_transition((), (), (), 1.0).shape, (0, 0))
        assert_allclose(continuous_time_transition(('p', 'q'), (), (), 2.0), np.eye(2), atol=1e-12)
        vertices = ('p', 'q', 'r', 's', 't')
        result = continuous_time_transition(vertices, (('p', 'q'), ('r', 's')), (1.0, 3.0), 0.4)
        assert_allclose(result[:2, 2:], 0, atol=1e-12)
        assert_allclose(result[2:4, :2], 0, atol=1e-12)
        assert_allclose(result[4], [0, 0, 0, 0, 1], atol=1e-12)
        assert_allclose(result[:, 4], [0, 0, 0, 0, 1], atol=1e-12)
        self.assertAlmostEqual(float((np.array([0.2, 0.3, 0.1, 0.1, 0.3]) @ result)[:2].sum()), 0.5)

    def test_scaling_orientation_and_vertex_order(self):
        vertices, edges, weights = ('p', 'q', 'r'), (('p', 'q'), ('q', 'r')), (1.0, 2.0)
        original = continuous_time_transition(vertices, edges, weights, 0.7)
        changed = continuous_time_transition(vertices, (('r', 'q'), ('q', 'p')), (14.0, 7.0), 0.7)
        assert_allclose(original, changed, atol=1e-12)
        permutation = [2, 0, 1]
        reordered = continuous_time_transition(tuple(vertices[i] for i in permutation), edges, weights, 0.7)
        assert_allclose(reordered, original[np.ix_(permutation, permutation)], atol=1e-12)

    def test_invalid_times_and_weights(self):
        for time in (-1.0, float('nan'), float('inf'), float('-inf')):
            with self.subTest(time=time):
                with self.assertRaises(ValueError):
                    continuous_time_transition(('p', 'q'), (('p', 'q'),), (1.0,), time)
        for weights in ((), (1.0, 2.0), (0.0,), (-1.0,), (float('nan'),), (float('inf'),)):
            with self.subTest(weights=weights):
                with self.assertRaises(ValueError):
                    continuous_time_transition(('p', 'q'), (('p', 'q'),), weights, 1.0)


class PreservationTests(unittest.TestCase):
    def test_inputs_unchanged(self):
        operator = np.array([[1, -1], [-1, 1]], dtype=float)
        original = operator.copy()
        heat_kernel(operator, 0.4)
        assert_allclose(operator, original, atol=0, rtol=0)
        vertices, edges, weights = ('p', 'q'), (('p', 'q'),), (2.0,)
        before = vertices[:], edges[:], weights[:]
        continuous_time_transition(vertices, edges, weights, 0.4)
        self.assertEqual((vertices, edges, weights), before)


if __name__ == '__main__':
    unittest.main()
