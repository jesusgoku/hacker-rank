import unittest

from queues_a_tale_of_two_stacks import MyQueue


class QueuesATaleOfTwoStacksTest(unittest.TestCase):
    def setUp(self):
        self.queue = MyQueue()

    def test_queue(self):
        self.assertRaises(Exception, self.queue.peek)
        self.queue.put(10)
        self.assertEqual(self.queue.peek(), 10)
        self.queue.put(20)
        self.assertEqual(self.queue.peek(), 10)
        self.queue.put(30)
        self.assertEqual(self.queue.pop(), 10)
        self.assertEqual(self.queue.pop(), 20)
        self.assertEqual(self.queue.pop(), 30)
        self.assertRaises(Exception, self.queue.peek)


if __name__ == '__main__':
    unittest.main()
