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
