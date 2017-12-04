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
    When additional characters from those in the tree are added,
    a new branch is added at the node where the difference occurs.
    """

    def __init__(self):
        """Create an empty Trie tree."""
        self.root = Node('*')
