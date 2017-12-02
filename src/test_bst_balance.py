"""Tests for the bast_balance module."""
import pytest


def test_rotate_right_rearranges_tree_with_right_parent(balanced_balance_bst):
    """Test that _rotate_right rearranges nodes correctly."""
    b = balanced_balance_bst
    b._rotate_right(b.search(20))
    order = [x for x in b.pre_order()]
    assert order == [41, 11, 1, 20, 15, 29, 25, 32, 72, 65, 50, 70, 91, 77, 99]


def test_rotate_right_rearranges_tree_with_left_parent(balanced_balance_bst):
    """Test that _rotate_right rearranges nodes correctly."""
    b = balanced_balance_bst
    b._rotate_right(b.search(72))
    order = [x for x in b.pre_order()]
    assert order == [41, 20, 11, 1, 15, 29, 25, 32, 65, 50, 72, 70, 91, 77, 99]


def test_rotate_right_reassigns_all_pointers(balanced_balance_bst):
    """Test that _rotate_right reassigns all pointers of the nodes."""
    b = balanced_balance_bst
    pivot = b.search(11)
    root = pivot.parent
    child = pivot.right
    grandparent = pivot.parent.parent
    b._rotate_right(b.search(20))
    assert grandparent.left == pivot
    assert pivot.parent == grandparent
    assert pivot.right == root
    assert root.parent == pivot
    assert root.left == child
    assert child.parent == root


def test_rotate_right_from_root_reassigns_root(balanced_balance_bst):
    """Test that _rotate_right from root reassigns the root."""
    b = balanced_balance_bst
    new_root = b.root.left
    old_root = b.root
    b._rotate_right(b.root)
    assert b.root == new_root
    assert b.root.right == old_root


def test_rotate_left_rearranges_tree_with_left_parent(balanced_balance_bst):
    """Test that _rotate_left rearranges nodes correctly."""
    b = balanced_balance_bst
    b._rotate_left(b.search(72))
    order = [x for x in b.pre_order()]
    assert order == [41, 20, 11, 1, 15, 29, 25, 32, 91, 72, 65, 50, 70, 77, 99]


def test_rotate_left_rearranges_tree_with_right_parent(balanced_balance_bst):
    """Test that _rotate_right rearranges nodes correctly."""
    b = balanced_balance_bst
    b._rotate_left(b.search(20))
    order = [x for x in b.pre_order()]
    assert order == [41, 29, 20, 11, 1, 15, 25, 32, 72, 65, 50, 70, 91, 77, 99]


def test_rotate_left_reassigns_all_pointers(balanced_balance_bst):
    """Test that _rotate_left reassigns all pointers of the nodes."""
    b = balanced_balance_bst
    pivot = b.search(91)
    root = pivot.parent
    child = pivot.left
    grandparent = pivot.parent.parent
    b._rotate_left(b.search(72))
    assert grandparent.right == pivot
    assert pivot.parent == grandparent
    assert pivot.left == root
    assert root.parent == pivot
    assert root.right == child
    assert child.parent == root


def test_rotate_left_from_root_reassigns_root(balanced_balance_bst):
    """Test that _rotate_left from root reassigns the root."""
    b = balanced_balance_bst
    new_root = b.root.right
    old_root = b.root
    b._rotate_left(b.root)
    assert b.root == new_root
    assert b.root.left == old_root


def test_find_depth_of_empty_tree_is_neg_1(empty_balance_bst):
    """Test that _find_depth of an empty tree is -1."""
    assert empty_balance_bst._find_depth(empty_balance_bst.root) == -1


def test_find_depth_of_single_node_tree_is_zero():
    """Test that _find_depth of a single node tree is 0."""
    from bst_balance import BalanceBST
    b = BalanceBST([10])
    assert b._find_depth(b.root) == 0


@pytest.mark.parametrize('iter', [[1, 2], [2, 1], [2, 1, 3],
                                  [6, 3, 8, 4, 7, 2, 1]])
def test_find_depth_from_root_is_same_as_depth(iter):
    """Test that _find_depth from the root is equal to depth."""
    from bst_balance import BalanceBST
    b = BalanceBST(iter)
    assert b._find_depth(b.root) == b.depth()


@pytest.mark.parametrize('val, depth', [(3, 2), (8, 1), (4, 0),
                                        (7, 0), (2, 1), (1, 0)])
def test_find_depth_from_inner_node_is_correct(val, depth):
    """Test that the depth from inner nodes is determined correctly."""
    from bst_balance import BalanceBST
    b = BalanceBST([6, 3, 8, 4, 7, 2, 1])
    assert b._find_depth(b.search(val)) == depth
