"""Tests for the hash_table module."""
import pytest
import random


def test_additive_hash_raises_type_error_for_non_string():
    """Test that the additive hash raises a TypeError for a non-string."""
    from hash_table import additive_hash
    with pytest.raises(TypeError):
        additive_hash(10)


@pytest.mark.parametrize('val, sol', [('', 0), ('a', 97), ('ab', 195),
                                      ('this', 440), ('long key time', 1256)])
def test_additive_hash_gets_correct_hash(val, sol):
    """Test that the additive hash gets the correct hash value."""
    from hash_table import additive_hash
    assert additive_hash(val) == sol


def test_fnv_hash_raises_type_error_for_non_string():
    """Test that the fnv hash raises a TypeError for a non-string."""
    from hash_table import fnv_hash
    with pytest.raises(TypeError):
        fnv_hash(10)


@pytest.mark.parametrize('val, sol', [
    ('', 2166136261),
    ('a', 36342608889142654),
    ('ab', 609742445408048685460792),
    ('this', 171635485923009561422634911170838452933),
    ('long key time', 18079234363021010787510523336376950754471158886120709393319078922713372768153835952231452296335172489493)
])
def test_fnv_hash_gets_correct_hash(val, sol):
    """Test that the fnv hash gets the correct hash value."""
    from hash_table import fnv_hash
    assert fnv_hash(val) == sol


def test_fnv_better_hash_than_additive():
    """Test that FNV is gets unique values and is thus better than additive."""
    from hash_table import additive_hash, fnv_hash
    assert additive_hash('apple') == additive_hash('papel')
    assert fnv_hash('apple') != fnv_hash('papel')


def test_hash_table_constructor_makes_empty_table():
    """Test that the hash table comstructor creates an empty table."""
    from hash_table import HashTable, additive_hash
    h = HashTable(10, additive_hash)
    assert not all(h.values)
    assert len(h.values) == 10
    assert h.hashing is additive_hash


def test_hash_table_hash_uses_given_hash_function():
    """Test that the _hash method uses the hash function given in constructor."""
    from hash_table import HashTable, fnv_hash
    h = HashTable(10, fnv_hash)
    assert h._hash('apple') == fnv_hash('apple')


def test_setting_value_into_hash_table_adds_value_to_empty_slot(empty_add_table):
    """Test that setting a value into table adds it to the correct, empty slot."""
    h = empty_add_table
    h.set('apple', 'pie')
    assert h.values[30][0] == ['apple', 'pie']


def test_setting_value_into_hash_table_adds_value_to_filled_slot(empty_add_table):
    """Test that setting a value into table adds it to the correct, filled slot."""
    h = empty_add_table
    h.set('apple', 'pie')
    h.set('papel', 'pope')
    assert h.values[30][0] == ['apple', 'pie']
    assert h.values[30][1] == ['papel', 'pope']


def test_setting_value_into_hash_table_replaces_value_for_key(empty_add_table):
    """Test setting val into table replaces the val for a key already in the table."""
    h = empty_add_table
    h.set('apple', 'pie')
    h.set('apple', 'core')
    assert h.values[30][0] == ['apple', 'core']
    assert len(h.values[30]) == 1


def test_setting_non_string_key_raises_error(empty_add_table):
    """Test setting a non string key raises a TypeError."""
    with pytest.raises(TypeError):
        empty_add_table.set(10, 'ten')


def test_getting_value_from_hash_table_gets_value_from_one_key_slot(empty_add_table):
    """Test that getting a value from table gets correct value from one key slot."""
    h = empty_add_table
    h.set('apple', 'pie')
    assert h.get('apple') == 'pie'


def test_getting_value_from_hash_table_gets_value_from_multi_key_slot(empty_add_table):
    """Test that getting a value from table gets correct value from multi-key slot."""
    h = empty_add_table
    h.set('apple', 'pie')
    h.set('papel', 'pope')
    assert h.get('apple') == 'pie'
    assert h.get('papel') == 'pope'


def test_getting_key_not_in_hash_table_raises_error(empty_add_table):
    """Test that getting a key not in the table raises a KeyError."""
    with pytest.raises(KeyError):
        empty_add_table.get('apple')


def test_getting_non_string_key_raises_error(empty_add_table):
    """Test getting a non string key raises a TypeError."""
    with pytest.raises(TypeError):
        empty_add_table.get(10)


with open('/usr/share/dict/words') as f:
    DICT_LIST = [word.strip() for word in f]


def giant_add_table():
    """Create a giant filled hash table from a dictionary."""
    from hash_table import additive_hash, HashTable
    h = HashTable(100000, additive_hash)
    for word in DICT_LIST:
        h.set(word, word)
    return h


GIANT_ADD_TABLE = giant_add_table()


def giant_fnv_table():
    """Create a giant filled hash table from a dictionary."""
    from hash_table import fnv_hash, HashTable
    h = HashTable(100000, fnv_hash)
    for word in DICT_LIST:
        h.set(word, word)
    return h

GIANT_FNV_TABLE = giant_fnv_table()


@pytest.mark.parametrize('_', [None for _ in range(1000)])
def test_getting_random_words_from_giant_add_table_works(_):
    """Test that getting random words from a giant table works."""
    word = random.choice(DICT_LIST)
    assert GIANT_ADD_TABLE.get(word) == word


@pytest.mark.parametrize('_', [None for _ in range(1000)])
def test_getting_random_words_from_giant_fnv_table_works(_):
    """Test that getting random words from a giant table works."""
    word = random.choice(DICT_LIST)
    assert GIANT_FNV_TABLE.get(word) == word


def test_key_distribution_over_smaller_range_for_add_than_fnv_hash():
    """Test that the key distribution is better for FNV than additive hash.

    The number of slots filled by the FNV is much larger than the
    additive hash. This indicates better key distribution.
    """
    add_filled_slots = sum(1 for slot in GIANT_ADD_TABLE.values if len(slot))
    fnv_filled_slots = sum(1 for slot in GIANT_FNV_TABLE.values if len(slot))
    assert fnv_filled_slots > add_filled_slots


def test_key_distribution_larger_diff_max_min_slot_add_than_fnv_hash():
    """Test that the key distribution is better for FNV than additive hash.

    The maximum keys in a slot is much smaller for the FNV hash
    than the additive hash. This indicates better key distribution.
    """
    add_slot_sizes = [len(bucket) for bucket in GIANT_ADD_TABLE.values]
    add_size_range = max(add_slot_sizes) - min(add_slot_sizes)
    fnv_slot_sizes = [len(bucket) for bucket in GIANT_FNV_TABLE.values]
    fnv_size_range = max(fnv_slot_sizes) - min(fnv_slot_sizes)
    assert add_size_range > fnv_size_range
