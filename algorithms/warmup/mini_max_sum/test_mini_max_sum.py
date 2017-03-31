import unittest

from mini_max_sum import mini_max_sum


class MiniMaxSumTest(unittest.TestCase):
    def test_mini_max_sum(self):
        self.assertEqual(
            mini_max_sum([1, 2, 3, 4, 5]),
            (10, 14))


if __name__ == '__main__':
    unittest.main()
