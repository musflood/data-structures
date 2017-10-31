"""Implements a max binary heap."""


class BinHeap(object):
    """Structure for values in a max binary heap.

    A max binary heap is a complete binary tree where each level of the
    tree is greater than the level below it.
    """

    def __init__(self):
        """Construct a new binary heap."""
        self._values = [None]

    def push(self, val):
        """Put a new value into the binary heap."""
        if val in self._values:
            return

        self._values.append(val)

        i = len(self._values) - 1
        while _pi(i) and self._values[_pi(i)] < val:
            self._values[_pi(i)], self._values[i] = self._values[i], self._values[_pi(i)]
            i = _pi(i)


def _pi(idx):
    """Find the index for the parent of the given index in a binheap."""
    return idx // 2


def _lci(idx):
    """Find the index for the left child of the given index in a binheap."""
    return idx * 2


def _rci(idx):
    """Find the index for the right child of the given index in a binheap."""
    return idx * 2 + 1
