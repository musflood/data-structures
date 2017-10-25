"""Implements a Stack."""


from linked_list import LinkedList


class Stack(object):
    """List of values stored in a stack."""

    def __init__(self, iterable=None):
        """Construct a Stack."""
        self._values = LinkedList(iterable)

    def pop(self):
        """Remove the first node and return it's value."""
        return self._values.pop()
