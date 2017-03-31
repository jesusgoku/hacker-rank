import unittest

from iid_array_ds import get_max_sandclock


class IIDArrayDsTest(unittest.TestCase):
    def test_get_max_sandclock(self):
        self.assertEqual(
            get_max_sandclock([
                [1, 1, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [0, 0, 2, 4, 4, 0],
                [0, 0, 0, 2, 0, 0],
                [0, 0, 1, 2, 4, 0]
            ]),
            19)


if __name__ == '__main__':
    unittest.main()
