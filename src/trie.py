"""Implements a Trie tree."""


class Node(object):
    """Node for a Trie tree."""

    def __init__(self, value, parent=None):
        """Create a node with the given value."""
        self.val = value
        self.parent = parent
        self.children = {}


class Trie(object):
    """Structure for values in a Trie tree.

    Stores strings as individual character nodes. Each string
    starts with a '*' node and ends with a '$' node. Only characters
    that are not in the tree in the string order are added to the tree.
    When characters different from those already in the tree are added,
    a new branch is added at the node where the difference occurs.
    """

    def __init__(self, iterable=None):
        """Create an empty Trie tree."""
        self.root = Node('*')
        self._size = 0

        if isinstance(iterable, (list, tuple)):
            for item in iterable:
                self.insert(item)
        elif iterable is not None:
            raise TypeError('Iterable must be a list, or tuple.')

    def insert(self, string):
        """Insert the given string into the Trie tree.

        Duplicate characters are ignored.
        """
        if not isinstance(string, str):
            raise TypeError('Can only insert strings into the trie.')

        curr = self.root
        for ch in string:
            curr.children.setdefault(ch, Node(ch, curr))
            curr = curr.children[ch]

        new_end = Node('$', curr)
        set_end = curr.children.setdefault('$', new_end)
        if set_end is new_end:
            self._size += 1

    def contains(self, string):
        """Check if the given string is in the Trie tree."""
        if not isinstance(string, str):
            raise TypeError('Can only check for strings in the trie.')

        curr = self.root
        for ch in string + '$':
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return True

    def size(self):
        """Get that number of strings in the Trie tree."""
        return self._size

    def remove(self, string):
        """Remove the given string from the Trie tree."""
        if not isinstance(string, str):
            raise TypeError('Can only remove strings from the trie.')

        curr = self.root
        for ch in string + '$':
            if ch not in curr.children:
                raise ValueError('The string is not in the trie.')
            curr = curr.children[ch]

        curr = curr.parent
        last_ch = '$'
        while len(curr.children) == 1 and curr.val != '*':
            last_ch = curr.val
            curr = curr.parent

        del curr.children[last_ch]
        self._size -= 1
