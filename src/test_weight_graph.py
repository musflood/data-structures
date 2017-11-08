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
