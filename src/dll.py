"""Implements a doubly-linked list."""
from linked_list import LinkedList


class Node(object):
    """A single node from a doubly-linked list."""

    def __init__(self, val, nxt=None, prev=None):
        """Construct a new Node."""
        self.val = val
        self.nxt = nxt
        self.prev = prev


class DLL(LinkedList):
    """List of values stored in nodes linked in two directions."""

    def __init__(self, iterable=None):
        """Construct a Doubly-Linked List (DLL)."""
        self.tail = None
        self.head = None
        self.length = 0
