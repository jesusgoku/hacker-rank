#!/usr/bin/env python


class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node


class LinkedList(object):
    head = None

    def append(self, data):
        new_node = Node(data)

        if None == self.head:
            self.head = new_node
            return self

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

        return self

    def append_node(self, node):
        if not self.head:
            self.head = node
            return self

        current = self.head
        while current.next:
            current = current.next
        current.next = node

        return self


def has_cycle_v1(head):
    if not head:
        return False

    current = head
    register = [current]
    while current:
        if current in register:
            return True
        current = current.next
        register.append(current)
    return False


def has_cycle_v2(head):
    fast = head
    while fast != None and fast.next != None:
        fast = fast.next.next
        head = head.next
        if head == fast:
            return True
    return False


has_cycle = has_cycle_v2
