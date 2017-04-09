import unittest

from array_left_rotation import array_left_rotation


class ArrayLeftRotationTest(unittest.TestCase):
    def test_array_left_rotation(self):
        self.assertEqual(
            array_left_rotation([1,2,3,4,5], 5, 4),
            [5, 1, 2, 3, 4]
        )


if __name__ == '__main__':
    unittest.main()
