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
        self._size = 0
        self.left_depth = 0
        self.right_depth = 0

        if isinstance(iterable, (str, list, tuple)):
            for item in iterable:
                self.insert(item)
        elif iterable is not None:
            raise TypeError('Iterable must be a str, list, or tuple.')

    def insert(self, val):
        """Insert a new value into the Binary Search Tree.

        Duplicate values are ignored when inserted into the tree.
        """
        if not self.root:
            self.root = Node(val)
            self._size += 1
            return

        left_branch = val < self.root.val

        curr = self.root
        depth = 0

        while curr:
            depth += 1

            if val < curr.val:
                if not curr.left:
                    curr.left = Node(val)
                    self._size += 1
                    break
                curr = curr.left

            elif val > curr.val:
                if not curr.right:
                    curr.right = Node(val)
                    self._size += 1
                    break
                curr = curr.right

            else:
                return

        if left_branch:
            self.left_depth = max(self.left_depth, depth)
        else:
            self.right_depth = max(self.right_depth, depth)

    def search(self, val):
        """Find the node that contains the given value.

        Returns None if value is not in the tree.
        """
        curr = self.root
        while curr:
            if val < curr.val:
                curr = curr.left
            elif val > curr.val:
                curr = curr.right
            else:
                return curr

    def size(self):
        """Get the size of the Binary Search Tree."""
        return self._size

    def depth(self):
        """Get the maximum depth of the Binary Search Tree.

        The depth is the number of levels in the tree. A tree with only
        one value has a depth of 0.
        """
        return max(self.right_depth, self.left_depth)

    def contains(self, val):
        """Check if a value is in the Binary Search Tree."""
        return bool(self.search(val))

    def balance(self):
        """Get the balance of the Binary Search Tree.

        balance > 0: Tree is deeper on the left than right
        balance < 0: Tree is deeper on the right than left
        balance == 0: Tree is balanced, with the same depth on left and right
        """
        return self.left_depth - self.right_depth


if __name__ == '__main__':  # pragma: no cover
    from timeit import timeit
    print("""-- Searching a Binary Search Tree --
    Best Case search for 7, O(log(n)):
                    4
                  /   \\
                 2     6
                / \\   / \\
               1   3 5   7""")
    setup = 'from bst import BST; tree = BST([4, 2, 6, 1, 3, 5, 7])'
    print('    {}ms'.format(timeit('tree.search(7)', setup)))
    print("""
    Worst Case search for 7, O(n):
                    1
                     \\
                      2
                       \\
                        3
                         \\
                          4
                           \\
                            5
                             \\
                              6
                               \\
                                7""")
    setup = 'from bst import BST; tree = BST([1, 2, 3, 4, 5, 6, 7])'
    print('    {}ms'.format(timeit('tree.search(7)', setup)))
