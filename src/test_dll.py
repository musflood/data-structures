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


def test_empty_doubly_linked_list_constructor():
    """Test that a doubly-linked list created with no arguments is empty."""
    from dll import DLL
    l = DLL()
    assert l.head is None
    assert l.tail is None
    assert l.length == 0
