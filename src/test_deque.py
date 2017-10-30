"""Tests for the deque module."""

import pytest


def test_empty_deque_constructor(empty_deque):
    """Test that a deque created with no arguments is empty."""
    d = empty_deque
    assert d.end is None
    assert d.front is None
    assert d._values.length == 0


def test_deque_constructor_with_empty_iterable():
    """Test that a deque created with an empty iterable is empty."""
    from deque import Deque
    d = Deque([])
    assert d.end is None
    assert d.front is None
    assert d._values.length == 0


@pytest.mark.parametrize('itr', [[x for x in range(y)] for y in range(1, 20)])
def test_deque_constructor_with_iterable(itr):
    """Test that a deque created with an iterable contains all items."""
    from deque import Deque
    d = Deque(itr)
    assert d.end.val == itr[-1]
    assert d.front.val == itr[0]
    assert d._values.length == len(itr)


def test_append_one_node_into_deque(empty_deque):
    """Test that appending one value adds it to front of deque."""
    d = empty_deque
    d.append(0)
    assert d.end.val == 0
    assert d.front.val == 0
    assert d.end.nxt is None
    assert d.end.prev is None
    assert d.front.nxt is None
    assert d.front.prev is None
    assert d._values.length == 1


def test_append_two_values_into_deque(empty_deque):
    """Test that appending two values adds to front of deque."""
    d = empty_deque
    d.append(0)
    d.append(1)
    assert d.end.val == 1
    assert d.front.val == 0
    assert d.end.nxt.val == 0
    assert d.end.prev is None
    assert d.front.nxt is None
    assert d.front.prev.val == 1
    assert d._values.length == 2


def test_append_multiple_values_into_deque_change_head(empty_deque):
    """Test that appending multiple values adds to front of deque."""
    d = empty_deque
    d.append(0)
    d.append(1)
    d.append(3)
    d.append(4)
    assert d.end.val == 4
    assert d.front.val == 0
    assert d.end.nxt.val == 3
    assert d.end.prev is None
    assert d.front.nxt is None
    assert d.front.prev.val == 1
    assert d._values.length == 4


def test_append_values_into_deque_adjust_inner_nodes(empty_deque):
    """Test that appending multiple values changes inner node connections."""
    d = empty_deque
    d.append(0)
    d.append(1)
    d.append(3)
    d.append(4)
    assert d.end.nxt.val == 3
    assert d.end.nxt.nxt.val == 1
    assert d.end.nxt.nxt.nxt.val == 0
    assert d.front.prev.val == 1
    assert d.front.prev.prev.val == 3
    assert d.front.prev.prev.prev.val == 4
    assert d._values.length == 4