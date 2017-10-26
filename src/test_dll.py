"""Tests for the dll module."""

import pytest


def test_node_constructor_with_no_nxt():
    """Test that there is a node that points at None."""
    from dll import Node
    n = Node(0)
    assert n.val == 0
    assert n.nxt is None
    assert n.prev is None


def test_node_constructor_one_diection():
    """Test that there is a node that points at another node one direction."""
    from dll import Node
    n = Node(0, Node(1))
    assert n.val == 0
    assert isinstance(n.nxt, Node)
    assert n.prev is None


def test_node_constructor_both_diections():
    """Test that there is a node that points at two different nodes."""
    from dll import Node
    n = Node(0, Node(1), Node(2))
    assert n.val == 0
    assert isinstance(n.nxt, Node)
    assert isinstance(n.prev, Node)
    assert n.nxt is not n.prev


def test_empty_doubly_linked_list_constructor(empty_dll):
    """Test that a doubly-linked list created with no arguments is empty."""
    assert empty_dll.head is None
    assert empty_dll.tail is None
    assert empty_dll.length == 0


@pytest.mark.parametrize('itr', [[x for x in range(y)] for y in range(1, 20)])
def test_doubly_linked_list_constructor_with_iterable(itr):
    """Test that a DLL created with an iterable contains all items."""
    from dll import DLL
    l = DLL(itr)
    assert l.head.val == itr[-1]
    assert l.tail.val == itr[0]
    assert l.length == len(itr)


def test_push_one_node_into_doubly_linked_list(empty_dll):
    """Test that pushing one value adds it to front of doubly linked list."""
    l = empty_dll
    l.push(0)
    assert l.head.val == 0
    assert l.tail.val == 0
    assert l.head.nxt is None
    assert l.head.prev is None
    assert l.tail.nxt is None
    assert l.tail.prev is None
    assert l.length == 1


def test_push_two_values_into_doubly_linked_list(empty_dll):
    """Test that pushing two values adds to front of DLL."""
    l = empty_dll
    l.push(0)
    l.push(1)
    assert l.head.val == 1
    assert l.tail.val == 0
    assert l.head.nxt.val == 0
    assert l.head.prev is None
    assert l.tail.nxt is None
    assert l.tail.prev.val == 1
    assert l.length == 2


def test_push_multiple_values_into_doubly_linked_list_change_head(empty_dll):
    """Test that pushing multiple values adds to front of DLL."""
    l = empty_dll
    l.push(0)
    l.push(1)
    l.push(3)
    l.push(4)
    assert l.head.val == 4
    assert l.tail.val == 0
    assert l.head.nxt.val == 3
    assert l.head.prev is None
    assert l.tail.nxt is None
    assert l.tail.prev.val == 1
    assert l.length == 4


def test_push_values_into_doubly_linked_list_adjust_inner_nodes(empty_dll):
    """Test that pushing multiple values changes inner node connections."""
    l = empty_dll
    l.push(0)
    l.push(1)
    l.push(3)
    l.push(4)
    assert l.head.nxt.val == 3
    assert l.head.nxt.nxt.val == 1
    assert l.head.nxt.nxt.nxt.val == 0
    assert l.tail.prev.val == 1
    assert l.tail.prev.prev.val == 3
    assert l.tail.prev.prev.prev.val == 4
    assert l.length == 4


def test_append_one_node_into_doubly_linked_list(empty_dll):
    """Test that appending one value adds it to front of doubly linked list."""
    l = empty_dll
    l.append(0)
    assert l.head.val == 0
    assert l.tail.val == 0
    assert l.head.nxt is None
    assert l.head.prev is None
    assert l.tail.nxt is None
    assert l.tail.prev is None
    assert l.length == 1


def test_append_two_values_into_doubly_linked_list(empty_dll):
    """Test that appending two values adds to front of DLL."""
    l = empty_dll
    l.append(0)
    l.append(1)
    assert l.head.val == 0
    assert l.tail.val == 1
    assert l.head.nxt.val == 1
    assert l.head.prev is None
    assert l.tail.nxt is None
    assert l.tail.prev.val == 0
    assert l.length == 2


def test_append_multiple_values_into_doubly_linked_list_change_head(empty_dll):
    """Test that appending multiple values adds to front of DLL."""
    l = empty_dll
    l.append(0)
    l.append(1)
    l.append(3)
    l.append(4)
    assert l.head.val == 0
    assert l.tail.val == 4
    assert l.head.nxt.val == 1
    assert l.head.prev is None
    assert l.tail.nxt is None
    assert l.tail.prev.val == 3
    assert l.length == 4


def test_append_values_into_doubly_linked_list_adjust_inner_nodes(empty_dll):
    """Test that appending multiple values changes inner node connections."""
    l = empty_dll
    l.append(0)
    l.append(1)
    l.append(3)
    l.append(4)
    assert l.head.nxt.val == 1
    assert l.head.nxt.nxt.val == 3
    assert l.head.nxt.nxt.nxt.val == 4
    assert l.tail.prev.val == 3
    assert l.tail.prev.prev.val == 1
    assert l.tail.prev.prev.prev.val == 0
    assert l.length == 4


def test_pop_only_item_from_doubly_linked_list(empty_dll):
    """Test that pop only item empties the DLL."""
    l = empty_dll
    l.push(0)
    x = l.pop()
    assert x == 0
    assert l.head is None
    assert l.tail is None
    assert l.length == 0


