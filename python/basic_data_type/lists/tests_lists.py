import unittest

import lists


class ListTests(unittest.TestCase):
    def setUp(self):
        self.l = []

    def test_insert(self):
        lists.linsert(self.l, 0, 5)
        self.assertEqual(self.l, [5])

        lists.linsert(self.l, 1, 10)
        self.assertEqual(self.l, [5, 10])

        lists.linsert(self.l, 0, 6)
        self.assertEqual(self.l, [6, 5, 10])

        lists.lremove(self.l, 6)
        self.assertEqual(self.l, [5, 10])

        lists.lappend(self.l, 9)
        self.assertEqual(self.l, [5, 10, 9])

        lists.lappend(self.l, 1)
        self.assertEqual(self.l, [5, 10, 9, 1])

        lists.lsort(self.l)
        self.assertEqual(self.l, [1, 5, 9, 10])

        lists.lpop(self.l)
        self.assertEqual(self.l, [1, 5, 9])

        lists.lreverse(self.l)
        self.assertEqual(self.l, [9, 5, 1])


if __name__ == '__main__':
    unittest.main()
