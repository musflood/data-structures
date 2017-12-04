"""Tests for the trie module."""
import pytest
import random

with open('/usr/share/dict/words') as f:
    DICT_LIST = [word.strip() for word in f]

SMALL_DICT_LIST = ['whirlpuff', 'lycopodium', 'diblastula', 'antenati',
                   'scaticook', 'tricrotous', 'lenitively', 'unidealistic',
                   'anthrapurpurin', 'unretained', 'cacopharyngia',
                   'multifoliolate', 'agonista', 'unamused', 'chimakum',
                   'enheritage', 'nonsequestration', 'ormond', 'pseudo',
                   'unrepleviable', 'whirl']


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


@pytest.mark.parametrize('num', [x for x in range(1, 20)])
def test_trie_constructed_with_iterable_has_star_root_and_words(num):
    """Test that a constructed trie has '*' as the root node."""
    from trie import Trie
    itr = random.sample(DICT_LIST, num)
    t = Trie(itr)
    assert t.root.val == '*'
    assert t._size == num


def test_trie_constructed_with_string_raises_error():
    """Test that trie constructed with string directly raisesa TypeError."""
    from trie import Trie
    with pytest.raises(TypeError):
        Trie('apple')


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
    t = empty_trie
    for word in DICT_LIST:
        t.insert(word)
    assert t._size == len(DICT_LIST)
    assert len(t.root.children) == len(set([word[0] for word in DICT_LIST]))


@pytest.fixture
def small_trie():
    """Create a small filled trie."""
    from trie import Trie
    return Trie(SMALL_DICT_LIST)


def test_contains_for_non_string_raises_error(small_trie):
    """Test that contains for non-string raises a TypeError."""
    with pytest.raises(TypeError):
        small_trie.contains(10)


@pytest.mark.parametrize('trie, word', [(small_trie(), 'ormond'),
                                        (small_trie(), 'lycopodium'),
                                        (small_trie(), 'unamused'),
                                        (small_trie(), 'whirlpuff'),
                                        (small_trie(), 'whirl')])
def test_contains_returns_true_for_word_in_trie(trie, word):
    """Test that contains for an word in the trie returns True."""
    assert trie.contains(word) is True


@pytest.mark.parametrize('trie, word', [(small_trie(), 'zebra'),
                                        (small_trie(), 'apple'),
                                        (small_trie(), 'unintended'),
                                        (small_trie(), 'unideal'),
                                        (small_trie(), 'pseudopod')])
def test_contains_returns_false_for_word_not_in_trie(trie, word):
    """Test that contains for an word not in the trie returns False."""
    assert trie.contains(word) is False


@pytest.mark.parametrize('num', [x for x in range(1, 20)])
def test_size_returns_current_size_of_trie_unique_strings(num):
    """Test that size returns the current size of the tire."""
    from trie import Trie
    itr = random.sample(DICT_LIST, num)
    t = Trie(itr)
    assert t.size() == num


@pytest.mark.parametrize('num', [x for x in range(1, 20)])
def test_size_returns_current_size_of_trie_duplicate_strings(num):
    """Test that size returns the current size of the tire."""
    from trie import Trie
    itr = random.sample(DICT_LIST, num)
    t = Trie(itr + itr)
    assert t.size() == num


def test_remove_for_non_string_raises_error(small_trie):
    """Test that remove for non-string raises a TypeError."""
    with pytest.raises(TypeError):
        small_trie.remove(10)


def test_remove_string_not_in_trie_raises_error(small_trie):
    """Test that removing a word not in the trie raises a ValueError."""
    with pytest.raises(ValueError):
        small_trie.remove('apple')


def test_remove_only_string_from_trie_empties_it(empty_trie):
    """Test that removing the only string from a trie empties it."""
    t = empty_trie
    t.insert('apple')
    t.remove('apple')
    assert t.root.val == '*'
    assert t.root.children == {}
    assert t.size() == 0


@pytest.mark.parametrize('trie, word', [(small_trie(), 'ormond'),
                                        (small_trie(), 'lycopodium'),
                                        (small_trie(), 'unamused'),
                                        (small_trie(), 'whirlpuff'),
                                        (small_trie(), 'whirl')])
def test_remove_string_from_trie_removes_the_string(trie, word):
    """Test that removing a string removes it from the trie."""
    assert trie.contains(word) is True
    trie.remove(word)
    assert trie.contains(word) is False


@pytest.mark.parametrize('trie, word', [(small_trie(), 'ormond'),
                                        (small_trie(), 'lycopodium'),
                                        (small_trie(), 'unamused'),
                                        (small_trie(), 'whirlpuff'),
                                        (small_trie(), 'whirl')])
def test_remove_string_from_trie_adjusts_the_size(trie, word):
    """Test that removing a string removes it from the trie."""
    size = trie.size()
    trie.remove(word)
    assert trie.size() == size - 1


def test_remove_all_values_from_trie_empties_it(small_trie):
    """Test that removing all strings from the trie empties it."""
    t = small_trie
    words = SMALL_DICT_LIST[:]
    random.shuffle(words)

    for word in words:
        t.remove(word)
    assert t.size() == 0
    assert t.root.val == '*'
    assert t.root.children == {}


def test_inserting_and_removing_from_trie_works(empty_trie):
    """Test that inserting and removing from the trie works."""
    t = empty_trie

    all_words = DICT_LIST[:]
    random.shuffle(all_words)
    half_1 = all_words[:(len(all_words) // 2)]
    half_2 = all_words[(len(all_words) // 2):]

    for word in half_1:
        t.insert(word)

    assert t.size() == len(half_1)
    assert len(t.root.children) == len(set([word[0] for word in half_1]))

    removing_half_1 = random.sample(half_1, len(half_1) // 2)
    for word in removing_half_1:
        t.remove(word)
    assert t.size() == len(half_1) - (len(half_1) // 2)

    for word in half_2:
        t.insert(word)
    assert t.size() == len(half_1) - (len(half_1) // 2) + len(half_2)
