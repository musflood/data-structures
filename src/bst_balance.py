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

        curr = self.search(val).parent
        rebalanced = False
        while curr:
            if self._rebalance(curr):
                rebalanced = True
            curr = curr.parent

        if rebalanced:
            self.right_depth = self._find_depth(self.root.right) + 1
            self.left_depth = self._find_depth(self.root.left) + 1

    def delete(self, val):
        """Delete the given value from the tree."""
        curr = self.search(val).parent

        super(BalanceBST, self).delete(val)

        rebalanced = False
        while curr:
            if self._rebalance(curr):
                rebalanced = True
            curr = curr.parent

        if rebalanced:
            self.right_depth = self._find_depth(self.root.right) + 1
            self.left_depth = self._find_depth(self.root.left) + 1

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
        node.left = child
        if child:
            child.parent = node
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
        node.right = child
        if child:
            child.parent = node
        pivot.left, node.parent = node, pivot

    def _rebalance(self, node):
        """Rebalance the node if it is out of balance.

        Returns whether or not a rebalance occured.
        """
        balance = self._find_depth(node.left) - self._find_depth(node.right)
        if abs(balance) <= 1:
            return False
        if balance > 0:  # left cases
            child = node.left
            child_balance = self._find_depth(child.left) - self._find_depth(child.right)
            if child_balance < 0:  # left-right case
                self._rotate_left(child)
            self._rotate_right(node)
        else:  # right cases
            child = node.right
            child_balance = self._find_depth(child.left) - self._find_depth(child.right)
            if child_balance > 0:  # right-left case
                self._rotate_right(child)
            self._rotate_left(node)
        return True

    def _find_depth(self, node, depth=-1):
        """Find the maximum depth from the given node."""
        if node is None:
            return depth

        left_depth = self._find_depth(node.left, depth + 1)
        right_depth = self._find_depth(node.right, depth + 1)
        return max(left_depth, right_depth)
