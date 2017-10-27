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


def test_enqueue_one_node_into_queue(empty_queue):
    """Test that enqueueing one value adds it to front of queue."""
    q = empty_queue
    q.enqueue(0)
    assert q._values.head.val == 0
    assert q._values.tail.val == 0
    assert q._values.head.nxt is None
    assert q._values.head.prev is None
    assert q._values.tail.nxt is None
    assert q._values.tail.prev is None
    assert q._values.length == 1


def test_enqueue_two_values_into_queue(empty_queue):
    """Test that enqueueing two values adds to front of queue."""
    q = empty_queue
    q.enqueue(0)
    q.enqueue(1)
    assert q._values.head.val == 1
    assert q._values.tail.val == 0
    assert q._values.head.nxt.val == 0
    assert q._values.head.prev is None
    assert q._values.tail.nxt is None
    assert q._values.tail.prev.val == 1
    assert q._values.length == 2


def test_enqueue_multiple_values_into_queue_change_head(empty_queue):
    """Test that enqueueing multiple values adds to front of queue."""
    q = empty_queue
    q.enqueue(0)
    q.enqueue(1)
    q.enqueue(3)
    q.enqueue(4)
    assert q._values.head.val == 4
    assert q._values.tail.val == 0
    assert q._values.head.nxt.val == 3
    assert q._values.head.prev is None
    assert q._values.tail.nxt is None
    assert q._values.tail.prev.val == 1
    assert q._values.length == 4


def test_enqueue_values_into_queue_adjust_inner_nodes(empty_queue):
    """Test that enqueueing multiple values changes inner node connections."""
    q = empty_queue
    q.enqueue(0)
    q.enqueue(1)
    q.enqueue(3)
    q.enqueue(4)
    assert q._values.head.nxt.val == 3
    assert q._values.head.nxt.nxt.val == 1
    assert q._values.head.nxt.nxt.nxt.val == 0
    assert q._values.tail.prev.val == 1
    assert q._values.tail.prev.prev.val == 3
    assert q._values.tail.prev.prev.prev.val == 4
    assert q._values.length == 4
