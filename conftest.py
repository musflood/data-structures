"""Fixtures for data-structures."""
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


@pytest.fixture
def edge_weight_graph():
    """"Create a weight graph with edges."""
    from weight_graph import Graph
    g = Graph()
    g. add_edge(1, 2, 1)
    g. add_edge(3, 4, 2)
    g. add_edge(5, 6, 3)
    g. add_edge(7, 8, 4)
    g. add_edge(9, 10, 5)
    return g


@pytest.fixture
def full_weight_graph_tree():
    """Create a graph with nodes and edge that connect to each other."""
    from weight_graph import Graph
    g = Graph()
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 5)
    g.add_edge(2, 4, 2)
    g.add_edge(2, 5, 9)
    g.add_edge(3, 6, 1)
    g.add_edge(3, 7, 3)
    return g


@pytest.fixture
def complex_weight_graph():
    """Create a graph with interconnecting nodes and edges."""
    from weight_graph import Graph
    g = Graph()
    g.add_edge(0, 1, 4)
    g.add_edge(1, 0, 4)
    g.add_edge(0, 7, 8)
    g.add_edge(7, 0, 8)
    g.add_edge(1, 7, 11)
    g.add_edge(7, 1, 11)
    g.add_edge(7, 8, 7)
    g.add_edge(8, 7, 7)
    g.add_edge(7, 6, 1)
    g.add_edge(6, 7, 1)
    g.add_edge(1, 2, 8)
    g.add_edge(2, 1, 8)
    g.add_edge(2, 5, 4)
    g.add_edge(5, 2, 4)
    g.add_edge(2, 8, 2)
    g.add_edge(8, 2, 2)
    g.add_edge(2, 3, 7)
    g.add_edge(3, 2, 7)
    g.add_edge(8, 6, 6)
    g.add_edge(6, 8, 6)
    g.add_edge(6, 5, 2)
    g.add_edge(5, 6, 2)
    g.add_edge(5, 3, 14)
    g.add_edge(3, 5, 14)
    g.add_edge(5, 4, 10)
    g.add_edge(4, 5, 10)
    g.add_edge(3, 4, 9)
    g.add_edge(4, 3, 9)
    return g


@pytest.fixture
def empty_bst():
    """Create an empty binary search tree."""
    from bst import BST
    return BST()


@pytest.fixture
def filled_bst():
    """Create an empty binary search tree."""
    from bst import BST
    return BST([57, 20, 17, 86, 23, 12, 100, 45, 49, 26,
                -2, 89, 53, 52, 15, 13, 87, 75, 30, 54, 101])


@pytest.fixture
def empty_balance_bst():
    """Create an empty self-balancing binary search tree."""
    from bst_balance import BalanceBST
    return BalanceBST()


@pytest.fixture
def balanced_balance_bst():
    """Create a already balanced self-balancing binary search tree."""
    from bst_balance import BalanceBST
    return BalanceBST([41, 20, 72, 11, 29, 65, 91, 1,
                       15, 25, 32, 50, 70, 77, 99])


@pytest.fixture
def empty_add_table():
    """Create an empty hash table with add hash function."""
    from hash_table import additive_hash, HashTable
    return HashTable(100, additive_hash)


@pytest.fixture
def empty_trie():
    """Create an empty trie."""
    from trie import Trie
    return Trie()


@pytest.fixture(scope='session')
def giant_trie():
    """Create a giant tire from a dictionary."""
    from trie import Trie
    with open('/usr/share/dict/words') as f:
        dict_list = [word.strip() for word in f]
    return Trie(dict_list)
