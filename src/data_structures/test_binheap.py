"""Test binHeap module."""

import pytest


def test_binheap_constructed_with_no_arguments_is_empty(empty_max_binheap):
    """Test that new binheap constructed with no arguments is empty."""
    assert empty_max_binheap._values[0] is None
    assert empty_max_binheap._size == 0


def test_binheap_constructed_with_empty_iterable_is_empty():
    """Test that new binheap constructed with an empty iterable is empty."""
    from binheap import BinHeap
    h = BinHeap([])
    assert h._values[0] is None
    assert h._size == 0


@pytest.mark.parametrize('itr', [[x for x in range(y)] for y in range(1, 20)])
def test_binheap_constructed_with_iterable_is_filled_properly(itr):
    """Test that new binheap constructed with an iterable is filled."""
    from binheap import BinHeap
    h = BinHeap(itr)
    assert h._values[0] is None
    assert h._values[1] is itr[-1]
    assert h._size == len(itr)


@pytest.mark.parametrize('itr', [{1: 2, 2: 3}, 400, set([4, 2, 3, 5, 2])])
def test_binheap_constructed_with_invalid_iterable_raises_error(itr):
    """Test that new binheap constructed invalid iterable raises TypeError."""
    from binheap import BinHeap
    with pytest.raises(TypeError):
        BinHeap(itr)


@pytest.mark.parametrize('idx, result', [(2, 1), (3, 1), (4, 2),
                                         (5, 2), (6, 3), (7, 3)])
def test_find_parent_of_random_node_in_binheap(idx, result):
    """Test that _pi returns the parent of selected index."""
    from binheap import BinHeap
    h = BinHeap()
    assert h._pi(idx) == result


@pytest.mark.parametrize('idx, result', [(1, 2), (2, 4), (3, 6)])
def test_find_left_child_of_random_node_in_binheap(idx, result):
    """Test that _lci returns the left child of selected index."""
    from binheap import BinHeap
    h = BinHeap()
    assert h._lci(idx) == result


@pytest.mark.parametrize('idx, result', [(1, 3), (2, 5), (3, 7)])
def test_find_right_child_of_random_node_in_binheap(idx, result):
    """Test that _rci returns the right child of selected index."""
    from binheap import BinHeap
    h = BinHeap()
    assert h._rci(idx) == result


def test_push_one_value_adds_value_to_empty_max_binheap(empty_max_binheap):
    """Test that adding a value to empty binheap returns binheap with value."""
    h = empty_max_binheap
    h.push(1)
    assert h._values[1] == 1


def test_push_two_values_maintains_the_max_heap_property(empty_max_binheap):
    """Test that adding two values will keep heap properties."""
    h = empty_max_binheap
    h.push(1)
    h.push(2)
    assert h._size == 2
    assert h._values[1] == 2
    assert h._values[2] == 1


def test_push_multiple_values_maintains_the_max_heap_property(empty_max_binheap):
    """Test that adding multiple values will keep heap properties."""
    h = empty_max_binheap
    h.push(1)
    h.push(2)
    h.push(3)
    h.push(4)
    assert h._size == 4
    assert h._values == [None, 4, 3, 2, 1]


def test_push_non_unique_values_add_all_to_max_heap(empty_max_binheap):
    """Test that duplicate values are added to heap."""
    heap = empty_max_binheap
    heap.push(1)
    heap.push(2)
    heap.push(2)
    assert heap._size == 3
    assert heap._values[1] == 2
    assert heap._values[2] == 1
    assert heap._values[3] == 2


def test_pop_only_item_from_max_heap_empties_it(empty_max_binheap):
    """Test that popping only item from a heap empties the heap."""
    h = empty_max_binheap
    h.push(1)
    assert h.pop() == 1
    assert h._size == 0


def test_pop_from_two_value_max_heap_removes_value_from_top(empty_max_binheap):
    """Test that popping from two value heap removes top."""
    h = empty_max_binheap
    h.push(1)
    h.push(2)
    assert h.pop() == 2
    assert h._size == 1
    assert h._values[1] == 1


def test_pop_from_unique_random_max_heap_in_sorted_order():
    """Test that popping all items from a unique heap are in sorted order."""
    from binheap import BinHeap
    from random import randint
    random_nums = list(set([randint(0, 100) for _ in range(20)]))
    h = BinHeap(random_nums)
    popped = [h.pop() for _ in range(len(h._values) - 1)]
    assert popped == sorted(random_nums, reverse=True)


def test_pop_from_random_max_heap_in_sorted_order():
    """Test that popping all the items from a heap are in sorted order."""
    from binheap import BinHeap
    from random import randint
    random_nums = [randint(0, 100) for _ in range(20)]
    h = BinHeap(random_nums)
    popped = [h.pop() for _ in range(len(h._values) - 1)]
    assert popped == sorted(random_nums, reverse=True)


def test_pop_from_empty_max_heap_raises_indexerror(empty_max_binheap):
    """Test popping from empty list raises an IndexError."""
    with pytest.raises(IndexError):
        empty_max_binheap.pop()


# min binheap


def test_push_one_value_adds_value_to_empty_min_binheap(empty_min_binheap):
    """Test that adding a value to empty min binheap returns binheap with value."""
    h = empty_min_binheap
    h.push(1)
    assert h._values[1] == 1


def test_push_two_values_maintains_the_min_heap_property(empty_min_binheap):
    """Test that adding two values will keep heap properties."""
    h = empty_min_binheap
    h.push(1)
    h.push(2)
    assert h._size == 2
    assert h._values[1] == 1
    assert h._values[2] == 2


def test_push_multiple_values_maintains_the_min_heap_property(empty_min_binheap):
    """Test that adding multiple values will keep heap properties."""
    h = empty_min_binheap
    h.push(1)
    h.push(2)
    h.push(3)
    h.push(4)
    assert h._size == 4
    assert h._values == [None, 1, 2, 3, 4]


def test_push_non_unique_values_add_all_to_min_heap(empty_min_binheap):
    """Test that duplicate values are added to heap."""
    h = empty_min_binheap
    h.push(1)
    h.push(2)
    h.push(2)
    assert h._size == 3
    assert h._values[1] == 1
    assert h._values[2] == 2
    assert h._values[3] == 2


def test_pop_only_item_from_min_heap_empties_it(empty_min_binheap):
    """Test that popping only item from a heap empties the heap."""
    h = empty_min_binheap
    h.push(1)
    assert h.pop() == 1
    assert h._size == 0


def test_pop_from_two_value_min_heap_removes_value_from_top(empty_min_binheap):
    """Test that popping from two value heap removes top."""
    h = empty_min_binheap
    h.push(2)
    h.push(1)
    assert h.pop() == 1
    assert h._size == 1
    assert h._values[1] == 2


def test_pop_from_unique_random_min_heap_in_sorted_order():
    """Test that popping all items from a unique heap are in sorted order."""
    from binheap import BinHeap
    from random import randint
    random_nums = list(set([randint(0, 100) for _ in range(20)]))
    h = BinHeap(random_nums, is_max_heap=False)
    popped = [h.pop() for _ in range(len(h._values) - 1)]
    assert popped == sorted(random_nums)


def test_pop_from_random_min_heap_in_sorted_order():
    """Test that popping all the items from a heap are in sorted order."""
    from binheap import BinHeap
    from random import randint
    random_nums = [randint(0, 100) for _ in range(20)]
    h = BinHeap(random_nums, is_max_heap=False)
    popped = [h.pop() for _ in range(len(h._values) - 1)]
    assert popped == sorted(random_nums)
