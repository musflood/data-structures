"""Implements a Binary Search Tree."""


class Node(object):
    """A node for a Binary Search Tree."""

    def __init__(self, val, left=None, right=None, parent=None):
        """Instantiate a new node for a binary search tree."""
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


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

    # def __str__(self):
    #     """String representation of the tree."""
    #     if not self.root:
    #         return ''

    #     row = [self.root]
    #     rows = []
    #     vals = []
    #     while any(row):
    #         rows.append(row)
    #         next_row = []
    #         for node in row:
    #             if node:
    #                 vals.append(node.val)
    #                 if node.left:
    #                     next_row.append(node.left)
    #                 else:
    #                     next_row.append(None)
    #                 if node.right:
    #                     next_row.append(node.right)
    #                 else:
    #                     next_row.append(None)
    #             else:
    #                 next_row.append(None)
    #                 next_row.append(None)
    #         row = next_row

    #     max_row_width = len(rows[-1])
    #     max_num_width = len(str(max(vals, key=lambda n: len(str(n)))))
    #     tree_width = max_row_width * (max_num_width * 2) - max_num_width
    #     num_spaces = tree_width

    #     string_tree = []
    #     for i, row in enumerate(rows):
    #         if i:
    #             num_spaces = (num_spaces - max_num_width) // 2
    #         space = ' ' * num_spaces
    #         nodes = [node.val if node else ' ' for node in row]
    #         string_row = space.join('{:^{}}'.format(n, max_num_width) for n in nodes)
    #         string_tree.append('{:^{}}'.format(string_row, tree_width))

    #     return '\n'.join(string_tree)

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
                    curr.left = Node(val, parent=curr)
                    self._size += 1
                    break
                curr = curr.left

            elif val > curr.val:
                if not curr.right:
                    curr.right = Node(val, parent=curr)
                    self._size += 1
                    break
                curr = curr.right

            else:
                return

        if left_branch:
            self.left_depth = max(self.left_depth, depth)
        else:
            self.right_depth = max(self.right_depth, depth)

    def delete(self, val):
        """Delete the given value from the tree."""
        deleted = self.search(val)

        if not deleted:  # val not in tree
            return

        if not deleted.left and not deleted.right:  # leaf val
            replacement = None

        elif not deleted.left:  # val has only right child
            replacement = deleted.right

        elif not deleted.right:  # val has only left child
            replacement = deleted.left

        else:  # val has two children
            curr = deleted.left  # get rightmost left child
            while curr.right:
                curr = curr.right
            replacement = curr

            self.delete(curr.val)
            self._size += 1  # going to add the replacement back in

            if deleted.left != replacement:
                replacement.left = deleted.left
                if replacement.left:
                    replacement.left.parent = replacement
            if deleted.right != replacement:
                replacement.right = deleted.right
                if replacement.right:
                    replacement.right.parent = replacement

        parent = deleted.parent
        if not parent:
            self.root = replacement
        elif parent.left == deleted:
            parent.left = replacement
        elif parent.right == deleted:
            parent.right = replacement

        if replacement:
            replacement.parent = parent

        self._size -= 1

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

    def in_order(self):
        """Get an in-order traversal generator of the tree.

        In-order gets values from the tree by traversing the left branch,
        root, then right branch.
        """
        def traverse(node):
            if node:
                for val in traverse(node.left):
                    yield val
                yield node.val
                for val in traverse(node.right):
                    yield val

        return traverse(self.root)

    def pre_order(self):
        """Get an pre-order traversal generator of the tree.

        Pre-order gets values from the tree by traversing the root,
        left branch, then right branch.
        """
        def traverse(node):
            if node:
                yield node.val
                for val in traverse(node.left):
                    yield val
                for val in traverse(node.right):
                    yield val

        return traverse(self.root)

    def post_order(self):
        """Get an post-order traversal generator of the tree.

        Post-order gets values from the tree by traversing the left branch,
        right branch, then root.
        """
        def traverse(node):
            if node:
                for val in traverse(node.left):
                    yield val
                for val in traverse(node.right):
                    yield val
                yield node.val

        return traverse(self.root)

    def breadth_first(self):
        """Get an breadth-first traversal generator of the tree.

        Breadth-first gets values from the tree by stepping down through
        the layers of the tree.
        """
        if not self.root:
            return

        row = [self.root]
        while row:
            next_row = []

            for node in row:
                yield node.val

                if node.left:
                    next_row.append(node.left)
                if node.right:
                    next_row.append(node.right)

            row = next_row


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
