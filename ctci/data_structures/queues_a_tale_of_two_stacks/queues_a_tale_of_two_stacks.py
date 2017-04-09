#!/usr/bin/env python


class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []

    def peek(self):
        if 0 == len(self.first):
            raise Exception('Queue is empty.')

        return self.first[0]

    def pop(self):
        temp = self.first[0]
        del self.first[0]
        return temp

    def put(self, value):
        self.first.append(value)


if __name__ == '__main__':
    queue = MyQueue()
    t = int(raw_input())
    for line in xrange(t):
        values = map(int, raw_input().strip().split())

        if values[0] == 1:
            queue.put(values[1])
        elif values[0] == 2:
            queue.pop()
        else:
            print queue.peek()
