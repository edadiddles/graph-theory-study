"""Separate hand-checkable cuts and boundary matrices; no family classifier."""

import unittest

import numpy as np
from numpy.testing import assert_allclose

from lab import BOUNDARY_CASES, boundary_operators, cut_discrepancy


class DiscrepancyTests(unittest.TestCase):
    def test_hand_counted_cuts(self):
        vertices = ("p", "q", "r", "u")
        left, right = frozenset(('p', 'q')), frozenset(('r', 'u'))
        cases = (
            ("positive", (("p", "q"), ("p", "r"), ("q", "u")), 0.25, left, right, 1.0),
            ("negative", (("p", "q"),), 0.5, left, right, -2.0),
            ("empty_side", (("p", "r"),), 0.5, frozenset(), right, 0.0),
            ("zero_density", (("p", "r"), ("q", "u")), 0.0, left, right, 2.0),
        )
        for name, edges, density, side_a, side_b, expected in cases:
            with self.subTest(case=name):
                result = cut_discrepancy(vertices, edges, density, side_a, side_b)
                self.assertIs(type(result), float)
                self.assertAlmostEqual(result, expected)
        self.assertEqual(cut_discrepancy((), (), 0.5, frozenset(), frozenset()), 0.0)

    def test_side_swap_and_representation(self):
        vertices = ("p", "q", "r", "u")
        edges = (("p", "r"), ("q", "u"), ("p", "q"))
        left, right = frozenset(('p', 'q')), frozenset(('r', 'u'))
        value = cut_discrepancy(vertices, edges, 0.25, left, right)
        self.assertAlmostEqual(value, cut_discrepancy(vertices, edges, 0.25, right, left))
        names = {'p':'z', 'q':'x', 'r':'w', 'u':'y'}
        renamed_edges = tuple((names[b], names[a]) for a,b in reversed(edges))
        self.assertAlmostEqual(value, cut_discrepancy(
            tuple(names[v] for v in reversed(vertices)), renamed_edges, 0.25,
            frozenset(names[v] for v in left), frozenset(names[v] for v in right),
        ))

    def test_invalid_density(self):
        for density in (-0.1, 1.1, float('nan'), float('inf')):
            with self.subTest(density=density):
                with self.assertRaises(ValueError):
                    cut_discrepancy(("p", "q"), (("p", "q"),), density, frozenset(('p',)), frozenset(('q',)))

    def test_invalid_sets(self):
        for left, right in (
            (frozenset(('unknown',)), frozenset(('q',))),
            (frozenset(('p',)), frozenset(('unknown',))),
            (frozenset(('p',)), frozenset(('p',))),
        ):
            with self.subTest(left=left, right=right):
                with self.assertRaises(ValueError):
                    cut_discrepancy(("p", "q"), (("p", "q"),), 0.5, left, right)


