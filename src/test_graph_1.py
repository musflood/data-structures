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
    assert len(g.node) == 0


def test_del_node_with_edge_deletes_node_and_edge(full_graph_1):
    """Test that deleting a node with an edge deletes both node and edge."""
    g = full_graph_1
    g.del_node(4)
    g.del_node(3)
    assert 4 not in g.node_set
    assert 3 not in g.node_set
    assert (3, 5) not in g.edge_set
    assert (5, 3) not in g.edge_set
    assert (4, 2) not in g.edge_set


def test_del_edge_from_empty_graph_raises_error(empty_graph_1):
