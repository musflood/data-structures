"""Tests for the weight_graph module."""

import pytest


def test_empty_constructor_constructs_empty_weight_graph():
    """Test that a new graph is empty."""
    from weight_graph import Graph
    g = Graph()
    assert len(g.graph) == 0


def test_nodes_of_empty_weight_weight_graph_is_empty(empty_weight_graph):
    """Test that the list of nodes for an empty graph is empty."""
    assert empty_weight_graph.nodes() == []


def test_edges_of_empty_weight_graph_is_empty(empty_weight_graph):
    """Test that the list of edges for an empty graph is empty."""
    assert empty_weight_graph.edges() == []


@pytest.mark.parametrize('num', [x for x in range(1, 20)])
def test_nodes_of_filled_weight_graph_has_all_nodes(num):
    """Test that nodes lists all the nodes in a graph."""
    from weight_graph import Graph
    g = Graph()
    for x in range(num):
        g.add_node(x)
    assert len(g.nodes()) == num
    assert sorted(g.nodes()) == list(range(num))


@pytest.mark.parametrize('num', [x for x in range(1, 20)])
def test_edges_of_filled_weight_graph_has_all_edges(num):
    """Test that edges lists all the edges in a graph."""
    from weight_graph import Graph
    g = Graph()
    for x in range(num):
        g.add_edge(x, x + 1, x + 2)
    assert len(g.edges()) == num


@pytest.mark.parametrize('num', [x for x in range(1, 20)])
def test_adding_unique_values_to_a_weight_graph_adds_all_nodes(num):
    """Test that adding unique values to the graph adds all of them."""
    from weight_graph import Graph
    g = Graph()
    for x in range(num):
        g.add_node(x)
    assert len(g.nodes()) == num


@pytest.mark.parametrize('num', [x for x in range(1, 20)])
def test_dublicate_values_to_a_weight_graph_adds_some_nodes(num):
    """Test that adding duplicate values to the graph add only unique items."""
    from weight_graph import Graph
    g = Graph()
    for x in range(num):
        g.add_node(x % 5)
    assert len(g.nodes()) == 5 if num > 5 else num


@pytest.mark.parametrize('num', [x for x in range(1, 20)])
def test_adding_duplicate_edges_to_a_weight_graph_adds_unique_edges(num):
    """Test that adding duplicate edges to the graph unique edges."""
    from weight_graph import Graph
    g = Graph()
    for x in range(num):
        g.add_edge(x % 5, x % 5 + 1, x + 1)
    assert len(g.edges()) == 5 if num > 5 else num


def test_adding_edge_to_existing_nodes_only_adds_edge(empty_weight_graph):
    """Test that adding an edge for existing nodes only adds the edge."""
    g = empty_weight_graph
    g.add_node(1)
    g.add_node(9)
    g.add_edge(1, 9, 3)
    assert len(g.nodes()) == 2
    assert len(g.edges()) == 1


def test_adding_edges_between_existing_nodes_adds_both_edges(empty_weight_graph):
    """Test that adding an edges between existing nodes adds both edges."""
    g = empty_weight_graph
    g.add_node(1)
    g.add_node(9)
    g.add_edge(1, 9, 2)
    g.add_edge(9, 1, 4)
    assert len(g.nodes()) == 2
    assert len(g.edges()) == 2


def test_adding_edge_to_one_existing_nodes_adds_edge_and_node(empty_weight_graph):
    """Test that adding an edge for one node adds the edge and other node."""
    g = empty_weight_graph
    g.add_node(1)
    g.add_edge(1, 9, 3)
    assert len(g.nodes()) == 2
    assert 9 in g.nodes()
    assert len(g.edges()) == 1


def test_adding_edge_to_nonexisting_nodes_adds_edge_and_nodes(empty_weight_graph):
    """Test that adding an edge for existing nodes only adds the edge."""
    g = empty_weight_graph
    g.add_edge(1, 9, 4)
    assert len(g.nodes()) == 2
    assert 9 in g.nodes()
    assert 1 in g.nodes()
    assert len(g.edges()) == 1


def test_adding_edge_with_two_equal_values_raises_error(empty_weight_graph):
    """Test that adding an edge with two equal values raises a value error."""
    g = empty_weight_graph
    with pytest.raises(ValueError):
        g.add_edge(2, 2, 3)


@pytest.mark.parametrize('num', [x for x in range(1, 20)])
def test_adding_unique_edges_to_a_weight_graph_adds_all_edges(num):
    """Test that adding unique edges to the weight graph adds all edges."""
    from weight_graph import Graph
    g = Graph()
    for x in range(num):
        g.add_edge(x, x + 1, x + 2)
    assert len(g.edges()) == num
