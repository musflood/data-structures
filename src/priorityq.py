"""Implements a priority queue."""

from que_ import Queue
from binheap import BinHeap


class Bucket(object):
    """Priority bucket used in a Priority Queue."""

    def __init__(self, priority, iterable=None):
        """Create a new Bucket with given priority, filled using iterable."""
        self.priority = priority
        self._values = Queue(iterable)

    def __gt__(self, value):
        """Overwrite greater-than operator for comparing buckets."""
        if isinstance(value, Bucket):
            return self.priority > value.priority
        return self.priority > value

    def __eq__(self, value):
        """Overwrite equals operator for comparing buckets."""
        if isinstance(value, Bucket):
            return self.priority == value.priority
        return self.priority == value

    def __ne__(self, value):
        """Overwrite not equals operator for comparing buckets."""
        if isinstance(value, Bucket):
            return self.priority != value.priority
        return self.priority != value

    def __len__(self):
        """Overwrite len function to find length of a Bucket."""
        return len(self._values)


class PriorityQ(object):
    """Structure for values in a priorty queue.

    Items added to the priority queue are given a priority. If not set
    by the user, priority is set to be the lowest. When removing items,
    higher priority items are removed before lower priority items.
    """

    def __init__(self):
        """Construct a new priority queue."""
        self._values = BinHeap()
        self._min_priority = 0

    def __len__(self):
        """Overwrite length to give us the amount of items in priority Q.

        Get all the items from all the buckets in the priority Q.
        """
        return sum(len(b) for b in self._all_values[1:])

    @property
    def _all_values(self):
        return self._values._values

    @property
    def _size(self):
        return self._values._size

    def insert(self, val, priority=None):
        """Add a new value into the priority queue.

        If no priority is given, uses current lowest priority.
        """
        if priority is None:
            priority = self._min_priority

        if priority < self._min_priority:
            self._min_priority = priority

        try:
            i = self._all_values.index(priority)
            bucket = self._all_values[i]
            bucket._values.enqueue(val)

        except ValueError:
            self._values.push(Bucket(priority, [val]))

    def pop(self):
        """Remove the first value from priority Q.

        If no values in bucket then bucket is removed.
        """
        if len(self._all_values) < 2:
            raise IndexError('Can not pop from empty priority Q.')
        bucket = self._all_values[1]
        result = bucket._values.dequeue()
        if len(bucket._values) == 0:
            self._values.pop()
        return result

    def peek(self):
        """Get the the most important item without removing it."""
        if len(self._all_values) < 2:
            return
        bucket = self._all_values[1]
        return bucket._values.peek()
