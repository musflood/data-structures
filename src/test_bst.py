"""Tests for the bst module."""

import pytest


def test_node_constructor_with_no_children():
    """Test that there is a node that has None for both children."""
    from bst import Node
    n = Node(0)
    assert n.val == 0
    assert n.left is None
    assert n.right is None


def test_node_constructor_with_left_child():
    """Test that there is a node that has another node as a left child."""
    from bst import Node
    n = Node(0, left=Node(1))
    assert n.val == 0
    assert isinstance(n.left, Node)
    assert n.right is None


def test_node_constructor_with_right_child():
    """Test that there is a node that has another node as a right child."""
    from bst import Node
    n = Node(0, right=Node(1))
    assert n.val == 0
    assert isinstance(n.right, Node)
    assert n.left is None


def test_node_constructor_with_both_children():
    """Test that there is a node that has nodes for children."""
    from bst import Node
    n = Node(0, left=Node(1), right=Node(2))
    assert n.val == 0
    assert isinstance(n.left, Node)
    assert isinstance(n.right, Node)


def test_bst_constructor_with_no_iterable():
    """Test that tree constructed with no arguments is empty."""
    from bst import BST
    t = BST()
    assert t.root is None
