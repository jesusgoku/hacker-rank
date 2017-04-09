import unittest

from hash_table_ransom_note import ransom_note


class HashTableRansomNoteTest(unittest.TestCase):
    def test_ransom_note(self):
        self.assertTrue(
            ransom_note(
                ['give', 'me', 'one', 'grand', 'today', 'night'],
                ['give', 'one', 'grand', 'today']
            ))
        self.assertFalse(ransom_note(
            ['o', 'l', 'x', 'imjaw', 'bee', 'khmla', 'v', 'o', 'v', 'o', 'imjaw', 'l', 'khmla', 'imjaw', 'x'],
            ['imjaw', 'l', 'khmla', 'x', 'imjaw', 'o', 'l', 'l', 'o', 'khmla', 'v', 'bee', 'o', 'o', 'imjaw', 'imjaw', 'o']
        ))
