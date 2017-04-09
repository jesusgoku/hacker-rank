import unittest

from linked_lists_detect_a_cycle import has_cycle
from linked_lists_detect_a_cycle import Node, LinkedList


class TestLinkedListsDetectACycle(unittest.TestCase):
    def setUp(self):
        ll = LinkedList()
        ll.append(1).append(2).append(3)
        self.linkedListWithoutCycle = ll

        ll = LinkedList()
        ll.append(1).append(2).append(3).append_node(ll.head)
        self.linkedListWithCycle = ll

    def test_has_cycle(self):
        self.assertFalse(has_cycle(self.linkedListWithoutCycle.head))
        self.assertTrue(has_cycle(self.linkedListWithCycle.head))
