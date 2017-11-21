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


def test_del_node_from_empty_weight_graph_raises_error(empty_weight_graph):
    """Test that del_node from an empty graph raises ValueError."""
    g = empty_weight_graph
    with pytest.raises(ValueError):
        g.del_node(1)


def test_del_false_node_from_weight_graph_raises_value_error(empty_weight_graph):
    """Test that deleting node that does not exist from weight graph raises error."""
    g = empty_weight_graph
    g.add_node(1)
    g.add_node(2)
    with pytest.raises(ValueError):
        g.del_node(4)


def test_del_node_from_graph_deletes_node_from_graph(empty_weight_graph):
    """Test that del node from graph takes the node out of the graph."""
    g = empty_weight_graph
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)
    g.del_node(3)
    assert 3 not in g.nodes()
    assert 4 in g.nodes()


def test_del_nodes_from_weight_graph_result_empty_graph(empty_weight_graph):
    """Test that deleting nodes from weight graph results in empty graph."""
    g = empty_weight_graph
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)
    g.del_node(4)
    g.del_node(3)
    g.del_node(2)
    g.del_node(1)
    assert len(g.nodes()) == 0


def test_del_node_with_edge_deletes_node_and_edge(edge_weight_graph):
    """Test that deleting a node with an edge deletes both node and edge."""
    g = edge_weight_graph
    g.del_node(4)
    g.del_node(1)
    assert 4 not in g.nodes()
    assert 1 not in g.nodes()
    assert (3, 4, 2) not in g.edges()
    assert (1, 2, 1) not in g.edges()


def test_del_edge_from_empty_weight_graph_raises_error(empty_weight_graph):
    """Test that deleting an edge from empty graph raises an error."""
    g = empty_weight_graph
    with pytest.raises(ValueError):
        g.del_edge(1, 2)


def test_del_edge_from_weight_graph_with_node_and_no_edge_raises_error(empty_weight_graph):
    """Test deleting edge from graph with node but no edge raises key error."""
    g = empty_weight_graph
    g.add_node(3)
    g.add_node(5)
    g.add_node(1)
    with pytest.raises(ValueError):
        g.del_edge(5, 1)


def test_del_edge_from_weight_graph_removes_edge_leaves_node(edge_weight_graph):
    """Test del edge from weight graph removes edge but not node."""
    g = edge_weight_graph
    g.del_edge(1, 2)
    assert (1, 2, 1) not in g.edges()
    assert 1 in g.nodes()
    assert 2 in g.nodes()


def test_has_node_returns_false_if_node_not_in_weight_graph(empty_weight_graph):
    """Test that has node returns false if node not in weight graph."""
    g = empty_weight_graph
    x = g.has_node(4)
    assert x is False


@pytest.mark.parametrize('num', [x for x in range(1, 20)])
def test_has_node_returns_true_if_node_serched_is_in_weight_graph(num):
    """Test that has node returns true if looking for node present in weight graph."""
    from weight_graph import Graph
    g = Graph()
    for x in range(num):
        g.add_node(x)
    for x in range(num):
        assert g.has_node(x)


def test_neighbors_raises_error_if_node_not_in_weight_graph(empty_weight_graph):
    """Test that looking for neighbor of a node with no edge raises error."""
    g = empty_weight_graph
    g.add_node(3)
    g.add_node(4)
    g.add_node(5)
    g.add_edge(6, 4, 7)
    with pytest.raises(ValueError):
        g.neighbors(8)


def test_neighbors_gets_list_of_all_values_the_val_connected_to(node_weight_graph):
    """Test neighbor returns a list of all values connected to value given."""
    g = node_weight_graph
    g.add_edge(2, 5, 1)
    x = g.neighbors(2)
    assert x == [5]


def test_adjacent_raises_error_if_no_edge_with_value_pair(edge_weight_graph):
    """Test that adjacent raises error if values given are not in an edge."""
    g = edge_weight_graph
    with pytest.raises(ValueError):
        g.adjacent(9, 20)


@pytest.mark.parametrize('num', [x for x in range(1, 20)])
def test_adjacent_returns_true_if_specific_pair_of_values_given_exist(num):
    """Test adjacent is true if pair of values given exist in graph as edge."""
    from weight_graph import Graph
    g = Graph()
    for x in range(num):
        g.add_edge(x, x + 1, x % 3 + 1)
    for x in range(num):
        assert g.adjacent(x, x + 1)


@pytest.mark.parametrize('num', [x for x in range(1, 20)])
def test_adjacent_returns_false_if_specific_pair_of_values_has_no_edge(num):
    """Test adjacent is false if pair of values given doesn't exist in graph as edge."""
    from weight_graph import Graph
    g = Graph()
    for x in range(num):
        g.add_edge(x, x + 1, x % 3 + 1)
    for x in range(num - 1):
        assert not g.adjacent(x, x + 2)


def test_d_traversal_from_node_not_in_graph_raises_error(empty_weight_graph):
    """Test that trying to travers from empty graph raises key error."""
    with pytest.raises(ValueError):
        empty_weight_graph.depth_first_traversal(0)


