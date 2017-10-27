"""Implements queue."""


from dll import DLL


class Queue(object):
    """Creates a queue."""

    def __init__(self, iterable=None):
        """Construct a new queue."""
        self._values = DLL(iterable)

    def enqueue(self, val):
        """Add a value to the end of the queue."""
        self._values.push(val)

    def dequeue(self):
        """Remove the value from the front of the queue."""
        try:
            return self._values.shift()
        except IndexError:
            raise IndexError('Cannot dequeue from empty queue.')

    def peek(self):
        """Get the value from the front of the queue without removing it."""
        if self.front:
            return self.front.val
        return None

    @property
    def front(self):
        """Get the node at front of the queue."""
        return self._values.tail

    @property
    def back(self):
        """Get the node at back of the queue."""
        return self._values.head
