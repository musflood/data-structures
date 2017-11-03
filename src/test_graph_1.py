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


def test_edges_of_empty_graph_is_empty(empty_graph_1):
    """Test that the list of edges for an empty graph is empty."""
    assert empty_graph_1.edges() == []


@pytest.mark.parametrize('num', [x for x in range(1, 20)])
def test_adding_unique_values_to_a_graph_adds_all_nodes(num):
    """Test that adding unique values to the graph adds all of them."""
    from graph_1 import Graph
    g = Graph()
    for x in range(num):
        g.add_node(x)
    assert len(g.node_set) == num


def test_del_node_from_empty_graph_raises_error(empty_graph_1):
    """Test that del_node from an empty graph raises ValueError."""
    g = empty_graph_1
    with pytest.raises(ValueError):
        g.del_node(1)


def test_del_false_node_from_graph_raises_value_error(empty_graph_1):
    """Test that deleting node that does not exist from graph raises error."""
    g = empty_graph_1
    g.add_node(1)
    g.add_node(2)
    with pytest.raises(ValueError):
        g.del_node(4)


def test_del_node_from_graph_deletes_node_from_graph(empty_graph_1):
    """Test that del node from graph takes the node out of the graph."""
    g = empty_graph_1
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)
    g.del_node(3)
    assert 3 not in g.node_set
    assert 4 in g.node_set


def test_del_all_nodes_from_graph_result_empty_graph(empty_graph_1):
    """Test that deleting all nodes from graph results in empty graph."""
    g = empty_graph_1
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)
    g.del_node(4)
    g.del_node(3)
    g.del_node(2)
    g.del_node(1)
    assert len(g.nodes) == 0


def test_del_node_with_edge_deletes_node_and_edge(full_graph_1):
    """Test that deleting a node with an edge deletes both node and edge."""
    g = full_graph_1
