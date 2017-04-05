import unittest

from is_circle_word import is_circle_word


class IsCircleWordTest(unittest.TestCase):
    def test_is_circle_word(self):
        self.assertTrue(is_circle_word('jesus', 'jesus'))
        self.assertTrue(is_circle_word('jesus', 'susje'))
        self.assertFalse(is_circle_word('jesus', 'jes'))
        self.assertFalse(is_circle_word('jesus', 'abcde'))


if __name__ =='__main__':
    unittest.main()