def teest_d_traversal_from_neighborless_node_returns_node(edge_weight_graph):
    """Test depth traversing a node with no neighbors returns just the node."""
    assert edge_weight_graph.depth_first_traversal(2) == [2]


def test_d_traversal_from_node_with_one_neighbor_gets_two_node_list(edge_weight_graph):
    """Test that depth traversing node with one neighbor gets a list of two."""
    assert edge_weight_graph.depth_first_traversal(1) == [1, 2]


def test_d_traversal_from_deep_node_gets_full_depth_node_list(full_weight_graph_tree):
    """Test that depth traversal of deep weight graph gets full depth of nodes, no repeat."""
    assert full_weight_graph_tree.depth_first_traversal(1) == [1, 2, 4, 5, 3, 6, 7]


def test_d_traversal_from_deep_node_with_loop_has_no_repeat(full_weight_graph_tree):
    """Test that there are no duplicates in depth traversal of graph with loop."""
    full_weight_graph_tree.add_edge(4, 1, 6)
    assert full_weight_graph_tree.depth_first_traversal(1) == [1, 2, 4, 5, 3, 6, 7]


# breadth traversal tests


def test_b_traversal_from_node_not_in_weight_graph_raises_error(full_weight_graph_tree):
    """Test that traversing from node not in graph raises ValueError."""
    with pytest.raises(ValueError):
        full_weight_graph_tree.breadth_first_traversal(0)


def test_b_traversal_from_neighborless_node_gets_one_node_list(node_weight_graph):
    """Test that traversing from neightborless node gets one node list."""
    assert node_weight_graph.breadth_first_traversal(2) == [2]


def test_b_traversal_from_one_neighbor_node_gets_two_node_list(edge_weight_graph):
    """Test that traversing from one neightbor node gets two node list."""
    assert edge_weight_graph.breadth_first_traversal(1) == [1, 2]


def test_b_traversal_from_one_neighbor_loop_gets_two_node_list(empty_weight_graph):
    """Test that traversing from one neightbor node loop gets two node list."""
    g = empty_weight_graph
    g.add_edge(3, 5, 5)
    g.add_edge(5, 3, 4)
    assert g.breadth_first_traversal(3) == [3, 5]


def test_b_traversal_from_deep_node_gets_full_node_list(full_weight_graph_tree):
    """Test that traversing from deep node gets all the nodes."""
    assert full_weight_graph_tree.breadth_first_traversal(1) == [1, 2, 3, 4, 5, 6, 7]


def test_b_traversal_from_deep_node_with_loop_has_no_repeats(full_weight_graph_tree):
    """Test that traversing from deep node with a loop does not repeat."""
    full_weight_graph_tree.add_edge(4, 1, 4)
    assert full_weight_graph_tree.breadth_first_traversal(1) == [1, 2, 3, 4, 5, 6, 7]


# dijkstra tests
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


def test_dijkstra_with_empty_graph_raises_error(empty_weight_graph):
    """Test that ValueError raised if dijkstra used on empty graph."""
    with pytest.raises(ValueError):
        empty_weight_graph.dijkstra_min(4, 19)


def test_dijkstra_start_not_in_graph_raises_error(complex_weight_graph):
    """Test ValueError raised if dijkstra is used with start not in graph."""
    with pytest.raises(ValueError):
        complex_weight_graph.dijkstra_min(14, 2)


def test_dijkstra_end_not_in_graph_raises_error(complex_weight_graph):
    """Test ValueError raised if dijkstra is used with end not in graph."""
    with pytest.raises(ValueError):
        complex_weight_graph.dijkstra_min(4, 19)


def test_dijkstra_start_end_not_connected_raises_error(complex_weight_graph):
    """Test ValueError raised if dijkstra is used with end not cennected to start."""
    complex_weight_graph.add_node(14)
    with pytest.raises(ValueError):
        complex_weight_graph.dijkstra_min(4, 14)


def test_dijkstra_path_for_node_to_itself_is_node(complex_weight_graph):
    """Test dijkstra path from node to itself is the node."""
    path = complex_weight_graph.dijkstra_min(8, 8)
    assert len(path) == 1
    assert path[0] == 8


def test_dijkstra_path_for_node_to_adjacent_is_two(complex_weight_graph):
    """Test dijkstra path from node to adjacent is two nodes."""
    path = complex_weight_graph.dijkstra_min(8, 2)
    assert len(path) == 2
    assert path[0] == 8
    assert path[1] == 2


@pytest.mark.parametrize('graph, start, end, solution',
                         [(complex_weight_graph(), 0, 6, [0, 7, 6]),
                          (complex_weight_graph(), 7, 3, [7, 6, 5, 2, 3]),
                          (complex_weight_graph(), 1, 5, [1, 2, 5]),
                          (complex_weight_graph(), 4, 0, [4, 5, 6, 7, 0]),
                          (complex_weight_graph(), 5, 3, [5, 2, 3])])
def test_dijkstra_path_is_correct(graph, start, end, solution):
    """Test dijkstra path is correct shortest path."""
    assert graph.dijkstra_min(start, end) == solution
