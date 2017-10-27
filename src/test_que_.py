"""Tests for the que_ module."""
import pytest


def test_empty_queue_constructor(empty_queue):
    """Test that a queue created with no arguments is empty."""
    q = empty_queue
    assert q.back is None
    assert q.front is None
    assert q._values.length == 0


def test_queue_constructor_with_empty_iterable():
    """Test that a Queue created with an empty iterable is empty."""
    from que_ import Queue
    q = Queue([])
    assert q.back is None
    assert q.front is None
    assert q._values.length == 0


@pytest.mark.parametrize('itr', [[x for x in range(y)] for y in range(1, 20)])
def test_queue_constructor_with_iterable(itr):
    """Test that a queue created with an iterable contains all items."""
    from que_ import Queue
    q = Queue(itr)
    assert q.back.val == itr[-1]
    assert q.front.val == itr[0]
    assert q._values.length == len(itr)


def test_enqueue_one_node_into_queue(empty_queue):
    """Test that enqueueing one value adds it to front of queue."""
    q = empty_queue
    q.enqueue(0)
    assert q.back.val == 0
    assert q.front.val == 0
    assert q.back.nxt is None
    assert q.back.prev is None
    assert q.front.nxt is None
    assert q.front.prev is None
    assert q._values.length == 1


def test_enqueue_two_values_into_queue(empty_queue):
    """Test that enqueueing two values adds to front of queue."""
    q = empty_queue
    q.enqueue(0)
    q.enqueue(1)
    assert q.back.val == 1
    assert q.front.val == 0
    assert q.back.nxt.val == 0
    assert q.back.prev is None
    assert q.front.nxt is None
    assert q.front.prev.val == 1
    assert q._values.length == 2


def test_enqueue_multiple_values_into_queue_change_head(empty_queue):
    """Test that enqueueing multiple values adds to front of queue."""
    q = empty_queue
    q.enqueue(0)
    q.enqueue(1)
    q.enqueue(3)
    q.enqueue(4)
    assert q.back.val == 4
    assert q.front.val == 0
    assert q.back.nxt.val == 3
    assert q.back.prev is None
    assert q.front.nxt is None
    assert q.front.prev.val == 1
    assert q._values.length == 4


def test_enqueue_values_into_queue_adjust_inner_nodes(empty_queue):
    """Test that enqueueing multiple values changes inner node connections."""
    q = empty_queue
    q.enqueue(0)
    q.enqueue(1)
    q.enqueue(3)
    q.enqueue(4)
    assert q.back.nxt.val == 3
    assert q.back.nxt.nxt.val == 1
    assert q.back.nxt.nxt.nxt.val == 0
    assert q.front.prev.val == 1
    assert q.front.prev.prev.val == 3
    assert q.front.prev.prev.prev.val == 4
    assert q._values.length == 4


def test_dequeue_only_item_from_queue(empty_queue):
    """Test that dequeue only item empties the Queue."""
    q = empty_queue
    q.enqueue(0)
    x = q.dequeue()
    assert x == 0
    assert q.back is None
    assert q.front is None
    assert q._values.length == 0


@pytest.mark.parametrize('itr', [[x for x in range(y)] for y in range(2, 20)])
def test_dequeue_one_item_from_any_length_queue(itr):
    """Test that dequeue item removes value from head of Queue."""
    from que_ import Queue
    q = Queue(itr)
    x = q.dequeue()
    assert x == itr[0]
    assert q.back.val == itr[-1]
    assert q.front.val == itr[1]
    assert q.front.nxt is None
    assert q._values.length == len(itr) - 1


@pytest.mark.parametrize('itr', [[x for x in range(y)] for y in range(3, 20)])
def test_dequeue_multiple_items_from_any_length_queue(itr):
    """Test that dequeue items removes head from Queue."""
    from que_ import Queue
    from random import randint
    q = Queue(itr)
    num = randint(2, len(itr) - 1)
    for _ in range(num):
        x = q.dequeue()
    assert x == itr[num - 1]
    assert q.back.val == itr[-1]
    assert q.front.val == itr[num]
    assert q.front.nxt is None
    assert q._values.length == len(itr) - num


def test_dequeue_empty_queue(empty_queue):
    """Test that dequeue on a empty queue throws an IndexError."""
    with pytest.raises(IndexError):
        empty_queue.dequeue()


def test_peek_at_empty_queue_is_none(empty_queue):
    """Test that peek at empty queue is None."""
    assert empty_queue.peek() is None


@pytest.mark.parametrize('itr', [[x for x in range(y)] for y in range(1, 20)])
def test_peek_finds_value_of_front_of_queue(itr):
    """Test that peek finds the value of the front of the queue."""
    from que_ import Queue
    q = Queue(itr)
    assert q.peek() == itr[0]
    assert q._values.length == len(itr)
