"""Test priorityq module."""

import pytest


def test_new_bucket_has_priority_and_is_empty():
    """Test that a new bucket has a priority and is empty."""
    from priorityq import Bucket
    b = Bucket(1)
    assert b.priority == 1
    assert len(b._values) == 0


def test_comparing_priority_of_buckets():
    """Test that comparison of two buckets work."""
    from priorityq import Bucket
    b1 = Bucket(1)
    b2 = Bucket(2)
    assert b2 > b1


def test_buckets_with_same_priority_are_equal():
    """Test that buckets with same priority are the same."""
    from priorityq import Bucket
    b1 = Bucket(1)
    b2 = Bucket(1)
    assert b1 == b2


def test_two_buckets_with_different_priority_not_equal():
    """Test that buckets with different values are not the same."""
    from priorityq import Bucket
    b1 = Bucket(1)
    b2 = Bucket(2)
    assert b1 != b2


def test_comparing_priority_of_buckets_to_int():
    """Test that comparison of bucket priority and int works."""
    from priorityq import Bucket
    b1 = Bucket(1)
    assert b1 > 0


def test_bucket_with_same_priority_can_be_equal_to_int():
    """Test that bucket with same priority as int are the same."""
    from priorityq import Bucket
    b1 = Bucket(1)
    assert b1 == 1


def test_bucket_with_different_priority_not_equal_to_int():
    """Test that bucket with different priority than int is not equal."""
    from priorityq import Bucket
    b1 = Bucket(1)
    assert b1 != 2


@pytest.mark.parametrize('priority, iterable', [(2, []), (1, [1]),
                                                (1, [1, 3, 4, 5, 6, 45, 34])])
def test_giving_itr_to_bucket_creates_bucket_with_values(priority, iterable):
    """Test that creating a bucket with iterable stores values in bucket."""
    from priorityq import Bucket
    b = Bucket(priority, iterable)
    assert len(b._values) == len(iterable)


def test_priorityq_constructed_with_no_arguments_is_empty(empty_priorityq):
    """Test that new priorityq constructed with no arguments is empty."""
    assert empty_priorityq._all_values[0] is None
    assert empty_priorityq._size == 0


def test_insert_an_item_without_priority_adds_lowest_priority(empty_priorityq):
    """Test inserting an item into the queue adds it as lowest priority."""
    q = empty_priorityq
    q.insert(5)
    assert q._size == 1
    assert q._all_values[1].priority == 0


def test_insert_items_without_priority_add_all_as_lowest(empty_priorityq):
    """Test inserting items into the queue adds all as lowest priority."""
    q = empty_priorityq
    q.insert(5)
    q.insert(3)
    q.insert(1)
    assert q._size == 1
    assert q._all_values[1].priority == 0
    assert len(q._all_values[1]) == 3


def test_insert_an_item_with_priority_adds_at_that_priority(empty_priorityq):
    """Test inserting an item into the queue adds it at given priority."""
    q = empty_priorityq
    q.insert(5, 6)
    assert q._size == 1
    assert q._all_values[1].priority == 6


def test_insert_items_with_priority_add_all_at_that_priority(empty_priorityq):
    """Test inserting items into the queue adds them at given priority."""
    q = empty_priorityq
    q.insert(5, 6)
    q.insert(3, 6)
    q.insert(1, 6)
    assert q._size == 1
    assert q._all_values[1].priority == 6
    assert len(q._all_values[1]) == 3


def test_insert_an_item_with_low_priority_changes_lowest(empty_priorityq):
    """Test inserting an item into the queue can change min priority."""
    q = empty_priorityq
    q.insert(5, -6)
    assert q._size == 1
    assert q._min_priority == -6


def test_insert_items_after_low_priority_add_to_same_priority(empty_priorityq):
    """Test inserting an item into the queue can change min priority."""
    q = empty_priorityq
    q.insert(5, -6)
    q.insert(3)
    q.insert(8)
    assert q._size == 1
    assert len(q._all_values[1]) == 3


def test_insert_items_with_diff_priority_order_by_priority(empty_priorityq):
    """Test inserting items into the queue orders them by priority."""
    q = empty_priorityq
    q.insert(5, 6)
    q.insert(3, 5)
    q.insert(1, 10)
    assert q._size == 3
    assert q._all_values == [None, 10, 5, 6]


