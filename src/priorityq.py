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

    def __init__(self, iterable=None):
        """Construct a new priority queue."""
        self._values = BinHeap()
        self._min_priority = 0

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