class BoundaryOperatorTests(unittest.TestCase):
    def test_hand_derived_weighted_restriction(self):
        result = boundary_operators(
            ("p", "q", "r", "u"), (("p", "q"), ("q", "r"), ("r", "u")),
            (1.0, 2.0, 3.0), ("p", "q", "r"),
        )
        self.assertEqual(set(result), {'dirichlet', 'induced'})
        expected_dirichlet = [[1, -1/np.sqrt(3), 0], [-1/np.sqrt(3), 1, -2/np.sqrt(15)], [0, -2/np.sqrt(15), 1]]
        expected_induced = [[1, -1/np.sqrt(3), 0], [-1/np.sqrt(3), 1, -2/np.sqrt(6)], [0, -2/np.sqrt(6), 1]]
        assert_allclose(result['dirichlet'], expected_dirichlet, rtol=1e-10, atol=1e-12)
        assert_allclose(result['induced'], expected_induced, rtol=1e-10, atol=1e-12)
        for matrix in result.values():
            self.assertIsInstance(matrix, np.ndarray)
            self.assertEqual(matrix.dtype, np.dtype('float64'))

    def test_single_interior_vertex(self):
        result = boundary_operators(("p", "q", "r"), (("p", "q"), ("q", "r")), (1.0, 3.0), ("q",))
        assert_allclose(result['dirichlet'], [[1.0]])
        assert_allclose(result['induced'], [[0.0]])

    def test_original_and_induced_isolates(self):
        result = boundary_operators(("p", "q", "r"), (("p", "q"),), (2.0,), ("p", "r"))
        assert_allclose(result['dirichlet'], [[1, 0], [0, 0]])
        assert_allclose(result['induced'], np.zeros((2, 2)))

    def test_empty_and_full_interior(self):
        for interior in ((), ("p", "q")):
            with self.subTest(interior=interior):
                result = boundary_operators(("p", "q"), (("p", "q"),), (2.0,), interior)
                for matrix in result.values():
                    self.assertEqual(matrix.shape, (len(interior), len(interior)))
                    expected = np.zeros((0, 0)) if not interior else np.array([[1, -1], [-1, 1]])
                    assert_allclose(matrix, expected)

    def test_interior_order_and_graph_relabeling(self):
        vertices, edges, weights = ("p", "q", "r", "u"), (("p", "q"), ("q", "r"), ("r", "u")), (1.0, 2.0, 3.0)
        interior = ("q", "p", "r")
        original = boundary_operators(vertices, edges, weights, interior)
        permutation = [2, 0, 1]
        reordered = boundary_operators(vertices, edges, weights, tuple(interior[i] for i in permutation))
        names = {'p':'z', 'q':'x', 'r':'w', 'u':'y'}
        renamed = boundary_operators(
            tuple(names[v] for v in reversed(vertices)),
            tuple((names[right], names[left]) for left,right in reversed(edges)),
            tuple(reversed(weights)), tuple(names[v] for v in interior),
        )
        for key in ('dirichlet', 'induced'):
            assert_allclose(reordered[key], original[key][np.ix_(permutation, permutation)], atol=1e-12)
            assert_allclose(renamed[key], original[key], atol=1e-12)

    def test_main_case_spectra_and_weight_scaling(self):
        for name, case in BOUNDARY_CASES.items():
            with self.subTest(scenario=name):
                result = boundary_operators(case['vertices'], case['edges'], case['weights'], case['interior'])
                scaled = boundary_operators(case['vertices'], case['edges'], tuple(5*w for w in case['weights']), case['interior'])
                for key in ('dirichlet', 'induced'):
                    matrix = result[key]
                    assert_allclose(matrix, matrix.T, atol=1e-12)
                    assert_allclose(matrix, scaled[key], rtol=1e-10, atol=1e-12)
                    values, vectors = np.linalg.eigh(matrix)
                    self.assertTrue(np.all(values >= -1e-12))
                    self.assertTrue(np.all(values <= 2 + 1e-12))
                    assert_allclose(matrix @ vectors, vectors * values, rtol=1e-10, atol=1e-12)

    def test_invalid_interior_and_weights(self):
        cases = (
            ((1.0,), ("unknown",)), ((1.0,), ("p", "p")),
            ((), ("p",)), ((1.0, 2.0), ("p",)), ((0.0,), ("p",)),
            ((-1.0,), ("p",)), ((float('nan'),), ("p",)), ((float('inf'),), ("p",)),
        )
        for weights, interior in cases:
            with self.subTest(weights=weights, interior=interior):
                with self.assertRaises(ValueError):
                    boundary_operators(("p", "q"), (("p", "q"),), weights, interior)


class InputPreservationTests(unittest.TestCase):
    def test_inputs_unchanged(self):
        vertices, edges, weights = ("p", "q", "r"), (("p", "q"), ("q", "r")), (1.0, 2.0)
        left, right, interior = frozenset(('p',)), frozenset(('r',)), ("p", "q")
        for function, arguments in (
            (cut_discrepancy, (vertices, edges, 0.5, left, right)),
            (boundary_operators, (vertices, edges, weights, interior)),
        ):
            with self.subTest(function=function.__name__):
                before = (vertices[:], edges[:], weights[:], left, right, interior[:])
                function(*arguments)
                self.assertEqual((vertices, edges, weights, left, right, interior), before)


if __name__ == "__main__":
    unittest.main()
