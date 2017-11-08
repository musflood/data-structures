"""Implement a graph."""


class Graph(object):
    """Structure for values in a graph."""

    def __init__(self):
        """Create a graph with no values."""
        pass

    def nodes(self):
        """Get all nodes in the graph to display in list form."""
        pass

    def edges(self):
        """Get all edges in graph to display in list of tuples."""
        pass

    def add_node(self, val):
        """Add a node with a value to the graph."""
        pass

    def add_edge(self, val1, val2):
        """Add an edge with two values to the graph that does not exist."""
        pass

    def del_node(self, val):
        """Remove the node with the given value from the graph.

        Also removes all edges connected to the node.
        """
        pass

    def del_edge(self, val1, val2):
        """Remove the edge connecting node of val1 to node of val2."""
        pass

    def has_node(self, val):
        """Check if the given value is in the graph."""
        pass

    def neighbors(self, val):
        """List all nodes the node of the given value connects to."""
        pass

    def adjacent(self, val1, val2):
        """Check if there is an edge connecting the nodes with given values."""
        pass

    def breadth_first_traversal(self, start_val):
        """Get the full visited path of a breadth first traversal."""
        pass

    def depth_first_traversal(self, start_val):
        """Get the full visited path of a depth first traversal."""
        pass
