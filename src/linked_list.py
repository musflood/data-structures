"""Implements a linked list."""


class Node(object):
    """."""

    def __init__(self, val, nxt=None):
        """."""
        self.val = val
        self.nxt = nxt


class LinkedList(object):
    """."""

    def __init__(self, itr=None):
        """."""
        self.head = None
        self.length = 0

    def push(self, val):
        """Add another value to the front of the list."""
        new_node = Node(val, self.head)
        self.head = new_node
        self.length += 1
