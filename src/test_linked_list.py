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
    """Test that a LinkedList created with an empty iterable is empty."""
    from linked_list import LinkedList
    l = LinkedList([])
    assert l.head is None
    assert l.length == 0


@pytest.mark.parametrize('itr', [[1], [1, 2, 3, 4, 5, 6, 7]])
def test_linked_list_constructor_with_iterable(itr):
    """Test that a LinkedList created with an iterable contains all items."""
    from linked_list import LinkedList
    l = LinkedList(itr)
    assert l.head.val == itr[-1]
    assert l.length == len(itr)


@pytest.mark.parametrize('itr', [[], [1], [1, 2, 3, 4, 5, 6, 7]])
def test_len_function_works_for_linked_list(itr):
    """Test that len function gets the length of a LinkedList."""
    from linked_list import LinkedList
    l = LinkedList(itr)
    assert len(l) == l.length


@pytest.mark.parametrize('itr', [[], [1], [1, 2, 3, 4, 5, 6, 7]])
def test_size_for_linked_list(itr):
    """Test that size gets the length of a LinkedList."""
    from linked_list import LinkedList
    l = LinkedList(itr)
    assert l.size() == l.length


@pytest.mark.parametrize('itr', [[1, 2], [1, 2, 3, 4, 5, 6, 7]])
def test_pop_removes_last_item_from_linked_list(itr):
    """Test that pop removes the last item and returns the value."""
    from linked_list import LinkedList
    l = LinkedList(itr)
    x = l.pop()
    assert x == itr[-1]
    assert l.head.val == itr[-2]
    assert l.length == len(itr) - 1


def test_pop_empty_linked_list():
    """Test that pop on a empty list throws an IndexError."""
    from linked_list import LinkedList
    l = LinkedList()
    with pytest.raises(IndexError):
        l.pop()


def test_search_of_empty_list_is_none():
    """Test that searching an empty list returns None."""
    from linked_list import LinkedList
    l = LinkedList()
    assert l.search(0) is None


@pytest.mark.parametrize('itr', [[x for x in range(y)] for y in range(1, 20)])
def test_search_of_linked_list_finds_value(itr):
    """Test that searching an empty list returns None."""
    from linked_list import LinkedList
    from random import choice
    l = LinkedList(itr)
    find_item = choice(itr)
    assert l.search(find_item).val == find_item


@pytest.mark.parametrize('itr', [[x for x in range(y)] for y in range(1, 20)])
def test_search_of_linked_list_for_invalid_gets_none(itr):
    """Test that searching an empty list returns None."""
    from linked_list import LinkedList
    l = LinkedList(itr)
    assert l.search('a') is None


def test_remove_only_item_in_linked_list():
    """Test that remove only item from linked list empties it."""
    from linked_list import LinkedList
    l = LinkedList([1])
    l.remove(l.head)
    assert l.head is None
    assert l.length == 0


def test_remove_item_not_in_linked_list():
    """Test that removing node not in list raises a ValueError."""
    from linked_list import LinkedList, Node
    l = LinkedList([1])
    with pytest.raises(ValueError):
        l.remove(Node(1))


@pytest.mark.parametrize('itr', [[x for x in range(y)] for y in range(2, 20)])
def test_remove_head_of_linked_list(itr):
    """Test that removing the head from any length list moves the head."""
    from linked_list import LinkedList
    l = LinkedList(itr)
    l.remove(l.head)
    assert l.head.val == itr[-2]
    assert l.length == len(itr) - 1


@pytest.mark.parametrize('itr', [[x for x in range(y)] for y in range(3, 20)])
def test_remove_random_inner_node_from_linked_list(itr):
    """Test that removing any node from any length list adjusts the list."""
    from linked_list import LinkedList
    from random import choice
    l = LinkedList(itr)

    remove_item = choice(itr[1:-1])
    remove_node = l.search(remove_item)
    l.remove(remove_node)

    before_node = l.search(remove_item + 1)

    assert l.search(remove_item) is None
    assert before_node.nxt is remove_node.nxt
    assert l.length == len(itr) - 1


@pytest.mark.parametrize('itr', [[x for x in range(y)] for y in range(3, 20)])
def test_remove_last_node_from_linked_list(itr):
    """Test that removing last node from any length list adjusts the list."""
    from linked_list import LinkedList
    l = LinkedList(itr)

    l.remove(l.search(itr[0]))

    assert l.search(itr[1]).nxt is None
    assert l.length == len(itr) - 1
