import unittest

from min_diff import min_diff


class MinDiffTests(unittest.TestCase):

    def test_one(self):
        self.assertEqual(min_diff(6, 3, [10, 20, 30, 100, 200, 300]), 20)

    def test_two(self):
        self.assertEqual(
            min_diff(7, 3, [100, 200, 300, 350, 400, 401, 402]),
            2)


if __name__ == '__main__':
    unittest.main()
