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

        i = self._size
        while self._pi(i) and self._values[self._pi(i)] < val:
            p = self._pi(i)
            self._values[p], self._values[i] = self._values[i], self._values[p]
            i = p

    def pop(self):
        """Remove top from the binary heap."""
        if len(self._values) < 2:
            raise IndexError('Can not pop from empty heap.')

        if len(self._values) == 2:
            return self._values.pop()

        top = self._values[1]
        x = self._values[1] = self._values.pop()

        i = 1
        lc = self._values[self._lci(i):self._lci(i) + 1]
        rc = self._values[self._rci(i):self._rci(i) + 1]

        while (lc and lc[0] > x) or (rc and rc[0] > x):

            if rc and rc[0] > lc[0]:
                c = self._rci(i)
            else:
                c = self._lci(i)

            self._values[c], self._values[i] = self._values[i], self._values[c]

            i = c
            lc = self._values[self._lci(i):self._lci(i) + 1]
            rc = self._values[self._rci(i):self._rci(i) + 1]

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

    @property
    def _size(self):
        """Get the number of items in the binary heap."""
        return len(self._values) - 1
