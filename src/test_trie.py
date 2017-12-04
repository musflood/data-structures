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


def test_trie_constructed_is_empty_and_has_star_root():
    """Test that a constructed trie has '*' as the root node."""
    from trie import Trie
    t = Trie()
    assert t.root.val == '*'
    assert t._size == 0


def test_insert_non_string_raises_error(empty_trie):
    """Test inserting a non-string value into the trie raises a TypeError."""
    with pytest.raises(TypeError):
        empty_trie.insert(10)


def test_insert_word_into_empty_trie_added_from_root(empty_trie):
    """Test that a word inserted into an empty trie works."""
    t = empty_trie
    t.insert('apple')
    curr = t.root
    for ch in 'apple':
        assert ch in curr.children
        assert curr.children[ch].val == ch
        curr = curr.children[ch]
    assert '$' in curr.children
    assert curr.children['$'].val == '$'


def test_insert_distinct_words_into_trie_multiple_branches(empty_trie):
    """Test that distinct words inserted into a trie works."""
    t = empty_trie
    t.insert('apple')
    t.insert('fruit')
    assert 'a' in t.root.children
    assert 'f' in t.root.children


def test_insert_distinct_words_into_trie_all_of_words_added(empty_trie):
    """Test that distinct words inserted into a trie works."""
    t = empty_trie
    t.insert('apple')
    t.insert('fruit')

    curr = t.root
    for ch in 'apple':
        assert ch in curr.children
        curr = curr.children[ch]
    assert '$' in curr.children

    curr = t.root
    for ch in 'fruit':
        assert ch in curr.children
        curr = curr.children[ch]
    assert '$' in curr.children


def test_insert_branch_words_into_trie_has_one_branch(empty_trie):
    """Test inserting words with the same start create one branch from root."""
    t = empty_trie
    t.insert('apple')
    t.insert('ape')
    assert 'a' in t.root.children
    assert len(t.root.children) == 1


def test_insert_branch_words_into_trie_all_of_words_added(empty_trie):
    """Test that branch words inserted into a trie works."""
    t = empty_trie
    t.insert('apple')
    t.insert('ape')

    curr = t.root
    for ch in 'apple':
        assert ch in curr.children
        curr = curr.children[ch]
    assert '$' in curr.children

    curr = t.root
    for ch in 'ape':
        assert ch in curr.children
        curr = curr.children[ch]
    assert '$' in curr.children


def test_insert_same_word_twice_is_ignored(empty_trie):
    """Test that inserting a word already in the trie is ignored."""
    t = empty_trie
    t.insert('apple')
    t.insert('apple')

    assert t._size == 1
    curr = t.root
    for ch in 'apple':
        assert len(curr.children) == 1
        curr = curr.children[ch]
    assert len(curr.children) == 1


def test_insert_dictionary_adds_all_words_with_no_extra_branches(empty_trie):
    """Test that inserting a dictionary of words works."""
    from string import ascii_letters
    t = empty_trie
    count = 0
    with open('/usr/share/dict/words') as f:
        for word in f:
            t.insert(word.strip())
            count += 1
    assert t._size == count
    assert len(t.root.children) == len(ascii_letters)
