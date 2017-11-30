"""Tests for the bst module."""

import pytest
from random import randint


def test_node_constructor_with_no_children():
    """Test that there is a node that has None for both children."""
    from bst import Node
    n = Node(0)
    assert n.val == 0
    assert n.left is None
    assert n.right is None


def test_node_constructor_with_left_child():
    """Test that there is a node that has another node as a left child."""
    from bst import Node
    n = Node(0, left=Node(1))
    assert n.val == 0
    assert isinstance(n.left, Node)
    assert n.right is None


def test_node_constructor_with_right_child():
    """Test that there is a node that has another node as a right child."""
    from bst import Node
    n = Node(0, right=Node(1))
    assert n.val == 0
    assert isinstance(n.right, Node)
    assert n.left is None


def test_node_constructor_with_both_children():
    """Test that there is a node that has nodes for children."""
    from bst import Node
    n = Node(0, left=Node(1), right=Node(2))
    assert n.val == 0
    assert isinstance(n.left, Node)
    assert isinstance(n.right, Node)


def test_bst_constructor_with_no_iterable():
    """Test that tree constructed with no arguments is empty."""
    from bst import BST
    t = BST()
    assert t.root is None


@pytest.mark.parametrize('itr', [[randint(-10, 10) for x in range(y)]
                                 for y in range(1, 20)])
def test_bst_constructed_with_iterable_is_filled_properly(itr):
    """Test that new tree constructed with an iterable is filled."""
    from bst import BST
    t = BST(itr)
    assert t._size == len(set(itr))
    assert t.root.val == itr[0]


@pytest.mark.parametrize('itr', [{1: 2, 2: 3}, 400, set([4, 2, 3, 5, 2])])
def test_bst_constructed_with_invalid_iterable_raises_error(itr):
    """Test that new tree constructed invalid iterable raises TypeError."""
    from bst import BST
    with pytest.raises(TypeError):
        BST(itr)


def test_insert_first_val_set_as_root(empty_bst):
    """Test that the first value inserted into the tree becomes the root."""
    from bst import Node
    t = empty_bst
    t.insert(5)
    assert isinstance(t.root, Node)
    assert t.root.val == 5
    assert t.root.left is None
    assert t.root.right is None


def test_insert_second_smaller_val_set_as_left_child(empty_bst):
    """Test that when the second val is less that root it is set as left."""
    from bst import Node
    t = empty_bst
    t.insert(5)
    t.insert(1)
    assert t.root.val == 5
    assert isinstance(t.root.left, Node)
    assert t.root.left.val == 1
    assert t.root.right is None


def test_insert_second_larger_val_set_as_right_child(empty_bst):
    """Test that when the second val is more that root it is set as right."""
    from bst import Node
    t = empty_bst
    t.insert(5)
    t.insert(10)
    assert t.root.val == 5
    assert isinstance(t.root.right, Node)
    assert t.root.right.val == 10
    assert t.root.left is None


@pytest.mark.parametrize('values', [[1, 2, 3], [3, 2, 1], [5, 2, 3, 7, 1],
                                    [72, 42, 54, 87, 3, 25],
                                    [2, 8, 4, 6, 1, 6, 9, 52, 4, 8, 9, 52, 9]])
def test_insert_multiple_values_correctly_placed(values):
    """Test that multiple values are inserted into correct place."""
    from bst import BST
    t = BST()
    for n in values:
        t.insert(n)
    curr = t.root
    while curr:
        if curr.left:
            assert curr.left.val < curr.val
        if curr.right:
            assert curr.right.val > curr.val
        curr = curr.left
    curr = t.root.right
    while curr:
        if curr.left:
            assert curr.left.val < curr.val
        if curr.right:
            assert curr.right.val > curr.val
        curr = curr.right


