"""Implements a deque."""

from dll import DLL


class Deque(object):
    """Structure for values in a deque."""

    def __init__(self, iterable=None):
        """Construct a ne deque."""
        self._values = DLL(iterable)

    @property
    def front(self):
        """Get the node at front of the deque."""
        return self._values.tail

    @property
    def end(self):
        """Get the node at end of the deque."""
        return self._values.head

    def append(self, val):
        """Add a value to the end of the deque."""
        self._values.push(val)

    def popleft(self):
        """Remove the value from the front of the deque and return it."""
        try:
            return self._values.shift()
        except IndexError:
            raise IndexError('Cannot popleft from empty deque.')
