import unittest

from string_making_anagrams import number_needed


class StringMakingAnagramsTest(unittest.TestCase):
    def test_number_needed(self):
        self.assertEqual(number_needed('abc', 'cde'), 4)
        self.assertEqual(number_needed('hello', 'billion'), 6)
        self.assertEqual(number_needed('glue', 'legs'), 2)
        self.assertEqual(number_needed('candy', 'day'), 2)


if __name__ == '__main__':
    unittest.main()
