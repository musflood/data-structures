"""Test binHeap module."""

import pytest


def test_binheap_constructed_with_no_arguments_is_empty(empty_binheap):
    """Test that new binheap constructed with no arguments is empty."""
    assert empty_binheap._values[0] is None
    assert len(empty_binheap._values) == 1


@pytest.mark.parametrize('idx, result', [(2, 1), (3, 1), (4, 2),
                                         (5, 2), (6, 3), (7, 3)])
def test_find_parent_of_random_node_in_binheap(idx, result):
    """Test that _pi returns the parent of selected index."""
    from binheap import BinHeap
    assert BinHeap._pi(idx) == result


@pytest.mark.parametrize('idx, result', [(1, 2), (2, 4), (3, 6)])
def test_find_left_child_of_random_node_in_binheap(idx, result):
    """Test that _lci returns the left child of selected index."""
    from binheap import BinHeap
    assert BinHeap._lci(idx) == result


@pytest.mark.parametrize('idx, result', [(1, 3), (2, 5), (3, 7)])
def test_find_right_child_of_random_node_in_binheap(idx, result):
    """Test that _rci returns the right child of selected index."""
    from binheap import BinHeap
    assert BinHeap._rci(idx) == result
