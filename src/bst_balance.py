"""Implements a self-balancing binary search tree."""
from bst import BST


class BalanceBST(BST):
    """Structure for values in a Self-Balancing Binary Search Tree.

    Each node has a maximum of two children, where the the left
    child is 'less' than the parent and the right child is 'greater'
    than the parent. Duplicate values cannot be added to the tree.
    Each time an item is added or removed from the tree, it is
    rebalanced such that the |balance| is no more than 1 at every node.
    """

    def insert(self, val):
        """Insert a new value into the Binary Search Tree.

        Duplicate values are ignored when inserted into the tree.
        """
        super(BalanceBST, self).insert(val)

    def delete(self, val):
        """Delete the given value from the tree."""
        super(BalanceBST, self).delete(val)

    def _balance(self):
        """."""

    def _rotate_right(self, node):
        """Rotate the node to the right down the tree."""
        pivot = node.left
        child = pivot.right
        parent = node.parent

        if parent:
            if parent.left == node:
                parent.left = pivot
            else:
                parent.right = pivot
        else:
            self.root = pivot
        pivot.parent = parent
        node.left, child.parent = child, node
        pivot.right, node.parent = node, pivot

    def _rotate_left(self, node):
        """Rotate the node to the right down the tree."""
        pivot = node.right
        child = pivot.left
        parent = node.parent

        if parent:
            if parent.left == node:
                parent.left = pivot
            else:
                parent.right = pivot
        else:
            self.root = pivot
        pivot.parent = parent
        node.right, child.parent = child, node
        pivot.left, node.parent = node, pivot

    def _find_depth(self, node, depth=-1):
        """Find the maximum depth from the given node."""
        if node is None:
            return depth

        left_depth = self._find_depth(node.left, depth + 1)
        right_depth = self._find_depth(node.right, depth + 1)
        return max(left_depth, right_depth)
