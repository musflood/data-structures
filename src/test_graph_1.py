"""Tests for the graph_1 module."""

import pytest


def test_empty_constructor_constructs_empty_graph():
    """Test that a new graph is empty."""
    from graph_1 import Graph
    g = Graph()
    assert len(g.node_set) == 0
    assert len(g.edge_set) == 0


def test_nodes_of_empty_graph_is_empty(empty_graph_1):
    """Test that the list of nodes for an empty graph is empty."""
    assert empty_graph_1.nodes() == []


@pytest.mark.parametrize('num', [x for x in range(1, 20)])
def test_nodes_of_filled_graph_has_all_nodes(num):
    """Test that nodes lists all the nodes in a graph."""
    from graph_1 import Graph
    g = Graph()
    for x in range(num):
        g.add_node(x)
    assert len(g.nodes()) == num
    assert sorted(g.nodes()) == list(range(num))


def test_edges_of_empty_graph_is_empty(empty_graph_1):
    """Test that the list of edges for an empty graph is empty."""
    assert empty_graph_1.edges() == []


@pytest.mark.parametrize('num', [x for x in range(1, 20)])
def test_edges_of_filled_graph_has_all_edges(num):
    """Test that edges lists all the edges in a graph."""
    from graph_1 import Graph
    g = Graph()
    for x in range(num):
        g.add_edge(x, x + 1)
    assert len(g.edges()) == num


@pytest.mark.parametrize('num', [x for x in range(1, 20)])
def test_adding_unique_values_to_a_graph_adds_all_nodes(num):
    """Test that adding unique values to the graph adds all of them."""
    from graph_1 import Graph
    g = Graph()
    for x in range(num):
        g.add_node(x)
    assert len(g.node_set) == num


@pytest.mark.parametrize('num', [x for x in range(1, 20)])
def test_dublicate_values_to_a_graph_adds_some_nodes(num):
    """Test that adding duplicate values to the graph add only unique items."""
    from graph_1 import Graph
    g = Graph()
    for x in range(num):
        g.add_node(x % 5)
    assert len(g.node_set) == 5 if num > 5 else num


def test_adding_edge_to_existing_nodes_only_adds_edge(empty_graph_1):
    """Test that adding an edge for existing nodes only adds the edge."""
    g = empty_graph_1
    g.add_node(1)
    g.add_node(9)
    g.add_edge(1, 9)
    assert len(g.node_set) == 2
    assert len(g.edge_set) == 1


def test_adding_edges_between_existing_nodes_adds_both_edges(empty_graph_1):
    """Test that adding an edges between existing nodes adds both edges."""
    g = empty_graph_1
    g.add_node(1)
    g.add_node(9)
    g.add_edge(1, 9)
    g.add_edge(9, 1)
    assert len(g.node_set) == 2
    assert len(g.edge_set) == 2


def test_adding_edge_to_one_existing_nodes_adds_edge_and_node(empty_graph_1):
    """Test that adding an edge for one node adds the edge and other node."""
    g = empty_graph_1
    g.add_node(1)
    g.add_edge(1, 9)
    assert len(g.node_set) == 2
    assert 9 in g.node_set
    assert len(g.edge_set) == 1


def test_adding_edge_to_nonexisting_nodes_adds_edge_and_nodes(empty_graph_1):
    """Test that adding an edge for existing nodes only adds the edge."""
    g = empty_graph_1
    g.add_edge(1, 9)
    assert len(g.node_set) == 2
    assert 9 in g.node_set
    assert 1 in g.node_set
    assert len(g.edge_set) == 1


@pytest.mark.parametrize('num', [x for x in range(1, 20)])
def test_adding_unique_edges_to_a_graph_adds_all_edges(num):
    """Test that adding unique edges to the graph adds all edges."""
    from graph_1 import Graph
    g = Graph()
    for x in range(num):
        g.add_edge(x, x + 1)
    assert len(g.edge_set) == num


@pytest.mark.parametrize('num', [x for x in range(1, 20)])
def test_adding_duplicate_edges_to_a_graph_adds_unique_edges(num):
    """Test that adding duplicate edges to the graph unique edges."""
    from graph_1 import Graph
    g = Graph()
    for x in range(num):
        g.add_edge(x % 5, x % 5 + 1)
    assert len(g.edge_set) == 5 if num > 5 else num
