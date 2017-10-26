"""Tests for the que_ module."""
import pytest


def test_empty_queue_constructor(empty_queue):
    """Test that a queue created with no arguments is empty."""
    q = empty_queue
    assert q._values.head is None
    assert q._values.tail is None
    assert q._values.length == 0


def test_queue_constructor_with_empty_iterable():
    """Test that a Queue created with an empty iterable is empty."""
    from que_ import Queue
    q = Queue([])
    assert q._values.head is None
    assert q._values.tail is None
    assert q._values.length == 0


@pytest.mark.parametrize('itr', [[x for x in range(y)] for y in range(1, 20)])
def test_queue_constructor_with_iterable(itr):
    """Test that a queue created with an iterable contains all items."""
    from que_ import Queue
    q = Queue(itr)
    assert q._values.head.val == itr[-1]
    assert q._values.tail.val == itr[0]
    assert q._values.length == len(itr)
