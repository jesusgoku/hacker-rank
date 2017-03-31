import unittest

from time_conversion import time_conversion


class TimeConversionTest(unittest.TestCase):
    def test_time_conversion(self):
        self.assertEqual(
            time_conversion('07:05:45PM'),
            '19:05:45')
        self.assertEqual(
            time_conversion('12:45:54PM'),
            '12:45:54')
        self.assertEqual(
            time_conversion('00:00:00PM'),
            '12:00:00')


if __name__ == '__main__':
    unittest.main()
