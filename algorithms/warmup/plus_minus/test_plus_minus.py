import unittest

import plus_minus


class PlusMinusTest(unittest.TestCase):
    def setUp(self):
        self.a = (-4, 3, -9, 0, 4, 1)

    def test_positives(self):
        self.assertEqual(
            plus_minus.positives(self.a),
            (3, 4, 1))

    def test_negatives(self):
        self.assertEqual(
            plus_minus.negatives(self.a),
            (-4, -9))

    def test_zeros(self):
        self.assertEqual(
            plus_minus.zeros(self.a),
            (0, ))

    def test_count_plus_minus(self):
        self.assertEqual(
            plus_minus.count_plus_minus(self.a),
            (3, 2, 1))

    def test_percet_plus_minus(self):
        self.assertEqual(
            '%.3f %.3f %.3f' % plus_minus.percent_plus_minus(
                *plus_minus.count_plus_minus(self.a)),
            '0.500 0.333 0.167')

if __name__ == '__main__':
    unittest.main()
