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
    """Create an empty maxbinheap."""
    from binheap import BinHeap
    return BinHeap()


@pytest.fixture
def empty_min_binheap():
    """Create an empty minbinheap."""
    from binheap import BinHeap
    return BinHeap(is_max_heap=False)


@pytest.fixture
def empty_priorityq():
    """Create an empty priority queue."""
    from priorityq import PriorityQ
    return PriorityQ()


@pytest.fixture
def empty_graph_1():
    """Create an empty graph."""
    from graph_1 import Graph
    return Graph()


@pytest.fixture
def full_graph_1():
    """Create a graph with nodes and edges."""
    from graph_1 import Graph
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(4, 2)
    g.add_edge(3, 5)
    g.add_edge(7, 9)
    g.add_edge(6, 8)
    g.add_edge(5, 3)
    g.add_node(21)
    return g


@pytest.fixture
def full_graph_tree():
    """Create a graph with nodes and edge that connect to eachother."""
    from graph_1 import Graph
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 6)
    g.add_edge(3, 7)
    return g


@pytest.fixture
def empty_weight_graph():
    """Create an empty graph."""
    from weight_graph import Graph
    return Graph()


@pytest.fixture
def node_weight_graph():
    """Create a graph with nodes, but no edges."""
    from weight_graph import Graph
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)
    g.add_node(5)
    return g
