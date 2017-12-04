"""Tests for the bast_balance module."""
import pytest


INSERT_TESTS = [
    ([1, 77], [1, 77]),
    ([1, 77, 72], [72, 1, 77]),
    ([65, 53, 60], [60, 53, 65]),
    ([1, 77, 72, 56], [72, 1, 56, 77]),
    ([1, 77, 72, 56, 60], [72, 56, 1, 60, 77]),
    ([1, 77, 72, 56, 60, 18], [56, 1, 18, 72, 60, 77]),
    ([1, 77, 72, 56, 60, 18, 58], [56, 1, 18, 72, 60, 58, 77]),
    ([1, 77, 72, 56, 60, 18, 58, 92], [56, 1, 18, 72, 60, 58, 77, 92]),
    ([1, 77, 72, 56, 60, 18, 58, 92, 100],
     [56, 1, 18, 72, 60, 58, 92, 77, 100]),
    ([1, 77, 72, 56, 60, 18, 58, 92, 100, 95],
     [72, 56, 1, 18, 60, 58, 92, 77, 100, 95]),
    ([1, 77, 72, 56, 60, 18, 58, 92, 100, 95, 93],
     [72, 56, 1, 18, 60, 58, 92, 77, 95, 93, 100]),
    ([1, 77, 72, 56, 60, 18, 58, 92, 100, 95, 93, 59],
     [72, 56, 1, 18, 59, 58, 60, 92, 77, 95, 93, 100]),
    ([1, 77, 72, 56, 60, 18, 58, 92, 100, 95, 93, 59, 10],
     [72, 56, 10, 1, 18, 59, 58, 60, 92, 77, 95, 93, 100]),

]


@pytest.mark.parametrize('values, order', INSERT_TESTS)
def test_insert_vals_into_self_balanceing_bst_correct(values, order):
    """Test that inserting values into a self-balancing bst works correctly."""
    from bst_balance import BalanceBST
    b = BalanceBST()
    for val in values:
        b.insert(val)
    assert [x for x in b.pre_order()] == order


INSERT_DEPTH_TESTS = [
    ([8], 0, 0),
    ([1, 3], 0, 1),
    ([3, 1], 1, 0),
    ([1, 2, 3], 1, 1),
    ([3, 2, 1], 1, 1),
    ([2, 1, 3], 1, 1),
    ([5, 2, 3, 7, 1, 8], 2, 2),
    ([72, 42, 54, 87, 3, 25], 2, 2),
    ([2, 8, 4, 6, 1, 9, 52], 2, 3),
    ([57, 20, 17, 86, 23, 12, 100, 45, 49, 26,
      -2, 89, 53, 52, 15, 13, 87, 75], 4, 4)
]


@pytest.mark.parametrize('values, l_depth, r_depth', INSERT_DEPTH_TESTS)
def test_insert_multiple_values_sets_depth_properly(values, l_depth, r_depth):
    """Test that multiple values are inserted sets the depth correctly."""
    from bst_balance import BalanceBST
    b = BalanceBST()
    for val in values:
        b.insert(val)

    assert b.left_depth == l_depth
    assert b.right_depth == r_depth


DELETE_TESTS = [
    ([41, 20, 72, 11, 29, 65, 91, 1, 15, 25, 32, 50, 70, 77, 99], 15,
     [41, 20, 11, 1, 29, 25, 32, 72, 65, 50, 70, 91, 77, 99]),

    ([41, 20, 72, 11, 29, 65, 91, 1, 25, 32, 50, 70, 77, 99], 1,
     [41, 20, 11, 29, 25, 32, 72, 65, 50, 70, 91, 77, 99]),

    ([41, 20, 72, 11, 29, 65, 91, 25, 32, 50, 70, 77, 99], 11,
     [41, 29, 20, 25, 32, 72, 65, 50, 70, 91, 77, 99]),

    ([41, 29, 72, 20, 32, 65, 91, 25, 50, 70, 77, 99], 32,
     [41, 25, 20, 29, 72, 65, 50, 70, 91, 77, 99]),

    ([41, 25, 72, 20, 29, 65, 91, 50, 70, 77, 99], 29,
     [41, 25, 20, 72, 65, 50, 70, 91, 77, 99]),

    ([41, 25, 72, 20, 65, 91, 50, 70, 77, 99], 20,
     [72, 41, 25, 65, 50, 70, 91, 77, 99]),

    ([72, 41, 91, 25, 65, 77, 99, 50, 70], 99,
     [72, 41, 25, 65, 50, 70, 91, 77]),

    ([72, 41, 91, 25, 65, 77, 50, 70], 77,
     [65, 41, 25, 50, 72, 70, 91]),

    ([41, 20, 72, 11, 29, 65, 91, 1, 15, 25, 32, 50, 70], 91,
     [41, 20, 11, 1, 15, 29, 25, 32, 65, 50, 72, 70]),

    ([41, 20, 65, 11, 29, 50, 72, 1, 15, 25, 32, 70], 50,
     [41, 20, 11, 1, 15, 29, 25, 32, 70, 65, 72]),

    ([41, 20, 70, 11, 29, 72, 1, 15, 25, 32], 72,
     [20, 11, 1, 15, 41, 29, 25, 32, 70]),

    ([20, 11, 41, 15, 29, 70, 25, 32], 15,
     [29, 20, 11, 25, 41, 32, 70]),
]


