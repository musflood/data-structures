"""Tests for the deque module."""

import pytest


def test_empty_deque_constructor(empty_deque):
    """Test that a deque created with no arguments is empty."""
    d = empty_deque
    assert d.back is None
    assert d.front is None
    assert d._values.length == 0


def test_deque_constructor_with_empty_iterable():
    """Test that a deque created with an empty iterable is empty."""
    from deque import Deque
    d = Deque([])
    assert d.back is None
    assert d.front is None
    assert d._values.length == 0


@pytest.mark.parametrize('itr', [[x for x in range(y)] for y in range(1, 20)])
def test_deque_constructor_with_iterable(itr):
    """Test that a deque created with an iterable contains all items."""
    from deque import Deque
    d = Deque(itr)
    assert d.back.val == itr[-1]
    assert d.front.val == itr[0]
    assert d._values.length == len(itr)
