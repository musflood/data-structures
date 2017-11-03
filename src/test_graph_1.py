"""Tests for the graph_1 module."""

import pytest


def test_empty_constructor_constructs_empty_graph():
    """Test that a new graph is empty."""
    from graph_1 import Graph
    g = Graph()
    assert len(g.nodes) == 0
    assert len(g.edges) == 0


def test_nodes_of_empty_graph_is_empty(empty_graph_1):
    """Test that the list of nodes for an empty graph is empty."""
    assert empty_graph_1.nodes() == []


def test_edges_of_empty_graph_is_empty(empty_graph_1):
    """Test that the list of edges for an empty graph is empty."""
    assert empty_graph_1.edges() == []


@pytest.mark.parametrize('itr', [x for x in range(1, 20)])
def test_adding_unique_values_to_a_graph_adds_all_nodes(itr):
    """Test that adding unique values to the graph adds all of them."""
    from graph_1 import Graph
    g = Graph()
    for x in itr:
        g.add_node(x)
    assert len(g.nodes) == len(itr)