TREES = [
    [8], [1, 3], [3, 1], [1, 2, 3], [3, 2, 1], [2, 1, 3], [5, 2, 3, 7, 1, 8],
    [72, 42, 54, 87, 3, 25], [2, 8, 4, 6, 1, 6, 9, 52, 4, 8, 9, 52, 9],
    [57, 20, 17, 86, 23, 12, 100, 45, 49, 26, -2, 89, 53, 52, 15, 13, 87, 75]
]


@pytest.mark.parametrize('values', TREES)
def test_insert_multiple_values_increases_size(values):
    """Test that multiple values are inserted increments the size."""
    from bst import BST
    t = BST()
    for n in values:
        t.insert(n)

    assert t._size == len(set(values))


LDEPTH = [
    0, 0, 1, 0, 2, 1, 2,
    3, 1,
    6
]

RDEPTH = [
    0, 1, 0, 2, 0, 1, 2,
    1, 3,
    4
]


@pytest.mark.parametrize('values, l_depth, r_depth',
                         zip(TREES, LDEPTH, RDEPTH))
def test_insert_multiple_values_increases_depth(values, l_depth, r_depth):
    """Test that multiple values are inserted increments the depth."""
    from bst import BST
    t = BST()
    for n in values:
        t.insert(n)

    assert t.left_depth == l_depth
    assert t.right_depth == r_depth


def test_delete_val_from_empty_tree_does_nothing(empty_bst):
    """Test that deleting a val from an empty tree does nothing."""
    empty_bst.delete('6')
    assert empty_bst.size() == 0
    assert empty_bst.root is None


def test_delete_only_val_from_tree_empties_tree(empty_bst):
    """Test that deleting the only value from the tree empties the tree."""
    t = empty_bst
    t.insert(2)
    t.delete(2)
    assert t.size() == 0
    assert t.root is None


def test_delete_val_not_in_the_tree_does_nothing(filled_bst):
    """Test that deleting a val not in the tree does nothing."""
    filled_bst.delete(0)
    assert filled_bst.size() == 20
    order = [x for x in filled_bst.pre_order()]
    assert order == [57, 20, 17, 12, -2, 15, 13, 23, 45, 26,
                     30, 49, 53, 52, 54, 86, 75, 100, 89, 87]


def test_delete_leaf_val_from_the_tree_removed_correctly(filled_bst):
    """Test deleting a leaf val from the tree works."""
    filled_bst.delete(-2)
    assert filled_bst.size() == 19
    order = [x for x in filled_bst.pre_order()]
    assert order == [57, 20, 17, 12, 15, 13, 23, 45, 26,
                     30, 49, 53, 52, 54, 86, 75, 100, 89, 87]


def test_delete_branch_val_with_left_child_leaf_removed_correctly(filled_bst):
    """Test deleting a branch val with leaf left child from the tree works."""
    filled_bst.delete(15)
    assert filled_bst.size() == 19
    order = [x for x in filled_bst.pre_order()]
    assert order == [57, 20, 17, 12, -2, 13, 23, 45, 26,
                     30, 49, 53, 52, 54, 86, 75, 100, 89, 87]


def test_delete_branch_val_with_right_child_leaf_removed_correctly(filled_bst):
    """Test deleting a branch val with leaf right child from the tree works."""
    filled_bst.delete(26)
    assert filled_bst.size() == 19
    order = [x for x in filled_bst.pre_order()]
    assert order == [57, 20, 17, 12, -2, 15, 13, 23, 45,
                     30, 49, 53, 52, 54, 86, 75, 100, 89, 87]


def test_delete_branch_val_with_left_child_branch_removed_correctly(filled_bst):
    """Test deleting a branch val with branch left child from the tree works."""
    filled_bst.delete(17)
    assert filled_bst.size() == 19
    order = [x for x in filled_bst.pre_order()]
    assert order == [57, 20, 12, -2, 15, 13, 23, 45, 26,
                     30, 49, 53, 52, 54, 86, 75, 100, 89, 87]


