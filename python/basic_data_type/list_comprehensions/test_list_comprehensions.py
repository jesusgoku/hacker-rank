import unittest

import list_comprehensions


class ListComprehensionsTest(unittest.TestCase):
    def test_list_comprehensions(self):
        self.assertEqual(
            list_comprehensions.list_comprehensions(1, 1, 1, 2),
            [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]])


if __name__ == '__main__':
    unittest.main()
