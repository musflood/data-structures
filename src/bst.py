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
        self.size = 0
        self.left_depth = 0
        self.right_depth = 0

    def insert(self, val):
        """Insert a new value into the Binary Search Tree.

        Duplicate values are ignored when inserted into the tree.
        """
        if not self.root:
            self.root = Node(val)
            self.size += 1
            return

        left_branch = val < self.root.val

        curr = self.root
        depth = 0

        while curr:
            depth += 1

            if val < curr.val:
                if not curr.left:
                    curr.left = Node(val)
                    self.size += 1
                    break
                curr = curr.left

            elif val > curr.val:
                if not curr.right:
                    curr.right = Node(val)
                    self.size += 1
                    break
                curr = curr.right

            else:
                return

        if left_branch:
            self.left_depth = max(self.left_depth, depth)
        else:
            self.right_depth = max(self.right_depth, depth)
