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
    assert t.size == len(set(itr))
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


@pytest.mark.parametrize('values, size', [([1, 2, 3], 3), ([3, 2, 1], 3),
                                          ([5, 2, 3, 7, 1], 5),
                                          ([72, 42, 54, 87, 3, 25], 6),
                                          ([2, 8, 4, 6, 1, 6, 9, 52, 4, 8, 9,
                                            52, 9], 7)])
def test_insert_multiple_values_increases_size(values, size):
    """Test that multiple values are inserted increments the size."""
    from bst import BST
    t = BST()
    for n in values:
        t.insert(n)

    assert t.size == size


@pytest.mark.parametrize('values, l_depth, r_depth',
                         [([1, 2, 3], 0, 2), ([3, 2, 1], 2, 0),
                          ([5, 2, 3, 7, 1], 2, 1),
                          ([72, 42, 54, 87, 3, 25], 3, 1),
                          ([2, 8, 4, 6, 1, 6, 9, 52, 4, 8, 9, 52, 9], 1, 3)])
def test_insert_multiple_values_increases_depth(values, l_depth, r_depth):
    """Test that multiple values are inserted increments the depth."""
    from bst import BST
    t = BST()
    for n in values:
        t.insert(n)

    assert t.left_depth == l_depth
    assert t.right_depth == r_depth


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
