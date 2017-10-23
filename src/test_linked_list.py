"""Tests for the linked-list module."""

import pytest


def test_node_constructor_with_no_nxt():
    """Test that there is a node that points at None."""
    from linked_list import Node
    n = Node(0)
    assert n.val == 0
    assert n.nxt is None


def test_node_constructor():
    """Test that there is a node that points at another node."""
    from linked_list import Node
    n = Node(0, Node(1))
    assert n.val == 0
    assert isinstance(n.nxt, Node)


def test_empty_linked_list_constructor():
    """Test that a linked list created with no arguments is empty."""
    from linked_list import LinkedList
    l = LinkedList()
    assert l.head is None
    assert l.length == 0


@pytest.mark.parametrize('val', [0, 'a', [], (1, 2, 3)])
def test_push_new_val_to_linked_list(val):
    """Test that push adds a value to the front of the list."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push(val)
    assert l.length == 1
    assert l.head.val == val
    assert l.head.nxt is None


@pytest.mark.parametrize('val1, val2', [(0, 'a'), ([], (1, 2, 3))])
def test_push_two_new_vals_to_linked_list(val1, val2):
    """Test that push adds multiple values to the front of the list."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push(val1)
    old_head = l.head
    l.push(val2)
    assert l.length == 2
    assert l.head.val == val2
    assert l.head.nxt == old_head


def test_linked_list_constructor_with_empty_iterable():
    """."""
    from linked_list import LinkedList
    l = LinkedList([])
    assert l.head is None
    assert l.length == 0


@pytest.mark.parametrize('itr', [[1], [1, 2, 3, 4, 5, 6, 7]])
def test_linked_list_constructor(itr):
    """."""
    from linked_list import LinkedList
    l = LinkedList(itr)
    assert l.head.val == itr[-1]
    assert l.length == len(itr)


@pytest.mark.parametrize('itr', [[], [1], [1, 2, 3, 4, 5, 6, 7]])
def test_len_function(itr):
    """."""
    from linked_list import LinkedList
    l = LinkedList(itr)
    assert len(l) == l.length


@pytest.mark.parametrize('itr', [[], [1], [1, 2, 3, 4, 5, 6, 7]])
def test_size(itr):
    """."""
    from linked_list import LinkedList
    l = LinkedList(itr)
    assert l.size() == l.length


@pytest.mark.parametrize('itr', [[1, 2], [1, 2, 3, 4, 5, 6, 7]])
def test_pop(itr):
    """."""
    from linked_list import LinkedList
    l = LinkedList(itr)
    x = l.pop()
    assert x == itr[-1]
    assert l.head.val == itr[-2]
    assert l.length == len(itr) - 1


def test_pop_empty_linked_list():
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    with pytest.raises(IndexError):
        l.pop()
