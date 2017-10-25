"""Implements a Stack."""


from linked_list import LinkedList


class Stack(object):
    """List of values stored in a stack."""

    def __init__(self, iterable=None):
        """Construct a Stack."""
        self._values = LinkedList(iterable)

    def __len__(self):
        """Overwrite the default return for len function."""
        return len(self._values)

    def pop(self):
        """Remove the top node and return it's value."""
        return self._values.pop()

    def push(self, val):
        """Add a value to the top of the stack."""
        self._values.push(val)
