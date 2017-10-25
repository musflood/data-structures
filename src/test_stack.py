"""Test for Stack module."""


import pytest


def test_empty_stack_constructor():
    """Test that a Stack created with no arguments is empty."""
    from stack import Stack
    s = Stack()
    assert s._values.head is None
    assert s._values.length == 0


def test_stack_constructor_with_empty_iterable():
    """Test that a Stack created with an empty iterable is empty."""
    from stack import Stack
    s = Stack([])
    assert s._values.head is None
    assert s._values.length == 0


@pytest.mark.parametrize('itr', [[x for x in range(y)] for y in range(1, 20)])
def test_stack_constructor_with_iterable(itr):
    """Test that a Stack created with an iterable contains all items."""
    from stack import Stack
    s = Stack(itr)
    assert s._values.head.val == itr[-1]
    assert s._values.length == len(itr)


@pytest.mark.parametrize('itr', [[x for x in range(y)] for y in range(2, 20)])
def test_pop_removes_last_item_from_stack(itr):
    """Test that pop removes the last item and returns the value."""
    from stack import Stack
    s = Stack(itr)
    x = s.pop()
    assert x == itr[-1]
    assert s._values.head.val == itr[-2]
    assert s._values.length == len(itr) - 1


def test_pop_removes_last_item_from_one_item_stack():
    """Test that pop from one item stack returns the value."""
    from stack import Stack
    s = Stack([1])
    x = s.pop()
    assert x == 1
    assert s._values.head is None
    assert s._values.length == 0


def test_pop_empty_stack():
    """Test that pop on a empty stack throws an IndexError."""
    from stack import Stack
    s = Stack()
    with pytest.raises(IndexError):
        s.pop()