@pytest.mark.parametrize('itr', [[x for x in range(y)] for y in range(2, 20)])
def test_pop_one_item_from_any_length_doubly_linked_list(itr):
    """Test that pop item removes head from DLL."""
    from dll import DLL
    l = DLL(itr)
    x = l.pop()
    assert x == itr[-1]
    assert l.head.val == itr[-2]
    assert l.head.prev is None
    assert l.tail.val == itr[0]
    assert l.length == len(itr) - 1


@pytest.mark.parametrize('itr', [[x for x in range(y)] for y in range(3, 20)])
def test_pop_multiple_items_from_any_length_doubly_linked_list(itr):
    """Test that pop items removes head from DLL."""
    from dll import DLL
    from random import randint
    l = DLL(itr)
    num = randint(2, len(itr) - 1)
    for _ in range(num):
        x = l.pop()
    assert x == itr[-num]
    assert l.head.val == itr[-num - 1]
    assert l.head.prev is None
    assert l.tail.val == itr[0]
    assert l.length == len(itr) - num


def test_pop_empty_doubly_linked_list(empty_dll):
    """Test that pop on a empty list throws an IndexError."""
    with pytest.raises(IndexError):
        empty_dll.pop()


def test_shift_only_item_from_doubly_linked_list(empty_dll):
    """Test that shift only item empties the DLL."""
    l = empty_dll
    l.push(0)
    x = l.shift()
    assert x == 0
    assert l.head is None
    assert l.tail is None
    assert l.length == 0


@pytest.mark.parametrize('itr', [[x for x in range(y)] for y in range(2, 20)])
def test_shift_one_item_from_any_length_doubly_linked_list(itr):
    """Test that shift item removes head from DLL."""
    from dll import DLL
    l = DLL(itr)
    x = l.shift()
    assert x == itr[0]
    assert l.head.val == itr[-1]
    assert l.tail.val == itr[1]
    assert l.tail.nxt is None
    assert l.length == len(itr) - 1


@pytest.mark.parametrize('itr', [[x for x in range(y)] for y in range(3, 20)])
def test_shift_multiple_items_from_any_length_doubly_linked_list(itr):
    """Test that shift items removes head from DLL."""
    from dll import DLL
    from random import randint
    l = DLL(itr)
    num = randint(2, len(itr) - 1)
    for _ in range(num):
        x = l.shift()
    assert x == itr[num - 1]
    assert l.head.val == itr[-1]
    assert l.tail.val == itr[num]
    assert l.tail.nxt is None
    assert l.length == len(itr) - num


def test_shift_empty_doubly_linked_list(empty_dll):
    """Test that shift on a empty list throws an IndexError."""
    with pytest.raises(IndexError):
        empty_dll.shift()


@pytest.mark.parametrize('itr', [[x for x in range(y)] for y in range(20)])
def test_len_function_works_for_doubly_linked_list(itr):
    """Test that len function gets the length of a DLL."""
    from dll import DLL
    l = DLL(itr)
    assert len(l) == l.length


def test_remove_only_item_in_doubly_linked_list(empty_dll):
    """Test that remove only item from doubly linked list empties it."""
    l = empty_dll
    l.push(0)
    l.remove(0)
    assert l.head is None
    assert l.length == 0
    assert l.tail is None


def test_remove_item_not_in_doubly_linked_list(empty_dll):
    """Test that removing node not in list raises a ValueError."""
    with pytest.raises(ValueError):
        empty_dll.remove(1)


@pytest.mark.parametrize('itr', [[x for x in range(y)] for y in range(2, 20)])
def test_remove_head_of_doubly_linked_list(itr):
    """Test that removing the head from any length list moves the head."""
    from dll import DLL
    l = DLL(itr)
    l.remove(itr[-1])
    assert l.head.val == itr[-2]
    assert l.length == len(itr) - 1
    assert l.tail.val == itr[0]
    assert l.head.prev is None


def test_remove_invalid_item_from_doubly_linked_list():
    """."""
    from dll import DLL
    l = DLL([1, 2, 3, 4, 5, 6])
    with pytest.raises(ValueError):
        l.remove('a')


@pytest.mark.parametrize('itr', [[x for x in range(y)] for y in range(3, 20)])
def test_remove_random_inner_node_from_doubly_linked_list(itr):
    """Test that removing any node from any length list adjusts the list."""
    from dll import DLL
    from random import choice
    l = DLL(itr)

    remove_item = choice(itr[1:-1])
    l.remove(remove_item)
    with pytest.raises(ValueError):
        l.remove(remove_item)
    assert l.length == len(itr) - 1


@pytest.mark.parametrize('itr', [[x % 2 for x in range(y)]
                                 for y in range(5, 20) if y % 2])
def test_remove_first_instance_of_value_from_doubly_linked_list(itr):
    """Test that removing any node from any length list adjusts the list."""
    from dll import DLL
    l = DLL(itr)
    print(itr)
    l.remove(1)
    assert l.head.val == 0
    assert l.head.nxt.val == 0
    assert l.head.nxt.nxt.val == 1
    assert l.length == len(itr) - 1


@pytest.mark.parametrize('itr', [[x for x in range(y)] for y in range(2, 20)])
def test_remove_tail_from_doubly_linked_list(itr):
    """Test that removing tail from any length list adjusts the list."""
    from dll import DLL
    l = DLL(itr)

    l.remove(itr[0])

    assert l.tail.val == itr[1]
    assert l.tail.nxt is None
    assert l.length == len(itr) - 1
