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


def test_adding_edge_with_two_equal_values_raises_error(empty_graph_1):
    """Test that adding an edge with two equal values raises a value error."""
    g = empty_graph_1
    with pytest.raises(ValueError):
        g.add_edge(2, 2)


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
    assert len(g.nodes()) == 0


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
    """Test that deleting an edge from empty graph raises an error."""
    g = empty_graph_1
    with pytest.raises(ValueError):
        g.del_edge(1, 2)


def test_del_edge_from_graph_with_node_and_no_edge_raises_error(empty_graph_1):
    """Test deleting edge from graph with node but no edge raises key error."""
    g = empty_graph_1
    g.add_node(3)
    g.add_node(5)
    g.add_node(1)
    with pytest.raises(ValueError):
        g.del_edge(5, 1)


def test_del_edge_from_graph_removes_edge_leaves_node(full_graph_1):
    """Test del edge from graph removes edge but not node."""
    g = full_graph_1
    g.del_edge(4, 2)
    assert (4, 2) not in g.edges()
    assert 4 in g.nodes()
    assert 2 in g.nodes()


def test_has_node_returns_false_if_node_not_in_graph(empty_graph_1):
    """Test that has node returns false if node not in graph."""
    g = empty_graph_1
    x = g.has_node(4)
    assert x is False


@pytest.mark.parametrize('num', [x for x in range(1, 20)])
def test_has_node_returns_true_if_node_serched_is_in_graph(num):
    """Test that has node returns true if looking for node present in graph."""
    from graph_1 import Graph
    g = Graph()
    for x in range(num):
        g.add_node(x)
    for x in range(num):
        assert g.has_node(x)


def test_neighbors_raises_error_if_node_not_in_graph(empty_graph_1):
    """Test that looking for neighbor of a node with no edge raises error."""
    g = empty_graph_1
    g.add_node(3)
    g.add_node(4)
    g.add_node(5)
    g.add_edge(6, 4)
    with pytest.raises(ValueError):
        g.neighbors(8)


def test_neighbors_gets_list_of_all_values_the_val_connected_to(full_graph_1):
    """Test neighbor returns a list of all values connected to value given."""
    g = full_graph_1
    g.add_edge(2, 5)
    x = g.neighbors(2)
    assert x == [5]


def test_adjacent_raises_error_if_no_edge_with_value_pair(full_graph_1):
    """Test that adjacent raises error if values given are not in an edge."""
    g = full_graph_1
    with pytest.raises(ValueError):
        g.adjacent(21, 22)


@pytest.mark.parametrize('num', [x for x in range(1, 20)])
def test_adjacent_returns_true_if_specific_pair_of_values_given_exist(num):
    """Test adjacent is true if pair of values given exist in graph as edge."""
    from graph_1 import Graph
    g = Graph()
    for x in range(num):
        g.add_edge(x, x + 1)
    for x in range(num):
        assert g.adjacent(x, x + 1)


def test_b_traversal_from_node_not_in_graph_raises_error(full_graph_1):
    """Test that traversing from node not in graph raises ValueError."""
    with pytest.raises(ValueError):
        full_graph_1.breadth_first_traversal(0)


def test_b_traversal_from_neighborless_node_gets_one_node_list(full_graph_1):
    """Test that traversing from neightborless node gets one node list."""
    assert full_graph_1.breadth_first_traversal(21) == [21]


def test_b_traversal_from_one_neighbor_node_gets_two_node_list(full_graph_1):
    """Test that traversing from one neightbor node gets two node list."""
    assert full_graph_1.breadth_first_traversal(1) == [1, 2]


def test_b_traversal_from_one_neighbor_loop_gets_two_node_list(full_graph_1):
    """Test that traversing from one neightbor node loop gets two node list."""
    assert full_graph_1.breadth_first_traversal(3) == [3, 5]


def test_b_traversal_from_deep_node_gets_full_node_list(full_graph_tree):
    """Test that traversing from deep node gets all the nodes."""
    assert full_graph_tree.breadth_first_traversal(1) == [1, 2, 3, 5, 4, 6, 7]


def test_b_traversal_from_deep_node_with_loop_has_no_repeats(full_graph_tree):
    """Test that traversing from deep node with a loop does not repeat."""
    full_graph_tree.add_edge(4, 1)
    assert full_graph_tree.breadth_first_traversal(1) == [1, 2, 3, 5, 4, 6, 7]


def test_d_traversal_from_node_not_in_graph_raises_error(full_graph_1):
    """Test that trying to travers from empty graph raises key error."""
    with pytest.raises(ValueError):
        full_graph_1.depth_first_traversal(0)


def teest_d_traversal_from_neighborless_node_returns_node(full_graph_1):
    """Test depth traversing a node with no neighbors returns just the node."""
    assert full_graph_1.depth_first_traversal(21) == 21


def test_d_traversal_from_node_with_one_neighbor_gets_two_node_list(full_graph_1):
    """Test that depth traversing node with one neighbor gets a list of two."""
    assert full_graph_1.depth_first_traversal(7) == [7, 9]


def test_d_traversal_from_deep_node_gets_full_depth_node_list(full_graph_tree):
    """Test that depth traversal of deep graph gets full depth of nodes, no repeat."""
    assert full_graph_tree.depth_first_traversal(1) == [1, 2, 5, 4, 3, 6, 7]


def test_d_traversal_from_deep_node_with_loop_has_no_repeat(full_graph_tree):
    """Test that there are no duplicates in depth traversal of graph with loop."""
    full_graph_tree.add_edge(4, 1)
    assert full_graph_tree.depth_first_traversal(1) == [1, 2, 5, 4, 3, 6, 7]
