import unittest

from stacks_balanced_brackets import is_matched


class StacksBalancedBracketsTest(unittest.TestCase):
    def test_is_matched(self):
        self.assertTrue(is_matched('{[()]}'))
        self.assertFalse(is_matched('{[(])}'))
        self.assertTrue(is_matched('{{[[(())]]}}'))
        self.assertTrue(is_matched('{}{}{{{}}{{}}}{}'))
        self.assertFalse(is_matched('}'))


if __name__ == '__main__':
    unittest.main()
