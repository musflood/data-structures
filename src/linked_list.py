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
        if itr:
            for item in itr:
                self.push(item)

    def __len__(self):
        """Overwrite the default return for len function."""
        return self.length

    def size(self):
        """."""
        return len(self)

    def push(self, val):
        """Add another value to the front of the list."""
        new_node = Node(val, self.head)
        self.head = new_node
        self.length += 1

    def pop(self):
        """."""
        if self.head is None:
            raise IndexError('Cannot pop from empty list.')
        val = self.head.val
        self.head = self.head.nxt
        self.length -= 1
        return val
