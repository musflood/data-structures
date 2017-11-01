"""Implements a max binary heap."""


class BinHeap(object):
    """Structure for values in a max binary heap.

    A max binary heap is a complete binary tree where each level of the
    tree is greater than the level below it.
    """

    def __init__(self, iterable=None):
        """Construct a new binary heap."""
        self._values = [None]
        if isinstance(iterable, (str, list, tuple)):
            for item in iterable:
                self.push(item)

    def push(self, val):
        """Put a new value into the binary heap."""
        if val in self._values:
            return

        self._values.append(val)

        i = len(self._values) - 1
        while self._pi(i) and self._values[self._pi(i)] < val:
            p = self._pi(i)
            self._values[p], self._values[i] = self._values[i], self._values[p]
            i = p

    def pop(self):
        """Remove lowest value from binary heap."""
        if len(self._values) < 2:
            raise IndexError('Can not pop from empty heap.')
        top = self._values[1]
        x = self._values[1] = self._values.pop()
        i = 1
        while self._lci(i) < len(self._values) and self._values[self._lci(i)] > x:
            if self._values[self._lci(i)] > self._values[self._rci(i)]:
                c = self._lci(i)
            else:
                c = self._rci(i)
            self._values[c], self._values[i] = self._values[i], self._values[c]
            i = c
        return top

    def _pi(self, idx):
        """Find the index for the parent of the given index."""
        return idx // 2

    def _lci(self, idx):
        """Find the index for the left child of the given index."""
        return idx * 2

    def _rci(self, idx):
        """Find the index for the right child of the given index."""
        return idx * 2 + 1
