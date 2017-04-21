#!/usr/bin/env python


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_ordered(l):
    return all([l[i] < l[i + 1] for i in xrange(len(l) - 1)])


def process_in_order(root, func):
    if root != None:
        process_in_order(root.left, func)
        func(root.data)
        process_in_order(root.right, func)


def make_list(l):
    def append_to_list(data):
        l.append(data)
    return append_to_list

def check_binary_search_tree_(root):
    l = []
    process_in_order(root, make_list(l))
    return is_ordered(l)


if __name__ == '__main__':
    