def test_insert_items_with_diff_priority_group_by_priority(empty_priorityq):
    """Test inserting items into the queue groups them by priority."""
    q = empty_priorityq
    q.insert(5, 2)
    q.insert(3, 5)
    q.insert(1, 2)
    assert q._size == 2
    assert q._all_values == [None, 5, 2]
    assert len(q._all_values[2]) == 2


def test_insert_items_with_same_priority_add_them_in_order(empty_priorityq):
    """Test inserting items into the queue adds them at given priority."""
    q = empty_priorityq
    q.insert(5, 6)
    q.insert(3, 6)
    q.insert(1, 6)
    assert q._size == 1
    assert q._all_values[1]._values.dequeue() == 5
    assert q._all_values[1]._values.dequeue() == 3
    assert q._all_values[1]._values.dequeue() == 1


def test_pop_value_from_empty_priority_queue(empty_priorityq):
    """Test that popping from empty queue raises a IndexError."""
    with pytest.raises(IndexError):
        empty_priorityq.pop()


def test_pop_only_value_from_priority_queue_empties_it(empty_priorityq):
    """Test that popping only item from queue empties it."""
    q = empty_priorityq
    q.insert(5)
    assert q.pop() == 5
    assert q._size == 0


@pytest.mark.parametrize('amount', range(2, 20))
def test_pop_values_of_same_priority_acts_like_queue(amount):
    """Test that popping only item from queue empties it."""
    from random import randint
    from priorityq import PriorityQ
    q = PriorityQ()
    random_nums = [randint(0, 100) for _ in range(amount)]
    for n in random_nums:
        q.insert(n)
    popped = [q.pop() for _ in random_nums]
    assert popped == random_nums


def test_pop_from_random_p_q_with_all_diff_priority_in_sorted_order():
    """Test popping all the items from a priority queue are in sorted order.

    All items inserted have the same priority as their value, so when
    removed they should be in sorted order.
    """
    from priorityq import PriorityQ
    from random import randint
    random_nums = list(set([randint(0, 100) for _ in range(20)]))
    q = PriorityQ()
    for n in random_nums:
        q.insert(n, n)
    popped = [q.pop() for _ in range(len(q._all_values) - 1)]
    assert popped == sorted(random_nums, reverse=True)


def test_pop_from_multiple_items_at_same_priority_works(empty_priorityq):
    """Test that popped items are in proper order based on priority."""
    q = empty_priorityq
    q.insert(1, 5)
    q.insert(2, 2)
    q.insert(3, 9)
    q.insert(4, 1)
    q.insert(5, 2)
    q.insert(6, 5)
    q.insert(7, 1)
    q.insert(8)
    q.insert(9, 1)
    q.insert(10, 9)
    popped = [q.pop() for _ in range(len(q))]
    assert popped == [3, 10, 1, 6, 2, 5, 4, 7, 9, 8]


def test_peek_into_empty_priority_q_returns_none(empty_priorityq):
    """Test that peeking into empty priority q returns none."""
    assert empty_priorityq.peek() is None


def test_peek_into_one_item_q_returns_top_priority_q_value(empty_priorityq):
    """Test that peeking into priority q returns a value.

    Value returned is the first value of the que in the first priority bucket.
    """
    q = empty_priorityq
    q.insert(2, 2)
    assert q.peek() == 2
    assert len(q) == 1


def test_peek_into_priority_q_returns_gets_top_value(empty_priorityq):
    """Test that peeking into priority q with one priority returns valeu.

    Get first of the many values within the bucket.
    """
    q = empty_priorityq
    q.insert(2, 2)
    q.insert(3, 2)
    q.insert(4, 2)
    q.insert(6, 2)
    assert q.peek() == 2
    assert len(q) == 4


def test_peek_q_with_multiple_buckets_gets_top_priority_value(empty_priorityq):
    """Test that peeking into q with multiple buckets returns top value."""
    q = empty_priorityq
    q.insert(1, 5)
    q.insert(2, 2)
    q.insert(3, 9)
    q.insert(4, 1)
    assert q.peek() == 3
    assert len(q) == 4
