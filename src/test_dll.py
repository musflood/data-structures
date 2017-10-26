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


def test_push_one_node_into_doubly_linked_list(empty_dll):
    """Test that pushing one value adds it to front of doubly linked list."""
    empty_dll.push(0)
    assert empty_dll.head.val == 0
    assert empty_dll.tail.val == 0
    assert empty_dll.head.nxt is None
    assert empty_dll.head.prev is None
    assert empty_dll.tail.nxt is None
    assert empty_dll.tail.prev is None
    assert empty_dll.length == 1


def test_push_two_values_into_doubly_linked_list(empty_dll):
    """Test that pushing two values adds to front of DLL."""
    l = empty_dll
    l.push(0)
    l.push(1)
    assert empty_dll.head.val == 1
    assert empty_dll.tail.val == 0
    assert empty_dll.head.nxt.val == 0
    assert empty_dll.head.prev is None
    assert empty_dll.tail.nxt is None
    assert empty_dll.tail.prev.val == 1
    assert empty_dll.length == 2


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