def test_delete_branch_val_with_right_child_branch_removed_correctly(filled_bst):
    """Test deleting a branch val with branch right child from the tree works."""
    filled_bst.delete(23)
    assert filled_bst.size() == 19
    order = [x for x in filled_bst.pre_order()]
    assert order == [57, 20, 17, 12, -2, 15, 13, 45, 26,
                     30, 49, 53, 52, 54, 86, 75, 100, 89, 87]


def test_delete_branch_val_with_both_children_leaf_removed_correctly(filled_bst):
    """Test deleting a branch val with both children leaves from the tree works."""
    filled_bst.delete(53)
    assert filled_bst.size() == 19
    order = [x for x in filled_bst.pre_order()]
    assert order == [57, 20, 17, 12, -2, 15, 13, 23, 45, 26,
                     30, 49, 52, 54, 86, 75, 100, 89, 87]


def test_delete_branch_val_with_left_leaf_right_branch(filled_bst):
    """Test deleting a branch val with two children from the tree.

    Left child is a leaf and right child is a branch.
    When deleted, will be replaced with the left leaf.
    """
    filled_bst.delete(86)
    assert filled_bst.size() == 19
    order = [x for x in filled_bst.pre_order()]
    assert order == [57, 20, 17, 12, -2, 15, 13, 23, 45, 26,
                     30, 49, 53, 52, 54, 75, 100, 89, 87]


def test_delete_branch_val_with_right_leaf_left_branch_rightmost_is_leaf(filled_bst):
    """Test deleting a branch val with two children from the tree.

    Right child is a leaf and left child is a branch.
    When deleted, will be replaced with rightmost child of
    the left branch, which is a leaf.
    """
    filled_bst.delete()
    assert filled_bst.size() == 19
    order = [x for x in filled_bst.pre_order()]
    assert order == [57, 20, 17, 12, -2, 15, 13, 23, 45, 26,
                     30, 49, 53, 52, 54, 86, 75, 100, 89, 87]


def test_delete_branch_val_with_right_leaf_left_branch_rightmost_is_branch(filled_bst):
    """Test deleting a branch val with two children from the tree.

    Right child is a leaf and left child is a branch.
    When deleted, will be replaced with rightmost child of
    the left branch, which is a branch.
    """
    filled_bst.delete()
    assert filled_bst.size() == 19
    order = [x for x in filled_bst.pre_order()]
    assert order == [57, 20, 17, 12, -2, 15, 13, 23, 45, 26,
                     30, 49, 53, 52, 54, 86, 75, 100, 89, 87]


def test_delete_branch_val_with_both_children_branch_rightmost_is_leaf(filled_bst):
    """Test deleting a branch val with both children branches from the tree.

    When deleted, will be replaced with rightmost child of
    the left branch, which is a leaf.
    """
    filled_bst.delete(45)
    assert filled_bst.size() == 19
    order = [x for x in filled_bst.pre_order()]
    assert order == [57, 20, 17, 12, -2, 15, 13, 23, 30, 26,
                     49, 53, 52, 54, 86, 75, 100, 89, 87]


def test_delete_branch_val_with_both_children_branch_rightmost_is_branch(filled_bst):
    """Test deleting a branch val with both children branches from the tree.

    When deleted, will be replaced with rightmost child of
    the left branch, which is a branch with only a right child.
    """
    filled_bst.delete(20)
    assert filled_bst.size() == 19
    order = [x for x in filled_bst.pre_order()]
    assert order == [57, 17, 12, -2, 15, 13, 23, 45, 26,
                     30, 49, 53, 52, 54, 86, 75, 100, 89, 87]


def test_delete_root_val_reassigns_the_root(filled_bst):
    """Test deleting the root val works and reassigns the root."""
    filled_bst.delete(57)
    assert filled_bst.root.val == 54

    order = [x for x in filled_bst.pre_order()]
    assert order == [54, 20, 17, 12, -2, 15, 13, 23, 45, 26,
                     30, 49, 53, 52, 86, 75, 100, 89, 87]


