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
    assert b1 > b2


def test_there_can_not_be_buckets_with_same_priority():
    """Test that there can't be two buckets of the same priority."""
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


@pytest.mark.parametrize('priority, iterable', [(1, None), (2, []), (1, [1]),
                                                (1, [1, 3, 4, 5, 6, 45, 34])])
def test_giving_itr_to_bucket_creates_bucket_with_values(priority, iterable):
    """Test that creating a bucket with iterable stores values in bucket."""
    from priorityq import Bucket
    b = Bucket(priority, iterable)
    assert len(b._values) == len(iterable)
