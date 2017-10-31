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