@pytest.mark.parametrize('tree, value, order', DELETE_TESTS)
def test_delete_leaf_vals_from_self_balancing_bst_correct(tree, value, order):
    """Test deleting leaf vals from a self-balancing bst works correctly."""
    from bst_balance import BalanceBST
    b = BalanceBST(tree)
    b.delete(value)
    assert [x for x in b.pre_order()] == order


DELETE_TESTS = [
    ([41, 11, 72, 20, 65, 91, 50, 70, 77, 99], 11,
     [72, 41, 20, 65, 50, 70, 91, 77, 99]),

    ([72, 41, 91, 20, 65, 77, 50, 70], 91,
     [65, 41, 20, 50, 72, 70, 77]),

    ([41, 20, 91, 11, 29, 99, 1, 15, 25, 32], 91,
     [20, 11, 1, 15, 41, 29, 25, 32, 99]),

    ([20, 11, 1, 41, 29, 99, 25, 32], 11,
     [29, 20, 1, 25, 41, 32, 99]),
]


@pytest.mark.parametrize('tree, value, order', DELETE_TESTS)
def test_delete_one_child_vals_from_balancing_bst_correct(tree, value, order):
    """Test deleting vals with one child from balancing bst works correctly."""
    from bst_balance import BalanceBST
    b = BalanceBST(tree)
    b.delete(value)
    assert [x for x in b.pre_order()] == order


DELETE_TESTS = [
    ([41, 20, 72, 1, 29, 65, 91, 25, 32, 50, 70, 77, 99], 20,
     [41, 29, 1, 25, 32, 72, 65, 50, 70, 91, 77, 99]),

    ([20, 11, 41, 29, 70], 20,
     [41, 11, 29, 70]),

]


@pytest.mark.parametrize('tree, value, order', DELETE_TESTS)
def test_delete_two_child_vals_from_balancing_bst_correct(tree, value, order):
    """Test deleting vals with two children from balancing bst works correctly."""
    from bst_balance import BalanceBST
    b = BalanceBST(tree)
    b.delete(value)
    assert [x for x in b.pre_order()] == order


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


def test_rebalance_does_nothing_for_balanced_node(balanced_balance_bst):
    """Test that _rebalance does nothing for a balanced node."""
    b = balanced_balance_bst
    order = [x for x in b.pre_order()]
    rebalanced = b._rebalance(b.search(20))
    assert [x for x in b.pre_order()] == order
    assert not rebalanced


def test_rebalance_fixes_left_left_case(balanced_balance_bst):
    """Test that _rebalance balances left-left unbalanced case."""
    b = balanced_balance_bst
    order = [x for x in b.pre_order()]
    b._rotate_left(b.search(20))
    rebalanced = b._rebalance(b.search(29))
    assert order == [x for x in b.pre_order()]
    assert rebalanced


def test_rebalance_fixes_left_left_case_no_right(balanced_balance_bst):
    """Test that _rebalance balances left-left unbalanced case."""
    b = balanced_balance_bst
    order = [x for x in b.pre_order()]
    b._rotate_left(b.search(11))
    b._rebalance(b.search(15))
    assert order == [x for x in b.pre_order()]


def test_rebalance_fixes_right_right_case(balanced_balance_bst):
    """Test that _rebalance balances right-right unbalanced case."""
    b = balanced_balance_bst
    order = [x for x in b.pre_order()]
    b._rotate_right(b.search(72))
    b._rebalance(b.search(65))
    assert order == [x for x in b.pre_order()]


def test_rebalance_fixes_right_right_case_no_left(balanced_balance_bst):
    """Test that _rebalance balances right-right unbalanced case."""
    b = balanced_balance_bst
    order = [x for x in b.pre_order()]
    b._rotate_right(b.search(65))
    b._rebalance(b.search(50))
    assert order == [x for x in b.pre_order()]


def test_rebalance_fixes_left_right_case(balanced_balance_bst):
    """Test that _rebalance balances left-right unbalanced case."""
    b = balanced_balance_bst
    order = [x for x in b.pre_order()]
    b._rotate_left(b.search(20))
    b._rotate_right(b.search(20))
    b._rebalance(b.search(29))
    assert order == [x for x in b.pre_order()]


def test_rebalance_fixes_left_right_case_no_left(balanced_balance_bst):
    """Test that _rebalance balances left-right unbalanced case."""
    b = balanced_balance_bst
    order = [x for x in b.pre_order()]
    b._rotate_left(b.search(11))
    b._rotate_right(b.search(11))
    b._rebalance(b.search(15))
    assert order == [x for x in b.pre_order()]


def test_rebalance_fixes_right_left_case(balanced_balance_bst):
    """Test that _rebalance balances right-left unbalanced case."""
    b = balanced_balance_bst
    order = [x for x in b.pre_order()]
    b._rotate_right(b.search(72))
    b._rotate_left(b.search(72))
    b._rebalance(b.search(65))
    assert order == [x for x in b.pre_order()]


def test_rebalance_fixes_right_left_case_no_right(balanced_balance_bst):
    """Test that _rebalance balances right-left unbalanced case."""
    b = balanced_balance_bst
    order = [x for x in b.pre_order()]
    b._rotate_right(b.search(65))
    b._rotate_left(b.search(65))
    b._rebalance(b.search(50))
    assert order == [x for x in b.pre_order()]


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