def test_delete_root_repeatedly_removes_all_nodes_from_tree(filled_bst):
    """Test that all nodes can be removed from the tree."""
    t = filled_bst
    removed = []
    while t.root:
        removed.append(t.root.val)
        t.delete(t.root.val)

    order = [57, 54, 53, 52, 49, 45, 30, 26, 23, 20,
             17, 15, 13, 12, -2, 86, 75, 100, 89, 87]

    assert len(removed) == len(order)
    assert removed == order


def test_search_for_val_not_in_tree_is_none(filled_bst):
    """Test that searching for value not in tree returns None."""
    assert filled_bst.search(-10) is None


def test_search_for_root_val_finds_node(filled_bst):
    """Test that searching for value at the root of the tree returns node."""
    n = filled_bst.search(57)
    assert n == filled_bst.root


def test_search_for_inner_val_finds_node(filled_bst):
    """Test that searching for value inside the tree returns node."""
    n = filled_bst.search(45)
    assert n.val == 45
    assert n.left.val == 26
    assert n.right.val == 49


def test_search_for_leaf_val_finds_node(filled_bst):
    """Test that searching for leaf value returns node."""
    n = filled_bst.search(87)
    assert n.val == 87
    assert n.left is None
    assert n.right is None


def test_size_of_empty_tree_is_zero(empty_bst):
    """Test that the size of an empty tree is zero."""
    assert empty_bst.size() == 0


@pytest.mark.parametrize('values', TREES)
def test_size_of_filled_tree_is_correct(values):
    """Test that the size of a filled tree is correct."""
    from bst import BST
    t = BST(values)
    assert t.size() == len(set(values))


def test_depth_of_empty_tree_is_zero(empty_bst):
    """Test that the depth of an empty tree is zero."""
    assert empty_bst.depth() == 0


MAXDEPTH = [
    0, 1, 1, 2, 2, 1, 2,
    3, 3,
    6
]


@pytest.mark.parametrize('values, depth', zip(TREES, MAXDEPTH))
def test_depth_of_filled_tree_is_correct(values, depth):
    """Test that the depth of a filled tree is correct."""
    from bst import BST
    t = BST(values)
    assert t.depth() == depth


def test_contains_for_val_not_in_tree_is_none(filled_bst):
    """Test that checking if tree contains value not in tree returns False."""
    assert not filled_bst.contains(-10)


def test_contains_for_root_val_finds_node(filled_bst):
    """Test that checking if tree contains value at the root returns True."""
    assert filled_bst.contains(57)


def test_contains_for_inner_val_finds_node(filled_bst):
    """Test that checking if tree contains branch value returns True."""
    assert filled_bst.contains(45)


def test_contains_for_leaf_val_finds_node(filled_bst):
    """Test that checking if tree contains leaf value returns True."""
    assert filled_bst.contains(87)


def test_balance_of_empty_tree_is_zero(empty_bst):
    """Test that the balance of an empty tree is zero."""
    assert empty_bst.balance() == 0


BALANCE = [
    0, -1, 1, -2, 2, 0, 0,
    2, -2,
    2
]


@pytest.mark.parametrize('values, balance', zip(TREES, BALANCE))
def test_balance_of_filled_tree_is_correct(values, balance):
    """Test that the balance of a filled tree is correct."""
    from bst import BST
    t = BST(values)
    assert t.balance() == balance


def test_in_order_of_empty_tree_is_empty(empty_bst):
    """Test that in-order of an empty tree is empty."""
    assert len([x for x in empty_bst.in_order()]) == 0


@pytest.mark.parametrize('values', TREES)
def test_in_order_of_filled_tree_contains_all_values(values):
    """Test that the in-order of a filled tree contains all values."""
    from bst import BST
    t = BST(values)
    assert len([x for x in t.in_order()]) == len(set(values))


INORDER = [
    [8], [1, 3], [1, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3, 5, 7, 8],
    [3, 25, 42, 54, 72, 87], [1, 2, 4, 6, 8, 9, 52],
    [-2, 12, 13, 15, 17, 20, 23, 26, 45, 49, 52, 53, 57, 75, 86, 87, 89, 100]
]


