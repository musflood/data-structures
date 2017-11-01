import pytest


@pytest.fixture
def empty_dll():
    """Create an empty doubly linked list."""
    from dll import DLL
    return DLL()


@pytest.fixture
def empty_queue():
    """Create an empty queue."""
    from que_ import Queue
    return Queue()


@pytest.fixture
def empty_deque():
    """Create an empty deque."""
    from deque import Deque
    return Deque()


@pytest.fixture
def empty_max_binheap():
    """Create and empty maxbinheap."""
    from binheap import BinHeap
    return BinHeap()


@pytest.fixture
def empty_min_binheap():
    """Create and empty minbinheap."""
    from binheap import BinHeap
    return BinHeap(is_max_heap=False)
