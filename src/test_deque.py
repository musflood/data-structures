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


def test_append_multiple_values_into_deque_change_end(empty_deque):
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


def test_popleft_only_item_from_deque(empty_deque):
    """Test that popleft only item empties the deque."""
    d = empty_deque
    d.append(0)
    x = d.popleft()
    assert x == 0
    assert d.end is None
    assert d.front is None
    assert d._values.length == 0


@pytest.mark.parametrize('itr', [[x for x in range(y)] for y in range(2, 20)])
def test_popleft_one_item_from_any_length_deque(itr):
    """Test that popleft item removes value from front of deque."""
    from deque import Deque
    d = Deque(itr)
    x = d.popleft()
    assert x == itr[0]
    assert d.end.val == itr[-1]
    assert d.front.val == itr[1]
    assert d.front.nxt is None
    assert d._values.length == len(itr) - 1


@pytest.mark.parametrize('itr', [[x for x in range(y)] for y in range(3, 20)])
def test_popleft_multiple_items_from_any_length_deque(itr):
    """Test that popleft items removes front from deque."""
    from deque import Deque
    from random import randint
    d = Deque(itr)
    num = randint(2, len(itr) - 1)
    for _ in range(num):
        x = d.popleft()
    assert x == itr[num - 1]
    assert d.end.val == itr[-1]
    assert d.front.val == itr[num]
    assert d.front.nxt is None
    assert d._values.length == len(itr) - num


def test_popleft_empty_deque(empty_deque):
    """Test that popleft on a empty deque throws an IndexError."""
    with pytest.raises(IndexError):
        empty_deque.popleft()


def test_appendleft_one_node_into_deque(empty_deque):
    """Test that appendleft a value adds it to front of doubly linked list."""
    d = empty_deque
    d.appendleft(0)
    assert d.end.val == 0
    assert d.front.val == 0
    assert d.end.nxt is None
    assert d.end.prev is None
    assert d.front.nxt is None
    assert d.front.prev is None
    assert d._values.length == 1


def test_appendleft_two_values_into_deque(empty_deque):
    """Test that appendleft two values adds to front of DLL."""
    d = empty_deque
    d.appendleft(0)
    d.appendleft(1)
    assert d.end.val == 0
    assert d.front.val == 1
    assert d.end.nxt.val == 1
    assert d.end.prev is None
    assert d.front.nxt is None
    assert d.front.prev.val == 0
    assert d._values.length == 2


def test_appendleft_multiple_values_into_deque_change_end(empty_deque):
    """Test that appendleft multiple values adds to front of DLL."""
    d = empty_deque
    d.appendleft(0)
    d.appendleft(1)
    d.appendleft(3)
    d.appendleft(4)
    assert d.end.val == 0
    assert d.front.val == 4
    assert d.end.nxt.val == 1
    assert d.end.prev is None
    assert d.front.nxt is None
    assert d.front.prev.val == 3
    assert d._values.length == 4


def test_appendleft_values_into_deque_adjust_inner_nodes(empty_deque):
    """Test that appendleft multiple values changes inner node connections."""
    d = empty_deque
    d.appendleft(0)
    d.appendleft(1)
    d.appendleft(3)
    d.appendleft(4)
    assert d.end.nxt.val == 1
    assert d.end.nxt.nxt.val == 3
    assert d.end.nxt.nxt.nxt.val == 4
    assert d.front.prev.val == 3
    assert d.front.prev.prev.val == 1
    assert d.front.prev.prev.prev.val == 0
    assert d._values.length == 4
