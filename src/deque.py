"""Implements a deque."""

from dll import DLL


class Deque(object):
    """Structure for values in a deque, a double-ended queue."""

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

    def appendleft(self, val):
        """Add a value to the front of the deque."""
        self._values.append(val)

    def pop(self):
        """Remove the value from the end of the deque and return it."""
        try:
            return self._values.pop()
        except IndexError:
            raise IndexError('Cannot pop from empty deque.')

    def popleft(self):
        """Remove the value from the front of the deque and return it."""
        try:
            return self._values.shift()
        except IndexError:
            raise IndexError('Cannot popleft from empty deque.')

    def peek(self):
        """Get the value from the front of the deque without removing it."""
        if self.end:
            return self.end.val

    def size(self):
        """Get the size of the deque."""
        return len(self)
