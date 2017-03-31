import unittest

import diagonal_difference


class DiagonalDifferenceTest(unittest.TestCase):
    def setUp(self):
        self.a = (
            (11, 2, 4),
            (4, 5, 6),
            (10, 8, -12)
        )

    def test_diagonal_primary(self):
        self.assertEqual(
            diagonal_difference.diagonal_primary(self.a),
            [11, 5, -12])

    def test_diagonal_secondary(self):
        self.assertEqual(
            diagonal_difference.diagonal_secondary(self.a),
            [4, 5, 10])

    def test_diagonal_difference(self):
        self.assertEqual(
            diagonal_difference.diagonal_difference(self.a),
            -15)


if __name__ == '__main__':
    unittest.main()