@pytest.mark.parametrize('values, order', zip(TREES, INORDER))
def test_in_order_of_filled_tree_is_correct(values, order):
    """Test that the in-order traversal of a filled tree is correct."""
    from bst import BST
    t = BST(values)
    assert [x for x in t.in_order()] == order


PREORDER = [
    [8], [1, 3], [3, 1], [1, 2, 3], [3, 2, 1], [2, 1, 3], [5, 2, 1, 3, 7, 8],
    [72, 42, 3, 25, 54, 87], [2, 1, 8, 4, 6, 9, 52],
    [57, 20, 17, 12, -2, 15, 13, 23, 45, 26, 49, 53, 52, 86, 75, 100, 89, 87]
]


def test_pre_order_of_empty_tree_is_empty(empty_bst):
    """Test that pre-order of an empty tree is empty."""
    assert len([x for x in empty_bst.pre_order()]) == 0


@pytest.mark.parametrize('values', TREES)
def test_pre_order_of_filled_tree_contapres_all_values(values):
    """Test that the pre-order of a filled tree contains all values."""
    from bst import BST
    t = BST(values)
    assert len([x for x in t.pre_order()]) == len(set(values))


@pytest.mark.parametrize('values, order', zip(TREES, PREORDER))
def test_pre_order_of_filled_tree_is_correct(values, order):
    """Test that the pre-order traversal of a filled tree is correct."""
    from bst import BST
    t = BST(values)
    assert [x for x in t.pre_order()] == order


POSTORDER = [
    [8], [3, 1], [1, 3], [3, 2, 1], [1, 2, 3], [1, 3, 2], [1, 3, 2, 8, 7, 5],
    [25, 3, 54, 42, 87, 72], [1, 6, 4, 52, 9, 8, 2],
    [-2, 13, 15, 12, 17, 26, 52, 53, 49, 45, 23, 20, 75, 87, 89, 100, 86, 57]
]


def test_post_order_of_empty_tree_is_empty(empty_bst):
    """Test that post-order of an empty tree is empty."""
    assert len([x for x in empty_bst.post_order()]) == 0


@pytest.mark.parametrize('values', TREES)
def test_post_order_of_filled_tree_contaposts_all_values(values):
    """Test that the post-order of a filled tree contains all values."""
    from bst import BST
    t = BST(values)
    assert len([x for x in t.post_order()]) == len(set(values))


@pytest.mark.parametrize('values, order', zip(TREES, POSTORDER))
def test_post_order_of_filled_tree_is_correct(values, order):
    """Test that the post-order traversal of a filled tree is correct."""
    from bst import BST
    t = BST(values)
    assert [x for x in t.post_order()] == order


BREDTHFIRST = [
    [8], [1, 3], [3, 1], [1, 2, 3], [3, 2, 1], [2, 1, 3], [5, 2, 7, 1, 3, 8],
    [72, 42, 87, 3, 54, 25], [2, 1, 8, 4, 9, 6, 52],
    [57, 20, 86, 17, 23, 75, 100, 12, 45, 89, -2, 15, 26, 49, 87, 13, 53, 52]
]


def test_breadth_first_of_empty_tree_is_empty(empty_bst):
    """Test that breadth-first of an empty tree is empty."""
    assert len([x for x in empty_bst.breadth_first()]) == 0


@pytest.mark.parametrize('values', TREES)
def test_breadth_first_of_filled_tree_contaposts_all_values(values):
    """Test that the breadth-first of a filled tree contains all values."""
    from bst import BST
    t = BST(values)
    assert len([x for x in t.breadth_first()]) == len(set(values))


@pytest.mark.parametrize('values, order', zip(TREES, BREDTHFIRST))
def test_breadth_first_of_filled_tree_is_correct(values, order):
    """Test that the breadth-first traversal of a filled tree is correct."""
    from bst import BST
    t = BST(values)
    assert [x for x in t.breadth_first()] == order
