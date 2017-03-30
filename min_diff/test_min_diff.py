import unittest

from min_diff import min_diff
from min_diff import min_diff_v1
from min_diff import min_diff_v2


class MinDiffTests(unittest.TestCase):

    def test_case_one(self):
        self.assertEqual(min_diff(6, 3, [10, 20, 30, 100, 200, 300]), 20)

    def test_case_two(self):
        self.assertEqual(
            min_diff(7, 3, [100, 200, 300, 350, 400, 401, 402]),
            2)

    def test_versions(self):
        self.assertEqual(
            min_diff_v1(7, 3, [100, 200, 300, 350, 400, 401, 402]),
            min_diff_v2(7, 3, [100, 200, 300, 350, 400, 401, 402])
        )


if __name__ == '__main__':
    unittest.main()
