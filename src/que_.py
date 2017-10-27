"""Implements queue."""


from dll import DLL


class Queue(object):
    """Creates a queue."""

    def __init__(self, iterable=None):
        """Construct a new queue."""
        self._values = DLL(iterable)

    def enqueue(self, val):
        """Add a value to the queue."""
        self._values.push(val)
