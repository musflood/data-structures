"""Implements a Binary Search Tree."""


class Node(object):
    """A node for a Binary Search Tree."""

    def __init__(self, val, left=None, right=None):
        """Instantiate a new node for a binary search tree."""
        self.val = val
        self.left = left
        self.right = right


class BST(object):
    """Structure for values in a Binary Search Tree.

    Each node has a maximum of two children, where the the left
    child is 'less' than the parent and the right child is 'greater'
    than the parent. Duplicate values cannot be added to the tree.
    """

    def __init__(self, iterable=None):
        """Instantiate a new Binary Search Tree, filled with an iterable."""
        self.root = None
        self.left_depth = 0
        self.right_depth = 0
