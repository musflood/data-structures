"""Test for Stack module."""


import pytest


def test_empty_stack_constructor():
    """Test that a Stack created with no arguments is empty."""
    from stack import Stack
    s = Stack()
    assert s.top is None
    assert s._values.length == 0


def test_stack_constructor_with_empty_iterable():
    """Test that a Stack created with an empty iterable is empty."""
    from stack import Stack
    s = Stack([])
    assert s.top is None
    assert s._values.length == 0


@pytest.mark.parametrize('itr', [[x for x in range(y)] for y in range(1, 20)])
def test_stack_constructor_with_iterable(itr):
    """Test that a Stack created with an iterable contains all items."""
    from stack import Stack
    s = Stack(itr)
    assert s.top.val == itr[-1]
    assert s._values.length == len(itr)


@pytest.mark.parametrize('itr', [[x for x in range(y)] for y in range(2, 20)])
def test_pop_removes_last_item_from_stack(itr):
    """Test that pop removes the last item and returns the value."""
    from stack import Stack
    s = Stack(itr)
    x = s.pop()
    assert x == itr[-1]
    assert s.top.val == itr[-2]
    assert s._values.length == len(itr) - 1


def test_pop_removes_last_item_from_one_item_stack():
    """Test that pop from one item stack returns the value."""
    from stack import Stack
    s = Stack([1])
    x = s.pop()
    assert x == 1
    assert s.top is None
    assert s._values.length == 0


def test_pop_empty_stack():
    """Test that pop on a empty stack throws an IndexError."""
    from stack import Stack
    s = Stack()
    with pytest.raises(IndexError):
        s.pop()


@pytest.mark.parametrize('val', [0, 'a', [], (1, 2, 3)])
def test_push_new_val_to_stack(val):
    """Test that push adds a value to the top of the stack."""
    from stack import Stack
    s = Stack()
    s.push(val)
    assert s._values.length == 1
    assert s.top.val == val
    assert s.top.nxt is None


@pytest.mark.parametrize('val1, val2', [(0, 'a'), ([], (1, 2, 3))])
def test_push_two_new_vals_to_stack(val1, val2):
    """Test that push adds two values to the top of the stack."""
    from stack import Stack
    s = Stack()
    s.push(val1)
    old_head = s.top
    s.push(val2)
    assert s._values.length == 2
    assert s.top.val == val2
    assert s.top.nxt == old_head


@pytest.mark.parametrize('n', range(3, 20))
def test_push_multiple_new_vals_to_stack(n):
    """Test that push adds multiple values to the top of the stack."""
    from stack import Stack
    s = Stack()
    nums = range(n)
    for num in nums:
        s.push(num)
    assert s._values.length == n
    assert s.top.val == n - 1
    assert s.top.nxt.val == n - 2


@pytest.mark.parametrize('itr', [[x for x in range(y)] for y in range(1, 20)])
def test_len_function_works_for_stack(itr):
    """Test that len function gets the length of a Stack."""
    from stack import Stack
    s = Stack(itr)
    assert len(s) == len(itr)
