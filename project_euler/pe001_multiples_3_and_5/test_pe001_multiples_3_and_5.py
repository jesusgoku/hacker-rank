import unittest

from pe001_multiples_3_and_5 import sum_multiples_3_and_5


class TestPE001Multiples3And5(unittest.TestCase):
    def test_sum_multiples_3_and_5(self):
        self.assertEqual(sum_multiples_3_and_5(10), 23)
        self.assertEqual(sum_multiples_3_and_5(100), 2318)


if __name__ == '__main__':
    unittest.main()
