"""Tests for the trie module."""
import pytest


def test_node_constructed_with_no_parent():
    """Test that a Node constructed with no parent has None for parent."""
    from trie import Node
    n = Node('a')
    assert n.val == 'a'
    assert n.parent is None
    assert n.children == {}


def test_node_constructed_with_parent():
    """Test that a Node constructed with no parent has correct parent."""
    from trie import Node
    n = Node('a', parent=Node('b'))
    assert n.val == 'a'
    assert n.parent.val == 'b'
    assert n.children == {}


def test_trie_constructed_has_star_root():
    """Test that a constructed trie has '*' as the root node."""
    from trie import Trie
    t = Trie()
    assert t.root.val == '*'
