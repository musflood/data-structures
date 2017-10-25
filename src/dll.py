"""Implements a doubly-linked list."""
import linked_list


class Node(linked_list.Node):
    """A single node from a doubly-linked list."""

    def __init__(self, val, nxt=None, prev=None):
        """Construct a new Node."""
        super(Node, self).__init__(val, nxt)
        self.prev = prev


class DLL(linked_list.LinkedList):
    """List of values stored in nodes linked in two directions."""

    def __init__(self, iterable=None):
        """Construct a Doubly-Linked List (DLL)."""
        self.tail = None
        super(DLL, self).__init__(iterable)

    def push(self, val):
        """Insert the value val at the head of the list."""
        pass

    def append(self, val):
        """Append the value val at the tail of the list."""
        pass

    def pop(self, ):
        """Pop the first value off the head of the list and return it."""
        pass

    def shift(self, ):
        """Remove the last value from the tail of the list and return it."""
        pass

    def remove(self, val):
        """Remove the first instance of val found in the list, starts at head.

        Raises a ValueError if value is not in the list.
        """
        pass
